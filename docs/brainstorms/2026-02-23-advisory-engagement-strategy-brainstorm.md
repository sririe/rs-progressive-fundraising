---
type: brainstorm
category: engagement-strategy
tags:
  - advisory
  - proposal
  - tiered-engagement
  - portal
  - operational-tooling
  - lloyd-deep-dive
  - build-vs-buy
key_decisions:
  - Platform adoption (Fundstream, Giftbit) is a non-starter — Progressive's 1-4% margin depends on direct vendor relationships
  - Three-tier engagement proposal gives Doug investment agency while anchoring toward comprehensive solutions
  - Assessment-first is industry best practice for non-technical clients asking for advisory guidance
  - White-label architecture remains deferred until contracts are secured
  - WordPress custom post types + magic link auth is the right portal MVP approach
key_insights:
  - Progressive is one of only 2 bulk resellers of Walmart gift cards in Canada — the direct vendor relationship IS the competitive moat
  - The delivery pain (encrypted emails) is the visible symptom but operational fragility (Lloyd bus factor) is the bigger strategic risk
  - Doug explicitly wants advisory, not just execution — the proposal should lead with strategic framing, not feature lists
  - Industry has moved to API-driven fulfillment — Progressive is one generation behind but building custom is the right call given their margin model
  - The Lloyd deep-dive is a prerequisite for scoping any operational work and hasn't happened yet
participants:
  red_stamp:
    - Spencer R. (brainstorm lead)
  progressive:
    - Doug B. (decision-maker, proposal recipient)
    - Gord S. (advisor, influences decisions)
related:
  - docs/discovery/2025-01-29-client-discovery-call.md
  - docs/discovery/2025-01-29-client-meeting-transcript.md
  - docs/discovery/2025-01-27-internal-pre-meeting.md
  - docs/solutions/2026-02-23-gift-card-fulfillment-technology-landscape.md
  - docs/solutions/2026-02-23-mvp-customer-portal-research.md
  - docs/solutions/2026-02-23-giftbit-platform-evaluation.md
status: complete
blockers:
  - Lloyd technical deep-dive has not occurred — required before Option 2/3 can be scoped with confidence
---

# Advisory Engagement Strategy: Three-Tier Proposal for Progressive

## What We're Building

A three-tier engagement proposal for Progressive Gift Cards that ranges from "solve the immediate pain" to "transform digital operations." The proposal gives Doug investment agency while steering toward the comprehensive approach the business actually needs.

This is a **client-facing advisory recommendation**, not an internal technical plan. It answers Doug's explicit question: "What should we do?"

## Why This Approach

### The Core Tension

Progressive has two problems masquerading as one:

1. **Delivery friction** (visible pain): Customers can't open encrypted email attachments, lose passwords, trigger corporate email filters. Doug feels this daily through support calls.

2. **Operational fragility** (strategic risk): Lloyd is the single point of failure for all digital card generation. Custom scripts on local machines, spreadsheet-based inventory, no documentation. If Lloyd is unavailable, digital fulfillment stops.

Doug asked for a portal (solving #1). Red Stamp's advisory role is to ensure he understands #2 and invests accordingly.

### Why Tiered

- **Budget-conscious client**: Progressive has historically been tight with budget but now understands the need to invest. A tiered proposal reduces the "sticker shock" of comprehensive work while making the case for it.
- **Decision agency**: Doug picks his level of investment. The act of choosing makes him more committed than a take-it-or-leave-it proposal.
- **Anchoring**: The three-tier structure naturally anchors toward the middle option, which includes the Lloyd deep-dive Red Stamp believes is critical.

### Why Not Platforms

We evaluated Fundstream (Montreal, 150+ Canadian brands, fulfillment API with white-label) and Giftbit (Victoria, 1,000+ brands, partnership program). Both are non-starters because:

- Progressive's entire margin (1-4%) comes from the wholesale-to-face-value spread on direct vendor relationships
- Progressive is one of only 2 bulk resellers of Walmart gift cards in Canada
- Any intermediary platform either eliminates the margin (pay face value) or compresses it unacceptably
- The competitive advantage IS the direct vendor relationship — outsourcing fulfillment undermines it

The right strategy is to strengthen Progressive's existing advantage by making fulfillment more efficient and delivery more professional, not to outsource it.

## The Three Options

### Option 1 — "Solve the Pain" (~4-6 weeks)

**What it is:** A customer portal MVP built on Progressive's existing WordPress site.

**What it includes:**
- Authenticated customer login with magic link authentication (no passwords to manage or lose)
- Order list showing fulfilled deliveries with status indicators
- Secure card retrieval via URL (replacing encrypted email attachments)
- Automated email notification when cards are ready for retrieval
- Lloyd/Mario continue to manually generate and upload cards to the portal

**What it solves:**
- Eliminates the #1 support burden (customers unable to open encrypted attachments)
- Provides customers with a self-service retrieval experience
- Gives Progressive a more professional digital delivery mechanism

**What it doesn't solve:**
- Lloyd remains the single point of failure for card generation
- No documentation or visibility into operational processes
- No scalability improvement for digital fulfillment volume
- No preparation for white-label opportunities

**Technical direction:** WordPress-native build using custom post types, content restriction, and passwordless authentication. Formidable Forms remains unchanged for order intake. Details to be scoped in the planning phase.

**Who it's for:** Progressive wants the quickest, most affordable win that addresses the most visible customer pain point.

### Option 2 — "Solve + Explore" (~8-10 weeks)

**What it is:** Everything in Option 1, plus a technical deep-dive into Lloyd's card generation workflow and a roadmap for operational improvements.

**What it includes (in addition to Option 1):**
- Technical deep-dive with Lloyd: walk through every card generation workflow, vendor by vendor
- Process documentation: step-by-step runbooks for Walmart, Amazon, Chapters, Loblaws generation
- Failure pattern catalog: what goes wrong, how often, what Lloyd does to fix it
- Decision architecture: why each vendor's process is different, what the quirks are
- Operational improvement roadmap: prioritized recommendations for automation, tooling, and risk reduction
- Assessment of Mario's readiness to take over documented processes

**What it solves:**
- Everything Option 1 solves (delivery friction)
- Reduces bus factor by documenting critical knowledge currently held only by Lloyd
- Produces a data-informed roadmap for Phase 2+ investment decisions
- Enables Red Stamp to scope operational tooling work with confidence (rather than guessing)
- Validates whether Mario can realistically serve as Lloyd's backup with better documentation

**What it doesn't solve:**
- Card generation is still manual (scripts are documented, not replaced)
- No automation of fulfillment workflow
- No white-label readiness

**Who it's for:** Progressive wants both the customer-facing win AND strategic visibility into their operational risk, with a clear plan for what to do next.

### Option 3 — "Transform" (~3-6 months, phased)

**What it is:** A comprehensive engagement that addresses delivery, operations, and growth readiness.

**What it includes (in addition to Options 1 & 2):**
- Internal fulfillment tool: a web-based application replacing Lloyd's local scripts, usable by any trained staff member
- Card generation workflow with error handling and audit trails (replacing manual script execution)
- Inventory tracking moved from Google Docs/spreadsheets into the fulfillment tool
- Ongoing advisory retainer: monthly strategic guidance, vendor evaluation, and process improvement oversight
- White-label readiness assessment: architecture review ensuring portal work doesn't block future white-label capabilities
- Vendor integration evaluation: which merchants are moving toward API access and what that means for Progressive

**Scope note:** Option 3 is intentionally broad at this stage. The Lloyd deep-dive in Option 2 is required to scope this option with confidence. Several line items above may shrink, grow, or change based on what the deep-dive reveals.

**What it solves:**
- Everything Options 1 and 2 solve
- Eliminates the Lloyd bus factor by making digital fulfillment operable by non-developers
- Scales digital fulfillment capacity (no more 3-hour Loblaws orders)
- Positions Progressive for white-label opportunities when/if contracts materialize
- Establishes Red Stamp as an ongoing technology partner (not a one-off vendor)

**Who it's for:** Progressive wants to invest seriously in modernizing their digital operations and sees this as a growth-enabling investment, not just a cost.

## Key Decisions Made

1. **Platforms are off the table.** Fundstream and Giftbit were evaluated and eliminated due to margin model incompatibility.

2. **Three-tier proposal structure.** Gives Doug investment agency, anchors toward the middle option, and makes the comprehensive approach feel less overwhelming.

3. **Portal is WordPress-native.** Custom post types + magic link auth on the existing site. No need for a separate application in Phase 1.

4. **Lloyd deep-dive is the critical enabler.** Without it, Options 2 and 3 can't be scoped with confidence. It's the single highest-leverage research activity.

5. **White-label is deferred but acknowledged.** Option 3 includes a readiness assessment so Progressive knows they're not creating technical debt, but no white-label features are built until contracts are secured.

6. **Assessment-first is the industry best practice** for this type of engagement, but wrapping it in a tier that also delivers tangible output (the portal) makes it more palatable to a budget-conscious client.

7. **No explicit recommendation yet.** Red Stamp will determine which option to steer Doug toward during the planning phase, once pricing, internal capacity, and proposal format are settled.

## Open Questions

1. **Pricing for each tier.** Red Stamp needs to estimate hours and set pricing. Research suggests: Option 1 at $8-15K, Option 2 at $15-25K, Option 3 at $40-80K+ (rough ranges based on industry benchmarks for similar agency work — to be refined by Red Stamp's actual rates and estimation).

2. **Option 2 billing structure.** Should the Lloyd deep-dive be billed as a separate line item (advisory) or bundled into the portal project cost? Separate billing makes the advisory value visible; bundling makes it a simpler decision for Doug.

3. **Option 3 phasing.** How does the 3-6 month timeline break into phases? Likely: portal build (month 1-2) → Lloyd deep-dive and documentation (month 2-3) → tooling build (month 3-5) → refinement and handoff (month 5-6). But this needs scoping after the deep-dive.

4. **The Lloyd conversation.** Before delivering this proposal, should Red Stamp have an informal conversation with Lloyd about his willingness to participate in a deep-dive? He's expressed interest in automation ("stop paying me to do something that could be automated") but his cooperation is essential.

5. **Proposal format.** How does Red Stamp typically present proposals to Progressive? PDF document? Live walkthrough? The research strongly recommends delivering the roadmap in a live session — walking through it interactively and getting verbal commitment on next steps.

6. **Amazon display time limits.** The "Front Street" constraint on Amazon card display was flagged in the discovery call but never resolved. This affects portal architecture for Amazon cards specifically.
