# Status — rs-progressive-fundraising

> Session-start: read this file first. Session-end: update it following this section structure
> (full procedure: the Aurora `wrapup` skill, where installed).

## Current focus

**Phase 1 (Secure Card Vault) is SOLD and in the design phase.** Doug verbally approved 2026-07-14
("Sounds good, thanks Spencer", canonical Gmail thread `19e9a0905b082b87`, 17:38 UTC); the Support &
Maintenance SOW went out via HelloSign/Dropbox Sign the same day (Spencer's signature also requested —
inbox). Tim's working prototype is the source of truth (`gitlab.com/rs-dev/progressive-gift-cards-card-vault`;
local checkout `~/projects-work/progressive-card-vault/app`); a Figma import of all screens is the design
team's mirror. The design team (Candace + Kaitlin designing, Hannah ratifying, Stephanie PM) onramps via
the **design kickoff pack** in `projects/gift-cards/docs/design/` (PR #13, merged): success = a named
Progressive operator completes their first login unaided; phase 1 = the language pass; phase 2 = the
export/delivery flow redesign (Doug's 7/14 ruling: legacy clients keep PDF-in-ZIP, new clients move to
the simpler URL path).

## Last session

- **2026-07-14** — SOW verbally approved; full design-team onramp shipped. (1) **Design kickoff pack**
  (PR #13, merged): UI string inventory (~380 strings from prototype @ `bd1f16d`, audited against Tim's
  own Content Style rules — 7 dev-language leaks flagged, per-profile CSV lock status, placeholder
  Card Preparation screen excluded), design glossary (**Merchant ruled from canon** — the vault design
  note uses *merchant* 24–0; Client/Customer is open ruling #2, Hannah's first ratification), design
  primer, kickoff run-sheet. Codex cross-lineage review: 4 rounds, receipt on the PR. (2) **Workspace
  surfaces** (ruling: humans work in Workspace; the team Claude project holds read-only snapshots):
  rulings Sheet + two rs-pageless-branded gdocs (IDs under Runtime), built with the new one-shot
  batchUpdate renderer. Team Claude project "Progressive Fundraising Card Vault" (Redstamp workspace)
  loaded with the pack + Tim's two docs; project instructions/description drafted; Drive + Figma
  connectors recommended. (3) **Aurora tooling fallout** (merged to aurora main #405–#407):
  `md_to_batchupdate.py` one-shot Docs renderer (Apps Script route retired — SA-unsupported), CI gates
  in lane-verify/orch-verify ("PR opened" ≠ "PR done"; operator caught two failing PRs — capture:
  aurora `docs/solutions/2026-07-14-pr-done-means-ci-green.md`). Discovery worth repeating: **Tim's
  `docs/designer-user-flows.md` + style-guide Content Style section are designer-grade** — the audit
  extends them, never replaces.
- **2026-07-13** — Doug close-out package SENT (PR #12): all 8 answers, S&M Agreement (settled 8 hrs /
  $1,280 CAD+tax/mo in Stephanie's official retainer-template doc `1-NdeN-hbG8y3Miw-YxpwdbgcE5wfUEOQUmcerguyASw`),
  7-diagram merchant-workflow PDF, 3 yellow-highlighted SOW v2 edits applied in place (v2 doc
  `1aVIGSjhgzW6Eu95etE9MuubQEjoCXGm1Ucv4SqUJ8Vg`). Master doc:
  `projects/gift-cards/docs/plans/2026-07-13-doug-7-01-response-plan.md`.
- **2026-06-29** — SOW v2 amendment built + sent via #am-pm-review; amendment recipe captured in
  `docs/solutions/workflow-issues/gog-docs-amendment-edits-System-20260629.md`.

## In-flight work

- **Canonical client thread:** Gmail `19e9a0905b082b87` — fresh 7/14 design requirements live here
  (Lloyd's Loblaws/Shoppers OUTPUT correction; Doug's PDF-in-ZIP-stays-for-legacy ruling).
- **Design phase, week 1 (language pass):** designers rule in the Sheet; Tim applies "Ratified = yes" +
  "accept" rows in one batch. First application: Merchant replaces ~30 "Vendor" UI strings.
- **Kickoff decisions pending:** Tim's change-request format + Figma re-import cadence; GitLab view
  access for Candace/Kaitlin; standing sync cadence. (Agenda: the kickoff doc's "Decisions needed".)
- **Open PRs:** none in this repo.
- **Waiting on Spencer:** share the rulings Sheet + both gdocs to the team (sharing = operator-only);
  sign the S&M HelloSign request; record the Figma file URL durably (still nowhere in the repo).
- **Still open from pre-SOW:** National Zakat Foundation call; SystemBind activation tool + Walmart
  activation program still not received from Progressive.

## Repo state

- `main` clean, synced. PR #13 merged 7/14.
- **Hygiene candidates (verified merged; deletion offered at 7/14 wrap, not executed):**
  `session/2026-07-13-sow-close-out` (PR #12 merged, tip matches, herdr worktree clean),
  `claude/sweet-lumiere-6058d1` (PR #11 merged) + its detached `.claude/worktrees/` checkout,
  `codex/giftcard-vault-design` (no PR; 0 unmerged commits). Both host-branded names are sunset
  (ruling 2026-07-14).
- **Design docs home:** `projects/gift-cards/docs/design/` — inventory, glossary, primer, kickoff.
  The glossary markdown is the *record*; the live working surface is the Google Sheet.

## Runtime & environment

- **Prototype:** `gitlab.com/rs-dev/progressive-gift-cards-card-vault` (SSH as @sririe works; https
  prompts). Local checkout: `~/projects-work/progressive-card-vault/app` — Next.js / Node 22 + Prisma +
  Postgres. **Staging on Render free tier is internal-only; Progressive does not know staging exists —
  keep it out of all client comms.** Production plan: Render Pro (~USD $25/mo + compute) + ~$6/mo DB.
- **Workspace surfaces (spencer@redstamp.com Drive; gog DWD service account works for Docs/Drive/Sheets
  reads+writes — ignore the `auth list --check` invalid_rapt red herring; Gmail is NOT in SA scope, use
  the Gmail MCP):** rulings Sheet `1wsZCg5Yy0qz-ywLxHp1Lt1k4u_jAs7wowUH3COemNbc` ("Progressive Card
  Vault — Language Rulings", 3 tabs); kickoff gdoc `18hw5LuP_BC7ordyDOA1p1GqnrI9B0Smp-ZgFu92WR1U`;
  primer gdoc `1-XLjsCli0y9mQrH1u_1HzGTWMeDQEWyd9wP2ofFNJSs`. **Sync contract:** after ruling batches,
  regenerate the repo glossary/inventory markdown from the Sheet, then refresh the team Claude project
  copies.
- **Team Claude project:** "Progressive Fundraising Card Vault" in the Redstamp claude.ai workspace —
  read-only snapshots (the pack + Tim's two docs). Team-safe staging: `~/Documents/progressive-team-project-drop/`.
- **Fast gdoc rendering:** aurora `skills/operations/gog-workspace/scripts/md_to_batchupdate.py` (one
  batchUpdate call; gates + usage in aurora `docs/solutions/2026-07-14-gdoc-one-shot-batchupdate-renderer.md`).
  Not yet on installed hosts — publish pipeline wedged (RED-197).
- **Rate:** $160 CAD/hr (D-13).
- Materials local-only (git-ignored): `projects/gift-cards/_private/lloyd-materials-06162026/`.

## Next steps

1. **When resuming:** read `projects/gift-cards/docs/design/2026-07-14-design-kickoff.md` + check the
   rulings Sheet for design-team progress on the language pass.
2. **After the first ruling batch:** regenerate glossary/inventory md from the Sheet, refresh the Claude
   project copies, hand Tim the apply-list.
3. **Phase 2 prep (weeks 2–4):** export/delivery flow redesign brief from the 7/14 thread requirements.
4. **Spencer + Tim build-alignment sync** (post-signature): firm dates; seed agenda from the 7/13
   response-plan addendum build flags (import-engine maturity, Mode B PDF templates/acceptance criteria,
   PC/Loblaws columns).
5. **Follow up with Lloyd:** SystemBind activation tool + Walmart activation program.

## Blockers

- Team can't reach the Sheet/gdocs until Spencer shares them (operator-only action).
- Kickoff decisions 1–5 unanswered until the meeting output lands.
- (D-15 export-password: deferred by 7/13 ruling — V1 = System Bind protection; not blocking.)

## Cross-cutting note — Grok CLI data incident (2026-07-13)

Audit verdict for THIS repo: **did NOT upload** (single 6/27 session, 0 items, confirmed) — no
client-notification question for Progressive. Fleet rule: Grok dispatches = clean-room synthetic
payloads only, never a real checkout. Grok remains FROZEN (security ruling 2026-07-14).

## Decisions & context

- **2026-07-14 — Merchant ruled** (not Vendor/Supplier), from canon; locked client-format CSV headers
  keep `Gift Card Vendor` as documented exceptions. Record:
  `projects/gift-cards/docs/design/2026-07-14-design-glossary.md`.
- **2026-07-14 — Workspace-first collaboration:** working docs live in Google Workspace; the team
  Claude project is a read-only retrieval layer; repo markdown is the versioned record. (Spencer:
  static project-knowledge files are never working surfaces.)
- **2026-07-14 — Doug's output ruling:** PDF-in-ZIP stays for existing clients; new clients get the
  simpler URL path. Phase-2 design driver.
- **2026-07-14 — Activation boundary (glossary law):** the app prepares merchant work files and imports
  activated results; only Progressive activates, outside the app.
- **2026-07-13 — S&M shape:** fixed monthly fee w/ included hours (8 hrs / $1,280 CAD+tax/mo); defect
  fixes never change-ordered; new-pattern merchants = S&M work (2–4 hrs); self-serve merchant-config UI
  = Phase 2 candidate.
- Prior: SOW amendment decisions (6/29), 6/23 call rulings, normalization model — see
  `projects/gift-cards/docs/plans/2026-06-18-phase1-vault-normalization-design-note.md` and
  `2026-07-13-doug-7-01-response-plan.md`.
- House rule: read CLIENT.md + REDSTAMP-SOW-CONTEXT.md before client-facing artifacts.
