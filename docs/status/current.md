# Status — rs-progressive-fundraising

> Session-start: read this file first. Session-end: update it following this section structure
> (full procedure: the Aurora `wrapup` skill, where installed).

## Current focus

**2026-09-09: new business-development thread — IdeaSource partner API inquiry.** An employee
recognition company (Calvin Tang, IdeaSource) asked Progressive for an API to submit gift-card
orders from their own system; Doug forwarded it asking what's involved and framed it as the first
move into the loyalty/rewards segment. Spencer replied same day (capability yes, priced to
"some technical work", discovery questions supplied for Doug+Gord's meeting with IdeaSource).
Assessment + technical gap analysis:
`projects/gift-cards/docs/plans/2026-09-09-ideasource-partner-api-assessment.md`. Internal review
ticket with Tim: Asana `1218337331514879`. If it advances, it likely becomes a scoped Phase 2 SOW
(partner order capture also carries the white-label portal idea and email distribution).

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

- **2026-09-09 — IdeaSource partner API inquiry (AUR2 Prime / Fable, Herdr `w38`).** Retrieved
  Doug's same-day inbound (Gmail thread `1a0877cf7180a4f7`), ran a read-only survey of the vault
  app's order capture, and assessed the ask: the WordPress/Formidable intake already implements
  the partner-API pattern (HMAC per-connection auth, idempotent, Zod-validated); gaps are a
  partner/credential entity, stable vendor codes, status endpoints, hardening, and the automated
  allocation/delivery fork. Full read:
  `projects/gift-cards/docs/plans/2026-09-09-ideasource-partner-api-assessment.md`. Drafted the
  Doug reply in Spencer's voice (staged as Gmail draft); Spencer simplified and sent ~13:09 PT.
  Filed Asana `1218337331514879` ([Progressive] IdeaSource Partner API Inquiry, assignee Tim,
  Stephanie following) for Tim's technical read. Voice-canon verdict candidates from both edits
  handed to the aurora-skills prime seat for a SPENCER-VOICE-DNA version-log entry (operator
  promotes).
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
## In-flight work

- **IdeaSource partner API inquiry:** Spencer's reply sent 2026-09-09 (thread `1a0877cf7180a4f7`).
  Two open loops: (1) Tim's technical read on Asana `1218337331514879` — if he flags anything
  load-bearing, expectations with Doug get adjusted before scoping; (2) Doug+Gord's meeting with
  IdeaSource — its answers (volume, delivery model, payment) size the Phase 2 opportunity.
  Assessment doc: `projects/gift-cards/docs/plans/2026-09-09-ideasource-partner-api-assessment.md`.
- **Voice-canon verdicts (aurora-skills, cross-repo):** the aurora prime seat (Herdr `w37:pC`) was
  handed a brief on 2026-09-09 to append this session's edit verdicts to `SPENCER-VOICE-DNA.md`
  as candidates; lands via aurora's PR gate, Spencer promotes.
- **RapidCents inquiry:** Spencer sent the advisory response on August 25, recommending that Progressive
  first ask Elavon to match the written 2.00% offer, then clarify RapidCents' Elavon relationship and
  contract terms and have Avery independently confirm Benji Pays compatibility before any parallel
  pilot. Doug replied, "Thanks Spencer, this is very helpful information." No processor change has been
  approved. Canonical Gmail thread: `1a02bb25c1689fe5`; sent message: `1a03a745e70ca3e4`.
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
- **Open PRs:** none (this repo or the vault app repo); PR #16 merged 2026-09-09.
- **Canonical client thread:** Gmail `19e9a0905b082b87` (7/14 design requirements).

## Repo state

- PR #16 (RapidCents diligence + IdeaSource assessment + handoff) merged to `main` 2026-09-09;
  its branch deleted local + remote. All 16 repo PRs are merged — no open or abandoned PRs. The prior wrap landed via
  `session/2026-08-12-design-qa-security-audit`; `.gitignore` gained `.gstack/` (a lane working dir),
  and two run packs were added (design-qa ~11M incl. screenshots/figma-frames; security-audit 160K,
  gitleaks/npm-audit outputs redacted-verified).
- Vault app `main` @ `08c0c74`, read-only this session — **no writes to GitLab** (operator constraint).
  Local checkout synced 6241988 → 08c0c74.
- Herdr workspace `progressive design-qa · AUR2 · Fable` (`w1V`): PRIME tab + 5 dispatched recon lanes
  (3 design + 2 security), all verified done and closed at wrap. Gemini verifier ran as a one-shot
  cursor-agent (not a tab).
- 2026-09-09 hygiene sweep: remote is clean — only `main` remains; the prior stale-branch
  candidates no longer exist on the remote.

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
1a. **IdeaSource follow-through:** when Tim responds on Asana `1218337331514879`, reconcile his
   read with the assessment doc; when Doug reports back from the IdeaSource meeting, feed the
   answers (volume, delivery model, payment) into a Phase 2 partner-order-capture scoping draft.
   (PR #16 merged 2026-09-09.)
2. **If Doug advances RapidCents:** start with an Elavon rate-match request. If Elavon will not match,
   Redstamp coordinates the diligence checklist while Avery/Benji Pays owns compatibility confirmation.
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

- **2026-09-09 — Partner-API framing: one order-capture foundation serves three channels** (partner
  API, white-label portals, email distribution), and client-facing commitment stays priced to
  verification state (Tim reviews before scoping firms). Rationale + technical gaps:
  `projects/gift-cards/docs/plans/2026-09-09-ideasource-partner-api-assessment.md`.
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
