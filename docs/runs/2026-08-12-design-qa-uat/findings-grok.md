# Findings — design-qa-uat · recon · Grok

Lens: UAT walkthrough realism. Would a non-technical Progressive staffer know
what to do next? Date of inspection: 2026-08-12.

## 1. Method & coverage

- **Auth:** Logged in via the staging login form as `redstamp` (admin), then
  signed out and repeated dashboard + one order as `elaine` (operations). Did
  **not** reuse the operator Chrome profile; gstack browse was already in
  headless `launched` mode and had no session, so seed login was used.
- **Staging freshness gate: PASS.** `PGC-1027` showed a **Card Preparation**
  progress step between Paid and Allocated, with an expanded **Walmart Card
  Preparation** workflow card. Staging is Tim's 2026-08-12 build, not stale.
- **Tools:** gstack browse (`~/.claude/skills/gstack/browse/dist/browse`),
  viewport 1440×900, hard-refresh on first dashboard. No live Figma access —
  design comparison used static exports in `figma-frames/` only
  (`INDEX.md`: dashboard 564:1152, orders 601:2640, individual 601:123,
  Walmart steps 601:450 / 601:823 / 601:1196 / 601:1573, vault 601:3269,
  pills 421:1868).
- **Routes inspected (live):** `/login`, `/`, `/fulfillment`,
  `/requests/PGC-1027` (mutated end-to-end), `/requests/PGC-1028` (read-only),
  `/requests/PGC-1026` (read-only), `/requests/new` (create attempted, 500),
  `/users`, `/integrations/wordpress`, `/card-vault`,
  `/current-testing-instructions`.
- **Walmart path:** Generate file → (Fiserv button disabled, not clicked for
  a transaction) → file-upload of
  `PGC-1027-walmart-activated-result-120-valid.csv` → **500** → paste of the
  same file → 120 imported → allocate 120/120 → export → download → record
  delivery → close.
- **Core lifecycle on a fresh order:** blocked. `POST /requests/new` 500'd
  twice (with and without phone). Did not consume `PGC-1028` / `PGC-1029`.
  Completed allocate→export→download→delivery→close on `PGC-1027` after the
  Walmart import (this lane owns that mutation).
- **Could not cover:** live Figma; charts (none on the live dashboard);
  systematic table-hover width; inventory import profiles; standalone Card
  Preparation; Elaine walking allocate (left 1028/1029 for siblings).

**State change other lanes must know:** `PGC-1027` is now **Paid + Closed**.
Seeded “Needs Generation / 0 of 120” is gone.

---

## 2. P0 — UAT blockers

| id | route | finding | evidence | Figma ref | why P0 |
| --- | --- | --- | --- | --- | --- |
| G-P0-1 | `/requests/PGC-1027` Walmart Card Preparation | **Choose-file import of the designated valid 120-row CSV returns a full-page 500.** `POST /requests/PGC-1027?walmartError=input` → 500 in 5941ms, generic “This page couldn’t load / ERROR 777059612”. Order survived (reload OK) but no cards imported. Same file **pasted** into the textarea then imported successfully (`?walmartImported=120`). A non-technical user will use Choose file, not paste. | Live-inspected. `screens-grok/05-pgc-1027-import-result.png`, `04-pgc-1027-after-import.png` (empty-submit “needs review”), `07-pgc-1027-paste-import-result.png` (paste works). Network: POST 500. | 601:1196 / 601:1573 (import / success). | Walmart is the highest walkthrough-risk path. File upload is the obvious control. 500 on the blessed fixture is a derail. |
| G-P0-2 | `/requests/new` | **Create order 500s.** Filled a fake paid Starbucks × 2 order (`QA Walkthrough Client`) and submitted twice (with phone, then without). Both times: “This page couldn’t load / ERROR 294045514”. Order never appeared on `/fulfillment`. Console also: invalid phone `pattern` regex (`[0-9()+.\-\s]{7,20}` under `/v` flag). | Live-inspected. `screens-grok/10-new-manual-order.png`, `12-fresh-order-created.png`, `14-create-order-retry.png`. | n/a (behavior). | If the walkthrough starts “let’s make an order”, it dies on a white error page. |
| G-P0-3 | Dashboard, Orders, order header | **Status pills still do not match the order-screen steps** (Kaitlin 2026-08-12 + Tim “fixed” claim). Before import, `PGC-1027` progress said **Card Preparation** while the pill said **Needs Generation**. `PGC-1028` progress current step is **Allocated** while the pill says **Ready to Allocate**. `PGC-1026` progress is on **Download** while the pill still says **Allocated**. `src/lib/format.ts` still maps `needs_generation` → `"Needs Generation"`. | Live-inspected. `screens-grok/01-dashboard-redstamp.png`, `02-pgc-1027-walmart-freshness.png`, `19-pgc-1028-readonly.png`, `25-pgc-1026-pills.png`. Code read: `format.ts` lines 1–8. | 601:450 (Paid + Card Preparation), 601:123 (Paid + Export created), Kaitlin: pills match steps. | Explicit committed item, visibly unmet. Walkthrough will say “Card Preparation” while the list still says “Needs Generation”. |

---

## 3. P1 — fix before UAT if possible

| id | route | finding | evidence | Figma ref | why P1 |
| --- | --- | --- | --- | --- | --- |
| G-P1-1 | `/requests/PGC-1027` after successful import | Allocate card still shows a **red** “This order needs merchant preparation unless activated cards have already been imported into the vault.” The Walmart step above it has a green check and “120 … imported”. A staffer who just imported 120 cards is told they still need preparation. | Live-inspected. `screens-grok/07-pgc-1027-paste-import-result.png`. | 601:1573 (Allocate becomes current, no red warning). | High-frequency next-step confusion on the Walmart walkthrough. |
| G-P1-2 | `/requests/PGC-1027`, `/integrations/wordpress` | **Fiserv URL not set.** Walmart step shows a disabled “Fiserv URL not set” button. Integrations hero: “Fiserv URL / Missing / Not set” with placeholder `https://fiserv.example.com`. We did not transact in Fiserv (correct). The disabled button still looks unfinished if they demo Walmart. | Live-inspected. `screens-grok/02-pgc-1027-walmart-freshness.png`, `21-integrations.png`. | 601:450 helper “You will be taken to Fiserve…”. | Client will notice a disabled integration on the new step they asked for. |
| G-P1-3 | `/requests/new` | Page subtitle: **“Manually create a test order from the seeded gift card catalog.”** Visible from Dashboard **New Manual Order** (Elaine sees this too). Also: offering dropdown lists **Walmart · $25 twice**. | Live-inspected. `screens-grok/10-new-manual-order.png`. | n/a (hazard). | Language we do not want Progressive to see. |
| G-P1-4 | `/requests/PGC-1027` import | Import with **no file and no paste** returns a red “Walmart result import needs review. Check activated statuses, denominations, and matching Walmart Digital rows…” instead of “choose a file or paste rows.” Sounds like the operator ruined the data. | Live-inspected. `screens-grok/04-pgc-1027-after-import.png`. | n/a. | Alarming error on a normal missed click. |
| G-P1-5 | `/requests/PGC-1027` Walmart card | Unlabeled text box showing `PGC-1027` (name `walmartResultReference`, placeholder “Reference” only). Sitting between Generate file and the CSV upload with no visible label or help. | Live-inspected. `screens-grok/02-pgc-1027-walmart-freshness.png`. Snapshot `@e24`. | 601:450 has labeled Denomination / Quantity / Reference. | Non-technical user will not know whether to edit it. |
| G-P1-6 | `/fulfillment` @ 1440×900 | **Updated** column is clipped to a lone “U”. Dates `08.12.26` exist in the DOM (Kaitlin `00.00.00` format is implemented) but are not visible at laptop width. | Live-inspected. `screens-grok/09-orders-list.png`. Text dump includes `08.12.26`. | 601:2640 shows full `02.05.26`. | Primary orders table broken at the walkthrough laptop width. |

---

## 4. Verified-fixed (do not re-litigate)

- **Walmart Card Preparation is an order step between Paid and Allocated.** Freshness gate passed. Generate file produced an inline success and an audit “preparation file downloaded”.
- **Paste import of the 120-row valid file works** (`walmartImported=120`), inventory Available went 8 → 128, pill moved Needs Generation → Ready to Allocate, progress completed Card Preparation.
- **Allocate after import works** (120/120). Export → download → Record Delivery → Close sequential gating works. Cancel disables after download. Close pill becomes green **Closed**.
- **Paid pill is green** (old “Paid is blue” diagnosis stays dead).
- **Two header pills, not three “In Progress”.** `PGC-1026` = Paid + Allocated. `PGC-1028` = Paid + Ready to Allocate. Matches Kaitlin’s “2 total, not 3” even though the *words* still drift from the current step (G-P0-3).
- **Organization name under Client information is not a link**; only **View Client →**.
- **Users** uses the current navy buttons / metric tiles / role dropdowns (not a leftover old skin at 1440).
- **Tight dates `08.12.26`** are produced on the orders list (visibility is G-P1-6).
- **Elaine (operations)** sees Dashboard / Orders / Vault / Exports / Clients / Audit Log. No Users, no Integrations. Allocate is available. No extra debug chrome on her dashboard.
- **Fiserv stays outside the app** (disabled/missing URL, no in-app activation).

---

## 5. Questions for Tim / Kaitlin

1. Figma Walmart steps 1–4 still show denomination / quantity / “Generate Cards” and “you will be taken to Fiserve.” Staging is generate-file + CSV import, which matches the 8/12 product ruling. Treat as **behavior wins**, or does the Figma frame need a pass so the walkthrough deck matches the screen?
2. After export, should the fulfillment pill become **Export created** / **Downloaded** (Figma orders list) or stay **Allocated** until close? Today it stays Allocated from allocate through delivery.
3. Set a real-looking (non-transacting) Fiserv URL on staging before the client walkthrough so the button is not “Fiserv URL not set”?
4. Why two `Walmart · $25` offerings on `/requests/new`?
5. `/current-testing-instructions` is **not** in the sidebar, but the flag is on and the page is a full “Hidden QA…” pack. Hide it on staging for UAT, or leave URL-only?

---

## 6. P2 / P3 one-liners

- Progress first node is **Draft**; Figma says **Drafted**. Same for payment option “Draft”.
- Step title **Record Client Delivery** vs progress **Customer delivery** vs button **Record Delivery** vs option **Delivered to client**.
- After download, step 5 subtitle still says “Download an export before recording customer delivery.”
- After allocate, Cards Ordered **Available** drops back to a red **8** (leftover unused Walmart stock) and looks like a shortage.
- Card Vault headers **Available** and **Allocated** collide at 1440 (`screens-grok/23-card-vault.png`). Button is **Prepare Cards**, Figma **Generate Cards**.
- Integrations connection labeled **Staging WordPress Test**.
- New-order phone `pattern` is an invalid regex (console error); code at `requests/new/page.tsx` and `clients/client-form.tsx`.
- Generate file has no persistent “download again” link, only inline success.
- Closed order still shows an enabled Payment Status dropdown.
- No charts on the live dashboard, so Kaitlin’s `00.00.00` chart-date note is N/A here.

---

## Coverage note

All P0/P1 rows above are **live-inspected** on staging, not inferred from code (code cites are extra). File-upload 500 and create-order 500 were each reproduced; they are not single-shot flakes.
