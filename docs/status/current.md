# Status — rs-progressive-fundraising

> Session-start: read this file first. Session-end: update it following this section structure
> (full procedure: the Aurora `wrapup` skill, where installed).

## Current focus

**2026-08-25 operator update: the team has made substantial progress on the Phase 1 card vault and is
now preparing for a Progressive client demo.** The implementation details and disposition of the
August 12 QA/security handoffs were not enumerated in this session, so the older technical snapshot
below remains historical context rather than a claim that those blockers are still open.

**Phase 1 Card Vault: design QA round 2 (pre-UAT) + full security audit both complete; two
engineering handoffs ready for Tim, not yet sent.** Tim shipped the 2026-08-12 staging build
(Walmart Card Preparation step + Kaitlin's 8/12 styling list). We re-QA'd it with three parallel
agent lanes and separately ran a two-wave security audit of the GitLab source. Both produced
prioritized, agent-consumable handoffs. **Nothing has gone to Tim/Kaitlin/Slack — Spencer sends.**

**Design QA verdict: not ready for UAT — 4 P0 blockers** (2 server 500s seat-reproduced: create-order
+ Walmart file-upload import; status-pill lag confirmed by all 3 lanes; sidebar nav occlusion at
laptop height). Plus 9 P1. Tim's 8/12 fixes largely verified (11 items).
**Security verdict: no P0; 9 verified P1** (crypto boundary sound). Top: C-06 Walmart-import has no
reconciliation → bad cards can be allocated; C-01 crypto not fail-closed; **C-03 = SOW Q7
password-export commitment not built (build-to-spec, not a client question)**; C-04 dormant
double-spend.

**Canonical run packs:**
- Design QA: `docs/runs/2026-08-12-design-qa-uat/` → `CONSOLIDATED-FINDINGS.md`,
  `tim-eng-handoff-2026-08-12.html`.
- Security: `docs/runs/2026-08-12-security-audit/` → `WAVE1-CONSOLIDATED.md`,
  `tim-security-handoff-2026-08-12.html`, `WAVE0-REPORT.md`.

Vault app (read-only this session): `~/projects-work/progressive-card-vault/app` @ `08c0c74` (GitLab main).
Figma: `https://www.figma.com/design/Ztv1YtEx1S19i0w4bdHgo4/Digital-Gift-Card-Fulfillment-Design`.

## Last session

- **2026-08-25 — RapidCents payment-processor diligence (AUR2 Prime).** Retrieved Doug's August 22
  inquiry and prior Avery/Benji Pays correspondence using read-only Gmail access; ran independent
  public-source recon; recommendation is a gated diligence exercise and parallel pilot, not an
  immediate switch from Elavon. Durable analysis:
  `projects/gift-cards/docs/solutions/2026-08-25-rapidcents-payment-processor-diligence.md`. Spencer's
  live update says the card vault has advanced substantially and the team is preparing for a client
  demo; exact implementation status was not audited in this session.
- **2026-08-12 — Design QA round 2 + security audit (AUR2 Prime / Fable, Herdr `w1V`).** Tim's 8/12
  build re-QA'd by 3 recon lanes (Codex/Figma-fidelity, Claude/interaction-states, Grok/walkthrough);
  seat reproduced the create-order 500 firsthand + confirmed sidebar occlusion. Two-wave security
  audit: Wave 0 (gitleaks/npm-audit/config — clean); Wave 1 finders Codex (crypto/export/injection) +
  Opus 4.8 (authZ/intake/audit), Gemini-via-Cursor scoped verifier (5/6 confirmed, 1 narrowed, 0 false
  positives). Grok excluded from source (data-exposure ruling). Two HTML handoffs published as private
  Artifacts + copied to `~/Downloads/`. Reframed C-03 as SOW Q7 compliance after checking the 6/10
  responses to Doug.
- **2026-08-11 — Wrap of design↔dev reconcile (round 1, AUR2/Grok).** `PRIORITIZED-BACKLOG-v2.md`,
  Kaitlin design checkpoint DM sent; two P0s identified (Walmart step, semantic pills).

## In-flight work

- **RapidCents inquiry:** Doug is considering a processor change based on a lower-rate proposal and
  has asked Redstamp for advice and coordination. Recommended next move: get the full fee/contract and
  underwriting package, have Avery independently confirm Benji Pays compatibility, then run a
  controlled parallel pilot with Elavon left live. No processor change has been approved.
- **Client demo preparation:** live operator update says the team is preparing to demo the card vault.
  Confirm the current build, demo script, fixture data, and which prior QA/security items are closed
  before scheduling the walkthrough.
- **Awaiting Spencer:** send Tim the two handoffs (design + security). Design handoff is shareable
  with Tim; **security handoff is internal/build-team-only** (maps exploitable weaknesses — do not
  distribute to client).
- **Kaitlin:** queued to do a human QA pass *after* the agent round (her ask, Slack ts
  1786562864.456879). Comes after Tim's P0 fixes.
- **Doug's new "Gift Redemption Button" request** (Asana task 1217427026711277; Stephanie + Hannah
  Christie leading). A retiree/employee redemption form with a card+denomination dropdown pulling the
  full digital catalog; Doug confirmed "any of the cards." Stephanie flags it as a manual lift back
  into fulfillment with a possible Phase-2 vault-integration angle. Not on Redstamp's build plate yet
  — watch; Hannah mocking for Doug signoff.
- **Open PRs (this repo):** [PR #16](https://github.com/sririe/rs-progressive-fundraising/pull/16)
  carries the RapidCents diligence record and this status update. None in the vault app repo.
- **Canonical client thread:** Gmail `19e9a0905b082b87` (7/14 design requirements).

## Repo state

- Knowledge repo branch `codex/rapidcents-diligence` is pushed with open PR #16. Its only
  changes are this handoff and the RapidCents diligence record. The prior wrap landed via
  `session/2026-08-12-design-qa-security-audit`; `.gitignore` gained `.gstack/` (a lane working dir),
  and two run packs were added (design-qa ~11M incl. screenshots/figma-frames; security-audit 160K,
  gitleaks/npm-audit outputs redacted-verified).
- Vault app `main` @ `08c0c74`, read-only this session — **no writes to GitLab** (operator constraint).
  Local checkout synced 6241988 → 08c0c74.
- Herdr workspace `progressive design-qa · AUR2 · Fable` (`w1V`): PRIME tab + 5 dispatched recon lanes
  (3 design + 2 security), all verified done and closed at wrap. Gemini verifier ran as a one-shot
  cursor-agent (not a tab).
- Prior hygiene candidates (stale, offer only): `session/2026-07-13-sow-close-out`,
  `claude/sweet-lumiere-6058d1`, `codex/giftcard-vault-design`.

## Runtime & environment

- **Staging (internal only — never mention to Progressive):**
  `progressive-gift-cards-card-vault-staging.onrender.com`. Login via operator's Chrome session
  (Browser 1); agents cannot enter the password (hard rule) — operator logs in to unblock. Seeded
  users `redstamp` (admin), `elaine` (operations), `mario` (finance).
- **Vault prototype:** `gitlab.com/rs-dev/progressive-gift-cards-card-vault`. Local:
  `~/projects-work/progressive-card-vault/app`.
- **Figma PAT:** 1Password `Redstamp Automation Secrets` → `Redstamp Figma Comments Export`.
  Figma MCP reliable from Codex/Claude; Grok has no live Figma (used static exports).
- **Cross-model verifier:** `cursor-agent` (spencer@redstamp.com) → Gemini 3.1 Pro; **requires
  `--trust`** for a non-standard cwd (empty output otherwise — see solutions note). Grok CLI is
  `--allow`-flag based; Grok data-frozen for source review.
- **Slack for agents:** Codex `plugins.slack@openai-curated`; this Fable seat used the claude.ai Slack
  connector (read-only reads this session).
- **Rate:** $160 CAD/hr (D-13).
- Materials git-ignored: `projects/gift-cards/_private/lloyd-materials-06162026/`.

## Next steps

1. **Reconcile the live vault status:** confirm which August 12 QA/security findings have shipped,
   then prepare and dry-run the client demo against the current build.
2. **Reply to Doug on RapidCents:** recommend diligence and a controlled pilot; if Doug agrees,
   Redstamp coordinates the checklist while Avery/Benji Pays owns compatibility confirmation.
3. **If still outstanding (Spencer):** send Tim the two handoffs — design (`tim-eng-handoff-2026-08-12.html`) and
   security (`tim-security-handoff-2026-08-12.html`, internal-only). Optionally have me draft the Slack
   messages in your voice.
4. **Tim fixes any remaining P0s:** design 500s (create-order race, Walmart upload branch) + status-pill workflow
   state + sidebar occlusion; security C-06 → C-01 → **C-03 (build the Q7 password export)** → C-04.
5. **After fixes:** re-QA (agent), then Kaitlin human pass, then set staging Fiserv URL, then Progressive
   walkthrough.
6. **Harden going forward:** wire `/security-review` (diff-scoped) into the vault PR gate so future
   changes get a security pass automatically.
7. **Later / Phase 2 (deferred, do NOT build now):** secure delivery portal (expiring links, recipient
   access logs) — explicitly out of Phase 1 per Q7. Doug's Gift Redemption Button if it lands on our plate.

## Blockers

- None hard. Two design 500s and any security runtime-only claims have "confirm against Render logs"
  tails (source audit can't fully close them).
- Staging login requires the operator (agents can't authenticate) — recurring soft friction.

## Decisions & context

- **2026-08-12 — Grok excluded from source security audit** (data-exposure ruling; review lane frozen
  since cereblab). Design QA against staging UI with fake data was fine for Grok; source audit of the
  crypto/auth of a cash-equivalent vault was not.
- **2026-08-12 — Gemini-via-Cursor as scoped third-lineage security verifier** (snippets only, not a
  full-repo crawl — copied finding-local files into a scratch dir). Operator ruling: accept Google as a
  snippet-scoped verifier; not a full finder.
- **2026-08-12 — C-03 (exports have no password) is SOW spec-compliance, not a client decision.** The
  6/10 responses to Doug (Q7) committed password-protected export files with a unique random per-export
  password shown once, never filename-derived (`projects/gift-cards/docs/plans/2026-06-10-phase1-technical-responses-to-doug.md`).
  Expiring links / recipient access logs are Phase 2 (secure delivery portal) — deliberately deferred.
- **2026-08-12 — Severity discipline:** design QA and security both P0/P1-first; the two most severe
  design items (server 500s) were seat-reproduced before relay; security findings cross-verified by a
  third lineage before relay. Zero false positives reached the operator.
- **2026-08-10/11 — Round 1:** Walmart prep is an order step (Spencer+Kaitlin); agent QA before designer
  BugHerd; semantic pill labels (Paid-is-blue was a false diagnosis).
- **2026-07-14 — Merchant ruled**; Workspace-first collaboration; activation boundary (prepare/import
  only, Fiserv external). Glossary: `projects/gift-cards/docs/design/`.
- House rule: read `CLIENT.md` + `REDSTAMP-SOW-CONTEXT.md` before client-facing artifacts.
