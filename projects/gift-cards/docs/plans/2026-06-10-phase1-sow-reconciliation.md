---
title: "Phase 1 SOW Reconciliation — Doug's Questions × Tim's Responses × Evidence"
type: plan
category: internal-alignment
date: 2026-06-10
status: draft
tags:
  - progressive
  - sow
  - reconciliation
  - secure-card-vault
  - client-questions
key_insights:
  - Tim's Proof responses and the June 8 unblocker posture agree on direction for all 12 questions; the divergences are about confidence framing, not substance.
  - Six cross-cutting gaps in Tim's draft need fixing before the responses go back to Doug — most importantly the missing Phase 1A validation milestone and the export password-protection ownership question.
  - Only ~6 of the 20 open "Decision needed" items are genuine decisions; the rest collapse into recommended defaults.
related:
  - projects/gift-cards/docs/plans/2026-06-08-phase-1-sow-build-plan-unblocker.md
  - projects/gift-cards/docs/plans/2026-06-08-sow-merchant-evidence-inventory.md
  - projects/gift-cards/docs/plans/2026-05-27-progressive-secure-card-vault-sow-draft.md
  - projects/gift-cards/docs/discovery/2026-06-08-private-lloyd-materials-inventory.md
  - projects/gift-cards/docs/plans/2026-06-10-phase1-decision-sheet.md
  - projects/gift-cards/docs/plans/2026-06-10-doug-reply-draft.md
participants:
  redstamp:
    - Spencer Ririe
    - Tim Lemke
  progressive:
    - Doug Beers
    - James (role unconfirmed)
    - Lloyd S.
status_note: "Doug's 12 questions arrived June 5 (RE: Reschedule Needed-Phase 1 Proposal). Spencer sent a holding reply June 8 promising a detailed response. Tim's draft responses live in Proof doc 26niwbyj."
---

# Phase 1 SOW Reconciliation

**Sources reconciled:** Doug's June 5 email (12 questions; sales mix 55% Walmart / 22% Loblaws / 13% Amazon / 10% other; 60% of sales in Nov–Dec), Tim's Proof draft responses (rev 32), the June 8 unblocker brief, the June 8 merchant evidence inventory, and the May 27 SOW draft.

**Verdict legend:**
- **ANSWER-NOW** — Tim's position is supported by evidence; tighten language and send.
- **VALIDATE-FRAME** — right direction, but the answer must be framed around the Phase 1A validation milestone because the supporting fixtures are not in hand.
- **DECISION** — a genuine choice for Spencer (ours) or Progressive (theirs); recommended defaults are in the decision sheet.

## A. Reconciliation Matrix

| # | Doug's question | Tim's position | Evidence / unblocker posture | Verdict |
|---|---|---|---|---|
| 1 | What counts as customer-ready file creation for Walmart / Loblaws / Amazon? | Per-merchant definitions: Walmart = prepare activation work file, activation stays external, activated results imported back; Loblaws = approved URL spreadsheet; Amazon = claim-code/serial output as PDF/ZIP or URL spreadsheet. | Matches unblocker Exposure 1 almost verbatim. But Loblaws is stated flatly while evidence says the Loblaws format is *ambiguous* (older generated/branded flow vs. newer plain-URL inventory) and must be validated. Amazon URL-spreadsheet path depends on SystemOne, which is unvalidated. | **VALIDATE-FRAME** + 2 decisions (Walmart boundary → D2; Amazon output → D3) |
| 2 | Which merchant formats are included by name? | Walmart Digital, Loblaws Digital, Amazon Digital; all others generic CSV/export "unless separately scoped" (left as open decision). | Unblocker recommends a *bounded allowance of four format families* including the standard URL/code workflow for the long tail as an affirmative inclusion — Mario still has to fulfill the other 19 storefront brands. Tim leaves the long tail as an open question; evidence says it's a day-one operational requirement. | **ANSWER-NOW** with bounded-allowance language (count decision → D1) |
| 3 | How many format changes before change orders apply? | One approved format per named merchant + reasonable review pass; later drift = CO or support. | Consistent with unblocker and with SOW draft Assumption 17 (one consolidated feedback round per milestone). Just needs a number. | **DECISION** (revision rounds → D8) |
| 4 | Fallback intake if WordPress/Formidable handoff isn't clean? | Manual admin entry or structured CSV import; open decision whether fallback is in launch readiness or just documented. | Manual/admin request creation is *already an unconditional Phase 1 deliverable* in the May 27 draft. The fallback is in scope by construction — the open decision dissolves. | **ANSWER-NOW** (default: included; → D10) |
| 5 | Who can decrypt/view full card values? | Admin + Operations only, via export download; UI masked; Finance/Viewer no. Open: view vs. download as separate permissions. | Matches unblocker security defaults. Gap: Tim never addresses **Redstamp's own access** — the unblocker explicitly raises break-glass access, and Gord will ask. View-vs-download collapses if Q6's no-reveal default is adopted. | **ANSWER-NOW** + decision (Redstamp access → D7) |
| 6 | Audit log for *viewing* sensitive data, not just allocation/export? | Full values only decrypted at download boundaries; downloads + workflow actions audited. Open: prohibit in-browser reveal entirely? | Unblocker says log every sensitive view/reveal/export. Tim's design sidesteps elegantly: if there is no reveal, the download log *is* the complete access log. Strongest possible answer for a cash-equivalent system. | **DECISION** (prohibit reveal — recommend yes → D6) |
| 7 | How are exported files secured: password ZIP, expiry, access logging, deletion? | Vault records export metadata, stores no file copies; after download Progressive is responsible for storage, "applying any required password protection," delivery, deletion. | **Plain divergence.** Doug asked about "password ZIP" because today's customer-ready files ARE password-protected (Lloyd's `make-zip.ps1` / encrypted Excel). Tim's draft reads as if Progressive applies protection *after* download — which would leave staff a manual encryption step and break the no-scripts promise. The vault should generate password-protected exports; post-download handling stays with Progressive. Portal deferral is aligned. | **DECISION** (export protection ownership → D5) |
| 8 | What if an allocated card is invalid / inactive / wrong balance? | Quarantine with reason; allocate replacement if inventory exists, else needs-replacement state; invalid card never returns to available. Open: also track merchant credit/reconciliation? | Sound, and absent from the May 27 SOW draft — needs a scope bullet. Merchant-side reconciliation is process we can't validate (no merchant docs in hand); keep it a note field, not a workflow. | **ANSWER-NOW** + minor decision (→ D9) |
| 9 | Is Walmart activation documented/tracked, or partly supported by generated outputs? | Partly supported: vault generates the Fiserv-compatible work file once Progressive provides input/output requirements; running/replacing the Java activation is separate scope. Open: is activation-result import also required? | Tim's own Q1 answer already includes activation-result import — the Q9 open decision is answered by his Q1 posture. Unblocker agrees: prep + manual handoff + post-activation capture/import *where feasible*; everything conditioned on the missing Walmart assets (.jar, workbook, samples). | **VALIDATE-FRAME** (boundary decision folds into D2) |
| 10 | Recommended support agreement; emergency cost in Nov/Dec (60% of sales)? | Support strongly recommended (monitoring, backups, priority fixes, format drift, peak response). Open: retainer vs. prepaid block vs. hourly + emergency rate. | No evidence conflict — this was always going to be a commercial decision. Don't quote an emergency number in the Q&A reply; commit to a support proposal delivered alongside the revised SOW. | **DECISION** (support model → D11) |
| 11 | What training level do ordinary office staff need? | 60–90 min guided session + written SOP + supervised staging practice across Walmart/Loblaws/Amazon/inventory-short/invalid-card scenarios. Open: initial training only, or ongoing onboarding? | Matches May 27 draft (training, handoff docs, launch support). Boundary default: initial training + train-the-trainer materials in the build; ongoing onboarding belongs to the support agreement. | **ANSWER-NOW** (boundary → D12) |
| 12 | Acceptance criteria for "anyone in the office can fulfill"? | Trained, authorized staff complete the approved workflow in staging without scripts/dev help, including exception scenarios. Open: confirm "trained staff," not literally everyone. | Near-verbatim match with the unblocker's acceptance recommendation. The "decision" is client expectation-setting — handle in the reply, get Doug's nod. | **ANSWER-NOW** (theirs to confirm → T1) |

## Cross-Cutting Divergences (Tim's draft vs. evidence posture)

1. **No Phase 1A validation milestone anywhere in Tim's doc.** Tim conditions each answer on "Progressive provides known-good examples," but never names the milestone that collects them. The unblocker's central move — *Phase 1A: Fulfillment Source Validation and Merchant Configuration* as the first scheduled milestone inside the fixed fee — should anchor the reconciled responses. It converts every scattered ask into one scheduled work item and answers Doug's Q1–Q3 honestly without over-promising.
2. **Loblaws confidence overstated.** Tim states the Loblaws output flatly; evidence points two directions (legacy generated format vs. newer URL inventory). Reconciled language: Loblaws/Shoppers is a *priority format validated in Phase 1A*, and whether Shoppers shares the Loblaws format family must be confirmed, not assumed.
3. **Long-tail merchants under-served.** Doug asked only about the big three, but the storefront exposes 22 digital brands and Mario must fulfill all of them. The standard URL/code export workflow should be affirmatively *in* (it is format family #1 of 4), not left as an open client decision.
4. **Export password protection ownership.** See Q7 above — the single sharpest divergence. Resolve before the responses go back.
5. **Redstamp access is unaddressed.** Add the break-glass position (no raw-card access by default; per-incident written approval; logged) — this is a Gord question waiting to happen.
6. **The fixture package never appears.** Tim's per-question asks are scattered and incomplete; none mention `utilities.py`, `make-zip.ps1`, the Amazon SVG template, the Walmart activation assets, or SystemOne samples — the exact items the June 8 source-trail work identified as the unblocker (April 27 fixture request drafted, never sent). Appendix C below is the single consolidated ask.

Also noted: Doug's June 5 email introduces **James** as a technical reviewer alongside Lloyd. We don't know who James is. The reply should welcome him into the walkthrough call; identify his role before that call.

## C. Consolidated Ask — What We Need From Progressive / Lloyd

*Single checklist replacing the per-question asks scattered through the Proof doc. Framing for the client: "a folder dump is fine — we'll sort and inventory it."*

**Files (the fixture package — most from Lloyd):**
- [ ] `utilities.py` (imported by the Amazon generator)
- [ ] `make-zip.ps1` (password-protected ZIP creation)
- [ ] `amazon-e-giftcard-template.svg` (+ any helper files the generator expects)
- [ ] Merchant workbook templates under `orders/<merchant>/template/` (all merchants, not just Amazon)
- [ ] One representative invoice PDF
- [ ] One populated Amazon workbook with safe/fake card data + the known-good output folder it produced
- [ ] One representative URL-inventory file for a pass-through merchant (e.g., Loblaws current, Petro-Canada)
- [ ] Walmart activation assets: `walmart-giftcard-virtual-activation-production.jar`, activation workbook/template, launcher/PowerShell details, one safe sample input + output, one reconciliation workbook example
- [ ] SystemOne (ecard.proegiftcards.ca) samples: upload ZIP naming, log/export examples, URL format, any API notes
- [ ] Examples of successful AND failed Walmart activation results

**Lists and confirmations (Doug/Mario):**
- [ ] Current active digital merchant list (which of the 22 storefront brands are actually sold today)
- [ ] Current digital fulfillment folder list (which merchants Progressive actually fulfills)
- [ ] Whether all Loblaws banners (Superstore/PC/No Frills/Extra Foods/Provigo) share one format, and whether Shoppers shares it
- [ ] Whether Walmart, Loblaws, or Amazon have multiple active output variants today
- [ ] Current rules (if any) for export passwords, file cleanup, retention

**Decisions (Doug — defaults proposed in our reply):**
- [ ] Confirm controlled manual import of activated Walmart results is acceptable for V1
- [ ] Confirm Amazon V1 delivery format (we propose PDF/ZIP standard)
- [ ] Name staff for Admin / Operations / Finance / Viewer roles
- [ ] Approve the post-download file handling policy (storage, password channel, retention/deletion)
- [ ] Nominate 3+ staff for training and acceptance testing; confirm acceptance = trained, authorized staff
- [ ] Select support model from the proposal we'll include with the revised SOW

## D. SOW Delta List (language-level edits to the 2026-05-27 draft)

| # | Section | Edit |
|---|---|---|
| D-1 | §02 Project Setup and Production Planning | Recast as **"Phase 1A: Fulfillment Source Validation and Merchant Configuration"** — keep existing bullets, add named outputs (active digital merchant list, included Phase 1 format list, acceptance example per format, documented exclusions) and the sentence: *"Implementation of merchant-specific outputs depends on completion of this milestone."* No timeline change (this is Week 1). |
| D-2 | §02 Merchant-Specific Fulfillment, ¶1 | Replace "the agreed Phase 1 merchant fulfillment patterns" with the bounded allowance: *"up to four validated merchant output format families: (1) standard URL/code export for merchant-provided inventory, (2) Amazon generated PDF/ZIP, (3) the validated Loblaws/Shoppers format, (4) Walmart work-file preparation and activation-result import."* |
| D-3 | §02 Merchant-Specific Fulfillment, Walmart ¶ | Replace the current hedge with the affirmative boundary: *"Phase 1 will support Walmart order tracking, status visibility, manual activation handoff, preparation of the approved Walmart/Fiserv activation work file, controlled import of activated card results, customer-ready file preparation, and fulfillment activity history. Automated Walmart/Fiserv activation, portal automation, balance lookup, and monthly reconciliation automation are excluded unless separately validated and approved."* |
| D-4 | §02 Merchant-Specific Fulfillment | Add the validated-output-class definition: *"Customer-ready files are the agreed encrypted Excel, password-protected ZIP/PDF, or URL/code export formats used to deliver allocated cards. Each included format must be backed by a current template, sample inventory/input, and known-good output example supplied by Progressive."* |
| D-5 | §02 + Assumption 15 | State that **the vault generates password-protected/encrypted export files** (replacing the manual `make-zip.ps1` step), records export history, and stores no plain file copies; Assumption 15's post-download responsibility language stands unchanged after that point. |
| D-6 | §02 Production Application Foundation | Add: *"Full card values are not displayed in the browser in Phase 1; sensitive values are accessible only through audited, role-restricted export downloads."* (pending decision sheet ratification). |
| D-7 | §02 Production Application Foundation | Name the four roles (Admin, Operations, Finance, Viewer) and add the Redstamp access posture: no Redstamp access to decrypted card data in production except a logged, per-incident support path approved in writing by Progressive. |
| D-8 | §02 Fulfillment Request Workflow + Deliverables | Add the invalid-card workflow bullet: quarantine with reason, replacement allocation, needs-replacement state, merchant-credit note field; invalid cards never return to available inventory. |
| D-9 | §04 Assumptions | Add: *"Progressive will provide the source-material package itemized at kickoff (scripts, templates, sample inputs, known-good outputs, Walmart activation materials, SystemOne examples). Merchant formats for which materials are not provided will be implemented through a change order once materials are available."* |
| D-10 | §06 Out of Scope | Add: SystemOne API integration (draft only lists "replacement"); Walmart/Fiserv activation execution (make Fiserv explicit); in-browser reveal of full card values; ongoing staff onboarding beyond initial training. |
| D-11 | §02 Migration, Training, and Launch | Specify the training package: one 60–90 minute guided session, a written operating procedure, supervised staging practice covering the four format families plus inventory-short and invalid-card scenarios, for 3+ Progressive-nominated staff. Add the acceptance sentence (trained, authorized staff complete agreed test orders without developer support). |
| D-12 | §06 / closing | Add forward reference: *"A separate Support Agreement covering post-launch monitoring, merchant format changes, and peak-season (November–December) response will be proposed before launch."* |
| D-13 | §07 Project Terms | Resolve the rate: draft says $160/hr; CLIENT.md says $150/hr. Decision sheet item — fee ($32,000) unchanged either way. |
| D-14 | §06 Out of Scope | Fix "BenjaPay" → "Benji Pays" (per CLIENT.md / repo convention). |

*Note: REDSTAMP-SOW-EXAMPLES.md was not re-read for this pass — the May 27 draft was already calibrated against it, and these are language-level deltas, not a re-draft.*
