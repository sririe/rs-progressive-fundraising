---
title: "Punch List — What Still Needs to Happen Before Doug's Return"
type: plan
category: internal-brief
date: 2026-04-27
status: draft
tags:
  - progressive
  - internal
  - punch-list
  - next-steps
  - doug-return
  - mario-departure
  - lloyd-scripts
key_insights:
  - The forcing function is Mario's departure, not Doug's calendar — even if Doug returns and we have nothing new, continuity capture still has to happen this week.
  - Friday's team meeting narrowed the MVP from "internal fulfillment tool" to "secure card vault" — the punch list now reflects that scope.
  - Three distinct workstreams need to move in parallel: (1) continuity, (2) build-scoping reproduction, (3) client-facing artifacts ready for Doug's return.
key_decisions:
  - Treat Mario continuity capture as Tier 1 — it cannot wait for the build conversation to resolve.
  - Move Doug's distribution-help client to a separate eval track so it doesn't drag on the main scoping work.
  - Target end-of-week: fixture request sent to Lloyd, vendor matrix v1, security menu draft, updated recommendation outline.
related:
  - projects/gift-cards/docs/plans/2026-04-23-team-brief-lloyd-scripts-next-steps.md
  - projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md
  - projects/gift-cards/docs/plans/2026-03-31-discovery-synthesis.md
  - projects/gift-cards/docs/plans/2026-04-27-vendor-behavior-matrix.md
  - projects/gift-cards/docs/plans/2026-04-27-security-decision-menu.md
  - projects/gift-cards/docs/plans/2026-04-27-updated-client-recommendation.md
  - projects/gift-cards/docs/plans/2026-04-27-lloyd-fixture-request-email.md
  - projects/gift-cards/docs/plans/2026-04-27-doug-distribution-client-response-draft.md
---

# Punch List — What Still Needs to Happen Before Doug's Return

## Where We Are Right Now

Three things converged in the last two weeks:

1. **April 22:** Lloyd sent the two Python scripts and a sample Amazon workbook. Spencer reviewed them April 23 — see `2026-04-23-lloyd-script-review-next-steps.md`. The scripts are workflow glue, not a deeply complex generation engine. They are understandable enough to replace, brittle enough that we should not wrap them.
2. **April 24 (Friday):** Internal team meeting on planning and next steps (Gemini notes captured). The team converged on a narrower MVP — a **secure card vault** rather than a full internal fulfillment tool — kept QuickBooks integration manual to maintain focused scope, and confirmed that redemption tracking and mass distribution are technically difficult for most vendors. Spencer owns drafting artifacts; Tim owns digesting the PowerShell scripts; the group owes Doug a response on the distribution-client email.
3. **Doug returns from vacation next week.** He will expect a clear path forward, a response on the client he flagged on April 20, and likely a renewed conversation about pricing.

The forcing function underneath all of this is still Mario's departure. The March 31 synthesis flagged Mario leaving in roughly a month. We are now four weeks past that synthesis. Continuity capture cannot wait for the build conversation to resolve.

## Three Workstreams in Parallel

### Workstream A — Mario Continuity (Tier 1 — Urgent)

This was flagged in the March 31 synthesis and has not visibly moved since. None of the build-side work makes Progressive operationally safer if Mario walks out the door without it being captured.

| Item | Owner | Status | Notes |
|---|---|---|---|
| Screen recordings of Mario running each fulfillment pattern end-to-end | Danny + Tim | Not started | Three recordings — Pattern 1 (vendor-provided), Pattern 2 (Amazon/Loblaws/Shoppers), Pattern 3 (Walmart). Source: `2026-03-31-discovery-synthesis.md §Recommended Next Actions §3` |
| Credential and access map | Danny | Not started | Which Google accounts, which tools, which passwords, which Drive folders |
| Failure drill | Tim or Bronte | Not started | What does Mario do when a script breaks? Who does he contact? What does the error look like? |
| Vendor runbooks (3) — written for operators, not developers | Tim (draft) → Spencer (review) | Not started | Pattern 1, Pattern 2, Pattern 3 — see synthesis §Vendor Runbooks Are Urgent |
| Supervised dry run with Mario's replacement | Danny | Blocked — no replacement identified | Worth confirming with Doug whether replacement is being recruited |
| "5th-grade reading level" training playbook | Tim or Bronte | Not started | Mario's own framing per `mario-s2-notes §Opportunities` |

**Why this is Tier 1:** If Mario leaves before this is captured, Progressive's only fallback is bringing Lloyd back into day-to-day operations — and Lloyd is not interested in resuming that role. Doug stated this on the record: *"Nobody in this office, like if Mario had to stop working tomorrow, our only alternative would bring Lloyd back."*

### Workstream B — Build-Scoping Reproduction (Tier 1 — Blocker for Pricing)

The April 23 script review surfaced that we cannot finalize build estimates until we reproduce the workflow on a Redstamp machine. The scripts are not enough on their own.

| Item | Owner | Status | Notes |
|---|---|---|---|
| Send fixture request to Lloyd | Spencer | Drafted, needs sending | See `2026-04-27-lloyd-fixture-request-email.md`. Confirms we need utilities.py, SVG template, vendor templates, sample invoice, populated Amazon Excel, known-good output, Walmart PowerShell, SystemOne requirements. |
| Confirm with Doug that Lloyd can share supporting files | Danny | Pending Doug's return | Light touch — courtesy heads-up rather than approval ask. |
| Reproduction pass — run one clean example outside Lloyd's machine | Tim or Bronte | Blocked on fixtures | Output: dependency list, folder map, known-good input/output, confirmed failure points, list of remaining gaps. |
| Vendor behavior matrix | Tim or Bronte → Spencer | Draft v1 ready | See `2026-04-27-vendor-behavior-matrix.md`. Built from script analysis; will be refined after reproduction. |
| Tim digesting PowerShell scripts (Walmart) | Tim | Friday action item | Per Gemini meeting notes — current functionality, inputs, desired outputs. |
| Internal pricing session | Spencer + Tim + Kelso | Not scheduled | Cannot finalize numbers in proposal until reproduction confirms scope. Gating factor for the updated recommendation. |

### Workstream C — Client-Facing Artifacts (Doug Returns Next Week)

These are the things Doug will want to see, in some form, when he is back. Drafts exist for the high-priority ones; refinement will happen after the team reviews.

| Item | Owner | Status | Notes |
|---|---|---|---|
| Updated client recommendation (lead with secure card vault, not portal) | Spencer | Draft v1 ready | See `2026-04-27-updated-client-recommendation.md`. Reflects Friday narrowing. |
| Security decision menu for Doug | Spencer (draft) → Tim (review) | Draft v1 ready | See `2026-04-27-security-decision-menu.md`. Local-only / web-hosted / hybrid framed as choose-your-own-adventure. |
| Email response to Doug re: distribution-help client | Spencer | Draft v1 ready | See `2026-04-27-doug-distribution-client-response-draft.md`. Confirms eval + call, asks qualifying questions, sets honest expectations re: distribution feasibility. |
| Confirm white-label status (Save-on-Foods / Sequoia) with Doug | Spencer | Pending Doug's return | Affects whether Phase 3 architecture gets airtime. Async question, low effort. |
| Updated proposal draft (replaces March 10 draft) | Spencer | Not started — depends on pricing session | Will incorporate updated recommendation, security menu, narrowed MVP, and new pricing. |

## Sequencing for the Week

This is the order I would work through them. Adjust as Tim, Danny, or Kelso push back.

**Monday April 27**
- Send Lloyd the fixture request (Workstream B — unblocks reproduction).
- Internal sync on punch list — ensure Tim and Danny have what they need for their pieces.
- Reply to Doug's distribution-help client email (Workstream C — does not need to wait for him to return).

**Tuesday–Wednesday April 28–29**
- Tim begins reproduction pass as fixtures arrive.
- Tim/Bronte produce vendor runbook v1 (Pattern 1 — vendor-provided inventory — covers ~23 merchants, fastest to draft).
- Spencer refines security decision menu after Tim's review.
- Danny coordinates Mario screen recordings.

**Thursday May 1**
- Internal pricing session — fill the [STUB] fields in the recommendation.
- Vendor matrix v2 incorporates reproduction findings.

**Friday May 2 / weekend**
- Updated proposal draft consolidates everything Doug needs to see.
- Doug returns to a tight package: refreshed recommendation, security menu, and a credible answer on the distribution-help client.

## What I'm Watching For

- **Lloyd's response time on fixtures.** If we hit Wednesday without a reply, Danny may need to nudge directly.
- **Mario's actual departure date.** The "approximately one month" figure was from late March. Has it firmed up? If he is gone in two weeks, continuity capture has to compress.
- **Doug's tolerance for the narrowed MVP.** The March 10 proposal described a card generation tool *and* a customer portal. The Friday meeting endorsed leading with the vault. Doug may push back wanting more visible customer-facing value sooner — the security menu gives him a structured place to weigh that trade-off.
- **The PowerShell script gap.** Walmart activation behavior is still unverified. Tim digesting those scripts is on the Friday action list. If they require local internet connectivity in a way that breaks the web-hosted vault assumption, the security menu logic shifts.

## Open Questions / Confirmations Needed

- Has Mario's replacement been identified? (Doug)
- Is Lloyd OK sharing the fixture package directly, or do we need to route through Doug? (Danny to confirm)
- Are Save-on-Foods and Sequoia still active conversations? (Doug)
- What is the realistic budget envelope for the secure card vault MVP? (Doug, but we can scope without a number)
- Is there an updated retainer structure on the table that we should be designing the support layer around? (Internal — Spencer/Kelso)
