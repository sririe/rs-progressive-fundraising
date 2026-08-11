---
title: Adversarial review — design↔dev reconcile pack
date: 2026-08-11
reviewer: AUR2 Prime (Grok) — seat-side gate, pre-BugHerd / pre-builder
status: FAIL — do not file BugHerd or treat PRIORITIZED-BACKLOG v1 as executable
subject:
  - SESSION-BRIEF.md
  - PRIORITIZED-BACKLOG.md
  - Figma comment export (94/82)
  - Transcripts (voice 1:1 + morning sync)
  - Code @ progressive-card-vault 6241988
  - Tim style guide docs/application-style-guide.md
---

# Adversarial review (pre-action gate)

**Verdict: FAIL for action.**  
Do **not** leave BugHerd tasks, do **not** hand Tim the v1 backlog as-is, and do **not** treat verbal design complaints as pixel tickets until visual evidence pins surfaces.

This review attacks our own capture for: wrong facts, overclaim, non-actionable tickets, source pollution, and budget/product risk.

---

## Gate criteria (what “actionable” means)

A ticket/item is actionable only if it has:

1. **Pinned surface** — route + Figma frame id (Screens / Design System, not Design Direction history)  
2. **Observable defect** — what is wrong today (screenshot or code citation)  
3. **Desired state** — what correct looks like (token/label/step)  
4. **Severity** — operator impact, not aesthetic preference alone  
5. **Acceptance** — checkable without re-litigating product  

If any of 1–3 is missing → **HOLD**, not BugHerd.

---

## Critical findings (must change the pack)

### C1 · P0-2 “Paid is blue on the list” is likely misdiagnosed

| Claim in backlog v1 | Evidence |
| --- | --- |
| Paid appears blue; design wants green | **Not verified on staging by us.** |

**Code facts (`src/app/fulfillment/page.tsx`, `src/lib/format.ts`):**

- `paymentStatus` `paid` → label **`"Completed"`** (not `"Paid"`)
- `getPaymentPill("Completed")` → **green** success treatment (`#3CA761`)
- Unpaid/in-progress payments → **teal** (`#00C4CC`) — commonly described as blue
- Draft payment → **deep blue** (`#034771`)
- Status column flattens many fulfillment states to `"In Progress"` / `"Error"` / `"Completed"`

**Tim’s style guide (`docs/application-style-guide.md` §Payment):**

| Status | Treatment |
| --- | --- |
| Paid | **Success** |
| Payment pending | Warning |
| Draft / Invoiced | Neutral |

**Order detail** correctly uses step label **“Paid”** in the workflow (`workflowSteps`), while the list renames paid → **Completed**.

**Revised defect (actionable):**

> **Payment taxonomy collapse + label inconsistency**, not “green vs blue Paid.”  
> List shows paid as **Completed** (green). Design + style guide want **Paid** (Success). Progress column’s teal “In Progress” is the more likely “blue” people are pointing at.

**Do not BugHerd:** “Change Paid from blue to green” without a screenshot of the exact column.

**Do ticket (after visual confirm):**  
“List payment label: `paid` → display `Paid` with Success token; stop mapping payment onto fulfillment’s Completed label. Align filter option that currently says Completed for value `paid`.”

---

### C2 · P0-3 “Filters missing” overstates the code gap

**Code already has** filter categories Kaitlin named (08-10): payment, progress steps, client, merchant (`orders-filter-panel.tsx` + `paymentFilterOptions` / `progressFilterOptions`).

**Figma #83** asks for a **Squarespace-like category pattern** (visual IA), not “add filters from zero.”

**Revised:** P1 visual-pattern fidelity (or confirm filters unusable) — **not P0 product hole** unless QA shows filters broken/hidden.

---

### C3 · P0-1 Walmart inline is product-true but backlog wording risks wrong build

**Product ruling (Spencer+Kaitlin 1:1) stands.** Soft edge also stands: step must appear on the order; generation complexity may live nested.

**Stronger code evidence than “link to generation” alone:**

Order detail `workflowSteps` are only:

1. Draft → 2. Paid → 3. Allocated → 4. Export created → 5. Download → 6. Customer delivery → 7. Closed  

**No Preparation / Import-activated-results step**, despite style-guide workflow also listing seven non-prep stages. Walmart path is a **red “error-looking” card** + external nav to `/card-vault/generation` — conflicts with design comment “make this look less like an ERROR, it’s a step.”

**Risks if we ship P0-1 carelessly:**

| Bad ticket | Why bad |
| --- | --- |
| “Generate cards inline like Figma mock” | Tim correctly rejected fake “generate in app / go to Fiserv” copy |
| “Move entire generation page into order DOM” | Unknown field count; inventory shortfall still vault-shaped |
| Cite “55% volume” as fact | Spencer **estimate** on call — not a measured Progressive metric |

**Actionable acceptance (keep):**

- When order has `requiresGeneration` lines, **workflow shows a Preparation step** (not only a red banner).
- Operator can prepare work file + import results **without losing order context** (inline panel *or* order-scoped subroute OK).
- Copy: prepare/import language only; no “taken to Fiserv.”
- Prefill order # / line denominations **where data exists** (thread #82 open question).

**Still needs Tim answer before builder:** shape choice (inline / nested route / hybrid). Without that, item is **product-decided, engineering-unshaped** — fine for a decision ticket, bad for BugHerd “fix this.”

---

### C4 · Figma comment corpus is heavily polluted with Design Direction history

| Location bucket | Root threads (approx) |
| --- | --- |
| Design Direction | **68** |
| Screens / → Orders | **~12** |
| Design System | few |

**Implication:** Most numbered comments (#1–#70 era) target **old prototype screenshots**, not current Screens frames. Using them as implement-from source will create thrash.

**Rule for any BugHerd / builder ticket:**

- **Source = Screens + Design System + Tim style guide**, *or* a comment whose location is `→ Orders` / `Screens · …`
- Design Direction comments → **research hints only**, must be re-validated against current Screens before filing

Backlog P2 items that cite #5–#10, #30–#32, etc. from Design Direction are **not yet actionable**.

---

### C5 · Pack claims visual QA progress we do not have

- `DESIGN-QA-REPORT.md` — **missing**
- `design-qa.done` — **missing**
- Codex recon still running; Figma metadata pull started, no completed evidence pack

Filing BugHerd now would be **opinion + stale comments + partial code read**, not adversarial visual QA.

---

### C6 · “Agent headroom ⇒ few concessions” is a posture, not a budget fact

True that agents reduce cost of fidelity. Still true: Phase 1 SOW is a fixed product build with **“simple visual interface”** language — not unlimited design fidelity. Prioritization remains real (Tim morning sync). Our pack correctly prefers high-frequency paths; do not let “no concessions” become a blank check for P3 admin chrome.

---

## Item-by-item scorecard (PRIORITIZED-BACKLOG v1)

| ID | Verdict | Why | Action |
| --- | --- | --- | --- |
| **P0-1** Walmart step | **PASS with rewrite** | Product ruling solid; code missing step + error chrome is real | Rewrite around workflow step + non-error chrome + context-preserving prep; Tim shapes engineering |
| **P0-2** Paid blue→green | **FAIL as written** | Code shows paid→Completed green; likely label/taxonomy issue | Rewrite after one staging screenshot of Payment vs Status columns |
| **P0-3** Filters | **DOWNGRADE** | Categories largely exist | P1 pattern match to Figma #83 / node `433-3306` |
| **P0-4** Changelog | **PASS** | Process; not BugHerd | Tim/Steph ops, not design QA tool |
| **P1-1** Tokens | **HOLD** | Correct direction; needs Screens/Design System frame ids + visual diff | Wait for design-qa report |
| **P1-2** Shell | **HOLD** | Same | Wait for design-qa report |
| **P1-3** Orders layout | **PARTIAL PASS** | Candace #80–#81 on **→ Orders** (valid source); checkmarks Tim-acked | Keep only items with Screens location; need visual confirm what’s still open |
| **P1-4** Language | **PASS** | Style guide + rulings; residual sweep is concrete | Executable without BugHerd |
| **P2-*** | **HOLD / PARK** | Mostly Design Direction-era | Do not BugHerd |
| **P3** | **PARK** | Correct | — |

---

## What is solid enough to keep (do not throw away)

1. **Walmart preparation is an order-step UX problem** (Spencer+Kaitlin), not “design wants pretty.”  
2. **Changelog hygiene** after Codex UI deploys.  
3. **Screens / Design System / style guide** as implement-against sources; Design Direction is archive.  
4. **Agent design QA before designer BugHerd marathon** — still the right sequence.  
5. **SOW lens:** high-frequency operator clarity > secondary chrome.  
6. **Generation CTA evidence:** `/card-vault/generation` link + red card still true at `6241988`.

---

## Premature action risks (explicitly blocked)

| Action | Why blocked now |
| --- | --- |
| Leave BugHerd tasks from backlog v1 | Multiple items wrong or unpinned |
| Tell Tim “implement P0-2 as paid green” | May already be green; wrong fix |
| Tell Tim “build filters” | Filters largely exist |
| Implement Design Direction comments wholesale | Stale source pollution |
| Kaitlin full BugHerd pass | Agent visual report incomplete; burns designer time on agent-detectable slop |

---

## Required fixes before any external capture

### A. Revise backlog → v2 (Prime or recon)

- Rewrite P0-2 as **payment label/taxonomy** defect (style guide Paid / Success).  
- Downgrade P0-3 → P1 pattern.  
- Strengthen P0-1 with workflowSteps gap + non-error treatment; mark engineering shape **blocked on Tim**.  
- Strip P2 citations that only live on Design Direction.  
- Mark every item `evidence: code | figma-screens | verbal | unverified`.

### B. Finish design-qa recon with evidence discipline

Report must include, per primary route:

- Figma **node id** (Screens)  
- Staging path  
- Pass / gap  
- Severity  
- **Not inferred from Design Direction comments alone**

### C. Only then decide capture channel

| Channel | Use for |
| --- | --- |
| **GitLab issues / Tim Codex list** | Executable engineering (P0-1 shape, label fix, shared tokens) |
| **BugHerd** | Residual **human** visual issues agent cannot settle (taste, edge layouts, content) after agent pass |
| **Figma comments** | Design ownership / Tim replies — already live; don’t duplicate into BugHerd unless needed for QA workflow |

**Recommendation:** Prefer a **prioritized markdown / GitLab list for Tim** over BugHerd for engineering work. Use BugHerd only if the team already standardized on it for staging markup *after* agent triage.

---

## Open questions that still block clean tickets

1. **Spencer/Kaitlin/Tim:** Display label for paid payment — **Paid** (style guide + order form) vs **Completed** (list mapping)?  
2. **Tim:** P0-1 engineering shape this week?  
3. **Kaitlin:** Consolidated current-screens page link (morning sync ask) — without it, “current design” is ambiguous.  
4. **Anyone with staging eyes:** One screenshot of Orders table Payment + Status columns for a paid open order (settles C1).

---

## Bottom line

The pack is **directionally right** (Walmart step, agent-first QA, source-of-truth hierarchy, budget prioritization) and **not yet safe to externalize**.

Highest-value corrections:

1. Fix the **Paid/blue** story before it becomes a wrong ticket.  
2. Stop treating **Design Direction comments** as a backlog.  
3. Wait for **visual design-qa evidence** before BugHerd.  
4. Keep **Walmart step** as the only hard product P0; shape it for Tim without over-prescribing DOM structure.

**Next Prime action:** produce `PRIORITIZED-BACKLOG-v2.md` reflecting this review, then fold Codex design-qa report when it lands — still no BugHerd until then.
