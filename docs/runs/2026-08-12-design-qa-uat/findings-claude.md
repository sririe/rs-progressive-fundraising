# Findings — design-qa-uat round 2 · Claude lane (interaction states, consistency, responsive)

Date: 2026-08-12. Recon lane under AUR2 Prime. Lens: interaction states, design-system
consistency, responsive/laptop behavior, order-detail state coherence, console/a11y spot check.
Sibling lanes cover static Figma fidelity.

## 1. Method & coverage

- **Auth:** operator-provided `redstamp` (Admin) session in Chrome (Browser 1), claude-in-chrome
  against a fresh MCP tab. Hard-refresh before judging. An earlier auth block (expired session)
  was resolved by the dispatcher; the archived `.blocked` sidecar documents it.
- **Staging freshness gate: PASS.** PGC-1027 (Barton Group / Walmart) progress bar reads
  Draft → Paid → **Card Preparation** → Allocated → Export created → Download → Customer
  delivery → Closed, with a Walmart Card Preparation step panel between Payment and Allocate.
  Staging is running Tim's 2026-08-12 build. Evidence: `screens-claude/pgc1027-order-detail-closed.jpg`.
- **Routes live-inspected** (1440×900 and 1280×800): `/` (dashboard), `/fulfillment` (+ View
  All/Open/Closed/Canceled tabs, search, filter drawer, applied merchant filter), `/requests/PGC-1026`,
  `/requests/PGC-1027`, `/requests/PGC-1029`, `/card-vault`, merchant pages (Starbucks, Walmart),
  `/exports`, `/users`, `/integrations/wordpress`, `/clients`, `/clients/:id` (Barton Group).
- **Figma:** static exports in `figma-frames/` (all 9 present per its INDEX.md); live
  `get_screenshot` of hover-spec node 640-64 (saved as `screens-claude/figma-640-64-hover-spec.png`).
  No `get_metadata` (known hang risk on this host).
- **Interaction provenance:** all findings below are live-inspected (hover/click/type/keyboard in
  the running app); DOM checks via in-page JS where noted. No code inspection needed beyond that.
- **NOT covered (declared):** role-based views (`elaine`/`mario` — cannot enter passwords; only the
  operator's `redstamp` session existed); any mutating lifecycle action (no order created, nothing
  allocated/imported/exported/downloaded — per lane discipline and to avoid disturbing seeded
  orders); Audit Log page contents (visited nothing there; see P0-1 — its nav link is occluded);
  pixel-level Figma fidelity (sibling lane); formal contrast measurement (visual pass only).
- **Charts: none exist in the current build** (Dashboard is stat cards + lists; client detail has
  no charts). Kaitlin's `00.00.00` chart-date rule is unverifiable — vacuously satisfied today; it
  becomes testable only when a chart ships.

## 2. P0 — UAT blockers

| id | route | finding | evidence | Figma ref | why P0 |
| --- | --- | --- | --- | --- | --- |
| P0-1 | all routes (sidebar) | At laptop viewport heights (breaks below ≈700px inner height; reproduced at 1280×800 window = 623px viewport), the sidebar's pinned user block **covers the Integrations and Audit Log nav links**. `document.elementFromPoint` at the link centers returns the user-block div — the links are unclickable — and the sidebar is `overflow-y: hidden`, so there is no scroll path. Collapsed icon-rail mode restores Integrations but **Audit Log stays occluded**. Two admin screens become unreachable from the nav with zero affordance. | `screens-claude/clients-1280-sidebar-items-missing.jpg`, `screens-claude/sidebar-collapsed-1280-no-audit-log.jpg`; DOM probe in run log | n/a (behavioral) | Severity def: "layout broken at laptop width (~1280–1440)". 1280×800 is a standard walkthrough laptop; with browser chrome the viewport lands in the broken range. Nav dead-end = broken flow, and Integrations is on Kaitlin's own checklist. Fix is small (scrollable nav / user block in flow). **Check the walkthrough machine height regardless.** |

## 3. P1 — fix before UAT if at all possible

| id | route | finding | evidence | Figma ref | why P1 |
| --- | --- | --- | --- | --- | --- |
| P1-1 | `/requests/PGC-1026`, `/fulfillment`, dashboard | **Status pill does not advance past "Allocated".** PGC-1026's progress bar shows Export created ✓ / Download active, but the header pill, orders-list pill, and dashboard pill all still read "Allocated". Between Allocated and Closed there are three workflow states (Export created, Download, Customer delivery) that all display as "Allocated". | `screens-claude/pgc1026-pill-allocated-vs-progress-download.jpg` | 601:2640 shows an "Export created" status pill in the orders table; Final Pills 421:1868 | Kaitlin's ruling: pills "should match the Steps and language on the order screen." On the same screen two signals tell different stories; an operator scanning the list can't see an export is waiting for download. Residual of round-1 P0 #2. |
| P1-2 | `/requests/PGC-1027` (Walmart prep step), `/integrations/wordpress` | **Fiserv portal URL is not configured on staging.** The Walmart Card Preparation panel's external link renders as a disabled button labeled "Fiserv URL not set", and the Integrations page headline stat reads "Fiserv URL: **Missing** / Not set". Config, not code — the Fiserv portal field exists and is simply blank. | `screens-claude/pgc1027-walmart-prep-panel-fiserv-not-set.jpg`, `screens-claude/integrations-fiserv-url-missing.jpg` | Ruling 1 (Fiserv external URL) | The Walmart prep flow is THE new thing being demoed. A dead "Fiserv URL not set" button mid-walkthrough on the core path is exactly the embarrassment this round exists to catch. **Remediation: set the Fiserv Portal URL on staging before UAT** (Integrations → Fiserv portal). Escalates to P0 if left as-is. |
| P1-3 | `/fulfillment` filter drawer | **Filter vocabulary doesn't match the new step language.** "Progress steps" offers Drafted, **Needs Inventory**, **Needs Generation**, Ready to Allocate, Allocated, Closed, Canceled — "Needs Inventory/Needs Generation" appear nowhere else in the new UI, and Card Preparation / Export created / Download / Customer delivery are absent. Separately, **"Drafted" is listed under Payment status** (it's an order state, not a payment state). Filters do work mechanically (merchant filter verified). | `screens-claude/filter-drawer-payment-status-drafted.jpg` + full label dump in run log | Kaitlin pill-language ruling | Client opens "Filter by" during the walkthrough and meets the old vocabulary the pill cleanup just removed. Same ruling, one screen behind. |
| P1-4 | Card Vault (`/card-vault`, merchant pages) | **Vault numbers don't reconcile visibly and card-status pills are semantically misleading.** Walmart row: Available 32 / Allocated 0 / **Total 152** (only row where the columns don't add up); tabs: View All (592) ≠ Available (468) + Allocated (4). The gap is PGC-1027's 120 delivered cards, but no column/tab/status says "delivered": in card tables an **available** card shows a green "**Completed**" pill, an **allocated** card shows "**In Progress**", and delivered cards also show "Completed" — indistinguishable from available. | `screens-claude/card-vault-walmart-row-32-0-152.jpg`, `screens-claude/vault-walmart-merchant-stats-unreconciled.jpg` | Final Pills 421:1868 (colors comply; the *labels* are the generic category names) | "Data that looks wrong" on a core screen: an operator reads 32+0=152 as a bug, and "Completed" on an unused card is actively misleading. Semantic card states (Available/Allocated/Delivered) would fix both. |
| P1-5 | all tables/lists (orders, dashboard open-orders, vault) | **Row hover doesn't extend to the full width of the white card.** The grey band spans the table width but sits inset ~22px from the card's left/right edges (measured at 1440; same on dashboard list). Figma 640-64 specs the hover band flush edge-to-edge of the white card. Kaitlin's exact words: "the full width of the white not just to the end of the text." | hover zooms in run log; `screens-claude/figma-640-64-hover-spec.png` | 640-64 | Kaitlin-list item partially done (huge improvement over text-width hover, but not the flush spec). Cheap fix; she will re-check this one specifically. |

## 4. Verified fixed — Tim's 2026-08-12 claims (do not re-litigate)

1. **Walmart Card Preparation step between Paid and Allocated** — ✓ progress bar + step panel on
   PGC-1027; panel has generate-prep-file, external Fiserv link slot, activated-result CSV
   upload + paste import. (Not exercised end-to-end; PGC-1027's activity trail shows a complete
   historical run: prep file downloaded → export from activation work file → delivered → closed.)
2. **Two pills total, one In Progress pill + paid state** — ✓ everywhere: orders list, dashboard,
   order headers all show exactly Paid + one status pill. No duplicate "Inprogress" anywhere.
3. **Semantic status pill labels** — ✓ on orders surfaces (Ready to Allocate / Allocated / Closed;
   colors match Final Pills semantics: green=done, teal=in-progress, grey=draft, red=error; green
   Paid confirmed per ruling 3). Residual: P1-1 (label stops advancing at "Allocated") and P1-4
   (vault card pills still generic).
4. **Full-width grey table hover** — ✓ implemented globally (orders, dashboard, vault). Residual:
   P1-5 (~22px inset vs flush Figma spec).
5. **Tight `00.00.00` dates in tables** — ✓ orders Updated, clients Updated, vault Created,
   exports activity all show `08.12.26`. Long-form dates only in stat cards/activity feeds where
   space isn't tight (correct per the rule's intent). Charts: none exist (see coverage).
6. **Cards Ordered rows don't hover/highlight** — ✓ no hover state, cursor stays default
   (PGC-1027, PGC-1029). **Client name not clickable under Client information** — ✓ plain text;
   only "View Client" links (header + card).
7. **Users/Integrations styling pass** — ✓ judged aligned enough for a client walkthrough: stat
   cards, inputs, buttons, pills, destructive-red styling all match the new system on both pages.
   Not jarring. (Notes: P2-3 red permission chips, P2-4 dev-flavored blocks.)
8. **De-duplicated In Progress pills** — ✓ (same evidence as #2).

## 5. Questions for Tim/Kaitlin

1. **Closed-order Walmart actions:** on Closed PGC-1027, "Generate file" and "Import activated
   result" are still enabled (Cancel is properly disabled with an explanation). Intentional
   re-run capability or missed gating? (Ruling 4: behavior wins — flagging, not filing.)
2. **"Ready to Allocate" while allocation is blocked:** PGC-1029 pill says Ready to Allocate but
   the step says "Inventory is short" and Allocate Cards is disabled (8 available vs 12 ordered —
   internally coherent, red dot matches). Is "Ready to Allocate" the right label when allocation
   isn't actually possible yet, or should shortage surface in the pill/list?
3. **Vault card-state vocabulary** (pairs with P1-4): should card rows say Available / Allocated /
   Delivered instead of Completed / In Progress? And should merchant stats show a Delivered count
   so Total reconciles?
4. **Users page red permission chips:** sensitive permissions ("Allocate cards", "Create exports",
   "Download sensitive exports") use the error-red pill treatment. Red-as-category vs
   red-as-error — Kaitlin's call.
5. **Merchant icon editor** (hex value, image path, Save Icon) sits prominently between stats and
   inventory on every merchant page — fine for internal admin, but will be seen in the vault
   drill-down during the walkthrough. Acceptable, or collapse/relocate before UAT?

## 6. P2/P3 one-liners

- P2: Orders table horizontally scrolls at 1280 (thick dark-navy scrollbar; default-sort "Updated"
  column off-screen until scrolled) — `screens-claude/orders-1280-hscroll-sidebar-occluded.jpg`.
- P2: Collapsed icon-rail nav has no tooltips on hover — icon-only guessing.
- P3: 8-step Walmart progress bar at 1280 wraps "Customer delivery" to two lines with the ✓
  misaligned — `screens-claude/pgc1027-1280-progress-8-steps-wrap.jpg`.
- P3: Allocated Cards accordion renders all 120 rows inline (long scroll on closed Walmart order).
- P3: Clients table at 1280 wraps emails mid-word ("…exam / ple").
- P3: Step-description punctuation inconsistent ("Customer delivery has been recorded." vs
  periodless siblings).
- P3: Legacy deep links `/orders` and `/vault` silently redirect to the dashboard (canonical paths
  are `/fulfillment`, `/card-vault`; order detail lives at `/requests/:id`) — internal nit.
- Console: clean on every route inspected (hard refresh included) — the only console errors came
  from a Chrome extension, not the app. Tim's hydration noise did not reproduce user-visibly.
- Keyboard: focus rings visible and ordered on the core path; Escape closes the filter drawer.
  Contrast (visual pass only): nothing alarming; the light-grey disabled "Cancel order" explainer
  on white is the closest to borderline.
