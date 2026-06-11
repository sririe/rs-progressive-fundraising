---
title: "SENT — Phase 1 Technical Responses Email to Doug"
type: plan
category: client-email
date: 2026-06-10
status: sent
tags:
  - progressive
  - phase-1
  - client-email
  - sent-record
  - secure-card-vault
key_decisions:
  - Responses went in the email body directly (no attachment); the separate cover-email draft was not used.
  - D-3 resolved harder than the default — the Amazon hosted-URL option was cut entirely; Phase 1 Amazon output is PDF/ZIP only.
  - D-15 (per-export password model) sent to the client as proposed.
  - Closing reveals ongoing Doug/Walmart discussions about a possible direct integration — explicitly not scoped or priced; recommended as a future phase.
  - Next deliverable promised to client - clarifying SOW language (with Stephanie) plus ongoing-support options, once Doug confirms.
key_insights:
  - Spencer's hand edits cut the justify-the-position flourishes ("we'd rather scope them honestly," "convenience, not capability," "format drift is a real, ongoing cost") while keeping the substance — the positions stand without selling themselves.
  - The NZF call was dropped from this email — still agreed (June 8) but unscheduled and unmentioned; needs a separate thread.
related:
  - projects/gift-cards/docs/plans/2026-06-10-phase1-technical-responses-to-doug.md
  - projects/gift-cards/docs/plans/2026-06-10-phase1-decision-sheet.md
  - projects/gift-cards/docs/plans/2026-06-10-doug-reply-draft.md
---

# SENT — Phase 1 Technical Responses Email to Doug

| Field | Value |
| --- | --- |
| Sent | 2026-06-10 5:42 PM PT (2026-06-11T00:42:12Z) |
| Thread | "Re: Reschedule Needed-Phase 1 Proposal" — Gmail thread `19e9a0905b082b87` |
| Message ID | `19eb4212b57457ed` |
| To | dbeers@progressivefundraising.ca |
| Cc | stephanie.lamon@redstamp.com |
| Attachments | None — responses in body |

Verbatim body as sent (asterisks are Gmail bold markers):

---

Hi Doug,

We spent some time going over your questions in detail, and appreciate the thoughtfulness behind them. I know that you want to get this right, as do we.

Two things to highlight before I cover your questions individually (and we can provide an adjusted SOW to better reflect this):

*Phase 1 starts with a validation step.* The first project milestone confirms each included merchant format against your actual materials—current templates, sample inputs, and known-good output files — before we build against it. If an answer below depends on a file we haven't seen yet, we flag it. Confirming that file is scheduled work inside the project, not an open promise.

*Phase 1 includes four merchant output formats:*
A standard export format for merchants that provide URLs or codes — this covers the majority of your digital catalog with one workflow.
The Amazon generated card package (PDF-per-card, delivered as a ZIP).
The Loblaws/Shoppers format, confirmed during validation (see Question 1).
The Walmart format: activation work-file preparation plus import of activated results (see Questions 1 and 9).

To my understanding, these four merchant formats should cover your current merchant base.

*---- Answers to your original questions ---*

*1. What exactly counts as "customer-ready file creation" for Walmart, Loblaws, Amazon?*
It means the vault produces the final, password-protected file your customer receives. Staff never copy card numbers, PINs, claim codes, or URLs between spreadsheets, and never run scripts.

- *Walmart:* the vault prepares the activation work file, your current activation process runs exactly as it does today (outside the vault), and the activated card data comes back in through a controlled import. The vault matches the cards to the order, allocates them, and produces the final customer file — with checks against duplicate imports and a record of who imported and verified the results.
- *Loblaws / Shoppers:* the approved spreadsheet of allocated card URLs and order information. One thing we'll confirm during validation: whether your current Loblaws and Shoppers inventory is URL-based or still uses the older generated-card format — we'll implement whichever is actually in use today.
- *Amazon:* the PDF-per-card ZIP package your customers receive today, generated from validated card data and your current template.

Customer-ready file creation does not include emailing files to customers, hosting download links, or tracking whether a customer opened a file. Those are secure-delivery functions that belong to a later phase.

*2. Which merchant formats are included in Phase 1 by name?*
Walmart, Loblaws (including the banner brands — we'll confirm with you which banners share one format, and whether Shoppers does too), and Amazon — plus the standard export format that covers your remaining digital merchants. Every digital order your storefront takes today has a defined fulfillment path in Phase 1: the big three get their named formats, everything else flows through the standard workflow.

*3. How many merchant format changes are included before change orders apply?*
One approved format per included merchant format, with one consolidated revision round after you approve the acceptance example for that format. After approval, merchant-driven format changes, new templates, or additional variants are handled as change orders or under the support agreement.

*4. What is the fallback intake method if the WordPress/Formidable handoff is not clean?*
Fallback intake is included either way, because manual order entry is a core Phase 1 feature, not a contingency: staff can always create an order directly in the vault, and a structured file import is available as the assisted path. If the website handoff turns out to be messy, fulfillment still works on day one.

*5. Who can decrypt or view full card numbers, PINs, URLs, or access codes?*
Phase 1 has four roles: Admin, Operations, Finance, and Viewer. Only Admin and Operations can produce exports containing full card values. Screens show masked values for everyone — see Question 6. You tell us which staff hold which role (it's on the confirmation list at the end).

One thing you didn't ask but should know: Redstamp has no access to decrypted card data in your production system. If a support situation ever genuinely requires it, that happens only through a logged break-glass path with your written approval for that specific incident.

*6. Is there an audit log for viewing sensitive card data, not just allocation/export actions?*
Yes — and Phase 1 is designed so the answer is airtight: full card values never appear on screen. The only way card data leaves the vault is through an export download by an authorized user, and every export is logged — who, when, and for which order. That means the export log is the complete record of sensitive access; there's no separate "viewing" to account for. Allocation, inventory imports, status changes, replacements, and user management are all logged as well.

*7. How are exported files secured after generation: password ZIP, expiry, access logging, deletion policy?*
The vault generates the password-protected file itself — no manual encryption step, no separate tool. The password handling works like this:

- Each export gets its own randomly generated password, shown once to the operator who created it.
- The password travels to the customer separately from the file — the same separate-message practice you use today, with one improvement: the password is never the filename or anything guessable.
- If a password is lost or a file is compromised, staff don't "un-protect" anything — they generate a fresh export with a new password, and the event is logged. Files are disposable; the vault is the system of record.

The vault keeps a full export history (who exported what, when, and whether delivery was confirmed) but does not store copies of the generated files. Once a file is downloaded, it's outside the system — storage, delivery, and deletion follow your file-handling policy, and we'll help you define that policy during the validation step so it's written down rather than tribal knowledge.

The longer-term answer to this whole category — expiring download links, recipient access logs, no passwords at all — is a secure delivery portal, which we've deliberately kept out of Phase 1 and can scope separately when you're ready.

*8. What happens if an allocated card is later found invalid, inactive, or wrong balance?*
The card is quarantined with a written reason and never returns to available inventory. If matching replacement inventory exists, the vault allocates it and the order moves back to a state where a corrected export can be created; if not, the order sits in a clearly visible needs-replacement state until inventory arrives. Every step is logged. Following up with the merchant for credit stays your process outside the vault — the vault carries a note field so the status is visible, but it doesn't pretend to manage a merchant-side process it can't see.

*9. Is Walmart's activation workflow merely documented/tracked, or partly supported by generated outputs?*
Partly supported by generated outputs — the vault prepares the activation work file, tracks the order through the activation handoff, imports the activated results, and produces the final customer file (the same flow described in Question 1).

What Phase 1 deliberately does not include is automating the activation step itself. That's a boundary, not an oversight: activation touches cash-equivalent card creation through a third-party system, and we won't commit to automating it before we've reviewed the actual activation materials. Once we have them (they're on the materials list below), we can assess whether direct activation support is worth scoping as its own piece.

*10. What support agreement is recommended after launch, and what about November/December?*
With 60% of your sales in November and December and a system handling cash-equivalent data, we recommend a monthly support agreement starting at launch — covering monitoring, backups, priority bug fixes, merchant format updates, user and access support, and defined peak-season response expectations for November/December.

Rather than quote a one-off emergency rate here, we'll include a concrete support proposal with options and pricing alongside the updated SOW, so you can compare real numbers. Emergency work outside any agreement bills at the agency rate in the SOW.

*11. What level of training do ordinary office staff need?*
Office-operations training, not technical training. *The plan:* one guided training session (60–90 minutes), a written step-by-step operating procedure, and supervised practice in the staging environment covering normal orders for each included format plus the two exception cases that actually happen — inventory shortages and invalid-card replacement.

We'd ask you to nominate at least three staff members for training and acceptance testing, so fulfillment never depends on one person again — which was your stated goal. Initial training and materials are included in the build; onboarding new staff later is covered under the support agreement.

*12. What are the acceptance criteria for "anyone in the office can fulfill digital cards"?*
*The honest version of that goal:* trained, authorized staff — the group you nominate — can each complete agreed test orders end-to-end in staging for every included format, without developer help, or anyone technical in the room. That includes finding the order, confirming details, updating payment status, allocating inventory, generating the customer-ready export, recording delivery, closing the order, and handling the inventory-short and invalid-card cases. That's the test we pass together before launch.

*What We Need From You*
One consolidated list — this replaces the scattered per-question asks.

*Confirmations:*

- Which staff hold Admin, Operations, Finance, and Viewer roles.
- That a controlled manual import of activated Walmart results is acceptable for this first version.
- Beyond Amazon, Loblaws, and Shoppers — which one or two other merchants require in-house card generation today.
- Whether current Loblaws and Shoppers inventory is URL-based or generated, and which banner brands share one format.
- Whether Browns Social House, Hudsons Bay, and MasterCard are still active digital offerings.
- Your nominated training and acceptance group (three or more staff).

*Materials (for the validation step — a raw folder dump is perfect; we'll sort and inventory it):*

- The script helper files (utilities.py, make-zip.ps1) and the Amazon card template (SVG) with any related files. *We only receieved a sample example of these to work from.*
- The merchant workbook templates used for order generation (all merchants).
- One representative invoice PDF, one populated Amazon workbook with safe/test data, and the known-good output it produced.
- One sample URL-inventory file from a merchant that provides links.
- The Walmart activation materials: the activation program, workbook/template, launcher details, one safe sample input and output, and one monthly reconciliation example.
- Any examples from the URL upload system (file naming, logs, exports).
- Your current rules, if any, for export passwords, file cleanup, and retention.

Where This Leaves Phase 1
The Phase 1 validation step ensures that we have everything buttoned up, with particular focus on Walmart as it represents 55% of your digital business. I know that there have been ongoing discussions with the Walmart team about what a direct integration might look like (but we didn't scope or price that possibility, and would recommend it as a future phase). I believe that covers your questions. The remaining items are operational choices, and the confirmation list is everything we need to keep things moving!

If you are happy with the above, I can work with Stephanie add some clarifying language in the SOW to share back along with options for ongoing support.

Best,

Spencer
