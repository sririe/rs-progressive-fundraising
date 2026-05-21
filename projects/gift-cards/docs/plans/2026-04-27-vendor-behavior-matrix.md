---
title: "Vendor Behavior Matrix — Digital Fulfillment"
type: plan
category: technical-reference
date: 2026-04-27
status: draft
tags:
  - progressive
  - vendor-matrix
  - digital-fulfillment
  - card-generation
  - lloyd-scripts
  - reference
key_insights:
  - The 25+ vendors collapse cleanly into 3 patterns once mapped — most of the perceived complexity is variation within Pattern 1.
  - Pattern 2 (in-house generation) is the smallest cohort but carries the most build risk because it touches sensitive card numbers.
  - Walmart is its own column, not a row — the activation, reconciliation, and PowerShell layer don't fit the vendor-template model used elsewhere.
key_decisions:
  - Use this matrix as the bridge between Lloyd's hard-coded vendor dictionaries and the future vault's vendor-configuration model.
  - Treat the matrix as v1 — it will be refined after the reproduction pass and after the missing vendor templates arrive in the fixture package.
related:
  - projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md
  - projects/gift-cards/docs/plans/2026-03-31-discovery-synthesis.md
  - projects/gift-cards/docs/discovery/2026-03-27-mario-handoff-session2-notes.md
  - projects/gift-cards/docs/discovery/2026-03-27-lloyd-handoff-session1-notes.md
---

# Vendor Behavior Matrix — Digital Fulfillment

## Purpose

Lloyd's invoice-to-Excel script encodes vendor behavior in long `if/elif` branches and dictionary lookups. That is inspectable but not portable. This matrix takes the same information and presents it in a form the whole team can read — and that the future vault can use as the basis for a versioned vendor-configuration model.

This is **v1** based on script reading + the March 27 discovery sessions. It will be refined after Tim/Bronte run the reproduction pass with Lloyd's full fixture package, since we expect the vendor templates themselves to clarify several of the "manual step?" cells below.

## How to Read It

- **Pattern** — which of the three fulfillment models (see synthesis §Three Fulfillment Patterns) the vendor follows.
- **Inventory source** — where the actual card data comes from before generation/packaging.
- **Lloyd's template path** — relative to `orders/<vendor>/template/`, encoded in the invoice-to-Excel script. Means we should expect a workbook with a specific row format to exist there.
- **Output format** — what the customer ultimately receives.
- **Manual steps** — places where a human still has to intervene between the script's output and customer delivery.
- **Build risk** — how this vendor specifically complicates the secure card vault MVP.

## Pattern 1 — Vendor-Provided Inventory (~23 of 28 merchants)

Vendor supplies URLs, PDFs, or challenge codes. Progressive does not generate anything — copy/paste from inventory into a customer-ready encrypted Excel and deliver.

| Vendor | Inventory source | Lloyd template | Output format | Manual steps | Build risk |
|---|---|---|---|---|---|
| Tim Hortons | Vendor-provided URLs (CashStar) | `tim-hortons/template` | Encrypted Excel or URL list | Inventory pull from spreadsheet → paste into customer template → encrypt | Low. Standard Pattern 1. Blackhawk integration on the partner side may eventually replace this. |
| Chapters Indigo | Vendor PDFs | `chapters/template` | Encrypted Excel or URL list | Inventory pull → paste → encrypt | Low. |
| Esso | Vendor URLs (Fundstream) | `esso/template` | URL list | Inventory pull → paste → encrypt | Low. ESO API on Lloyd's roadmap, partner-side blocker. |
| Petro-Canada | Vendor URLs (Fundstream) | `petro-canada/template` | URL list | Inventory pull → paste → encrypt | Low. |
| Best Buy | Vendor URLs/codes | `best-buy/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Boston Pizza | Vendor URLs/codes | `boston-pizza/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Browns Social House | Vendor URLs/codes | `browns/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Cactus Club | Vendor URLs/codes | `cactus-club/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Cara | Vendor URLs/codes | `cara/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. Confirm exact brand portfolio with Lloyd. |
| DoorDash | Vendor URLs/codes | `doordash/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Earls | Vendor URLs/codes | `earls/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Fairmont Hotels | Vendor URLs/codes | `fairmont/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Home Depot | Vendor URLs/codes | `home-depot/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| H&M | Vendor URLs/codes | `hm/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Hudsons Bay | Vendor URLs/codes | `hudsons-bay/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Keg | Vendor URLs/codes | `keg/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| MasterCard | Vendor URLs/codes | `mastercard/template` | Encrypted Excel | Inventory pull → paste → encrypt | Verify — MC may have specific compliance requirements vs typical merchant cards. Flag for Lloyd. |
| Sephora | Vendor URLs/codes | `sephora/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Starbucks | Vendor URLs/codes | `starbucks/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Subway | Vendor URLs/codes | `subway/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Uber | Vendor URLs/codes | `uber/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |
| Winners | Vendor URLs/codes | `winners/template` | Encrypted Excel | Inventory pull → paste → encrypt | Low. |

**Pattern 1 build implications:**
- The vault's "import inventory → assemble customer package → encrypt → deliver" path covers 23 of 28 vendors with a single workflow.
- The variation lives in the template row format, the asset type (URL vs code vs PDF), and the inventory file shape. Each one is a config row, not a code path.
- Manual inventory population — Mario moving denominations from "Mario's folder" (staging) into the live vendor folder — is upstream of the script today. The vault can either encode that step or leave it manual on day one. Recommend leaving it manual for MVP.

## Pattern 2 — In-House Card Generation (5 of 28 merchants)

Progressive generates the card asset (PDF) from raw card numbers using Lloyd's Python + Inkscape pipeline.

| Vendor | Inventory source | Lloyd template | Output format | Manual steps | Build risk |
|---|---|---|---|---|---|
| Amazon | Inventory CSV/Excel populated with claim codes from Amazon | `amazon-ecards/template` + `templates/amazon-e-giftcard-template.svg` | PDF per card → ZIP, optionally pushed to SystemOne for hosted URLs | Populate `CLAIM CODE` and `SERIAL NUMBER` from inventory before running generator; manually upload to SystemOne for URL flow | **High.** Cash-equivalent claim codes pass through generation. Required Amazon workbook contract is documented (see `2026-04-23-lloyd-script-review-next-steps.md §Amazon workbook contract`). |
| Loblaws | Inventory file → script generates branded PDF | `loblaws/template` (and likely an SVG under `templates/`) | PDF per card → ZIP, often via SystemOne | Same as Amazon — populate inventory before generation; SystemOne upload manual | **High.** 600-card order = 3+ hours at 20 sec/card. Performance is a real V1 concern. |
| Shoppers Drug Mart | Inventory file → script generates branded PDF | `shoppers/template` (likely SVG) | PDF per card → ZIP / SystemOne | Same as above | **High.** Confirm SVG template parity with Amazon flow during reproduction. |
| Vendor 4 (TBD) | Per March 27 sessions, "5 of 28" was Mario's verbal estimate | TBD | TBD | TBD | TBD — requires Drive walkthrough |
| Vendor 5 (TBD) | Same | TBD | TBD | TBD | TBD — requires Drive walkthrough |

**Pattern 2 build implications:**
- This is where the secure card vault earns its name — these are the workflows that touch raw cash-equivalent numbers.
- The Inkscape/SVG generation is replaceable but does not need to be replaced from first principles — the SVG template + field-replacement model is sound; the brittle parts are the local folder assumptions, missing fixtures, and lack of audit/access controls.
- Performance is a real concern: rebuilding Loblaws-style 600-card runs needs to be parallelizable, not sequential.
- SystemOne is downstream and out of scope for V1 unless Lloyd surfaces an API option.

## Pattern 3 — Walmart (Unique)

Walmart is its own pattern because there is no pre-purchased inventory — Progressive generates card numbers + PINs via Walmart's Virtual GC Activation tool just-in-time, then runs the same PDF generation as Pattern 2.

| Step | What happens | Tooling | Manual? | Build risk |
|---|---|---|---|---|
| Generate base Excel from invoice | Invoice → vendor-specific Walmart Excel | PowerShell script (Lloyd) | Semi-automated | **Unknown.** Tim digesting PowerShell is a Friday action item. |
| Activate cards via Walmart Virtual GC tool | Generates card numbers + PINs in Walmart's portal | Walmart portal (web) | Manual today; senior management at Walmart pushing for first/last-number bulk activation | High. Activation behavior may not be replicable in a web app — need to confirm internet/VPN/SSO requirements. |
| Generate card PDFs across denomination tabs (25 / 50 / 100 / variable) | Same SVG-based PDF generation as Pattern 2 | Lloyd's PDF generator | Automated | Same as Pattern 2 build risk. |
| Encrypt and deliver | ZIP + password-protected | Same as all patterns | Manual | Low. |
| Monthly reconciliation | Track first/last card numbers per activation; settle with Walmart at month-end | Excel | Manual | Medium. Reconciliation report is a separate deliverable that the vault should be able to produce, but it is not on the critical path for MVP. |

**Pattern 3 build implications:**
- Walmart needs its own dedicated module — it is not a vendor adapter.
- Until the PowerShell scripts and the Walmart Virtual GC interface are characterized (Tim's task), Walmart is a known unknown in pricing and architecture.
- Possible future-state simplification: Lloyd + Doug's planned call with 5serve/Walmart on bulk activation could collapse the manual activation step. Worth tracking outside our scope.

## Cross-Cutting Notes

**Encryption convention.** Across all patterns, password = invoice number stripped of "CPN" prefix and dashes (e.g., CPN-104-5415-2 → 10454152). The vault should preserve this convention — customers know it, Mario validates it by reopening the file before sending, and Doug has been consistent on this with clients.

**Two-email delivery.** Every customer order generates two emails: (1) files + invoice PDF + instructions, (2) password only. Mario uses Gmail draft templates today. The vault should at minimum produce both messages; whether it sends them or hands off to Mario is a design decision tied to the security menu.

**SystemOne.** Third-party service that converts generated card PDFs into hosted URLs. Currently a manual upload from Mario. SystemOne cost, contract, and API availability are still open per the March 31 synthesis. For V1, treat SystemOne as an external dependency we do not replace.

**Inventory staging.** Pattern 1 vendors operate against a "Mario's folder" → "vendor live folder" staging model. The vault can encode this state or leave it as upstream manual work. Recommend leaving it upstream for V1 to keep scope focused.

## What This Matrix Doesn't Yet Have

- The five Pattern 2 vendors are not all confirmed — "5 of 28" was a verbal estimate from Mario. Confirm during reproduction or via Drive walkthrough.
- Vendor template row formats are not yet inspected (we have not opened the workbooks).
- The MasterCard row may need a separate compliance column if there are PCI implications beyond standard merchant cards.
- Walmart's PowerShell internals are not characterized.

This is a v1 working document. It moves us from "Lloyd's dictionaries" to "team-readable behavior matrix" and gives us a structured target for the reproduction pass.
