---
title: "Phase 1 Technical Responses — Client-Facing Document for Doug"
type: plan
category: client-deliverable
date: 2026-06-10
status: draft
tags:
  - progressive
  - phase-1
  - secure-card-vault
  - client-questions
  - technical-responses
key_decisions:
  - Supersedes the plan to edit Tim's Proof doc (26niwbyj) in place — Spencer is sending responses directly to Doug.
  - Bakes in all ratified decisions (D-1 through D-12 as ratified, T-1) plus recommended defaults for D-3 (Amazon PDF/ZIP) and D-15 (export password model), flagged below for Spencer's review.
related:
  - projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md
  - projects/gift-cards/docs/plans/2026-06-10-phase1-decision-sheet.md
  - projects/gift-cards/docs/plans/2026-06-10-doug-reply-draft.md
---

# Internal Review Notes — Remove Before Sending

- **D-3 and D-15 defaults are baked in** (Amazon PDF/ZIP as the Phase 1 standard in Q1; the per-export password model in Q7). If you override either, those two answers change.
- **No pricing or rates appear in this document** by design — fee, rate (D-13), and payment schedule (D-14) belong to the revised SOW; the support proposal carries its own pricing.
- **Tim's Proof doc (26niwbyj) is superseded by this version.** It diverges from his draft in six places (the validation milestone, Loblaws confidence framing, the long-tail standard format, export password ownership, Redstamp access, and the consolidated ask). Your call whether Tim gets a pass over this before it goes out.
- **Staffing-agnostic language applied throughout** — no named operators; "your current activation process" rather than naming who runs it.
- Send as PDF attachment or paste into email per your preference; the companion email draft is `2026-06-10-doug-reply-draft.md`.

---

# Progressive Gift Cards — Phase 1 Secure Card Vault

## Responses to Your Technical Questions

**Prepared for:** Doug Beers, Progressive Fundraising
**From:** Redstamp
**Date:** June 10, 2026

Thanks for these questions — and for the sales mix numbers, which shaped the answers. With roughly 90% of digital volume on Walmart, Loblaws, and Amazon, Phase 1 names those three merchants specifically, and adds a standard workflow that covers the rest of your digital catalog from day one.

Two things to know before the individual answers:

**Phase 1 starts with a validation step.** The first project milestone confirms each included merchant format against your real materials — current templates, sample inputs, and known-good output files — before we build against it. Where an answer below depends on a file we haven't seen yet, we say so, and confirming it is scheduled work inside the project, not an open promise.

**Phase 1 includes four merchant output formats:**

1. A **standard export format** for merchants that provide URLs or codes — this covers the majority of your digital catalog with one workflow.
2. The **Amazon generated card package** (PDF-per-card, delivered as a ZIP).
3. The **Loblaws/Shoppers format**, confirmed during validation (see Question 1).
4. The **Walmart format**: activation work-file preparation plus import of activated results (see Questions 1 and 9).

Additional merchant-specific formats beyond these are handled through change orders, so the scope you're approving is the scope you get.

---

### 1. What exactly counts as "customer-ready file creation" for Walmart, Loblaws, Amazon?

It means the vault produces the final, password-protected file your customer receives. Staff never copy card numbers, PINs, claim codes, or URLs between spreadsheets, and never run scripts.

- **Walmart:** the vault prepares the activation work file, your current activation process runs exactly as it does today (outside the vault), and the activated card data comes back in through a controlled import. The vault matches the cards to the order, allocates them, and produces the final customer file — with checks against duplicate imports and a record of who imported and verified the results.
- **Loblaws / Shoppers:** the approved spreadsheet of allocated card URLs and order information. One thing we'll confirm during validation: whether your current Loblaws and Shoppers inventory is URL-based or still uses the older generated-card format — we'll implement whichever is actually in use today.
- **Amazon:** the PDF-per-card ZIP package your customers receive today, generated from validated card data and your current template. If you need the hosted-URL delivery option as well, we'll assess that during validation, since it depends on the upload system behind it.

Customer-ready file creation does **not** include emailing files to customers, hosting download links, or tracking whether a customer opened a file. Those are secure-delivery functions that belong to a later phase, and we'd rather scope them honestly than fold them in quietly.

### 2. Which merchant formats are included in Phase 1 by name?

Walmart, Loblaws (including the banner brands — we'll confirm with you which banners share one format, and whether Shoppers does too), and Amazon — plus the standard export format that covers your remaining digital merchants. Every digital order your storefront takes today has a defined fulfillment path in Phase 1: the big three get their named formats, everything else flows through the standard workflow.

### 3. How many merchant format changes are included before change orders apply?

One approved format per included merchant format, with one consolidated revision round after you approve the acceptance example for that format. After approval, merchant-driven format changes, new templates, or additional variants are handled as change orders or under the support agreement — format drift is a real, ongoing cost, and it's better covered by support than hidden in a fixed fee.

### 4. What is the fallback intake method if the WordPress/Formidable handoff is not clean?

Fallback intake is included either way, because manual order entry is a core Phase 1 feature, not a contingency: staff can always create an order directly in the vault, and a structured file import is available as the assisted path. If the website handoff turns out to be messy, fulfillment still works on day one — the handoff affects convenience, not capability.

### 5. Who can decrypt or view full card numbers, PINs, URLs, or access codes?

Phase 1 has four roles: Admin, Operations, Finance, and Viewer. Only Admin and Operations can produce exports containing full card values. Screens show masked values for everyone — see Question 6. You tell us which staff hold which role (it's on the confirmation list at the end).

One thing you didn't ask but should know: **Redstamp has no access to decrypted card data in your production system.** If a support situation ever genuinely requires it, that happens only through a logged break-glass path with your written approval for that specific incident.

### 6. Is there an audit log for viewing sensitive card data, not just allocation/export actions?

Yes — and Phase 1 is designed so the answer is airtight: **full card values never appear on screen.** The only way card data leaves the vault is through an export download by an authorized user, and every export is logged — who, when, and for which order. That means the export log *is* the complete record of sensitive access; there's no separate "viewing" to account for. Allocation, inventory imports, status changes, replacements, and user management are all logged as well.

### 7. How are exported files secured after generation: password ZIP, expiry, access logging, deletion policy?

The vault generates the password-protected file itself — no manual encryption step, no separate tool. The password handling works like this:

- Each export gets its own randomly generated password, shown once to the operator who created it.
- The password travels to the customer separately from the file — the same separate-message practice you use today, with one improvement: the password is never the filename or anything guessable.
- If a password is lost or a file is compromised, staff don't "un-protect" anything — they generate a fresh export with a new password, and the event is logged. Files are disposable; the vault is the system of record.

The vault keeps a full export history (who exported what, when, and whether delivery was confirmed) but does not store copies of the generated files. Once a file is downloaded, it's outside the system — storage, delivery, and deletion follow your file-handling policy, and we'll help you define that policy during the validation step so it's written down rather than tribal knowledge.

The longer-term answer to this whole category — expiring download links, recipient access logs, no passwords at all — is a secure delivery portal, which we've deliberately kept out of Phase 1 and can scope separately when you're ready.

### 8. What happens if an allocated card is later found invalid, inactive, or wrong balance?

The card is quarantined with a written reason and never returns to available inventory. If matching replacement inventory exists, the vault allocates it and the order moves back to a state where a corrected export can be created; if not, the order sits in a clearly visible needs-replacement state until inventory arrives. Every step is logged. Following up with the merchant for credit stays your process outside the vault — the vault carries a note field so the status is visible, but it doesn't pretend to manage a merchant-side process it can't see.

### 9. Is Walmart's activation workflow merely documented/tracked, or partly supported by generated outputs?

Partly supported by generated outputs — the vault prepares the activation work file, tracks the order through the activation handoff, imports the activated results, and produces the final customer file (the same flow described in Question 1).

What Phase 1 deliberately does **not** include is automating the activation step itself. That's a boundary, not an oversight: activation touches cash-equivalent card creation through a third-party system, and we won't commit to automating it before we've reviewed the actual activation materials. Once we have them (they're on the materials list below), we can assess whether direct activation support is worth scoping as its own piece.

### 10. What support agreement is recommended after launch, and what about November/December?

With 60% of your sales in November and December and a system handling cash-equivalent data, we recommend a monthly support agreement starting at launch — covering monitoring, backups, priority bug fixes, merchant format updates, user and access support, and defined peak-season response expectations for November/December.

Rather than quote a one-off emergency rate here, we'll include a concrete support proposal with options and pricing alongside the updated SOW, so you can compare real numbers. Emergency work outside any agreement bills at the agency rate in the SOW.

### 11. What level of training do ordinary office staff need?

Office-operations training, not technical training. The plan: one guided training session (60–90 minutes), a written step-by-step operating procedure, and supervised practice in the staging environment covering normal orders for each included format plus the two exception cases that actually happen — inventory shortages and invalid-card replacement. No PowerShell, no Python, no scripts, no database access.

We'd ask you to nominate at least three staff members for training and acceptance testing, so fulfillment never depends on one person again — which was your stated goal. Initial training and materials are included in the build; onboarding new staff later is covered under the support agreement.

### 12. What are the acceptance criteria for "anyone in the office can fulfill digital cards"?

The honest version of that goal: **trained, authorized staff** — the group you nominate — can each complete agreed test orders end-to-end in staging for every included format, without scripts, developer help, or anyone technical in the room. That includes finding the order, confirming details, updating payment status, allocating inventory, generating the customer-ready export, recording delivery, closing the order, and handling the inventory-short and invalid-card cases. That's the test we pass together before launch.

---

## What We Need From You

One consolidated list — this replaces the scattered per-question asks.

**Confirmations:**

1. Which staff hold Admin, Operations, Finance, and Viewer roles.
2. That a controlled manual import of activated Walmart results is acceptable for this first version.
3. Beyond Amazon, Loblaws, and Shoppers — which one or two other merchants require in-house card generation today.
4. Whether current Loblaws and Shoppers inventory is URL-based or generated, and which banner brands share one format.
5. Whether Browns Social House, Hudsons Bay, and MasterCard are still active digital offerings.
6. Your nominated training and acceptance group (three or more staff).

**Materials** (for the validation step — a raw folder dump is perfect; we'll sort and inventory it):

- The script helper files (`utilities.py`, `make-zip.ps1`) and the Amazon card template (SVG) with any related files.
- The merchant workbook templates used for order generation (all merchants).
- One representative invoice PDF, one populated Amazon workbook with safe/test data, and the known-good output it produced.
- One sample URL-inventory file from a merchant that provides links.
- The Walmart activation materials: the activation program, workbook/template, launcher details, one safe sample input and output, and one monthly reconciliation example.
- Any examples from the URL upload system (file naming, logs, exports).
- Your current rules, if any, for export passwords, file cleanup, and retention.

---

## Where This Leaves Phase 1

The build is realistic and maintainable as scoped: secure order intake, card vault inventory, allocation, validated customer-ready exports, delivery tracking, and a complete audit history — with the validation milestone making sure every merchant format is confirmed against your real materials before the build hardens around it. The remaining items are operational choices (roles, policies, support model) rather than feasibility questions, and the confirmation list above is everything we need to keep moving.
