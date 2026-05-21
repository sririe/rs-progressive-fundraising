#!/usr/bin/env python3
"""
Import tasks from a CSV file into an Asana project.

Expected CSV headers:
  - Task name
  - Description
  - Section
  - Assignee
  - Dependencies

Usage:
  ASANA_PAT=... python3 projects/gift-cards/scripts/import_asana_tasks.py \
    --project-gid 123456789 \
    projects/gift-cards/docs/plans/inbox/2026-03-19-progressive-asana-import.csv \
    --dry-run

Optional assignee map JSON:
  {
    "Danny": "120000000000001",
    "Spencer": "120000000000002"
  }

Notes:
  - If a CSV assignee value cannot be mapped to a single Asana user GID, the task is
    left unassigned and the suggested owner is appended to the task notes.
  - Existing tasks with the same name can be skipped to avoid duplicate imports.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass


API_BASE = "https://app.asana.com/api/1.0"


class AsanaError(RuntimeError):
    pass


@dataclass
class ImportResult:
    created: int = 0
    skipped_existing: int = 0
    dry_run: int = 0


class AsanaClient:
    def __init__(self, token: str):
        self.token = token

    def request(self, method: str, path: str, data: dict | None = None, absolute_url: str | None = None) -> dict:
        url = absolute_url or f"{API_BASE}{path}"
        body = None
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}",
        }

        if data is not None:
            body = json.dumps({"data": data}).encode("utf-8")
            headers["Content-Type"] = "application/json"

        request = urllib.request.Request(url=url, data=body, headers=headers, method=method)

        try:
            with urllib.request.urlopen(request) as response:
                payload = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")
            raise AsanaError(f"{method} {url} failed with {exc.code}: {error_body}") from exc
        except urllib.error.URLError as exc:
            raise AsanaError(f"{method} {url} failed: {exc.reason}") from exc

        return json.loads(payload)

    def paginate(self, path: str, query: dict[str, str] | None = None) -> list[dict]:
        query_string = f"?{urllib.parse.urlencode(query)}" if query else ""
        url = f"{API_BASE}{path}{query_string}"
        items: list[dict] = []

        while url:
            payload = self.request("GET", path="", absolute_url=url)
            items.extend(payload.get("data", []))
            next_page = payload.get("next_page") or {}
            url = next_page.get("uri")

        return items

    def get_project_sections(self, project_gid: str) -> list[dict]:
        return self.paginate(f"/projects/{project_gid}/sections")

    def create_project_section(self, project_gid: str, name: str) -> dict:
        return self.request("POST", f"/projects/{project_gid}/sections", {"name": name})["data"]

    def get_project_tasks(self, project_gid: str) -> list[dict]:
        return self.paginate(
            f"/projects/{project_gid}/tasks",
            {"opt_fields": "name"},
        )

    def create_task(self, payload: dict) -> dict:
        return self.request("POST", "/tasks", payload)["data"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import a CSV task list into an Asana project.")
    parser.add_argument("csv_path", help="Path to the CSV file to import.")
    parser.add_argument("--project-gid", required=True, help="Target Asana project GID.")
    parser.add_argument(
        "--assignee-map",
        help="Path to a JSON file mapping CSV assignee labels to Asana user GIDs.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned import without creating or updating anything in Asana.",
    )
    parser.add_argument(
        "--no-create-sections",
        action="store_true",
        help="Do not create missing sections automatically.",
    )
    parser.add_argument(
        "--allow-duplicates",
        action="store_true",
        help="Create tasks even if a task with the same name already exists in the project.",
    )
    return parser.parse_args()


def load_assignee_map(path: str | None) -> dict[str, str]:
    if not path:
        return {}

    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise AsanaError("Assignee map must be a JSON object of label -> user_gid.")

    return {str(key).strip(): str(value).strip() for key, value in data.items()}


def clean(value: str | None) -> str:
    return (value or "").strip()


def resolve_assignee_gid(raw_assignee: str, assignee_map: dict[str, str]) -> str | None:
    if not raw_assignee:
        return None

    if raw_assignee in assignee_map:
        return assignee_map[raw_assignee]

    if "/" in raw_assignee or "," in raw_assignee:
        return None

    return assignee_map.get(raw_assignee)


def build_task_payload(
    row: dict[str, str],
    project_gid: str,
    section_gid: str | None,
    assignee_gid: str | None,
) -> dict:
    task_name = clean(row.get("Task name"))
    description = clean(row.get("Description"))
    assignee_hint = clean(row.get("Assignee"))
    dependencies = clean(row.get("Dependencies"))

    notes_parts = []
    if description:
        notes_parts.append(description)
    if assignee_hint and not assignee_gid:
        notes_parts.append(f"Suggested owner: {assignee_hint}")
    if dependencies:
        notes_parts.append(f"Dependencies: {dependencies}")

    memberships = [{"project": project_gid}]
    if section_gid:
        memberships[0]["section"] = section_gid

    payload = {
        "name": task_name,
        "notes": "\n\n".join(notes_parts),
        "memberships": memberships,
    }

    if assignee_gid:
        payload["assignee"] = assignee_gid

    return payload


def ensure_required_headers(fieldnames: list[str] | None) -> None:
    required = {"Task name", "Description", "Section", "Assignee", "Dependencies"}
    actual = set(fieldnames or [])
    missing = sorted(required - actual)
    if missing:
        raise AsanaError(f"CSV is missing required headers: {', '.join(missing)}")


def main() -> int:
    args = parse_args()
    token = os.environ.get("ASANA_PAT")

    if not token:
        raise AsanaError("ASANA_PAT environment variable is required.")

    assignee_map = load_assignee_map(args.assignee_map)
    client = AsanaClient(token)
    results = ImportResult()

    with open(args.csv_path, "r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        ensure_required_headers(reader.fieldnames)
        rows = list(reader)

    sections_by_name = {
        clean(section.get("name")): str(section.get("gid"))
        for section in client.get_project_sections(args.project_gid)
        if clean(section.get("name"))
    }

    existing_task_names = set()
    if not args.allow_duplicates:
        existing_task_names = {
            clean(task.get("name"))
            for task in client.get_project_tasks(args.project_gid)
            if clean(task.get("name"))
        }

    for row in rows:
        task_name = clean(row.get("Task name"))
        section_name = clean(row.get("Section"))
        assignee_label = clean(row.get("Assignee"))

        if not task_name:
            print("Skipping blank task row.", file=sys.stderr)
            continue

        if not args.allow_duplicates and task_name in existing_task_names:
            results.skipped_existing += 1
            print(f"Skipping existing task: {task_name}")
            continue

        section_gid = None
        if section_name:
            section_gid = sections_by_name.get(section_name)
            if section_gid is None and not args.no_create_sections:
                if args.dry_run:
                    print(f"[dry-run] Would create missing section: {section_name}")
                    section_gid = f"dry-run-section:{section_name}"
                else:
                    created_section = client.create_project_section(args.project_gid, section_name)
                    section_gid = str(created_section["gid"])
                    sections_by_name[section_name] = section_gid
                    print(f"Created section: {section_name} ({section_gid})")

        assignee_gid = resolve_assignee_gid(assignee_label, assignee_map)
        payload = build_task_payload(
            row=row,
            project_gid=args.project_gid,
            section_gid=None if section_gid and section_gid.startswith("dry-run-section:") else section_gid,
            assignee_gid=assignee_gid,
        )

        if args.dry_run:
            results.dry_run += 1
            print(f"[dry-run] Would create task: {task_name}")
            print(json.dumps(payload, indent=2))
            continue

        created_task = client.create_task(payload)
        existing_task_names.add(task_name)
        results.created += 1
        print(f"Created task: {task_name} ({created_task['gid']})")

    print(
        "\nImport complete:"
        f" created={results.created}"
        f" skipped_existing={results.skipped_existing}"
        f" dry_run={results.dry_run}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AsanaError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
