# Lane brief — design-qa-uat · recon · Claude

You are a **recon** lane under AUR2 Prime. Read
`/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-12-design-qa-uat/SHARED-CONTEXT.md`
first — it carries the canon, rulings, severity definitions, evidence discipline, and the recon
lane floor. All of it binds you.

## Your lens: interaction states, consistency, and responsive behavior

A sibling lane covers static Figma fidelity. You cover everything that only shows up when you
*use* the app:

1. **Interaction states** across Dashboard, Orders (list + filter drawer), order detail, Card
   Vault, Exports: hover (full-width table row hover — Kaitlin's rule, Figma 640-64), focus,
   active, disabled, empty states, loading states, error states. Search inputs + clear buttons +
   as-you-type filtering. Informational rows must NOT hover as clickable (Cards Ordered table).
2. **Design-system consistency** — one app, one system: pill colors/shapes (Final Pills 421:1868),
   button variants, card shadows, date formats (tight tables `00.00.00`; charts rule from
   Kaitlin's list), typography scale. Special eye on **Users** and **Integrations**: Kaitlin
   flagged them as old-look; Tim claims a lighter alignment pass. Judge: aligned enough for a
   client walkthrough, or still jarring (severity per definitions)?
3. **Responsive/laptop behavior** — ~1280 and ~1440 widths: collapsed sidebar usability, table
   overflow (Clients table phone/email columns), filter drawer, chart legibility.
4. **State-machine coherence on order detail** — walk one order's states and check every
   simultaneous signal (pills, step list, buttons, banners) tells one consistent story. Max two
   state pills on the header (Kaitlin's rule). Greyed future steps are intentional gating, not
   defects.
5. **Console/a11y spot check** — Tim's QA notes hydration noise on order detail; note anything
   user-visible it causes. Quick keyboard-nav/contrast pass on the core path only.

## Tools

- Staging: claude-in-chrome against the operator's logged-in Chrome (create a NEW tab; call
  tabs_context first), or gstack (`~/.claude/skills/gstack`). Hard-refresh. Log in as `redstamp`
  unless a case needs a role check.
- Figma: claude.ai Figma MCP on the node IDs; static exports in `figma-frames/` as fallback.

## Deliverable

`/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-12-design-qa-uat/findings-claude.md`
(structure per SHARED-CONTEXT §Deliverable). Screenshots under
`docs/runs/2026-08-12-design-qa-uat/screens-claude/`.
Sentinel when complete: `docs/runs/2026-08-12-design-qa-uat/design-qa-claude.done` (one line: the
findings path). Blocked: `design-qa-claude.blocked` per the lane floor.

Start with the staging freshness gate, then work your lens. Start now.
