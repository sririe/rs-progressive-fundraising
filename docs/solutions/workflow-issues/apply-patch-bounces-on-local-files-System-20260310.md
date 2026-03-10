---
module: System
date: 2026-03-10
problem_type: workflow_issue
component: editing-tooling
symptoms:
  - "apply_patch Add File hunks failed repeatedly with no useful error output"
  - "apply_patch Update File hunks also failed on a newly created file containing placeholder content"
  - "Manual retries on simple hunks still failed, slowing otherwise straightforward documentation work"
  - "Work had to pause while testing whether the failure was path-related, file-state-related, or tool-state-related"
root_cause: tool_instability
resolution_type: workflow_update
severity: medium
tags: [apply_patch, editing, workflow, fallback, documentation, codex]
---

# Troubleshooting: `apply_patch` Bounced During Simple Documentation Edits

## Problem

While creating the Progressive internal strategy brief, the normal `apply_patch` workflow failed repeatedly on very simple file operations. `Add File` hunks failed, `Update File` hunks failed after an empty file was created, and even a minimal test patch did not apply.

The issue was not the content itself. The same content could be written successfully with shell-based file writes. The failure mode was the patch tool becoming unreliable for that session or environment, which turned a short documentation task into a slower debugging loop.

## Environment

- Module: System (local documentation workflow)
- Affected component: `apply_patch` editing tool in Codex desktop session
- Workspace: `D:\projects-work\rs-progressive-fundraising`
- Date resolved: March 10, 2026

## Symptoms

- `apply_patch` failed on `*** Add File` for a new markdown document.
- `apply_patch` also failed on `*** Update File` for the same file after it had been created through the shell.
- Failures did not return useful diagnostics, making it hard to tell whether the issue was grammar, file state, or tool condition.
- Multiple retries added friction before the work was completed with `Set-Content`.

## What Didn't Work

**Retrying the same `Add File` hunk.** The patch continued to fail even with a tiny payload.

**Switching to a placeholder file and then using `Update File`.** The patch still failed, so the problem was not limited to new-file creation.

**Testing with a trivial file like `x.txt`.** That also failed, which confirmed this was a broader tool issue, not a path-specific markdown problem.

## Solution

Use a shell fallback quickly once this pattern appears:

1. Create the target file with `New-Item` if needed.
2. Write the content with `Set-Content` using a PowerShell here-string.
3. Verify with `Get-Content -Raw`.
4. Continue with normal git review and commit flow.

That fallback was what ultimately unblocked the work and produced:

- `docs/plans/2026-03-10-internal-strategy-brief.md`
- `docs/solutions/documentation-gaps/strategy-recommendation-not-collapsed-System-20260310.md`

## Why This Worked

The problem was with the patch mechanism, not with filesystem permissions inside the workspace and not with the markdown content. Direct file writes through PowerShell bypassed the unstable editing path while keeping the work local, reviewable, and easy to verify.

## Prevention

1. **Do one tiny patch test after the second unexplained patch failure.**
   If a one-line `Add File` or `Update File` hunk also fails, stop assuming the next retry will succeed.

2. **Switch to shell-based file writes sooner for documentation-only work.**
   When the task is creating or replacing a markdown document and `apply_patch` is unstable, use `Set-Content` rather than spending more time debugging the patch tool.

3. **Verify immediately after fallback.**
   Always run `Get-Content -Raw` after shell writes so the fallback remains transparent and easy to audit.

4. **Note the failure mode in session docs.**
   If `apply_patch` starts failing without actionable diagnostics, record it as a workflow issue so future runs can recognize the pattern quickly.

## Related Issues

- [session-tooling-and-repo-setup.md](../session-tooling-and-repo-setup.md) — General repo and tooling setup context.
- [proof-not-discoverable-across-projects-System-20260302.md](../workflow-issues/proof-not-discoverable-across-projects-System-20260302.md) — Another tooling/workflow issue captured in this repo.
