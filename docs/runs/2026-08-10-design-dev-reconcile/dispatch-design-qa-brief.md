# Recon brief — Progressive Card Vault design QA (read-only preferred)

You are a **recon** lane under AUR2 Prime. Do **not** implement product changes in this lane unless a tiny local note file is needed for the report. Primary job: compare design to staging and produce an executable gap list.

## Context pack (read these first)

1. `/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-10-design-dev-reconcile/SESSION-BRIEF.md`
2. `/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-10-design-dev-reconcile/PRIORITIZED-BACKLOG.md`
3. `/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-10-design-dev-reconcile/figma-comments/review-current-design-reconcile-figma-comments.md` (focus threads #81–#84 and Screens pages)
4. This app repo README + `docs/application-style-guide.md` + `src/lib/format.ts` (status pills)

## Sources of truth

- **Figma:** https://www.figma.com/design/Ztv1YtEx1S19i0w4bdHgo4/Digital-Gift-Card-Fulfillment-Design
  - Implement against **Screens** pages (Orders, Card Vault, Dashboard) + Design System (Pills, Sidebar, Header)
  - Prefer Figma MCP (`get_screenshot` / `get_design_context` on specific frames). You historically have Figma MCP reliable.
  - File key `Ztv1YtEx1S19i0w4bdHgo4`. Do not treat Design Direction historical screenshots as current.
- **Staging:** https://progressive-gift-cards-card-vault-staging.onrender.com/
  - Operator has a logged-in Chrome session on this Mac; use available browser tools or document if you cannot auth.
  - Staging is internal-only; no real card data.
- **Code cwd:** this repo (already at latest main).

## Product rulings already decided (do not re-open)

1. **Walmart prep must appear as an order workflow step** (Spencer+Kaitlin 2026-08-10). Tim preferred separate `/card-vault/generation` page for complexity — that is now a *how*, not *whether*. Propose technical shape in the report.
2. Paid/status pills must be consistent with Design System · Pills.
3. Budget: prioritize operator clarity on high-frequency paths over pixel-perfect secondary admin screens.

## Deliverable (write this file)

Write: `/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-10-design-dev-reconcile/DESIGN-QA-REPORT.md`

Structure:
1. Method (what you inspected: Figma node ids, staging routes, code paths)
2. Route-by-route gaps table: route | figma frame | severity P0–P3 | gap | suggested fix locus (file if known)
3. Confirm or refine PRIORITIZED-BACKLOG.md P0/P1 items with evidence
4. Explicit list of what is **already close** (so Tim doesn't re-do work)
5. Recommended next builder slices (branch names `lane/...`)

## Constraints

- Read-only recon: no commits, no pushes, no production changes.
- If blocked on Figma MCP or staging auth, write `.blocked` notes in the report with exact error — do not invent visual gaps.
- When finished, create sentinel file: `/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-10-design-dev-reconcile/design-qa.done` containing one line with the report path.

Start now.
