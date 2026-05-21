---
title: "Updated Client Recommendation — Lead With the Vault"
type: plan
category: client-recommendation
date: 2026-04-27
status: draft
tags:
  - progressive
  - recommendation
  - client-facing
  - doug
  - card-vault
  - mvp
  - revised-scope
key_insights:
  - The MVP is narrower than the March 10 proposal — secure card vault first, customer-facing portal later.
  - Friday's team meeting confirmed redemption tracking and mass distribution are technically infeasible for most vendors today; the recommendation reflects that honestly.
  - QuickBooks integration stays manual at MVP — confirmed by the team Friday — to keep the first build focused.
key_decisions:
  - Lead the next conversation with Doug on the secure card vault, not the customer portal.
  - Position Lloyd's scripts as proven workflow knowledge, not production architecture.
  - Be explicit that distribution-to-recipients and redemption tracking are bounded asks, not blanket promises.
related:
  - projects/gift-cards/docs/plans/2026-03-10-progressive-proposal-draft.md
  - projects/gift-cards/docs/plans/2026-04-23-team-brief-lloyd-scripts-next-steps.md
  - projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md
  - projects/gift-cards/docs/plans/2026-04-27-security-decision-menu.md
  - projects/gift-cards/docs/plans/2026-04-27-vendor-behavior-matrix.md
---

# Updated Client Recommendation — Lead With the Vault

**Audience:** Doug Beers (eventually); internally circulated first
**Status:** Draft v1, written to be the basis of an updated proposal — not yet a client deliverable.

## What's Changed Since the March 10 Proposal

Three things have happened since the original proposal landed:

1. **The discovery sessions on March 27 happened.** We watched Lloyd, Mario, and the physical operation end-to-end. The picture is clearer and in some ways narrower than we assumed.
2. **Lloyd shared the actual scripts on April 22.** We've now read them. They are workflow glue, not a proprietary generation engine. Replaceable, not reverse-engineerable.
3. **The internal team aligned on April 24.** The MVP narrowed from "internal fulfillment tool covering everything" to "**secure card vault** focused on the cash-equivalent surface" — with QuickBooks integration deliberately kept manual to maintain a focused first scope.

Everything below reflects that updated picture. The bones of the original three-phase proposal still hold — but the first build is sharper.

---

## What We Recommend

**Build the secure card vault first. Add the customer-facing layer on top of it later.**

The original proposal led with the order platform and the customer portal. After watching Mario, Lloyd, and the operation end-to-end on March 27 — and after spending time with the actual scripts last week — we no longer think that's the right first move.

The customer-facing pain is real. The encrypted email friction, the lack of self-service, the gap with Fundstream on delivery speed — those all matter, and they all come back. But none of them is what breaks Progressive if Mario walks out the door at the end of next month. What breaks Progressive is that one person in your office knows how to handle cash-equivalent card data, that the tooling around that data is brittle and undocumented, and that nobody — Redstamp included — can support that tooling remotely when it goes wrong.

Fix that first. Build the customer-facing layer on top of it once the foundation is solid. That sequence is what protects you against the Mario-leaves scenario, what gives Redstamp a way to actually help when something breaks, and what sets up everything else on your roadmap (food bank reporting, distribution help for clients like the one you forwarded last week, white-label vendor portals) without throwing away work to get there.

### Why "Vault" and not "Card Generation Tool"

The March 10 proposal called this a "card generation tool." After looking at the actual scripts, that framing is too narrow. Only 5 of 28 vendors require in-house card generation (Amazon, Loblaws, Shoppers, plus 1–2 others). The other 23 are inventory lookup and packaging — different work, same sensitivity.

What unifies all of it is that **cash-equivalent card data passes through.** That is what the system has to protect, audit, and give Progressive's team a reliable way to handle. Calling it a vault is more honest about what it does — and gives us a clearer way to talk to you about the security trade-offs.

---

## What's In the MVP

The first build is a focused application that does the following five things well:

1. **Order intake from the existing channels.** The web order form (Formidable Forms) and the legacy email order path keep working exactly as they do today. Elena keeps stamping invoices "PAID + R" the way she does today. Once that physical stamp happens, the vault picks the order up — Mario doesn't have to dig through Gmail and Drive folders to start. **What changes for Mario:** the trigger to fulfill is a queued order in the vault, not a stack of paper on his desk.

2. **Vendor-aware fulfillment.** Mario opens the order in the vault, and the system already knows whether this is a Tim Hortons URL pull, an Amazon PDF generation, or a Walmart just-in-time activation. It walks him through the right steps for the right merchant. **What changes for Mario:** no more switching between Lloyd's PowerShell, the Walmart portal, Inkscape, the merchant inventory spreadsheets, and the customer template — the vault stitches the steps together.

3. **Secure handling of card data.** Card numbers are cash. We treat them that way: encrypted at rest, encrypted in transit, role-based access (Mario sees what Mario needs; the future Mario-replacement gets the same scope; Doug or Danny can see audit trail without seeing card numbers), and a retention policy you sign off on before we build it. **What changes for Progressive:** if a card number leaves the system unaccounted for, you'll know. Today, you wouldn't.

4. **Customer-ready output.** The same encrypted Excel files and URL packages your customers receive today, with the same password convention they already know (invoice number minus the CPN prefix and dashes), but generated and validated by the system instead of by Mario in the last hour before delivery. **What changes for Mario:** the two emails per order — files-and-instructions, then password — are pre-staged and ready to send. He still hits send; he doesn't have to compose them.

5. **Job history.** Every order is a record: who processed it, when, what the input was, what the output was, what failed and why. **What this gives Progressive:** when a customer calls three weeks later asking about an order, the answer is in one place. When Mario leaves and someone new picks up his work, the new person inherits a system that explains itself — not Mario's tribal knowledge.

This is the MVP. Not "everything we could imagine" — the things that, in order, give your team a fulfillment operation that doesn't depend on one person's spreadsheets and one contractor's scripts.

### What's Explicitly *Not* in the MVP

We want to be straight about what the first build doesn't do, so you can decide what's most important to add next.

- **No customer portal.** Customers still receive cards by email the way they do today. The portal stays on the roadmap.
- **No QuickBooks integration.** Invoicing stays the way Mario and Elena do it today.
- **No mass distribution to individual recipients.** The system delivers to the buyer; the buyer distributes from there. (More on this below — it deserves its own section.)
- **No redemption tracking for most vendors.** This is a vendor-side limitation, not ours. (Same — see below.)
- **No SystemOne replacement.** The Amazon/Loblaws → SystemOne flow stays as-is. Mario continues to upload manually.

These are deliberate choices. Each one is a real ask, and each one is the right thing to defer to keep the first build focused.

---

## On Distribution Help and Redemption Reporting

These two come up in almost every conversation we have with you, and we expect them to come up more once the food bank and large-client side of the business keeps growing. They deserve a direct answer up front, separate from the vault, so we can talk about each one on its own terms.

**Sending cards directly to recipients on a client's behalf** — this is what the customer in your April 20 email is asking about, and what Edmonton Food Bank-type clients ask about. It is buildable. It is also a different posture for Progressive than what you do today. Today, Progressive delivers to the buyer (the food bank, the corporate office, the fundraiser); the buyer distributes from there. Sending direct-to-recipient changes who is on the hook when delivery goes wrong.

That's the part Gord is going to want to talk through, and rightly so:

- Email deliverability at hundreds or thousands of recipients per order — bounce rates, spam filtering, the messages getting blocked before they land.
- Recipient support — when someone says "I never got my card," who answers them, with what evidence?
- The provability question — if a recipient claims a card wasn't received and we can prove it was sent and opened, where does that leave Progressive legally and operationally?
- Doug's stated principle that Progressive should not become a helpdesk for end recipients — direct-to-recipient delivery puts a version of that helpdesk question right back on the table.

None of this is a "no." It's a "let's build the operating posture before we build the feature." If we sign up Progressive's first direct-to-recipient client without having that posture written down — what we deliver, what we don't, what we charge for support, what the SLA is, what the disclaimer reads — we'd be building a feature that breaks the business at the first edge case.

**Redemption reporting — telling a client which of the cards they bought have been used** — this one is mostly a vendor problem, not a Progressive problem. The vendors don't expose redemption data to third parties, except Walmart, and even Walmart is a partial manual lookup rather than a stream. We can build a redemption reporting workflow vendor-by-vendor, but it will not be a single flat feature you turn on. The vault is the foundation that makes the *good* version of this possible — once card numbers and orders live in one system, "what's the status of these 600 cards?" becomes a question we can structurally answer for the vendors who allow it. Today, that question doesn't have a place to land.

The way we'd recommend handling both: keep them on the roadmap, scope each one as its own engagement, and earn the right to expand into them through delivered results on the vault. The fastest path to credibly offering distribution help to the client you forwarded — and the food banks that will ask next — is to have the vault running first.

---

## How This Fits the Three-Phase Picture

The original three phases still hold, with the work reshuffled to reflect what we've learned:

| Phase | What It Is | What It Was in March | What Changed |
|---|---|---|---|
| **Phase 1 (mostly done)** | Discovery — Lloyd workflow capture, script review, vendor mapping | Discovery + technical spec | The on-site sessions on March 27 and the script review on April 22–23 substantially completed this. A short reproduction pass on a Redstamp machine is the remaining piece. |
| **Phase 2** | Build the secure card vault | Card generation tool | Renamed and refocused — the vault, not a tool, and built around protecting card data rather than just generating PDFs faster. Targeted to ship before Q4 holiday volume. |
| **Phase 3a** | Order platform MVP — customer accounts, 2FA, order submission, status tracking, admin backend, QuickBooks integration | Phase 3 stage 1 | Same — the natural next step once the vault is running. Replaces Formidable Forms and removes the manual QuickBooks invoicing step. |
| **Phase 3b** | Direct-to-recipient delivery, customer self-service for trusted clients, redemption reporting where vendors allow it | Phase 3 stage 2 | Pulled forward in priority because of conversations like the April 20 distribution-help client — but still after the vault and the order platform are stable. |
| **Phase 3c** | White-label vendor portals (Save-on-Foods, Sequoia) | Phase 3 stage 3 | Same — built when the vendor contracts justify it, architected for from day one. |

What changed most isn't the phase structure — it's what Phase 2 is. We've stopped describing it as "the card generation tool" because that name was too narrow. The vault is what holds your business together.

We have not committed to a fixed price for the vault yet. We need one short reproduction pass on a Redstamp machine — running Lloyd's workflow end-to-end with sanitized data — before we put a number in front of you we can stand behind. We will have that number in the next two weeks.

---

## What We Need From You

Three things, in roughly this order:

1. **Pick a security posture.** The companion document — the security decision menu — gives you three options for where card data lives. The choice shapes everything downstream. A sentence or two of direction is all we need.
2. **Confirm Lloyd can share the supporting files.** We've reviewed the scripts. We need the supporting templates, the Amazon SVG, and a sample sanitized invoice/output to reproduce the workflow on a Redstamp machine. Lloyd has been generous so far; this is a formality more than a request.
3. **Give us a half hour to walk through this.** Once you're back, we'd like to walk you through the updated picture together — with you weighing in on the trade-offs in real time rather than reading them on paper.

We are not asking for a green light on a build estimate yet. We need to reproduce the workflow before we put a number we can stand behind in front of you. We will have that number in the next two weeks.

---

## Internal Note (Not Client-Facing)

Items deliberately removed from the client-facing version of this recommendation:

- The "5 of 28" vendor breakdown — useful internally, off-topic for the client framing.
- Pricing for the vault — we don't have post-reproduction pricing yet, so the recommendation deliberately doesn't quote a number. The security menu carries the comparative pricing as a directional anchor; the proposal pricing follows.
- Detailed tech-stack discussion (Next.js vs Laravel) — Doug doesn't want to choose a stack, he wants the right answer. The team picks; we tell him.
- Explicit comparison to Fundstream — present in the original proposal, omitted here intentionally; the better positioning is "you are a service business with technology that finally matches the service" rather than re-litigating the gap with the competitor.

Calibration notes:
- Pass against `REDSTAMP-SOW-CONTEXT.md` tone guidelines — Progressive registers as **low** sophistication in CLIENT.md, which means more concrete grounding, not less. Each MVP item now includes a "what changes for Mario / for Progressive" line. Distribution and redemption sections name Gord's likely concerns explicitly because Gord is the cautious-on-liability voice in CLIENT.md.
- "Earn the right to expand the roadmap through delivered results, not promises" — the CLIENT.md scope-management direction — is now load-bearing in the distribution/reporting section.
- Phase 1 framing softened to acknowledge that the discovery work the March 25 SOW scoped has substantially happened, without claiming it was paid for under a signed agreement. The discovery SOW status in CLIENT.md is "drafted, pending execution" — be careful in any follow-up not to imply otherwise.
- "Redstamp" used throughout (one word, never "Red Stamp" in body copy per SOW-CONTEXT §1).
