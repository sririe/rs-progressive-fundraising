---
title: "Card Vault — UI String Inventory & Language Audit"
type: reference
category: internal-design
date: 2026-07-14
status: ready-for-rulings
audience: internal (design team, Tim, Spencer) — not client-sent
---

# Card Vault — UI String Inventory & Language Audit

**Date:** 2026-07-14 · **Source:** `gitlab.com/rs-dev/progressive-gift-cards-card-vault` @ `bd1f16d` (2026-07-14)
**For:** Candace + Kaitlin (rulings), Hannah (ratification), Tim (application)
**Companion docs:** `2026-07-14-design-glossary.md` (the rulings land there), `2026-07-14-design-primer.md`

## How to use this document

Every user-facing string in the prototype is inventoried below. The work happens top-down:

1. **Section 1 — Glossary rulings.** Term-level decisions that cascade through everything else.
   Rule on these first; each resolves dozens of strings at once. **This section is a worklist —
   rulings are recorded only in `2026-07-14-design-glossary.md`, never here.**
2. **Section 2 — Flagged strings.** Specific strings with a defect (dev language leaking through,
   inconsistency, machine-optimization) and a proposed replacement. Accept, amend, or reject each —
   except rows marked LOCKED, which designers route to Progressive rather than rule on.
3. **Section 3 — Full inventory.** Every user-facing string, by screen. Paths are relative to the
   prototype repo's `src/`; repeated strings are consolidated into one row with a ×N count, and
   long runs of similar fields are grouped with line ranges — Tim applies changes from the source,
   where every pointer resolves unambiguously. Anything not flagged in Sections 1–2 was judged fine
   as built — but designers should skim their screen's table and challenge anything that reads wrong.

**Credit where due:** most of this prototype's copy is already good. Tim's style guide has an explicit
Content Style section (voice, capitalization, five terminology rulings), and the blocked-state helpers
("Download the approved export before recording customer delivery.") are exactly the standard. This
audit extends that foundation; it doesn't replace it.

**Two constraint classes to respect:**

- **Most output CSV column headers are not free to rename — locked per profile, not globally.** The
  Loblaws/Shoppers, Shoppers, and Amazon workbook headers mirror files Progressive's clients already
  consume; the Walmart work-file headers feed the external Fiserv activation process. Renaming any of
  those is a Progressive conversation, not a design call (§3.15 marks them LOCKED, with why). The
  **Generic internal CSV** is Redstamp-internal and its headers are renameable like any UI string.
- **The Card Preparation screen (`/card-vault/generation`) is placeholder UI** by Tim's own docs — it
  gets redesigned around Walmart preparation-file generation, not re-worded. Its strings are inventoried
  (§3.6) but excluded from the language pass.

---

## Section 1 — Glossary rulings needed (decide these first)

| # | Term as built | The question | Evidence to weigh | Ruling |
|---|---------------|--------------|-------------------|--------|
| 1 | **Vendor** | Vendor vs **Merchant** vs Supplier — the word for Amazon/Walmart/Loblaws etc. Appears in nav, headings, columns, forms (~30 strings). | **Default: Merchant** — the repo's design canon uses *merchant* exclusively, the client-facing workflows doc (reviewed by Lloyd 7/14) says *Merchant*, and Tim's style guide says "official *merchant* capitalization." The `Gift Card Vendor` CSV header is a locked format exception, not counter-evidence. Confirm operators don't say "supplier" (Lloyd's emails sometimes do), then ratify. | Default: Merchant — confirm & ratify |
| 2 | **Client / Customer** | The app uses both: the *Clients* area vs the *Customer* column on requests, "Customer email," "Delivered to customer." Same party — the fundraising organization ordering cards. | Tim's rule: "use customer or client consistently within a section." A cleaner rule may be: **Client** = the account/organization; **Customer delivery** = the handoff act. Or collapse to one word everywhere. | _____ |
| 3 | **Fulfillment / Fulfillment Requests / Requests** | The nav says *Fulfillment Requests*, the page title says *Fulfillment*, the dashboard says *Digital Gift Card Fulfillment*, detail pages say *Fulfillment request*. One name, used everywhere. | "Request" is Tim's ruled term for the record. The list page should probably just be **Requests** or **Fulfillment Requests** in both nav and title. | _____ |
| 4 | **Denomination** | Do Progressive operators say "denomination," or do they say value/amount? (~15 strings + CSV headers.) | Gift-card industry standard is *denomination*; Lloyd's materials use it. Likely keep — confirm at the Doug/Lloyd call, don't assume. | _____ |
| 5 | **Allocate / Allocated** | Keep as the word for reserving cards to a request? | Keep. Lloyd's 7/14 email uses "allocation" unprompted — it's already Progressive's word. Ruling here is just to make it official. | _____ |
| 6 | **Quarantine** | Keep as the word for pulling an invalid card out of circulation? | Precise and safe (a quarantined card never returns to inventory — the word carries that). Keep, but add first-use helper text near the action. | _____ |
| 7 | **Export / Export package** | The app alternates ("Create export," "Export package created," "Export packages"). Pick one. | "Export" alone is probably enough; "package" adds no meaning for a single CSV. If multi-file ZIPs arrive (Amazon PDF/ZIP), "package" may earn its place — decide with that future in view. | _____ |
| 8 | **Activation boundary** | — | — | **RULED** — see glossary "Ruled" table: the app prepares files and imports activated results; only Progressive activates. Listed here only to keep numbering; audit new copy against it. |
| 9 | **Offering** | "Catalog offerings," "Gift card offering," "Offering" column — the vendor+type+denomination combination a client can order. | Keep — "offerings" is Doug's own word (6/16 email: "active offerings"). Standardize casing and use. | _____ |
| 10 | **Empty-value convention** | The app shows "Not provided," "Not applicable," "–", "Never," "No vendor," "No cards requested" for absent data. | Pick one primary convention ("Not provided" for missing data, "—" for empty cells) and apply it; keep genuinely distinct meanings (e.g. "Never" for last-used) only where the distinction informs. | _____ |

---

## Section 2 — Flagged strings (defect + proposal, ruled individually)

**P1 — dev/internal language leaking into the product:**

| Where | Current | Problem | Proposed | Source |
|-------|---------|---------|----------|--------|
| Dashboard metric detail | "Seeded local test inventory" | Dev-environment language on the operator dashboard | "All card inventory" (or drop the detail line) | `src/app/page.tsx:132` |
| New request page description | "Manually create a test request from the seeded gift card catalog." | "test request" + "seeded catalog" are dev concepts | "Create a request on behalf of a client from the current card catalog." | `src/app/requests/new/page.tsx:61` |
| Browser tab title | "Progressive Gift Cards Admin" | "Admin" is builder-perspective; every role sees this title | "Progressive Gift Cards — Card Vault" | `src/app/layout.tsx:5` |
| Sidebar caption (signed-out fallback) | "Card vault V1" | Version tag shown to users | "Card Vault" | `src/components/app-shell.tsx:124` |
| WordPress connection label placeholder | "Pantheon Multidev to Staging" | Hosting-vendor jargon as the example | "Main website" (a realistic connection name) | `src/app/integrations/wordpress/page.tsx:143` |
| Request cancel section title | "Danger zone" | Developer idiom (GitHub-ism) | "Cancel this request" | `src/app/requests/[requestNumber]/page.tsx:1040` |
| Audit message | "{req} payment status changed to {status}" — interpolates the raw enum (`payment_pending`) | Machine value shown where the label exists | Route through the existing `labelPaymentStatus()` → "Payment pending" | `src/app/requests/[requestNumber]/actions.ts:108` |

**P2 — inconsistencies (one ruling, applied everywhere):**

| Where | Current | Problem | Proposed | Source |
|-------|---------|---------|----------|--------|
| Nav vs page titles | "Fulfillment Requests" (nav) / "Fulfillment" (list title) / "Digital Gift Card Fulfillment" (dashboard title) / "Fulfillment request" (detail eyebrow) | Four names for one area | Glossary ruling #3, then align all four | `app-shell.tsx:54`, `fulfillment/page.tsx:247`, `page.tsx:214` |
| Exports table column | "Exporter" | Reads like a machine role | "Exported by" (matches the CSV header already named `Exported By`) | `src/app/exports/page.tsx:66` |
| Shipping form card title | "Shipping details optional" | Missing punctuation — reads as one phrase | "Shipping details (optional)" | `src/app/requests/new/page.tsx:248` |
| Empty-value fallbacks | "Not provided" / "Not applicable" / "–" / "No vendor" / "No cards requested" | Mixed conventions | Glossary ruling #10, then align | multiple (see §3) |
| Loblaws CSV header | "Gift Card Pin" | Casing inconsistent with "PIN" elsewhere | LOCKED — not a design ruling; flag to Progressive, since it may mirror the file their clients already receive | `merchant-output-profiles.ts:52` |
| Preparation language outside the placeholder screen | "Generate cards" button (`card-vault/page.tsx:138`), "Digital generators" stat (`card-vault/page.tsx:157`), "Needs generation" status (`format.ts:6`), "…complete any required generation step first" (`requests/[requestNumber]/page.tsx:427`) | The placeholder *screen* is excluded from this pass, but these strings live on non-placeholder surfaces and say "generate" where the ruled boundary says "prepare" | "Prepare cards" · "Preparation merchants" · "Needs preparation" · "…complete any required preparation step first" | see left |

**P3 — worth a designer look, not defects:**

| Where | Current | Consideration | Source |
|-------|---------|---------------|--------|
| Form placeholder examples | "Northstar Foods," "Elaine," "Sample," "ops@example.com" | Fine as examples — but Progressive's clients are schools, teams, community groups. Examples that look like their world ("Maple Ridge Elementary PAC") make the form self-explaining. | `requests/new/page.tsx:77–124` |
| Delivery status | "Internally downloaded" | Matches Tim's ruled distinction (downloaded internally ≠ delivered to customer) but reads stiffly; "Downloaded (internal)" or "Downloaded — not yet delivered" may scan better in a badge. Keep the distinction either way. | `format.ts:29` |
| Login helper | "Use your assigned account to access the card vault." | Good. Only consider adding who to contact when locked out (there's no self-serve reset — Admin resets passwords). | `login/page.tsx:36` |
| Quarantine action | "Quarantine and replace" | Keep the term (ruling #6), but the button does two things; when no replacement inventory exists the second half silently fails into "Needs replacement." Consider stating the outcome in the confirmation. | `requests/[requestNumber]/page.tsx:863` |
| Import profile names | "URL + Account Number + PIN," "Amazon Claim Code," etc. | Machine-flavored, but Lloyd's own 7/14 email quotes them verbatim ("04 URL + Account # + PIN") — these names are already the shared vocabulary with the client. Keep. | `merchant-import-profiles.ts` |

---

## Section 3 — Full inventory by area

Legend: kind · string · source · context. Strings flagged above are not repeated with proposals here.
"LOCKED" tables are client-format-bound — do not rename without Progressive sign-off.

### 3.1 App shell & navigation

| Kind | String | Source | Context |
|------|--------|--------|---------|
| heading | Progressive Gift Cards | app-shell.tsx:99 | default eyebrow above every page title |
| helper | {Role} access | app-shell.tsx:124 | sidebar caption, e.g. "Admin access" |
| helper | Card vault V1 | app-shell.tsx:124 | sidebar fallback — flagged P1 |
| nav | Dashboard | app-shell.tsx:42 | sidebar |
| nav | Card Vault | app-shell.tsx:48 | sidebar |
| nav | Fulfillment Requests | app-shell.tsx:54 | sidebar — glossary #3 |
| nav | Closed Requests | app-shell.tsx:60 | sidebar |
| nav | Exports | app-shell.tsx:66 | sidebar, admin/operations |
| nav | Clients | app-shell.tsx:72 | sidebar |
| nav | Users | app-shell.tsx:78 | sidebar, admin |
| nav | Integrations | app-shell.tsx:84 | sidebar, admin |
| nav | Audit Log | app-shell.tsx:90 | sidebar, admin/operations |
| button | Sign out | app-shell.tsx:177 | header |
| label | Pro Gift Cards | login/page.tsx:24, app-shell.tsx:109,153 | logo alt text ×3 |
| heading | Progressive Gift Cards Admin | layout.tsx:5 | browser tab — flagged P1 |
| helper | Internal card vault and fulfillment workbench. | layout.tsx:6 | metadata description |
| empty-state | No rows match the current search. | filterable-table.tsx:50 | default for all tables |
| placeholder | Search table | filterable-table.tsx:52 | default search placeholder |

### 3.2 Dashboard (/)

| Kind | String | Source | Context |
|------|--------|--------|---------|
| heading | Digital Gift Card Fulfillment | page.tsx:214 | page title — glossary #3 |
| helper | Digital requests, vault inventory, allocation, and exports. | page.tsx:213 | page description |
| button | Import cards | page.tsx:197 | header action |
| button | New request | page.tsx:206 | header action |
| label | Open requests | page.tsx:122 | metric card |
| helper | {n} active workflows | page.tsx:125 | metric detail |
| label | Available cards | page.tsx:128 | metric card |
| helper | Seeded local test inventory | page.tsx:132 | flagged P1 |
| helper | Digital inventory only | page.tsx:133 | metric detail (physical disabled) |
| label | Allocated value | page.tsx:136 | metric card |
| helper | Reserved for fulfillment | page.tsx:139 | metric detail |
| label | Paid requests | page.tsx:142 | metric card |
| helper | Payment manually confirmed | page.tsx:145 | metric detail |
| status | No vendor | page.tsx:180 | request row fallback — glossary #1/#10 |
| heading | Open fulfillment requests | page.tsx:242 | list card title |
| helper | Showing the 10 most recently updated open requests. | page.tsx:245 | list subtitle |
| button | View All | page.tsx:254,335 | ×2 links |
| status | No cards requested | page.tsx:277 | row fallback — glossary #10 |
| helper | Updated {date} | page.tsx:308 | row timestamp |
| empty-state | No open fulfillment requests. | page.tsx:316 | list empty state |
| heading | Recent activity | page.tsx:327 | audit feed title |

### 3.3 Login (/login)

| Kind | String | Source | Context |
|------|--------|--------|---------|
| heading | Sign In | login/page.tsx:34 | form heading |
| helper | Use your assigned account to access the card vault. | login/page.tsx:36 | subtitle — P3 note |
| error | Your previous session needs to be refreshed. Sign in again to continue. | login/page.tsx:42 | expired-session banner |
| error | Check your username or email and password, then try again. | login/page.tsx:49 | failed-login banner |
| label | Username or email | login/page.tsx:56 | field |
| label | Password | login/page.tsx:67 | field |
| button | Sign in | login/page.tsx:79 | submit |

### 3.4 Card Vault (/card-vault)

| Kind | String | Source | Context |
|------|--------|--------|---------|
| heading | Card Vault | card-vault/page.tsx:145 | page title (eyebrow on subpages ×4) |
| helper | Review inventory by card type and vendor before drilling into individual cards. | card-vault/page.tsx:144 | page description — glossary #1 |
| button | Back to dashboard | card-vault/page.tsx:130 (+6 more routes) | ×7 header action |
| button | Import cards | card-vault/page.tsx:135 (+3) | ×4 |
| button | Generate cards | card-vault/page.tsx:138 | links to placeholder screen — see §3.6 note |
| label | Total cards / Total digital cards | card-vault/page.tsx:151 | stat, flag-dependent |
| label | Available | card-vault/page.tsx:155 (+2) | ×3 stat |
| label | Allocated | card-vault/page.tsx:156 (+2) | ×3 stat |
| label | Digital generators | card-vault/page.tsx:157 | stat — machine-y; screen owning it is placeholder |
| heading | Digital cards / Physical cards | card-vault/page.tsx:34–35 | group headings |
| helper | {n} denominations | card-vault-overview.tsx:37 | vendor tile — glossary #4 |
| label | Total | card-vault-overview.tsx:54 | tile stat |
| label | Available by denomination | card-vault-overview.tsx:60 | tile sub-list |
| placeholder | Search vendors, card types, or denominations | card-vault-overview.tsx:125 | sticky search — glossary #1/#4 |
| helper | {x} of {y} vendors shown. | card-vault-overview.tsx:145 | filter count |
| empty-state | No vendors match the current search. | card-vault-overview.tsx:160 | search empty state |

### 3.5 Vendor detail (/card-vault/[vendorId])

| Kind | String | Source | Context |
|------|--------|--------|---------|
| button | Back to vault | [vendorId]/page.tsx:96 (+1) | ×2 |
| helper | {cardType} inventory for {vendor}. | [vendorId]/page.tsx:105 | page description |
| label | Quarantined / Denominations | [vendorId]/page.tsx:114–115 | stats |
| heading | Vendor inventory | [vendorId]/page.tsx:132 | table title — glossary #1 |
| column | Card number / PIN / Denomination / Status / Issue / Batch / Created | [vendorId]/page.tsx:140–146 | table headers |
| placeholder | Search {vendor} | [vendorId]/page.tsx:149 | table search |

### 3.6 Card Preparation (/card-vault/generation) — PLACEHOLDER SCREEN, excluded from language pass

Tim's docs mark this whole screen for redesign around Walmart preparation-file generation + activated-result
import. Strings inventoried for completeness only; the redesign (phase 2+) replaces them. Note the screen
already models the ruled language ("Preparation only," "Activation remains outside the app").

| Kind | String | Source |
|------|--------|--------|
| heading | Card Preparation | generation/page.tsx:65 |
| helper | Stage Walmart file-preparation work without activating cards inside the app. | generation/page.tsx:63 |
| toast | Generated {n} test Walmart digital cards in batch {batch}. This is staging test inventory only; production Walmart cards should come back through activated result import. | generation/page.tsx:69–73 |
| label/status | Generation vendors · Workflow status · Preparation only · Inventory impact · Result import | generation/page.tsx:85–98 |
| helper | Digital only, Walmart for V1 · Activation remains outside the app · Activated cards return through import | generation/page.tsx:88–100 |
| heading | Walmart preparation placeholder | generation/page.tsx:130 |
| helper | This staging-only test tool keeps Walmart work separate from inventory import. In production, the app should prepare the Walmart/Fiserv work file, Progressive should run activation externally, and activated result files should be imported back into the vault. | generation/page.tsx:133–138 |
| labels/placeholders | Vendor · Denomination ($25) · Quantity (100) · Reference (PGC-1027 or invoice number) · Generation notes | generation/page.tsx:143–199 |
| button | Generate test cards | generation/page.tsx:208 |
| heading | Preparation-enabled vendors | generation/page.tsx:218 |
| helper | Physical cards are not part of the V1 digital workflow. Walmart activation is not performed by this app unless separately scoped. | generation/page.tsx:221–223 |
| empty-states | No generation vendors configured · No vendors are currently configured for generation. | generation/page.tsx:156,239 |
| errors | Denomination is required. · Quantity is required. · Reference is required. · Vendor is required. · Enter a valid denomination. · Denomination must be greater than zero. · Quantity must be a whole number. · Quantity must be at least 1. · Generate 500 or fewer test cards at a time. · Check the generation form values. · Test generation is currently limited to Walmart Digital. | generation/actions.ts:15–82 |

### 3.7 Inventory Import (/inventory/import)

| Kind | String | Source | Context |
|------|--------|--------|---------|
| heading | Inventory Import | import/page.tsx:62 | page title |
| helper | Paste vendor-provided card rows, preview them, and import valid cards into the vault. | import/page.tsx:60 | description — glossary #1 |
| toast | Imported {n} cards. Skipped {d} duplicates and {u} unmatched rows. | import/page.tsx:67–69 | success banner |
| error | No valid rows were found. Check that the CSV includes vendor, card type, denomination, and card number. | import/page.tsx:74–76 | banner |
| error | Import blocked. Resolve {n} validation issue(s) shown in the preview, then try again. | import/page.tsx:80–83 | banner |
| error | Import blocked. Resolve {n} unmatched catalog row(s) shown in the preview, then try again. | import/page.tsx:87–89 | banner |
| label | Catalog offerings | import/page.tsx:97 | stat — glossary #9 |
| helper | Import rows must match an existing vendor and card type. | import/page.tsx:103 | stat detail |
| label | Available cards | import/page.tsx:110 | stat |
| helper | Cards currently available for allocation. | import/page.tsx:116 | stat detail |
| heading | Paste inventory CSV | import/page.tsx:125 | form title |
| helper | Required headers: Vendor, Card Type, Denomination, and one card value column such as Card Number, Gift Card URL, Claim Code, or Account Number. Optional recognized fields include PIN, Serial Number, Challenge Code, Token, Reference ID, Merchant ID, Idempotency Key, Transaction Status, and Expiry. | import/page.tsx:129–133 | CSV instructions |
| label | Import profile | inventory-import-preview.tsx:89 | profile select |
| status | Primary: {field type} · Output: {mode} · External activation step | inventory-import-preview.tsx:108–115 | profile pills — "Primary: {field}" surfaces underscore-mangled enum text; align with ruling #8 language |
| status | {n} rows ready to import · {n} blocked · {n} warning(s) | inventory-import-preview.tsx:128–132 | preview summary |
| button | Choose CSV | inventory-import-preview.tsx:150 | file picker |
| heading | Detected columns | inventory-import-preview.tsx:161 | mapping panel |
| helper | Known merchant fields will be encrypted into the vault. Unmatched columns are ignored for now. | inventory-import-preview.tsx:162–165 | mapping description |
| status | Encrypted | inventory-import-preview.tsx:180 | sensitive-column badge |
| empty-state | Add a CSV header row to begin. | inventory-import-preview.tsx:187 | no columns yet |
| helper | Imports are blocked until every row has valid required fields, no duplicates, and a matching catalog vendor/type. Warnings can be imported only when there are no blocking errors. | inventory-import-preview.tsx:192–194 | blocked-state explainer |
| heading | Rows needing review | inventory-import-preview.tsx:199 | issues panel |
| error | Row {n}: [Warning – ]{message} | inventory-import-preview.tsx:203–205 | per-row issue |
| error | Catalog match: {vendor} / {type} is not in the current catalog. | inventory-import-preview.tsx:210–212 | unmatched row |
| heading | Preview | inventory-import-preview.tsx:219 | preview table |
| helper | Showing {n} rows | inventory-import-preview.tsx:221 | row count |
| column | Vendor · Type · Denomination · Card number · PIN · Fields · Expiry · Catalog | inventory-import-preview.tsx:228–235 | preview headers |
| status | Matched / Review | inventory-import-preview.tsx:262 | catalog badges |
| error | Paste at least one CSV row. | import/actions.ts:17 | validation |

### 3.8 Fulfillment list (/fulfillment)

| Kind | String | Source | Context |
|------|--------|--------|---------|
| heading | Fulfillment | fulfillment/page.tsx:247 | page title — glossary #3 |
| helper | Track request payment, allocation, and export readiness. | fulfillment/page.tsx:246 | description |
| button | New request | fulfillment/page.tsx:241 | header action |
| nav | All / Physical / Digital | fulfillment/page.tsx:226–228 | type tabs (flag-dependent) |
| label | Fulfillment request type | fulfillment/page.tsx:255 | tab aria-label |
| heading | Fulfillment requests / Digital fulfillment requests | fulfillment/page.tsx:280–281 | card title, flag-dependent |
| helper | Showing {a}–{b} of {n} requests. | fulfillment/page.tsx:284 | pagination count |
| placeholder | Search requests, customers, status, or cards | fulfillment/page.tsx:300 | search input |
| button | Search / Clear | fulfillment/page.tsx:307–311 | search controls |
| column | Request · Customer · Type · Cards · Payment · Status · Allocated · Exported · Value · Updated | fulfillment/page.tsx:328–371 | table headers — glossary #2 |
| status | Yes / No | fulfillment/page.tsx:201 | Exported cell |
| empty-state | No requests match the current search. | fulfillment/page.tsx:377 | with active search |
| empty-state | No fulfillment requests found. | fulfillment/page.tsx:378 | no search |
| helper | Page {x} of {y} | fulfillment/page.tsx:386 | pagination |
| button | Previous / Next | fulfillment/page.tsx:398–416 | pagination |

### 3.9 Request detail (/requests/[requestNumber])

| Kind | String | Source | Context |
|------|--------|--------|---------|
| heading | Fulfillment request | page.tsx:389 | eyebrow — glossary #3 |
| toast | Customer delivery recorded. The request can now be closed after final review. | page.tsx:395 | banner |
| toast | Request cancelled and retained for audit history. | page.tsx:400 | banner |
| toast | The invalid card was quarantined and a replacement was allocated. Create a corrected export before redelivery. | page.tsx:404 | banner |
| toast | The invalid card was quarantined. Matching replacement inventory is required. | page.tsx:409 | banner |
| error | This request cannot be cancelled because sensitive data was already downloaded or delivered. | page.tsx:414 | banner |
| error | Download the approved export before recording customer delivery. | page.tsx:419 | banner — the house-style exemplar |
| error | Allocation was not completed because matching inventory is short. | page.tsx:423 | banner |
| error | This request is not eligible for allocation. Confirm payment and complete any required generation step first. | page.tsx:427 | banner — "generation step" vs ruling #8 "preparation" |
| error | Vendor preparation is still required. Import the activated result file before allocating this request. | page.tsx:432 | banner |
| error | A customer export cannot be created until all required cards are allocated or replaced. | page.tsx:437 | banner |
| error | Record customer delivery before closing this request. | page.tsx:442 | banner |
| heading | Client information | page.tsx:448 | card — glossary #2 |
| button | View client | page.tsx:451 | link |
| label | Company / organization · Contact name · Email · Phone · Delivery type · Preferred delivery · Payment method · Purchase order · Submitted order total · Source · Source entry | page.tsx:259–274 | client info fields |
| helper | Not provided (×10) · Not applicable | page.tsx:80,274 | fallbacks — glossary #10 |
| label | Pro Gift Cards WordPress Site / Manual entry | page.tsx:255–257 | source names |
| label | WordPress site: {url} | page.tsx:487 | source detail |
| label | Billing address · Shipping details · Notes | page.tsx:496–524 | info blocks |
| heading | Workflow | page.tsx:533 | step tracker |
| helper | Request created and ready for payment tracking. | page.tsx:309 | step: Draft |
| helper | Payment has been manually confirmed. | page.tsx:315 | step: Paid |
| helper | Cards have been reserved from the vault. | page.tsx:322 | step: Allocated |
| helper | A customer-ready export has been created. | page.tsx:329 | step: Export created |
| status/helper | Downloaded — An authorized operator downloaded sensitive card data. | page.tsx:335–338 | step |
| status/helper | Customer delivery — Delivery to the customer was explicitly confirmed. | page.tsx:341–344 | step |
| helper | Final fulfillment review is complete. | page.tsx:347 | step: Closed |
| heading | Vendor preparation required | page.tsx:573 | warning card — glossary #1 |
| helper | This request includes {vendors}. Cards are not allocated from preloaded inventory until activated card results have been imported into the vault. | page.tsx:578 | warning body |
| helper | For Walmart V1, the app should prepare the Walmart/Fiserv work file and import the activated result file. Progressive remains responsible for running activation outside the app unless that work is separately scoped. | page.tsx:583 | scope caveat — reads like SOW text in product UI; candidate for plainer operator phrasing |
| button | Go to card preparation | page.tsx:591 | link |
| label | Request value · Line items · Allocated cards · Created | page.tsx:602–609 | stats |
| column | Offering · Available · Quantity · Value | page.tsx:642–646 | line items — glossary #9 |
| heading | Payment status | page.tsx:701 | card |
| button | Update payment | page.tsx:730 | submit |
| heading | Card allocation | page.tsx:738 | card |
| label | Requested | page.tsx:743 | summary row |
| helper | Cards are allocated and ready for export. | page.tsx:753 | state |
| helper | This request needs vendor preparation unless activated cards have already been imported into the vault. | page.tsx:757 | state |
| helper | Inventory is short. Allocation will be available once enough cards are in the vault. | page.tsx:762 | state |
| helper | Mark payment as paid before allocating cards. | page.tsx:767 | state |
| helper | Inventory is available for every line item. | page.tsx:771 | state |
| button | Allocate cards | page.tsx:785 | action |
| label | · PIN {masked} | page.tsx:814 | allocated card row |
| placeholder | Reason card is invalid | page.tsx:855 | quarantine input |
| button | Quarantine and replace | page.tsx:863 | action — P3 note |
| heading | Export package | page.tsx:875 | card — glossary #7 |
| helper | Export package created. Downloading exposes sensitive card data internally; customer delivery is recorded separately. | page.tsx:880 | state |
| helper | Create a CSV export from the allocated cards for this request. | page.tsx:885 | state |
| helper | Allocate cards before creating an export package. | page.tsx:890 | state |
| button | Create export | page.tsx:905 | action |
| button | Vendor work file CSV | page.tsx:946 | flag-gated download |
| helper | {profile} · Downloaded {n} time(s); last downloaded {date}; delivered {date} | page.tsx:954 | export metadata |
| placeholder | Optional delivery notes | page.tsx:984 | input |
| button | Mark delivered to customer | page.tsx:990 | action |
| heading/button | Close request | page.tsx:999,1029 | card + action |
| helper | This request is closed and ready for historical reference. | page.tsx:1004 | state |
| helper | Payment, allocation, export, download, and customer delivery are complete. Close this request after final review. | page.tsx:1008 | state |
| helper | Requests can be closed after payment is paid, cards are allocated, an export has been downloaded, and customer delivery has been recorded. | page.tsx:1013 | prerequisites |
| heading | Danger zone | page.tsx:1040 | flagged P1 |
| helper | Cancel this request only if it was created in error and sensitive card data has not left the vault. The request stays visible for audit history. | page.tsx:1045 | guidance |
| helper | Cancellation is disabled after export download, customer delivery, or closeout. | page.tsx:1056 | disabled explanation |
| heading | Audit activity | page.tsx:1066 | card |
| empty-state | No request-specific audit activity yet. | page.tsx:1083 | feed |
| button | Cancel request | delete-request-dialog.tsx:44,88 | trigger + confirm |
| heading | Cancel {requestNumber}? | delete-request-dialog.tsx:49 | dialog title |
| helper | The request and audit history will be retained. Up to {n} allocated cards that have not left the vault will be returned to Available inventory. | delete-request-dialog.tsx:51 | dialog body |
| label | Cancellation reason · Type cancel to confirm | delete-request-dialog.tsx:59,72 | dialog fields |
| placeholder | Created in error | delete-request-dialog.tsx:66 | reason example |
| error | Add a cancellation reason. · Add a reason for quarantining the card. | actions.ts:30,36 | validation |

### 3.10 Request audit-feed messages (shown in Audit Log + dashboard)

| String | Source |
|--------|--------|
| {req} payment status changed to {status}. — **flagged P1 (raw enum)** | actions.ts:108 |
| {req} was not eligible for card allocation. | actions.ts:191 |
| {req} needs vendor preparation before cards can be allocated. | actions.ts:238 |
| {req} could not be allocated because inventory is short. | actions.ts:261 |
| {req} allocated {n} card(s) from the vault. | actions.ts:328 |
| {req} was not eligible for export. | actions.ts:380 |
| {req} export package created using {profile}. | actions.ts:423 |
| {req} was not eligible to close. | actions.ts:467 |
| {req} closed after export. | actions.ts:490 |
| {req} marked delivered to the customer by {name}. | actions.ts:598 |
| {req} quarantined {card} and allocated replacement {card}. Reason: {reason} | actions.ts:706 |
| {req} quarantined {card}; replacement inventory is required. Reason: {reason} | actions.ts:707 |
| {req} cancelled by {name}; {n} allocated cards returned to the vault. Reason: {reason} | actions.ts:815 |
| {req} export package downloaded by {name}. | exports/[exportId]/route.ts:155 |
| {req} Lloyd work file downloaded by {name}. — internal name in user-visible audit text; rename ("vendor work file") | work-file/route.ts:104 |
| Users: {actor} created {user} with {role} access. · changed {user} to {role} access. · reset the password for {user}. · reactivated/deactivated {user}. | users/actions.ts:62–165 |
| Inventory: {n} cards imported into the vault; {d} duplicates and {u} unmatched rows skipped. · {profile} import profile used for manual inventory import. | import/actions.ts:169–178 |
| WordPress: {actor} created/updated WordPress connection {label}. · rotated the secret for… · tested the stored secret for… | integrations/wordpress/actions.ts:68–176 |

### 3.11 New request (/requests/new)

| Kind | String | Source | Context |
|------|--------|--------|---------|
| heading | New Fulfillment Request | new/page.tsx:62 | page title |
| helper | Manually create a test request from the seeded gift card catalog. | new/page.tsx:61 | flagged P1 |
| heading | Customer details | new/page.tsx:68 | form card — glossary #2 |
| labels | Company / organization · Purchase order · First name · Last name · Customer email · Phone · Delivery type · Preferred delivery · Payment method · Submitted order total · Billing address (+ line 2, city, province, postal code, country) · Notes | new/page.tsx:72–233 | form fields |
| placeholders | Northstar Foods · PO-12345 · Elaine · Sample · ops@example.com · 555-555-5555 · Email, pickup, courier · Invoice, cheque, EFT · 500.00 · Street address · PO Box, unit, suite · Internal notes for this request | new/page.tsx:77–238 | examples — P3 note |
| label | Digital E-Cards / Physical Cards · Select delivery type | new/page.tsx:137–139 | delivery options |
| heading | Shipping details optional | new/page.tsx:248 | flagged P2 |
| labels | Company · First name · Last name · Email · Phone · Shipping address (+ line 2, city, province, postal code, country) | new/page.tsx:253–293 | shipping fields |
| heading | Gift card line items | new/page.tsx:302 | form card |
| button | Cancel · Create request | new/page.tsx:311–314 | actions |
| helper | {n} of {max} line items · {type} request | line-items-fieldset.tsx:106 | count |
| button | Add line item | line-items-fieldset.tsx:117 | action |
| label | Gift card offering | line-items-fieldset.tsx:127 | select — glossary #9 |
| placeholder | Select a card and denomination | line-items-fieldset.tsx:136 | empty option |
| label | Quantity | line-items-fieldset.tsx:151 | field |
| label | Remove line item {n} | line-items-fieldset.tsx:164 | icon aria-label |
| error | Company is required. | new/actions.ts:18 | validation |

### 3.12 Exports, Closed Requests, Audit Log, Clients

| Kind | String | Source | Context |
|------|--------|--------|---------|
| heading | Exports | exports/page.tsx:53 | title |
| helper | Review and download fulfillment export packages. | exports/page.tsx:52 | description — glossary #7 |
| heading | Export packages | exports/page.tsx:57 | table title |
| column | File · Request · Customer · Output profile · Exporter · Exported · Downloads · Last downloaded · Customer delivery | exports/page.tsx:62–70 | headers — "Exporter" flagged P2 |
| placeholder | Search exports | exports/page.tsx:73 | search |
| heading | Closed Requests | closed-requests/page.tsx:79 | title |
| helper | Completed and cancelled requests retained for operational history. | closed-requests/page.tsx:78 | description |
| heading | Closed and cancelled requests | closed-requests/page.tsx:83 | table title |
| column | Request · Customer · Payment · Status · Allocated · Value · Exported · Closed | closed-requests/page.tsx:94–101 | headers |
| placeholder | Search closed requests | closed-requests/page.tsx:104 | search |
| heading | Audit Log | audit-log/page.tsx:47 | title |
| helper | Search and filter the operational audit trail. | audit-log/page.tsx:46 | description |
| heading | Audit activity | audit-log/page.tsx:51 | table title |
| status | System | audit-log/page.tsx:28 | actor fallback |
| column | Time · Actor · Action · Entity · Message | audit-log/page.tsx:56–60 | headers — "Actor"/"Entity" are systems words; consider "Who"/"Record" |
| placeholder | Search audit log | audit-log/page.tsx:64 | search |
| heading | Clients | clients/page.tsx:91,95 | title + table |
| helper | Search clients and review their related fulfillment history. | clients/page.tsx:90 | description |
| column | Client · Email · Phone · Requests · Total value · Latest request · Updated | clients/page.tsx:100–106 | headers |
| placeholder | Search clients | clients/page.tsx:109 | search |
| status | Not provided (×9) · – (×8) | clients/page.tsx:59–60 etc. | fallbacks — glossary #10 |
| button | All requests | clients/[clientId]/page.tsx:161 | link |
| helper | Review this client's submitted fulfillment requests. | clients/[clientId]/page.tsx:165 | description |
| label | Last updated · Company / organization · Contact name · Email · Phone · Billing address · Shipping contact/email/phone/address | clients/[clientId]/page.tsx:135–194 | info fields |
| heading | Client information · Client requests | clients/[clientId]/page.tsx:204,221 | cards |
| column | Request · Type · Cards · Payment · Status · Exported · Value · Updated | clients/[clientId]/page.tsx:231–238 | headers |
| status | Yes / No · {vendor} {denom} x {qty} | clients/[clientId]/page.tsx:108,118 | cells |
| placeholder | Search this client's requests | clients/[clientId]/page.tsx:241 | search |

### 3.13 Users (/users) & Integrations (/integrations/wordpress)

| Kind | String | Source | Context |
|------|--------|--------|---------|
| heading | Users | users/page.tsx:104 | title |
| helper | Create accounts, assign roles, deactivate access, and reset passwords. | users/page.tsx:103 | description |
| toasts | User account created. · User role updated. · User password reset. · User deactivated. · User reactivated. | users/page.tsx:37–53 | banners |
| errors | You cannot deactivate your own account. · Use a password with at least 8 characters. · Check the new user details and try again. | users/page.tsx:61–69 | banners |
| heading | Create user · Existing users | users/page.tsx:120,177 | cards |
| labels | Name · Email · Username · Temporary password · Role · Reset password | users/page.tsx:125–291 | fields |
| placeholders | At least 8 characters · New temporary password | users/page.tsx:147,298 | inputs |
| buttons | Create account · Deactivate · Reactivate · Update role · Reset | users/page.tsx:168–306 | actions |
| status | Active / Inactive | users/page.tsx:204 | badges |
| helper | Added {date} · Updated {date} · {n} permissions · {m} sensitive | users/page.tsx:213,265 | metadata |
| heading | WordPress Integration | wordpress/page.tsx:118 | title |
| helper | Pair WordPress/Formidable sites with this vault environment. | wordpress/page.tsx:117 | description — "Formidable"/"environment" are admin-page technical terms; acceptable per style guide's admin-page carve-out |
| toasts | WordPress connection created. Paste its Connection Info into the WordPress handoff settings. · WordPress connection updated. · Connection secret regenerated. Update WordPress with the new Connection Info before sending more orders. · Stored connection secret decrypted successfully. | wordpress/page.tsx:45–57 | banners |
| error | Check the connection details and try again. | wordpress/page.tsx:65 | banner |
| heading/button | Create connection | wordpress/page.tsx:135,163 | card + submit |
| labels | Label · Allowed WordPress site URL · Allowed site URL · Connection Info | wordpress/page.tsx:141–258 | fields |
| placeholders | Pantheon Multidev to Staging (**flagged P1**) · https://example.pantheonsite.io | wordpress/page.tsx:143,154 | examples |
| helper | Optional. When set, orders from other WordPress origins are rejected. · Any WordPress site URL allowed · Paste this into the WordPress Vault Handoff settings for the matching site. | wordpress/page.tsx:157–268 | helpers |
| status | Enabled / Disabled · Created {date} · Last used {date} · Never · Last error: {message} | wordpress/page.tsx:201–282 | badges/metadata |
| buttons | Save connection · Test stored secret · Regenerate secret | wordpress/page.tsx:251–311 | actions |
| empty-state | No WordPress connections have been created yet. | wordpress/page.tsx:173 | list |
| errors (API) | WordPress connection was not found. · WordPress connection is disabled. · Invalid JSON request body. · Invalid connection test payload. · Connection ID mismatch. · WordPress site URL is not allowed for this connection. · Invalid WordPress order payload. · WordPress order could not be imported. | api/integrations/wordpress/… | surface in plugin + Last error |

### 3.14 Status labels (src/lib/format.ts — one map, shown everywhere)

| Domain | Labels |
|--------|--------|
| Payment | Draft · Invoiced · Payment pending · Paid |
| Fulfillment | Draft · Ready to allocate · Needs generation (**vs ruling #8: consider "Needs preparation"**) · Needs inventory · Allocated · Closed · Cancelled |
| Delivery | Not ready · Ready for export · Export created · Internally downloaded (P3 note) · Delivered to customer · Needs replacement · Needs redelivery · Cancelled |
| Card | Available · Allocated · Delivered · Quarantined |
| Request type | Digital · Physical · Mixed · Unknown |

### 3.15 Output CSV headers (src/lib/merchant-output-profiles.ts) — lock status per profile

Profile display names (shown in-app, renameable like any UI string): Generic internal CSV · Generic
URL vendor CSV · Walmart activation work file CSV · Loblaws/Shoppers customer CSV · Shoppers customer
CSV · Amazon workbook CSV — plus their descriptions (source lines 94–147).

| Profile | Column headers | Lock status |
|---------|----------------|-------------|
| Generic internal CSV (lines 17–32) | Request Number · Customer Name · Customer Email · Export File · Exported By · Exported At · Output Profile · Allocation ID · Vendor · Card Type · Denomination Cents · Denomination · Card Number · PIN · Card Status · Allocated At | **Renameable** — Redstamp-internal fallback file; "Denomination Cents" and "Vendor" follow glossary rulings like UI strings |
| Generic URL vendor CSV (lines 36–44) | Row ID · Brand · eGift Card Number · URL · Challenge Code · Denomination · Recipient Name · Message · Token | **In refinement** — customer-style file; confirm with Progressive which client formats it must match before renaming |
| Loblaws/Shoppers + Shoppers customer CSV (lines 48–52) | Gift Card Vendor · Gift Card Value · Gift Card URL · Account Number · Gift Card Pin (casing flag, §2 P2) | **LOCKED — client-consumed**; changes are a Progressive conversation |
| Amazon workbook CSV (lines 56–63) | SEQUENCE · CLAIM CODE · AMOUNT · SERIAL NUMBER · CUSTOMER · MESSAGE · Invoice # · Date | **LOCKED — client-consumed** (mirrors the workbook format in use) |
| Walmart activation work file (lines 67–74) | Operation · Card Number · PIN · Card Value · Card Type · Original Idempotency Key · Transaction Status · Target System | **LOCKED — process-bound**; feeds Progressive's external Fiserv activation |

### 3.16 Import profile names & notes (src/lib/merchant-import-profiles.ts)

Display names (P3 — keep; Lloyd quotes them verbatim): Auto-detect / Generic CSV · URL + Challenge
Code · URL Only · URL + Account Number + PIN · Card Number + PIN · Amazon Claim Code · Walmart
Activated Result. Each carries a description + two/three review notes (source lines 36–144) — these read
well and already model the preparation-not-activation rule.

### 3.17 Permission names (src/lib/permissions.ts — shown on /users)

View fulfillment work · Create requests · Update payment status · Allocate cards · Create exports ·
Download sensitive exports · Confirm customer delivery · Cancel requests · View inventory · Import
inventory · Manage users · Manage integrations · View audit log — each with a one-line description
(lines 28–114). All read cleanly; align "fulfillment work" wording with glossary ruling #3.

---

*Assembled 2026-07-14 from three parallel extraction passes over the prototype source, verified against
`docs/designer-user-flows.md` and the Content Style section of `docs/application-style-guide.md`.*
