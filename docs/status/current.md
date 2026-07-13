# Status — rs-progressive-fundraising

> Session-start: read this file first. Session-end: update it following this section structure
> (full procedure: the Aurora `wrapup` skill, where installed).

## Current focus

Phase 1 (Secure Card Vault) — **closing Doug's 7/1 pre-signing asks so the SOW can go to Dropbox Sign.**
Timeline: SOW v2 went to Doug 6/29 (Stephanie). Doug replied **7/1: two items before signing** (a known
S&M fee; the workflow diagrams promised to Lloyd) **plus 8 clarification questions**. Doug nudged 7/8
(third nudge); Spencer sent a holding reply 7/8 ("updated SOW + S&M draft + diagrams coming together") —
**none of which existed until this session built them (7/13).**

- **Master doc for the close:** `projects/gift-cards/docs/plans/2026-07-13-doug-7-01-response-plan.md`
  (Doug's asks → proposed answers → punch list to signature).
- **v2 SOW (Google Doc, unchanged since 6/29):** `1aVIGSjhgzW6Eu95etE9MuubQEjoCXGm1Ucv4SqUJ8Vg`.

## Last session

- **2026-07-13** — Reconstructed the week (email/Slack/Drive; no repo commits since 6/29; no Progressive
  client call last week — the "last call" remains 6/23; the 6/29 "Progressive Design Kick-Off" was internal
  design, Candace + Kaitlin starting UX review of Tim's staging app). Built the Doug close-out package:
  1. **S&M Agreement draft** — `2026-07-13-support-maintenance-agreement-draft.md` + branded Google Doc
     (rs-pageless; retainer template unregistered in branded-gdoc). **$800 CAD + tax/mo, 5 hrs included,
     $160/hr overage, month-to-month from launch, Nov–Dec priority response. PRICE IS SPENCER'S CALL —
     sending the staged materials = approving it.**
  2. **Merchant workflow diagrams** — `2026-07-13-merchant-flow-diagrams.html` (overview + 6 patterns:
     CashStar URL+challenge, URL-only, PC URL+acct+PIN, code+PIN, Amazon claim-code→PDF, Walmart
     bidirectional activation). Print to PDF for Doug/Lloyd.
  3. **Answers to Doug's 8 questions** — in the response plan; three imply small yellow-highlight SOW
     edits (Q1 "first set" wording, Q4 inventory CSV export, Q7 support-request activity records).
  4. **Gmail draft to Doug** staged on thread `19e9a0905b082b87` (draft `r-2697339329393018958`), cc
     Stephanie + Lloyd — full answers, attachments to be added by Spencer (S&M PDF + diagrams PDF).
- **2026-06-29** — SOW v2 amendment built + sent to #am-pm-review; Stephanie sent to Doug same day.
  Transcripts ported; amendment plan written.

## In-flight work

- **Doug close-out package (this session's output)** — Spencer reviews → sends Slack draft to Stephanie →
  sends Gmail draft to Doug with PDFs attached.
- **Design track (parallel, internal):** Candace + Kaitlin doing UX review of Tim's staging build in Figma
  (Codex review packet); Spencer owed them fixed screenshots + design-system load. Not SOW-blocking.
- **Other worktree:** main repo checkout parked on `codex/giftcard-vault-design`.

## Punch list to signature

| # | Item | Owner | State |
|---|---|---|---|
| 1 | S&M price sign-off ($800/mo drafted) | **Spencer** | decision — approve or edit both the doc and the Gmail draft |
| 2 | Q6b posture: self-serve merchant config named as Phase 2 candidate | **Spencer** | drafted that way; confirm |
| 3 | Diagrams: review + export to PDF | Spencer | first pass built |
| 4 | 3 small SOW edits (yellow-highlighted) | Claude (gog docs) | **DONE 7/13** — applied to v2 in place (yellow = delta-from-v1 rule holds), verified via HTML export |
| 5 | Slack message to Stephanie in #am-pm-review | **SENT 7/13** (Spencer; Tim tagged to review) — implies $800/mo price approved | |
| 6 | Gmail draft to Doug + attach 2 PDFs | staged (Spencer attaches + sends) | |
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
- **Rate note:** executed Progressive SOW rate is **$160 CAD/hr** (D-13); `CLIENT.md` still says $150 — stale.

## Next steps

1. Spencer: approve S&M price + Q6b posture → send Slack draft (Stephanie) + Gmail draft (Doug, attach PDFs).
2. On Spencer's word: apply the 3 yellow-highlight SOW edits via gog docs.
3. After Doug's OK: Stephanie sends SOW + S&M through Dropbox Sign together.
4. Spencer + Tim: firm dates (post-signature is fine; SOW keeps 6–8 weeks + October-peak target).
5. Design track continues in parallel (not client-facing until SOW signed).

## Blockers

- None mechanical. Both remaining gates are Spencer decisions (#1, #2 in the punch list).

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
