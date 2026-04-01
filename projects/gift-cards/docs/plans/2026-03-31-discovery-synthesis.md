---
title: "Discovery Synthesis — What We Learned on March 27 and What It Changes"
type: plan
category: internal-brief
date: 2026-03-31
status: draft
tags:
  - synthesis
  - discovery
  - internal
  - progressive
  - card-generation
  - digital-fulfillment
  - workflow-mapping
  - recommendation-input
key_decisions: []
related:
  - projects/gift-cards/docs/plans/2026-03-10-progressive-proposal-draft.md
  - projects/gift-cards/docs/plans/2026-03-10-internal-strategy-brief.md
  - projects/gift-cards/docs/plans/2026-03-11-internal-solution-comparison.md
  - projects/gift-cards/docs/discovery/2026-03-27-lloyd-handoff-session1-notes.md
  - projects/gift-cards/docs/discovery/2026-03-27-mario-handoff-session2-notes.md
  - projects/gift-cards/docs/discovery/2026-03-27-physical-review-session3-gemini-transcript.md
  - projects/gift-cards/docs/discovery/2026-03-27-danny-field-notes.md
---

# Discovery Synthesis — What We Learned on March 27 and What It Changes

## Purpose

This document collapses eight discovery artifacts from the March 27 working sessions into one shared picture for the Redstamp team. It is the foundation for updating the proposal, scoping the build, writing vendor runbooks, and pricing the engagement. Every team member working on deliverables should read this before they start.

### Source Key

Inline citations use short tags in brackets. All source documents are in `projects/gift-cards/docs/discovery/` unless noted otherwise.

| Tag | Document |
|---|---|
| `lloyd-s1-notes` | `2026-03-27-lloyd-handoff-session1-notes.md` — Spencer's structured notes from Lloyd's technical demo |
| `lloyd-s1-transcript` | `2026-03-27-lloyd-handoff-session1-transcript.md` — Supernormal transcript, Session 1 |
| `lloyd-s1-gemini` | `2026-03-27-lloyd-session1-gemini-transcript.md` — Gemini AI notes + transcript, Session 1 |
| `mario-s2-notes` | `2026-03-27-mario-handoff-session2-notes.md` — Spencer's structured notes from Mario's walkthrough |
| `mario-s2-transcript` | `2026-03-27-mario-handoff-session2-transcript.md` — Supernormal transcript, Session 2 |
| `mario-s2-gemini` | `2026-03-27-mario-session2-gemini-transcript.md` — Gemini AI notes + transcript, Session 2 |
| `session3-gemini` | `2026-03-27-physical-review-session3-gemini-transcript.md` — Gemini AI notes + transcript, Session 3 (physical card review) |
| `danny-field-notes` | `2026-03-27-danny-field-notes.md` — Danny's handwritten observations and questions |
| `proposal-draft` | `plans/2026-03-10-progressive-proposal-draft.md` |
| `strategy-brief` | `plans/2026-03-10-internal-strategy-brief.md` |
| `solution-comparison` | `plans/2026-03-11-internal-solution-comparison.md` |

### Methodology and Source Quality

**How provenance works in this document:** Every factual claim is followed by one or more bracketed tags (e.g., `[mario-s2-notes §Section]`) linking to the specific source document and section. Claims supported by multiple independent sources are stronger. Claims with a single source should be verified before they become proposal commitments. Where a claim rests on observation rather than verified code or data, this is called out explicitly.

**Transcript comparison — Supernormal vs Gemini:** Both tools captured the same sessions but with different strengths:

- **Supernormal** (Spencer's capture): Raw conversational transcript with speaker labels and timestamps. Higher fidelity on exact phrasing, crosstalk, and conversational dynamics. However, speaker labels are anonymized ("Speaker 2") and required manual identification. Transcription quality is uneven — some phrases are garbled or contextually wrong (e.g., "Saying the princess" instead of what Lloyd actually said). Best used for: exact quotes, conversational tone, who-said-what disputes.

- **Gemini** (Danny's capture via Google Meet): AI-structured notes with a summary, detailed bullet points, and a raw transcript below. Speaker names are resolved (Lloyd Scrubb, Danny Norton, etc.). The structured notes section is highly useful — it extracts topics, timestamps, and key points into a scannable format. However, Gemini editorializes: it synthesizes and occasionally infers intent. Best used for: topic scanning, chronological reconstruction, and cross-validation against Supernormal.

- **Session 3 (physical card review) exists only in Gemini.** Spencer's Supernormal did not capture this session. Findings from Session 3 have single-source provenance and should be verified with Danny.

- **Recommendation:** Use Supernormal as the primary record for verbatim claims and quotes. Use Gemini for structured topic extraction and gap-filling. Neither should be treated as perfectly accurate — both are AI transcriptions of a noisy in-person/remote meeting. Where possible, claims in this synthesis are cross-referenced against Spencer's structured notes, which were written contemporaneously by a human.

**Known limitations of this synthesis:**

- We have not read Lloyd's actual code. All technical claims about script behavior are based on observation and verbal description, not code review. Pricing, scoping, and stack decisions should not be finalized until Google Drive access is secured and the scripts are reviewed.
- Volume and timing estimates come from Mario and Doug's verbal reports, not system data. They are directionally correct but not precise.
- "5 of 28 merchants need in-house generation" is based on Mario's verbal estimate of the Google Drive folder structure. The actual number may differ once we can inspect the folders.

---

## What Actually Happens Today

We observed three sessions on March 27: Lloyd demonstrating the technical generation process (Session 1), Mario walking through end-to-end digital fulfillment operations (Session 2), and Danny touring the physical card handling operation (Session 3). Below is the consolidated workflow as it actually works — not as we assumed it worked from the January call.

### The Order Lifecycle

```
Customer places order (website via Formidable Forms, or legacy email order form)
    ↓
Elena receives → prints form → places hard copy on Mario's desk
    ↓
Mario creates invoice in QuickBooks (CCs himself + Doug on digital orders)
    ↓
Invoice sent to customer → Elena tracks payment
    ↓
Payment confirmed → Elena stamps "PAID" + "R" (reconciled) on hard copy
    ↓
Hard copy returns to Mario's desk → this is the trigger to fulfill
    ↓
Mario opens Google Drive (Lloyd's folder structure) → runs PowerShell script against invoice
    ↓
Script generates per-merchant folders with Excel templates
    ↓
[Merchant-specific fulfillment — see below]
    ↓
Output: encrypted Excel/ZIP or URL list per merchant
    ↓
Mario sends two emails: (1) files + invoice PDF, (2) password only
    ↓
Mario notes date/time/initials on physical invoice → Elena files it
```

**Key actors:** Elena (intake/payment), Mario (invoicing + fulfillment), Doug (inventory decisions, approvals), Lloyd (scripts/tools owner, remote support for errors). `[mario-s2-notes §Roles, Access]` `[mario-s2-gemini §Order Intake and Invoicing]`

**Key constraint we didn't fully appreciate before:** The trigger is a physical piece of paper on a desk. There is no digital queue, no status tracking, no automated handoff from payment to fulfillment. The Gmail e-card folder is Mario's personal workaround. `[mario-s2-notes §Order intake]` `[mario-s2-gemini §Payment Confirmation and Fulfillment Trigger]`

**Elena's upstream business-rule layer is more complex than it appears.** Elena doesn't just print orders — she determines discount eligibility (e.g., 3% non-profit offset that wipes out the credit card fee), handles province-specific tax calculations not captured by the order form, annotates special pricing on the printed copy for Mario, and manages payment posting/reconciliation. When Doug is away (e.g., Palm Springs), she covers his approval role. There are also trusted-client exceptions to the "nothing before payment" rule — Doug can authorize fulfillment when payment confirmation is imminent. Any workflow automation that touches invoicing or order intake must account for these rule-based decisions, not just the fulfillment mechanics downstream. `[mario-s2-notes §Invoicing specifics]` `[mario-s2-notes §Payment dependency]` `[session3-gemini §Invoice Processing and Client Discounts]`

### Three Fulfillment Patterns

We went in thinking every vendor was different. In reality, there are exactly three patterns: `[mario-s2-notes §Standard Digital Fulfillment]` `[lloyd-s1-notes §Inventory sourcing vs generation]`

#### Pattern 1: Vendor-Provided Inventory (majority of merchants)
**Merchants:** Tim Hortons, Chapters/Indigo, Esso, Petro-Canada (via Fundstream), CashStar brands, and ~23 of 28 digital merchant folders. `[mario-s2-notes §Merchants and inputs]`

The merchant provides URLs, PDFs, or challenge codes. Progressive doesn't generate anything — they pull from inventory, package into an encrypted Excel, and deliver. The work is copy/paste from inventory files into a customer-ready spreadsheet. `[lloyd-s1-notes §Invoice-to-Excel prep]` `[lloyd-s1-gemini §Manual Inventory and Fulfillment]`

**Important caveat:** "No generation" does not mean "no complexity." Each merchant has its own asset format, packaging rules, delivery format preferences, and inventory file structure. Multi-merchant orders (like the Skate Canada edge case — 15 merchants, 1-2 cards each) still require context-switching across merchant-specific spreadsheets. The tool needs to handle this long tail even though it's not PDF rendering. `[mario-s2-notes §Edge cases]` `[danny-field-notes §General Process Notes]`

**Time:** 5–10 minutes per order for simple cases. `[mario-s2-notes §Volume, Timing]`

#### Pattern 2: In-House Card Generation (5 of 28 merchants)
**Merchants:** Amazon, Loblaws, Shoppers Drug Mart, plus 1–2 others. `[mario-s2-notes §Merchants and inputs]` `[lloyd-s1-gemini §General System Operations]`

Lloyd's Python scripts + Inkscape generate card PDFs from card numbers. The output is either delivered as an encrypted ZIP or uploaded to SystemOne to produce hosted URLs. `[lloyd-s1-notes §Amazon generation flow]` `[lloyd-s1-notes §SystemOne]`

**Time:** 10–30 minutes depending on denomination count and delivery format. `[mario-s2-gemini §Walmart Fulfillment Step 1]`

#### Pattern 3: Walmart (unique exception)
**Why different:** Just-in-time issuance. No pre-purchased inventory. Progressive has direct access to Walmart's virtual GC activation system. `[mario-s2-notes §Walmart §Why different]` `[mario-s2-gemini §Walmart Fulfillment Step 2]`

**Steps:** PowerShell generates base Excel from invoice → copy/paste into Lloyd's Walmart-specific template → Walmart Virtual GC Activation tool generates card numbers + PINs → Lloyd's PDF generator creates card PDFs across denomination tabs (25/50/100/Variable) → encrypt and deliver. `[mario-s2-notes §Walmart §Steps]` `[mario-s2-gemini §Walmart Fulfillment Steps 1–3]`

**Additional obligation:** Monthly reconciliation sheet tracking first/last card numbers for every activation, used to settle with Walmart at month-end. `[mario-s2-notes §Walmart §Reliability and checks]` `[mario-s2-gemini §Internal Tracking]`

**Time:** 15–30 minutes. Same regardless of whether it's 1 card or 1,000 — every step is the same. `[mario-s2-gemini §Walmart Fulfillment Step 1]`

### The Inventory System

- **Vendor-provided merchants:** Doug/Mario do daily lookbacks against same period last year to decide what to order. Grocery (Loblaws) never more than 2 weeks out due to velocity. Other categories up to 1 month. `[lloyd-s1-notes §Process and triggers]` `[lloyd-s1-gemini §Inventory Management]`
- **Staging model:** New inventory arrives in "Mario's folder" (staging). When needed for an order, Mario moves the required denominations into the merchant's live inventory folder. Counter columns in the spreadsheets track remaining quantities. `[lloyd-s1-notes §Inventory staging]`
- **Walmart:** Purely just-in-time. No inventory to manage. Order what you need, activate, fulfill. `[mario-s2-gemini §Walmart Fulfillment Step 2]`
- **Replenishment trigger:** Large unanticipated orders require procurement before fulfillment can begin. Payment is the trigger, not the order. `[lloyd-s1-gemini §Triggering the Order Fulfillment Process]`

### The Delivery System

- **Default:** URL-based delivery (Doug has moved away from giving customers a choice) `[mario-s2-notes §Service philosophy]`
- **Exception:** Some clients still request encrypted ZIPs of PDFs `[mario-s2-notes §Walmart §Client delivery]`
- **Encryption:** Password = invoice number without "CPN" prefix or dashes (e.g., CPN-104-5415-2 → 10454152). Consistent per client. Described to customer, validated by reopening before sending. `[danny-field-notes §General Process Notes]` `[lloyd-s1-notes §Encryption practices]` `[mario-s2-gemini §Encryption Process]`
- **Email flow:** Two emails per order — (1) files + invoice PDF + instructions, (2) password only. Mario uses Gmail draft templates for both. `[mario-s2-notes §Walmart §Client delivery]` `[mario-s2-gemini §Final Steps]`
- **SystemOne:** Third-party service that converts generated card PDFs into hosted URLs. Upload ZIP containing PDFs + GiftCardLog.xlsx → export URL report → encrypt and deliver. `[lloyd-s1-notes §SystemOne]` `[lloyd-s1-gemini §Customer Delivery Format Options]`

---

## What Changed From Our Pre-Discovery Assumptions

The March 10 proposal and internal strategy brief were built on the January discovery call plus assumptions. Here's what the March 27 sessions confirmed, contradicted, or revealed:

### Confirmed

| Assumption | Status | Source |
|---|---|---|
| Lloyd dependency is the critical business risk | **Confirmed and worse than assumed** — Mario is the only person who can run fulfillment, and he's leaving in ~1 month | `mario-s2-notes §Risk to operations`, `mario-s2-gemini §Process Pain Points` |
| Card generation is manual and fragile | **Confirmed** — but the scope is smaller than we thought (5 of 28 merchants, not "every vendor") | `lloyd-s1-notes §Stability and brittleness`, `danny-field-notes §Observations`, `mario-s2-notes §Merchants and inputs` |
| Doug wants advisory, not just execution | **Confirmed on the record** — Doug stated willingness to accept risk to simplify, wants recommendations | `mario-s2-notes §Risk posture`, `mario-s2-gemini §Business Risk and Streamlining` |
| Encrypted email delivery causes friction | **Confirmed** — but Doug has already moved to default URL delivery, reducing the urgency of the portal-first approach | `mario-s2-notes §Service philosophy`, `lloyd-s1-notes §Customer delivery formats` |
| No version control on scripts | **Confirmed** — versions stored on Google Drive, changes logged in Google Calendar entries | `lloyd-s1-notes §Tooling and dependencies`, `lloyd-s1-gemini §Script Version Control` |
| Payment triggers fulfillment | **Confirmed** — physical paper stamp, no digital automation | `mario-s2-notes §Payment dependency`, `lloyd-s1-gemini §Triggering the Order Fulfillment` |

### Changed or New

| What we assumed | What's actually true | Impact on proposal | Source |
|---|---|---|---|
| "Every vendor requires custom scripting" | Only 5 of 28 merchants need in-house generation. The other 23 are copy/paste from vendor-provided inventory. | The card generation tool's scope is narrower than we estimated. Build complexity drops. | `mario-s2-notes §Merchants and inputs`, `lloyd-s1-gemini §General System Operations` |
| Walmart is similar to other merchants | Walmart is a completely unique flow with just-in-time activation, a separate Excel template, PowerShell scripts, and monthly reconciliation obligations. | Walmart needs its own dedicated module — not just another "vendor adapter." | `mario-s2-notes §Walmart`, `mario-s2-gemini §Walmart Fulfillment Steps 1–3` |
| The bottleneck is card generation speed | The bottleneck is actually the number of manual steps across the entire workflow — not generation speed per se. Mario's pain is copy/paste, email templating, and context-switching across merchants, not waiting for scripts to run. | The tool should optimize for reducing manual steps, not just speeding up PDF generation. | `mario-s2-notes §Pain Points`, `mario-s2-gemini §Workflow Pain Points`, `danny-field-notes §Observations` |
| Portal is the highest-priority customer-facing need | Doug has already defaulted to URL delivery and stopped giving customers format choices. The immediate pain is operational, not customer-facing. | This strengthens the case for "fix the engine before the storefront" — which is what the proposal already recommends, but now with stronger evidence. | `mario-s2-notes §Service philosophy`, `mario-s2-gemini §Process Pain Points and Risk` |
| Lloyd needs to be "handed off from" | Lloyd is willing and supportive, but the real risk is Mario leaving in ~1 month with no documented process. The hand-off already happened — it's just fragile. | The vendor runbooks deliverable is now urgent, not just a Phase 1 nice-to-have. | `mario-s2-notes §Risk to operations`, `lloyd-s1-gemini §General System Operations` |
| We need a Lloyd validation call to resolve technical assumptions | We got far more than a validation call — we have full workflow observation across all three patterns. | Many blockers from the internal strategy brief are answered at the observation level, but code-level verification still requires Google Drive access. | `lloyd-s1-notes` (entire session), `mario-s2-notes` (entire session), `session3-gemini` |

### Newly Discovered

| Finding | Source | Significance |
|---|---|---|
| Physical card stickering costs ~$20K/year in manual labor | `session3-gemini §Scalability and Automation Challenges` | Separate opportunity — not in current proposal scope, but Doug raised it. Level 1 automation (denomination stickers) is the ask. |
| Business grew from $13-14M pre-COVID → $25M during COVID → $30M post-COVID | `session3-gemini §Sales Volume and Business Growth` | Revenue context for the proposal. Growth driven by food insecurity groups and First Nations organizations. |
| Edmonton Food Bank: $300-400K digital last year, single denomination | `mario-s2-notes §Large client references`, `mario-s2-gemini §Business Risk and Streamlining` | Validates that large orders are simple (one merchant, one denomination). The complexity is in the long tail of small, multi-merchant orders. |
| Elena's role is more central than we knew | `mario-s2-notes §Roles, Access`, `mario-s2-gemini §Order Intake and Invoicing`, `session3-gemini §Invoice Processing and Client Discounts` | She handles intake, payment posting, discount annotation (3% non-profit offset), and covers for Doug. Any workflow automation needs to account for her role. |
| Fundstream is the benchmark competitor | `mario-s2-notes §Service philosophy`, `session3-gemini §Competitive Automation Capabilities`, `session3-gemini §Competitive Technology and Market Niche` | Doug calls them "slowest supplier" with weaker service, but acknowledges they're 10+ years ahead on technology. Progressive's moat is people/service, not tech. |
| Walmart physical activation volume is a separate problem | `lloyd-s1-gemini §Blackhawk Activation Process`, `mario-s2-gemini §Walmart Physical Card Activation` | Senior management at Walmart is pushing to end manual activations. Lloyd + Doug have a call planned with 5serve/Walmart to get first-and-last-number activation access. Not our problem to solve, but relevant context. |
| QuickBooks is the system of record for invoicing | `mario-s2-notes §Invoicing specifics`, `mario-s2-gemini §Invoicing Process in QuickBooks` | Any future integration needs to work with QuickBooks, not replace it. |
| Mario suggested self-service for micro-orders (1–3 cards) from trusted clients | `mario-s2-notes §Opportunities` | This is a tighter, more defensible first wedge than a generic "portal." Directly reduces Mario's daily burden on the long tail of small orders. |
| Doug does not want Progressive becoming end-recipient helpdesk | `mario-s2-notes §Risk posture` | Constrains any portal or reporting feature toward client-admin workflows, not recipient-facing sprawl. The user of any self-serve tool is the buyer's admin, not the card recipient. |
| Training playbook needed at "5th-grade reading level" | `mario-s2-notes §Opportunities` | Runbooks alone are not enough for Mario's replacement. The team needs screenshots, video walkthroughs, credential maps, failure drills, and a supervised dry run — not just written instructions. |
| Website order form hasn't materially reduced Elena's invoicing work | `session3-gemini §Invoice Processing and Client Discounts` | The problem is bad denomination data and rule handling, not the order channel. Old order forms with discontinued denominations still cause back-and-forth. Weakens any generic "replace Formidable, save admin time" pitch. |
| Jordan's Principle funding rule change caused ~$10M revenue dip last year | `session3-gemini §Sales Volume and Business Growth` | Federal policy changes in First Nations funding directly impact Progressive's revenue. The business is exposed to government program rule changes, not just market dynamics. |

---

## Updated Unknowns

### Resolved by March 27 Sessions

- ~~Lloyd validation call has not happened yet~~ → **Done.** Full workflow observation across all three patterns. `[lloyd-s1-notes, mario-s2-notes, session3-gemini]`
- ~~Authentication, card storage, and Amazon display constraints remain assumptions~~ → **Partially resolved.** We now know Amazon requires in-house PDF generation because Amazon provides numbers only, no URLs. Card storage is spreadsheet-based on Lloyd's Google Drive. Auth is not relevant to the current tooling. `[lloyd-s1-notes §Amazon generation flow]` `[lloyd-s1-gemini §Amazon Card Generation Script]`
- ~~Mario's actual readiness as backup~~ → **Resolved.** Mario has been solo for 2 months. He can run the process but has zero knowledge of the underlying scripts. If something breaks, he stops and messages Lloyd. `[mario-s2-notes §Roles, Access]` `[lloyd-s1-gemini §Addressing Script Errors]`
- ~~Whether the operational pain has worsened~~ → **Resolved and urgent.** Mario is leaving in ~1 month. Doug explicitly said "we can't continue to live with what we've been doing" on the digital side. `[mario-s2-transcript, ~1:49:00]` `[mario-s2-gemini §Need for Process Documentation]`

### Still Open

| Unknown | Why it matters | How to resolve | First raised |
|---|---|---|---|
| Does the Walmart activation PowerShell require internet connectivity? | Determines whether Walmart generation can be replicated in a web app or requires local execution | Ask Lloyd or test offline | `danny-field-notes §Questions` |
| Google Drive access for Redstamp | We need to see the scripts, templates, and folder structure to scope the build | Spencer emails Lloyd (cc Doug) — action item from session | `mario-s2-notes §Action Items` |
| React/Next.js comfort level for Tim and Bronte | Affects stack decision for the card generation tool | Internal team conversation | `solution-comparison` |
| Pricing for Phase 1 and Phase 2 | Proposal has [STUB] placeholders | Internal pricing session needed | `proposal-draft` |
| Current retainer structure with Progressive | Affects how ongoing support is framed | Spencer to confirm | `strategy-brief` |
| Save-on-Foods / Sequoia white-label status | Affects whether Phase 3 architecture needs to be discussed now | Quick check with Doug | `proposal-draft` |
| Exact script logic for each vendor's generation | Need to read the Python/PowerShell code to scope the build accurately | Requires Google Drive access | `lloyd-s1-notes §Scripts, Tools, and Environment` |
| Card number validation before delivery | No mechanism exists to verify cards are valid/active before sending to customer — business risk if invalid cards are delivered | Ask Lloyd re: merchant validation APIs; check Walmart balance lookup capability | `danny-field-notes §Questions` |
| SystemOne cost, contract, and API availability | Determines whether to replace, integrate, or abstract over SystemOne in the new tool | Ask Lloyd | `lloyd-s1-notes §SystemOne` |

---

## Pain Points Ranked by Business Impact

Ranked using Doug's own words and observed operational reality, not our assumptions.

### Tier 1 — Existential

1. **Single point of failure on digital fulfillment.** Mario is leaving in ~1 month. No one else in the office can do this. Lloyd is remote and not interested in resuming day-to-day operations. If Mario leaves without a replacement trained, digital fulfillment stops. `[mario-s2-notes §Risk to operations]`

   > "Nobody in this office, like if Mario had to stop working tomorrow, our only alternative would bring Lloyd back." — Doug `[mario-s2-transcript, ~1:48:00]` `[mario-s2-gemini §Need for Process Documentation]`

2. **Process can't scale with growth.** Digital volume is growing ~20%/year. At peak (Nov-Dec), Mario spends half his time on digital cards. If volume doubles, it breaks. The Skate Canada edge case (15 merchants, 1-2 cards each, 60+ minutes) shows how quickly small orders consume capacity. `[mario-s2-notes §Volume, Timing]` `[mario-s2-notes §Edge cases]`

   > "We can't live with doing what Mario's doing on the digital side if it continues to grow and grow and grow." — Doug `[mario-s2-transcript, ~1:49:00]` `[mario-s2-gemini §Need for Process Documentation]`

### Tier 2 — Operational Drag

3. **Copy/paste across spreadsheets and tools.** Mario's #1 pain point. Every order involves opening inventory files, copying card details, pasting into customer-ready templates, adding encryption, validating passwords. Same steps regardless of order size. `[mario-s2-notes §Pain Points]` `[mario-s2-gemini §Workflow Pain Points]` `[danny-field-notes §General Process Notes]`

4. **No validation before delivery.** There is no mechanism to verify that card numbers are valid or active before sending them to the customer. Mario described balance checking as "tedious" and not done card-by-card. Danny flagged this explicitly: "Is there always an assumption that the card numbers are valid?" If invalid cards are delivered, the business risk is real — these are cash-equivalent. `[danny-field-notes §Questions]` `[mario-s2-notes §Walmart §Reliability and checks]` `[danny-field-notes §Observations — "No checks or validations built into PowerShell"]`

5. **Repetitive email templating.** Two emails per order (files + password), manually composed from Gmail draft templates. The content barely changes between orders but must be customized each time. `[mario-s2-notes §Pain Points]` `[mario-s2-gemini §Final Steps and Sending]`

6. **No automated trigger from payment to fulfillment.** The "paid" trigger is a physical stamp on paper. No digital queue, no status tracking. Mario's Gmail folder is a personal workaround that wouldn't survive a personnel change. `[mario-s2-notes §Order intake]` `[mario-s2-gemini §Payment Confirmation]`

### Tier 3 — Strategic

7. **Can't help large clients with distribution or reporting.** Edmonton Food Bank ($300-400K/year) and similar clients want to know if cards were received and redeemed. Today, this is only possible for Walmart via their API. Other merchants vary. Doug sees this as the service differentiator that keeps large clients from going to Fundstream. `[mario-s2-notes §Data and integration]` `[mario-s2-gemini §Bulk Sales Definition]` `[danny-field-notes §Observations]`

8. **Physical card stickering is manual and expensive.** ~$20K/year in labor for denomination stickers. Fundstream's automated scanning/stickering system is the competitive benchmark. Doug wants Level 1 automation. Separate from digital fulfillment scope but a real opportunity. `[session3-gemini §Scalability and Automation Challenges]` `[session3-gemini §Manual Sticker Application]`

9. **No archive or folder hygiene.** Hundreds of completed order folders accumulate with no cleanup cadence. Mario navigates by visual cues (folder name length) rather than any organizational system. Annoying but not a business risk. `[mario-s2-notes §Pain Points]`

### Background Dependencies (not ranked — not in Redstamp's control)

- **Merchant API integrations stalled.** Blackhawk (Tim Hortons) and Esso integrations are tested but awaiting partner-side certification and resource assignment. Cancel operation on Blackhawk is undocumented. These are blockers Doug/Lloyd need to push, not Redstamp deliverables. Relevant to future architecture decisions but not proposal pain points. `[lloyd-s1-notes §Blackhawk]` `[lloyd-s1-notes §Esso integration]` `[lloyd-s1-gemini §Blackhawk API]` `[lloyd-s1-gemini §ESO API]`

---

## What This Means for the Deliverables

### The Proposal Needs Updating

The March 10 draft is structurally sound but needs revision in several places:

1. **Phase 1 observation is complete; verification is not.** The "capture what exists" sessions happened and produced substantial findings. However, the team has not yet reviewed the actual scripts, folder structures, or SystemOne configuration. The proposal should present Phase 1 as "observation complete, code review pending" — not fully delivered until Google Drive access is secured and the scripts are inspected. Pricing and scoping decisions based purely on verbal observation carry under-scoping risk. `[lloyd-s1-notes, mario-s2-notes, session3-gemini — all three sessions constitute Phase 1 observation]`

2. **The generation tool scope is narrower than estimated, but the packaging scope is not.** Only 5 merchants need in-house PDF generation. Walmart is a unique module. The other ~23 are inventory lookup + packaging — but each merchant has its own asset format, file structure, and delivery rules. The generation build estimate should decrease, but the packaging/automation layer still requires merchant-by-merchant handling. `[mario-s2-notes §Merchants and inputs]` `[danny-field-notes §General Process Notes]`

3. **Urgency framing should shift.** The proposal currently leads with "fulfillment can't scale." That's true, but the more immediate crisis is "Mario is leaving in a month and there's no backup." The urgency is personnel, not volume. `[mario-s2-notes §Risk to operations]`

4. **Security posture is a decision Doug needs to make, not one we should assume.** Doug expressed willingness to accept some risk to simplify. Danny's field notes frame this as "present to Doug to choose own adventure" — meaning a decision menu, not a settled answer. Card numbers are cash-equivalent. The proposal should present explicit security position options (local-only processing vs web-hosted, data retention policies, access logging, breach response) and let Doug choose, rather than treating his general openness as blanket authorization for any architecture. `[mario-s2-notes §Risk posture]` `[mario-s2-gemini §Business Risk and Streamlining]` `[danny-field-notes §Observations]`

5. **Volume numbers are now concrete.** 1–3 orders/day typical, 5–10 at peak, 5–10 minutes per order typical, 60 minutes worst case. $30M total business, digital growing ~20%/year. These replace the [STUB] fields. `[mario-s2-notes §Volume, Timing]` `[session3-gemini §Sales Volume and Business Growth]`

6. **The "portal first" vs "engine first" debate is settled.** Doug has already moved to default URL delivery. The portal is still valuable but is no longer the burning customer-facing pain. The engine (card generation tool) is the right first build. The proposal already recommends this — now we have the evidence to back it up. `[mario-s2-notes §Service philosophy]`

### Vendor Runbooks Are Urgent

Mario is leaving in ~1 month. Whether or not the card generation tool is ready, someone needs to be able to run the current process. The vendor runbooks — step-by-step documentation for each of the three fulfillment patterns — should be a near-term deliverable, not deferred.

Recommended structure:
- **Runbook 1:** Vendor-provided inventory (covers ~23 merchants — one runbook, same process)
- **Runbook 2:** In-house card generation (Amazon, Loblaws, Shoppers — Python scripts + Inkscape + SystemOne)
- **Runbook 3:** Walmart (unique flow — PowerShell + Walmart GC Activation + monthly reconciliation)

### Solution Comparison Holds, But Security Decision Is Upstream

The three-option comparison (Desktop / Web App / Hybrid) from March 11 remains valid. `[solution-comparison]` The March 27 findings provide evidence for each option, but the architecture choice depends on Doug's security decision (see Action #5):

**Evidence favoring web app (Option 2):**
- The need for remote support is acute (Mario leaving, Lloyd remote) `[mario-s2-notes §Risk to operations]`
- The web app can naturally absorb the inventory lookup pattern (Pattern 1) as a future enhancement
- We now know the generation scope is narrower (5 merchants + Walmart), reducing the attack surface `[mario-s2-notes §Merchants and inputs]`

**Evidence that should give pause:**
- Card numbers are cash-equivalent — the proposal must present an explicit security architecture, not hand-wave with "Doug is willing to accept risk"
- The current system keeps card data on local machines with no internet exposure — moving to web-hosted changes the threat model fundamentally
- Walmart activation may require local connectivity (unverified) `[danny-field-notes §Questions]`

The right framing for the proposal: present all three options with their security trade-offs and let Doug choose. `[danny-field-notes §Observations — "Security posture, risk tolerance, present to Doug to choose own adventure"]`

### New Opportunity: Self-Serve Micro-Orders

Mario explicitly suggested self-service for trusted clients placing small orders (1–3 cards). This is a tighter first wedge than a generic "portal" because it directly reduces Mario's daily burden on the long tail of simple orders without requiring Progressive to become a helpdesk for end recipients. Doug was clear: he does not want Progressive becoming first-line support for card recipients. Any self-serve feature should target the buyer's admin, not the recipient. `[mario-s2-notes §Opportunities]` `[mario-s2-notes §Risk posture]`

### New Opportunity: Physical Card Automation

Not in the current proposal scope, but Doug raised it explicitly. The stickering problem ($20K/year, Fundstream 10+ years ahead) is a separate engagement opportunity. Level 1 is just denomination sticker application. Level 2 is QR/barcode scanning tied to inventory. Level 3 is merchant integration. Worth noting in the proposal as a "we heard this too" signal. `[session3-gemini §Scalability and Automation Challenges]` `[session3-gemini §Competitive Technology and Market Niche]`

---

## Recommended Next Actions

Sequenced for risk reduction first, then deliverable production. Mario's departure (~1 month) is the forcing function.

### Immediate — This Week (Continuity + Access)

1. **Spencer: Email Lloyd (cc Doug) for Google Drive access.** This unblocks script review, which unblocks accurate build scoping. Without it, pricing and architecture decisions are based on observation, not code. Do this today.

2. **Spencer: Share this synthesis with Tim and Danny.** Get alignment on the updated picture before anyone starts writing deliverables.

3. **Team: Begin continuity capture with Mario while he's still available.** This is the most time-sensitive item. Runbooks are necessary but not sufficient — the team also needs:
   - Screen recordings of Mario running each fulfillment pattern end-to-end
   - Credential and access map (which Google accounts, which tools, which passwords)
   - A failure drill: what does Mario do when a script breaks? Who does he contact? What does the error look like?
   - A supervised dry run with Mario's replacement (once identified) before Mario leaves
   - Training materials at "5th-grade reading level" per the team's own standard `[mario-s2-notes §Opportunities]`

### Near-Term — Weeks 2-3 (Deliverable Production)

4. **Tim: Draft vendor runbooks from the session notes, transcripts, and screen recordings.** Three runbooks (see structure above). These serve double duty: Mario's replacement needs them now, and they become part of the client deliverable.

5. **Spencer: Prepare security decision menu for Doug.** Not a recommendation of one architecture — a structured choice: local-only vs web-hosted vs hybrid, each with explicit trade-offs on security posture, operational risk, support burden, and time-to-resilience. Doug can choose his own adventure. `[danny-field-notes §Observations]`

6. **Spencer: Internal pricing session.** The solution comparison has estimates but the proposal has [STUB] fields. Fill them. Stack decision (Next.js vs Laravel) depends on team comfort AND the security decision from #5.

7. **Spencer: Update the proposal draft.** Revise the March 10 draft using this synthesis. Key changes: Phase 1 observation is complete (code review pending), narrow the generation tool scope while acknowledging packaging complexity, lead with personnel urgency, add concrete volume numbers, present security as a decision menu.

### Background — Async

8. **Spencer: Confirm white-label status with Doug.** Quick async check — are Save-on-Foods and Sequoia conversations still active? This determines whether Phase 3 architecture gets airtime in the proposal.

9. **Danny: Document physical card observations.** Brain dump from Session 3 into a structured brief. This seeds a future proposal for the stickering automation opportunity.

---

## Source Documents

All discovery materials from March 27 are stored in `projects/gift-cards/docs/discovery/`:

| Document | Type | Content |
|---|---|---|
| `2026-03-27-lloyd-handoff-session1-notes.md` | Structured notes | Lloyd's technical demo — fulfillment, scripts, APIs |
| `2026-03-27-lloyd-handoff-session1-transcript.md` | Supernormal transcript | Full session 1 transcript |
| `2026-03-27-lloyd-session1-gemini-transcript.md` | Gemini notes + transcript | Danny's Gemini capture of session 1 |
| `2026-03-27-mario-handoff-session2-notes.md` | Structured notes | Mario's operational walkthrough |
| `2026-03-27-mario-handoff-session2-transcript.md` | Supernormal transcript | Full session 2 transcript |
| `2026-03-27-mario-session2-gemini-transcript.md` | Gemini notes + transcript | Danny's Gemini capture of session 2 |
| `2026-03-27-physical-review-session3-gemini-transcript.md` | Gemini notes + transcript | Physical card review — stickering, warehouse, automation |
| `2026-03-27-danny-field-notes.md` | Field notes | Danny's handwritten observations and questions |

Pre-discovery planning documents in `projects/gift-cards/docs/plans/`:

| Document | Content |
|---|---|
| `2026-03-10-progressive-proposal-draft.md` | Client-facing proposal (needs updating) |
| `2026-03-10-internal-strategy-brief.md` | Internal recommendation framework |
| `2026-03-11-internal-solution-comparison.md` | Desktop vs Web App vs Hybrid comparison |
