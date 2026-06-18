---
title: "Phase 1 Vault — Card Normalization Model & Call-Prep Design Note"
type: plan
category: internal-design
date: 2026-06-18
status: draft
audience: internal (Spencer, Tim, Stephanie) — call prep, not client-sent
participants:
  redstamp:
    - Spencer Ririe
    - Tim Lemke
    - Stephanie Lamon
  progressive:
    - Doug Beers
    - Lloyd Scrubb
    - James (outside technical counsel)
tags:
  - progressive
  - phase-1
  - secure-card-vault
  - normalization
  - redemption-credential
  - merchant-formats
  - walmart
  - call-prep
  - sow
key_decisions:
  - "Vault owns a canonical card record; Progressive's spreadsheet input formats are incidental (how they store cards today), not a constraint to model faithfully."
  - "Redemption credential normalizes to one shape: optional redemption URL + a typed bag of secrets (claim code / card # / PIN / challenge / account # / security code). New merchant = a column mapping, not a code change."
  - "Inputs collapse to ~7 supplier/source-system families, not 23 merchant formats — matches Lloyd's 'inhomogeneous by supplier' point."
  - "Output is rule-driven from the canonical store; two modes (repackage existing credentials vs generate PDF). Walmart is the one externally-constrained OUTPUT (bidirectional activation contract)."
  - "SOW reframes from '4 hardcoded format families' to 'one configurable supplier-aware importer + generation for Amazon/Walmart/Chapters-Indigo,' bounded for the fixed fee by the Phase 1A active-merchant list."
key_insights:
  - "Our independent data analysis of redstamp.zip lands on the same model Lloyd and James are already advocating — strong alignment going into the call."
  - "The yesterday format_class taxonomy is filename-keyword-driven and internally inconsistent (Fairmont≡Winners split apart; Chapters≈Cara hidden in unknown-tabular). Use schema fingerprint + supplier provenance instead."
related:
  - projects/gift-cards/docs/plans/2026-06-17-lloyd-materials-analysis-and-phase1-technical-recommendations.md
  - projects/gift-cards/docs/discovery/2026-06-16-phase1-annotated-qa-thread.md
  - projects/gift-cards/docs/plans/2026-06-10-phase1-decision-sheet.md
  - projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md
  - projects/gift-cards/docs/plans/2026-05-27-progressive-secure-card-vault-sow-draft.md
blockers:
  - "Hosting specifics need Tim's input (proposed posture below is a placeholder for his confirmation)."
  - "D-13 rate ($150 relationship vs $160 last-executed) is Spencer's call."
  - "Walmart activation program still withheld; SystemOne/SystemBind naming unconfirmed."
---

# Phase 1 Vault — Card Normalization Model & Call-Prep Design Note

**What this is.** The technical model for how the vault handles every merchant's cards, written so it (a) resolves every open question from Doug's team, (b) is usable as prep for the Lloyd + Doug + Redstamp call, and (c) gives Tim a concrete model to adjust rather than a wall of text. The model is deliberately left open where Tim has already done importer work.

**One-line thesis.** Progressive's 23 different spreadsheets are just how they *store* cards today. The vault should normalize on ingest into one canonical card record, store it the vault's way, and render whatever output a given order needs by rule. The only place an outside party dictates our format is **Walmart**.

---

## 1. The reframe (why this is simpler than it looks)

The discovery instinct was "23 merchants, ~23 formats — how many do we hardcode?" The data and Progressive's own team both say that's the wrong axis:

- **Lloyd (operator):** the data is "inhomogeneous by *supplier*, not merchant" — suppliers like CashStar/Blackhawk deliver homogeneous groups, so covering a supplier covers its merchants. Only **Amazon, Walmart, Chapters-Indigo** are true card-*generation* cases; everything else is pass-through (import → drop valueless columns → protect → send). Adding such a merchant "should not require a software change."
- **James (their counsel):** is pushing Doug toward a **general** system rather than targeted merchants, on exactly the grounds that merchants share import structure.
- **Our data:** profiling the real inventory files in `redstamp.zip` independently collapses the 23 merchants into ~7 source-system families (§3). Two merchants with *byte-identical* schemas (Fairmont, Winners) only looked different because of filenames.

We arrived at the same model from three directions. That's the headline for the call: **we're not proposing something new — we're formalizing what your operator already does, and making it safe and repeatable.**

---

## 2. The canonical model

### 2.1 Canonical card record (what the vault stores)

One internal shape for every card, regardless of source:

| Field | Notes |
|---|---|
| `merchant` / `brand` | e.g. Tim Hortons |
| `supplier` / `source_system` | provenance — which platform delivered it (CashStar, PC allocation, fuel portal, Amazon, …) |
| `value` + `currency` | normalized from `Denomination` / `AMOUNT` / `Card Value` / `Value` / `Gift Card Value` / `Unit Price` |
| `credential` | the redemption payload — see 2.2 |
| `recipient_name`, `recipient_email` | optional; present in some families |
| `customer`, `order_ref`, `invoice_ref`, `date` | Progressive's fulfillment metadata (today appended as trailing columns) |
| `status` | available → allocated → fulfilled; plus quarantined / needs-replacement / voided |
| `source_provenance` | import batch, file, row — for audit and the stray-card question (§5.1) |

### 2.2 Redemption credential — the simplification

Every merchant's "secret" reduces to **one redemption URL (optional) + a typed bag of secrets**:

```
credential = {
  url?:      string                       # redemption / claim link
  secrets[]: { type, value }              # type ∈ {claim_code, card_number, pin,
                                          #         challenge, account_number, security_code}
  instructions?: string                   # per-merchant redemption steps
}
```

That single shape covers every observed family:

| Family | Maps to |
|---|---|
| Amazon | `secrets:[claim_code]` |
| CashStar `_Links` (most merchants) | `url + secrets:[challenge]` |
| Reference-Id (Fairmont, Winners) | `url` |
| PC allocation (Loblaws, Shoppers) | `url + secrets:[account_number, pin]` |
| Code+PIN (Cara, Chapters-Indigo) | `secrets:[card_number, pin]` |
| Fuel portal (Esso, Petro-Canada) | `url + secrets:[card_number, pin]` |
| Starbucks / CashStar download | `url + secrets:[card_number, security_code]` |

**Why it matters:** new merchant or supplier change = map its columns to `{url, secrets[]}`. No new code path. This is exactly Lloyd's "shouldn't require a software change," made concrete.

### 2.3 Input side — adapters, not per-merchant formats

An importer is **schema-fingerprint → supplier family → column mapping → canonical record**. Three rules the real data forces on us:

1. **Detect the data sheet and header band** — don't assume sheet name or position. (Sheet names seen: `Sub Order 4`, `in`, `Report Data`, `CashStar Download`, `Sheet1`, truncated filenames; Starbucks even ships an `Instructions` sheet.)
2. **Split native vs appended columns.** Every file is `[merchant-native] + [Customer, Invoice/Invoice #, Date] + [trailing junk]`. The vault owns the fulfillment metadata; the adapter only maps the native columns. (Even Progressive's own appended names drift — `Invoice` vs `Invoice #`.)
3. **Map by synonym, ignore junk.** Value/URL/secret fields go by many names, with whitespace traps (`Card  Number`, `Denomination `); trailing junk columns appear in every file and one (Esso) even contains a stray sensitive value — so junk must be dropped by *position after the mapped band*, not by "it's numeric."

### 2.4 Output side — by rule, not by merchant

Output is derived from the canonical record at fulfillment time, in one of two modes:

- **Mode A — repackage** existing credentials into a customer-ready file (password-protected Excel / URL export). The pass-through majority.
- **Mode B — generate** a PDF card from the credential, packaged in a ZIP. Today: **Amazon** (claim code → rendered PDF); per Doug, also **Walmart** and **Chapters-Indigo**.

Lloyd's key point: the *same* brand can go out as URL-Excel **or** PDF-ZIP — it's an order/brand setting, not fixed by merchant. So in the vault, **output format is a rule on the canonical record, which is why storing it our way simplifies things** (Spencer's point): you set the condition, the output follows.

### 2.5 The one exception — Walmart (bidirectional)

Walmart is the only case where an outside party dictates *our* output. Walmart is just-in-time activation with no static inventory: the vault must **produce a Walmart/Fiserv-expected work file**, hand it off for activation, and **import the activated results back**. That return contract is the fixed format. Everything else, Progressive/the vault controls.

---

## 3. The ~7 source families (input adapters)

Profiled from the real inventory files in `redstamp.zip` (headers only). This *replaces* the yesterday `format_class` taxonomy, which classified by filename keyword and was internally inconsistent.

| # | Family / supplier | Merchants | Credential | Output |
|---|---|---|---|---|
| 1 | **CashStar `_Links`** | Best Buy, Boston Pizza, Cactus Club, DoorDash, Earls, H&M, Keg, Sephora, Subway, Tim Hortons | URL + challenge | Mode A |
| 2 | **Reference-Id** | Fairmont, Winners | URL | Mode A |
| 3 | **PC allocation** | Loblaws, Shoppers | URL + account # + PIN | Mode A (or B, legacy) |
| 4 | **Code + PIN** | Cara, Chapters-Indigo | card # + PIN | A; **B for Chapters** |
| 5 | **Fuel portal** | Esso, Petro-Canada | card # + PIN + URL | Mode A (Petro now via Fundstream — see §5) |
| 6 | **Starbucks / CashStar download** | Starbucks (2 historical variants) | card # + security code + URL | Mode A |
| 7 | **Amazon allocation** | Amazon | claim code | **Mode B (generate)** |
| — | **Walmart** | Walmart | JIT activation | bidirectional (§2.5) |

**Coverage note:** families 1–2 alone are ~12 of the active merchants through two adapters. Master Card, Hudson's Bay, Browns, Uber are out (Doug: MasterCard yes but no fixtures yet; the rest no/not-now).

---

## 4. What this changes in the SOW (findings vs. SOW)

The May 27 draft + June 10 reconciliation framed Phase 1 as **"up to four merchant output format families"** (D-1/D-2). The model says that's accurate on *output* but mis-frames the *engineering*: it's really **one configurable, supplier-aware importer + generation for three merchants + the Walmart contract.**

| Aspect | Current SOW framing | Model | Net |
|---|---|---|---|
| Importer | 4 format families | 1 configurable importer over ~7 supplier adapters | Simpler to build & extend; matches Lloyd/James |
| Generation | Amazon (+ maybe Loblaws/Shoppers) | Amazon, Walmart, Chapters-Indigo (Doug-confirmed) | Corrects the merchant list |
| Output choice | per-merchant | per-order rule (URL **or** PDF) | Flexibility Lloyd asked for |
| Commercial bound | fixed fee, 4 families | **bound by the Phase 1A active-merchant list + named supplier families; a genuinely new supplier family = change order** | Keeps the fee bounded *without* hardcoding — the reconciliation we need |

**Important:** the general architecture does **not** mean unbounded scope. The fixed fee stays bounded by "active digital merchants as of Phase 1A + the supplier families they use." Adding a merchant inside a known family = configuration (no charge); a brand-new supplier shape = CO. That gives Lloyd his "no software change to add a merchant" *and* protects the fee. This is the one nuance to land cleanly with Tim and in Stephanie's SOW language.

Everything else in the reconciliation holds: Phase 1A validation milestone (D-4), vault-generated password protection (D-5/D-15), no in-browser reveal (D-6), no Redstamp card access by default (D-7), invalid-card workflow (D-8/D-9), support retainer proposed separately (D-11), training boundary (D-12).

---

## 5. Resolving their open questions (call-ready)

### 5.1 Doug — a stray old "Progressive"-branded Loblaws card slips through
Because the vault is the system of record and validates on import, an item that doesn't fingerprint to a current supplier family is **quarantined for operator review, not silently fulfilled**. Doug already expects stragglers to be converted before vault entry, so this is an edge guard, not a workflow. **Answer:** "It can't reach a customer unnoticed — unrecognized formats/brands land in a review queue with their source row recorded."

### 5.2 Lloyd / James — where is it hosted (security + backup/data-loss)?
**Proposed posture (needs Tim's confirmation):** Redstamp-managed cloud, **Canadian data residency** (cash-equivalent data, Canadian entity), encrypted at rest and in transit, automated daily backups with tested restore, full access logging, no card data in application logs. **Flag:** Tim to confirm the actual stack/provider — this is a placeholder, and hosting/ownership may also feed the support agreement.

### 5.3 Lloyd — "What is a 'banner brand'?"
A **banner** is a retail store brand operated under a parent company; sibling banners usually share one gift-card platform/format. Example: Loblaw Companies banners — Loblaws, Shoppers Drug Mart, No Frills, Zehrs, Real Canadian Superstore. So "banner brands that share one format" = sibling stores under one parent whose cards arrive through the same supplier, so **one adapter covers them all.** (Ties directly to the open confirmation: which Loblaws banners share the format.)

### 5.4 Lloyd — "Is this SystemBind?" (vs our "SystemOne")
Terminology, not architecture. We've called the URL upload/delivery system **SystemOne** (`ecard.proegiftcards.ca`); Lloyd calls it **SystemBind**. Almost certainly the same system. **Action:** confirm the canonical name on the call. In the model it's an external *delivery target* for Mode A exports, not part of the vault.

### 5.5 Open confirmations
- **Manual Walmart activated-results import for v1** — recommend we accept (D-2/T-2): controlled import in, direct Fiserv activation out until we've reviewed the (still-withheld) activation assets.
- **Which Loblaws banners share one format** — confirm with Lloyd once "banner" is defined (5.3).

### 5.6 Internal decisions still open
- **D-3 Amazon output:** with svg2pdf validated and output now a per-order rule, Amazon defaults to **PDF/ZIP** (best-evidenced); URL export available once SystemOne/SystemBind is confirmed. No longer a hard either/or.
- **D-13 rate:** $150 (CLIENT.md / relationship) vs $160 (last executed Progressive SOW). **Spencer's call** — fixed fee unchanged either way.
- **D-14 payment:** keep 40/40/20.
- **D-15 export password:** random per-export password, shown once to the operator, delivered via the existing separate-email channel; lost password = re-export; no un-password workflow.

---

## 6. Technical underlay (settled — for the appendix/credibility)

- **Renderer:** `svg2pdf` (resvg family) reproduces Lloyd's Inkscape output to within rasterization noise (MAE 0.15/255); chosen over Playwright (fallback) and CairoSVG (rejected — breaks the logo). No Inkscape in the vault.
- **Generation runtime:** ~120 ms/card. Generation is a background job, so this is ample — a typical ~20-card Amazon order ≈ 2.4 s; 500 cards ≈ 60 s. Parallelism is available but caps early (~4 concurrent renders, ~12 cards/s) and is not needed at Progressive's volume.
- **Ops caveats (renderer-independent):** ship Arial/Verdana fonts in the render image; set the output page size. Replace the script's fragile string-replace placeholders with named template fields.
- Detail: [2026-06-17 analysis §4](2026-06-17-lloyd-materials-analysis-and-phase1-technical-recommendations.md) and private `E2E-RUN-FINDINGS.md` §7/§7a.

---

## 7. Open for Tim

Tim has already prototyped importer work — these are the seams where his version should drive:

1. The canonical record + credential shape (2.1/2.2) — does his prototype already encode something close? Adopt his if so.
2. Supplier-family adapter boundary (§3) — confirm the families match what he built.
3. Hosting posture (5.2) — his call on stack.
4. The bounded-but-configurable SOW framing (§4) — does it match how he scoped the build?

---

## 8. Proposed call flow (Lloyd + Doug + Redstamp)

1. **Frame:** "We analyzed Lloyd's package; our model matches what Lloyd and James are already describing." (alignment, not new news)
2. **Confirm the model:** supplier families, generation = Amazon/Walmart/Chapters-Indigo, output-by-rule.
3. **Close the 4 questions** (§5.1–5.4) — most are quick.
4. **Confirm:** Walmart manual import for v1; banner-format grouping.
5. **Walmart assets + SystemOne/SystemBind:** what's still needed, what it's called.
6. **Hand to Stephanie:** SOW clarifying language (§4) + support proposal.
7. **Internal-only, not for the call:** D-13 rate, D-14 schedule.

---

*Next: on sign-off of this model, build the interactive HTML decision artifact on top of it (questions resolved, findings vs SOW, the model, renderer + parallelism), leaving the model panel open for Tim's adjustments.*
