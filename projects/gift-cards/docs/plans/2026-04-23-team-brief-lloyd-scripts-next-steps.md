---
title: "Team Brief — What Lloyd's Scripts Tell Us and What We Do Next"
type: plan
category: internal-brief
date: 2026-04-23
status: draft
tags:
  - progressive
  - internal
  - team-brief
  - lloyd
  - digital-fulfillment
  - next-steps
  - build-scope
key_insights:
  - Lloyd's scripts are understandable enough to replace, but not stable enough to wrap as the future product.
  - The next step is a short reproduction pass with missing fixtures, not a full build estimate.
  - The recommended first build is an internal fulfillment tool that reduces operator risk before customer-facing portal work.
key_decisions:
  - Use Lloyd's scripts as reference material.
  - Ask Lloyd for the remaining supporting files needed to run the workflow end-to-end.
  - Update the client recommendation around an internal fulfillment tool first.
related:
  - projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md
  - projects/gift-cards/docs/plans/2026-03-31-discovery-synthesis.md
  - projects/gift-cards/docs/plans/2026-03-11-internal-solution-comparison.md
---

# Team Brief — What Lloyd's Scripts Tell Us and What We Do Next

## Bottom Line

Lloyd's scripts confirm the recommendation we were already moving toward: Progressive needs an internal fulfillment tool before it needs a customer portal.

The scripts are not magic. They are a local workflow that reads invoices, creates vendor-specific Excel files, generates Amazon PDFs through Inkscape, and packages output folders for delivery or SystemOne. That is good news. It means Redstamp can replace the process.

The caution is that the current scripts are brittle. We should not wrap them directly or treat them as production architecture.

## What We Now Know

The current workflow has two main script layers.

**Invoice to vendor Excel files**

The first script reads an invoice PDF, tries to identify the customer/order details, then creates one Excel file per vendor. It relies on:

- PDF text extraction through Tika
- hard-coded vendor names and template paths
- a specific local folder structure
- vendor-specific row formats
- manual inventory population after the file is generated

**Amazon Excel file to generated PDFs**

The second script takes a populated Amazon Excel file, creates one PDF per gift card, writes a log CSV, and zips the output. It relies on:

- the Amazon workbook columns Lloyd provided
- a local SVG gift card template
- Inkscape
- a missing helper file called `utilities.py`
- local output folders and ZIP naming rules

The Amazon workbook contract is clear:

| Field | What It Does |
|---|---|
| `SEQUENCE` | Card row/order number |
| `CLAIM CODE` | Amazon claim code from inventory |
| `AMOUNT` | Card value |
| `SERIAL NUMBER` | Inventory serial number |
| `CUSTOMER` | Customer name |
| `MESSAGE` | Optional message |
| `Invoice #` | Invoice number |
| `Date` | Invoice date |

## What This Means

This is a workflow replacement problem, not a hard reverse-engineering problem.

The value of the new system is not just "generate PDFs faster." The real value is:

- fewer manual steps for Mario or the next operator
- fewer fragile invoice parsing failures
- clearer vendor behavior
- better handling of sensitive card data
- an audit trail for who processed what
- a system Redstamp can support without Lloyd in the middle

The current scripts are useful because they show the required behavior. They should become test fixtures and reference material, not the foundation of the new product.

## What Is Still Missing

We do not yet have enough to run the process end-to-end on a Redstamp machine.

We still need Lloyd to provide:

- `utilities.py`
- the Amazon SVG template
- all vendor Excel templates under `orders/<vendor>/template`
- one representative invoice PDF
- one populated Amazon Excel file with safe test data
- one known-good generated output folder
- any Walmart PowerShell scripts or activation templates
- SystemOne requirements for ZIP files and log files

This matters because final pricing should be based on a reproduced workflow, not just a code read.

## Recommended Path

### 1. Reproduce the Current Workflow

Owner: Tim or Bronte, with Danny collecting files from Lloyd.

Goal: run one clean example outside Lloyd's machine and document exactly what is required.

Output:

- dependency list
- folder map
- known-good input/output examples
- confirmed failure points
- list of scripts/templates still missing

This should be a short technical validation pass, not a new discovery project.

### 2. Build a Vendor Behavior Matrix

Owner: Tim or Bronte.

Turn Lloyd's hard-coded mappings into a table the whole team can read:

- vendor name
- fulfillment pattern
- template file
- required fields
- manual inventory step
- generated output
- delivery format
- known risks

This becomes the bridge between discovery, runbooks, and build scope.

### 3. Update the Client Recommendation

Owner: Spencer.

The next client-facing recommendation should lead with an internal fulfillment tool:

- import or parse invoice data
- normalize order details
- generate vendor Excel outputs
- generate Amazon PDFs/ZIPs
- track job status
- keep sensitive card data scoped and auditable

Portal and customer self-service can stay on the roadmap, but they should not be the first build.

### 4. Make a Security Choice Explicit

Owner: Spencer, with Tim.

Doug needs a clear choice on where sensitive card data lives:

| Option | Tradeoff |
|---|---|
| Local/internal-only processing | Lower exposure, harder remote support |
| Secure web app | Easier support and future portal path, higher security responsibility |
| Hybrid | Stronger boundary, more complexity and support cost |

The team can recommend a path, but we should not bury this decision inside technical implementation.

## Proposed MVP Shape

The first useful product should be an internal fulfillment tool.

It should handle:

- invoice/order intake
- normalized order review before processing
- vendor-specific Excel generation
- Amazon PDF and ZIP generation
- output folder/package creation
- job history and operator notes
- basic role-based access
- retention/deletion rules for generated files

It should not try to do everything at once.

Leave these outside the first version unless reproduction proves they are straightforward:

- Walmart activation automation
- SystemOne API integration
- full inventory procurement forecasting
- customer portal delivery
- direct end-recipient delivery

## Questions for Lloyd

Send Lloyd a short follow-up focused on missing inputs:

1. Can he share the remaining support files needed to run the scripts?
2. Is inventory population handled manually, or is there another script?
3. Is Walmart activation handled by Python, PowerShell, a portal, or some mix?
4. What does SystemOne require from the ZIP/log file?
5. Why does the Amazon generator require serial number if it does not appear in the output?

## Suggested Internal Sequence

This should be the next working order:

1. Spencer sends Lloyd the fixture request.
2. Danny confirms with Doug that Lloyd can share the supporting files.
3. Tim or Bronte runs the reproduction pass.
4. Tim or Bronte creates the vendor behavior matrix.
5. Spencer updates the recommendation and pricing assumptions.
6. Team reviews build path and security posture before putting the next proposal in front of Doug.

## Draft Slack Update

I reviewed Lloyd's scripts. The good news is that they are understandable workflow glue, not a mysterious generation system.

They read invoice PDFs, create vendor Excel files, and generate Amazon PDFs/ZIPs through an SVG template and Inkscape. The risk is brittleness: hard-coded invoice parsing, local folder assumptions, missing templates, and no real audit/security layer.

Recommended next step: ask Lloyd for the remaining fixtures so Tim/Bronte can reproduce one full run, then turn the vendor mappings into a matrix and update the client recommendation around an internal fulfillment tool first.

