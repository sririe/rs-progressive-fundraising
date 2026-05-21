---
title: "Lloyd Script Review — Findings and Next Steps"
type: plan
category: technical-assessment
date: 2026-04-23
status: complete
tags:
  - progressive
  - lloyd
  - script-review
  - digital-fulfillment
  - card-generation
  - amazon
  - invoice-parsing
  - next-steps
key_insights:
  - The scripts are operational glue, not a deeply complex generation engine: PDF text parsing, vendor-specific Excel template creation, SVG field replacement, Inkscape PDF rendering, and ZIP packaging.
  - The highest technical risk is brittleness around invoice parsing, local folder structure, hidden dependencies, and undocumented templates/fixtures.
  - The provided Amazon workbook confirms the data contract: SEQUENCE, CLAIM CODE, AMOUNT, SERIAL NUMBER, CUSTOMER, MESSAGE, Invoice #, Date.
  - The supplied scripts are not enough to reproduce the workflow; Redstamp still needs utilities.py, SVG templates, vendor Excel templates, sample invoices, expected output folders, and representative inventory files.
key_decisions:
  - Treat Lloyd's scripts as behavioral reference material, not as code to wrap directly in a production system.
  - Recommend a short technical follow-up to collect missing fixtures and run the scripts end-to-end before final build scoping.
related:
  - projects/gift-cards/docs/plans/2026-03-31-discovery-synthesis.md
  - projects/gift-cards/docs/discovery/2026-03-27-lloyd-handoff-session1-notes.md
  - projects/gift-cards/docs/discovery/2026-03-27-mario-handoff-session2-notes.md
  - projects/gift-cards/docs/plans/2026-03-11-internal-solution-comparison.md
---

# Lloyd Script Review — Findings and Next Steps

## Source Material Reviewed

Lloyd provided three files on April 22, 2026, and local copies were reviewed from Spencer's Downloads folder on April 23, 2026:

- `e-giftcard-excelfile-generator-new-invoice-format.py`
- `amazon-e-giftcard-generator.py`
- `2022-10-20-Amazon.xlsx`

These files were reviewed as technical discovery inputs. They should not be committed to the repo unless Progressive explicitly approves storing source scripts here.

## Executive Read

The code review confirms the March 27 discovery finding: this is a fragile but understandable workflow, not a deeply complex proprietary system.

The current scripts automate the awkward middle of Progressive's fulfillment process:

1. Read an invoice PDF.
2. Infer invoice number, date, customer, merchant, denomination, and card quantity from extracted PDF text.
3. Create one output folder per merchant/order.
4. Copy the invoice and the relevant Excel template into that folder.
5. Append order rows into each merchant-specific Excel template.
6. For Amazon, take a populated Amazon Excel file, generate one SVG/PDF per card, create a log CSV, and ZIP the output for delivery or SystemOne.

The hard part is not the PDF rendering. The hard part is turning an undocumented, local-machine workflow into something resilient enough for non-technical staff.

## What the Invoice-to-Excel Script Does

The first script, `e-giftcard-excelfile-generator-new-invoice-format.py`, is a 990-line procedural script with a small Tkinter file picker.

Inputs:

- One invoice PDF selected manually through a desktop file dialog.
- Vendor Excel templates expected under `../orders/<vendor-folder>/template/`.
- A specific folder layout where the script is run from `prototype/` and writes into `../orders/...`.

Core dependencies:

- `pandas`
- `openpyxl`
- `tika`
- local template workbooks
- local folder structure

Behavior:

- Uses Apache Tika to extract text from the invoice PDF.
- Searches extracted PDF lines for `INVOICE`, `Corporate`, `DATE`, and `BILL TO`.
- Uses regex and many line-length-specific branches to identify e-card line items.
- Builds a `cardList` with vendor, denomination, quantity, invoice number, invoice date, and customer.
- Maps vendors to template folders using hard-coded dictionaries.
- Copies the invoice and template workbook into a timestamped order folder.
- Appends the appropriate number of rows into each vendor's Excel template.

Vendors encoded in the script include:

- Amazon
- Best Buy
- Boston Pizza
- Browns Social House
- Cactus Club
- Cara
- Chapters Indigo
- DoorDash
- Esso
- Earls
- Fairmont Hotels
- Hudsons Bay
- Home Depot
- H&M
- Keg
- Loblaws
- Master Card
- Petro Canada
- Sephora
- Shoppers Drug Mart
- Starbucks
- Subway
- Tim Hortons
- Uber
- Walmart
- Winners

Important caveat: the provided invoice-to-Excel script appears to prepare vendor-specific Excel files and populate order metadata rows. It does not, in this provided copy, appear to fully retrieve or consume card inventory by itself. For Amazon, the `CLAIM CODE` and `SERIAL NUMBER` fields are still expected to be populated from inventory before the Amazon generator runs, matching Lloyd's email.

## What the Amazon Generator Does

The second script, `amazon-e-giftcard-generator.py`, is a 561-line procedural script with a Tkinter file picker.

Inputs:

- One populated Amazon Excel workbook.
- A local SVG template at `../templates/amazon-e-giftcard-template.svg`.
- Inkscape installed at a hard-coded OS-specific path.
- A missing local helper module, `utilities.py`, providing `zipFilesInDir`.

Amazon workbook contract:

| Column | Purpose |
|---|---|
| `SEQUENCE` | Required numeric row/card sequence |
| `CLAIM CODE` | Required Amazon claim code |
| `AMOUNT` | Required amount, expected to parse as decimal |
| `SERIAL NUMBER` | Required inventory serial number |
| `CUSTOMER` | Required customer name/id |
| `MESSAGE` | Optional customer message; defaults to blank |
| `Invoice #` | Required invoice number |
| `Date` | Required invoice date |

Behavior:

- Reads every sheet in the workbook with pandas.
- Validates required values at a basic null/printable level.
- Formats the amount as `CDN$`.
- Creates a run folder, then an invoice/date folder, then denomination folders.
- Copies the Amazon SVG template for each card.
- Performs string replacement for claim code, message, and amount.
- Renders the SVG to PDF using Inkscape.
- Retries failed/timeout PDF generation up to five times.
- Writes `giftcardlogfile.csv` with card type, card value, and generated PDF filename.
- Deletes intermediate SVG files.
- Creates ZIP files with generated PDFs and CSV logs using `zipFilesInDir`.

Important caveat: the script reads `SERIAL NUMBER` and requires it to be present, but the reviewed code does not appear to insert the serial number into the PDF or log file. It may exist only for inventory traceability in the input workbook.

## Main Risks Found

### 1. Invoice Parsing Is Brittle

The invoice parser depends on PDF text line positions, token counts, and specific string fragments. It starts scanning at fixed line numbers and uses unbounded `while True` loops when looking for invoice number, date, and customer. If the invoice export changes shape or a keyword is missing, the script can crash or hang.

This matches Danny's field note about month/day reversal, missing customers, and script breakage. The failure mode is predictable: the script is tuned to observed invoice text, not to a stable invoice data contract.

### 2. Vendor Logic Is Hard-Coded

Vendor names, folder names, template names, row formats, sheet names, and special cases all live in dictionaries and long `if/elif` branches. This makes the workflow inspectable, which is good, but it means every vendor format change is a code change.

This is the strongest argument for a proper vendor configuration model in the replacement tool.

### 3. Hidden Dependencies Still Matter

The provided files are not enough to reproduce the workflow end-to-end. Redstamp still needs:

- `utilities.py`
- `amazon-e-giftcard-template.svg`
- every referenced Excel template in `../orders/<vendor>/template/`
- representative invoice PDFs
- representative populated inventory/input files
- known-good generated output folders for comparison
- SystemOne expectations for `giftcardlogfile.csv` and ZIP naming

Without those fixtures, we can understand the workflow but should not finalize build estimates as if reproduction has been proven.

### 4. Local Folder Structure Is Part of the System

The script assumes it is run from a specific `prototype/` directory and writes relative to `../orders/...`. That folder structure is not just storage; it is part of the program's behavior.

Any future system needs to deliberately replace this with an explicit order/job model, not merely move the existing files somewhere else.

### 5. Security and Audit Are Incidental

The scripts process cash-equivalent card data locally, but they do not provide modern audit, access control, data-retention, or validation behavior. Debug output can print full extracted invoice text. Intermediate files and generated outputs are created in local folders and remain there unless an operator cleans them up.

This does not mean Progressive has been careless; it means the current system was built as a trusted-operator local workflow. A web-hosted replacement changes the threat model and needs an explicit security posture.

## What This Changes From the March 31 Synthesis

The March 31 synthesis said code review was still pending. This review resolves part of that blocker.

What is now clearer:

- The scripts are understandable enough for Redstamp to replace.
- There is no obvious exotic dependency beyond Inkscape, Tika, pandas/openpyxl, local templates, and SystemOne ZIP/log expectations.
- The main build risk is workflow/data modeling, not reverse-engineering a complex generation engine.
- The invoice parser should be replaced, not ported as-is.
- The Amazon generator can be rebuilt from first principles using the SVG/PDF/template behavior as a reference.

What remains unresolved:

- Whether all vendor templates in Lloyd's folder match the hard-coded mappings.
- Whether Walmart has additional PowerShell or internet-connected activation steps not present in these Python files.
- Whether SystemOne has API options or only manual upload/export.
- Whether the template-generated Excel files are manually populated from inventory, semi-automatically populated elsewhere, or populated by another missing script/process.

## Recommendation

Do not wrap these scripts as the future-state product.

Use them as a behavioral reference and rebuild the workflow around three explicit pieces:

1. **Order extraction and normalization**
   - Replace PDF line parsing with a stable import path where possible.
   - If invoices remain PDF-only, build a tested parser with fixtures and clear failure messages.
   - Output a normalized order model: invoice, customer, merchant, denomination, quantity, delivery preference.

2. **Vendor output generation**
   - Convert the hard-coded vendor dictionaries into versioned vendor configurations.
   - Generate the same Excel outputs the team uses today, but with validation and predictable folder/job records.
   - Preserve SystemOne-compatible logs/ZIPs where needed.

3. **Sensitive card processing**
   - Keep claim codes, serial numbers, PINs, and PDFs in a deliberately scoped secure area.
   - Add audit logs, role-based access, retention rules, and clear deletion/archive behavior.
   - For the first production release, avoid storing unused inventory in the web app unless Doug explicitly accepts that risk.

The fastest valuable MVP is not a full portal. It is a controlled internal fulfillment tool that replaces invoice parsing, template population, and Amazon PDF ZIP generation, while leaving merchant procurement, SystemOne upload, and Walmart activation as external/manual steps until they are better understood.

## Recommended Immediate Next Actions

1. **Ask Lloyd for a reproducible fixture package.**
   - Include `prototype/`, `orders/amazon-ecards/template/`, `orders/<all-vendors>/template/`, `templates/`, `utilities.py`, one sample invoice PDF, one populated Amazon Excel input, and one known-good output folder.
   - Sanitized fixtures are acceptable if the card numbers are not real, but structure must match production.

2. **Run one end-to-end reproduction on a Redstamp machine.**
   - Goal: prove the environment, dependencies, folder layout, and expected output.
   - Capture exact Python version, pip dependencies, Inkscape version, Java/Tika requirement, and OS assumptions.

3. **Create a vendor behavior matrix from the script mappings.**
   - For each vendor: template file, generated columns, whether encrypted template is used, whether card data is manually populated, whether output becomes URL file, PDF ZIP, or both.

4. **Hold a short Lloyd technical follow-up.**
   - Focus only on missing inputs:
     - Where does inventory population happen?
     - Is there another script not included?
     - What is the exact Walmart PowerShell/activation dependency?
     - What does SystemOne require in the ZIP/log file?
     - Why is Amazon serial number required if it is not output?

5. **Update the build recommendation.**
   - Lead with an internal fulfillment tool, not a customer portal.
   - Position current scripts as proven workflow knowledge, but not production architecture.
   - Include a small discovery/reproduction milestone before fixed-price build commitment.

## Draft Note to Lloyd

Hi Lloyd,

Thanks for sending the scripts and Amazon template. We were able to review the general flow: invoice PDF to vendor-specific Excel files, then the Amazon Excel file to generated PDFs/ZIP using the SVG template and Inkscape.

To complete the technical assessment, could you send or share a small reproducible package with the supporting files these scripts expect?

- the `prototype` folder context the scripts run from
- `utilities.py`
- the Amazon SVG template under `templates`
- the referenced Excel templates under `orders/<vendor>/template`
- one representative invoice PDF
- one populated Amazon Excel file with fake/sanitized card data if needed
- one known-good generated output folder so we can compare expected results

The goal is not to take over the live process yet. We just want to run the workflow in a clean environment, document the dependencies, and make sure our recommendation to Doug is grounded in the real moving parts.

Thanks,
Spencer

