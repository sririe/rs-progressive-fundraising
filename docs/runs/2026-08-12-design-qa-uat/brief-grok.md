# Lane brief — design-qa-uat · recon · Grok

You are a **recon** lane under AUR2 Prime. Read
`/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-12-design-qa-uat/SHARED-CONTEXT.md`
first — it carries the canon, rulings, severity definitions, evidence discipline, and the recon
lane floor. All of it binds you.

## Your lens: UAT walkthrough realism

Play the client walkthrough before the client does. Progressive's stated goal: "digital
fulfillment should not depend on one technically skilled employee" — an ordinary office person
must be able to fulfill orders. You are that person. Sibling lanes cover pixel fidelity and
interaction states; you hunt **workflow traps, confusing language, and dead ends** on the paths
the walkthrough will actually take.

1. **Core lifecycle, end to end** (use the test package's fresh-order QA helper — see app repo
   `_testing-packages/2026-08-12/README.md` + `TEST_CASES.md`; do NOT consume seeded orders other
   lanes may be inspecting): order → payment marked paid → allocate → export → download →
   record delivery → close. At every step ask: would a non-technical user know what to do next?
   Is any state name, empty state, or error message confusing or alarming? Does anything dead-end?
2. **Walmart path** (the new build — highest walkthrough risk): Walmart order → Card Preparation
   step between Paid and Allocated → generate/download prep file → (Fiserv is external — link
   only, do not attempt to transact) → import
   `_testing-packages/2026-08-12/sample-files/PGC-1027-walmart-activated-result-120-valid.csv`
   (or paste flow) → continue to allocation. Compare the experience against the design intent in
   `figma-frames/walmart-order-step{1..4}-*.png`. Failures, unclear instructions, or wrong counts
   here are P0.
3. **Language pass** — status pills, step names, buttons, banners across the core path: does the
   language match what the screen is actually doing (Tim's semantic-labels claim)? Flag anything
   generic, contradictory, or internal-jargon.
4. **Walkthrough hazards** — anything on screen we would not want Progressive to see: obviously
   fake/broken-looking data, debug artifacts, dev-only affordances, the hidden testing
   instructions page reachable from normal nav, error toasts on normal actions.

## Tools

- Design canon: static Figma exports in
  `docs/runs/2026-08-12-design-qa-uat/figma-frames/` (INDEX.md maps files to nodes). You have no
  live Figma access — say so in Method; do not guess beyond the exports.
- Staging: browser automation via the gstack skill at `~/.claude/skills/gstack` (see its
  BROWSER.md / browse/ subsystem; it reuses the operator's logged-in Chrome profile session).
  Hard-refresh first. If browser automation is not workable after ~15 minutes of honest attempts,
  write `design-qa-grok.blocked` with the exact command + error and stop — do NOT fall back to
  code-only guessing presented as visual QA.
- Log in as `redstamp`; use `elaine` (operations) for one repeat of the core lifecycle if time
  allows — she is the realistic UAT persona.
- Fake data only; no destructive ops beyond the test package's designated cases; never touch
  anything outside staging.

## Deliverable

`/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-12-design-qa-uat/findings-grok.md`
(structure per SHARED-CONTEXT §Deliverable). Screenshots under
`docs/runs/2026-08-12-design-qa-uat/screens-grok/`.
Sentinel when complete: `docs/runs/2026-08-12-design-qa-uat/design-qa-grok.done` (one line: the
findings path). Blocked: `design-qa-grok.blocked` per the lane floor.

Start with the staging freshness gate, then work your lens. Start now.
