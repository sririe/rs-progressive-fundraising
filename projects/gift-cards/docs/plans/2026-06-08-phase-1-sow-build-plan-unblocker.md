---
title: "Phase 1 SOW and Build Plan Unblocker"
type: plan
category: internal-alignment
date: 2026-06-08
status: draft
tags:
  - progressive
  - sow
  - build-plan
  - merchant-evidence
  - secure-card-vault
related:
  - projects/gift-cards/docs/plans/2026-05-27-progressive-secure-card-vault-sow-draft.md
  - projects/gift-cards/docs/plans/2026-06-08-sow-merchant-evidence-inventory.md
  - projects/gift-cards/docs/discovery/2026-06-08-private-lloyd-materials-inventory.md
  - projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md
  - projects/gift-cards/docs/plans/2026-03-31-discovery-synthesis.md
blockers:
  - The current evidence base supports the Phase 1 direction, but not unlimited merchant-format commitments.
  - Walmart activation is understood at the workflow level but not validated from source files.
  - The runnable fixture package requested after script review was not found in the recovered Asana/Drive/Gmail/Slack materials.
---

# Phase 1 SOW and Build Plan Unblocker

## Why This Exists

Progressive hired Redstamp to recommend the path forward, not simply document what is hard. The recommended path is still sound: build the Secure Card Vault and Fulfillment Tool before replacing the customer-facing ordering experience.

The gap is confidence around the fulfillment boundary. If the vault ingests orders from the current Pro Gift Cards order flow, Progressive's team needs to be able to fulfill those orders end-to-end inside the new operating model, or clearly know which pieces remain manual. The SOW needs to be honest about that boundary.

This brief is the working input for Spencer and Tim to tighten the SOW and build plan.

## Bottom Line

Phase 1 is still the right recommendation, but the SOW should be tightened before it is sent back to Progressive.

The safest client-ready posture is:

- Build the Secure Card Vault and Fulfillment Tool as the first phase.
- Include a short fulfillment-source validation milestone at the start of Phase 1.
- Scope Phase 1 around a bounded number of validated merchant output formats.
- Prioritize Walmart, Loblaws/Shoppers, Amazon, and a standard merchant-provided URL/code workflow.
- Treat Walmart activation automation, SystemOne replacement, merchant APIs, customer portal work, QuickBooks integration, and direct recipient delivery as outside Phase 1 unless separately validated and priced.

The main issue is not whether the vault is valuable. It is whether the SOW promises more merchant-specific fulfillment automation than the evidence supports.

## Working Checklist For Tomorrow

Use this checklist to turn the current proposal into a tighter SOW/build plan:

| Decision | Recommended Starting Point |
| --- | --- |
| What is Phase 1? | Secure internal vault, inventory, fulfillment queue, allocation, customer-ready outputs, export security, and activity history. |
| What is Phase 1 not? | Customer portal, QuickBooks integration, direct recipient delivery, SystemOne replacement, merchant API integrations, and Walmart/Fiserv activation automation. |
| How many merchant output formats are included? | Choose a fixed allowance, not unlimited coverage. Suggested starting point: four format families. |
| Which format families? | Standard URL/code export, Amazon generated PDF/ZIP, Loblaws/Shoppers validated format, Walmart tracking/output-prep format. |
| What must Progressive/Lloyd provide? | Templates, sample inventory/input, known-good outputs, Walmart activation assets, SystemOne examples, and current merchant folder/list confirmation. |
| What proves staff can use it? | A trained office staff member can fulfill agreed test orders for the included format families without developer support. |

## Current Recommendation

Proceed with Phase 1, but restructure the SOW/build plan around a short validation-and-setup milestone before full implementation.

The Phase 1 promise should be:

> Progressive will have one secure internal system for tracking paid digital gift card orders, managing available digital inventory, allocating cards, preparing validated customer-ready outputs, and recording fulfillment activity.

The Phase 1 promise should not be:

> Every merchant currently available through the Pro Gift Cards digital order form will be fully automated end-to-end.

That second promise is not supported by the materials in hand.

## What We Can Say With Confidence

### 1. The Problem Is Real And Well-Evidenced

Discovery consistently showed that digital fulfillment is manual, fragile, and overly dependent on specific people. Current fulfillment uses WordPress/Formidable order intake, QuickBooks/payment handling, paper triggers, Google Drive folders, spreadsheets, Lloyd's scripts, manual copy/paste, encrypted Excel/ZIP files, SystemOne for some URL output, and two-email delivery.

This is enough to justify Phase 1 as an operational system, not just a technical modernization.

### 2. There Are Three Fulfillment Patterns

The repo evidence still supports the three-pattern model:

| Pattern | Plain-English Definition | SOW Meaning |
| --- | --- | --- |
| Merchant-provided inventory | Merchant provides URLs, PDFs, codes, or challenge-code style access. Progressive packages and encrypts what was provided. | The vault can reduce manual handling by storing inventory, allocating cards, assembling customer-ready files, and tracking activity. |
| Progressive-generated card files | Merchant provides raw card data, and Progressive generates customer-facing PDFs/ZIPs or URL-ready packages. | The vault can support this only where templates, sample inputs, and expected outputs are validated. |
| Walmart just-in-time activation | Walmart cards are ordered/activated as part of fulfillment through a Fiserv-related activation workflow, then prepared for delivery. | The vault can track and guide the workflow, but activation automation is not ready to include without the missing Walmart assets. |

### 3. The Current Website Has A Digital Merchant Catalog Wider Than The Big Three

Doug's sales split makes Walmart, Loblaws, and Amazon the commercial priority. But the customer-facing Pro Gift Cards order form still exposes a broader digital catalog.

Current order-form evidence resolves to 22 unique Digital E-Cards brands:

- Amazon
- Best Buy
- Boston Pizza
- Cactus Club
- Chapters - Indigo - Coles
- DoorDash
- Earls
- Esso
- Fairmont Hotel
- H&M
- Home Depot
- Loblaws - Superstore, PC, No Frills, Extra Foods, Provigo
- Petro-Canada
- Recipe Unlimited
- Sephora
- Shopper's Drug Mart
- Starbucks
- Subway
- The Keg
- Tim Hortons
- Walmart
- Winners

The public merchant page has more visible tiles than unique order-form brands because grouped merchants such as Loblaws and Recipe Unlimited appear under multiple banners/logos.

SOW implication: the build can prioritize Walmart, Loblaws, and Amazon, but it should not ignore the rest of the customer-facing digital catalog. Staff need a clean way to fulfill or at least track/handle those order lines.

### 4. The Recovered Lloyd Package Is Useful But Incomplete

Recovered files:

- `e-giftcard-excelfile-generator-new-invoice-format.py`
- `amazon-e-giftcard-generator.py`
- `2022-10-20-Amazon.xlsx`

These confirm merchant-specific workbook creation and Amazon's PDF/ZIP workflow. They do not provide a runnable environment.

Missing items still matter:

- `utilities.py`
- `make-zip.ps1`
- Amazon SVG/PDF template
- all non-Amazon merchant workbook templates
- sample invoice PDF
- populated safe test workbook
- known-good generated output
- Walmart/Fiserv activation files and examples
- SystemOne upload/export requirements

### 5. The Missing Fixture Request Was Identified But Not Closed

The source trail shows:

| Date / Source | What Happened | What It Means |
| --- | --- | --- |
| March 26 Lloyd pre-onsite notes | Lloyd described the broader Windows/Python/Java/PowerShell/Inkscape environment, `make-zip.ps1`, Walmart/Fiserv activation, and SystemOne upload/export. | We understood there were more files and dependencies than the later attachment set. |
| April 17 Danny request | Danny asked Lloyd for the digital gift card scripts and setup context. | Good broad ask, but not the later exact fixture package. |
| April 21 / 22 Lloyd response and Asana/Drive storage | Lloyd provided the two Python scripts and Amazon workbook. | Confirmed package is useful but incomplete. |
| April 23 script review | Redstamp identified `utilities.py`, SVG templates, vendor templates, sample invoices, outputs, Walmart assets, and SystemOne notes as missing. | The gap was known before proposal development. |
| April 27 fixture request draft | A precise follow-up request was drafted. | I found no evidence in the repo/source trail that it was sent and answered. |
| June 8 recovery pass | Asana, Gmail, Slack, and the Drive folder all point back to the same three recovered files. | The missing fixture package remains missing. |

This is the key unblocker: we need to close the fixture request now, before the SOW language hardens around assumptions.

### 6. The Existing SOW Draft Is Directionally Right But Needs A Tighter Boundary

The May 27 SOW draft already says merchant-specific file creation is limited to agreed Phase 1 formats and that special activation processes are excluded unless added by change order. That is the right posture.

The weakness is that the SOW currently pushes source verification into "production planning" without making that a strong enough milestone. Doug's follow-up questions show they expect clarity now on named merchant formats, customer-ready files, exported-file security, Walmart activation, and ordinary-staff fulfillment.

## SOW Edits To Make Next

These are the specific edits I would make before sharing a final SOW:

- Add a Phase 1A fulfillment-source validation milestone before implementation language.
- Replace broad "customer-ready file creation" language with a definition tied to encrypted Excel/export files, PDF/ZIP packages, or URL/code exports for validated formats.
- State the included merchant-format allowance by count and type.
- Say Walmart fulfillment is included as tracking, manual activation handoff, post-activation capture/import where feasible, output preparation, and activity history.
- Exclude Walmart/Fiserv activation automation unless separately validated and approved.
- Treat Loblaws/Shoppers as a priority format to validate, not as an already-proven generated-card workflow.
- Include activity logging for sensitive-card view/reveal, allocation, export, and status changes.
- Clarify exported-file security: password protection, expiration/deletion policy, export history, and responsibility after download.
- Add a client dependency for templates, sample inputs, known-good outputs, and current active merchant confirmation.
- Resolve the Redstamp hourly-rate mismatch before finalizing the Project Terms.

## Where We Are Exposed

### Exposure 1: "Customer-Ready File Creation" Is Too Broad

Doug asked what this means for Walmart, Loblaws, and Amazon. The current answer cannot be one generic phrase.

Recommended breakdown:

- For merchant-provided inventory: customer-ready file means an encrypted Excel/export containing the card URLs/codes/access details allocated to that order.
- For Amazon-style generated cards: customer-ready file means a PDF ZIP or URL-ready package created from validated card data and a supplied template.
- For Walmart: customer-ready file can mean generated delivery files after the activation step has produced card numbers/PINs; it should not imply the vault activates cards with Walmart/Fiserv unless separately validated.

### Exposure 2: Walmart Is Commercially Important But Technically Under-Provided

What we know:

- Walmart is high volume.
- Walmart is just-in-time.
- Lloyd described a Fiserv-related Java activation program.
- Mario's walkthrough shows activation, monthly tracking, generated PDFs, encryption, and delivery.

What we do not have:

- activation `.jar`
- activation workbook/template
- PowerShell/launcher setup
- sample activation input/output
- reconciliation workbook example
- confirmation of whether activation can be safely supported in a web app

SOW posture: track, guide, and record Walmart fulfillment in Phase 1; exclude direct activation automation until we validate the assets and external dependency.

### Exposure 3: Loblaws / Shoppers Status Is Ambiguous

The current evidence points in two directions:

- Earlier notes/script mappings treat Loblaws and Shoppers as generated or special-format workflows.
- Lloyd's pre-onsite notes say newer Loblaws, Shoppers, and Petro-Canada inventory may now be ordinary URL inventory.

SOW posture: treat Loblaws/Shoppers as priority formats to validate, not as already-proven generated-PDF flows.

### Exposure 4: We Have The Amazon Logic But Not Enough To Reproduce It

Amazon is the best-evidenced generated workflow. We have the generator script and workbook structure, and Lloyd's email explains manual claim-code/serial-number population.

Still missing:

- `utilities.py`
- SVG template
- populated safe workbook
- known-good output folder
- SystemOne expectations if URL delivery is required

SOW posture: include Amazon as the first generated-card format, but require missing fixtures before acceptance criteria are finalized.

### Exposure 5: The Long-Tail Merchants Still Need A Workflow

Even if most revenue is Walmart/Loblaws/Amazon, the storefront allows other digital merchant orders. Mario still has to fulfill those.

SOW posture: Phase 1 should support a general merchant-provided inventory workflow for the long tail. It does not need bespoke automation for every merchant, but it should let staff:

- create/order line items by merchant,
- see inventory by merchant/denomination,
- allocate URLs/codes/PDFs to a paid order,
- export an encrypted customer-ready file,
- record delivery/status.

This may be more important than rebuilding every historical template on day one.

### Exposure 6: Script Merchants And Storefront Merchants Do Not Match Perfectly

The recovered script references merchants that are not currently standard Digital E-Cards dropdown options:

- Browns Social House
- Hudsons Bay
- Master Card
- Uber

The current storefront names also need alias handling:

- `Cara` in scripts = Recipe Unlimited in the storefront.
- `Keg` in scripts = The Keg.
- `Chapters Indigo` in scripts = Chapters - Indigo - Coles.
- `Petro Canada` in scripts = Petro-Canada.
- `Fairmont Hotels` in scripts = Fairmont Hotel.
- `Shoppers Drug Mart` in scripts = Shopper's Drug Mart in the live form.

SOW/build implication: the vault should not key merchant behavior off raw storefront strings alone. It needs merchant aliases/configuration, and the SOW should scope against the active order-form brand list plus validated operational formats.

## Recommended SOW Shape

### Add A Phase 1A Validation And Configuration Milestone

Before the main build commitments, add a short milestone inside the SOW:

**Phase 1A: Fulfillment Source Validation and Merchant Configuration**

Purpose:

- confirm current customer-facing digital merchant catalog,
- confirm which merchants are active in Progressive's fulfillment folders,
- validate the initial merchant formats,
- confirm Walmart boundary,
- define acceptance examples for customer-ready files.

Outputs:

- active digital merchant list,
- included Phase 1 merchant-format list,
- output examples for each included format,
- unresolved merchant/activation exclusions,
- final build configuration assumptions.

This can be part of the fixed-fee project, but the SOW should say that implementation of merchant-specific outputs depends on this milestone.

### Use A Bounded Merchant-Format Allowance

Recommended SOW language:

> Phase 1 includes configuration and implementation for up to [X] validated merchant output formats. The initial priority will be Walmart, Loblaws/Shoppers, Amazon, and the standard merchant-provided URL/code workflow. Additional merchant-specific templates, generated-file rules, or format changes will be handled through an approved change order or later phase.

Tim and Spencer need to choose X. My recommendation is:

- 1 standard merchant-provided URL/code export format for the long tail,
- 1 Amazon generated PDF/ZIP format,
- 1 Loblaws/Shoppers format after validation,
- 1 Walmart tracking/output-prep format that excludes activation automation.

That gives Progressive practical coverage without promising full automation of all edge cases.

### Keep Walmart Activation Out, But Not Walmart Fulfillment

Do not say "Walmart is out of Phase 1." That would be commercially tone-deaf.

Say:

> Phase 1 will support Walmart order tracking, status visibility, manual activation handoff, post-activation card capture/import where feasible, customer-ready file preparation, and fulfillment activity history. Automated Walmart/Fiserv activation, portal automation, balance lookup, and monthly reconciliation automation are excluded unless separately validated and approved.

This respects Walmart's importance without pretending we have the activation source.

### Treat Customer-Ready Files As A Validated Output Class

Replace generic wording with:

> Customer-ready files include the agreed encrypted Excel, ZIP/PDF, or URL/code export formats used to deliver allocated digital gift cards to Progressive's customers. Each included format must be backed by a current template, sample inventory/input, and expected output example supplied by Progressive.

## What We Need Before Tim/Spencer Lock Scope

### Must-Have For SOW Confidence

1. Current active digital merchant list from Progressive.
2. Current list of merchants/folders Progressive actually fulfills digitally.
3. Confirmation of the exact Phase 1 merchant formats to include.
4. Representative sample inventory/input for each included format.
5. Known-good customer-ready output for each included format.
6. Clear Walmart boundary: track/manual handoff versus activation support.
7. Export security decision: password ZIP/Excel, retention/deletion, access logging, and post-export responsibility.
8. Acceptance criteria for "ordinary office staff can fulfill digital orders."

### Must-Have For Technical Reproduction

1. `utilities.py`.
2. `make-zip.ps1`.
3. Amazon SVG template.
4. Merchant workbook templates under `orders/<merchant>/template/`.
5. Representative invoice PDF.
6. Populated safe/fake Amazon workbook.
7. Known-good Amazon output.
8. Walmart activation `.jar`, workbook/template, sample input/output, and reconciliation example.
9. SystemOne sample ZIP/log/export and API/manual-process notes.

### Must-Have Source Trail Follow-Up

1. Confirm whether the April 27 fixture request was ever sent.
2. If it was sent, locate the response or shared folder.
3. If it was not sent, send the updated request now.
4. Ask for a folder dump rather than a polished package. Redstamp can sort and inventory the materials.

### Nice-To-Have But Not Blocking

- API documentation for Esso or Blackhawk/Tim Hortons.
- Save-on-Foods or Sequoia white-label status.
- Merchant-provided current reporting options for Walmart/Loblaws/Amazon bulk orders.
- Historical error examples.
- Current support process for invalid, inactive, or already-redeemed cards.

## Recommended Agenda For Tim And Spencer

### 1. Align On Build Philosophy

Decision:

- Are we replacing Lloyd's scripts directly?
- Or are we rebuilding the workflow around a vault/order/job model using Lloyd's scripts as behavioral references?

Recommended answer: rebuild the workflow model; do not wrap the scripts as production architecture.

### 2. Define The Phase 1 Merchant Boundary

Decision:

- Which output formats are included?
- How many merchant formats are included before change orders apply?
- Is Loblaws/Shoppers one format or multiple?
- Is Walmart included as tracking/output prep only?

Recommended answer: include a bounded format allowance and make Walmart activation a separate validation item.

### 3. Define "Customer-Ready File"

Decision:

- What exact outputs does the vault produce?
- Encrypted Excel?
- Password-protected ZIP?
- Generated PDFs?
- URL/code export?
- Email drafts?

Recommended answer: support encrypted files/exports and activity history in Phase 1; keep automated delivery emails and customer portal delivery out.

### 4. Define Security/Audit Defaults

Decision:

- Who can view full card data?
- Does every reveal/decrypt/export get logged?
- How long do exported files remain available?
- What happens after files leave the vault?
- Does Redstamp have break-glass access?

Recommended answer: Progressive role-based access by default; Redstamp no raw-card access except approved support path; log every sensitive view/export; define retention and deletion explicitly.

### 5. Define Staff Acceptance Criteria

Decision:

- What proves ordinary office staff can fulfill orders?

Recommended answer:

> A trained Progressive staff member can fulfill agreed test orders for the standard URL/code workflow, Amazon generated-card workflow, Loblaws/Shoppers validated workflow, and Walmart manual-activation handoff workflow without developer support, using the vault, provided runbook, and approved test data.

## Draft Follow-Up Ask To Progressive / Lloyd

This is the low-friction ask that gets us unstuck without sounding like discovery failed:

> As we tighten the Phase 1 SOW and implementation plan, we want to confirm the exact merchant formats and sample outputs that should be included in the first build. We have the initial scripts and Amazon workbook Lloyd shared, but the remaining support files and examples are what will let us define the build boundary cleanly and avoid assumptions.
>
> Could you share or help us collect the current materials for the initial Phase 1 merchant set?
>
> - current active digital merchant list,
> - current digital merchant folder list,
> - sample inventory/input files for Walmart, Loblaws/Shoppers, Amazon, and one standard URL/code merchant,
> - known-good customer-ready output files for each,
> - the Amazon SVG template and helper files used by the generator,
> - Walmart activation workbook/template, launcher details, and one safe sample input/output,
> - SystemOne sample upload/export/log files or notes,
> - any current rules around exported-file passwords, cleanup, or retention.
>
> This does not need to be polished. A folder dump is fine; Redstamp can sort and inventory it.

## Who Needs To Do What

| Owner | Action | Reason |
| --- | --- | --- |
| Spencer | Decide whether to send a short client-facing note asking for the missing package now, or route it through Stephanie/Doug first. | Protects relationship while reducing ambiguity. |
| Tim | Review this brief and choose the bounded merchant-format allowance for the SOW. | The fixed-fee scope needs an engineering-owned boundary. |
| Lloyd / Progressive | Provide the raw fixture package or confirm the missing assets do not exist in shareable form. | Required to validate generated-card and Walmart assumptions. |
| Stephanie | Help turn the final decisions into client-ready SOW language and support plan language. | Keeps proposal posture advisory and clear. |

## Recommendation For Doug Response

Do not answer every technical question as though all implementation choices are final. Instead:

- acknowledge that the questions are exactly the right ones,
- say we are tightening the Phase 1 scope around named merchant formats, file security, and Walmart boundaries,
- request the missing support materials now so kickoff is not spent hunting for them,
- commit to returning with a clean Phase 1 scope and support recommendation.

Practical posture:

> We can proceed, but we should not pretend the SOW is fully locked until the merchant-format and Walmart activation evidence is closed.

That is not weakness. That is good advisory work.
