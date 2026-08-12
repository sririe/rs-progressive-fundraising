# Consolidated design QA — round 2, pre-UAT (2026-08-12)

Three parallel recon lanes (Codex = Figma fidelity, Claude = interaction/responsive, Grok =
walkthrough realism) against Tim's 2026-08-12 staging build. Deduped and severity-reconciled by
AUR2 Prime (Fable). Two of the three most severe items were **verified firsthand by the seat**
against the live authenticated staging session; provenance is marked per finding.

Source lane reports: `findings-codex.md`, `findings-claude.md`, `findings-grok.md`.
All three passed the staging freshness gate — staging IS Tim's 8/12 build (Walmart Card
Preparation step present between Paid and Allocated).

## Provenance legend
- **[3-lane]** independently found by all three lanes
- **[seat-verified]** AUR2 reproduced it firsthand on live staging this session
- **[Grok×2]** Grok reproduced twice with network evidence; not personally re-run by the seat

---

## P0 — UAT blockers (fix before the client walkthrough)

| # | Finding | Route | Severity basis | Provenance | Fix locus |
| --- | --- | --- | --- | --- | --- |
| P0-1 | **Create-order 500.** A normal well-formed paid order (Starbucks ×2, valid client+email, fake data) returns a full-page "This page couldn't load / A server error occurred" (`ERROR 294045514`). No order is created. If the walkthrough opens with "let's make an order," it dead-ends on a white error page. | `/requests/new` | Hard failure on a core path | **[seat-verified]** — AUR2 reproduced live, identical error code to Grok's; confirmed no orphan order created. Grok reproduced twice. | Server-side POST handler for order create. Console also shows an invalid phone `pattern` regex under the `/v` flag (`requests/new/page.tsx`, `clients/client-form.tsx`) — candidate cause. |
| P0-2 | **Walmart activated-result import 500 on file upload.** Choosing the blessed 120-row fixture via the file picker returns a full-page 500 (`ERROR 777059612`); pasting the same file succeeds. A non-technical operator reaches for "Choose file," not paste. This is THE new Walmart demo path. | `/requests/PGC-1027` Walmart Card Preparation | Hard failure on the highest-risk demo path | **[Grok×2]** with network POST 500; transitively corroborated by the seat-verified sibling 500 (same error-page mechanism). Not personally re-run to avoid mutating shared staging. | Walmart activated-result upload handler (file path vs paste path diverge — `walmart-result-import-form.tsx` + its server action). |
| P0-3 | **Status pill never advances past "Allocated."** Orders past allocation (Export created / Download / Customer delivery) still show "Allocated" on the dashboard, orders list, AND the order header — while the same order's progress bar shows a later step. The pill reads only `fulfillmentStatus`. Directly against Kaitlin's ruling that pills match the order-screen steps; Tim reported this fixed, but it's only partially closed. | `/`, `/fulfillment`, order headers | Kaitlin commitment visibly unmet + misleading status on every core order surface | **[3-lane]** — Codex + Grok (P0) + Claude (P1); two root-caused to `fulfillmentStatus`-only mapping. | `src/lib/format.ts` + the pill selector: derive the furthest current workflow state (Export created / Downloaded / Customer delivery), not just `fulfillmentStatus`. |
| P0-4 | **Sidebar user block occludes Integrations + Audit Log nav.** At laptop viewport heights (<~700px inner height; reproduced at 1280×800 window / 623px viewport), the pinned "Redstamp Admin" block covers the Integrations and Audit Log links; the nav is `overflow-y: hidden`, so there's no scroll path. Collapsed icon-rail restores Integrations but Audit Log stays hidden. Two admin screens become unreachable. | all routes (sidebar) | Functional dead-end at a standard walkthrough resolution | **[seat-verified]** — AUR2 saw Integrations + Audit Log absent from the sidebar live at 1280×623; Claude DOM-probed (`elementFromPoint`). | Make the nav list scrollable or put the user block in normal flow. **Check the actual walkthrough machine's viewport height regardless.** |

> **P0-5 borderline — Orders "Updated" column clipped at laptop width.** Codex (P0, 1280px, said no horizontal scroll recovers it) + Grok (clipped to "U" at 1440) + Claude (P2, saw a horizontal scrollbar at 1280). Lanes disagree on whether scrolling recovers the column, which points to viewport/zoom sensitivity. The `00.00.00` dates are correctly in the DOM but not visible. **Resolve by testing at the exact walkthrough resolution** — if the default-sort column is hidden with no recovery there, it's a P0; otherwise P1 polish.

---

## P1 — fix before UAT if at all possible

| # | Finding | Provenance |
| --- | --- | --- |
| P1-1 | **Fiserv portal URL not set on staging** — Walmart step shows a disabled "Fiserv URL not set" button; Integrations reads "Fiserv URL: Missing." Config, not code (the conditional external-link treatment is correctly built). A dead control mid-Walmart-demo. **Fix: set a real-looking non-transacting Fiserv URL on staging before UAT.** Escalates to P0 if left. | **[3-lane]** |
| P1-2 | **Vault numbers don't reconcile + card-status pills are generic/misleading.** Walmart row Available 32 / Allocated 0 / Total 152 (only row that doesn't add up); tabs View All (592) ≠ Available (468)+Allocated (4). The gap is delivered cards with no "delivered" column/status. In card tables an *available* card shows a green "Completed" pill and an *allocated* one shows "In Progress" — an unused card reads as done. | Claude (deep); Grok partial ("Available drops to red 8, looks like a shortage") |
| P1-3 | **Filter drawer still uses old vocabulary** — "Needs Inventory / Needs Generation" (appear nowhere else in the new UI); Card Preparation / Export created / Download / Customer delivery absent; "Drafted" mislisted under Payment status. The pill cleanup didn't reach the filters. | Claude |
| P1-4 | **Row hover not flush to card edge** — grey band sits ~22px inset from the white card's left/right; Kaitlin's spec (Figma 640-64) is flush edge-to-edge. Big improvement over text-width, but not the spec — she will re-check this one. | Claude |
| P1-5 | **Persistent red "needs merchant preparation" warning after a successful import** — after 120 cards import, the Allocate step still shows a red "this order needs merchant preparation…" while the step above shows a green check + "120 imported." | Grok |
| P1-6 | **Internal test-language visible to users** — `/requests/new` subtitle: "Manually create a test order from the seeded gift card catalog." Visible from the Dashboard "New Manual Order" (Elaine sees it too). | Grok |
| P1-7 | **Alarming error on an empty import submit** — import with no file/paste returns red "Walmart result import needs review. Check activated statuses, denominations…" instead of "choose a file or paste rows." Reads like the operator corrupted data on a normal missed click. | Grok |
| P1-8 | **Duplicate "Walmart · $25" offering** in the new-order dropdown (two identical options, same value `…hin018b…:2500`). | **[seat-verified]** + Grok |
| P1-9 | **Unlabeled Walmart reference field** — a text box pre-filled `PGC-1027` (name `walmartResultReference`, placeholder "Reference") sits between Generate file and CSV upload with no visible label/help. | Grok |

---

## Verified fixed — Tim's 2026-08-12 claims (credit; do not re-litigate)

Convergent across lanes:
- **Walmart Card Preparation is an order step between Paid and Allocated** — structure, generate/download prep file, activated-result upload+paste controls, sequential gating. [3-lane]
- **Paste-import → allocate 120/120 → export → download → record delivery → close** lifecycle works; Cancel disables after download; Close pill goes green. (Grok drove it end-to-end.)
- **Two header pills, not three "In Progress"** — everywhere. Green Paid confirmed (old "Paid is blue" stays dead).
- **Semantic pill labels on orders surfaces** — Ready to Allocate / Allocated / Closed; colors match Final Pills. (Caveat: the lag, P0-3, and generic vault pills, P1-2.)
- **Users + Integrations styling** — judged aligned enough for a client walkthrough (not a leftover old skin).
- **Tight `00.00.00` dates** in constrained tables; long-form elsewhere. (Charts: none exist in this build — Kaitlin's chart-date rule is vacuously satisfied.)
- **Client name not clickable** under Client information; **Cards Ordered rows don't hover** as clickable.
- **Full-width table hover** implemented globally (with the P1-4 inset caveat).
- **Console clean** on inspected routes; Tim's hydration noise did not reproduce user-visibly (Claude). Elaine (operations) role scoping looks correct — no Users/Integrations for her.

---

## Questions for Tim / Kaitlin

1. **Tim (fixes P0-3):** can the pill selector derive the furthest completed/current workflow state (Export created / Downloaded / Customer delivery) instead of reading only `fulfillmentStatus`?
2. **Tim/Spencer (fixes P1-1):** which non-sensitive Fiserv portal URL to configure on staging before UAT?
3. **Kaitlin (pairs with P1-2):** should vault card rows say Available / Allocated / Delivered instead of Completed / In Progress, and should merchant stats show a Delivered count so Total reconciles?
4. **Grok Q5 — hide `/current-testing-instructions` for UAT?** The flag is on; the page is a full hidden QA pack (not in sidebar, URL-reachable).
5. **Behavior-vs-Figma:** the Walmart Figma frames (601:450–1573) still show denomination/quantity/"Generate Cards" and "you will be taken to Fiserve"; staging is generate-file + CSV import per the 8/12 ruling. Treat as behavior-wins, or refresh the Figma so the walkthrough deck matches the screen?
6. **Closed-order Walmart actions** ("Generate file" / "Import activated result") remain enabled on a Closed order — intentional re-run, or missed gating?
7. **"Ready to Allocate" while allocation is blocked** (PGC-1029: pill says Ready to Allocate, step says "Inventory is short," Allocate disabled) — right label?
8. **Users page red permission chips** (Allocate cards / Create exports / Download sensitive exports use error-red) — red-as-category vs red-as-error?

## P2/P3 (note-only, post-UAT)
Card Vault header collision + 8-step progress-bar wrap at 1280px; collapsed nav has no tooltips;
Allocated Cards renders all 120 rows inline; Clients emails wrap mid-word at 1280; step-language
drift (Drafted/Draft, Record Client Delivery vs Customer delivery vs Record Delivery); legacy
`/orders` `/vault` deep links redirect to dashboard; closed order still shows an enabled Payment
Status dropdown; merchant icon editor prominent on merchant pages.
