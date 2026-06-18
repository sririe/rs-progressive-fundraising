---
repo_type: knowledge
landing: ship
private_paths:
  - projects/gift-cards/_private/
---

# AGENTS.md

> **This repository is agent- and lineage-agnostic.** `AGENTS.md` is the single source of truth.
> `CLAUDE.md`, `.cursorrules`, and any other agent-named file are thin shims that point here —
> **never add project content to them; edit this file.** Lineage-specific config directories
> (`.claude/`, `.codex/`, `.cursor/`) are gitignored and must not be committed.

This file is the canonical guidance for any agent or person working in this repository.

> **Session start:** confirm `repo_type` / `landing` above → read `docs/status/current.md` for current focus, in-flight work, and next steps.
> **Session end:** update `current.md`; on `landing: ship` repos commit + push durable docs unless Spencer said "park" (Aurora `wrapup` skill, where installed).

## Project Overview

This is a knowledge work repository for the **Progressive Gift Cards** client engagement. Progressive is a corporate bulk gift card fulfillment business. Redstamp is engaged as a long-term technology partner.

**Status:** Discovery is complete and the team is in proposal alignment. The current recommendation is **secure card vault first**, then order platform/customer portal, then service expansion modules.

## Repository Structure

This repo now uses a multi-project structure:

```
rs-progressive-fundraising/
├── AGENTS.md
├── CLAUDE.md
├── CLIENT.md
├── REDSTAMP-SOW-CONTEXT.md
├── REDSTAMP-SOW-EXAMPLES.md
├── projects/
│   └── gift-cards/
│       ├── docs/
│       │   ├── discovery/
│       │   ├── solutions/
│       │   ├── plans/
│       │   └── brainstorms/
│       └── scripts/
└── docs/
    └── solutions/
```

### Document Conventions

All documents in `docs/` use YAML frontmatter for agent discoverability:

- **`type`**: document type (discovery, solution, plan, brainstorm)
- **`category`**: sub-classification (requirements-gathering, internal-discussion, meeting-transcript, etc.)
- **`tags`**: searchable keywords for cross-referencing
- **`key_decisions`** / **`key_insights`**: extracted high-signal takeaways
- **`related`**: links to related documents in this repo
- **`participants`**: who was involved, grouped by organization
- **`status`**: complete, in-progress, draft
- **`blockers`**: unresolved dependencies

When creating new documents, follow the naming pattern: `YYYY-MM-DD-descriptive-slug.md`.

For HTML review documents, keep the language concrete, team-shareable, and grounded in Progressive's discovery vocabulary. Avoid vague strategy terms such as "spine," "artifact," "decision gates," "output package," "retention," "audit history," and "governed workflow" unless they are explained in plain operational language.

## Institutional Context — Read Before Client-Facing Artifacts

Before producing any client-facing artifact (recommendation, proposal, SOW, or email to Doug/Gord/Lloyd), read:
- **`CLIENT.md`** — Progressive's legal entity, rate ($150 CAD/hr), currency, Services Agreement, stakeholder profiles, communication patterns.
- **`REDSTAMP-SOW-CONTEXT.md`** — agency-wide SOW context (engagement taxonomy, pricing, tone, templates; "Redstamp" is one word).
- **`REDSTAMP-SOW-EXAMPLES.md`** — seven executed SOWs; match the closest before drafting.
- **`.agents/skills/writing/sow-drafting/SKILL.md`** — orchestrates the three files above for SOW drafting.

Cross-project context (operator's second brain): `~/projects-personal/second-brain/` — `Ideas/redstamp-*`, `Logs/action-items-*.md`, `Meta/project-registry.md`.

## Key Business Context

**Core problem:** Digital gift card fulfillment is manual, fragile, and depends on specific people understanding the workflow, folder structure, scripts, merchant spreadsheets, and failure paths. Card data is cash-equivalent, and the current process does not give Progressive one clear place to track inventory, fulfillment status, generated files, delivery emails, or support history.

**Current tech stack:** WordPress + Formidable Forms pseudo-commerce flow, Benji Pays (payment processing, external to site), QuickBooks for invoicing, Google Drive/spreadsheets for digital inventory, Lloyd's Python/PowerShell scripts, Inkscape/PDF generation for some merchants, SystemOne for hosted URLs, Gmail for encrypted delivery.

**Merchant fulfillment patterns:**
- **Merchant-provided cards:** Most merchants provide URLs, PDFs, codes, or card files. Progressive pulls inventory, prepares a customer-ready file, encrypts it, and sends it.
- **Progressive-generated PDFs:** A small group require Progressive to generate customer-facing card files from raw card data using Lloyd's scripts/templates: **Amazon and Chapters-Indigo** (plus Walmart, below). Confirmed by Doug 2026-06-16. Loblaws/Shoppers are now URL/account+PIN allocation handled as merchant-provided pull, not generation.
- **Walmart:** Unique just-in-time activation flow using Walmart's virtual gift card activation tool, PDF generation, delivery, and monthly reconciliation.

## Current Recommendation

**Phase 0:** Discovery closeout and proposal alignment
- Discovery SOW is signed.
- March 27, 2026 discovery sessions are complete.
- Lloyd provided initial script/materials on April 22, 2026; Spencer reviewed them April 23, 2026.
- Current internal alignment artifacts live in `projects/gift-cards/docs/plans/`.

**Phase 1:** Secure card vault
- Build a secure internal system for digital gift card inventory and fulfillment.
- Include paid-order queue, digital card inventory, merchant-aware workflows, customer-ready card files and emails, order history, access rules, and file cleanup rules.
- Keep Formidable Forms, QuickBooks integration, customer portal, direct recipient delivery, redemption reporting, SystemOne replacement, and white-label portals out of the first build unless the team deliberately changes scope.

**Phase 2:** Order platform and customer portal
- Replace the current Formidable Forms pseudo-commerce flow with a proper account and ordering experience.
- Include customer accounts, order submission, order history, status/card retrieval, and Progressive admin tools.
- QuickBooks integration may belong here depending on effort and business-rule complexity.

**Phase 3:** Service expansion modules
- Recipient delivery service: Progressive sends digital gift cards directly to a buyer's recipient list instead of giving the buyer one package to distribute.
- Delivery and redemption reporting where technically possible and where merchants expose the required data.
- Merchant-branded portals for partnerships such as Save-on-Foods or Sequoia.
- Physical card stickering automation remains a separate future opportunity.

## Important Current Documents

- `projects/gift-cards/docs/plans/2026-05-21-progressive-roadmap-review.html` — primary internal recommendation review
- `projects/gift-cards/docs/plans/2026-05-21-current-state-workflow-map.html` — current-state workflow
- `projects/gift-cards/docs/plans/2026-05-21-merchant-fulfillment-matrix.html` — merchant fulfillment patterns
- `projects/gift-cards/docs/plans/2026-05-21-security-choices.html` — security architecture choices
- `projects/gift-cards/docs/plans/2026-05-21-phase-1-mvp-boundary.html` — Phase 1 in/out scope
- `projects/gift-cards/docs/plans/2026-05-21-progressive-proposal-alignment-brief.md` — Markdown companion brief
- `projects/gift-cards/docs/plans/2026-03-31-discovery-synthesis.md` — deep discovery synthesis
- `projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md` — technical script review
- `projects/gift-cards/docs/plans/2026-04-27-updated-client-recommendation.md` — prior prose recommendation draft

## Key Constraints and Decisions

- **Payment stays external** via Benji Pays; do not propose storing or processing credit cards on Progressive's site.
- **Card numbers are cash-equivalent**; security architecture, access rules, order activity records, and cleanup rules must be explicit.
- **Progressive's team is non-technical**; solutions must be operable by staff without developer support.
- **Merchant terminology matters**; use "merchant" rather than "vendor" or "supplier" unless quoting older source docs.
- **White-label timing is uncertain**; keep merchant-branded portals as roadmap work until partnerships justify the investment.
- **Doug wants advisory, not just execution**; Redstamp should recommend what Progressive should do, not just list options.
- **Use concrete language**; Progressive has low internal technical sophistication, so explain workflow changes through observable operational details.

## People

- **Doug B.** — Owner, decision-maker, open to investment but needs guidance
- **Gord S.** — Advisor, cautious voice on scope, liability, and recipient-delivery support posture
- **Lloyd S.** — Technical contractor, built the scripts and shared initial technical materials
- **Mario** — Runs digital fulfillment day-to-day but depends on Lloyd when scripts or edge cases break
- **Elena** — Intake/payment/reconciliation/business-rule layer; central to order and invoice flow
- **Redstamp team:** Spencer R. (primary contact), Tim L. (dev lead), Brontë B. (dev), Stephanie L., Danny (Director of Operations)

## Open Questions

- What exact Phase 1 scope and pricing should Redstamp propose?
- How much of Walmart activation/reconciliation belongs in V1 versus remaining manual?
- Which merchant templates and inventory formats are consistent enough to model in the first build?
- What security posture should Progressive choose: local-only, secure web vault, or hybrid?
- What is the current status of Save-on-Foods, Sequoia, and other merchant-branded portal opportunities?
- Does SystemOne have API or integration options, or should it remain manual in V1?
