# Lane brief — design-qa-uat · recon · Codex

You are a **recon** lane under AUR2 Prime. Read
`/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-12-design-qa-uat/SHARED-CONTEXT.md`
first — it carries the canon, rulings, severity definitions, evidence discipline, and the recon
lane floor. All of it binds you.

## Your lens: Figma fidelity + P0-closure verification

You ran round 1 of this QA (2026-08-10, `DESIGN-QA-REPORT.md`) with reliable live Figma MCP.
Round 2 focus:

1. **Verify the two round-1 P0s are truly closed on staging:**
   - Walmart Card Preparation as an order workflow step between Paid and Allocated — compare the
     live staging flow against Figma Walmart Orders steps 1–4 (601:450, 601:823, 601:1196,
     601:1573). Check: step placement, step card layout, generate/download prep file affordance,
     Fiserv external-link treatment, activated-result import UI, loading/success states.
   - Semantic status pills — compare Dashboard/Orders/order-detail pills against Final Pills
     (421:1868) and `src/lib/format.ts`. Check label semantics AND the Kaitlin rule: max two
     state pills on an individual order header (one workflow + paid), not three.
2. **Verify each item on Kaitlin's 8/12 list** (quoted in SHARED-CONTEXT) — item by item, each one
   confirmed-fixed, partially-fixed (P1), or not-fixed (severity per definitions).
3. **Route-by-route fidelity diff** against the node table (Dashboard 564:1152, Orders 601:2640,
   order detail 601:123, Card Vault 601:3269): layout, spacing, tokens, table treatment. Apply the
   budget bias — high-frequency paths first; do not pixel-hunt secondary screens.

## Tools

- Figma: live Figma MCP (`get_screenshot`/`get_design_context` on the node IDs). Static fallbacks
  in `figma-frames/`.
- Staging: your proven browser tooling (gstack / operator Chrome profile session). Hard-refresh.
- Log in as `redstamp` unless a case needs a role check.

## Deliverable

`/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-12-design-qa-uat/findings-codex.md`
(structure per SHARED-CONTEXT §Deliverable). Screenshots under
`docs/runs/2026-08-12-design-qa-uat/screens-codex/`.
Sentinel when complete: `docs/runs/2026-08-12-design-qa-uat/design-qa-codex.done` (one line: the
findings path). Blocked: `design-qa-codex.blocked` per the lane floor.

Start with the staging freshness gate, then work your lens. Start now.
