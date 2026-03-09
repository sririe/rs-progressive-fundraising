---
title: "Client Discovery Call — Progressive Gift Cards"
type: discovery
category: requirements-gathering
date: 2025-01-29
status: complete
participants:
  progressive:
    - Doug B. (Owner)
    - Gord S. (Advisor)
    - Lloyd S. (Technical Contractor)
  redstamp:
    - Spencer R.
    - Tim L.
    - Brontë B.
    - Stephanie L.
tags: [discovery, digital-fulfillment, customer-portal, white-label, automation-roadmap, card-generation, business-continuity]
key_decisions:
  - Ordering flow stays as-is (no login required to place orders)
  - Account creation added post-order via link in invoice
  - Payment remains external via BenjaPay
  - URLs preferred over PDFs for digital card delivery
  - Doug wants advisory relationship, not just execution
blockers:
  - Technical deep-dive with Lloyd on card generation workflow not yet completed
  - White-label sales outcomes (Save-on-Foods, Sequoia, White Spot) still pending
related:
  - docs/discovery/2025-01-27-internal-pre-meeting.md
  - docs/discovery/2025-01-29-client-meeting-transcript.md
---

# Meeting Summary: Progressive Gift Cards - January 29, 2025

**Call Type:** Discovery / Requirements Gathering
**Prepared for:** Internal Team Review

---

## TLDR

What began as a conversation about adding customer login functionality and white-label portals revealed a more pressing underlying challenge: Progressive's digital gift card fulfillment process is fragile, manual-intensive, and dependent on specialized knowledge held by one contractor (Lloyd). Doug explicitly asked Red Stamp to take an advisory role in recommending solutions, not just respond to stated requirements. The immediate website enhancements remain relevant, but addressing the operational bottleneck in digital card generation and delivery may be a higher-value starting point.

---

## Key Takeaways

### 1. Digital Card Fulfillment Is the Core Pain Point

The current process for digital gift card orders is manual, time-consuming, and knowledge-dependent:

- **Card generation varies by vendor:** Some vendors (Best Buy, Starbucks) provide URLs that can be passed through directly. Others (Walmart, Amazon, Chapters, and some Loblaws products) require Progressive to generate cards from raw data (card numbers and PINs).

- **Generation is slow:** Loblaws cards take approximately 20 seconds each to generate. For an order of 600 cards, this represents significant processing time.

- **Multiple manual steps:** Inventory tracking in spreadsheets, copying data between files, running generation scripts, verifying output, zipping/encrypting, and emailing with separate password delivery.

- **Knowledge concentration risk:** Lloyd built and maintains these custom tools. Mario is being trained as backup, but the process isn't easily transferable to other staff members. Most of the team skews older and less technically sophisticated.

- **Scalability concern:** Lloyd noted that if digital orders reached the same volume as physical cards, they "wouldn't be able to keep up."

### 2. Website Enhancement Request (Original Scope)

Doug's initial request focused on adding a secure login area to the website for digital card retrieval:

- **Current state:** Orders placed without login; digital cards delivered via encrypted email attachments.
- **Desired state:** Customers create accounts and retrieve their digital cards from a secure portal after payment is confirmed.
- **Rationale:** Reduce support burden from customers who can't open encrypted files, lose passwords, or have corporate email restrictions blocking attachments.

**Open question on implementation approach:** Tim suggested keeping the existing order flow intact and adding account creation as a post-order step (via link in invoice) rather than requiring login before ordering. Doug seemed open to this, but there are tradeoffs to consider:

- *Post-order account creation:* Preserves current conversion flow; adds friction only for digital orders after purchase.
- *Pre-order account creation for digital:* Enables automatic order-to-account association; may reduce abandonment from confused customers.

### 3. White-Label Portal Opportunity (Dependent on Sales Wins)

Doug and Gord are actively pursuing bulk fulfillment contracts with Save-on-Foods, Sequoia Group (Seasons, Tea House), and White Spot. If secured, these clients would need branded ordering experiences:

- **Tier 1:** Direct link to existing Progressive site (no customization).
- **Tier 2:** Dedicated single-brand portal (e.g., only White Spot cards, administered by Progressive).
- **Tier 3:** Fully branded white-label experience (client branding, Progressive administration). Mockups previously provided were for this tier.

*Important dependency:* These opportunities are contingent on Progressive winning the business. The white-label solution is architecturally different from the current site and would likely require rework if we build the account/login features first on the existing platform.

### 4. Broader Automation Roadmap (New Information)

Doug shared a three-phase internal automation vision, which provides context for where web/digital solutions fit:

- **Phase 1 (Imminent):** In-office sticker machine for applying denominations to physical cards.
- **Phase 2 (Significant investment):** Barcode/magstripe/QR capture system for inventory management and order fulfillment automation. Doug mentioned potential tie-ins with invoicing and AI capabilities.
- **Phase 3 (3-5 year horizon):** Direct integration with merchant backends. Already in progress with Tim Hortons (via Cash Star), Amazon, and Walmart.

*Assumption:* This roadmap is primarily focused on physical card operations. The digital fulfillment challenges exist somewhat separately and may benefit from earlier intervention.

---

## Meaningful Client Statements

1. *"I don't know what the f*** to do. Seriously... that's why I'm talking to family members. I'm bringing in people that know machinery stuff because I don't have a clue and I know we got to go there."* — Doug, on his need for advisory guidance beyond just executing stated requirements.

2. *"If you had the same number of digital card orders as you had physical, then you wouldn't be able to keep up."* — Lloyd, highlighting the scalability cliff.

3. *"You can't just go to Elena and say, 'Can you take this?' She won't, right? So you have to have multiple backups... it's not something that everybody's just going to be able to pick up and do."* — Lloyd, on the knowledge concentration risk.

4. *"We really trust your company and trust you guys. We see this as a long-term partnership where we're going to need you for a lot of different things."* — Doug, signaling openness to expanded engagement.

---

## Next Steps

1. **Internal discussion:** Red Stamp team to review options and develop recommendations (this week).
2. **Technical deep-dive:** Spencer to coordinate a session with Danny and Lloyd to walk through current card generation workflow. Goal: identify quick wins for streamlining/hardening the process.
3. **Follow-up to Progressive:** Early next week with initial recommendations and proposed approach.

---

## Red Stamp Advisory Perspective

*The following represents initial internal thinking for team discussion, not recommendations to share with Progressive yet.*

### Observations

- **The stated request (website login/portal) addresses a symptom, not the root cause.** The delivery mechanism (email vs. portal retrieval) matters less than the upstream process that creates the deliverables. If card generation remains fragile and manual, a portal just moves where the friction occurs.

- **Lloyd's tooling is a liability disguised as an asset.** Custom scripts that only one person understands, running on local machines, with manual inventory tracking in spreadsheets — this is a business continuity risk. If Lloyd is unavailable, digital orders stop.

- **The white-label opportunity may be premature to build for.** Until Progressive secures those contracts, investing in Tier 3 architecture is speculative. However, any near-term work should avoid creating technical debt that makes white-label harder later.

- **Doug is asking for partnership, not just execution.** He explicitly said he wants us to tell him what he *should* be doing, not just respond to what he asks for. This is an opportunity to demonstrate strategic value.

### Potential Approaches to Discuss

**Option A: Start with the portal (as requested)**
- Build account system and secure retrieval interface
- Cards still generated manually by Progressive team, then uploaded to customer accounts
- Addresses the delivery/support pain point but not the generation bottleneck
- Risk: If white-label wins happen, may need to rebuild

**Option B: Start with operational tooling**
- Work with Lloyd to understand current scripts and workflows
- Build a more robust, documented, user-friendly generation/fulfillment tool
- Could be a lightweight internal web app that any trained staff member could use
- Addresses the "bus factor" and scalability concerns first
- Portal becomes Phase 2 once the backend is solid

**Option C: Hybrid — scoped portal with operational improvements**
- Implement account creation and basic portal (Tier 1 functionality)
- Simultaneously consult on and potentially improve the generation workflow
- Position as two parallel workstreams with different billing structures

### Questions to Resolve Internally

1. **Appetite for operational/tooling work:** Is this something we want to take on? It's outside typical web dev scope but aligns with the AI/automation direction Danny has been exploring.

2. **Billing structure:** Doug has investment appetite but no defined budget. How do we scope discovery/consulting vs. implementation? Should the Lloyd deep-dive be billable or positioned as discovery for a larger engagement?

3. **White-label timing:** Should we ask Doug for a timeline on when he expects decisions from Save-on-Foods, Sequoia, etc.? This affects whether we should architect for flexibility now or wait.

4. **Security considerations:** Any solution involving card numbers being transmitted or stored on web infrastructure introduces risk. Tim flagged this. How do we address without over-engineering?

### Flagged Assumptions

- We're assuming Mario is technically capable of taking over Lloyd's processes if properly trained and given better tools. This should be validated.
- We're assuming the white-label sales conversations are genuinely active, not aspirational. Worth confirming priority level.
- "Front Street" was mentioned regarding Amazon card display time limits — unclear if this is a vendor or contact we should know about.
