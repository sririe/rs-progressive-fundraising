---
title: "Can't download Gmail attachments or Drive link-shares via available tooling"
type: solution
category: workflow-issue
date: 2026-06-16
status: open
tags:
  - tooling
  - gmail
  - gog
  - google-drive
  - email-attachments
---

# Email attachment / Drive link-share download gap

## Friction (observed 2026-06-16)

Doug sent the Walmart reconciliation as a **Gmail attachment** and Lloyd's software as a **Google Drive
link-share** (`redstamp.zip`). Neither could be pulled by the agent:

- **Gmail MCP connector** reads threads and message bodies but exposes **no attachment-download tool** — so
  the `.xlsx` could not be fetched programmatically.
- **`gog` CLI** is authed as spencer@redstamp.com with **`docs,drive` scopes only — no `gmail` scope** — so
  it can't touch Gmail attachments either.
- The **Drive link-share 404s** for both the Drive MCP and `gog`: the `drive.google.com/open?id=...` link
  carries no resourceKey and the file lives on a `progressivefundraising.ca` Workspace that restricts
  external sharing, so an outside `@redstamp.com` identity can't resolve it by ID. Spencer had to fall back
  to the browser / request access manually.

Net effect: any task that needs a file out of email/Drive stalls and hands back to the operator.

## Fix candidates (reusable)

1. **Add the `gmail` scope to `gog`** (re-run gog's auth/consent with Gmail readonly + attachment access).
   Then `gog` can list and download attachments directly — the durable fix for the recurring case.
2. **For cross-domain Drive shares:** ask the sender to **attach the file to email** instead of sharing via
   Drive (sidesteps the Workspace external-sharing restriction), or click **"Request access"** on the link
   and wait for grant. An "anyone with link" link from a restricted Workspace silently fails for outside
   accounts.
3. When a file must be pulled and neither path works, say so early and let the operator download it into the
   git-ignored `_private/` drop folder for inventory — don't burn turns retrying 404s.

## Status

Open. Recorded at 2026-06-16 wrap-up. No repo tracker — surfaced in `docs/status/current.md`
Runtime & environment section. Fix #1 (gog gmail scope) is an operator config action.
