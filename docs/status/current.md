# Status — rs-progressive-fundraising

> Session-start: read this file first. Session-end: update it following this section structure
> (full procedure: the Aurora `wrapup` skill, where installed).

## Current focus

Phase 1 (Secure Card Vault) — **technical validation of Lloyd materials is done; parked pending Tim
return + Doug/Lloyd call + SOW revision.** Spencer analyzed `redstamp.zip` (received 2026-06-17),
ran scripts headlessly, mapped inventory formats, and locked PDF rendering direction (server-side hybrid;
no Inkscape in vault). **Canonical cold-start doc:**
`projects/gift-cards/docs/plans/2026-06-17-lloyd-materials-analysis-and-phase1-technical-recommendations.md`

## Last session

- **2026-06-17** — `redstamp.zip` received (Spencer moved to private folder). Extracted to
  `_private/lloyd-materials-06162026/extracted/redstamp/`. Updated `SOURCE-INVENTORY.md`. Built
  headless runner + inventory profiler; ran invoice→Excel and Amazon generator E2E (partial success).
  Mapped ~8 inventory importer classes across 25 merchants. Documented Inkscape context + **hybrid PDF
  recommendation** (resvg spike first, Playwright fallback). Wrote committed summary plan (link above).
- **2026-06-16** — Processed Doug's reply; annotated Q&A thread; Walmart reconciliation xlsx inventoried;
  Spencer requested `redstamp.zip` Drive access.

## In-flight work

- **Canonical thread:** Gmail "RE: Reschedule Needed-Phase 1 Proposal" (thread `19e9a0905b082b87`).
- **Decisions Doug locked 2026-06-16:** Roles, active offerings (MasterCard yes; Browns/Hudson's Bay no;
  Uber not now), in-house generation merchants (Amazon, Walmart, Chapters-Indigo). Manual Walmart import
  v1 = "still to be discussed."
- **⚠️ Scope item to reconcile:** Lloyd/James generic importer vs earlier D-3 "Amazon PDF/ZIP only" —
  settle on call + SOW language.
- **Open client questions** (call / SOW): stray old Progressive-branded cards; vault hosting; "banner brand";
  SystemOne vs SystemBind.
- **Technical validation (NEW — done):** See `2026-06-17-lloyd-materials-analysis-and-phase1-technical-recommendations.md`.
  Key takeaways: don't wrap invoice script; Amazon PDF needs server renderer not Inkscape; ~8 merchant
  importer modules for Phase 1 scoping.
- **Still open:** D-13 (rate $160 vs $150), D-14 (payment schedule). Loop **Tim** on analysis when back.
- **National Zakat Foundation call:** still needs scheduling.

## Repo state

- **New committed doc (when committed):** `projects/gift-cards/docs/plans/2026-06-17-lloyd-materials-analysis-and-phase1-technical-recommendations.md`
- `docs/status/current.md` updated this session.
- Main may have untracked presentation artifacts — commit at Spencer's discretion.

## Runtime & environment

- **Materials local-only (git-ignored):** `projects/gift-cards/_private/lloyd-materials-06162026/`
  - `redstamp.zip` + `extracted/redstamp/` (full Lloyd demo package)
  - `WM Ecards - May2026.xlsx` (Walmart reconciliation)
  - `notes/SOURCE-INVENTORY.md`, `notes/E2E-RUN-FINDINGS.md`
  - `scripts/headless_runner.py`, `scripts/inventory_format_map.py`
  - `runs/` (logs, `inventory-formats.json`)
  - `.venv/` (pandas, openpyxl, pypdf, pdfplumber)
- Older recovered scripts: `projects/gift-cards/_private/lloyd-materials/2026-06-08/`
- **Not on analysis machine:** Java/Tika, Inkscape — E2E used pypdf + headless runner patches.

## Next steps

1. **When resuming:** Read `2026-06-17-lloyd-materials-analysis-and-phase1-technical-recommendations.md` first.
2. **Optional spike:** resvg vs Playwright against Amazon reference PDFs in private `test/20260615122646/`.
3. **Tim review** — merchant modules, defer list, PDF direction.
4. **Doug/Lloyd call** — generic importer, SystemBind, hosting, Walmart activation, old inventory.
5. **SOW revision with Stephanie** — clarifying language + D-13/D-14 + support proposal.
6. **Follow up with Lloyd:** Walmart activation program, cleanup/retention rules, Master Card fixtures.

## Blockers

- Walmart activation program deliberately withheld — confirm Phase 1 boundary.
- Renderer choice pending optional spike (recommendation logged; not a hard blocker for SOW drafting).
- D-13/D-14 are internal decisions, not external blockers.

## Decisions & context

- **2026-06-17 technical decisions:** Lloyd scripts = reference only; Phase 1 PDF = server-side hybrid
  (resvg → Playwright fallback); defer full invoice PDF parse.
- **2026-06-16 client thread:** `projects/gift-cards/docs/discovery/2026-06-16-phase1-annotated-qa-thread.md`
- **SOW reconciliation:** `projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md`
- **April script review (superseded by 2026-06-17 analysis for fixture/E2E status):**
  `projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md`
- House rule: read CLIENT.md + REDSTAMP-SOW-CONTEXT.md before client-facing artifacts.
