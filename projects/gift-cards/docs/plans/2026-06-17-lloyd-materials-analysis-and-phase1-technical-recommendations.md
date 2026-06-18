---
title: "Lloyd Materials Analysis — E2E Findings, Inventory Map, PDF Rendering Recommendations"
type: plan
category: technical-assessment
date: 2026-06-17
status: complete
tags:
  - progressive
  - lloyd
  - phase-1
  - secure-card-vault
  - redstamp-zip
  - inventory-formats
  - amazon
  - inkscape
  - pdf-generation
  - e2e-validation
key_insights:
  - redstamp.zip received 2026-06-17; closes most April fixture gaps (scripts, templates, inventory samples, Amazon pipeline demo). Walmart activation program still withheld; written cleanup/retention rules still missing.
  - Invoice-to-Excel script is brittle — sample runs parsed Amazon E-Card lines only; Shopping Card lines on the same invoice were ignored. Do not wrap; use as behavioral reference.
  - Amazon PDF flow validated through log-CSV init; Inkscape dependency should be replaced with server-side rendering (resvg spike first, Playwright fallback).
  - Inventory formats collapse into ~8 importer modules; most merchants share a URL-link pattern; Amazon/Walmart/Loblaws-Shoppers are the outliers.
key_decisions:
  - Treat Lloyd scripts as reference material, not production code to wrap.
  - Phase 1 PDF generation — hybrid approach — keep SVG templates short-term; render server-side with resvg (primary spike) or headless Chromium/Playwright (fidelity fallback); migrate to HTML or native PDF templates later.
  - Defer full PDF invoice auto-parse, Master Card, Hudson's Bay, and Uber until fixtures exist or scope is explicitly added.
related:
  - projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md
  - projects/gift-cards/docs/plans/2026-06-08-sow-merchant-evidence-inventory.md
  - projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md
  - projects/gift-cards/docs/discovery/2026-06-16-phase1-annotated-qa-thread.md
  - projects/gift-cards/docs/discovery/2026-06-08-private-lloyd-materials-inventory.md
blockers:
  - Walmart activation program deliberately withheld by Lloyd
  - File cleanup and retention rules not documented in shared materials
  - "Inkscape not suitable for vault deployment — renderer resolved 2026-06-18: svg2pdf (resvg family) matches Inkscape; see §4"
---

# Lloyd Materials Analysis — E2E Findings, Inventory Map, PDF Rendering Recommendations

**Cold-start summary for Spencer / Tim.** Written 2026-06-17 after `redstamp.zip` landed in the private folder and was extracted, inventoried, and exercised headlessly.

## Where the files live

| What | Path | In git? |
|------|------|---------|
| Zip + extracted tree | `projects/gift-cards/_private/lloyd-materials-06162026/` | No (git-ignored) |
| Source inventory | `.../notes/SOURCE-INVENTORY.md` | No |
| E2E run detail + logs | `.../notes/E2E-RUN-FINDINGS.md`, `.../runs/` | No |
| Headless runner + inventory profiler | `.../scripts/headless_runner.py`, `inventory_format_map.py` | No |
| Walmart reconciliation (Doug email) | `.../WM Ecards - May2026.xlsx` | No |
| **This summary** | `projects/gift-cards/docs/plans/2026-06-17-lloyd-materials-analysis-and-phase1-technical-recommendations.md` | **Yes** |

**Sensitive:** Treat the entire `_private/lloyd-materials-06162026/` tree as cash-equivalent-adjacent. Do not commit extracted contents.

---

## 1. What Progressive shared (`redstamp.zip`)

~3.8 MB curated demo package (packaged 2026-06-15). Top-level layout:

- `prototype/` — Python scripts + `make-zip.ps1`
- `templates/amazon-e-giftcard-template.svg`
- `orders/<merchant>-ecards/` — per-merchant `template/`, `inventory/`, sample order outputs
- `Downloads/` — sample invoice PDFs

### Scripts

| File | Role |
|------|------|
| `e-giftcard-excelfile-generator-new-invoice-format.py` | Invoice PDF → merchant Excel workbook (27 merchants in code) |
| `amazon-e-giftcard-generator-new-generated-cards-folder-location.py` | Amazon xlsx → SVG/PDF + log CSV + ZIP |
| `utilities.py` | ZIP packaging helper |
| `make-zip.ps1` | 7-Zip password = first two numeric groups from filename (`10590-1655` → `105901655`) |

### Against the June 11 materials request

| # | Item | Status |
|---|------|--------|
| 1 | Script helpers + Amazon SVG | **Received** |
| 2 | Merchant workbook templates | **Mostly** — 23 merchants; Master Card empty; Hudson's Bay + Uber missing |
| 3 | Invoice + Amazon input/output example | **Received** |
| 4 | URL-inventory samples | **Received** (one per active merchant) |
| 5 | Walmart materials | **Partial** — reconciliation xlsx from Doug (separate file); activation tool **withheld** |
| 6 | SystemOne / URL upload examples | **Partial** — Amazon ZIP + `giftcardlogfile.csv` show delivery shape; no SystemOne docs |
| 7 | Password / cleanup / retention | **Partial** — password rule in `make-zip.ps1` only |

---

## 2. E2E script runs (2026-06-17)

Ran headlessly via `scripts/headless_runner.py` (Tkinter mocked, **pypdf** instead of Tika/Java, Inkscape not installed on analysis machine).

### Invoice → Excel

| Invoice | Result |
|---------|--------|
| `Invoice_105901655` (large multi-merchant) | **Partial** — only Amazon $100 × 20 parsed; 20+ other lines skipped |
| `Invoice_20270-40` | **Partial** — 3 Amazon lines ($50, $100, $250) → workbook created |

**Worked:** invoice #, date, customer; Amazon template copy; populated xlsx with correct column contract.

**Failed / limited:**

- Parser only matches **E-Card** line shapes (`EAMZN100 Amazon $100 E-Cards E 20 …`). **Shopping Card** lines (Walmart, Starbucks, Keg, etc.) on the same invoice are ignored.
- Hardcoded PDF line indices (`i = 50`) assume Apache Tika output; brittle across extractors.
- **Phase 1 implication:** Do not wrap this script. Use manual/structured order entry in vault. If PDF import exists at all, treat as best-effort assist for E-Card lines only.

### Amazon PDF generator

| Step | Status |
|------|--------|
| Read xlsx, validate rows, create folders, open log CSV | ✓ |
| SVG copy + field replace | ✗ macOS path bug with absolute paths |
| Inkscape → PDF | ✗ Inkscape not installed |
| ZIP packaging | Not reached |

**Known-good reference** (from zip, not re-generated): `orders/amazon-ecards/test/20260615122646/` — PDF + `giftcardlogfile.csv` + output ZIP (SystemOne delivery package shape).

**Amazon data contract (workbook):** `SEQUENCE`, `CLAIM CODE`, `AMOUNT`, `SERIAL NUMBER`, `CUSTOMER`, `MESSAGE`, `Invoice #`, `Date`.

**Template injection today:** string replace on placeholders in SVG (`Claim Code: …`, message text, `CDN$200.00`) — fragile; should become named template fields in vault.

---

## 3. Inventory format map (Phase 1 scoping)

Header-only analysis of `orders/*/inventory/*.xlsx` (no card values). Machine-readable: `_private/.../runs/inventory-formats.json`.

| Format class | Merchants | Vault notes |
|--------------|-----------|-------------|
| **Amazon allocation** | Amazon | Pre-allocated codes → Progressive-generated PDFs |
| **URL-link** (most common) | Best Buy, Boston Pizza, Cactus Club, DoorDash, Earls, H&M, Home Depot, Keg, Sephora, Subway, Tim Hortons | Row ID, Brand, URL, Challenge Code, Denomination — **single generic importer candidate** |
| **Loblaws / Shoppers** | Loblaws, Shoppers Drug Mart | Value, URL, Account #, PIN; plain + encrypted export variants |
| **Bulk ecert** | Cara | Card #, PIN, pickup URL |
| **Merchant order export** | Esso, Petro-Canada | Portal export column layouts |
| **Starbucks** | Starbucks | Distinct column set (Name, eMail, URL, Challenge, …) |
| **Reference-id URL** | Fairmont Hotels, Winners | Reference Id, Merchant Id, Denomination, URL |
| **Home Depot variant** | Home Depot | Claim Link + Challenge Token naming |
| **Walmart workbook** | Walmart | Multi-sheet `$25` / `$50` / `$100` / `Variable`; JIT activation — no inventory sample in zip |

### Fixture gaps

| Merchant | Issue |
|----------|-------|
| Brown's Social House | Template only |
| Master Card | Empty folder |
| Hudson's Bay, Uber | In invoice script only |
| Walmart | Order workbooks only; activation tool withheld |

### Suggested Phase 1 merchant modules

1. Amazon PDF pipeline  
2. Shared URL-link importer (~12 merchants)  
3. Loblaws / Shoppers family  
4. Cara ecert  
5. Esso / Petro-Canada exports  
6. Starbucks  
7. Walmart (partial until activation tool shared)  
8. Fairmont / Winners / Brown's  

**Defer:** full PDF invoice auto-parse, Master Card, Hudson's Bay/Uber without fixtures.

---

## 4. PDF rendering — Inkscape context and recommendations

### What Inkscape is

**Open source** (GPL), free vector editor focused on SVG. Lloyd uses it only as a **CLI converter** (SVG → PDF), not as an operator-facing design tool. Progressive pays no license fee — the problem is **operational shape**, not cost.

### Why not Inkscape in the vault

- Desktop app dependency on fulfillment machines or servers
- OS-specific CLI paths and behavior (Mac vs Windows path bugs already observed)
- Hard to run reliably in containers/workers
- Same fragility class as today's Lloyd workflow, just relocated

### Recommended approach: hybrid for Phase 1

| Layer | Phase 1 | Later |
|-------|---------|-------|
| Template format | Keep Lloyd's SVG (low migration risk) | HTML or native PDF layout |
| Variable injection | Placeholder replace initially | Named fields / template schema |
| Rendering | **Server-side library** | Same, cleaner inputs |
| Validation | Golden-file compare vs Lloyd reference PDFs | CI regression per template version |

### Renderer options (priority order)

1. **resvg / svg2pdf** (resvg-family, Rust) — **chosen, see spike below.** Small, fast, container-friendly; single static binary.
2. **Headless Chromium / Playwright** (fidelity fallback) — load SVG, print to PDF; keep in reserve for any future template usvg can't handle.
3. **CairoSVG** — rejected by the spike; visibly degrades the Amazon logo on Inkscape-heavy SVG.
4. **Native PDF** (ReportLab, pdf-lib) — best long-term maintainability; highest upfront cost (redesign card layout).

**Avoid:** Inkscape in server containers; proprietary PDF SDKs without clear benefit; SVG→PNG→PDF shortcuts.

### Spike result — RESOLVED 2026-06-18 (svg2pdf wins)

Ran the spike against Lloyd's reference Amazon PDF (`test/20260615122646/.../25/00cce0...pdf`). Reproduced the exact card from the template + the generator's 3 string replacements, rendered with each backend, and scored every render against the reference (mean per-channel error + % differing pixels; diff heatmaps + side-by-side saved in `_private/.../runs/spike/`).

| Backend | MAE /255 | % diff px | Verdict |
|---------|---------:|----------:|---------|
| **svg2pdf** (resvg family) | **0.15** | **0.22%** | **Winner — indistinguishable from Inkscape** (heatmap essentially black). |
| Playwright (Chromium) | 1.23 | 1.64% | Faithful; heavier runtime. Fallback only. |
| CairoSVG | 4.41 | 5.16% | Rejected — breaks the Amazon logo. |

**Decision: lock svg2pdf (`cargo install svg2pdf-cli`, v0.13 tested) as the Phase 1 Amazon renderer.** Playwright fallback is no longer needed for V1.

**Performance (benchmarked 2026-06-18, M2 Max):** ~**120 ms per card** warm. Generation runs as a background job, so this is ample — a typical ~20-card Amazon order is ~2.4 s; a 500-card order ~60 s sequential. Parallelism is possible but caps early (peak ~1.9×/~12 cards/s at 4 concurrent renders; *degrades below sequential past ~8* because each render already uses ~2 cores internally). Guidance: sequential is fine at Progressive's volume; if pooling, bound workers to performance-core count and run a long-lived worker that loads fonts once. Detail: `E2E-RUN-FINDINGS.md` §7a.

**Two deployment caveats (renderer-independent):**
1. **Fonts** — template uses Arial + Verdana as *system* fonts (no `@font-face`). Ship those fonts (or metric-compatible Liberation Sans / Arimo + a Verdana equivalent) in the Linux renderer image, or text will substitute. Applies to Chromium too.
2. **Page size** — svg2pdf maps px→pt 1:1 (1200×1111 pt) vs reference 900×833.25 pt; aspect/fidelity identical, just set the intended output size/DPI in production.

Full detail + artifacts: `_private/lloyd-materials-06162026/notes/E2E-RUN-FINDINGS.md` §7, harness `scripts/render_spike.py`.

### Build pattern

- Background worker: template version → inject fields → render PDF → package ZIP
- Template versions stored in vault (not filesystem paths)
- Golden-file tests in CI
- No Inkscape on staff machines or servers

### Scope discipline

PDF generation is primarily an **Amazon-class** problem (possibly Loblaws/Shoppers later). Most merchants are URL-link pull — **no PDF engine needed**. Build one merchant renderer module with a pluggable backend, not a generic SVG platform.

---

## 5. Open follow-ups (unchanged from client thread)

- Walmart activation program — Lloyd withheld; confirm Phase 1 boundary on Doug/Lloyd call.
- Written file cleanup and retention rules — not in zip.
- SystemOne vs SystemBind — Lloyd's terminology; no explicit upload docs in package.
- D-3 tension — Lloyd/James toward configurable generic importer vs earlier "Amazon PDF/ZIP only" framing; reconcile on call + SOW language.
- Loop **Tim** when he returns — this analysis supersedes the "run E2E when zip arrives" action from April review.

---

## 6. Session state when parked (updated 2026-06-18)

**Done:** zip received, extracted, inventoried, E2E exercised, inventory mapped, PDF direction chosen (hybrid). **Renderer spike complete (2026-06-18) — svg2pdf/resvg locked; see §4.**

**Not done:** Tim review, client call, SOW revision with Stephanie, answers to four open client questions, Walmart activation follow-up.

**Next when resuming:**

1. ~~Run resvg/Playwright spike~~ — done; svg2pdf chosen.
2. Fold merchant modules + defer list + the svg2pdf renderer decision into Phase 1 SOW scope with Tim.
3. Doug/Lloyd call — generic importer, SystemBind, hosting, old inventory edge case.
4. SOW clarifying language + D-13/D-14 resolution.
