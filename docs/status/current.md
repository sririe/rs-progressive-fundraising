# Status — rs-progressive-fundraising

> Session-start: read this file first. Session-end: update it following this section structure
> (full procedure: the Aurora `wrapup` skill, where installed).

## Current focus

Phase 1 (Secure Card Vault) — **model + call-prep artifact are done and facts-corrected; parked pending Tim
review, the Doug/Lloyd call, and SOW revision.** The deliverable is an interactive **decision board**
(`2026-06-18-phase1-vault-decision-artifact.html`) backed by the **normalization design note** (same date):
the vault owns a canonical card record, credential normalizes to `url + typed secrets`, ~7 card families
(not 23 formats), output is rule-driven, Walmart is the one bidirectional exception. Our analysis converged
with Lloyd's "inhomogeneous by supplier" and James's "general system" framing — the alignment headline for
the call. Board + note were re-grounded 2026-06-23 against Doug's 6/16 email (fixing earlier re-litigation
drift) and voiced in Spencer's register. **Biggest open item: the D-15 export-password mechanism** — a
shown-once password breaks on multi-file orders; Spencer + Tim owe a real answer before the SOW. **Read
first:** the design note, then the `2026-06-17` analysis for renderer/technical detail.

## Last session

- **2026-06-23** — Turned the normalization model into a clean **decision board** artifact (replaced the
  prose-heavy version). Ran a **Codex adversarial-PM review**, applied its P1 fixes, then **re-grounded the
  facts from Doug's 6/16 email** after Spencer caught re-litigation drift: roles resolved (Doug's names),
  SystemBind confirmed (we'd mislabeled it SystemOne), Amazon output reopened, rate settled at $160, D-15
  export-password flagged unsolved/top-priority, fixtures narrowed (package received; only SystemBind +
  Walmart activation tools outstanding). Voiced the board in Spencer's register (canon-fed, approved).
  Reconciled the design note to match. Netlify-ready copy at `~/Documents/progressive-phase1-decisions/index.html`.
  PRs #6–#9 merged.
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
- **Decision artifact (live on `main`):** `2026-06-18-phase1-vault-decision-artifact.html` — board form,
  voiced, facts-corrected. Counts: **8 open / 5 for-the-call / 4 resolved**. Netlify-ready copy in `~/Documents/`.
- **Biggest open — D-15 export-password mechanism** (Spencer + Tim): a shown-once password breaks on
  multi-file orders; needs a real design before the SOW.
- **Amazon output reopened** (Spencer + Tim, with Lloyd): activation-tool/SystemBind output vs vault output;
  bundled ZIP vs per-card files. Clarify what Progressive sends today and what we produce.
- **Waiting on Tim:** his renderer/stack pick (reconcile our svg2pdf benchmark to it); whether his importer
  prototype already encodes the canonical record/credential.
- **SOW framing** (Spencer + Tim → Stephanie): configurable for today's card formats; a format that doesn't
  fit the config = software change (change order). Gut-check before it reaches the SOW.
- **Doug locked 2026-06-16:** active offerings (MasterCard yes; Browns/Hudson's Bay no; Uber not now);
  in-house generation = Amazon, Walmart, Chapters-Indigo. Manual Walmart import v1 = "still to be discussed."
- **Resolved 2026-06-23 (were open):** roles & access (Doug named them: Admin = Doug + Elena; Operations =
  new hire, Lisa, Lloyd); SystemBind naming (it's SystemBind); D-13 rate ($160).
- **Still missing from Progressive:** SystemBind activation tool + Walmart activation program. Rest received.
- **National Zakat Foundation call:** still needs scheduling.

## Repo state

- **Decision artifact (current deliverable):** `projects/gift-cards/docs/plans/2026-06-18-phase1-vault-decision-artifact.html` — self-contained interactive decision board (voiced, facts-corrected 2026-06-23, render-verified). Deploy copy at `~/Documents/progressive-phase1-decisions/index.html`.
- **Vault normalization model + call prep:** `projects/gift-cards/docs/plans/2026-06-18-phase1-vault-normalization-design-note.md` — reconciled 2026-06-23 to match the board; Spencer-internal long-form.
- **Phase 1 analysis (renderer/technical):** `projects/gift-cards/docs/plans/2026-06-17-lloyd-materials-analysis-and-phase1-technical-recommendations.md`
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
- **Deploy copy (local, not in repo):** `~/Documents/progressive-phase1-decisions/index.html` — byte copy of
  the committed decision artifact, named for Netlify Drop. Re-create by copying the committed `.html`; not a
  cold-start dependency.
- **Spiral MCP** (voice tool) disconnected this session; not needed — voice is canon-fed via the `my-voice`
  skill + `aurora-skills/.agents/context/voice/SPENCER-VOICE-DNA.md`. Re-auth tools exist if wanted.

## Next steps

1. **When resuming:** open the decision board `2026-06-18-phase1-vault-decision-artifact.html` (or its design
   note) — it's the live picture: 8 open / 5 for-the-call / 4 resolved.
2. **D-15 export password (top priority, Spencer + Tim)** — design a mechanism that survives multi-file
   orders; the shown-once approach is dead.
3. **Amazon output (Spencer + Tim, with Lloyd)** — clarify activation-tool vs vault output, and bundled ZIP
   vs per-card files.
4. **Tim review** — canonical model + credential shape + ~7 card-family boundaries vs his importer prototype;
   reconcile our svg2pdf benchmark with his renderer/stack.
5. **Doug/Lloyd call** — confirm the model; remaining questions (stray-card residual risk, hosting, Loblaws
   banner list); Walmart manual import; the still-missing SystemBind + Walmart activation tools. (design note §8)
6. **SOW with Stephanie** — configurable-scope language (§4) + D-14 + support proposal (Stephanie + Tim).
7. **Follow up with Lloyd:** SystemBind activation tool, Walmart activation program, cleanup/retention rules,
   Master Card fixture.

## Blockers

- **D-15 export-password mechanism unsolved** — shown-once password breaks on multi-file orders; blocks the SOW.
- **Still missing from Progressive:** SystemBind activation tool + Walmart activation program (rest received).
- Walmart activation program deliberately withheld — confirm the Phase 1 boundary on the call.
- Renderer is ops, not a decision: ship Arial/Verdana fonts + set page size in the render image (pending Tim's stack).

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
- **2026-06-23 corrections (re-grounded from Doug's 6/16 email):** SystemBind is the name (we'd said
  SystemOne); rate settled at $160; roles named by Doug (Admin = Doug + Elena; Operations = new hire, Lisa,
  Lloyd); Amazon output reopened (activation-tool vs vault, ZIP vs per-card); D-15 export-password unsolved.
  Decision artifact rebuilt as a voiced board; design note reconciled to match. SOW trigger is now "a card
  format that doesn't fit the config = software change," not "new supplier family."
- **2026-06-16 client thread:** `projects/gift-cards/docs/discovery/2026-06-16-phase1-annotated-qa-thread.md`
- **SOW reconciliation:** `projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md`
- **April script review (superseded by 2026-06-17 analysis for fixture/E2E status):**
  `projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md`
- House rule: read CLIENT.md + REDSTAMP-SOW-CONTEXT.md before client-facing artifacts.
