---
title: Adversarial review — DESIGN-QA-REPORT.md
date: 2026-08-11
reviewer: AUR2 Prime (Grok)
subject: docs/runs/2026-08-10-design-dev-reconcile/DESIGN-QA-REPORT.md
status: PASS with minor notes — safe to drive backlog v2
---

# Adversarial review of design-QA report

## Verdict

**PASS (with minor notes).**  
The report is stronger than PRIORITIZED-BACKLOG v1: live Figma Screens node ids, live staging fixtures (`PGC-1026` / `PGC-1027`), code loci, and an explicit “already close / don’t re-do” list. It **independently confirms** the adversarial FAIL on v1 (Paid-is-blue wrong; filters already exist; Design Direction pollution avoided).

Safe to use as the **engineering source of truth** for Tim/Codex slices. Still not a BugHerd dump — file GitLab/Codex work from backlog v2.

---

## What the report gets right (high confidence)

| Claim | Cross-check |
| --- | --- |
| Staging close on shell, orders list, filters, non-Walmart detail, vault, tokens | Matches morning sync + code; avoids wasteful rewrite |
| P0: Walmart prep detached → `/card-vault/generation` | Confirmed `page.tsx` “Merchant preparation required” + link; `workflowSteps` has no Preparation stage |
| P0: semantic labels collapsed to Completed / In Progress | Confirmed `format.ts` + `getPaymentPill` / `getOrderStatusPill` |
| Paid is green, not blue | Confirmed staging diagnosis; matches adversarial C1 |
| Filters already have 4 categories | Confirmed adversarial C2; close as implemented |
| Post-allocation export builders ≠ pre-allocation Walmart work file | Confirmed `merchant-output-export.ts` / `vendor-work-files.ts` require allocations — critical build constraint |
| Reuse import mutation, don’t rebuild | Sound; `generation/actions.ts` already has validation/import path |
| Figma Walmart copy may overclaim Fiserv handoff | Correctly subordinated to product boundary (prepare / external activate / import) |

---

## Attacks that did not land (report holds)

1. **“Too narrow — ignoring design investment”** — No: P0s are operator-critical; P1s are small; “already close” protects design work already in staging rather than discarding it.  
2. **“Inline prep over-prescribes Tim”** — Report offers least-context-loss inline step but keeps shared services + batch route; aligns with Spencer soft edge (step on order; generation complexity may nest). Acceptable default for builder; Tim can escalate if blocked.  
3. **“Missing visual evidence”** — Live Figma screenshots + logged-in Chrome staging cited; no `.blocked`. Accept as recon evidence for engineering (not a design pixel audit of every secondary page).

---

## Minor notes (do not block v2)

| # | Note | Impact |
| --- | --- | --- |
| N1 | Search copy is literally `Search requests, customers, status, or merchant` (not only “Search requests…”) | Language slice still valid; use exact string |
| N2 | Generation page **title** is already “Card Preparation”; residual “Generate Cards” is mainly **vault list CTA** (`card-vault/page.tsx`) plus some generate-test chrome | Language slice: target CTA/nav, not assume whole page is wrong |
| N3 | Report does not re-score SOW budget hours | Spencer still gates Tim shape risk on Walmart work-file builder |
| N4 | No independent second-eyes staging re-walk by Prime | Accept Codex recon; optional Spencer 2-min click on `PGC-1027` before builder starts |

---

## Gate comparison: pack v1 vs report

| Gate item (ADVERSARIAL-REVIEW) | Report |
| --- | --- |
| C1 Paid blue misdiagnosis | **Fixed diagnosis** — green + semantic labels |
| C2 Filters overstated | **Closed** — already implemented |
| C3 Walmart rewrite needed | **Strengthened** with workflow step + work-file contract warning |
| C4 Design Direction pollution | **Avoided** — Screens nodes only |
| C5 No visual QA | **Satisfied** for primary routes |
| C6 Budget posture | Still implicit; v2 keeps only 2 P0 + small P1 |

---

## Allowed next actions

| Action | Allowed? |
| --- | --- |
| Write PRIORITIZED-BACKLOG **v2** from report | **Yes** |
| Hand Tim v2 as execute list | **Yes** (after Spencer skim optional) |
| File BugHerd for every gap | **No** — engineering tickets / Codex lanes first |
| Broad shell/token/vault table rebuild | **No** — report closes those |

## Disallowed without new evidence

- Re-opening “Paid is blue” color rewrite  
- Rebuilding Orders filter from scratch  
- Implementing Design Direction historical comments as scope  
- Treating Figma Walmart “taken to Fiserv” copy as product truth  

---

## Bottom line

Report is **on-target and actionable**. Drive **backlog v2** and builder order from it. Keep adversarial bar on **implementation PRs** (especially Walmart work-file builder vs post-allocation export reuse).
