---
title: Progressive Card Vault — Prioritized design→dev backlog
date: 2026-08-10
status: draft-v1 — SUPERSEDED by PRIORITIZED-BACKLOG-v2.md — ADVERSARIAL FAIL — do not use
superseded_by: PRIORITIZED-BACKLOG-v2.md
adversarial_review: docs/runs/2026-08-10-design-dev-reconcile/ADVERSARIAL-REVIEW.md
audience: Tim / Codex builder + Spencer gate
source_of_truth_screens: "Figma file Ztv1YtEx1S19i0w4bdHgo4 · Screens pages (Orders, Card Vault, Dashboard) + Design System tokens"
staging: https://progressive-gift-cards-card-vault-staging.onrender.com/
---

# Prioritized backlog for Codex execution

> **GATE (2026-08-11):** Adversarial review **FAILED** this document for external action.
> Do **not** file BugHerd from this file. Do **not** hand to Tim as an execute list until v2.
> Read `ADVERSARIAL-REVIEW.md` first — especially C1 (Paid/blue misdiagnosis), C2 (filters already exist), C4 (Design Direction pollution).

**How to use (after v2):** implement top-down. Each item is written so an agent can open Figma node + staging route and close the gap without re-litigating product intent.

**Priority key**

| Pri | Meaning | Budget posture |
| --- | --- | --- |
| **P0** | Product correctness / operator confusion on high-frequency path | Ship before Progressive UAT walkthrough |
| **P1** | Visual system consistency that design already specified | Ship with agent headroom; high ROI |
| **P2** | Fidelity polish on primary screens | Do if P0/P1 green and budget allows |
| **P3** | Secondary screens / nice-to-have | Park or fold into S&M / Phase 2 |

**Acceptance pattern for UI items:** match the named Figma frame in `Screens` (not `Design Direction` historical screenshots) within token/spacing tolerance; note intentional deviations.

---

## P0 — Product / workflow (do not skip)

### P0-1 · Walmart preparation lives in the order step workflow
- **Ruling:** Spencer + Kaitlin 2026-08-10. Walmart ~55% of volume; operators should not leave the order journey for “just the form.”
- **Current code:** order detail shows “Merchant preparation required” + link to `/card-vault/generation`.
- **Figma:** `Screens · Walmart Orders` (+ comment thread #82–#84).
- **Constraints (Tim, keep):**
  - App does **not** open Fiserv.
  - App **prepares** the work file and **imports** activated results.
  - Copy must not say “you will be taken to Fiserv.”
- **Acceptable technical shapes (pick one; prefer least disruption):**
  1. **Inline step panel** on order detail when any line item `requiresGeneration` (expandable step in the existing progress/timeline).
  2. **Order-scoped preparation route** nested under the order (e.g. `/requests/[n]/prepare`) that reuses generation components but keeps order chrome/context.
  3. Keep vault generation page for batch/admin prep, but order path must not be “go somewhere else and lose context.”
- **Acceptance:** From a Walmart order, operator can prepare work file + import results without hunting the vault nav; order context (order #, line items, denominations) pre-fills where known.
- **Not in scope:** automating Fiserv UI/login.

### P0-2 · Status / payment pills consistent with Design System · Pills
- **Reported:** Paid appears blue on orders list; design wants paid = green (and consistent token use sitewide).
- **Code:** `src/lib/format.ts` maps `paid` → label `Completed` + green `Completed` style — verify actual orders table path isn’t bypassing this.
- **Acceptance:** Same semantic status uses same pill token on list, detail, dashboard; labels match glossary (Paid vs Completed is a language decision — if design says “Paid”, show “Paid” in green, don’t silently rename).

### P0-3 · Filter model on Orders matches design intent
- **Figma comment #83 (08-10):** Squarespace-style categories — paid status, progress steps, client, merchant.
- **Code:** filter panel already exists (`orders-filter-panel.tsx`) — validate against Figma frame and wire any missing categories/visual pattern.
- **Acceptance:** Filters usable without overwhelming; matches Figma pattern or documented intentional simplification.

### P0-4 · Changelog / design sync hygiene (process, not code)
- After each staging deploy that touches UI, post 3–8 bullets in `#progressive-fundraising`: routes touched, Figma frames referenced, known remaining gaps.
- Reduces “prototype moved under me” friction (Kaitlin 08-10).

---

## P1 — Design system consistency (high ROI, agent-friendly)

### P1-1 · Shared tokens from Design System pages
- Source: Figma `Design System → Styleguide / Sidebar / Header / Pills`.
- Align: primary teal `#00C4CC`, navy `#212A3E`, deep blue `#034771`, pill fills, 5px radii, table density.
- Prefer edits in shared components (`admin-ui.tsx`, `app-frame.tsx`, `badge.tsx`) over one-off page CSS.

### P1-2 · Sidebar + header fidelity
- Recent commits already chased Figma measurements; re-diff against latest Screens after Kaitlin’s consolidated page lands.
- Candace: collapse control shouldn’t fight the logo; buttons less “website-y.”

### P1-3 · Orders list + order detail layout
- Keylines between stacked info (Candace #80).
- Timeline checkmarks before labels (Candace #81 — Tim agreed).
- Icon accuracy (merchant icons already landing — verify wrong-icon reports).
- Secondary text contrast (Steph a11y concern on light gray summaries).

### P1-4 · Language already ruled
- Merchant not Vendor; order not request in UI; cancel not delete; prepare/import not “activate in-app.”
- Commit `3267a04` applied much of this — sweep residual “request/vendor” UI strings.

---

## P2 — Primary-screen fidelity (after P0/P1)

### P2-1 · Dashboard
- Active-nav indication (Candace #1).
- Consistency of status cards with orders list (#16).
- Optional compress sidebar (#71) if not already shipped.

### P2-2 · Card Vault list / merchant detail
- Table cleanup, sort, less “lost” header actions (#30–#32, #69).
- Generator path UX after P0-1 (may simplify vault entry points).

### P2-3 · Import flow
- Dropdowns, preview-as-review surface (#33–#34).

### P2-4 · New order form polish
- Mandatory field marks, PO- prefix, $ prefix, client typeahead (#5–#10) — only if UAT will use manual create heavily.

---

## P3 — Park / later

- Full Users / WordPress integrations visual redesign (#62–#64).
- Clients chart cleanup (#49–#56) unless client training hits it first.
- Physical-card UI (feature-flagged; design notes acknowledge digital-only V1).
- Historical **Design Direction** comments against old screenshots — treat as backlog ideas, not implement-from source. **Screens** pages win.

---

## Suggested Codex execution slices (small PRs)

1. **`lane/orders-pill-and-filter-fidelity`** — P0-2 + P0-3 + P1-3 list-only  
2. **`lane/walmart-inline-prepare-step`** — P0-1 (product-shaped; needs Tim design choice among 3 shapes)  
3. **`lane/shell-tokens-sidebar-header`** — P1-1 + P1-2  
4. **`lane/card-vault-table-pass`** — P2-2  

Do not open a single mega-PR that mixes workflow restructure with pixel polish.

---

## Agent design QA checklist (pre-BugHerd)

For each route below, capture: Figma frame id, staging URL, gap list (layout / type / color / copy / interaction), severity P0–P3.

| Route | Figma page |
| --- | --- |
| `/fulfillment` (Orders) | Screens → Orders |
| `/requests/[n]` (Order detail, non-Walmart) | Screens → Orders |
| `/requests/[n]` (Walmart / needs_generation) | Screens → Walmart Orders |
| `/card-vault` | Screens → Card Vault |
| `/card-vault/generation` | Screens / Process as applicable |
| `/` Dashboard | Screens → Dashboard |
| Login shell | Design System / Sidebar |

**Stop condition for Kaitlin BugHerd:** P0 closed or explicitly deferred with operator note; P1 gaps filed as executable tickets, not free-form screenshots only.

---

## Open questions for humans (minimal)

1. **Tim:** Which P0-1 shape (inline panel / nested route / hybrid) can ship this week without blowing export/allocation edge cases?
2. **Kaitlin:** Confirm the consolidated “current screens” page is ready (Tim’s ask from morning sync). Link or page name.
3. **Spencer:** Confirm Paid label stays “Paid” (green) vs “Completed” (current code mapping) — language vs design token.

---

## Evidence pointers

- Figma comments export: `docs/runs/2026-08-10-design-dev-reconcile/figma-comments/`
- Transcripts: same run folder
- Session brief: `SESSION-BRIEF.md`
