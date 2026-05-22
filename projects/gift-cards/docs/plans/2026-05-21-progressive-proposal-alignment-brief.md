---
title: "Progressive Proposal Alignment Brief"
type: plan
category: internal-brief
date: 2026-05-21
status: draft
tags:
  - progressive
  - proposal
  - internal-alignment
  - roadmap
  - secure-card-vault
  - discovery-closeout
key_insights:
  - The recommended proposal direction is now secure card vault first, not customer portal first.
  - Discovery deliverables should be used as proof and supporting material, while the client narrative should lead with business impact.
  - The internal alignment need is narrower than a full proposal: bring the team current, align on implementation shape, and prepare for a Progressive walkthrough.
key_decisions:
  - Lead with a concrete recommendation rather than a menu of equal options.
  - Position the vault as the operating foundation for portal, direct distribution, reporting, and white-label work.
  - Treat security posture, QuickBooks timing, direct-to-recipient posture, and white-label timing as decision gates.
related:
  - projects/gift-cards/docs/plans/2026-03-25-progressive-discovery-sow-clean.md
  - projects/gift-cards/docs/plans/2026-03-31-discovery-synthesis.md
  - projects/gift-cards/docs/plans/2026-04-23-team-brief-lloyd-scripts-next-steps.md
  - projects/gift-cards/docs/plans/2026-04-27-updated-client-recommendation.md
  - projects/gift-cards/docs/plans/2026-04-27-security-decision-menu.md
  - projects/gift-cards/docs/plans/2026-04-27-vendor-behavior-matrix.md
---

# Progressive Proposal Alignment Brief

## Purpose

This brief is the internal bridge between completed discovery and the proposal we need to take back to Progressive. It is written for team alignment: people who were less involved in discovery need the clean story, and the implementation team needs a crisp recommendation frame so scoping can converge.

The goal is not to finalize pricing or write the client proposal in this pass. The goal is to align Redstamp on the recommended direction, the business narrative, the remaining decisions, and the shape of the walkthrough Progressive should see next.

## Recommendation

Recommend a secure card vault as the first build.

The vault is the operating foundation that lets Progressive handle digital gift cards safely and repeatedly. It comes before the customer-facing portal because discovery showed the most immediate risk is not customer login. The immediate risk is that cash-equivalent card data moves through a fragile, local, under-documented workflow that depends on specific people holding the steps, folder structure, scripts, and failure paths in their heads.

Portal, direct-to-recipient distribution, redemption reporting, and white-label merchant portals should stay on the roadmap. They become more credible after the vault exists because they can reuse the same secure order, card-data, activity-record, and delivery foundation.

## How To Use This Review

This document is the orientation layer. It should help the team understand the recommendation quickly, then point into deeper context where refinement is needed.

| Review lens | What to pressure-test |
|---|---|
| Project | Does this give Progressive a clear path from discovery findings to a next SOW? Are the phase boundaries and client decisions easy to explain? |
| Technical | Does Phase 1 describe a buildable first version? Are merchant workflows, inventory assumptions, Walmart exceptions, and security choices scoped clearly enough? |
| Proposal | Does the recommendation connect the current workflow pain to business impact, and does it make the vault-first sequence feel practical rather than abstract? |

## What Changed After Discovery

Before the March 27 discovery sessions, the natural proposal shape was portal-first: give customers a cleaner place to retrieve cards, reduce encrypted email friction, and pair that with a Lloyd deep dive.

After discovery and script review, the house view should shift:

| Earlier assumption | Updated view | Proposal impact |
|---|---|---|
| The customer portal is the obvious first product. | The operating core is the immediate risk. | Lead with the vault, then show the portal as the next layer. |
| Card generation is the main bottleneck. | Manual handoffs, copy/paste, sensitive data handling, and operator dependency are the bottleneck. | Sell resilience and throughput, not just faster PDF generation. |
| Most gift card merchants require custom generation. | Most merchants provide URLs or card files; only a smaller cohort needs Progressive to generate PDFs from raw card data. | Scope around three patterns: merchant-provided cards, Progressive-generated PDFs, and Walmart just-in-time activation. |
| Lloyd validation was still outstanding. | Lloyd/Mario deep dives happened, and Lloyd provided initial scripts/materials for review. | The proposal can be more concrete, while still noting reproduction/fixture validation as a scoping step. |
| The SOW deliverables were future-tense. | Discovery work is now substantially complete and should be packaged as proof. | Use runbooks, technical spec inputs, security assessment, and roadmap as supporting documents. |

## The Business Story

The client narrative should be simple:

Progressive has built a strong service business around trust, responsiveness, and operational flexibility. Digital gift card volume is growing, and customers increasingly expect faster, cleaner, more self-serve fulfillment. But the current digital workflow is still held together by manual steps, trusted operators, local folders, scripts, spreadsheets, and email.

Today, that works because specific people understand the system. It does not scale as a business capability.

The proposed work turns digital fulfillment from a person-dependent workflow into a supported operating system:

| Today | After the vault |
|---|---|
| Paid digital orders are triggered by paper, email, and operator memory. | Paid orders appear in a fulfillment queue with clear status. |
| Digital inventory lives across merchant spreadsheets, folders, and generated files. | Cards are tracked by merchant, denomination, source, and fulfillment status. |
| Merchant-specific steps live in scripts, spreadsheets, and memory. | The tool guides staff through the right steps for each merchant. |
| Staff assemble card files and delivery emails manually. | Customer-ready card files and delivery emails are generated or pre-staged. |
| When a script fails, the team has to reconstruct what happened from files and memory. | Each order keeps a record of what was created, sent, skipped, or failed. |
| Customers receive card files by email, with limited self-serve history. | The vault creates a cleaner foundation for portal access and order history. |

## Recommended Roadmap

### Phase 0 - Discovery Closeout and Alignment

Package the discovery findings, validate the house recommendation, and prepare the client walkthrough. This includes confirming that the signed discovery SOW deliverables are represented:

- Merchant runbook structure for the three fulfillment patterns
- Technical specification inputs from Lloyd/Mario workflow observation and script review
- Security and handoff assessment
- Strategic roadmap and recommended sequencing
- Adjacent operational inputs for invoicing and physical stickering

### Phase 1 - Secure Card Vault

Build the internal fulfillment foundation:

- Order intake or order creation from existing channels
- Digital gift card inventory by merchant, denomination, source, and status
- Merchant-aware fulfillment workflow
- Secure card-data handling
- Customer-ready card files and delivery emails
- Order history: who processed the order, what card files were created, what was sent, and what failed
- Email package generation or pre-staging
- File cleanup and access policy: who can access card data and how long generated files stay in the system

This is the recommended first commercial proposal.

### Phase 2 - Order Platform and Customer Portal

Once the vault is stable, replace the current Formidable Forms pseudo-commerce flow with a more complete account and ordering experience:

- Customer accounts
- Two-factor authentication or agreed authentication posture
- Order submission that handles the business rules the current forms cannot capture cleanly
- Order history for customers and Progressive staff
- Status tracking from submission through fulfillment
- Customer retrieval of completed card files
- Admin tools for Progressive staff to review orders, manage customer accounts, and connect orders back to fulfillment
- Potential QuickBooks integration if the team agrees it belongs in this phase

### Phase 3 - Service Expansion Modules

Add optional capabilities once the operating foundation exists:

- Trusted-client self-serve micro-orders
- Recipient delivery service: Progressive sends digital gift cards directly to the buyer's recipient list instead of giving the buyer one package of card numbers to distribute on their own. This requires support, proof-of-delivery, bounce handling, and liability posture to be defined first.
- Delivery and redemption reporting: reporting that shows what was sent, to whom, when it was delivered/opened where technically possible, and whether cards were redeemed where merchants expose that data.
- Merchant-branded portals: branded ordering and fulfillment portals for merchant partnerships such as Save-on-Foods or Sequoia, where Progressive operates bulk gift card sales on behalf of a specific merchant brand.
- Physical card stickering automation as a separate operational engagement

## Decisions To Align On Before Client Proposal

These are the decisions Redstamp should align on before the client-facing proposal is finalized.

| Decision | Recommended default | Why it matters |
|---|---|---|
| Security architecture | Secure Web Vault, with explicit decisions on access, file cleanup, and recorded order activity | It is the only option that solves support and future roadmap needs without rebuilding. |
| MVP boundary | Vault first; no customer portal, QuickBooks integration, or direct-to-recipient delivery in V1 | Keeps the first build focused on operational resilience. |
| Walmart scope | Model as a dedicated module, but avoid overcommitting until PowerShell/activation flow is characterized | Walmart is not just another merchant row. |
| SystemOne | Keep as external/manual in V1 unless API availability is confirmed | Replacing it too early adds risk without proving core value. |
| Direct-to-recipient delivery | Roadmap item, not V1 | It changes Progressive's support posture and should be priced as a service model, not just a feature. |
| White-label | Architect with future compatibility, but do not build until contracts justify it | Avoids speculative architecture while preserving the path. |

## Deeper Context HTML Drafts

These companion pages are candidate deliverable drafts. They are meant to keep the recommendation review light while giving the team enough detail to contribute meaningfully.

| Draft | Purpose |
|---|---|
| `2026-05-21-current-state-workflow-map.html` | Shows the observed order-to-delivery flow, with people, systems, handoffs, and failure points. |
| `2026-05-21-merchant-fulfillment-matrix.html` | Shows the three merchant fulfillment models and how they affect the vault. |
| `2026-05-21-security-choices.html` | Shows where card data could live, how support changes, and what Progressive needs to choose. |
| `2026-05-21-phase-1-mvp-boundary.html` | Defines the likely Phase 1 in/out boundary and pricing questions. |

## How This Meets The Discovery SOW

The signed discovery SOW promised a focused discovery engagement, not a finished software build. We should make clear that Redstamp has met the spirit of the work and is now turning findings into a recommendation.

| SOW deliverable | Current state | How to use it |
|---|---|---|
| Merchant runbooks | Source material captured; runbook structure now clear across three patterns | Include summary in proposal appendix; produce operator docs as follow-on if needed. |
| Technical specification | Workflow and script behavior documented; reproduction pass can sharpen estimates | Use as basis for MVP scope and implementation review. |
| Security and handoff assessment | Core risks identified: card data, access, file cleanup, order activity records, and person-dependent process knowledge | Convert into client decision menu and architecture assumptions. |
| Strategic roadmap | Recommendation is now vault first, then portal, then expansion modules | Make this the main proposal narrative. |
| Adjacent operational inputs | Invoicing and stickering pain captured but bounded | Acknowledge as future opportunities without distracting from vault proposal. |

## Proposed Walkthrough Arc

For the Progressive call, avoid walking them through every document. Walk them through the change in understanding.

1. What we saw: the current digital workflow works, but it depends on a fragile chain of people, files, scripts, and manual checks.
2. What that means: the business risk is not just customer convenience; it is continuity, supportability, and safe handling of card data.
3. What we recommend: build the secure card vault first.
4. What changes: staff get a repeatable workflow, Progressive gets auditability, Redstamp can support the system, and customers get a cleaner experience as the next layer.
5. What comes next: agree on security posture and MVP boundary, then Redstamp prices the first build.

## Internal Next Steps

1. Use this brief and the HTML review to bring the team current.
2. Align on MVP boundary, security architecture recommendation, and pricing assumptions.
3. Decide whether to present the client version as a roadmap deck, HTML leave-behind, or proposal memo.
4. Book the Progressive walkthrough for next week.
5. After the walkthrough, Redstamp converts the selected path into the next SOW.
