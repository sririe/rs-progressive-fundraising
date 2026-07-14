# Status — rs-progressive-fundraising

> Session-start: read this file first. Session-end: update it following this section structure
> (full procedure: the Aurora `wrapup` skill, where installed).

## Current focus

Phase 1 (Secure Card Vault) — **full close-out package SENT to Doug 7/13 (evening).** Everything he gated
signing on is in his hands: amended SOW v2 (3 new yellow-highlighted edits), the S&M Agreement (8 hrs /
$1,280 CAD+tax/mo in Stephanie's official retainer-template doc), the 7-diagram merchant-workflow PDF,
and written answers to all 8 clarification questions. **Ball is with Doug/Lloyd** → on their OK, Stephanie
sends SOW + S&M together via Dropbox Sign. Nothing Redstamp-side is blocking.

- **Master doc for the close:** `projects/gift-cards/docs/plans/2026-07-13-doug-7-01-response-plan.md`
  (Doug's asks → proposed answers → punch list to signature).
- **v2 SOW (Google Doc, incl. the 7/13 edits):** `1aVIGSjhgzW6Eu95etE9MuubQEjoCXGm1Ucv4SqUJ8Vg`. **S&M doc
  of record:** `1-NdeN-hbG8y3Miw-YxpwdbgcE5wfUEOQUmcerguyASw` (Stephanie's retainer-template port).

## Last session

- **2026-07-13** — Reconstructed the week (email/Slack/Drive; no repo commits since 6/29; no Progressive
  client call last week — the "last call" remains 6/23; the 6/29 "Progressive Design Kick-Off" was internal
  design, Candace + Kaitlin starting UX review of Tim's staging app). Built the Doug close-out package:
  1. **S&M Agreement draft** — `2026-07-13-support-maintenance-agreement-draft.md` + branded Google Doc
     (rs-pageless; retainer template unregistered in branded-gdoc). **Settled 7/13: $1,280 CAD + tax/mo, 8 hrs included** (Stephanie proposed 10; Spencer capped at 8;
     two-month calibration review language in the Doug email). **Doc of record moved to the official
     retainer template by Stephanie: `1-NdeN-hbG8y3Miw-YxpwdbgcE5wfUEOQUmcerguyASw` — already reads 8 hrs;
     tell Stephanie 8 stands (she thought she had to revert to 10).**
  2. **Merchant workflow diagrams** — `2026-07-13-merchant-flow-diagrams.html` (overview + 6 patterns:
     CashStar URL+challenge, URL-only, PC URL+acct+PIN, code+PIN, Amazon claim-code→PDF, Walmart
     bidirectional activation). Print to PDF for Doug/Lloyd.
  3. **Answers to Doug's 8 questions** — in the response plan; three imply small yellow-highlight SOW
     edits (Q1 "first set" wording, Q4 inventory CSV export, Q7 support-request activity records).
  4. **Doug email SENT 7/13** on thread `19e9a0905b082b87` — all 8 answers + calibration note, with
     S&M PDF + diagrams PDF attached. Tim/Codex reviewed the diagrams pre-send (triage in the response
     plan's addendum; 2 wording fixes folded in, build flags captured internally).
- **2026-06-29** — SOW v2 amendment built + sent to #am-pm-review; Stephanie sent to Doug same day.
  Transcripts ported; amendment plan written.

## In-flight work

- **Doug close-out package — SENT 7/13.** Awaiting Doug/Lloyd reply → Stephanie Dropbox Signs both docs.
- **Design track (parallel, internal):** Candace + Kaitlin doing UX review of Tim's staging build in Figma
  (Codex review packet); Spencer owed them fixed screenshots + design-system load. Not SOW-blocking.
- **Other worktree:** main repo checkout parked on `codex/giftcard-vault-design`.

## Punch list to signature

| # | Item | Owner | State |
|---|---|---|---|
| 1 | S&M price | settled | **8 hrs / $1,280/mo** — Stephanie's template doc already reads 8; confirm to her in-thread |
| 2 | Q6b posture: self-serve merchant config named as Phase 2 candidate | settled | sent that way in the email |
| 3 | Diagrams: review + export to PDF | done | Tim-reviewed, sent |
| 4 | 3 small SOW edits (yellow-highlighted) | Claude (gog docs) | **DONE 7/13** — applied to v2 in place (yellow = delta-from-v1 rule holds), verified via HTML export |
| 5 | Slack message to Stephanie in #am-pm-review | **SENT 7/13** (Spencer; Tim tagged) — Stephanie re-templated + repriced; settled at 8 hrs in her thread | |
| 6 | Doug email + attachments | **SENT 7/13** (Spencer) | package complete: answers + S&M + diagrams |
| 7 | Firm timeline dates | Spencer + Tim | SOW keeps relative dates — NOT blocking |
| 8 | D-15 export-password mechanism | Spencer + Tim | deferred; V1 = System Bind protection; not blocking |
| 9 | PM approval → Dropbox Sign (SOW + S&M together) | Stephanie | after Doug OKs |

## Repo state

- Session docs land via PR from `session/2026-07-13-sow-close-out`: response plan, S&M draft, diagrams
  HTML, this status update.

## Runtime & environment

- **App codebase (cross-repo):** `~/projects-work/progressive-card-vault/app` — Next.js / Node 22 + Prisma +
  Postgres (Tim's build). Staging on Render free tier — **internal only; Progressive does not know staging
  exists; keep it out of all client comms.** Production = Render Pro (~USD $25/mo + compute) + ~$6/mo DB.
- **gog:** `~/.local/bin/gog` v0.31.1; Docs/Drive via DWD service account (ignore `auth list --check`
  red herring). Gmail NOT in SA scope — use Gmail MCP. Recipe:
  `docs/solutions/workflow-issues/gog-docs-amendment-edits-System-20260629.md`.
- **Rate:** $160 CAD/hr (D-13); `CLIENT.md` corrected 7/13.

## Next steps

1. **Wait on Doug/Lloyd's reply** to the 7/13 package; on OK, Stephanie sends SOW + S&M via Dropbox Sign.
2. If Doug pushes back on the 8-hr S&M sizing, the position: two-month usage review, right-size together
   (language already in the sent email).
3. Spencer + Tim: firm dates + build-alignment sync (post-signature fine; SOW keeps 6–8 weeks +
   October-peak target). Seed agenda: the internal build flags in the 7/13 response-plan addendum
   (import-engine maturity, Mode B PDF templates/acceptance criteria, PC/Loblaws columns).
4. Design track continues in parallel (not client-facing until SOW signed).

## Blockers

- None Redstamp-side. Waiting on the client.

## Cross-cutting note — Grok CLI data incident (2026-07-13)

xAI's Grok Build CLI bulk-uploaded repo archives to a vendor bucket (public disclosure 7/13). Audit
verdict for THIS repo: **rs-progressive-fundraising did NOT upload** (single 6/27 session, 0 items,
confirmed) — no client-notification question for Progressive. Operator-level containment complete;
full record in Claude memory (`project_grok-cli-exposure-2026-07-13`) + checklist artifact. Fleet
rule pending write-up: Grok dispatches = clean-room synthetic payloads only, never a real checkout.

## Decisions & context

- **2026-07-13:** S&M shape = fixed monthly fee w/ included hours (Doug's ask was cost certainty);
  defect fixes never change-ordered — warranty free, then from included hours; new-pattern merchants
  = S&M work (2–4 hrs) w/ end-to-end validation, per 6/23 decision; self-serve merchant-config UI
  positioned as Phase 2 candidate, not Phase 1 scope.
- **2026-06-29 SOW amendment decisions** (unchanged): yellow-highlighted v2, v1 preserved; D-15 deferred;
  relative timeline; Render named w/ approximate cost; new-merchant additions = S&M not change orders.
- **6/23 call:** normalization model endorsed; Walmart on-demand; System Bind stays for V1.
- Prior: reconciliation `2026-06-10-phase1-sow-reconciliation.md`; design note
  `2026-06-18-phase1-vault-normalization-design-note.md`.
- House rule: read CLIENT.md + REDSTAMP-SOW-CONTEXT.md before client-facing artifacts.
