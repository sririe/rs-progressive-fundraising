# Status — rs-progressive-fundraising

> Session-start: read this file first. Session-end: update it following this section structure
> (full procedure: the Aurora `wrapup` skill, where installed).

## Current focus

Phase 1 (Secure Card Vault) — **the Phase 1 SOW amendment (v2) is built and in PM review.** Coming out of
the **2026-06-23 "Digital Fulfillment Sync"** call with Doug + Lloyd (Tim + Stephanie on the Redstamp side),
we amended the May 29 SOW to reflect the validated normalization model. v2 is a **copy** of the signed-format
SOW with **every change highlighted in yellow** (Doug's explicit request); v1 is preserved. It's staged in
**#am-pm-review** for Stephanie's PM Approval → Dropbox Sign → Doug. The Doug delivery email is drafted and
waits on approval.

- **v2 SOW (Google Doc):** `1aVIGSjhgzW6Eu95etE9MuubQEjoCXGm1Ucv4SqUJ8Vg` — Redstamp Clients [Internal] →
  Progiftcards.ca → _Client Level Agreements. v1: `1CIugJL3zGlP_ORJX9iEBt0JXTh_WUaeW2H-9WTDWxQE`.
- **Amendment plan (what/why/how + exact edits):** `projects/gift-cards/docs/plans/2026-06-29-sow-amendment-plan.md`.

## Last session

- **2026-06-29** — Processed the 6/23 Digital Fulfillment Sync: ported transcript + notes to
  `docs/discovery/2026-06-23-digital-fulfillment-sync-{transcript,notes}.md` (attendee roster +
  diarization/provenance frontmatter). Built the **v2 SOW amendment** via `gog docs` (copy → surgical
  find-replace/insert → `--bg-color #FFFF00` highlights) — 10 highlighted changes: normalization /
  canonical-record model, Walmart **on-demand** activation (corrected from "store inactive then activate"),
  credential patterns, **Render** hosting (app + DB; ~USD $25/mo Pro + compute + ~$6/mo DB, loose),
  System Bind naming fix, Phase 1A milestone rename, **Support & Maintenance** framing for new-merchant
  additions (not change orders), Support Agreement reference. Wrote the amendment plan; captured gog
  doc-editing gotchas (`docs/solutions/workflow-issues/gog-docs-amendment-edits-System-20260629.md`).
  Staged the #am-pm-review Slack draft for Stephanie; drafted the Doug delivery email (unsent).
- **2026-06-23** — Decision board + normalization design note re-grounded from Doug's 6/16 email; PRs #6–#9.
  This 6/23 work + the 6/23 client call are the inputs the amendment is built on.
- **2026-06-18** — Renderer spike (svg2pdf) + vault normalization design note + interactive decision artifact.

## In-flight work

- **SOW v2 in PM review** — staged Slack draft in **#am-pm-review** (channel `CDXL51RFS`), tagged Stephanie
  Lamon (`UHEG5DDMW`); **draft not yet sent** (Spencer sends). Flow: send → 👀 → PM Approval form →
  Stephanie sends via **Dropbox Sign** → Doug. Stephanie already gave one review note (add approx. Render
  cost) — incorporated.
- **Doug delivery email** — drafted in-conversation, **not yet created as a Gmail draft**; push after the SOW
  clears review. Replies on thread `19e9a0905b082b87` ("RE: Reschedule Needed-Phase 1 Proposal"). Doug
  nudged 2026-06-27 asking for timing.
- **2nd-pass SOW details** deliberately left under the normalization umbrella (Doug: "don't sweat every
  question"): import-mapping UI bullet, invalid-card workflow, four role types, training-package detail.
- **Other worktree:** main repo checked out on `codex/giftcard-vault-design` (at origin/main SHA; no
  unpushed commits observed).

## Repo state

- This session's docs land via a **docs-only PR** from `claude/sweet-lumiere-6058d1`: the two ported 6/23
  transcripts, `2026-06-29-sow-amendment-plan.md`, the new `gog-docs-amendment-edits` solution, and this
  status update.
- No unpushed code; sibling worktree clean at origin/main.

## Runtime & environment

- **App codebase (cross-repo):** `~/projects-work/progressive-card-vault/app` — Next.js / Node 22 + Prisma +
  Postgres (Tim's build). Deploy config: `app/render.yaml` (Render web service + Postgres). Staging runs on
  Render's **free** tier — **internal only: Progressive does not know staging exists (built pre-signature);
  keep it out of all client comms.** Production = Render Pro (~USD $25/mo + compute) + Postgres (~$6/mo).
- **gog (Google Workspace CLI):** `~/.local/bin/gog` v0.31.1 (source build, ahead of brew `gogcli`).
  Docs/Drive writes work via the DWD **service account** for spencer@redstamp.com (no reauth; ignore the
  `auth list --check` "invalid" red herring). **Gmail is NOT in the SA scope** (401) — use the Gmail MCP for
  mail. `docs copy/find-replace/insert/format` are blocked under `gog-agent-safe`; use stock
  `gog --enable-commands docs.<cmd>` for authorized edits. Full recipe + traps:
  `docs/solutions/workflow-issues/gog-docs-amendment-edits-System-20260629.md`.
- **Second-brain inbox:** `~/projects-personal/second-brain/Incoming/` — the two 6/23 captures live there
  with enriched frontmatter; now redundant with the repo copies (Spencer's call whether to prune).
- No required local services for this repo.

## Next steps

1. **Send the #am-pm-review draft** (Spencer) → Stephanie's PM Approval → Dropbox Sign to Doug.
2. **After approval:** push the Doug delivery email as a Gmail draft (reply on thread `19e9a0905b082b87`).
3. **Timeline:** Spencer + Tim sync (Tim out the week of 6/30) to set firm dates; SOW keeps 6–8 weeks +
   "ahead of the October peak."
4. **Merchant-flow diagrams** (5–6 common merchants: source → vault → output) — deferred companion Lloyd
   asked for; build after the SOW.
5. **D-15 export-password mechanism** (Spencer + Tim) still unsolved long-term; V1 leaves export protection
   with System Bind.

## Blockers

- None blocking the SOW. (D-15 export-password is deferred, not blocking V1.)

## Decisions & context

- **2026-06-29 SOW amendment decisions:** deliverable = yellow-highlighted modified SOW only (Doug dropped
  the Q&A companion); copy v1 → v2, v1 preserved; D-15 deferred (System Bind keeps export protection for
  V1); timeline 6–8 wks + October-peak target, dates post-Tim-sync; roles named as types not individuals
  (and deferred to 2nd pass); Render named as hosting with loose approximate cost (per Stephanie);
  **new-merchant additions that fit an existing credential pattern = Support & Maintenance work + an
  end-to-end validation pass, NOT a change order; only a genuinely new credential type is a change order.**
- **branded-gdoc runs on gog;** for an *amendment* (vs. fresh template fill) the working method is gog docs
  surgical edits on a copy + `--bg-color` highlighting (recipe in the solutions doc above).
- **6/23 call:** Doug + Lloyd endorsed the normalization model; Walmart confirmed on-demand (no pre-stored
  inventory); System Bind stays for V1 (post-V1 consolidation possible).
- **Speaker attribution (6/23 transcript):** Supernormal verified only "You" (Spencer); Speaker 3 = Doug,
  Speaker 4 = Lloyd inferred from content; Speaker 1/2 = Tim/Stephanie unresolved.
- Prior: SOW reconciliation `projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md`;
  normalization design note `projects/gift-cards/docs/plans/2026-06-18-phase1-vault-normalization-design-note.md`.
- House rule: read CLIENT.md + REDSTAMP-SOW-CONTEXT.md before client-facing artifacts.
