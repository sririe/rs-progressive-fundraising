---

## title: "Internal Solution Comparison — Card Generation Tool"
type: plan
category: internal-brief
date: 2026-03-11
status: draft
tags:
  - internal
  - pricing
  - architecture
  - card-generation
  - team-capacity
  - progressive
related:
  - projects/gift-cards/docs/plans/2026-03-10-progressive-proposal-draft.md
  - projects/gift-cards/docs/discovery/2026-03-09-internal-strategy-session.md

# Card Generation Tool — Internal Solution Comparison

For team discussion. Not client-facing.

This covers the card generation / fulfillment tool only — not the customer portal, white-label, or order matching work.

## The Problem We're Solving

Progressive's digital card generation is a manual pipeline run by one person (Lloyd) using custom scripts on a local machine. The process varies by vendor, involves sensitive card data, and can't be picked up by non-technical staff. Lloyd wants out. Mario is the designated successor. The solution needs to be simple enough that Mario — or a new hire — can run it without developer support.

## Three Approaches

### Option 1: Guided Desktop Tool (Electron)

**What it is:** A local application on their office machine. Select vendor, drop in spreadsheet, generate card URLs. Card data never leaves their network.

**Tech stack:** JavaScript, HTML/CSS, Node.js. Electron for desktop packaging. SheetJS for spreadsheet handling.

**Team comfort:** High. Web technologies the dev team already works in, deployed differently.


|                                                |               |
| ---------------------------------------------- | ------------- |
| **Build estimate (Redstamp)**                  | $8K-$15K      |
| **Build hours**                                | 80-150 hrs    |
| **Market equivalent**                          | $25K-$55K     |
| **Monthly ongoing (stabilization, Q1)**        | 8-12 hrs/mo   |
| **Monthly ongoing (steady state)**             | 3-5 hrs/mo    |
| **Monthly cost to Progressive (steady state)** | ~$500-$750/mo |


**Pros:**

- Simplest security model — no web exposure
- Fastest to V1
- Lowest ongoing cost
- Team can build and maintain confidently

**Cons:**

- Harder to support remotely when something breaks
- Tied to a physical machine
- No visibility for Redstamp into day-to-day operations
- Limited extensibility — connecting this to a portal or adding features later means rearchitecting

**Redstamp capacity impact:** Low. Minimal ongoing drain once stable.

---

### Option 2: Secure Web Application (Laravel)

**What it is:** A browser-based tool hosted in a secure environment. Same workflow as Option 1, but accessible from anywhere. Redstamp can monitor, update, and support it remotely.

**Tech stack:** Laravel (PHP), PostgreSQL, hosted on Forge/DigitalOcean or Railway. Built-in auth and encryption. Blade templates for the frontend.

**Team comfort:** Moderate. PHP is familiar from WordPress. Laravel is a step up in structure but the language is the same. The hosting and deployment patterns are new.


|                                                |                 |
| ---------------------------------------------- | --------------- |
| **Build estimate (Redstamp)**                  | $18K-$35K       |
| **Build hours**                                | 185-305 hrs     |
| **Market equivalent**                          | $55K-$120K      |
| **Monthly ongoing (stabilization, Q1)**        | 12-18 hrs/mo    |
| **Monthly ongoing (steady state)**             | 5-10 hrs/mo     |
| **Monthly cost to Progressive (steady state)** | ~$750-$1,500/mo |


**Pros:**

- Easiest to maintain and update long-term
- Redstamp has full remote access for support
- Natural path to portal integration, new vendors, additional features
- Laravel's security patterns are mature and well-documented
- AI tooling works extremely well with Laravel — extensive documentation and community patterns

**Cons:**

- Card data transits the internet — security architecture must be solid
- More upfront investment
- Hosting costs (modest — $20-50/mo for infrastructure)
- Tim's "bank site" concern applies — needs to be addressed head-on in the security design

**Redstamp capacity impact:** Moderate. Ongoing hosting management, security patches, and support. But remote access makes it efficient — no site visits needed.

---

### Option 3: Hybrid — Web Workflow + Isolated Processing

**What it is:** Web interface for order management and workflow. Actual card data processing happens in a sandboxed environment (serverless functions or containers) that spins up, generates URLs, and tears down. The web app never touches raw card numbers.

**Tech stack:** Laravel or Next.js for web layer. AWS Lambda or Cloudflare Workers for processing. API layer connecting the two. Encrypted temporary storage for card data in transit.

**Team comfort:** Low to moderate. The web layer is familiar enough (especially if Laravel). The serverless/container infrastructure is new territory for the team. Debugging failures in the processing layer requires concepts they haven't worked with.


|                                                |                   |
| ---------------------------------------------- | ----------------- |
| **Build estimate (Redstamp)**                  | $28K-$50K         |
| **Build hours**                                | 260-425 hrs       |
| **Market equivalent**                          | $80K-$170K        |
| **Monthly ongoing (stabilization, Q1)**        | 15-22 hrs/mo      |
| **Monthly ongoing (steady state)**             | 8-14 hrs/mo       |
| **Monthly cost to Progressive (steady state)** | ~$1,200-$2,000/mo |


**Pros:**

- Strongest security boundary — cleanest separation of sensitive data from the web interface
- Most extensible architecture for future growth
- Easiest to pass a formal security review if Progressive ever needs one

**Cons:**

- Most complex to build and architect
- Longest time to V1
- Highest ongoing maintenance burden
- Team would struggle to debug the infrastructure layer independently
- Overkill for current volume — this architecture is designed for scale Progressive may not reach for years

**Redstamp capacity impact:** High. Redstamp is effectively the ops team for the infrastructure layer indefinitely. This is a real ongoing commitment.

---

## Recommendation for What to Pitch


| Factor                      | Option 1 (Desktop) | Option 2 (Web App)       | Option 3 (Hybrid)            |
| --------------------------- | ------------------ | ------------------------ | ---------------------------- |
| Solves the Lloyd problem    | Yes                | Yes                      | Yes                          |
| Mario can run it            | Yes                | Yes                      | Yes, but debugging is harder |
| Team can build it           | Confidently        | With some stretch        | Significant stretch          |
| Team can maintain it        | Yes                | Yes, with learning curve | Needs Redstamp ongoing       |
| Extends to portal later     | Poorly             | Naturally                | Naturally                    |
| Monthly Redstamp commitment | 3-5 hrs            | 5-10 hrs                 | 8-14 hrs                     |
| Client monthly cost         | ~$500-750          | ~$750-1,500              | ~$1,200-2,000                |


**Option 3 is probably too much.** The security benefit is real but the ongoing capacity commitment is high, the team can't own it independently, and the architecture solves for scale Progressive doesn't need yet. It's the right answer for a company with a dedicated engineering team. Progressive isn't that company.

**Option 1 is the fastest win but the worst foundation.** It solves the immediate Lloyd problem but creates a new island — a local app that's hard to extend, hard to support remotely, and disconnected from everything else we'd build. If the plan is to eventually connect this to a customer portal, Option 1 becomes throwaway work.

**Option 2 is the sweet spot.** It solves the immediate problem, the team can build it in a stack adjacent to what they know, Redstamp can support it remotely, and it's the natural foundation for the portal and any future features. The ongoing commitment is manageable. The security concern is real but solvable with the right design — and the Lloyd session will inform exactly how card data needs to be handled.

### What to put in front of Doug

Propose Option 2 as the recommended path. Reference the market cost ($55K-$120K from a traditional firm) to anchor the value. Price the build at [TBD — needs internal pricing session]. Include the ongoing monthly support as a line item so there are no surprises.

Option 1 could be mentioned as a faster, lower-cost alternative if Doug pushes back on investment — but position it honestly as a shorter-term fix that doesn't set up the next phase.

Option 3 doesn't need to be in the proposal. It's overbuilt for where they are.

## Order Platform Re-architecture (Phase 3 in the Proposal)

Separate from the card generation tool. This replaces the Formidable Forms setup with a proper B2B order platform: customer accounts, 2FA, order submission, order history/status, admin backend, QuickBooks integration, Benji Pays workflow, white-label ready.


|                               | Traditional | Redstamp  |
| ----------------------------- | ----------- | --------- |
| **Total hours**               | 610-1,050   | 285-490   |
| **Market rate ($150-200/hr)** | $90K-$210K  | —         |
| **Redstamp**                  | —           | $30K-$60K |


**Phased internally:**


| Stage            | Scope                                                                       | Redstamp estimate |
| ---------------- | --------------------------------------------------------------------------- | ----------------- |
| MVP              | Accounts, 2FA, order submission, status, admin view, QuickBooks integration | $18K-$30K         |
| Digital delivery | Card retrieval connected to gen tool, direct-to-recipient                   | $8K-$15K          |
| White-label      | Branded vendor portals, white-label architecture                            | $8K-$18K          |


**Ongoing support (steady state):** 8-15 hrs/month (~$1,200-$2,200/mo) — higher than the card generation tool because it's customer-facing and touches payment flows.

**Stack:** Same as Phase 2 (likely Next.js). Shared codebase or shared infrastructure would reduce the combined maintenance burden. An outside consultant for initial architecture and security is worth considering here as well.

---

## Stack Note

The team has some React experience, and Spencer has successfully shipped React projects using our current development workflows. This means a **Next.js** path for Option 2 may be more practical than Laravel despite Laravel being closer to the WordPress/PHP world. Next.js also has the strongest tooling ecosystem (Vercel's own tools, extensive documentation, large community pattern library).

If we go Next.js, the main gap would be backend patterns and security architecture — not the React frontend. An **outside consultant** for the initial architecture and security setup could bridge that gap, with the team owning ongoing development and maintenance once the foundation is solid.

This changes the team comfort assessment for Option 2 from "moderate" to "moderate-high" if we go the Next.js route.

## Open Questions for Team Discussion

- Confirm React comfort level with Tim and Bronte — is it enough to maintain a Next.js app, or limited to component-level work?
- Does the dev team have any Laravel experience, or is this a full ramp-up?
- What's the realistic timeline for the Lloyd session? Can we schedule it within the next 2 weeks?
- Do we have access to Progressive's QuickBooks to pull revenue/volume numbers for the proposal?
- What's our current retainer structure with Progressive, and what would a restructured support agreement look like?
- Has Doug mentioned any budget ceiling or range in recent conversations?

