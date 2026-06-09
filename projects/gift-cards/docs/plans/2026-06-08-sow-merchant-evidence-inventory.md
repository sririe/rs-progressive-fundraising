---
title: "SOW Merchant Evidence Inventory"
type: plan
category: scope-readiness
date: 2026-06-08
status: draft
tags:
  - progressive
  - sow
  - merchant-inventory
  - secure-card-vault
  - scope-readiness
related:
  - projects/gift-cards/docs/discovery/2026-06-08-private-lloyd-materials-inventory.md
  - projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md
  - projects/gift-cards/docs/plans/2026-04-27-vendor-behavior-matrix.md
  - projects/gift-cards/docs/plans/inbox/2026-03-19-digital-vendor-and-workflow-prework-sheet.csv
blockers:
  - Missing support files prevent end-to-end reproduction of Lloyd's current workflows.
  - Walmart activation assets were not included in the materials recovered from Asana, Gmail, Slack, or Google Drive.
---

# SOW Merchant Evidence Inventory

## Purpose

This document translates the Lloyd source trail into SOW-ready scope guidance. It is intentionally stricter than the earlier merchant behavior matrix: it separates what Redstamp has actually received from what we understand at a process level.

The goal is to avoid committing to merchant-specific fulfillment formats, Walmart activation behavior, or customer-ready file generation that we have not validated with source files or known-good outputs.

## Status Definitions

| Status | Meaning for SOW |
| --- | --- |
| Evidence in hand | We have source material we can inspect locally. This does not always mean the workflow is reproducible. |
| Process-level only | We have meeting notes, Lloyd email language, or Slack notes, but not the files needed to reproduce the workflow. |
| Missing | We know the item exists or likely exists, but it was not provided. |
| SOW-ready | Safe to include as a Phase 1 deliverable with clear assumptions. |
| Conditional | Can be included only if framed around validation, client-provided files, or a limited named format count. |
| Not ready | Should be excluded, deferred, or treated as a separate technical validation item before fixed pricing. |

## Evidence in Hand

| Source | What We Have | What It Supports | Limit |
| --- | --- | --- | --- |
| Lloyd April 21 email | Written explanation of invoice-to-merchant Excel generation, Amazon PDF ZIP generation, Amazon workbook fields, folder structure, and Inkscape dependency | Confirms the workflow shape and manual inventory population step | Does not include the full runnable environment |
| Asana / Google Drive attachment set | `e-giftcard-excelfile-generator-new-invoice-format.py`, `amazon-e-giftcard-generator.py`, `2022-10-20-Amazon.xlsx` | Confirms script-encoded merchant list, Amazon workbook contract, and template-driven generation approach | Missing helper files, templates, inputs, outputs, and Walmart assets |
| March 26 Slack note from Danny sharing Lloyd's pre-onsite notes | Process description for Windows/Python/Java/PowerShell/Inkscape tooling, PDF vs URL delivery, SystemOne upload/export, and Walmart/Fiserv activation | Confirms Walmart is a distinct just-in-time activation workflow | Does not provide Walmart activation files or reproducible examples |
| April 24 internal Google Doc: `Progressive: Lloyd's Scripts + Next Steps` | Prior Redstamp assessment of scripts and missing support inputs | Confirms the current source gap was already identified | It is an internal assessment, not new client-provided material |
| Storefront prework sheet | Customer-facing digital merchant list and initial workflow assumptions | Helps compare script merchants against storefront merchants | Many rows were explicitly marked "needs validation" |

## June 8 Gmail And Slack Recovery Check

Spencer asked for an additional check of Gmail and messages with Danny to see whether the missing runnable package had been shared elsewhere.

Checked sources:

- Gmail exact and broad searches for `utilities.py`, `make-zip.ps1`, `walmart-giftcard-virtual-activation-production.jar`, `amazon-e-giftcard-template.svg`, Progressive/Lloyd/scripts/prototype terms, Danny messages, and Lloyd messages with attachments.
- Slack search across public channels, private channels, DMs, and files for the same missing filenames and Progressive/Lloyd/Danny/script/template terms.
- Slack thread replies on Danny's March 26, 2026 Lloyd pre-onsite context post and April 22, 2026 Lloyd scripts handoff post.

Result:

- Gmail found only the known April 21, 2026 Lloyd message with three attachments: the invoice-to-Excel script, the Amazon PDF generator script, and the Amazon workbook.
- Slack found Danny's March 26, 2026 pre-onsite post and April 22, 2026 Asana/Drive handoff post, but no additional package and no thread replies containing missing files.
- Danny-specific Gmail attachment results found calendar invites and the known Asana notification, not additional script packages.

Updated conclusion: there is still no evidence that the missing runnable fixture package was shared through Spencer's Gmail, Danny's Gmail-visible thread, Slack, the Asana ticket, or the linked Google Drive folder.

## Current Customer-Facing Digital Catalog

The current Pro Gift Cards order form resolves to 22 unique Digital E-Cards brands. Scope should be measured against these order-form brands, not against every visible merchant tile/logo or every historical script row.

| Order-form brand | Notes |
| --- | --- |
| Amazon | Priority merchant; strongest generated-card evidence. |
| Best Buy | Long-tail merchant-provided format until proven otherwise. |
| Boston Pizza | Long-tail merchant-provided format until proven otherwise. |
| Cactus Club | Long-tail merchant-provided format until proven otherwise. |
| Chapters - Indigo - Coles | Script alias: `Chapters Indigo`; workflow needs confirmation. |
| DoorDash | Long-tail merchant-provided format until proven otherwise. |
| Earls | Long-tail merchant-provided format until proven otherwise. |
| Esso | API exploration noted; Phase 1 should treat as external/manual unless separately scoped. |
| Fairmont Hotel | Script alias: `Fairmont Hotels`. |
| H&M | Long-tail merchant-provided format until proven otherwise. |
| Home Depot | Long-tail merchant-provided format until proven otherwise. |
| Loblaws - Superstore, PC, No Frills, Extra Foods, Provigo | Priority merchant group; confirm whether all banners share one current format. |
| Petro-Canada | Newer inventory may be URL-based. |
| Recipe Unlimited | Script alias: `Cara`; grouped customer-facing brand. |
| Sephora | Long-tail merchant-provided format until proven otherwise. |
| Shopper's Drug Mart | Script alias: `Shoppers Drug Mart`; confirm relationship to Loblaws formats. |
| Starbucks | Long-tail merchant-provided format until proven otherwise. |
| Subway | Long-tail merchant-provided format until proven otherwise. |
| The Keg | Script alias: `Keg`. |
| Tim Hortons | Blackhawk/CashStar API exploration noted; Phase 1 should treat as external/manual unless separately scoped. |
| Walmart | Priority merchant; activation automation not validated. |
| Winners | Long-tail merchant-provided format until proven otherwise. |

Script-configured merchants not currently confirmed as standard Digital E-Cards dropdown options: Browns Social House, Hudsons Bay, Master Card, and Uber.

## Evidence Still Missing

These gaps matter before the Phase 1 SOW is locked:

- `utilities.py`, required by the Amazon generator for ZIP creation.
- `make-zip.ps1`, referenced by Lloyd for password-protected ZIP creation.
- `amazon-e-giftcard-template.svg`, required by the Amazon PDF generator.
- All merchant workbook templates under `orders/<merchant>/template/`, except the Amazon workbook we recovered.
- One representative invoice PDF.
- One populated Amazon workbook with safe or fake test card data.
- One known-good generated Amazon output folder.
- Walmart activation assets, including `walmart-giftcard-virtual-activation-production.jar`, activation workbook/template, launcher details, sample input, sample output, and reconciliation example.
- SystemOne requirements for ZIP naming, logs, upload/import, export, URL format, and any API availability.
- Representative URL inventory files for pass-through merchants.
- Confirmation of which storefront merchants are still active digital offerings.

## Source Trail Conclusion

The fixture gap appears to be a follow-up gap, not a discovery-session gap.

Redstamp identified the missing support materials after reviewing Lloyd's initial scripts and drafted a precise fixture request on April 27, 2026. I did not find evidence that the full request was sent and answered. The currently confirmed package remains limited to the two Python scripts and Amazon workbook.

SOW implication: before finalizing named merchant-format commitments, Redstamp should either obtain the missing fixture package or explicitly scope Phase 1 around validated formats only, with unprovided formats handled as change orders or follow-on work.

## High-Priority Merchant Readiness

Doug's current sales breakdown makes Walmart, Loblaws, and Amazon the commercial priority. The source evidence does not make those three equally ready for SOW commitment.

| Merchant / Group | What We Know | What We Have | What Is Missing | SOW Posture |
| --- | --- | --- | --- | --- |
| Walmart | Large volume. Lloyd described this as just-in-time ordering and activation through Fiserv using a Java activation program. Script has a Walmart template mapping. | Process-level notes and invoice-to-Excel script mapping. | Activation program, Walmart workbook/template, activation input/output, reconciliation example, operational screenshots or walkthrough video, and confirmation of whether activation can be safely supported inside Phase 1. | Not ready for activation automation. Phase 1 can track Walmart orders, inventory/status, generated customer files if validated, and manual handoff steps. Activation support should be excluded or separately priced until assets are reviewed. |
| Loblaws banner group | Doug cites Loblaws as a major share. Storefront prework lists Superstore, PC, No Frills, Extra Foods, and Provigo under Loblaws. Lloyd noted older Loblaws inventory had generated/Progressive-branded behavior, while newer Loblaws URLs may be treated like ordinary URL inventory. | Invoice-to-Excel script mapping and template filenames. Process-level notes. | Loblaws template files, current URL inventory examples, old-format examples if still active, customer-ready output examples, and confirmation of which banners share the same format. | Conditional. Safe to include as a prioritized merchant group only if SOW says formats are validated during implementation and excludes old-format generation unless fixtures are provided. |
| Amazon | Lloyd provided the most evidence here. Existing flow creates an Amazon workbook, then a PDF ZIP using Inkscape after claim codes and serial numbers are manually populated. | Amazon generator script, invoice-to-Excel script mapping, Amazon workbook/template, Lloyd email explanation. | `utilities.py`, Amazon SVG template, populated safe test workbook, known-good output, SystemOne expectations if URLs are required. | Conditional. Strongest candidate for named Phase 1 customer-ready file support, but still requires missing fixtures before we can promise exact reproduction. |

## Other Script-Configured Merchants

The invoice-to-Excel script references these merchant configurations. For most of them, we have the mapping but not the actual template file or example inventory.

| Merchant | Seen In | Current Evidence | Missing Before Format Commitment | SOW Posture |
| --- | --- | --- | --- | --- |
| Best Buy | Script and storefront | Template filename only | Template, sample inventory, customer-ready output | Conditional as pass-through/URL format |
| Boston Pizza | Script and storefront | Template filename only | Template, sample inventory, customer-ready output | Conditional as pass-through/URL format |
| Browns Social House | Script only | Template filename only | Confirm active offering, template, sample inventory, output | Do not name unless confirmed active |
| Cactus Club | Script and storefront | Template filename only | Template, sample inventory, output | Conditional |
| Cara / Recipe Unlimited | Script and storefront prework | Template filename only | Confirm storefront naming, included brands, template, sample inventory, output | Conditional |
| Chapters Indigo | Lloyd email, script, storefront | Process-level generation notes and template filename | Template, sample inventory, generated output, delivery example | Conditional; likely more complex than ordinary URL pass-through |
| DoorDash | Script and storefront | Template filename only | Template, sample inventory, output | Conditional |
| Earls | Script and storefront | Template filename only | Template, sample inventory, output | Conditional |
| Esso | Script and notes | Template filename and API exploration note | Current source format, template, output, API status | Conditional; API work is outside Phase 1 unless scoped |
| Fairmont Hotels | Script and storefront | Template filename only | Template, sample inventory, output | Conditional |
| H&M | Script and storefront | Template filename only | Template, sample inventory, output | Conditional |
| Home Depot | Script and storefront | Template filename only | Template, sample inventory, output | Conditional |
| Hudsons Bay | Script only | Template filename only | Confirm active offering, template, sample inventory, output | Do not name unless confirmed active |
| Keg | Script and storefront | Template filename only | Template, sample inventory, output | Conditional |
| Master Card | Script only | Template filename only | Confirm active offering, compliance requirements, template, sample inventory, output | Do not name without separate validation |
| Petro Canada | Script and storefront | Template filename and Lloyd note that newer inventory may be URL-based | Current source format, template, sample output | Conditional as URL/pass-through |
| Sephora | Script and storefront | Template filename only | Template, sample inventory, output | Conditional |
| Shoppers Drug Mart | Lloyd email, script, storefront | Template filename and process-level notes; newer inventory may be URL-based | Current source format, old-format examples if still used, template, output | Conditional; likely tied to Loblaws assumptions but should not be collapsed without confirmation |
| Starbucks | Script and storefront | Template filename and prework note as likely pass-through | Template, sample inventory, output | Conditional |
| Subway | Script and storefront | Template filename only | Template, sample inventory, output | Conditional |
| Tim Hortons | Script and storefront | Template filename and note of Blackhawk/CashStar API exploration | Current source format, template, output, API status | Conditional; API integration outside Phase 1 unless scoped |
| Uber | Lloyd pre-onsite note says Progressive no longer sells these digital cards | Script mapping only | Confirm inactive status | Exclude unless Progressive confirms active |
| Winners | Script and storefront | Template filename only | Template, sample inventory, output | Conditional |

## What This Means For The Phase 1 SOW

### Safe To Scope

These items are supported by discovery and source evidence:

- A secure internal card vault and fulfillment workbench.
- Manual order entry into the vault for Phase 1.
- Digital inventory records by merchant, denomination, source, status, and order use.
- Fulfillment queue/status tracking for paid digital gift card orders.
- Role-based access rules for sensitive card data.
- Activity logging for allocation, viewing sensitive values, exporting files, and changing order status.
- Customer-ready file generation as a capability, but only for validated merchant formats.
- Export security rules such as password protection, expiry/deletion policy, and export history.
- Merchant configuration model to replace hard-coded script mappings.

### Conditional Scope Language

Use language like this in the SOW:

> Phase 1 will include customer-ready file creation for the merchant formats validated during implementation, with initial priority on Walmart, Loblaws, and Amazon. Merchant-specific formats will be confirmed against source templates, sample inventory, and expected output examples before implementation.

Avoid language like:

> Phase 1 includes customer-ready file creation for Walmart, Loblaws, and Amazon.

The second version sounds cleaner, but it implies all three formats are equally understood and reproducible. They are not.

### Items To Keep Out Of Phase 1 Unless Separately Validated

- Walmart activation automation or direct Fiserv interaction.
- Walmart reconciliation automation beyond basic order/activity tracking.
- SystemOne API integration or replacement.
- Merchant API integrations for Esso, Tim Hortons/Blackhawk, Amazon, Walmart, or Loblaws.
- Direct recipient delivery.
- Customer portal/order submission.
- QuickBooks integration.
- Full replacement of all merchant templates in the current script set.
- Support for inactive or unconfirmed merchants.

### Suggested Format Boundary

For the SOW, avoid promising unlimited merchant format coverage. Use a bounded structure:

- Include up to a defined number of validated merchant output formats in Phase 1.
- Treat Walmart activation as manual/external unless a validation add-on is approved.
- Treat additional merchant formats, format changes, or unprovided templates as change-order work.
- Require Progressive to provide sample inventory, template files, known-good outputs, and current operating rules for each included merchant format.

## Recommended Immediate Ask

Before finalizing SOW pricing, request a complete runnable fixture package from Progressive/Lloyd:

1. `prototype/` folder context and dependency notes.
2. `utilities.py`.
3. `make-zip.ps1`.
4. Amazon SVG template.
5. All merchant templates under `orders/<merchant>/template/`.
6. One representative invoice PDF.
7. One populated safe/fake Amazon workbook and known-good output folder.
8. Walmart activation workbook/template, Java activation file, launcher notes, sample input/output, and reconciliation example.
9. SystemOne upload/export/log requirements.
10. Current list of active digital merchants and which Loblaws/Shoppers banners share the same format.

## Internal Recommendation

The SOW should not be delayed indefinitely while we chase every merchant detail. It should, however, avoid pretending that every merchant format is already known.

The best path is to propose Phase 1 as a secure fulfillment system with a bounded merchant-format implementation allowance, then make Walmart activation and any unvalidated merchant-specific formats explicit exclusions or validation add-ons.
