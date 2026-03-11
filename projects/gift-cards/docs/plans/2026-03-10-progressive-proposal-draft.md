---
title: "Progressive Gift Cards — Strategic Proposal (Draft)"
type: plan
category: client-proposal
date: 2026-03-10
status: draft
tags:
  - proposal
  - client-facing
  - progressive
  - portal
  - card-generation
  - advisory
  - phased-engagement
related:
  - projects/gift-cards/docs/discovery/2026-01-29-client-discovery-call.md
  - projects/gift-cards/docs/discovery/2026-01-29-client-meeting-transcript.md
  - projects/gift-cards/docs/discovery/2026-03-09-internal-strategy-session.md
  - projects/gift-cards/docs/plans/2026-03-10-internal-strategy-brief.md
---

# Progressive Gift Cards — Where We Go From Here

## How We Got Here

Progressive and Redstamp have been working together for some time now — from the original operational assessment through to the commerce integration that replaced phone, email, and fax ordering with a system built around your margins. In January, we sat down for a wide-ranging conversation about what's next. What came out of that call is what this document is built on.

## Where You Are

Three things are true about your digital business right now.

### The fulfillment process can't scale

Digital card generation runs through one person, one set of scripts, and a manual pipeline that touches spreadsheets, vendor data, file packaging, and encrypted email delivery. Loblaws cards alone take 20 seconds each to generate — a 600-card order is over three hours.

> "If you had the same number of digital card orders as you had physical, then you wouldn't be able to keep up." — Lloyd

The delivery side compounds this. Encrypted attachments trigger corporate email filters, customers lose passwords, and every failed delivery creates a support ticket. Fundstream can get a card to an end user in two seconds. The gap between that and your current process is widening.

The back-office friction is just as real. Every order that comes through Formidable Forms generates an email notification — and from there, someone has to manually create the corresponding invoice in QuickBooks. There's no sync, no automation, just a person re-entering data from one system into another. It works at current volume, but it's the kind of process that quietly breaks as the business grows.

### You're committed to change — and you need the right partner to navigate it

You've already started moving: the sticker machine for physical cards, barcode capture for inventory, merchant backend integrations on a 3-5 year horizon. You've standardized on URL-based delivery to simplify automation. Customer self-service for digital card retrieval is a top priority. Branded vendor experiences for merchants like Save-on-Foods and Sequoia represent an opportunity to expand — taking over fulfillment for stores and chains that are currently handling it themselves.

You're committed to the work and effort these organizational and operational changes require. We've been in this together since before you had an online ordering system — when every order came in by phone, email, or fax. The commerce integration we built has processed hundreds of thousands of dollars in orders through a model that fits your margins, not a generic checkout flow. That foundation got you here. Now the business has reached the point where you're ready to see what the next phase looks like and how to move forward. Your operation is one of two of its kind in Canada — there's no off-the-shelf playbook. Each step needs to build on the last so that progress compounds instead of competing for attention.

> "I want you to come back and tell me what we should be doing. From your basis of your expertise. Because I'm happy to invest in you guys to help us make this better." — Doug

### The team is ready for this to change

Lloyd has been direct about wanting his role automated. Your team understands the risk of having critical processes concentrated in one person's tooling. The willingness to move is real — what you need is someone to translate that willingness into architecture, timelines, and a plan your team can execute against.

That's what this document lays out.

---

## What We Recommend

**Solve the card generation problem first. Then rebuild the order platform on top of it.**

The instinct is to start with the customer experience — it's the most visible pain point and the thing your customers would notice immediately. But a new front door without a reliable fulfillment engine behind it is a storefront with nothing on the shelves. The generation process is the bottleneck that constrains everything else: delivery speed, staff flexibility, volume capacity, and your ability to compete with Fundstream on digital.

Digital gift card volume is growing across the industry. Your direct vendor relationships — one of only two Walmart bulk distributors in Canada — are the competitive advantage no one can replicate. But that advantage only holds if your fulfillment infrastructure can keep pace with demand. Right now, it can't.

We recommend a phased approach where each step builds on the last and delivers standalone value.

### Phase 1 — Capture what exists

Before we build anything, we need to fully understand what Lloyd has built and how it works across every vendor. This is not a discovery exercise — we know what needs to happen. It's a structured hand-off session.

Danny, our Director of Operations, leads a half-day working session with Lloyd at your office — approximately four hours, with Spencer joining remotely and a member of the technical team available as needed. The goal is complete documentation of every vendor workflow: what data comes in, what scripts run, what the output looks like, where things break, and what the edge cases are. Walmart, Amazon, Chapters, Loblaws — each one mapped step by step.

This session produces two things:

1. **Vendor runbooks** — step-by-step documentation written for operators, not developers. Detailed enough that Mario or a new hire could reference them today, even before the new tool is built.
2. **A technical specification** for the card generation tool — informed by what actually happens in practice, not assumptions.

We can also revisit the order matching work during this phase. The tooling available today makes that problem significantly more straightforward than when we first looked at it.

| | |
| --- | --- |
| **Timeline** | April 2026 |
| **Investment** | [STUB: $X — to be confirmed with team] |

### Phase 2 — Build the card generation tool

This is the core build. A secure application that replaces Lloyd's scripts with a system any trained staff member can operate.

The goal is simple: Mario selects a vendor, uploads the card data, and the system handles generation, validation, and URL output. The same process Lloyd runs today — without the spreadsheets, manual scripting, and single-point-of-failure risk.

| What changes | What it means |
| --- | --- |
| Any trained staff member can process orders | No more single-point-of-failure dependency on Lloyd |
| New hire training in under a day | The system guides the workflow, not tribal knowledge |
| New vendors added through configuration | No custom scripting project for each merchant |
| Secure handling from intake through delivery | Card data protected throughout the process |

We're confident in delivering a solution that solves this long-term. One that's built to support future growth, additional vendors, and new features as your business evolves. The mass distribution capability — sending cards directly to hundreds of individual recipients — is a natural extension that can come later. The priority is eliminating the single point of failure and building a foundation that holds.

A traditional software firm starting from scratch would scope this type of custom application at $55K-$120K. We're not starting from scratch. Redstamp already understands your business, your vendors, and your operational constraints — context that would take an outside firm weeks of billable discovery to acquire. Combined with the development infrastructure we've built internally to work efficiently at our scale, we can deliver this at a fraction of the market rate without cutting corners on security or quality.

| | |
| --- | --- |
| **Timeline** | May–September 2026 |
| **Market rate** | $55K-$120K |
| **Redstamp investment** | [STUB: $X-$X — to be confirmed with team] |

**Phase 2 is designed to ship before the holiday busy season** — the card generation tool needs to be live and stable before order volume ramps up in Q4, which means complete and in your team's hands no later than early October.

### Phase 3 — Rebuild the order platform

The Formidable Forms setup has served its purpose. It proved the model works, and hundreds of thousands of dollars in orders have moved through it. But you're processing six-figure gift card orders through a form plugin with no customer accounts, no order history, and no direct connection to your back-office systems. As order volume grows and the business matures, the platform needs to reflect that.

Your marketing site stays exactly where it is — WordPress continues to serve that purpose well, and there's no reason to disrupt it. The order platform is a separate application, purpose-built for commerce, that lives alongside the marketing site rather than being bolted onto it.

| Capability | What it replaces |
| --- | --- |
| Customer accounts with 2FA | No accounts — orders placed through an anonymous form |
| Streamlined order submission | Formidable Forms plugin handling six-figure transactions |
| Order history and status tracking | Email threads and manual follow-ups |
| Admin backend | Scattered spreadsheets and email notifications |
| Direct QuickBooks integration | Manual invoice creation from form submission emails |

Benji Pays stays in place for payment capture — the platform handles everything around the payment without taking on credit card processing or the margin compression that comes with it.

This phase is the largest investment, and we'd approach it in stages:

**Stage 1 — MVP** | Customer accounts, 2FA, order submission, status tracking, admin view, and QuickBooks integration. This replaces Formidable Forms, eliminates the manual invoice creation bottleneck, and establishes the new foundation.

**Stage 2 — Digital delivery** | Digital card retrieval connected to the generation tool, direct-to-recipient distribution. This is where the card generation tool and the order platform come together — customers retrieve cards through the platform instead of encrypted email.

**Stage 3 — White-label** | Branded vendor portals. Standing up a Save-on-Foods or Sequoia instance becomes a configuration exercise, not a rebuild. We'll architect for this from day one, but won't build it until the contracts justify it.

A traditional firm would scope a custom B2B platform of this complexity at $90K-$210K. The same advantages apply here — our existing knowledge of your operations, the shared infrastructure with the card generation tool, and efficient development workflows mean this investment will be significantly below market rate.

| Stage | Timeline | Market rate | Redstamp investment |
| --- | --- | --- | --- |
| **Stage 1** — MVP | Q4 2026–Q1 2027 | $90K-$210K (full platform) | [STUB: $X-$X — to be confirmed with team] |
| **Stage 2** — Digital delivery | Q1–Q2 2027 | (included above) | [STUB: $X-$X — scoped once MVP is live] |
| **Stage 3** — White-label | 2027, when contracts justify it | (included above) | [STUB: scoped when contracts justify it] |

---

## What This Requires

We want to be straightforward about what this engagement looks like — both the build and what comes after.

### The build

Each phase represents a discrete investment. You don't commit to everything upfront — you see the results of one phase before deciding on the next. Timelines assume an early April start and will sharpen as each phase completes. We'll firm up Phase 2 pricing after the Phase 1 session gives us full visibility into the vendor-specific complexity. Phase 3 stages are priced individually as we reach them. We don't want to guess at numbers — we want to give you ones we can stand behind.

### Ongoing support

This is the part that's easy to overlook and important to get right.

Your team does exceptional work running the business. But the reality is that a custom software solution — no matter how well built — requires ongoing technical support. Security patches, vendor format changes, bug fixes, feature requests, and day-to-day questions from staff who are learning a new process.

The support commitment will grow as the system does. After Phase 2 launches, we anticipate [STUB: X-X hours/month] for the card generation tool. Once the order platform is live, that increases to [STUB: X-X hours/month] to cover a larger surface area — customer-facing systems, QuickBooks integration, security monitoring, and day-to-day staff support. The first quarter after each launch will require heavier involvement as your team builds comfort.

This is a restructuring of our existing support arrangement, not an entirely new cost — but it will be more than what the current retainer covers, and we want that to be clear upfront.

**The alternative — building something and walking away — doesn't work for a team at your current technical capacity.** Every hour we spend supporting your operations is an hour your team isn't stuck, and that's the point.

### The growth case

[STUB — revenue/volume numbers to be confirmed]

Your digital card business currently represents approximately [X%] of total revenue. If digital order volume doubles over the next [X] years — which the industry trend suggests is conservative — the current process can't handle it. The investment in Phases 1-3 isn't just about fixing what's broken today. It's about building the infrastructure that lets the digital side of your business grow without hitting a wall.

---

## Next Steps

Two things need to happen to get this moving.

1. **Walk through this document together.** We'll schedule a call to align on priorities, answer questions, and get a quick update on the Save-on-Foods and Sequoia conversations — not because it changes Phase 1, but because it helps us architect for what's ahead.
2. **Schedule the Lloyd hand-off session.** Redstamp sends an engineer to your office in April. This is the single action that unblocks everything else — and Phase 1 is the smallest commitment with the highest information value.

---
---

# INTERNAL ONLY — Below This Line Is Not Client-Facing

Everything below is for Redstamp team discussion. Do not include in the client deliverable.

---

## Card Generation Tool — Solution Comparison

This covers the card generation / fulfillment tool only — not the order platform, white-label, or order matching work.

### The Problem We're Solving

Progressive's digital card generation is a manual pipeline run by one person (Lloyd) using custom scripts on a local machine. The process varies by vendor, involves sensitive card data, and can't be picked up by non-technical staff. Lloyd wants out. Mario is the designated successor. The solution needs to be simple enough that Mario — or a new hire — can run it without developer support.

### Three Approaches

#### Option 1: Guided Desktop Tool (Electron)

**What it is:** A local application on their office machine. Select vendor, drop in spreadsheet, generate card URLs. Card data never leaves their network.

**Tech stack:** JavaScript, HTML/CSS, Node.js. Electron for desktop packaging. SheetJS for spreadsheet handling.

**Team comfort:** High. Web technologies the dev team already works in, deployed differently.

| | |
| --- | --- |
| **Build estimate (Redstamp)** | $8K-$15K |
| **Build hours** | 80-150 hrs |
| **Market equivalent** | $25K-$55K |
| **Monthly ongoing (stabilization, Q1)** | 8-12 hrs/mo |
| **Monthly ongoing (steady state)** | 3-5 hrs/mo |
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

#### Option 2: Secure Web Application (Laravel)

**What it is:** A browser-based tool hosted in a secure environment. Same workflow as Option 1, but accessible from anywhere. Redstamp can monitor, update, and support it remotely.

**Tech stack:** Laravel (PHP), PostgreSQL, hosted on Forge/DigitalOcean or Railway. Built-in auth and encryption. Blade templates for the frontend.

**Team comfort:** Moderate. PHP is familiar from WordPress. Laravel is a step up in structure but the language is the same. The hosting and deployment patterns are new.

| | |
| --- | --- |
| **Build estimate (Redstamp)** | $18K-$35K |
| **Build hours** | 185-305 hrs |
| **Market equivalent** | $55K-$120K |
| **Monthly ongoing (stabilization, Q1)** | 12-18 hrs/mo |
| **Monthly ongoing (steady state)** | 5-10 hrs/mo |
| **Monthly cost to Progressive (steady state)** | ~$750-$1,500/mo |

**Pros:**
- Easiest to maintain and update long-term
- Redstamp has full remote access for support
- Natural path to portal integration, new vendors, additional features
- Laravel's security patterns are mature and well-documented
- Extensive documentation and community patterns for tooling support

**Cons:**
- Card data transits the internet — security architecture must be solid
- More upfront investment
- Hosting costs (modest — $20-50/mo for infrastructure)
- Tim's "bank site" concern applies — needs to be addressed head-on in the security design

**Redstamp capacity impact:** Moderate. Ongoing hosting management, security patches, and support. But remote access makes it efficient — no site visits needed.

---

#### Option 3: Hybrid — Web Workflow + Isolated Processing

**What it is:** Web interface for order management and workflow. Actual card data processing happens in a sandboxed environment (serverless functions or containers) that spins up, generates URLs, and tears down. The web app never touches raw card numbers.

**Tech stack:** Laravel or Next.js for web layer. AWS Lambda or Cloudflare Workers for processing. API layer connecting the two. Encrypted temporary storage for card data in transit.

**Team comfort:** Low to moderate. The web layer is familiar enough (especially if Laravel). The serverless/container infrastructure is new territory for the team. Debugging failures in the processing layer requires concepts they haven't worked with.

| | |
| --- | --- |
| **Build estimate (Redstamp)** | $28K-$50K |
| **Build hours** | 260-425 hrs |
| **Market equivalent** | $80K-$170K |
| **Monthly ongoing (stabilization, Q1)** | 15-22 hrs/mo |
| **Monthly ongoing (steady state)** | 8-14 hrs/mo |
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

### Recommendation for What to Pitch

| Factor | Option 1 (Desktop) | Option 2 (Web App) | Option 3 (Hybrid) |
| --- | --- | --- | --- |
| Solves the Lloyd problem | Yes | Yes | Yes |
| Mario can run it | Yes | Yes | Yes, but debugging is harder |
| Team can build it | Confidently | With some stretch | Significant stretch |
| Team can maintain it | Yes | Yes, with learning curve | Needs Redstamp ongoing |
| Extends to portal later | Poorly | Naturally | Naturally |
| Monthly Redstamp commitment | 3-5 hrs | 5-10 hrs | 8-14 hrs |
| Client monthly cost | ~$500-750 | ~$750-1,500 | ~$1,200-2,000 |

**Option 3 is probably too much.** The security benefit is real but the ongoing capacity commitment is high, the team can't own it independently, and the architecture solves for scale Progressive doesn't need yet. It's the right answer for a company with a dedicated engineering team. Progressive isn't that company.

**Option 1 is the fastest win but the worst foundation.** It solves the immediate Lloyd problem but creates a new island — a local app that's hard to extend, hard to support remotely, and disconnected from everything else we'd build. If the plan is to eventually connect this to a customer portal, Option 1 becomes throwaway work.

**Option 2 is the sweet spot.** It solves the immediate problem, the team can build it in a stack adjacent to what they know, Redstamp can support it remotely, and it's the natural foundation for the portal and any future features. The ongoing commitment is manageable. The security concern is real but solvable with the right design — and the Lloyd session will inform exactly how card data needs to be handled.

#### What to put in front of Doug

Propose Option 2 as the recommended path. Reference the market cost ($55K-$120K from a traditional firm) to anchor the value. Price the build at [TBD — needs internal pricing session]. Include the ongoing monthly support as a line item so there are no surprises.

Option 1 could be mentioned as a faster, lower-cost alternative if Doug pushes back on investment — but position it honestly as a shorter-term fix that doesn't set up the next phase.

Option 3 doesn't need to be in the proposal. It's overbuilt for where they are.

---

## Order Platform Re-architecture (Phase 3 in the Proposal)

Separate from the card generation tool. This replaces the Formidable Forms setup with a proper B2B order platform: customer accounts, 2FA, order submission, order history/status, admin backend, QuickBooks integration, Benji Pays workflow, white-label ready.

| | Traditional | Redstamp |
| --- | --- | --- |
| **Total hours** | 610-1,050 | 285-490 |
| **Market rate ($150-200/hr)** | $90K-$210K | — |
| **Redstamp** | — | $30K-$60K |

**Phased internally:**

| Stage | Scope | Redstamp estimate |
| --- | --- | --- |
| MVP | Accounts, 2FA, order submission, status, admin view, QuickBooks integration | $18K-$30K |
| Digital delivery | Card retrieval connected to gen tool, direct-to-recipient | $8K-$15K |
| White-label | Branded vendor portals, white-label architecture | $8K-$18K |

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
- **What numbers do we put in the [STUB] fields?** The proposal has placeholders for Redstamp pricing on Phase 1, Phase 2, and Phase 3 stages. These need to be filled before delivery.
