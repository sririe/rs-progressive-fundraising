---
type: qa
category: design-dev-reconciliation
date: 2026-08-12
status: complete
lane: codex
tags:
  - progressive-card-vault
  - design-qa
  - pre-uat
  - figma-fidelity
key_insights:
  - Staging passed the Walmart Card Preparation freshness gate.
  - Advanced order states still display the fulfillment database state instead of the current workflow step.
  - Orders clips its Updated column at 1280px; Card Vault headers also crowd at that width.
  - The Fiserv action is implemented but disabled because staging has no portal URL configured.
---

# Codex findings — Figma fidelity + P0 closure

## 1. Method & coverage

**Verdict: not ready for client UAT.** The Walmart step itself is deployed and usable, but two P0s remain on core routes: advanced workflow pills lag the actual order step, and the Orders table clips its rightmost column at 1280px.

- Authenticated to staging as seeded `redstamp` admin.
- Hard-refreshed each route before judging it.
- **Freshness gate passed:** `/requests/PGC-1027` showed `Card Preparation` between `Paid` and `Allocated` at 1440×900. Evidence: `screens-codex/staging-walmart-pgc-1027-freshness.png`.
- Live-inspected staging routes: `/`, `/fulfillment`, `/requests/PGC-1026`, `/requests/PGC-1027`, `/card-vault`, `/users`, and `/integrations/wordpress`.
- Checked core routes at 1440×900 and 1280×800. No page-level horizontal overflow was reported, but route-level content clipping/crowding was visible at 1280px as noted below.
- Live-inspected Figma screenshots for nodes `564:1152`, `601:2640`, `601:123`, `601:450`, `601:823`, `601:1196`, `601:1573`, `601:3269`, and `421:1868`. The matching live captures are saved under `screens-codex/figma-live-*.png`; static exports were also present in `figma-frames/`.
- Compared pill behavior with app commit `08c0c74`, especially `src/lib/format.ts`, and inspected the order/Walmart UI code only where the brief explicitly required state verification.
- Browser console/page-error checks were clean on the inspected routes.

**Coverage limitation:** I live-exercised preparation-file generation and observed its inline success message. I did not replay the activated-result import because another concurrent QA lane advanced the shared `PGC-1027` fixture from Needs Generation through Closed during this pass. I observed the resulting allocated/closed state and audit entries live; the transient import loading and inline success states were verified from `walmart-result-import-form.tsx`, not personally captured live. I did not reset the shared database or create conflicting inventory.

## 2. P0 findings

| ID | Route | Finding | Evidence | Figma ref | Why P0 |
| --- | --- | --- | --- | --- | --- |
| C-P0-01 | `/`, `/fulfillment`, `/requests/PGC-1026` | **The workflow pill lags the order's real step.** `PGC-1026` shows `Allocated` on Dashboard, Orders, and its order header even though the detail workflow shows `Export created` complete and `Download` current. Code confirms all three surfaces label only `fulfillmentStatus`, so delivery/export progress cannot appear until the order becomes `Closed`. The two-pill cap is correct; the workflow pill semantics are not. | `screens-codex/staging-dashboard.png`; `screens-codex/staging-orders.png`; `screens-codex/staging-order-pgc-1026.png`; live-inspected and code-confirmed | `564:1152`, `601:2640`, `601:123`; Kaitlin 8/12 ruling | Misleading status language on every core order surface, and an explicitly committed P0 is only partially closed. A client can see two different states on the same order screen. |
| C-P0-02 | `/fulfillment` | **Orders clips the Updated column at 1280px.** At 1280×800 the card ends after Total Value; only the first letter of the `Updated` heading is visible at the right edge and all update dates are hidden. There is no page-level horizontal scrollbar (`scrollWidth === clientWidth`), so the data is not recoverable by scrolling. The same route is complete at 1440px. | `screens-codex/staging-orders-1280.png`; compare `screens-codex/staging-orders.png`; live-inspected | `601:2640` | This is a broken layout on the highest-frequency table at an explicitly in-scope laptop width. It hides a full data column and would be obvious in UAT. |

## 3. P1 findings

| ID | Route | Finding | Evidence | Figma ref | Why P1 |
| --- | --- | --- | --- | --- | --- |
| C-P1-01 | `/requests/PGC-1027`, `/integrations/wordpress` | **The external Fiserv action is visibly unavailable on staging.** The Walmart step renders a disabled `Fiserv URL not set` control; Integrations reports `Fiserv URL — Missing / Not set`. The conditional external-link treatment is implemented correctly, but the staging environment is not configured. Operators can still navigate to Fiserv outside the app, so this is not a functional dead end. | `screens-codex/staging-walmart-pgc-1027-freshness.png`; `screens-codex/staging-integrations-wordpress.png`; live-inspected | `601:450`, `601:823`, `601:1196`, `601:1573` | A disabled core-path control would be conspicuous in the Walmart walkthrough and weaken confidence, but activation remains intentionally external and can be reached independently. |
| C-P1-02 | `/card-vault` | **Card Vault column headers collide at 1280px.** `Available` and `Allocated` render without visible separation (`AvailableAllocated`), although row values remain readable. The 1440px layout is clean. | `screens-codex/staging-card-vault-1280.png`; compare `screens-codex/staging-card-vault.png`; live-inspected | `601:3269` | This is a noticeable polish/legibility regression on a high-frequency route at laptop width, but it does not hide the underlying inventory values. |

## 4. Kaitlin 8/12 checklist

| Item | Result | Verification |
| --- | --- | --- |
| Walmart step between Paid and Allocated | **Confirmed fixed** | Live freshness gate passed on `PGC-1027`; rail placement, inline step card, generated-file action, activated-result upload/paste controls, and sequential gating match the intended Figma structure. |
| Generate/download, loading/success, activated-result import | **Confirmed fixed with stated coverage limit** | Preparation file generation was live-exercised and displayed `Walmart/Fiserv preparation file has been generated.` Import controls were live-visible. Import loading/success components are code-confirmed; another lane completed the shared fixture before I could capture the transient states. |
| External Fiserv treatment | **Partially fixed — C-P1-01** | Correct conditional external-link treatment exists, but staging has no configured URL and therefore displays a disabled control. |
| Semantic status pills + max two on order header | **Partially fixed — C-P0-01** | Paid, Needs Generation, Ready to Allocate, Allocated, and Closed labels are semantic; filters also use semantic labels. Individual order headers show exactly two pills. Export/download/delivery-stage orders still show `Allocated`, so the workflow pill does not always match the screen's current step. |
| Users styling | **Confirmed fixed** | `/users` uses the current shell, surfaces, button colors, pill shapes, and deep-blue/bright-blue/red token family. Evidence: `screens-codex/staging-users.png`. |
| Integrations styling | **Confirmed fixed** | `/integrations/wordpress` uses the current shell, stat cards, form surfaces, buttons, and pill treatment. Evidence: `screens-codex/staging-integrations-wordpress.png`. |
| Tight date format `00.00.00` | **Confirmed fixed** | Orders shows dates such as `08.12.26`; `formatCompactDate()` returns `MM.DD.YY` and is used by Orders, Clients, merchant detail, Exports, and Audit Log. |
| Full-width grey table hover | **Confirmed fixed on high-frequency tables** | Hover fills the full inset row width on Orders and Card Vault, not only the text. Evidence: `screens-codex/staging-orders-row-hover.png`, `screens-codex/staging-card-vault-row-hover.png`. |
| Client name not clickable under Client information | **Confirmed fixed** | Organization names are static text; the separate `View Client` link remains. Evidence: `screens-codex/staging-order-pgc-1026.png`. |
| Cards Ordered rows do not highlight | **Confirmed fixed** | The informational row remained transparent before and after hover (`rgba(0, 0, 0, 0)`). Evidence: `screens-codex/staging-order-cards-row-hover.png`. |

## 5. Route-by-route fidelity summary

| Surface | Result |
| --- | --- |
| Dashboard · `564:1152` | Layout, stat strip, open-orders card, activity card, spacing, colors, and pill tokens are close at 1440px. Workflow labels inherit C-P0-01. |
| Orders · `601:2640` | Close at 1440px; search language, filters, compact dates, semantic basic states, and hover are correct. Fails at 1280px due C-P0-02. |
| Order detail · `601:123` | Two-column structure, step cards, disclosure defaults, client/card sections, and 1280px reflow are close. Header status inherits C-P0-01. |
| Walmart steps · `601:450`, `601:823`, `601:1196`, `601:1573` | Step placement and card structure are close; implementation correctly derives denomination/quantity from order line items and adds the explicit import UI absent from the visual-only Figma sequence. External action inherits C-P1-01. |
| Card Vault · `601:3269` | Close at 1440px; tabs, search/filter, logos, denomination chips, full-row hover, and table treatment are coherent. Header legibility degrades at 1280px per C-P1-02. |

## 6. Questions for Tim / Kaitlin

1. **Tim:** Can the status-pill selector derive the furthest completed/current workflow state across fulfillment + delivery (for example `Export created`, `Downloaded`, `Customer delivery`) instead of reading only `fulfillmentStatus`? This appears to be the root of C-P0-01.
2. **Tim / Spencer:** Which non-sensitive Fiserv portal URL should be configured on staging before UAT? The code path is present; this looks like environment setup rather than missing UI.
3. **Kaitlin:** `421:1868` still visually contains generic sample labels (`In Progress`, `Completed`). I treated that node as token/color reference only because the 8/12 semantic-language ruling is newer and binding.

## 7. P2 / P3 notes

- **P2:** Orders subtitle still says `Track request payment...` while the visible product language has otherwise moved from requests to orders.
- **P3 / Figma hygiene:** Walmart Figma frames still include the superseded sentence implying the app takes the operator to Fiserv. Staging correctly uses the settled external-boundary copy instead.

