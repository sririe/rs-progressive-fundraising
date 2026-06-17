# Status — rs-progressive-fundraising

> Session-start: read this file first. Session-end: update it following this section structure
> (full procedure: the Aurora `wrapup` skill, where installed).

## Current focus

Phase 1 (Secure Card Vault) — **the ball is back in our court (barely).** Doug replied on **2026-06-16**
with two emails: (1) an inline, color-coded markup of Spencer's June 11 answers by his team, and (2) a
materials forward. Doug gave most of the confirmations we asked for, and his proposed next step is a
**call (Lloyd + Doug + Redstamp), then Stephanie adds clarifying language to the SOW + ongoing-support
options, then finalize.** Spencer's read: the call resolves most open items; nothing they shared is
concerning; the SOW language mainly protects us against materials we hadn't received. **Gating item:
`redstamp.zip` (Lloyd's software bundle) is shared via Drive but not yet accessible to us — Spencer
requested access 6/16.** Once it lands, inventory it, then answer the open client questions. Nothing goes
to the client without Spencer's sign-off.

## Last session

- **2026-06-16** — Processed Doug's reply. Decoded the color-coded annotated Q&A email (the meaning lives
  in font color, lost in plaintext): **uncolored = Spencer's June 11 answers; blue+green = Lloyd (operator);
  black = James (outside technical counsel); red = Doug (decisions)** — legend per Doug, confirmed by
  Spencer. Wrote `projects/gift-cards/docs/discovery/2026-06-16-phase1-annotated-qa-thread.md` (decoded
  thread + decisions + open questions). Inventoried the Walmart May reconciliation spreadsheet into the
  git-ignored private folder. `redstamp.zip` blocked on Drive access. No client message sent by the agent;
  Spencer himself replied to Doug confirming receipt + requesting zip access.
- **2026-06-10** — Full reconciliation-to-send arc: reconciled Doug's 12 questions × Tim's Proof draft ×
  evidence; Spencer ratified via Proof (16 comments, added D-15); wrote + hand-tightened the client
  responses doc and **sent it to Doug** (logged verbatim); branch/worktree hygiene sweep.
- **2026-06-08** — Evidence inventory + unblocker brief (Phase 1 stands; bounded merchant formats;
  validation milestone first; missing fixture package identified as THE unblocker).

## In-flight work

- **Canonical thread:** Gmail "RE: Reschedule Needed-Phase 1 Proposal" (thread `19e9a0905b082b87`). Doug's
  2026-06-16 reply is message `19e9a0905b082b87` @ 22:29:12; the materials forward is a separate message
  (`19ed28dcc32c5621`) @ 22:29:26.
- **Decisions Doug locked 2026-06-16:** Roles — Admin = Doug + Elena; Operations = New Hire (TBA), Lisa,
  Lloyd. Training/acceptance group = Doug, New Hire, Lisa, Lloyd (Elena later). Active offerings —
  MasterCard yes; Browns Social House no; Hudson's Bay no; Uber not now (maybe future). In-house
  card-generation merchants = Amazon, Walmart, Chapters-Indigo (Lloyd). Old "Progressive"-branded Loblaws
  inventory nearly depleted; stragglers converted before vault. Manual Walmart import acceptable for v1 =
  "still to be discussed."
- **⚠️ Scope item to reconcile:** Lloyd says ANY brand can be delivered as a URL (password-protected Excel)
  OR PDFs-in-ZIP — this **contradicts the earlier D-3 verdict ("Amazon PDF/ZIP only")**. Lloyd + James both
  point toward a **configurable generic importer** (pass-through merchants need no software change) as the
  Phase 1 backbone. Settle on the call and in Stephanie's SOW clarifying language. (Spencer: not concerned;
  validation-step framing absorbs it as scheduled work, not an open promise.)
- **Open questions directed at us** (answer on the call / in SOW): (1) Doug — stray old "Progressive"-branded
  card handling if missed; (2) Lloyd — vault/app hosting (security + backup); (3) Lloyd — define "banner
  brand"; (4) Lloyd — reconcile our "SystemOne" vs his "SystemBind" for the URL upload system.
- **Decision state (prior):** D-1/D-2/D-4–D-12/T-1 ratified; **D-15** (per-export password model) sent as
  proposed — note Lloyd flagged it changes the customer notification practice (currently one shared
  password); **still open for SOW revision: D-13 (rate $160 vs $150) and D-14 (payment schedule).**
- **Proof docs:** Tim's Q&A doc (`26niwbyj`) **superseded** without his review — loop him in. Spencer's
  reconciliation review copy: `f7n13d69` (creds in `_private/proof-reconciliation-doc.json`, git-ignored).
- **National Zakat Foundation call:** Spencer agreed June 8 to join; still needs scheduling (Stephanie to
  send times). Qualifying questions (order scale, recipients, target dates) remain unasked — ask on/before
  the call. Background: Doug's April 20 "Fwd: Touching Base" (thread `19dab86ecc934f1f`).
- No open PRs or tracker issues (repo has no tracker).

## Repo state

- This session committed `2026-06-16-phase1-annotated-qa-thread.md` + this status update on
  `claude/zealous-elbakyan-b4d035` and **landed them on `main`** (fast-forward).
- Sibling worktrees all clean and 0 commits unmerged vs `origin/main`:
  `claude/intelligent-wiles-aa1563`, `claude/romantic-meitner-551fbc`, `claude/xenodochial-wilson`.
- **Hygiene still open (provably merged, removable on Spencer's confirmation):** the
  `claude/xenodochial-wilson` worktree + branch (at f30d6e7, an ancestor of main) is still present; the
  2026-06-10 doc also flagged `claude/eloquent-fermi` and `sririe/progressive-lloyd-meeting` (+ remote).
- Prior next-step "strip legacy Proof spans from CLIENT.md" is **done** (commit 6fc4eab).
- Main checkout has pre-existing untracked presentation artifacts (`.claude/launch.json`, the client
  presentation HTML, the Phase 1 walkthrough PDF) — commit or ignore at Spencer's discretion.

## Runtime & environment

- **Materials are local-only by design (git-ignored, cash-equivalent-adjacent).** A cold agent on another
  host will NOT have them:
  - `projects/gift-cards/_private/lloyd-materials-06162026/` — `WM Ecards - May2026.xlsx` (Walmart May
    reconciliation; financial only, no card data) + `notes/SOURCE-INVENTORY.md` (this session's inventory).
    Folder naming differs from the `lloyd-materials/2026-06-08/` convention; harmless.
  - `projects/gift-cards/_private/lloyd-materials/2026-06-08/` — three recovered Lloyd scripts/workbook.
  - **`redstamp.zip` NOT yet received** — Lloyd's Drive link won't grant a `@redstamp.com` account access
    (likely Workspace external-sharing restriction). Spencer requested access 6/16. Lloyd deliberately
    WITHHELD the Walmart activation program ("unsure why they need that"); sample I/O said to be in the zip.
- **gog CLI (Google Workspace):** authed as spencer@redstamp.com with **docs + drive scopes only — NO
  gmail scope.** Can reach Drive but could not 404-resolve Lloyd's link-shared zip. **Gmail MCP** reads
  threads but has **no attachment-download tool** — neither path can pull the zip or the xlsx; both files
  came/come via Spencer's browser.
- No services, env vars, or migrations otherwise.

## Next steps

1. **When `redstamp.zip` arrives:** expand into `_private/lloyd-materials-06162026/raw/*`, inventory
   against request items 1–4, 6, 7 (and the sample-I/O part of 5), flag remaining gaps. Spencer then
   answers the four open client questions. (Spencer is doing the inventory hand-off with the agent.)
2. **The call (Doug's proposed next step):** Lloyd + Doug + Redstamp. Resolve operational choices, the
   D-3 export-format/generic-importer question, "banner brand" definition, SystemOne/SystemBind, hosting,
   and the old-inventory edge case.
3. **SOW revision with Stephanie:** clarifying language per the call + the 14 deltas (section D of the
   reconciliation doc) applied to `2026-05-27-progressive-secure-card-vault-sow-draft.md`. Resolve D-13
   (rate $160 vs $150 — update CLIENT.md to match) and D-14 (payment schedule).
4. **Support proposal** (options + pricing) to accompany the updated SOW (promised in the Q10 answer).
5. **Loop Tim in** on the final reconciled positions (his Proof doc `26niwbyj` superseded without review).
6. **NZF call** scheduling (Stephanie to send times); ask qualifying questions on/before it.
7. **Roadmap:** Doug's ongoing Walmart direct-integration talks remain unscoped/unpriced — future phase.
8. **Hygiene (on Spencer's confirmation):** remove `claude/xenodochial-wilson` worktree+branch,
   `claude/eloquent-fermi`, `sririe/progressive-lloyd-meeting` (+ remote) — re-verify merged at delete time.

## Blockers

- **`redstamp.zip` access** — gates the technical validation/inventory and final SOW scope confidence.
  Spencer requested access from Doug/Lloyd 2026-06-16.
- Walmart activation program deliberately withheld by Lloyd — follow up if Phase 1 needs it.
- Internal D-13/D-14 are decisions, not blockers — resolve at SOW revision.

## Decisions & context

- Decoded 2026-06-16 thread + decisions + open questions:
  `projects/gift-cards/docs/discovery/2026-06-16-phase1-annotated-qa-thread.md`.
- Private materials inventory: `_private/lloyd-materials-06162026/notes/SOURCE-INVENTORY.md` (local-only)
  and `projects/gift-cards/docs/discovery/2026-06-08-private-lloyd-materials-inventory.md`.
- Reconciliation verdicts/divergences: `projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md`.
- Author legend for Doug's annotated emails: uncolored = Spencer; blue+green = Lloyd; black = James
  (outside technical counsel); red = Doug. Parse the HTML body — plaintext loses the color attribution.
- Doug's June 5 sales mix: 55% Walmart / 22% Loblaws / 13% Amazon / 10% other; ~60% of sales Nov–Dec.
- House rule: read CLIENT.md + REDSTAMP-SOW-CONTEXT.md before client-facing artifacts (CLAUDE.md/AGENTS.md).
