#!/usr/bin/env python3
"""Generate a Google Sheets-friendly XLSX for Progressive discovery prework."""

from __future__ import annotations

import csv
import html
import re
import urllib.parse
import urllib.request
from pathlib import Path

import xlsxwriter


ROOT = Path("/Users/spencer/projects-work/rs-progressive-fundraising/projects/gift-cards")
OUTPUT_XLSX = ROOT / "docs/plans/inbox/2026-03-19-digital-vendor-and-workflow-prework-sheet.xlsx"
OUTPUT_CSV = ROOT / "docs/plans/inbox/2026-03-19-digital-vendor-and-workflow-prework-sheet.csv"
STOREFRONT_URL = "https://www.progiftcards.ca/our-gift-cards/"


VENDOR_NOTES = {
    "Amazon": {
        "workflow_pattern": "Generate from data",
        "confidence": "Known",
        "upstream_source": "Progressive to confirm; direct relationship or distributor",
        "inventory_format": "Likely spreadsheet/file of card numbers and PINs",
        "stored_where": "To confirm during session",
        "tools_used": "Lloyd script or generation workflow",
        "activation_needed": "Unknown",
        "output_type": "Historically card-like PDF or generated deliverable; URL future preferred",
        "walkthrough_priority": "High",
        "owner_today": "Lloyd; validate Mario coverage",
        "mario_coverage": "Partial / needs validation",
        "risk_level": "High",
        "sample_artifacts": "Input file, generated output, any script or template, delivery example",
        "discovery_questions": "What exact input arrives? Is Amazon integration already underway? Is display or time-limit handling a factor?",
    },
    "Best Buy": {
        "workflow_pattern": "Pass-through / direct delivery",
        "confidence": "Known",
        "upstream_source": "Progressive to confirm",
        "inventory_format": "Likely direct link or vendor-provided digital artifact",
        "stored_where": "To confirm during session",
        "tools_used": "Minimal manual handling expected",
        "activation_needed": "Unknown",
        "output_type": "Forwarded URL or vendor artifact",
        "walkthrough_priority": "Medium",
        "owner_today": "Mario / Lloyd to confirm",
        "mario_coverage": "Unknown",
        "risk_level": "Low",
        "sample_artifacts": "Representative vendor email or link format",
        "discovery_questions": "Is this a true pass-through flow or is there any manual packaging step?",
    },
    "Chapters – Indigo – Coles": {
        "workflow_pattern": "Generate from data",
        "confidence": "Known",
        "upstream_source": "Progressive to confirm",
        "inventory_format": "Likely spreadsheet/file of card numbers and PINs",
        "stored_where": "To confirm during session",
        "tools_used": "Lloyd script or generation workflow",
        "activation_needed": "Unknown",
        "output_type": "Generated deliverable",
        "walkthrough_priority": "High",
        "owner_today": "Lloyd; validate Mario coverage",
        "mario_coverage": "Partial / needs validation",
        "risk_level": "High",
        "sample_artifacts": "Input file, script step, delivered output",
        "discovery_questions": "What differs here from Amazon and Walmart? Is the client deliverable still PDF-like?",
    },
    "Loblaws – Superstore, PC, No Frills, Extra Foods, Provigo": {
        "workflow_pattern": "Generate from data",
        "confidence": "Inferred",
        "upstream_source": "Progressive to confirm",
        "inventory_format": "Likely spreadsheet/file of card numbers and PINs",
        "stored_where": "To confirm during session",
        "tools_used": "Lloyd generation script",
        "activation_needed": "Unknown",
        "output_type": "Generated PDFs or similar deliverables",
        "walkthrough_priority": "High",
        "owner_today": "Lloyd; validate Mario coverage",
        "mario_coverage": "Partial / needs validation",
        "risk_level": "High",
        "sample_artifacts": "Input spreadsheet, generated batch output, error/verification process",
        "discovery_questions": "Is this the 20-30 seconds per card flow? What batching, verification, and failure recovery exist today?",
    },
    "Starbucks": {
        "workflow_pattern": "Pass-through / direct delivery",
        "confidence": "Known",
        "upstream_source": "Progressive to confirm",
        "inventory_format": "Likely direct link or vendor-provided artifact",
        "stored_where": "To confirm during session",
        "tools_used": "Minimal handling expected",
        "activation_needed": "Unknown",
        "output_type": "Forwarded URL or vendor artifact",
        "walkthrough_priority": "Medium",
        "owner_today": "Mario / Lloyd to confirm",
        "mario_coverage": "Unknown",
        "risk_level": "Low",
        "sample_artifacts": "Representative delivery example",
        "discovery_questions": "Is there any transformation layer at all, or just receipt and forwarding?",
    },
    "Tim Hortons": {
        "workflow_pattern": "Integrated API / portal-assisted",
        "confidence": "Known",
        "upstream_source": "Cash Star / Tim Hortons relationship to confirm",
        "inventory_format": "Potential direct integration or portal retrieval",
        "stored_where": "To confirm during session",
        "tools_used": "Integration / portal flow",
        "activation_needed": "Unknown",
        "output_type": "Likely URL or digital card artifact",
        "walkthrough_priority": "High",
        "owner_today": "Lloyd; validate Mario coverage",
        "mario_coverage": "Unknown",
        "risk_level": "Medium",
        "sample_artifacts": "Portal screenshots, exported files, delivery example",
        "discovery_questions": "What is already integrated here? Is this the cleanest future-state pattern to model elsewhere?",
    },
    "Walmart": {
        "workflow_pattern": "Generate from data",
        "confidence": "Known",
        "upstream_source": "Progressive to confirm; direct relationship likely",
        "inventory_format": "Likely spreadsheet/file of card numbers and PINs",
        "stored_where": "To confirm during session",
        "tools_used": "Lloyd script or generation workflow",
        "activation_needed": "Unknown",
        "output_type": "Generated deliverable; URL future preferred",
        "walkthrough_priority": "High",
        "owner_today": "Lloyd; validate Mario coverage",
        "mario_coverage": "Partial / needs validation",
        "risk_level": "High",
        "sample_artifacts": "Input file, generated output, delivery example, any activation step",
        "discovery_questions": "What is manual today versus already integrated? Are card numbers stored before activation or before fulfillment?",
    },
}


CHECKLIST_ROWS = [
    (
        "Workflow framing",
        "Confirm whether this vendor is a representative walkthrough candidate for the live session.",
        "All vendors",
    ),
    (
        "Acquisition",
        "Where does Progressive actually source these cards from: direct vendor, distributor, reseller, or integration?",
        "Per vendor",
    ),
    (
        "Inventory intake",
        "What exact input arrives: spreadsheet, portal export, email, URL list, PDF, API response, or something else?",
        "Per vendor",
    ),
    (
        "Storage",
        "Where are unsold or unfulfilled card records stored, and who can access them?",
        "Per vendor",
    ),
    (
        "Generation",
        "Is there a Lloyd-built script, macro, template, or manual transformation step before customer delivery?",
        "Per vendor",
    ),
    (
        "Verification",
        "How is batch completeness checked? Is there any validation that all cards generated successfully?",
        "Per vendor",
    ),
    (
        "Activation",
        "Is activation part of this digital flow, and if so when and where does it happen?",
        "Per vendor",
    ),
    (
        "Delivery",
        "What does the customer actually receive today: URL, PDF, image, spreadsheet row, or email copy?",
        "Per vendor",
    ),
    (
        "Security",
        "Where is the highest-risk moment for raw card data, and what protections are in place?",
        "Per vendor",
    ),
    (
        "Operator transfer",
        "Can Mario run this independently today, or where does Lloyd knowledge still matter?",
        "Per vendor",
    ),
    (
        "Artifacts",
        "Capture a representative input, output, and any script or portal screenshots if allowed.",
        "Per vendor",
    ),
    (
        "Adjacent ops",
        "Note any stickering, invoicing, or fulfillment-adjacent considerations without letting them take over the session.",
        "Only if it surfaces",
    ),
]


README_ROWS = [
    ("Purpose", "Seed the discovery prework with the current digital storefront, known workflow hypotheses, and the questions Red Stamp needs Progressive to answer."),
    ("Best use", "Import this workbook into Google Sheets, then use the Vendor Map tab live during prework and during the on-site walkthrough."),
    ("Important distinction", "Customer-facing digital vendors are not necessarily the same as Progressive's upstream sourcing relationships. Capture both."),
    ("Seed data source", "Digital storefront pulled from https://www.progiftcards.ca/our-gift-cards/ on 2026-03-19."),
    ("Suggested representative walkthroughs", "Amazon, Walmart, Loblaws, Tim Hortons, and one lower-complexity pass-through vendor such as Starbucks or Best Buy."),
    ("What to request ahead of time", "Representative input files, generated outputs, vendor emails/URLs, script screenshots, storage examples, and any current runbooks."),
]


def fetch_digital_vendors() -> list[dict[str, str]]:
    text = urllib.request.urlopen(STOREFRONT_URL).read().decode("utf-8", errors="ignore")
    pattern = re.compile(
        r'href="([^"]*gct=Digital\+E-Cards[^"]*)".*?<p class="merchant-name">(.*?)</p>',
        re.S,
    )

    vendors: list[dict[str, str]] = []
    seen: set[str] = set()

    for href, name_html in pattern.findall(text):
        name = html.unescape(re.sub(r"<[^>]+>", "", name_html)).strip()
        if name in seen:
            continue
        seen.add(name)
        vendors.append(
            {
                "name": name,
                "storefront_url": urllib.parse.urljoin(STOREFRONT_URL, html.unescape(href)),
            }
        )

    return vendors


def vendor_row(vendor: dict[str, str]) -> list[str]:
    defaults = {
        "workflow_pattern": "Needs validation",
        "confidence": "Unknown",
        "upstream_source": "To be confirmed with Progressive",
        "inventory_format": "To be confirmed with Progressive",
        "stored_where": "To be confirmed with Progressive",
        "tools_used": "To be confirmed with Progressive",
        "activation_needed": "Unknown",
        "output_type": "To be confirmed with Progressive",
        "walkthrough_priority": "Medium",
        "owner_today": "Lloyd / Mario to confirm",
        "mario_coverage": "Unknown",
        "risk_level": "Medium",
        "sample_artifacts": "Representative input and output needed",
        "discovery_questions": "What does this flow actually look like end to end today?",
    }
    defaults.update(VENDOR_NOTES.get(vendor["name"], {}))

    return [
        vendor["name"],
        "Yes",
        vendor["storefront_url"],
        defaults["workflow_pattern"],
        defaults["confidence"],
        defaults["upstream_source"],
        defaults["inventory_format"],
        defaults["stored_where"],
        defaults["tools_used"],
        defaults["activation_needed"],
        defaults["output_type"],
        defaults["walkthrough_priority"],
        defaults["owner_today"],
        defaults["mario_coverage"],
        defaults["risk_level"],
        defaults["sample_artifacts"],
        defaults["discovery_questions"],
    ]


def write_readme_sheet(workbook: xlsxwriter.Workbook) -> None:
    sheet = workbook.add_worksheet("Read Me")
    title = workbook.add_format({"bold": True, "font_size": 16})
    heading = workbook.add_format({"bold": True, "bg_color": "#D9EAF7", "border": 1})
    text = workbook.add_format({"text_wrap": True, "valign": "top", "border": 1})

    sheet.write("A1", "Progressive Digital Vendor and Workflow Prework", title)
    sheet.write("A3", "Topic", heading)
    sheet.write("B3", "Details", heading)

    row = 3
    for label, value in README_ROWS:
        sheet.write(row, 0, label, text)
        sheet.write(row, 1, value, text)
        row += 1

    sheet.set_column("A:A", 28)
    sheet.set_column("B:B", 95)


def write_vendor_map_sheet(workbook: xlsxwriter.Workbook, vendors: list[dict[str, str]]) -> list[list[str]]:
    headers = [
        "Customer-Facing Digital Vendor",
        "On Storefront",
        "Storefront Order URL",
        "Workflow Pattern",
        "Confidence",
        "Upstream Source / Distributor",
        "Inventory / Input Format",
        "Stored Where Today",
        "Tool / Script / Portal Used",
        "Activation Needed?",
        "Output Type To Client",
        "Walkthrough Priority",
        "Owner Today",
        "Mario Coverage",
        "Risk Level",
        "Sample Artifacts Needed",
        "Key Discovery Questions",
    ]
    rows = [vendor_row(vendor) for vendor in vendors]

    sheet = workbook.add_worksheet("Vendor Map")
    header = workbook.add_format(
        {
            "bold": True,
            "bg_color": "#2F5D7E",
            "font_color": "white",
            "border": 1,
            "text_wrap": True,
            "valign": "top",
        }
    )
    cell = workbook.add_format({"border": 1, "text_wrap": True, "valign": "top"})
    url = workbook.add_format({"border": 1, "text_wrap": True, "valign": "top", "font_color": "blue", "underline": 1})

    for col, value in enumerate(headers):
        sheet.write(0, col, value, header)

    for row_idx, row_values in enumerate(rows, start=1):
        for col_idx, value in enumerate(row_values):
            if col_idx == 2:
                sheet.write_url(row_idx, col_idx, value, url, string="Order link")
            else:
                sheet.write(row_idx, col_idx, value, cell)

    sheet.freeze_panes(1, 0)
    sheet.autofilter(0, 0, len(rows), len(headers) - 1)
    sheet.set_column("A:A", 34)
    sheet.set_column("B:B", 12)
    sheet.set_column("C:C", 16)
    sheet.set_column("D:D", 24)
    sheet.set_column("E:E", 12)
    sheet.set_column("F:F", 34)
    sheet.set_column("G:G", 28)
    sheet.set_column("H:H", 24)
    sheet.set_column("I:I", 28)
    sheet.set_column("J:J", 18)
    sheet.set_column("K:K", 26)
    sheet.set_column("L:L", 18)
    sheet.set_column("M:M", 20)
    sheet.set_column("N:N", 18)
    sheet.set_column("O:O", 14)
    sheet.set_column("P:P", 30)
    sheet.set_column("Q:Q", 48)

    end_row = len(rows)
    validations = {
        "B": ["Yes", "No"],
        "D": ["Pass-through / direct delivery", "Generate from data", "Integrated API / portal-assisted", "Needs validation"],
        "E": ["Known", "Inferred", "Unknown"],
        "J": ["Yes", "No", "Unknown"],
        "L": ["High", "Medium", "Low"],
        "N": ["Independent", "Partial / needs validation", "Unknown"],
        "O": ["High", "Medium", "Low"],
    }
    for column, options in validations.items():
        sheet.data_validation(
            f"{column}2:{column}{end_row + 1}",
            {"validate": "list", "source": options},
        )

    return [headers] + rows


def write_checklist_sheet(workbook: xlsxwriter.Workbook) -> None:
    sheet = workbook.add_worksheet("Session Checklist")
    header = workbook.add_format(
        {
            "bold": True,
            "bg_color": "#4A7C59",
            "font_color": "white",
            "border": 1,
            "text_wrap": True,
        }
    )
    cell = workbook.add_format({"border": 1, "text_wrap": True, "valign": "top"})

    headers = ["Area", "Prompt / Question", "Applies To", "Captured?", "Notes"]
    for col, value in enumerate(headers):
        sheet.write(0, col, value, header)

    for row_idx, (area, prompt, applies_to) in enumerate(CHECKLIST_ROWS, start=1):
        sheet.write(row_idx, 0, area, cell)
        sheet.write(row_idx, 1, prompt, cell)
        sheet.write(row_idx, 2, applies_to, cell)
        sheet.write(row_idx, 3, "", cell)
        sheet.write(row_idx, 4, "", cell)

    sheet.freeze_panes(1, 0)
    sheet.autofilter(0, 0, len(CHECKLIST_ROWS), len(headers) - 1)
    sheet.set_column("A:A", 20)
    sheet.set_column("B:B", 74)
    sheet.set_column("C:C", 20)
    sheet.set_column("D:D", 12)
    sheet.set_column("E:E", 44)
    sheet.data_validation(
        f"D2:D{len(CHECKLIST_ROWS) + 1}",
        {"validate": "list", "source": ["", "Yes", "No", "Partial"]},
    )


def write_storefront_sheet(workbook: xlsxwriter.Workbook, vendors: list[dict[str, str]]) -> None:
    sheet = workbook.add_worksheet("Storefront List")
    header = workbook.add_format({"bold": True, "bg_color": "#EDEDED", "border": 1})
    cell = workbook.add_format({"border": 1, "text_wrap": True, "valign": "top"})
    url = workbook.add_format({"border": 1, "font_color": "blue", "underline": 1})

    headers = ["Vendor", "Storefront Order URL", "Source"]
    for col, value in enumerate(headers):
        sheet.write(0, col, value, header)

    for row_idx, vendor in enumerate(vendors, start=1):
        sheet.write(row_idx, 0, vendor["name"], cell)
        sheet.write_url(row_idx, 1, vendor["storefront_url"], url, string="Order link")
        sheet.write(row_idx, 2, STOREFRONT_URL, cell)

    sheet.freeze_panes(1, 0)
    sheet.autofilter(0, 0, len(vendors), len(headers) - 1)
    sheet.set_column("A:A", 34)
    sheet.set_column("B:B", 18)
    sheet.set_column("C:C", 42)


def write_csv(rows: list[list[str]]) -> None:
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def main() -> None:
    vendors = fetch_digital_vendors()
    OUTPUT_XLSX.parent.mkdir(parents=True, exist_ok=True)
    workbook = xlsxwriter.Workbook(str(OUTPUT_XLSX))
    try:
        write_readme_sheet(workbook)
        vendor_rows = write_vendor_map_sheet(workbook, vendors)
        write_checklist_sheet(workbook)
        write_storefront_sheet(workbook, vendors)
    finally:
        workbook.close()

    write_csv(vendor_rows)
    print(f"Wrote {OUTPUT_XLSX}")
    print(f"Wrote {OUTPUT_CSV}")
    print(f"Seeded {len(vendors)} digital storefront vendors")


if __name__ == "__main__":
    main()
