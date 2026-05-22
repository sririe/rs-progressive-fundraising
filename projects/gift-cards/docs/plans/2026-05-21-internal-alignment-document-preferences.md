---
title: "Internal Alignment Document Preferences"
type: plan
category: working-notes
date: 2026-05-21
status: draft
tags:
  - writing-preferences
  - internal-alignment
  - strategy-docs
  - reusable-guidance
key_insights:
  - Internal alignment documents should sound shareable with the whole team, not addressed to a named subset unless names are operationally required.
  - Language should stay rooted in the client's discovery vocabulary and concrete workflow details.
  - Avoid LLM-coded strategy words that Spencer does not naturally use.
related:
  - projects/gift-cards/docs/plans/2026-05-21-progressive-roadmap-review.html
  - projects/gift-cards/docs/plans/2026-05-21-progressive-proposal-alignment-brief.md
---

# Internal Alignment Document Preferences

These notes capture reusable feedback from reviewing the Progressive internal alignment document. They are project-agnostic and should be considered candidate source material for a future writing skill or reference document.

## Naming And Framing

- Do not label the document an "artifact" inside the document. The format is obvious; call it an internal alignment document, recommendation review, roadmap review, working brief, or team review.
- Avoid "spine" in project documents. It reads like LLM language and does not match Spencer's natural project vocabulary.
- Better title patterns:
  - "[Client] Recommendation Review"
  - "[Client] Proposal Alignment"
  - "[Client] Roadmap Review"
  - "[Client] Direction Review"
  - "[Client] Internal Alignment"

## Audience

- Draft internal documents so they can be shared with the broader team.
- Do not name specific internal people in the purpose statement unless the document is truly for those people only.
- Prefer "bring the team current," "align on implementation shape," or "prepare the client walkthrough" over "get [person] up to speed."

## Recommendation Language

- Give the recommendation more setup when there are many moving pieces.
- Explain why the recommendation is the best first move, not just what it is.
- A strong recommendation should say:
  - what risk or gap it solves
  - why it can stand alone
  - what external dependencies it avoids
  - what future work it sets up

## Concrete Over Abstract

- Root language in discovery terms and observed workflow details.
- Avoid thin phrases like "output package," "governed workflow," "audit history," and "retention" unless immediately explained in plain operational terms.
- Prefer concrete replacements:
  - "customer-ready card files and delivery emails" instead of "output packages"
  - "how long files stay in the system" or "cleanup rules" instead of "retention"
  - "who processed an order, what was created, what was sent, and what failed" instead of "audit history"
  - "merchant-specific steps" instead of "vendor behavior" when that matches the client context

## Specificity

- If a metric like "5 of 28" appears, explain what the denominator means and how confident we are.
- If a label like "fulfillment patterns" appears, define the patterns in client/workflow language.
- Avoid single-number cards that flatten complex risk. For example, "1 critical dependency" may imply only one risk when the real issue is process knowledge concentrated in specific people.

## Client Vocabulary

- Check the client's own language and website language before defaulting to generic terms.
- For Progressive, use "merchant" as the default term. The public site uses "gift card merchants," and that is closer to the client's vocabulary than "vendor" or "supplier."
