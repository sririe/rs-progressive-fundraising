---
title: "Three-Tier Advisory Engagement Proposal for Progressive Gift Cards"
type: plan
category: engagement-proposal
status: active
date: 2026-02-23
origin: projects/gift-cards/docs/brainstorms/2026-02-23-advisory-engagement-strategy-brainstorm.md
tags:
  - advisory
  - proposal
  - portal-mvp
  - operational-assessment
  - digital-transformation
  - wordpress
key_decisions:
  - Platform adoption rejected — Progressive's 1-4% margin depends on direct vendor relationships (see brainstorm)
  - Three-tier proposal structure gives Doug investment agency while anchoring toward Option 2
  - WordPress custom post types for portal MVP; magic link auth recommended but not yet validated with client
  - Lloyd deep-dive is a prerequisite for scoping Options 2 and 3
  - White-label deferred until contracts secured
  - Only external URLs stored in WordPress — no raw card numbers/PINs in the portal database (assumption; unvalidated)
  - Individual recipient distribution deferred from MVP — Doug requested this capability; to be scoped in a future phase
key_insights:
  - The email-to-account matching mechanism is the highest-risk implementation detail for the MVP
  - The Lloyd/Mario upload interface is the bottleneck — if it's clunky, the portal starves for content
  - Option 3 must be priced as a two-phase commitment (fixed for Options 1+2, ranged for additional work)
  - Legacy customer migration is required for portal adoption — without it, encrypted email delivery persists indefinitely
  - Fundstream is both a rejected platform option AND a competitive threat — Doug cited their speed as a benchmark Progressive needs to match
  - Red Stamp internal capacity (two-person dev team) has not been assessed against Option 3 scope
participants:
  red_stamp:
    - Spencer R. (engagement lead, primary contact)
    - Tim L. (dev lead)
    - Bronte B. (developer)
    - Stephanie L. (present at client meeting, left early)
    - Danny (AI/automation, Lloyd deep-dive participant)
  progressive:
    - Doug B. (owner, decision-maker)
    - Gord S. (advisor, sales)
    - Lloyd S. (technical contractor, card generation)
    - Mario (Lloyd's backup, in training)
related:
  - projects/gift-cards/docs/brainstorms/2026-02-23-advisory-engagement-strategy-brainstorm.md
  - projects/gift-cards/docs/discovery/2026-01-29-client-discovery-call.md
  - projects/gift-cards/docs/discovery/2026-01-29-client-meeting-transcript.md
  - projects/gift-cards/docs/discovery/2026-01-27-internal-pre-meeting.md
  - projects/gift-cards/docs/solutions/2026-02-23-mvp-customer-portal-research.md
  - projects/gift-cards/docs/solutions/2026-02-23-gift-card-fulfillment-technology-landscape.md
  - projects/gift-cards/docs/solutions/2026-02-23-giftbit-platform-evaluation.md
blockers:
  - Lloyd technical deep-dive has not occurred — required before Options 2/3 can be scoped with full confidence
  - Amazon "Front Street" display time constraint is unverified — affects portal architecture for Amazon cards
  - Red Stamp pricing and internal capacity estimation not yet done
  - Authentication approach (magic link vs. 2FA vs. other) not validated with Progressive — Lloyd raised security concerns
  - Card data storage architecture (URLs only vs. raw card data) is an assumption, not confirmed
  - Shoppers Drug Mart / Loblaws generation status unclear — Lloyd was uncertain whether they still require manual generation
---

# Three-Tier Advisory Engagement Proposal for Progressive Gift Cards

## Overview

This plan defines the deliverables, scope, acceptance criteria, and sequencing for a three-tier engagement proposal to be presented to Doug B. at Progressive Gift Cards. The proposal answers Doug's explicit question: "What should we do?"

The three tiers range from a focused customer portal MVP (~4-6 weeks) to a comprehensive digital operations transformation (~3-6 months). Each tier builds on the previous one, allowing Progressive to start small and expand based on demonstrated value.

This is a **proposal plan** — it defines what Red Stamp will propose to Progressive, how the engagement is structured, and what needs to be resolved before the proposal is delivered. It is not a technical implementation plan (that comes after Progressive selects a tier).

## Problem Statement

### Doug's stated priorities (in his words, from the Jan 29 discovery call)

Doug presented three topics in order:
1. **Customer portal** for digital card retrieval — "We want our clients to be able to go in to that part of the website and retrieve gift cards"
2. **White-label portals** for bulk vendor clients (Save-on-Foods, Sequoia, White Spot) — contingent on winning those contracts
3. **Automation/AI discussion** — longer-term efficiency improvements

The immediate pain driving #1: digital cards are delivered via encrypted email attachments. Doug described this as "constant" — customers struggle with corporate email filters blocking attachments and lost encryption passwords. ("We get a lot of people that don't know how to do it properly... their company protections won't allow them to open things and it's just constant.")

Doug also cited competitive pressure from Fundstream, who can "have any gift card to the end user in two seconds." Progressive's manual delivery process is a competitive disadvantage, not just an operational annoyance.

### Red Stamp's advisory observation (our interpretation, not Doug's framing)

Beyond the delivery friction Doug feels daily, there is a second problem he acknowledged but did not lead with:

**Operational fragility:** All digital card generation depends on Lloyd S., a single contractor running custom scripts on local machines with spreadsheet-based inventory. If Lloyd is unavailable, digital fulfillment stops. Mario is being trained as backup but his readiness is unvalidated. Lloyd himself articulated this: "You can't just go to Elena and say, 'Can you take this?'... you have to have multiple backups... it's not something that everybody's just going to be able to pick up and do."

Doug agreed with this concern when Spencer raised it during the call, and Lloyd explicitly supports automation ("stop paying me to do something that could be automated"). But Doug's priority ordering was portal first, operational risk second. The proposal should respect that ordering — lead with what Doug asked for, then build the case for the deeper work.

See brainstorm for full analysis: [advisory-engagement-strategy-brainstorm.md](../brainstorms/2026-02-23-advisory-engagement-strategy-brainstorm.md)

## Proposed Solution

A three-tier engagement proposal that gives Doug investment agency:

- **Option 1 ("Solve the Pain"):** Customer portal MVP — addresses delivery friction
- **Option 2 ("Solve + Explore"):** Portal + Lloyd deep-dive — addresses delivery friction and surfaces operational risk
- **Option 3 ("Transform"):** Portal + deep-dive + operational tooling — addresses delivery, operations, and scalability

Red Stamp will determine which option to recommend during proposal preparation (deferred from brainstorm — see key decision #7 in the brainstorm document).

## Alternative Approaches Considered

**Platform adoption (Fundstream, Giftbit):** Evaluated internally by Red Stamp and rejected on margin grounds. Progressive's entire margin (1-4%) depends on the wholesale-to-face-value spread from direct vendor relationships. Progressive is one of only 2 bulk resellers of Walmart gift cards in Canada. Any intermediary platform eliminates or compresses margins unacceptably. Full analysis in [gift-card-fulfillment-technology-landscape.md](../solutions/2026-02-23-gift-card-fulfillment-technology-landscape.md) and [giftbit-platform-evaluation.md](../solutions/2026-02-23-giftbit-platform-evaluation.md). *Note: This evaluation has not been discussed with Progressive. Doug views Fundstream primarily as a competitor whose speed Progressive needs to match, not as a platform Progressive might adopt. The competitive angle should be used to strengthen the urgency case when presenting.*

**Assessment-only first engagement:** Considered leading with a standalone Lloyd deep-dive before building anything. Deferred in favor of wrapping the assessment into Option 2 alongside the portal build, which delivers tangible output alongside the advisory work. *Note: Doug has expressed openness to investment ("I'm happy to invest in you guys to help us make this better"), so an assessment-only approach is not necessarily off the table — but pairing it with the portal makes for a stronger proposal.*

**Build the portal without any operational assessment:** This is Option 1 — available as the lowest-investment tier, but Red Stamp should steer Doug toward at least Option 2 because the portal's upload workflow depends on understanding Lloyd's process.

## Implementation Phases

### Phase 1: Pre-Proposal Preparation (Red Stamp Internal)

Before delivering the proposal to Doug, Red Stamp must resolve several open questions.

**Tasks:**

1. **Resolve card data storage architecture**
   - Confirm with Lloyd: when he generates card URLs, where do they point? Who hosts the URL endpoints?
   - If only external URLs are stored in WordPress (links to vendor-hosted or Lloyd-hosted pages), the security posture is simpler
   - If raw card numbers/PINs must be stored in WordPress, encryption at rest becomes mandatory and the scope of Option 1 increases significantly
   - This is a 30-minute conversation with Lloyd — the single highest-leverage pre-proposal activity
   - **Assumption until resolved:** Only external URLs are stored; no raw card data touches the WordPress database

2. **Validate Amazon "Front Street" constraint**
   - Lloyd mentioned Amazon cards cannot be displayed on a site for more than ~1 hour
   - If true, Amazon card retrieval needs a different flow (on-demand generation or time-boxed access)
   - Can be resolved in the same Lloyd conversation above
   - **Assumption until resolved:** Treat Amazon cards the same as others until constraint is validated

3. **Price each tier**
   - Estimate hours and set pricing based on Red Stamp's rates
   - Industry benchmarks (from brainstorm research): Option 1 at $8-15K, Option 2 at $15-25K, Option 3 at $40-80K+
   - Option 3 should be priced as two phases: Phase A (Options 1+2, fixed price) + Phase B (additional work, scoped after deep-dive, with a budget range disclosed upfront)
   - Consider crediting Option 1 toward Option 2, and Option 2 toward Option 3, to incentivize the larger engagement

4. **Decide on recommendation**
   - Which option will Red Stamp actively steer Doug toward?
   - The three-tier structure naturally anchors to the middle option (Option 2)
   - Prepare the "why" for the recommended option in language Doug understands (business risk, not technical jargon)

5. **Choose proposal format**
   - Research recommends delivering the roadmap in a live session (video or in-person), not as a PDF sent via email
   - Walk through the options interactively and get verbal commitment on next steps
   - Prepare a leave-behind document Doug can reference after the meeting

6. **Informal Lloyd conversation**
   - Before the proposal goes to Doug, confirm Lloyd's willingness to participate in the deep-dive (Option 2/3)
   - Lloyd has expressed support ("stop paying me to do something that could be automated") but his cooperation is essential
   - This can be combined with the card data storage question (task 1)

7. **Decide Option 2 billing structure**
   - Should the Lloyd deep-dive be billed as a separate advisory line item or bundled into the portal project cost?
   - Separate billing: makes advisory value visible to Doug, positions Red Stamp as a strategic partner
   - Bundled: simpler decision for Doug, one invoice, one SOW
   - This affects how the proposal is structured and presented (see brainstorm open question #2)

**Success criteria:** All seven tasks resolved. Red Stamp has a priced, formatted proposal with a clear recommendation ready to present.

**Estimated effort:** 1-2 days of Red Stamp working time. Note: elapsed time will be longer due to scheduling the Lloyd call — target completing Phase 1 within one week.

### Phase 2: Proposal Delivery

**Tasks:**

1. **Schedule proposal session with Doug (and Gord if available)**
2. **Present three tiers with recommendation**
3. **Address questions, discuss budget, and get commitment on a tier**
4. **Send follow-up with leave-behind document and next steps**
5. **If Doug selects a tier, scope the engagement formally (SOW/contract)**

**Success criteria:** Doug selects a tier and commits to proceed. Or, Doug asks for time to decide — in which case, schedule a follow-up within one week.

### Phase 3: Option 1 Delivery — Customer Portal MVP (~4-6 weeks)

This is the core deliverable shared across all three tiers.

**Deliverables:**

1. **Customer portal on existing WordPress site**
   - Authenticated login — *Red Stamp recommends magic link authentication (WordPress Magic Login plugin) for simplicity, but this has not been discussed with Progressive. Lloyd raised concerns about username/password being insufficient and suggested "two step authentication or verifying that this is a computer that belongs to the organization." Authentication approach must be validated with Progressive before implementation.*
   - Order list showing fulfilled deliveries with status indicators (Received, Processing, Ready for Retrieval)
   - Multi-vendor order support: orders with multiple vendor batches display per-vendor line items with independent status (e.g., 3 of 5 vendors fulfilled) — *Note: this UI requirement is Red Stamp's interpretation of Lloyd's process description ("they received their cards per vendor... five different zip files"). The status-tracking interface was not discussed with Progressive.*
   - Secure card retrieval via URL displayed inline (not downloadable files)
   - Per-customer content restriction (each customer sees only their own orders)

2. **Internal upload interface for Lloyd/Mario**
   - WordPress admin screen for creating/updating order records
   - Fields: order reference, customer email, vendor, card URLs, status
   - Manual override to associate orders with accounts when email matching fails
   - Designed for non-developers handling multiple orders per day

3. **Automated notification system**
   - Combined "cards are ready" + magic link email sent when Lloyd/Mario marks an order as "fulfilled"
   - Customer clicks link, authenticates, and lands directly on their fulfilled order
   - Fallback: direct-login option on portal (enter email, request magic link manually)

4. **Legacy customer migration email**
   - One-time email campaign to existing customers inviting them to create portal accounts
   - Historical orders are NOT backfilled (portal only shows orders fulfilled after launch)
   - *Note: This deliverable is a Red Stamp addition — not discussed with Progressive. Required for portal adoption; without it, existing customers have no reason to create accounts.*

5. **Security baseline**
   - TLS 1.2+ for all data in transit
   - No raw card numbers/PINs stored in WordPress (URLs only) — *assumption, pending Lloyd validation*
   - Retrieval logging (timestamp, IP, user agent for every card access)
   - Authentication security parameters (session timeout, token expiry, 2FA requirements) to be determined during implementation based on the authentication approach selected with Progressive
   - Tim flagged during pre-meeting: any system holding card access is essentially a "bank site" — *"I think kind of a security risk that we'd want to avoid is having a lot of unsold inventory, like numbers or files sitting on the site... they could in theory kind of redeem the numbers... just like cash."* The URL-only assumption mitigates this, but must be validated.

**Explicit exclusions (Option 1 does NOT include):**
- **Individual recipient distribution** — *Doug requested this: "I want to be able to deliver to the end user as well" and "If they wanted to go out to a hundred or five hundred people in their company, what's the mechanism to set that up?" This is deferred to a future phase, not permanently excluded. The proposal presentation must acknowledge this was Doug's request and explain the phasing rationale, not treat it as scope creep.*
- Payment processing or BenjaPay integration
- Historical order backfill
- Multi-user organizational accounts (one account per email)
- Physical card order tracking
- White-label capabilities
- Card generation automation (Lloyd/Mario still generate manually)

**Technical approach:**
- WordPress custom post type ("Deliveries") with custom fields for order data
- Email address as linking key between Formidable Forms submissions and portal accounts
- Formidable Forms remains unchanged for order intake
- Content restriction ensuring per-customer visibility
- Authentication approach TBD — magic link recommended by Red Stamp; 2FA/device-level auth raised by Lloyd; to be validated with Progressive
- Architecture documented in [mvp-customer-portal-research.md](../solutions/2026-02-23-mvp-customer-portal-research.md)

**Gord's framing note:** Gord described the portal as more of a reference tool for problem cases — "a dashboard... there may not be any stickiness at all, they may be able to just disperse the e-cards as they normally had in the past, but it's only if from lost sort of cards or whatever that they'd have to refer to something." The proposal positions the portal as the new standard delivery channel. This may be the right call, but Gord's "optional fallback" framing should be considered — it may affect adoption expectations and how the portal is positioned to customers.

**Key implementation risks:**
- **Email matching fragility:** Customer may use different email for ordering vs. portal account. Mitigated by manual override in admin + "can't find your order?" help flow in portal.
- **Multi-vendor orders:** A single order may contain multiple vendor batches ready at different times. The status model must support partial fulfillment (per-vendor line items within an order).
- **Notification email deliverability:** Magic links in corporate email environments may be spam-filtered. Mitigated by direct-login fallback and domain warming.
- **Upload interface adoption:** If the admin interface is cumbersome, Lloyd/Mario will resist using it and the portal starves for content. Wireframe this before building the customer-facing side.

**Success criteria:**
- [ ] Customer can create an account, authenticate via agreed-upon method, and retrieve card URLs
- [ ] Lloyd/Mario can upload card URLs to an order and trigger customer notification
- [ ] Orders with multiple vendors display per-vendor line items with independent status
- [ ] Manual override exists for email-mismatch order-account association
- [ ] Retrieval logging captures every card access event
- [ ] Legacy customers receive migration email within 1 week of launch
- [ ] Zero raw card numbers/PINs stored in WordPress database

### Phase 4: Option 2 Additions — Lloyd Deep-Dive & Operational Assessment (~2-4 additional weeks)

If Doug selects Option 2 or 3, this work runs alongside or immediately after the portal build.

**Deliverables:**

1. **Vendor-by-vendor process documentation (runbooks)**
   - Step-by-step operational guides for each of the four generation vendors: Walmart, Amazon, Chapters, Loblaws
   - Input formats, processing steps, output formats, error handling
   - Written for operators (Mario), not developers

2. **Failure pattern catalog**
   - What goes wrong, how often, and what Lloyd does to fix it
   - Per-vendor: common errors, data format issues, vendor-specific quirks
   - Recovery procedures for each failure mode

3. **Decision architecture documentation**
   - Why each vendor's process is different
   - What the vendor-specific constraints are (e.g., Loblaws' 20-second-per-card speed, Amazon display limits)
   - Which processes are candidates for automation vs. which are inherently manual

4. **Operational improvement roadmap**
   - Prioritized recommendations for automation, tooling, and risk reduction
   - Categorized by: quick wins (< 1 week), medium effort (1-4 weeks), significant investment (1+ months)
   - Cost/benefit framing for each recommendation (in language Doug understands)

5. **Mario readiness assessment**
   - Can Mario independently process an order for each of the four generation vendors?
   - Can Mario recover from the most common failure modes without Lloyd?
   - Can Mario train someone else?
   - Gap analysis: what additional training or tooling does Mario need?

**Existing baseline:** Lloyd provided a partial process walkthrough during the Jan 29 discovery call — inventory storage, card number extraction from Excel, generation script execution, verification, zip/upload, URL generation. The deep-dive will validate, extend, and formalize this into operator-ready documentation, not start from zero. Shoppers Drug Mart / Loblaws generation status also needs clarification — Lloyd was uncertain whether they still require manual generation or now provide URLs directly.

**Key dependency:** The Danny/Spencer/Lloyd walkthrough session must be scheduled and completed. This has been a blocker since January 2026.

**Success criteria:**
- [ ] Runbooks exist for all four generation vendors, validated by Lloyd as accurate
- [ ] Failure pattern catalog covers at least the 5 most common failure modes per vendor
- [ ] Operational roadmap contains at least 3 prioritized recommendations with cost/benefit framing
- [ ] Mario readiness assessment answers all four questions above with evidence
- [ ] Deliverables are written for non-technical readers (Doug, Gord, Mario)

### Phase 5: Option 3 Additions — Digital Operations Transformation (~2-4 additional months)

If Doug selects Option 3, this work is scoped and priced after the Phase 4 deep-dive completes. The items below are directional — their scope will be refined based on deep-dive findings.

**Deliverables (subject to refinement):**

1. **Internal fulfillment tool**
   - Web-based application replacing Lloyd's local scripts
   - Standardized data intake (vendor-specific CSV templates)
   - Automated card generation with error handling and audit trails
   - Usable by any trained staff member (not just developers)
   - Connected to the customer portal (generated cards automatically populate order records)

2. **Inventory management**
   - Card inventory tracking moved from Google Docs/spreadsheets into the fulfillment tool
   - Per-vendor inventory status, depletion alerts, usage history

3. **Ongoing advisory retainer**
   - Monthly strategic guidance sessions
   - Vendor evaluation support (as Amazon/Walmart integrations progress)
   - Process improvement oversight
   - Defined scope: X hours/month at agreed rate (to be set during SOW)

4. **White-label readiness assessment**
   - Architecture review of the portal to identify what would need to change for multi-tenant white-label deployment
   - Deliverable: written assessment with specific recommendations, not a prototype or build
   - Explicitly scoped as "what would it take" — not "build white-label capabilities"

5. **Vendor integration evaluation**
   - Which merchants are moving toward API access — *note: Progressive is already integrated with Walmart's backend, and starting Amazon and Tim Hortons (via Cash Star) independently of Red Stamp. The landscape may shift during the engagement.*
   - What API integration would mean for Progressive's workflow and Lloyd's processes
   - Timeline and investment estimate for each integration opportunity

**Doug's parallel investment plans:** Doug described a three-phase physical card automation roadmap: (1) sticker machine (imminent), (2) barcode/magstripe/QR capture for inventory and fulfillment, (3) merchant backend integration over 3-5 years. If Red Stamp builds inventory management in Option 3, it should not conflict with or duplicate whatever Doug builds for physical card operations. This needs to be discussed during scoping.

**Red Stamp capacity note:** Bronte raised during the pre-meeting that Option 3 scope is substantial for a two-person dev team: "This is a lot of work and especially for like a two-team developer." Red Stamp's internal capacity to deliver Option 3 has not been assessed. This must be addressed during the pricing session — either through contractor augmentation, timeline extension, or scope reduction.

**Pricing structure:** Option 3 is priced as Phase A (Options 1+2, fixed price) + Phase B (additional work above, scoped and priced as a fixed-fee project after the deep-dive, with a budget range disclosed in the initial proposal). This protects both Red Stamp and Progressive from scope uncertainty.

**Success criteria (to be refined post-deep-dive):**
- [ ] At least one vendor's card generation is fully automated through the fulfillment tool
- [ ] Mario (or another non-developer staff member) can process a complete order without Lloyd
- [ ] Inventory tracking produces accurate real-time counts across all vendors
- [ ] White-label readiness assessment delivered and reviewed with Doug
- [ ] Advisory retainer established with defined cadence and scope

## Dependencies & Prerequisites

| Dependency | Blocks | Status | Owner |
|-----------|--------|--------|-------|
| Lloyd conversation (card data storage + Amazon constraint) | Phase 1 tasks 1-2, Portal architecture | Not started | Spencer/Danny |
| Red Stamp internal pricing | Proposal delivery | Not started | Spencer/Tim |
| Recommendation decision | Proposal delivery | Not started | Spencer |
| Proposal format preparation | Proposal delivery | Not started | Spencer |
| Doug's tier selection | Phases 3-5 | Blocked on proposal delivery | Doug |
| Danny/Spencer/Lloyd deep-dive session | Phase 4 | Not started | Spencer/Danny |
| Phase 4 deep-dive completion | Phase 5 scoping and pricing | Blocked on Phase 4 | Red Stamp |

## Risk Analysis & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Doug selects Option 1 only (no deep-dive) | Medium | Medium | Anchor the proposal toward Option 2. Frame the deep-dive as "insurance against your biggest operational risk." Begin retainer conversation during Option 1 delivery. |
| Email matching fails frequently in production | High | High | Build manual override from day one. Add "can't find your order?" help flow. Consider adding phone number as secondary matching key. |
| Lloyd is unavailable or uncooperative for deep-dive | Low | Critical | Have informal conversation before proposal. Lloyd has expressed support for automation. If unavailable, Option 2/3 cannot proceed — communicate this risk to Doug. |
| Portal adoption is slow (customers don't create accounts) | Medium | Medium | Legacy migration email campaign. Include portal link in all future invoices. Progressive staff verbally direct customers to portal during calls. |
| Amazon display time constraint is real | Unknown | Medium | Validate in Lloyd conversation. If confirmed, scope an Amazon-specific retrieval flow (adds ~1-2 weeks to Option 1). |
| Option 3 scope expands beyond budget after deep-dive | Medium | High | Two-phase pricing structure. Phase B is scoped and priced after deep-dive with a disclosed budget range. Doug commits to Phase A first. |
| WordPress cannot handle security requirements | Low | High | Only store URLs, not raw card data. If raw card data is required (resolved in Phase 1 task 1), re-evaluate platform choice before committing to build. |
| Doug expects individual recipient distribution in Option 1 | High | High | Doug explicitly asked for this — do NOT treat as scope creep. Frame as a phased deferral: "You asked for this and we want to build it. Here's why it makes sense as a Phase 2 capability once the portal foundation is solid." Verbal acknowledgment during presentation is critical. |

## Action Items (Immediate Next Steps)

1. **Schedule a 30-minute call with Lloyd** — resolve card data storage question and Amazon constraint. This unblocks the entire proposal. (Owner: Spencer/Danny)

2. **Internal pricing session** — estimate hours for each tier based on Red Stamp's rates. Use industry benchmarks as starting points. (Owner: Spencer/Tim)

3. **Decide on recommendation** — which tier will Red Stamp steer Doug toward? Prepare the "why" in business language. (Owner: Spencer)

4. **Prepare proposal materials** — slide deck or document for live walkthrough + leave-behind. (Owner: Spencer)

5. **Schedule proposal session with Doug** — target within 2 weeks of completing items 1-4. (Owner: Spencer)

## Decision Log

Tracks the provenance of every significant decision in this proposal — what was confirmed by the client, what Red Stamp added, and what still needs validation.

### Confirmed by client (from Jan 29 discovery call + transcript)

| Decision | Source | Quote/Evidence |
|----------|--------|----------------|
| Ordering flow stays as-is, no login to order | Doug, transcript ~36:10 | "The ordering will continue exactly how it is right now. They don't have to log in or anything to order" |
| Account creation post-order via invoice link | Tim proposed, Doug agreed, transcript ~16:57 | "In the invoice I could see potentially you also include a link to create your account there" |
| Payment stays external via BenjaPay | Doug, transcript ~14:04; Tim, pre-meeting ~15:10 | "We're not getting into login, place an order, pay with your credit card on the website. We're not going there yet" |
| URLs preferred over PDFs | Doug, transcript ~1:04:06 | "Let's just think in the world of URLs, don't worry about the PDFs" |
| Doug wants advisory, not just execution | Doug, transcript ~52:00 | "I want you to come back and tell me what we should be doing. From your basis of your expertise" |
| Doug wants individual recipient distribution (future) | Doug, transcript ~37:21 | "I want to be able to deliver to the end user as well... what's the mechanism to set that up?" |
| Lloyd supports automation | Lloyd, transcript ~7:30 | "Stop paying me to do something that could be automated" |
| Doug open to investment | Doug, transcript ~52:21 | "I'm happy to invest in you guys to help us make this better" |
| White-label is contingent on sales wins | Doug, transcript ~3:50-4:16 | Active conversations with Save-on-Foods, Sequoia, White Spot — but outcomes unknown |
| Lloyd wants strong auth on any portal | Lloyd, transcript ~49:00 | "Just having a username password is not good enough... two step authentication or verifying that this is a computer that belongs to the organization" |

### Red Stamp additions (our analysis, not discussed with client)

| Decision | Rationale | Needs validation? |
|----------|-----------|-------------------|
| Three-tier proposal structure | Anchoring strategy; gives Doug investment agency | No — this is proposal strategy, not a client-facing technical decision |
| WordPress custom post types for portal | Best fit for existing site; Tim proposed in pre-meeting | No — internal technical decision |
| Magic link authentication (recommended) | Simplicity, no passwords to manage | **Yes** — conflicts with Lloyd's 2FA concern; must be discussed |
| Platform adoption rejected (Fundstream, Giftbit) | Margin model incompatibility | Worth mentioning to Doug as due diligence, but decision is sound |
| "Operational fragility" as co-equal problem framing | Red Stamp's advisory judgment | **Presentation caution** — lead with what Doug asked for (portal), then build the case |
| Legacy customer migration email | Required for portal adoption | No — operational necessity, but should be mentioned to Doug as a deliverable |
| Per-vendor line items with independent status | Interpretation of Lloyd's per-vendor fulfillment process | Mild — reasonable inference, but specific UI not discussed |
| Security parameters (session timeout, token expiry) | To be determined based on auth approach | N/A — removed from plan, will be set during implementation |
| Fundstream as rejected platform (not competitive threat) | Incomplete framing | **Yes** — should also be positioned as competitive pressure when presenting to Doug |

### Still needs resolution

| Item | Blocks | How to resolve |
|------|--------|----------------|
| Card data storage architecture (URLs vs. raw data) | Portal security model, entire scope | 30-min Lloyd conversation |
| Amazon "Front Street" display time constraint | Amazon card portal flow | Same Lloyd conversation |
| Authentication approach | Portal UX and security | Discuss with Progressive during proposal or early in Option 1 |
| Shoppers/Loblaws generation status | Deep-dive scope (Option 2) | Lloyd conversation |
| "Front Street" identity (vendor or contact?) | Amazon constraint understanding | Lloyd conversation |
| Individual recipient distribution phasing | Proposal framing | Must be explicitly addressed during proposal presentation to Doug |
| Red Stamp internal capacity for Option 3 | Pricing and feasibility | Internal pricing session with Tim/Bronte |
| White-label sales outcomes | Option 3 relevance | Ask Doug for status update |
| Mario's readiness | Deep-dive scope | Part of Option 2 deliverables |
| Doug's physical automation roadmap intersection | Option 3 inventory management scoping | Discuss during Option 3 scoping |

## Sources & References

### Origin

- **Brainstorm document:** [projects/gift-cards/docs/brainstorms/2026-02-23-advisory-engagement-strategy-brainstorm.md](../brainstorms/2026-02-23-advisory-engagement-strategy-brainstorm.md) — Key decisions carried forward: platform adoption rejected, three-tier structure, WordPress-native portal, Lloyd deep-dive as critical enabler, no explicit recommendation yet.

### Internal References

- [Client discovery call summary](../discovery/2026-01-29-client-discovery-call.md) — Advisory perspective, three options, open questions
- [Client meeting transcript](../discovery/2026-01-29-client-meeting-transcript.md) — Doug's requirements, Lloyd's workflow details, Gord's input
- [Internal pre-meeting notes](../discovery/2026-01-27-internal-pre-meeting.md) — Red Stamp team alignment
- [MVP portal research](../solutions/2026-02-23-mvp-customer-portal-research.md) — WordPress architecture, magic link auth, security requirements
- [Gift card fulfillment landscape](../solutions/2026-02-23-gift-card-fulfillment-technology-landscape.md) — Industry context, platform evaluation, security standards
- [Giftbit evaluation](../solutions/2026-02-23-giftbit-platform-evaluation.md) — Platform fit analysis (rejected)

### External References (from brainstorm research)

- [Boagworld: Discovery Phase](https://boagworld.com/digital-strategy/discovery-phase/) — Paid discovery best practices
- [Matchstick Legal: Paid Discovery for Agencies](https://matchstick.legal/blog/paid-discovery-benefits-creative-agency) — Discovery agreement structure
- [Agency Mastery 360: Landing Bigger Retainers](https://www.agencymastery360.com/insights/land-bigger-retainers) — Retainer transition timing
- [WordPress Magic Login Plugin](https://wordpress.org/plugins/magic-login/) — Passwordless authentication
- [PCI Security Standards Council](https://www.pcisecuritystandards.org/) — PCI DSS 4.0 requirements
