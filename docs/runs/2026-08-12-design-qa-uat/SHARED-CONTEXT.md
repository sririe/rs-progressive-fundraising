# Shared context — Design QA round 2 (pre-UAT), 2026-08-12

Three parallel recon lanes (Codex, Claude, Grok) run design QA of the Progressive Card Vault
staging app against Figma, hunting **P0/P1 blockers for client UAT**. Each lane has its own
brief (`brief-<fuel>.md`) and lens; this file is the common canon. Read this first, then your brief.

## Where the project is (2026-08-12)

- **Round 1 (2026-08-10/11):** agentic design QA produced
  `docs/runs/2026-08-10-design-dev-reconcile/DESIGN-QA-REPORT.md` (adversarial-gate PASS) and
  `PRIORITIZED-BACKLOG-v2.md`. Two P0s identified: (1) Walmart preparation as an order workflow
  step, (2) semantic order-status pill labels. Designer checkpoint went to Kaitlin.
- **Kaitlin's answers (Slack #progressive-fundraising, ts 1786549230.749719, 2026-08-12 08:40 PDT),**
  quoted:
  - Walmart step: "Yes I think we should have Walmart step in the list between paid and allocated"
  - Status pills: "They should match the Steps and language on the order screen … on the individual
    orders screen there are current two 'Inprogress' pills, I think we should only need one along
    with the paid state (2 total, not 3)"
  - "Users" and "Integrations" pages "still feature the old look … at least make sure the colours
    (buttons/pills) match the styling we've applied throughout"
  - Charts: "any dates on the charts follow a date formatting of '00.00.00' to save on space when
    it's tight"
  - Tables: "General grey hover highlight on tables, ensure this extends the full width of the
    white not just to the end of the text" (Figma node 640-64)
  - Individual orders page: "Under Client information, we don't need the client name clickable
    because we have a link right above"; "Under Cards Ordered, the table lines don't need to
    highlight; it makes them feel clickable and they aren't"
- **Tim's update (Slack ts 1786561876.379329 + 1786562051.663229, 2026-08-12 ~12:11 PDT):** claims
  all of the above addressed and deployed: Walmart Card Preparation step between Paid and
  Allocated (generate/download Fiserv prep file, external Fiserv URL, activated-result CSV
  upload/paste import), status pill language cleanup, Users/Integrations styling pass, full-width
  hovers, `00.00.00` tight dates, de-duplicated In Progress pills, non-clickable informational
  rows. His own QA + security reports are green
  (app repo `_testing-reports/qa-reports/2026-08-12-current-state/QA_REPORT.md`).
- **Your job is round 2:** independently verify Tim's claims against Figma and staging, and find
  anything remaining that would embarrass us in the client UAT walkthrough. Kaitlin does a human
  pass after you; the client walkthrough follows.

## Sources of truth

- **Figma:** https://www.figma.com/design/Ztv1YtEx1S19i0w4bdHgo4/Digital-Gift-Card-Fulfillment-Design
  Current-design nodes (verified in round 1 — use these, NOT the "Design Direction" historical page):
  | Surface | Node |
  | --- | --- |
  | Dashboard | 564:1152 |
  | Orders list | 601:2640 |
  | Non-Walmart order detail | 601:123 |
  | Walmart order steps 1–4 | 601:450, 601:823, 601:1196, 601:1573 |
  | Card Vault | 601:3269 |
  | Final Pills | 421:1868 |
  | All-screens page | 294:12978 |
  Static PNG exports of these nodes (if present): `figma-frames/` in this run directory, with
  `INDEX.md`. If the directory is missing/empty, say so in your findings — do not guess at designs.
- **Staging:** https://progressive-gift-cards-card-vault-staging.onrender.com/
  Internal-only (NEVER mention to the client). Fake, disposable test data. Seeded users:
  `redstamp` (admin), `elaine` (operations), `mario` (finance) — password is the agreed
  seed/staging password (operator's Chrome on this Mac has a logged-in session; browser tooling
  that reuses that profile inherits it). Hard-refresh before judging any screen.
- **App code:** `/Users/spencer/projects-work/progressive-card-vault/app` @ `08c0c74` (read-only
  for you). Style guide: `docs/application-style-guide.md`. Status pills: `src/lib/format.ts`.
- **Test package:** app repo `_testing-packages/2026-08-12/` — README, TEST_CASES.md,
  RESET_NOTES.md, sample import files, `PGC-1027-walmart-activated-result-120-valid.csv`.

## Staging freshness gate (do this first)

Before filing any finding: confirm staging is running Tim's 2026-08-12 build — a Walmart order's
workflow must show a **Card Preparation step between Paid and Allocated**. If it does not, staging
is stale: record that in your findings, write your `.blocked` sidecar, and stop rather than QA-ing
an old deploy.

## Settled rulings — do not re-open

1. Walmart prep is an order workflow step; Fiserv activation stays OUTSIDE the app (external URL).
2. Sequential workflow gating is intentional: future steps greyed out, export-before-delivery,
   delivery-before-close. Not a defect.
3. Status pills: semantic labels matching order-screen workflow language; green paid token is
   correct (the old "Paid is blue" diagnosis was false).
4. Where Figma is visual-only and the app enforces business rules underneath, behavior wins —
   flag mismatches as "question for Tim/Kaitlin", not defects.
5. Budget bias: operator clarity on high-frequency paths beats pixel-perfection on secondary
   admin screens.

## Severity definitions (calibrate hard — the deliverable is P0/P1, not volume)

- **P0 — UAT blocker:** would derail or embarrass the client walkthrough on a core path.
  Broken/dead-end flow, error states on normal actions, misleading status language, data that
  looks wrong, layout broken at laptop width (~1280–1440), the Walmart prep flow failing, or a
  design promise Kaitlin/Tim explicitly committed to (list above) visibly unmet.
- **P1 — fix before UAT if at all possible:** client would notice; undermines polish/trust on
  high-frequency paths (Dashboard, Orders, order detail, Card Vault, Walmart prep). Includes the
  Kaitlin-list items if only partially done.
- **P2/P3 — note-only:** secondary screens, minor spacing/wording. List briefly at the end; do
  not pad the report with these.

## Evidence discipline (Collective Contract)

- Every P0/P1 finding: **route + what you observed (screenshot path if you captured one) +
  Figma node ref for fidelity claims + one-line severity rationale.**
- Never fabricate or extrapolate a finding. State provenance: live-inspected vs inferred from code.
- Degraded paths declared loudly: if you can't auth, can't reach Figma, can't screenshot — say
  exactly what failed and what your coverage actually was. A smaller honest report beats a padded one.
- Fake data only (fake names/emails); no real card numbers/PINs. Avoid destructive ops: no user
  deactivation beyond the test package's designated cases, no DB reset. If exercising the order
  lifecycle, use the test package's fresh-order QA helper / designated fixtures (see its README),
  not existing seeded orders another lane may be inspecting.

## Recon lane floor (replaces the builder PR floor — read-only recon, no branch/no PR)

1. Read-only recon: no commits, no pushes, no branches, no PRs, no product-code edits.
2. Your only writes: your findings file, screenshots under this run directory, and your sentinel.
3. Write sentinel `design-qa-<fuel>.done` (in this run directory) containing one line with your
   findings file path, ONLY after the findings file is complete.
4. If blocked: write `design-qa-<fuel>.blocked` with the exact command, exact error, and attempts,
   then stop. Do not grind silently on a fallback the dispatcher could unblock in seconds.
5. No Slack, no BugHerd, no email, no client contact, no external publication of any kind.
6. A false "done" or invented finding benches the fuel (COLLECTIVE-CONTRACT).

## Deliverable structure (your findings file)

1. **Method & coverage** — auth state, staging build check result, routes inspected, Figma nodes
   inspected (live vs static export), tools used, anything you could NOT cover.
2. **P0 table** — id | route | finding | evidence | Figma ref | why P0.
3. **P1 table** — same columns.
4. **Verified-fixed list** — Tim's 8/12 claims you confirmed (so nobody re-litigates them).
5. **Questions for Tim/Kaitlin** — ambiguities, visual-vs-functional judgment calls.
6. **P2/P3 one-liners** (optional, brief).
