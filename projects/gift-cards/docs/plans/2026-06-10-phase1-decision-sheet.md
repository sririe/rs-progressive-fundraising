---
title: "Phase 1 Decision Sheet — Confirm or Override"
type: plan
category: internal-alignment
date: 2026-06-10
status: partially-ratified
ratification_note: "Spencer ratified D-1 (with staffing-agnostic caveat), D-2, D-4 through D-12, and T-1 via Proof comments on 2026-06-10 (doc f7n13d69). Still open: D-3, D-13, D-14, and new D-15 (export password handling)."
tags:
  - progressive
  - sow
  - decisions
  - secure-card-vault
related:
  - projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md
  - projects/gift-cards/docs/plans/2026-06-10-doug-reply-draft.md
---

# Phase 1 Decision Sheet

*Every genuine decision from Doug's 12 questions and Tim's draft responses, with a recommended default. Confirm or override each line; nothing else is blocking.*

## Ours (Spencer confirms; Tim's doc gets updated to match)

| # | Decision | Recommended default | Why |
|---|---|---|---|
| D-1 ✅ | Merchant format allowance | **4 format families:** standard URL/code export (long tail), Amazon PDF/ZIP, Loblaws/Shoppers (validated in 1A), Walmart prep + import | Covers 90% of volume by name plus a workflow for the other 19 storefront brands. **Caveat (Spencer):** keep all scope/acceptance language staffing-agnostic — Mario's tenure is uncertain; say "Progressive office staff," never a named operator. |
| D-2 ✅ | Walmart boundary | **Work-file prep + controlled import of activated results in; direct Fiserv activation out** unless separately validated | We have zero Walmart activation assets in hand; import closes the loop without promising what we can't inspect. |
| D-3 | Amazon V1 output | **PDF/ZIP standard;** URL spreadsheet only if SystemOne fixtures arrive in 1A | PDF/ZIP is the best-evidenced workflow; the URL path runs through unvalidated SystemOne. |
| D-4 ✅ | Phase 1A validation milestone | **Add as the named first milestone inside the fixed fee** (recast of existing Week 1 production planning — no fee/timeline change) | Converts every evidence gap into scheduled work instead of silent assumptions. |
| D-5 ✅ | Export protection | **Vault generates password-protected/encrypted exports** (replaces `make-zip.ps1`); post-download handling stays Progressive's | Doug asked for "password ZIP" because that's today's customer expectation; pushing it post-download re-creates a manual technical step. |
| D-6 ✅ | In-browser reveal | **Prohibited in Phase 1** — sensitive values exist only in audited, role-restricted downloads | Smaller attack surface and a complete access log by construction; also collapses the view-vs-download permission question. |
| D-7 ✅ | Redstamp access to card data | **None by default;** logged break-glass support path requiring per-incident written approval from Progressive | The liability answer Gord will want before anyone asks. |
| D-8 ✅ | Format revision rounds | **1 consolidated revision round per merchant format** after acceptance-example approval; further changes = CO/support | Matches existing SOW Assumption 17; gives Doug a concrete number for Q3. |
| D-9 ✅ | Invalid-card scope | **Replacement workflow in; merchant credit/reconciliation tracking out** (note field only) | Reconciliation is a merchant-side process we have no documentation for. |
| D-10 ✅ | Fallback intake | **Declare it in scope** — manual admin entry is already an unconditional deliverable; CSV-assisted import is the structured fallback | Zero marginal cost; kills the open question. |
| D-11 ✅ | Support model | **Propose a separate monthly support retainer with the revised SOW:** defined hours, peak-season (Nov–Dec) priority SLA, emergency work at Agency Rate; no number in the Q&A reply | Cash-equivalent system + 60% seasonal concentration makes ad-hoc hourly risky for both sides; pricing belongs in its own proposal. |
| D-12 ✅ | Training boundary | **Initial training + train-the-trainer materials in the build; ongoing onboarding via support agreement** | Keeps the fixed fee bounded while answering Doug's key-person-risk goal. |
| D-13 | Hourly rate in SOW | **$160 CAD/hr** (matches the most recent executed Progressive SOW); update CLIENT.md to match | Fixed fee is unchanged either way — rate only governs overages/holds; if you prefer the $150 relationship rate, only D-13 changes. |
| D-14 | Payment schedule | **Keep 40/40/20** (kickoff / working V1 / launch) | Mid-build milestone gives Doug a natural review gate on a 6–8 week build; no reason to renegotiate. |
| D-15 *(new, from Spencer's Proof comment on Q7)* | Export password handling | **Vault generates a random per-export password and displays it once to the authorized operator; password travels by the existing separate-email practice (never in the filename, which is today's anti-pattern); a lost/compromised password = re-export with a new password, fully logged — there is no password-stripping workflow because files are disposable and the vault is the system of record** | Answers "how does the password reach the customer" and "how do you un-password a file" in one model; the no-passwords-at-all answer is the deferred secure delivery portal (Phase 2/3). |

## Theirs (we propose the default in the reply; Doug confirms)

| # | Decision | Default we propose to Doug | Why |
|---|---|---|---|
| T-1 ✅ | Acceptance definition | Trained, authorized staff (3+ nominated) complete agreed test orders without developer help — not literally "anyone, no training" | Honest version of his own goal; protects both sides at acceptance. |
| T-2 | Walmart manual import | Controlled import of activated results is acceptable for V1 | Direct activation can't be scoped until the Fiserv assets are reviewed. |
| T-3 | Roles & access | Doug names Admin/Operations/Finance/Viewer staff; approves masked-UI / export-only model | Policy is theirs to own; the system enforces it. |
| T-4 | Post-download policy | Doug approves storage, password channel, retention/deletion rules | The vault can't control files after download; the policy makes that boundary real. |
| T-5 | Support model selection | Doug picks from the support proposal (retainer recommended) | His Q10; our recommendation, his budget call. |
| T-6 | Fixture package | Lloyd/Doug deliver the consolidated checklist (folder dump fine) during Phase 1A | The single unblocker — the April 27 request was drafted but never sent. |

*James context (Spencer, 2026-06-10): believed to be Doug's son-in-law, joined as an advisor; engineering background (not software) and technical; primarily there to support Doug and give him confidence. Implication: write the responses for reassurance and concreteness, not depth — confirm role/title on the next call.*
