# Status — rs-progressive-fundraising

> Session-start: read this file first. Session-end: update it following this section structure
> (full procedure: the Aurora `wrapup` skill, where installed).

## Current focus

Phase 1 (Secure Card Vault) — **technical validation + the normalization model are done; parked pending Tim
review + Doug/Lloyd call + SOW revision.** Two things landed 2026-06-18: (1) the **renderer spike** —
svg2pdf (resvg family) matches Inkscape to rasterization noise, chosen for Amazon cards, no Inkscape in vault;
(2) the **vault normalization model** — inputs are incidental, the vault owns a canonical card record with a
simplified credential (`url + typed secrets`), 23 merchants collapse to ~7 supplier families, output is
rule-driven, Walmart is the one bidirectional exception. Our analysis independently converged with Lloyd's
"inhomogeneous by supplier" and James's "general system" framing — the alignment headline for the call.
**Canonical cold-start docs:** the normalization model + call prep
`projects/gift-cards/docs/plans/2026-06-18-phase1-vault-normalization-design-note.md` (read first), and the
technical/renderer detail `projects/gift-cards/docs/plans/2026-06-17-lloyd-materials-analysis-and-phase1-technical-recommendations.md`.

## Last session

- **2026-06-18** — (1) Renderer spike vs Lloyd's reference Amazon PDF: svg2pdf MAE 0.15/255 (winner),
  Playwright 1.23 (fallback), CairoSVG 4.41 (rejected — breaks logo); ~120 ms/card, parallelism caps ~4
  workers but generation is a background job so non-issue. (2) Adversarially reviewed yesterday's inventory
  format map against raw files — found the `format_class` taxonomy is filename-driven and inconsistent
  (Fairmont≡Winners split apart; Chapters≈Cara hidden). (3) Wrote the **vault normalization design note**
  (canonical record + credential + ~7 supplier families + findings-vs-SOW + resolves all 4 open client
  questions) and a **self-contained interactive HTML decision artifact** built from it (render-verified).
  Updated analysis doc §4/§6 + `E2E-RUN-FINDINGS.md` §7/§7a. Artifacts in `_private/.../runs/spike/`.
- **2026-06-17** — `redstamp.zip` received (Spencer moved to private folder). Extracted to
  `_private/lloyd-materials-06162026/extracted/redstamp/`. Updated `SOURCE-INVENTORY.md`. Built
  headless runner + inventory profiler; ran invoice→Excel and Amazon generator E2E (partial success).
  Mapped ~8 inventory importer classes across 25 merchants. Documented Inkscape context + **hybrid PDF
  recommendation** (resvg spike first, Playwright fallback). Wrote committed summary plan (link above).
  Committed Phase 1 client presentation HTML + walkthrough PDF to `docs/plans/`.
- **2026-06-16** — Processed Doug's reply; annotated Q&A thread; Walmart reconciliation xlsx inventoried;
  Spencer requested `redstamp.zip` Drive access.

## In-flight work

- **Canonical thread:** Gmail "RE: Reschedule Needed-Phase 1 Proposal" (thread `19e9a0905b082b87`).
- **Decisions Doug locked 2026-06-16:** Roles, active offerings (MasterCard yes; Browns/Hudson's Bay no;
  Uber not now), in-house generation merchants (Amazon, Walmart, Chapters-Indigo). Manual Walmart import
  v1 = "still to be discussed."
- **Scope item — now framed (was ⚠️):** Lloyd/James generic importer vs earlier "Amazon PDF/ZIP only" is
  resolved by the model as **bounded-but-configurable** (one configurable importer + generation for
  Amazon/Walmart/Chapters-Indigo; fee bounded by the Phase 1A active-merchant list; new supplier family =
  CO). Needs Spencer + Tim gut-check before it reaches Stephanie's SOW language.
- **Open client questions** (call / SOW): all four have call-ready answers in the design note §5 — stray
  old Progressive-branded card (quarantine on import), vault hosting (proposed posture, needs Tim's stack),
  "banner brand" (defined), SystemOne vs SystemBind (terminology confirm with Lloyd).
- **Waiting on Tim:** his renderer/stack pick (he reportedly already chose one — reconcile our svg2pdf
  benchmark to it) and whether his importer prototype already encodes the canonical record/credential.
- **Decision artifact to carry over:** the HTML artifact is built to be moved to Spencer's Redstamp account
  (self-contained single file). Finalize after Tim's model input.
- **Still open:** D-13 (rate $150 vs $160), D-14 (payment schedule — default keep 40/40/20).
- **National Zakat Foundation call:** still needs scheduling.

## Repo state

- **Phase 1 analysis (cold-start):** `projects/gift-cards/docs/plans/2026-06-17-lloyd-materials-analysis-and-phase1-technical-recommendations.md`
- **Vault normalization model + call prep (NEW 2026-06-18):** `projects/gift-cards/docs/plans/2026-06-18-phase1-vault-normalization-design-note.md` — canonical card record, credential = url + typed secrets, ~7 supplier families, findings-vs-SOW, resolves all 4 open client questions; model left open for Tim.
- **Interactive decision artifact (NEW 2026-06-18):** `projects/gift-cards/docs/plans/2026-06-18-phase1-vault-decision-artifact.html` — self-contained single-file HTML (portable across accounts; render-verified, no console errors). Built from the design note.
- **Client presentation deliverables (committed):**
  - `projects/gift-cards/docs/plans/2026-05-27-progressive-client-presentation-redstamp.html` — branded walkthrough deck (HTML)
  - `projects/gift-cards/docs/plans/Progressive-Secure-Card-Vault-Phase-1-Walkthrough.pdf` — Phase 1 walkthrough PDF export
  - Draft variant (older): `projects/gift-cards/docs/plans/2026-05-27-progressive-client-presentation-draft.html`

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

1. **When resuming:** Read `2026-06-18-phase1-vault-normalization-design-note.md` first (model + call prep),
   then the `2026-06-17` analysis for renderer/technical detail.
2. **Tim review** — the canonical model + credential shape + ~7 supplier-family boundaries (does his
   importer prototype match?); reconcile our svg2pdf benchmark with his renderer/stack pick. (design note §7)
3. **Spencer decisions** — D-13 rate ($150 vs $160); gut-check the bounded-but-configurable SOW framing.
4. **Doug/Lloyd call** — confirm the model; close the 4 questions; Walmart manual-import + banner grouping;
   SystemBind/SystemOne naming; Walmart activation assets. (call flow in design note §8)
5. **SOW revision with Stephanie** — bounded-but-configurable language (§4) + D-13/D-14 + support proposal.
6. **Follow up with Lloyd:** Walmart activation program, cleanup/retention rules, Master Card fixtures.

## Blockers

- Walmart activation program deliberately withheld — confirm Phase 1 boundary.
- ~~Renderer choice pending spike~~ — resolved 2026-06-18 (svg2pdf). Remaining renderer task is ops, not a decision: ship Arial/Verdana fonts + set page size in the renderer image.
- D-13/D-14 are internal decisions, not external blockers.

## Decisions & context

- **2026-06-17 technical decisions:** Lloyd scripts = reference only; Phase 1 PDF = server-side hybrid;
  defer full invoice PDF parse.
- **2026-06-18 renderer decision:** svg2pdf (resvg family) chosen for Phase 1 Amazon cards — MAE 0.15/255
  vs Inkscape reference; Playwright (1.23) is fallback-only; CairoSVG (4.41) rejected. Ship Arial/Verdana
  in renderer image; set output page size. Evidence: `_private/.../runs/spike/`, analysis doc §4.
- **2026-06-18 normalization model:** vault owns a canonical card record; inputs are incidental; credential
  normalizes to `url + typed secrets`; ~7 supplier families not 23 formats; output rule-driven; Walmart is
  the bidirectional output exception. SOW reframes to bounded-but-configurable. Full doc:
  `projects/gift-cards/docs/plans/2026-06-18-phase1-vault-normalization-design-note.md`.
- **2026-06-16 client thread:** `projects/gift-cards/docs/discovery/2026-06-16-phase1-annotated-qa-thread.md`
- **SOW reconciliation:** `projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md`
- **April script review (superseded by 2026-06-17 analysis for fixture/E2E status):**
  `projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md`
- House rule: read CLIENT.md + REDSTAMP-SOW-CONTEXT.md before client-facing artifacts.
