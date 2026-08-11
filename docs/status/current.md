# Status — rs-progressive-fundraising

> Session-start: read this file first. Session-end: update it following this section structure
> (full procedure: the Aurora `wrapup` skill, where installed).

## Current focus

**Phase 1 Card Vault is sold; design↔dev reconcile is mid-flight.** Staging is internal-only
(`progressive-gift-cards-card-vault-staging.onrender.com` — never mention to Progressive).

AUR2 Prime (Grok) ran design QA orchestration (2026-08-10/11): Figma Screens + staging comparison,
adversarial gate, executable backlog for Tim. **Kaitlin has the design checkpoint DM** (Slack,
with three HTML attachments) and is the gate before Tim executes P0s. Full BugHerd still held.

**Canonical run pack:** `docs/runs/2026-08-10-design-dev-reconcile/`  
**Tim execute list:** `PRIORITIZED-BACKLOG-v2.md` (ignore v1).  
**Design QA report:** `DESIGN-QA-REPORT.md` (PASS adversarial).

Figma: `https://www.figma.com/design/Ztv1YtEx1S19i0w4bdHgo4/Digital-Gift-Card-Fulfillment-Design`  
Vault local: `~/projects-work/progressive-card-vault/app` @ `6241988` (GitLab main).

## Last session

- **2026-08-11 — Wrap of design↔dev reconcile session (AUR2 Prime / Grok).** Codex design-QA recon
  completed against live Figma Screens + logged-in staging. Adversarial review of the report: **PASS**.
  Executable `PRIORITIZED-BACKLOG-v2.md` written (P0: Walmart order prep step + semantic status labels;
  filters/shell/vault closed as close enough). Human HTML artifacts for Kaitlin + Tim list + full
  backlog. Slack DM to Kaitlin **sent** (Codex Slack connector; Spencer manually attached 3 HTMLs after
  OAuth finickiness). Waiting on her three yes/nos before Tim handoff. BugHerd still held.
- **2026-08-10/11 — Session kickoff.** Herdr `progressive-vault · AUR2 · Grok`. Vault main pulled
  (+81). Signed SOW PDF, morning Progressive sync + Kaitlin 1:1 transcripts, Figma comment export
  (94/82). Product ruling: Walmart prep as order step (Spencer+Kaitlin). Backlog v1 failed adversarial
  gate (Paid-is-blue misdiagnosis; Design Direction comment pollution).
- **2026-07-14 — SOW verbally approved; design kickoff pack (PR #13).**

## In-flight work

- **Waiting on Kaitlin:** reply to design checkpoint DM (Walmart step, pill labels, “already close”
  list). Pack: `docs/runs/2026-08-10-design-dev-reconcile/slack-dm-pack/`.
- **After Kaitlin greenlight:** hand Tim `PRIORITIZED-BACKLOG-v2.md` + `DESIGN-QA-REPORT.md`
  (eng). Human short list: `tim-build-list-human.html`.
- **P0 builds (Tim/Codex, after design OK):**
  1. `lane/walmart-order-preparation-step`
  2. `lane/semantic-order-status-pills`
  Then staging walkthrough fixture `PGC-1027` before P1 polish.
- **BugHerd 535328:** do not use as first capture; residual human visual only after P0 engineering.
- **Tim:** Progressive testing environment / fixtures (morning sync).
- **Open PRs:** none in this knowledge repo.
- **Canonical client thread:** Gmail `19e9a0905b082b87` (7/14 design requirements).

## Repo state

- Knowledge repo `main`: dirty at wrap (this handoff + `docs/runs/` pack) — commit+push as wrap.
- Vault app `main` @ `6241988`, clean, no local product edits this session.
- Herdr workspace `progressive-vault · AUR2 · Grok` (`w1P`): Prime tab + closed recon tabs
  (`close-ok · design-qa-staging`, `close-ok · slack-dm-kaitlin`).
- **Hygiene candidates (unchanged from 7/14; offer only):**
  `session/2026-07-13-sow-close-out`, `claude/sweet-lumiere-6058d1`, `codex/giftcard-vault-design`.
- Design docs: `projects/gift-cards/docs/design/`.

## Runtime & environment

- **Prototype:** `gitlab.com/rs-dev/progressive-gift-cards-card-vault`. Local:
  `~/projects-work/progressive-card-vault/app`. Staging internal-only (Render free tier).
- **Figma PAT:** 1Password `Redstamp Automation Secrets` → `Redstamp Figma Comments Export`.
- **Slack for agents:** Codex `plugins.slack@openai-curated` (ChatGPT OAuth — can require browser
  reconnect). Grok seat has **no** Slack connector; use Codex for Slack DMs/files or operator paste.
- **Notify-operator:** works with `NOTIFY_OPERATOR_DIRECT=1` on this Mac (iMessage to
  `spencer@ririe.net`; chat.db verify may be unverified).
- **Workspace surfaces:** Language Rulings Sheet `1wsZCg5Yy0qz-ywLxHp1Lt1k4u_jAs7wowUH3COemNbc`;
  kickoff/primer gdocs (IDs in prior status). gog SA for Drive/Docs/Sheets; Gmail not SA-scoped.
- **Rate:** $160 CAD/hr (D-13).
- Materials git-ignored: `projects/gift-cards/_private/lloyd-materials-06162026/`.

## Next steps

1. **First:** Read Kaitlin’s Slack reply when it lands; fold any label/string/“still wrong” notes into
   `PRIORITIZED-BACKLOG-v2.md` if needed.
2. **Then:** Hand Tim the eng pack (`PRIORITIZED-BACKLOG-v2.md` + `DESIGN-QA-REPORT.md`); ask for
   `#progressive-fundraising` changelog after each UI staging deploy.
3. **Tim builds P0:** Walmart order prep step, then semantic status pills; walkthrough `PGC-1027`.
4. **Only then:** optional BugHerd residual pass for humans; P1 disclosure defaults + language cleanup.
5. **Later / still open:** Phase 2 export/delivery brief; Lloyd SystemBind/Walmart activation materials;
   rulings Sheet → glossary regen if language batch advances.

## Blockers

- **Kaitlin design checkpoint** (in flight — not blocked, waiting).
- BugHerd before P0 eng: **deliberately held**.
- (Stale from 7/14 may still apply if never done: Sheet/gdoc sharing to full team; kickoff decisions 1–5.)
- D-15 export-password deferred — V1 System Bind; not blocking.

## Cross-cutting note — Grok / security

Historical (2026-07-14): Grok review lane FROZEN after cereblab incident; this knowledge repo did not
upload client data. **This session used Grok as AUR2 Prime** for orchestration (durable work written
to repo docs only). Prefer Codex for Slack connector and live Figma MCP reliability; Grok for
orchestrator seat when Spencer chooses.

## Decisions & context

- **2026-08-11 — Design QA report PASS (adversarial).** Staging closer than draft backlog implied;
  only two true P0s before Progressive walkthrough: Walmart prep as order step; semantic status
  labels (not Paid-is-blue color). Filters/shell/vault closed. Record:
  `docs/runs/2026-08-10-design-dev-reconcile/ADVERSARIAL-REVIEW-DESIGN-QA-REPORT.md`.
- **2026-08-10 — Walmart prep is an order workflow step** (Spencer + Kaitlin 1:1). Soft edge:
  generation complexity may nest; step presentation on order is fixed. Fiserv stays outside app.
- **2026-08-10 — Agent design QA before designer BugHerd** (Spencer commitment to Kaitlin).
- **2026-08-10 — Changelog hygiene:** after each Codex UI staging deploy, short note in
  `#progressive-fundraising` (routes / frames / remaining gaps).
- **2026-07-14 — Merchant ruled**; Workspace-first collaboration; Doug PDF-in-ZIP for legacy;
  activation boundary (prepare/import only). Glossary: `projects/gift-cards/docs/design/`.
- House rule: read `CLIENT.md` + `REDSTAMP-SOW-CONTEXT.md` before client-facing artifacts.
