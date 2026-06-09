---
title: "Private Lloyd Materials Inventory"
type: discovery
category: source-inventory
date: 2026-06-08
status: draft
tags:
  - progressive
  - lloyd
  - private-materials
  - source-inventory
  - secure-card-vault
related:
  - projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md
  - projects/gift-cards/docs/plans/2026-04-27-lloyd-fixture-request-email.md
  - projects/gift-cards/docs/plans/2026-03-31-discovery-synthesis.md
blockers:
  - Raw files are intentionally stored outside git under projects/gift-cards/_private/.
---

# Private Lloyd Materials Inventory

Raw Lloyd materials for Progressive Phase 1 technical verification should be stored locally at:

`projects/gift-cards/_private/lloyd-materials/2026-06-08/`

This folder is intentionally ignored by git because it may contain client scripts, card data, templates, generated files, and other sensitive operational materials.

## Drop Folder Structure

- `raw/scripts/` — Python, PowerShell, utility scripts, macros, or command files.
- `raw/templates/` — SVG, PDF, workbook, merchant, or card-generation templates.
- `raw/workbooks/` — Amazon/Loblaws/Shoppers/etc. source or sample workbooks.
- `raw/walmart/` — Walmart activation templates, PowerShell files, screenshots, notes, or reconciliation samples.
- `raw/systemone/` — SystemOne ZIP/log/export examples or API notes.
- `raw/outputs/` — known-good generated PDFs, ZIPs, logs, URL exports, or sample customer-ready files.
- `raw/other/` — anything that does not fit cleanly yet.
- `notes/` — local-only source inventory and review notes.

## Review Notes

Populate the private `notes/SOURCE-INVENTORY.md` after files are dropped. The inventory should record:

- File name and local path.
- Source/person who provided it.
- Date received.
- Whether it contains sensitive card data.
- What workflow or merchant it proves.
- Whether it is safe to use for agent/code review.

## Current Status

Created June 8, 2026 as a durable local drop zone after Doug's follow-up technical questions exposed gaps in the Phase 1 proposal evidence base.

Three files were recovered from the April 22, 2026 Asana/Google Drive trail and stored in the private folder:

- Lloyd's invoice-to-merchant Excel generator script.
- Lloyd's Amazon gift PDF ZIP generator script.
- Lloyd's Amazon workbook/template file.

Lloyd's email notes are also captured in the private source inventory because they explain the intended workflow: the first script reads an invoice and generates merchant-specific Excel files; the Amazon script takes the generated Amazon workbook after manual inventory fields have been filled and creates a ZIP of gift PDFs; Inkscape is required for the Amazon generator.

The recovered materials confirm that Phase 1 should account for merchant-specific fulfillment formats, not just one generic export format. They also confirm that Amazon still has a manual inventory-content step in the existing workflow.

Early source review also indicates that Doug's Walmart/Loblaws/Amazon sales breakdown should be treated as volume prioritization, not total merchant coverage. Lloyd's invoice generator script references a broader set of merchant-specific templates and handling rules. The private inventory contains the exact list and should be reviewed before committing to named Phase 1 merchant formats.

One dependency is still missing from the recovered attachment set: the Amazon ZIP generator imports a local `utilities.py` helper. Reproducing the Amazon workflow will require locating that helper plus the relevant Inkscape/SVG/PDF templates.

The attached Google Drive folder was checked on June 8, 2026 and only contained the two Python scripts plus the Amazon workbook/template. Missing support files will need to be located through another source.

A March 26, 2026 Slack post from Danny sharing Lloyd's pre-onsite notes adds important workflow context. Lloyd described the current tooling as Windows-based, with Python/Java scripts, PowerShell command-line steps, and Inkscape for PDF generation. He also described Walmart as an exception to the normal merchant order pattern: Progressive orders Walmart digital cards as part of fulfillment and uses a Fiserv-related activation program. Treat Walmart activation as a distinct source gap and technical-workflow decision, not as a generic customer-ready file export.

An April 24, 2026 internal Google Doc titled `Progressive: Lloyd's Scripts + Next Steps` independently confirmed the same missing support inputs. That prior review should be used as evidence that the source gap is not new: Redstamp identified the need for runnable fixtures, merchant templates, Walmart assets, and SystemOne requirements before final pricing and implementation assumptions are locked.
