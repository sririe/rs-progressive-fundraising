---
title: "Phase 1 SOW Amendment Plan — post 6/23 Digital Fulfillment Sync"
type: plan
category: statement-of-work
date: 2026-06-29
status: draft-for-review
tags:
  - progressive
  - sow
  - amendment
  - secure-card-vault
  - normalization
participants:
  redstamp:
    - Spencer Ririe
    - Tim Lemke
    - Stephanie Lamon
  progressive:
    - Doug Beers
    - Lloyd Scrubb
sources:
  live_sow_doc: "1CIugJL3zGlP_ORJX9iEBt0JXTh_WUaeW2H-9WTDWxQE (Redstamp Clients [Internal] → Progiftcards.ca → _Client Level Agreements)"
  transcript: projects/gift-cards/docs/discovery/2026-06-23-digital-fulfillment-sync-transcript.md
  notes: projects/gift-cards/docs/discovery/2026-06-23-digital-fulfillment-sync-notes.md
  reconciliation: projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md
  design_note: projects/gift-cards/docs/plans/2026-06-18-phase1-vault-normalization-design-note.md
---

# Phase 1 SOW Amendment Plan

## What Doug actually asked for (6/23 transcript, lines 523–541)

- **One deliverable: a modified SOW with every change highlighted in yellow.** Spencer committed
  to it verbatim; Doug confirmed ("Just give us the best modified statement of work. You can yellow
  highlight, which is good").
- **Doug explicitly waved off the companion Q&A doc** Spencer floated ("don't worry about dealing
  with every question… just give us the best modified SOW"). → **Drop the Q&A companion.**
- **Lloyd wants to see the workflows** (source file → vault → output) for ~6 common merchants.
  → **Merchant-flow diagram system: deferred per Spencer; follow-up after the SOW.** Referenced in
  the SOW as a forthcoming companion, not built into it.

## Mechanics

1. `gog docs copy 1CIugJL… "Progressive Fundraising — Secure Card Vault & Fulfillment Tool — SOW (v2 — Amended 2026-06-29)"`
   into the same `_Client Level Agreements` folder. **v1 (`1CIugJL…`) stays untouched.**
2. Apply the edits below to the copy via `gog docs find-replace` / `insert`.
3. Yellow-highlight every changed/new run: `gog docs format <copy> --match "<text>" --match-all --bg-color "#FFFF00"`.
4. Verify by re-export + visual check before handing the link to Spencer.

## Base-state finding (important)

The live doc is the **May 29 version — original scope + Redstamp standard boilerplate. NONE of the
6/10 reconciliation deltas (D-1…D-15) were ever applied.** `Benji Pays` is already correct;
`SystemOne replacement` is still wrong. So this amendment folds in **two layers**: the unapplied
6/10 backlog **and** the new 6/23 clarifications. The 6/23 meeting *validated* the normalization
direction rather than contradicting it — low risk.

---

## Amendment edits (each → yellow highlight)

| # | SOW section | Change | Source |
|---|---|---|---|
| A1 | Header | `Date: May 29, 2026` → send date; refresh "valid for 30 days" anchor. | housekeeping |
| A2 | §01 Project Overview | Add one paragraph: the vault **normalizes all incoming inventory to a single canonical card record** regardless of merchant/source; operators see one uniform workflow. Sets up the whole amendment. | 6/23 L60–89, 224–262 |
| A3 | §02 Project Setup → **rename "Phase 1A: Fulfillment Source Validation & Merchant Configuration"** | Keep bullets; add named outputs (active-merchant list, included credential-pattern list, one acceptance example per pattern, documented exclusions) + sentence: *"Implementation of merchant-specific outputs depends on completion of this milestone."* Add a **test-import-per-merchant** bullet. | D-1; 6/23 L251–260, 276–283 |
| A4 | §02 Digital Card Vault & Inventory Mgmt | Add canonical-record bullets: normalized schema (merchant/brand, supplier/source system, credential, recipient name/email where present, customer, order ref, invoice ref, date, status, **provenance**: import batch/file/row); status set incl. **quarantined / need-replacement / voided**; **import mapping-verification UI** (source columns → vault fields, accept/adjust before commit). | 6/23 L74–78, 226–231, 276–283 |
| A5 | §02 Merchant-Specific Fulfillment (**the big one**) | Replace generic "agreed Phase 1 merchant fulfillment patterns" with the **credential-pattern model**: Amazon = claim-code; CashStar (most) = URL + secret/challenge; URL-only (Fairmont/Winners); URL + account + PIN (PC/Loblaws); Chapters = numbers → barcode/art. State the three-tier trigger precisely (N-4, refined 6/29 per Spencer): (1) **vendor column/format drift** of an existing merchant → import-mapping step, **no work**; (2) **new merchant fitting an existing pattern** → light back-end setup + an **end-to-end validation pass before rollout** (new-vendor inventory configured/validated with Redstamp before loading, not imported cold) → handled under the **ongoing Support & Maintenance Agreement**, *not* a change order; (3) **genuinely new credential type** → change order. | D-2; 6/23 L82–89, 202–203, 379–413; 6/29 Spencer |
| A6 | §02 Merchant-Specific Fulfillment — Walmart ¶ (**correction**) | Rewrite to **on-demand**, not stored-inactive-inventory: Walmart has **no pre-stored inventory**; activation+inquiry is combined. Flow: order → vault prepares the Fiserv activation work file → Progressive runs activation externally → **live cards ingested back into the vault** → allocated/packaged with the rest of the order → output generated. | D-3 (corrected); 6/23 L116–159, 458–464 |
| A7 | §02 Merchant-Specific Fulfillment — output ¶ | **Server-side** PDF/barcode generation for merchants with no card artifact (Amazon, Walmart, Chapters); minimized where pass-through suffices (one fewer break point); can produce a Progiftcards-branded card carrying the vendor logo. | 6/23 L326–365, 395–413 |
| A8 | §02 Production Application Foundation | Add **managed-cloud hosting — named as Render (render.com)**, the platform Tim's staging build already runs on (web service + Postgres; staging on free tier, production paid — Render Postgres ~$6/mo USD + a paid web service). Framed as current platform, monthly pass-through, exact totals confirmed near production. **Approximate cost added per Stephanie's 6/29 review:** ~USD $25/mo Render Pro (+ compute) + ~USD $6/mo card-vault DB, loosely worded (USD flagged distinct from the CAD project fee). No specific SLA committed. *(Roles + Redstamp break-glass + no-in-browser-reveal: still deferred to 2nd pass — see below.)* | N-1; 6/23 L469–498; render.yaml; 6/29 Stephanie |
| A9 | §02 Fulfillment Request Workflow | Add **invalid-card workflow**: quarantine with reason, allocate replacement if inventory exists else need-replacement state; invalid cards never return to available. | D-8; 6/23 L75–76 |
| A10 | §04 Assumptions | Add: source-material package itemized at kickoff (formats without materials → change order); **managed hosting is a monthly client pass-through cost**; **System Bind remains in place for V1** (URL generation / asset hosting). | D-9; N-1; N-2; 6/23 L491–521 |
| A11 | §06 Out of Scope | Fix **`SystemOne replacement` → `System Bind replacement` (V1 keeps System Bind; consolidation assessed post-V1)**; add **Walmart/Fiserv activation execution**; add **Walmart direct API integration (future)**; add **in-browser reveal of full card values**; add **ongoing staff onboarding beyond initial training**. | D-10; N-2; N-7; 6/23 L465–468, 436–438 |
| A12 | §06 / closing | Forward reference: a separate **Support Agreement** (post-launch monitoring, format-drift support, Nov–Dec peak response) proposed before launch. | D-12 |
| A13 | §02 Migration, Training & Launch | Specify training package: one 60–90 min guided session + written SOP + supervised staging practice across the credential patterns incl. inventory-short and invalid-card scenarios, for 3+ nominated staff; acceptance = trained staff complete agreed test orders without developer help. | D-11 |

---

## Open decisions / blockers (need Spencer ± Tim before send)

1. **D-15 export-password mechanism — STILL UNRESOLVED.** Not solved on the call. The shown-once
   password breaks on multi-file orders. Complication: **System Bind stays for V1 and currently does
   the ZIP/URL generation + hosting** (L507–521), so the vault may *not* own export-file protection in
   V1 at all. **Decision needed:** does V1 (a) keep System Bind's existing password/ZIP path as-is, or
   (b) have the vault generate password-protected exports? This determines whether A-edits touch export
   protection or leave it to System Bind. **Recommend (a) for V1** — leave the protection path with
   System Bind, defer the vault-owned export-password redesign — consistent with "don't rock that boat
   until the vault works."
2. **Timeline** — Spencer owes a Tim sync (Tim on vacation next week) before committing dates. Doug
   wants it live before the **October peak/blackout**. **Recommend: keep 6–8 weeks, add an explicit
   "targeting completion ahead of the October peak season" line, finalize dates post-Tim-sync.**
3. **Send date / "valid for 30 days"** — Spencer told Doug he'd check back Thu (≈ 7/2). Confirm the
   date to stamp.
4. **D-7 role names** — resolved 6/23 in the status doc (Admin = Doug + Elena; Operations = new hire,
   Lisa, Lloyd). Confirm whether to **name** them in the client SOW or keep role-generic.

## Deferred (per Spencer, 6/29)

- **Merchant-flow diagram system** (5–6 common merchants: source → vault mapping → output). Lloyd
  wants these; build as a companion after the SOW. SOW will reference it as forthcoming.
