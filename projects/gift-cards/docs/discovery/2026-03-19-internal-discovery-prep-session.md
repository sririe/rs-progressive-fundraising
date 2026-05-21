---
title: "Internal Discovery Prep Session"
type: discovery
category: internal-discussion
date: 2026-03-19
status: complete
participants:
  redstamp:
    - Spencer R.
    - Danny N.
    - Tim L.
    - Bronte B.
    - Stephanie L.
tags:
  - internal-sync
  - discovery-prep
  - digital-fulfillment
  - scope-management
  - session-planning
  - task-breakdown
key_decisions:
  - Keep the upcoming on-site discovery session anchored on digital gift card fulfillment, while capturing stickering and invoicing as lighter adjacent inputs
  - Run the session as a guided walkthrough with a live checklist rather than a rigid workshop format
  - Record the walkthrough if Progressive is comfortable, using either Google Meet or Loom, so the team can revisit vendor-specific steps afterward
  - Prepare a print-friendly client-facing session artifact and a separate internal task breakdown before scheduling is finalized
  - Use the discovery session to document acquisition, generation, storage, activation, and distribution workflows without assuming a future architecture too early
key_insights:
  - The team needs a vendor-by-vendor map that separates where digital cards are sourced from how Progressive fulfills them to customers
  - Existing PDF/card-generation scripts may be one of the most brittle parts of the workflow and may not be worth preserving in a future-state recommendation
  - Copies or examples of the real tools, spreadsheets, scripts, portals, and outputs will be essential for building a credible technical recommendation after the session
  - Mario may now be operating the workflow, but the real test is what still requires Lloyd's judgment or undocumented knowledge
  - A quick export from Formidable suggested digital orders are roughly 10 percent of total order count, but that needs cleanup and validation before it is reused externally
related:
  - projects/gift-cards/docs/plans/2026-03-17-post-meeting-action-plan.md
  - projects/gift-cards/docs/plans/2026-03-17-client-follow-up-email-draft.md
  - projects/gift-cards/docs/plans/2026-03-19-internal-sync-agenda-and-discovery-session-plan.md
  - projects/gift-cards/docs/discovery/2026-03-13-website-recommendations-meeting-transcript.md
blockers:
  - The on-site date is not yet confirmed
  - Progressive still needs to confirm who will attend from their side
  - The team does not yet have validated prework on active digital vendors, fulfillment sources, or sample artifacts
---

# Internal Discovery Prep Session

## Context

This internal discussion reviewed the prep document for the next Progressive session and focused on what Red Stamp needs to have ready before the on-site discovery work is scheduled.

The conversation reaffirmed that the session should stay tightly focused on the digital gift card workflow, even though Progressive also surfaced stickering and invoicing pain points during the March 13 client call.

## What The Team Agreed The Session Must Uncover

### 1. The actual digital workflow today

- How digital card data is acquired for each vendor
- What happens when inventory is received, stored, and prepared for fulfillment
- What Lloyd and Mario do step by step for each major vendor flow
- Which tools, scripts, spreadsheets, portals, or manual workarounds are involved
- Where the workflow is slow, brittle, error-prone, or dependent on operator judgment

### 2. Where sensitive data lives and moves

- Where card data exists at each stage
- Who can access it
- How it is transferred or stored today
- Whether activation is part of the digital workflow, the physical workflow, or both
- What protections exist today around files, URLs, and customer delivery

### 3. How transferable the workflow really is

- What Mario can do independently today
- What still lives mostly in Lloyd's head
- What a non-technical operator would still struggle to take over
- Which parts could be documented immediately in a runbook even before new tooling exists

### 4. What Progressive actually needs on the delivery side

- Whether end-recipient distribution is a near-term operational need or still more of an attractive idea
- Which delivery expectations are real versus sales-claim assumptions
- Whether certain customers or vendors are being handled differently today

### 5. Adjacent operational pain points

- High-level understanding of physical-card stickering
- High-level understanding of invoicing and QuickBooks friction
- Enough context to prioritize whether either one should come after digital fulfillment work

## Important Framing From The Discussion

### Do not over-architect before seeing the workflow

The team explicitly did not want to anchor the discovery around direct vendor integrations or a future customer delivery platform before seeing what Progressive actually does today.

That was especially important because:

- vendor acquisition methods may vary significantly
- some vendors may never support direct integrations
- the current card-generation scripts may be the real operational bottleneck
- existing presentation layers, such as PDF card generation, may be expensive to preserve but not especially valuable to customers

### Treat the session like a walkthrough, not a workshop

The preferred format is a guided show-and-tell:

- let Progressive walk through real work
- use a live checklist to ensure the team captures the right questions
- avoid forcing the conversation through a rigid interview script
- record the session if allowed so the team can revisit details later

### Separate sourcing from fulfillment

One important distinction surfaced in the discussion:

- the vendors a customer can order from are not necessarily the same as the upstream sources Progressive uses to obtain inventory

That means the team needs two maps:

1. customer-facing digital card types
2. upstream sourcing and fulfillment workflows behind those card types

## Early Data Points Mentioned In The Meeting

- Tim's quick export from Formidable suggested **3,632 total orders** and **362 digital orders**
- That implies digital is roughly **10 percent of orders by count**
- The largest digital order Tim noticed in the raw export was **$75,000**
- The team agreed those numbers still need cleanup before being used as formal project inputs

## Action Items Captured In The Discussion

| Owner | Action |
| --- | --- |
| Danny | Update the client follow-up email draft, add date options, and continue acting as PM while Stephanie is out |
| Spencer | Review Danny's edits to the follow-up email and draft the first pass of the SOW |
| Tim | Clean the exported order data and share a usable summary for digital versus physical volume and spend |
| Danny | Build a vendor worksheet from the current digital storefront and pair it with Tim's data for client prework |
| Bronte | Own a simple in-person agenda / printed session artifact for Danny to bring on site |
| Team | Confirm whether March 25 or March 27 are workable session dates |

## Open Questions

- Which digital vendors should be used as representative walkthroughs during the session
- Whether Progressive can share copies or screenshots of current scripts, spreadsheets, sample files, and outputs
- Whether recording the full walkthrough is allowed
- Whether activation belongs inside the digital workflow being scoped or is primarily part of physical-card operations
- How much of Progressive's larger digital roadmap is already being shaped by Lloyd's vendor integration conversations
