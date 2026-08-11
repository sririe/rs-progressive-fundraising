---
title: Progressive Card Vault — design QA reconciliation
date: 2026-08-11
run_date: 2026-08-10
status: complete
mode: read-only-recon
app_commit: 6241988b1a0f3c42924339d9eafba703ad1ecfc8
figma_file: Ztv1YtEx1S19i0w4bdHgo4
figma_version: 2386168815833423251
staging: https://progressive-gift-cards-card-vault-staging.onrender.com/
---

# Progressive Card Vault design QA report

## 1. Method

### Verdict

Staging is materially closer to the current Figma `Screens` page than the draft backlog implies. The shell, Dashboard, Orders list, four-category filter, non-Walmart order structure, Card Vault, and core design tokens are already close enough that a broad visual rewrite would waste time.

There are two P0 implementation needs before Progressive UAT:

1. Walmart preparation is still a detached alert/link instead of an order workflow step.
2. Status pills use the right state colors but generic labels (`Completed`, `In Progress`) that obscure the actual payment and fulfillment state.

The earlier “Paid is blue” diagnosis is false on current staging: paid renders green. The defect is semantic labeling, not the green token.

### Evidence inspected

**Figma — current file, live read-only inspection**

| Surface | Current node(s) |
| --- | --- |
| Dashboard | `564:1152` — Dashboard |
| Orders list | `601:2640` — Orders - Parent - Full Screen |
| Non-Walmart order detail | `601:123` — Orders - Individual |
| Walmart preparation sequence | `601:450`, `601:823`, `601:1196`, `601:1573` — Walmart Orders 1–4 |
| Card Vault | `601:3269` — Card Vault |
| Pills | `421:1868` — Final Pills |
| Screens page | `294:12978` |
| Design System page | `274:10805`; supporting Sidebar `274:10807`, Header `283:11843`, Pills page `296:13711` |

The file version recorded in the session brief was `2386168815833423251`, last modified `2026-08-10T18:17:00Z`. I used the current `Screens` frames, not historical Design Direction screenshots. Comment threads #80–#84 were used for intent and rulings.

The Walmart frames are useful for layout and state progression, but some frame copy conflicts with the locked V1 boundary (for example, implying an in-app/Fiserv handoff or card generation). The report therefore uses those frames as the visual source while preserving the product ruling: the app prepares a work file, the operator activates externally, and the app imports the activated result.

**Staging — live, logged-in Chrome inspection**

- `/`
- `/fulfillment`, including opening the filter drawer
- `/requests/PGC-1026` — non-Walmart fixture
- `/requests/PGC-1027` — Walmart / `needs_generation` fixture
- `/card-vault`
- `/card-vault/generation`
- `/login`

No staging data or settings were changed. Merchant image elements on `/card-vault` were also checked in the DOM: all merchant assets completed successfully with non-zero intrinsic dimensions.

**Code — read-only at `6241988` (`Clean up order workflow controls`)**

- `src/app/page.tsx`
- `src/app/fulfillment/page.tsx`
- `src/app/fulfillment/orders-overview.tsx`
- `src/app/fulfillment/orders-filter-panel.tsx`
- `src/app/requests/[requestNumber]/page.tsx`
- `src/app/requests/[requestNumber]/actions.ts`
- `src/app/card-vault/page.tsx`
- `src/app/card-vault/card-vault-overview.tsx`
- `src/app/card-vault/generation/page.tsx`
- `src/app/card-vault/generation/actions.ts`
- `src/app/login/page.tsx`
- `src/components/app-frame.tsx`
- `src/components/app-shell.tsx`
- `src/components/vendor-icon.tsx`
- `src/lib/format.ts`
- `src/lib/merchant-output-profiles.ts`
- `src/lib/merchant-output-export.ts`
- `src/lib/vendor-work-files.ts`
- `src/lib/inventory-import.ts`
- `src/lib/inventory-import-service.ts`

No `.blocked` conditions occurred. Figma, staging, the authenticated routes, and the public login route were all accessible. There is no dedicated current login frame in the inspected `Screens`/Design System top-level nodes, so no pixel-level login mismatch is asserted.

## 2. Route-by-route gaps

| Route | Figma frame | Severity | Gap | Suggested fix locus |
| --- | --- | --- | --- | --- |
| `/` | `564:1152` | P0 | Layout is close, but the status tables collapse domain states into `Completed` / `In Progress`. Operators cannot distinguish Paid, Needs Generation, Ready to Allocate, or Allocated at a glance. | `src/lib/format.ts`; consumers in `src/app/page.tsx` |
| `/fulfillment` | `601:2640` | P0 | Paid is already green, but the list says `Completed`; fulfillment states all appear as generic `In Progress`. Current Figma uses semantic labels such as `Paid`, `Needs Generation`, `Ready to Allocate`, `Cards Allocated`, `Export created`, and `Closed Order`. | Separate semantic labels from visual tones in `src/lib/format.ts`; simplify `getPaymentPill` / `getOrderStatusPill` in `src/app/fulfillment/page.tsx` |
| `/fulfillment` | `601:2640` | P1 | Search placeholder still says “Search requests…” after the UI language moved to Orders. Filter interaction itself is already correct. | `src/app/fulfillment/orders-overview.tsx` |
| `/requests/PGC-1026` | `601:123` | P0 | Header pills again show generic `Completed` / `In Progress` labels rather than payment, fulfillment, and delivery semantics. | `src/lib/format.ts`; `src/app/requests/[requestNumber]/page.tsx` |
| `/requests/PGC-1026` | `601:123` | P1 | `Allocated Cards` and `Order Activity` open automatically when an export exists. On the populated fixture this creates a long troubleshooting surface that pushes focus away from the workflow rail. Figma and the application style guide specify collapsed supporting disclosures. | Set supporting disclosures closed by default in `src/app/requests/[requestNumber]/page.tsx`; preserve active rail disclosure behavior |
| `/requests/PGC-1027` | `601:450`, `601:823`, `601:1196`, `601:1573` | P0 | Confirmed product gap: the progress rail jumps from Paid to Allocated and shows a detached “Merchant preparation required” alert linking to Card Vault. There is no conditional Card Preparation stage, no inline work-file action, no order-prefilled import, and the highlighted Allocated step is misleading while preparation blocks allocation. | `src/app/requests/[requestNumber]/page.tsx`; `src/app/requests/[requestNumber]/actions.ts`; add an order-scoped preparation component and download/import handlers |
| `/card-vault/generation` | Walmart sequence above | P0 | The import function exists, but this route is the wrong primary entry point for an order. It drops order context, asks for a free-form reference, and exposes staging-test generation utilities below the production-shaped import surface. Keep it as an admin/batch tool, not the Walmart order CTA. | Extract the import mutation from `src/app/card-vault/generation/actions.ts` into a shared service; reuse it from the order step. Gate staging-only panels by environment/feature flag. |
| `/card-vault/generation` | Walmart sequence above | P1 | Visible labels `Generate Cards` / `Card Generation` conflict with the ruled boundary. The body copy is mostly correct (`prepare` / `import activated result`). | `src/app/card-vault/page.tsx`; `src/app/card-vault/generation/page.tsx` |
| `/card-vault` | `601:3269` | P3 | No actionable primary-path gap. Structure, tabs, search/filter, density, and totals are close. Staging uses real merchant logo assets where Figma uses compact colored marks; all checked images load correctly, so do not file this as a broken-icon bug. | None unless design explicitly chooses initials over real logos |
| `/login` | No dedicated canonical frame found | P3 | Branded centered sign-in card is coherent with shared type, border, surface, button, and logo treatments. Without a dedicated current frame, there is no evidence-backed pixel gap. | None; `src/app/login/page.tsx` only if a canonical login frame is added later |

## 3. P0/P1 backlog reconciliation

| Backlog item | Verdict | Evidence and refinement |
| --- | --- | --- |
| P0-1 · Walmart preparation in order workflow | **Confirmed; highest-priority build slice.** | `PGC-1027` has no Card Preparation workflow segment and sends the operator to `/card-vault/generation`. Current code does this at `src/app/requests/[requestNumber]/page.tsx` via the “Merchant preparation required” card/link. The current Walmart Figma sequence places Card Preparation between Paid and Allocated. |
| P0-2 · Status/payment pill consistency | **Confirmed, but re-diagnosed.** | Paid is not blue on current staging; it is green. `src/lib/format.ts` maps `paid` to display label `Completed`, and multiple fulfillment states to `In Progress`. The Pills component styling is consistent; operational labels are not. Fix semantic labels while retaining shared state tones. |
| P0-3 · Orders filter model | **Close as already implemented.** | The staging drawer has all four requested groups: Payment status, Progress steps, Client, Merchant, with Apply and Clear. `orders-filter-panel.tsx` persists each group through query parameters. Only its payment option text inherits P0-2’s generic label problem. |
| P0-4 · changelog/design-sync hygiene | **Retain as a release process gate, not a code ticket.** | This recon cannot prove team posting behavior from the app. The need remains supported by the design-comment history. Require the 3–8-bullet route/frame/known-gap note for each UI staging deploy. |
| P1-1 · shared tokens | **Mostly complete; do not open a broad token pass.** | Teal/navy palette, 5px control/card radii, keylines, table density, buttons, progress bars, and pill tones match closely across inspected routes. Remaining status work is semantic and belongs in the focused P0 pill slice. |
| P1-2 · sidebar/header fidelity | **Close.** | Expanded and collapsed shell, active navigation, logo relationship, grouped nav, title/header spacing, and action sizing are all materially aligned. No shell rewrite is justified before UAT. |
| P1-3 · Orders list/detail layout | **Refine to one remaining detail issue.** | Keylines in Client information are present; checkmarks precede timeline labels; the two-column order layout and workflow rail are close; merchant assets load. Remaining actionable gap: supporting allocation/activity disclosures default open on exported orders. |
| P1-4 · ruled language | **Mostly complete; small visible-string sweep remains.** | Staging correctly uses Order, Merchant, Cancel, prepare, and import in the primary detail journey. Residual visible strings include “Search requests…” and `Generate Cards` / `Card Generation`. Do not rename internal model identifiers merely for cosmetic consistency. |

## 4. Already close — do not re-do

- **App shell:** 259px expanded navy sidebar, logo panel, collapse control, grouped nav, active state, header structure, and action sizing are already aligned to the current Figma direction.
- **Dashboard:** title/header, metric strip, status sections, table structure, spacing, and responsive composition are close. Only semantic status text needs the shared pill fix.
- **Orders list:** tabs, search/filter controls, table columns, row keylines, density, values, merchant/type display, and pagination treatment are close.
- **Orders filter:** Payment status, Progress steps, Client, and Merchant groups are present and usable. Do not rebuild it.
- **Non-Walmart order detail:** progress bars, checkmarks before labels, compact metric strip, client row keylines, line-item table, two-column primary layout, payment control, active/locked workflow cards, cancel wording, and secondary link treatment are close.
- **Card Vault:** tabs, metrics, search/filter/sort controls, grouped inventory table, status treatment, and merchant imagery are working. The merchant logos are loaded assets, not blank or broken icons.
- **Login:** branded login card is polished and consistent with the app system. There is no canonical current Figma frame that supports further churn.
- **Walmart boundary language inside the alert/import surface:** code already says Progressive runs activation outside the app and imports activated results. Preserve that boundary while moving the interaction into the order journey.
- **Underlying Walmart import capability:** parsing, blocking warnings/errors, unmatched-row checks, encrypted inventory import, audit logging, revalidation, and duplicate reporting already exist. Reuse the mutation logic rather than rebuilding import behavior.

## 5. Recommended next builder slices

### 1. `lane/walmart-order-preparation-step` — P0

Use the least-context-loss shape: an inline, conditional order step.

- Insert **Card Preparation** after Paid and before Allocated only when any line item has `vendor.requiresGeneration`.
- Make that stage current while the request is `needs_generation`; do not highlight Allocated until matching activated inventory is ready.
- Replace the detached alert/CTA with an order-scoped preparation panel. Prefill order number/reference and render each Walmart denomination + quantity from existing line items. Notes may remain optional.
- Provide `Download Walmart work file` and `Import activated result` within that panel. Copy must never imply that the app opens or automates Fiserv.
- Keep `/card-vault/generation` for batch/admin use, but stop using it as the primary order CTA.
- Extract the core activated-result import mutation from `src/app/card-vault/generation/actions.ts` so both surfaces share validation, import, audit, and error handling. The order wrapper should validate the result against the order reference/requirements and return to that order.
- After a successful matching import, recompute inventory readiness and move the request to `ready_to_allocate`; record an order-scoped audit event.
- Do **not** directly reuse the current post-allocation work-file endpoints as the pre-allocation contract. `src/lib/merchant-output-export.ts` and `src/lib/vendor-work-files.ts` build from allocations/export packages. The Walmart prep step needs a dedicated order-line-item builder or a deliberate decoupling of that contract, plus validation against the client-approved Walmart/Fiserv template.

Likely loci:

- `src/app/requests/[requestNumber]/page.tsx`
- `src/app/requests/[requestNumber]/actions.ts`
- new `src/app/requests/[requestNumber]/walmart-preparation-step.tsx` or shared equivalent
- new order-scoped download route under `src/app/requests/[requestNumber]/...`
- extracted service from `src/app/card-vault/generation/actions.ts`
- `src/lib/inventory-import-service.ts`
- a dedicated Walmart preparation builder beside `src/lib/merchant-output-export.ts`

### 2. `lane/semantic-order-status-pills` — P0

- Separate **display label** from **visual tone**. Current code uses generic display labels as style-map keys, which forces operational states into `Completed` / `In Progress`.
- Key tones by raw domain state (or a small `completed | progress | neutral | error` tone), while labels remain semantic.
- At minimum, make Paid, Needs Generation, Ready to Allocate, Allocated/Cards Allocated, Export Created, and Closed distinguishable wherever they appear.
- Apply the same label/tone resolver to Dashboard, Orders list, order detail, and filter options.
- Keep the current green treatment for Paid; this is not a color rewrite.

Likely loci:

- `src/lib/format.ts`
- `src/app/page.tsx`
- `src/app/fulfillment/page.tsx`
- `src/app/requests/[requestNumber]/page.tsx`

### 3. `lane/order-detail-disclosure-defaults` — P1

- Keep `Allocated Cards` and `Order Activity` collapsed on initial render, including after an export exists.
- Preserve counts/descriptions in the disclosure headers so operators can decide when to expand.
- Do not touch the already-correct timeline checkmarks, client-row keylines, or workflow rail layout.

Locus: `src/app/requests/[requestNumber]/page.tsx`.

### 4. `lane/operator-language-cleanup` — P1, optional tiny follow-up

- `Search requests…` → `Search orders…`
- `Generate Cards` / `Card Generation` → `Card Preparation` or `Prepare / import cards`, matching the exact surface
- Limit changes to visible operator copy; leave internal `request` identifiers alone.

Likely loci: `src/app/fulfillment/orders-overview.tsx`, `src/app/card-vault/page.tsx`, `src/app/card-vault/generation/page.tsx`.

Do not start the inherited `lane/shell-tokens-sidebar-header`, `lane/orders-pill-and-filter-fidelity`, or `lane/card-vault-table-pass` as originally scoped. Shell/tokens, filters, and Card Vault table work are already sufficiently close; those branches would mix closed work with the remaining gaps.

### Builder order and UAT gate

1. Ship `lane/walmart-order-preparation-step`.
2. Ship `lane/semantic-order-status-pills`.
3. Run a staging walkthrough using `PGC-1027` from Paid → prepare work file → external activation boundary → import result → ready to allocate, then verify the same semantic labels on `/`, `/fulfillment`, and the order.
4. Take the disclosure and language slices only if the P0 walkthrough is green.
5. Before handoff, post the P0-4 changelog note with routes touched, Figma frames referenced, and known remaining gaps.
