---
title: "Phase 1 Proposal — Annotated Q&A Reply (Doug/Lloyd/James)"
type: discovery
category: client-correspondence
date: 2026-06-16
status: complete
participants:
  progressive:
    - Doug Beers (President — decisions)
    - Lloyd Scrubb (technical contractor / operator)
    - James (outside supporting technical counsel)
  redstamp:
    - Spencer Ririe
    - Stephanie Lamon
tags:
  - progressive
  - phase-1
  - secure-card-vault
  - requirements-gathering
  - merchant-formats
  - walmart
  - client-correspondence
key_decisions:
  - "Roles: Admin = Doug + Elena; Operations = New Hire (TBA), Lisa, Lloyd."
  - "Training/acceptance group = Doug, New Hire, Lisa, Lloyd; Elena trained later."
  - "Active digital offerings: MasterCard yes; Browns Social House no; Hudson's Bay no; Uber not now (maybe future)."
  - "In-house card generation merchants: Amazon, Walmart, Chapters-Indigo (Lloyd)."
  - "Old Loblaws 'Progressive'-branded inventory nearly depleted; stragglers converted before vault."
  - "Doug's proposed next step: call (Lloyd + Doug + Redstamp) -> Stephanie adds SOW clarifying language + support options -> finalize."
key_insights:
  - "Lloyd + James both point toward a configurable generic importer as the Phase 1 backbone, not four hardcoded merchant formats."
  - "Any brand can be delivered as URLs (password-protected Excel) OR PDFs-in-ZIP — not Amazon-only."
  - "Per-export random passwords change the customer notification practice (currently one shared password)."
related:
  - projects/gift-cards/docs/discovery/2026-06-08-private-lloyd-materials-inventory.md
  - projects/gift-cards/docs/plans/2026-05-21-progressive-proposal-alignment-brief.md
  - projects/gift-cards/docs/plans/2026-05-21-phase-1-mvp-boundary.html
blockers:
  - "redstamp.zip (Lloyd's software bundle) shared via Drive but not accessible to redstamp.com; access requested 2026-06-16."
  - "Walmart activation program deliberately withheld by Lloyd (part of materials item #5)."
---

# Phase 1 Proposal — Annotated Q&A Reply (2026-06-16)

On 2026-06-16 Doug sent two emails on the "Reschedule Needed-Phase 1 Proposal" thread:

1. **This annotated Q&A reply** (22:29:12) — Progressive's team marked up Spencer's June 11 answers inline, in color, by author.
2. **A materials forward** (22:29:26) — Lloyd's `redstamp.zip` (Drive link) + the Walmart monthly report (`WM Ecards - May2026.xlsx`). See the private source inventory for file-level detail.

This doc decodes #1. The original email's meaning is carried entirely in font color, which is lost in any
plaintext view — hence this write-up.

## Author legend (from Doug's own cover note, confirmed by Spencer)

> Doug: *"include the comments from Lloyd (Blue and Green) and James (Black)… Red font are my comments."*

| Color | Author | Voice |
|---|---|---|
| Uncolored (quoted) | **Spencer** | The original June 11 answers |
| Blue + Green/lime | **Lloyd** | The operator currently doing the work — concrete, format-level |
| Black | **James** | Outside supporting technical counsel — strategic/architectural |
| Red / maroon | **Doug** | Decisions |

Note: Doug wrote his own cover note in blue and his inline decisions in red, so color is not a perfect 1:1
with author — use the legend plus context. Spencer confirmed the two strategic black comments
(general-vs-targeted system; merchant-data homogeneity) read as James, the outside counsel.

## Doug's decisions (red) — lockable

- **Roles:** Admin = Doug + Elena. Operations = New Hire (TBA), Lisa, Lloyd.
- **Training / acceptance group:** Doug, New Hire, Lisa, Lloyd; Elena trained when needed.
- **Active digital offerings:** MasterCard — yes. Browns Social House — no. Hudson's Bay — no. Uber — not now, possibly future.
- **Old "Progressive"-branded Loblaws inventory:** almost depleted; assumed used up before the project; any stragglers converted before entering the vault.
- **Manual Walmart activated-results import acceptable for v1?** — *"Still to be discussed."* (open)

## Lloyd (blue/green) — operator input, highest scope signal

- **Delivery format is per-brand-flexible:** any brand can be sent as URLs (password-protected Excel) **or** PDFs-in-ZIP. Applies to Loblaws/Shoppers/Walmart and Chapters-Indigo, not just Amazon.
- **Most merchants are pass-through:** import → drop valueless columns → password-protect → send. Argues adding such merchants **should not require a software change** — i.e., Phase 1 should let staff specify which imported fields carry to the customer export. Only **Amazon, Walmart, Chapters-Indigo** are true card-generation cases.
- **Data is inhomogeneous by *supplier*, not merchant:** suppliers (Cashstar/Blackhawk, etc.) deliver homogeneous groups, so targeting one merchant tends to cover its supplier family.
- **Format breaks only on submission-format change** → a mapping concern that could be designed into Phase 1.
- **Per-export random passwords** differ from the current single-shared-password practice → changes the customer notification email/method.
- **Supplier change to Fundstream** means Petro-Canada can no longer be sent as PDFs-in-ZIP.

## James (black) — outside counsel, strategic framing (directed at Doug/Lloyd, not us)

- Agrees with Lloyd in general, but asks Doug whether Phase 1 intends a **general system** or **targeted merchants** — notes generality is a function of how many merchants share Amazon/Loblaws/Walmart import structure.
- Asks Lloyd how inhomogeneous the merchant data is, and whether targeting Walmart already yields infrastructure for Amazon etc. — floats using that to **justify a broader Phase 1 merchant target**.

Treat these as Progressive's internal deliberation, not action items. But note: their own advisor is
advocating broader Phase 1 generality — alignment with Lloyd's pass-through point and an opening for the SOW.

## Open questions directed at Redstamp (need answers for the call / SOW)

1. **Doug:** if a stray old "Progressive"-branded card is missed (only visible by opening individual cards), what happens when it reaches the vault / customer?
2. **Lloyd:** where is the vault / fulfillment app hosted? (security + backup / data-loss — James seconded the importance)
3. **Lloyd:** "What is a 'banner brand'?" (terminology used in Spencer's answer)
4. **Lloyd:** "Is this SystemBind?" — reconcile against our "SystemOne" naming for the URL upload system.

## Confirmations still open

- Manual Walmart import acceptable for v1 (Doug: "still to be discussed").
- Which Loblaws banner brands share one format (term needs defining for Lloyd first).

## Next step (Doug, explicit)

Call with Lloyd + Doug + Redstamp team → Spencer + Stephanie add clarifying language to the SOW and
options for ongoing support → finalize the agreement.
