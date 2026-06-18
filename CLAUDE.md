# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a multi-project knowledge work repository for the **Progressive** client. Progressive is a corporate bulk gift card fulfillment business. Redstamp (the development agency) is engaged as a long-term technology partner.

## Repository Structure

```
rs-progressive-fundraising/
├── CLAUDE.md                     # This file — repo-level agent context (always loaded)
├── CLIENT.md                     # Progressive-specific client reference (legal entity, rate, stakeholders, comms patterns) — read before any client-facing artifact
├── REDSTAMP-SOW-CONTEXT.md       # Agency-wide SOW context (engagement taxonomy, pricing, tone, templates) — read before drafting SOWs, proposals, or client recommendations
├── REDSTAMP-SOW-EXAMPLES.md      # Seven real executed SOWs as calibration anchors — match the closest example before drafting
├── .agents/
│   └── skills/
│       └── writing/
│           └── sow-drafting/     # Repo-specific skill for drafting Redstamp SOWs (reads the three files above)
├── projects/
│   └── gift-cards/               # Gift card fulfillment engagement
│       ├── docs/
│       │   ├── discovery/        # Meeting transcripts, notes, requirements gathering
│       │   ├── solutions/        # Project-specific research and evaluations
│       │   ├── plans/            # Proposals, strategy docs, implementation plans
│       │   └── brainstorms/      # Ideation and exploration output
│       └── scripts/              # Project-specific tooling (e.g., docx generators)
├── docs/
│   └── solutions/                # Repo-level compound engineering docs
│       ├── documentation-gaps/   # Cross-cutting documentation issues
│       └── workflow-issues/      # Cross-cutting workflow learnings
└── AGENTS.md
```

### Adding a New Project

Create a new directory under `projects/` following the pattern:

```
projects/<project-slug>/
├── docs/
│   ├── discovery/
│   ├── solutions/
│   ├── plans/
│   └── brainstorms/
└── scripts/                      # Optional — only if the project needs tooling
```

### Document Conventions

All documents in `docs/` use YAML frontmatter for agent discoverability:

- **`type`**: document type (discovery, solution, plan, brainstorm)
- **`category`**: sub-classification (requirements-gathering, internal-discussion, meeting-transcript, etc.)
- **`tags`**: searchable keywords for cross-referencing
- **`key_decisions`** / **`key_insights`**: extracted high-signal takeaways
- **`related`**: links to related documents in this repo (use full repo-relative paths)
- **`participants`**: who was involved, grouped by organization
- **`status`**: complete, in-progress, draft
- **`blockers`**: unresolved dependencies

When creating new documents, follow the naming pattern: `YYYY-MM-DD-descriptive-slug.md`

## Institutional Context — Read Before Client-Facing Artifacts

Before producing any client-facing artifact (recommendation, proposal, SOW, or email to Doug/Gord/Lloyd), read these files. They are not auto-loaded by every agent harness, and skipping them causes drift from agency house style and missing context (e.g., Gord's role as the cautious-on-liability voice, Progressive's low-sophistication tier requiring more concrete grounding rather than less).

- **`CLIENT.md`** — Progressive's legal entity name, rate ($150 CAD/hr), currency (CAD), Services Agreement reference (active since 2024-02-21), stakeholder profiles, and communication patterns. Includes Doug's tendency to widen scope in conversation and the explicit guidance to "earn the right to expand the roadmap through delivered results, not promises."
- **`REDSTAMP-SOW-CONTEXT.md`** — Agency-wide context: brand is "Redstamp" (one word, never "Red Stamp" in body copy), engagement taxonomy (fixed-fee / retainer / discovery / staff-aug / change-order), pricing model, tone guidelines, template structures, client sophistication signals.
- **`REDSTAMP-SOW-EXAMPLES.md`** — Seven real executed SOWs across engagement types and budget ranges. Match the closest example by engagement type, budget, and client sophistication before drafting.
- **`.agents/skills/writing/sow-drafting/SKILL.md`** — The skill that orchestrates use of the three files above for SOW drafting specifically.

The shorthand: SOW or proposal-adjacent work → read all four. Internal docs and emails → at minimum read CLIENT.md.

## Client Context

- **Doug B.** — Owner, decision-maker, open to investment but needs guidance
- **Gord S.** — Advisor, involved in sales pitches to merchants
- **Lloyd S.** — Technical contractor, built all card generation scripts, sole knowledge holder for digital fulfillment
- **Mario** — Being trained as Lloyd's backup for digital card processes
- **Redstamp team:** Spencer R. (primary contact), Tim L. (dev lead), Brontë B. (dev), Stephanie L., Danny (Director of Operations)

## Active Projects

### Gift Cards (`projects/gift-cards/`)

**Status:** Discovery complete; proposal alignment in progress. The current recommendation is **secure card vault first**, then order platform/customer portal, then service expansion modules. Primary current review artifact: `projects/gift-cards/docs/plans/2026-05-21-progressive-roadmap-review.html`.

**Core problem:** Digital gift card fulfillment is manual, fragile, and depends on specific people understanding the workflow, folder structure, scripts, merchant spreadsheets, and failure paths. Card data is cash-equivalent, and the current process does not give Progressive one clear place to track inventory, fulfillment status, generated files, delivery emails, or support history.

**Discovery status:**
- Discovery SOW is signed.
- March 27, 2026 discovery sessions with Lloyd, Mario, Doug, Danny, and Spencer are complete.
- Lloyd provided initial scripts/materials on April 22, 2026; Spencer reviewed them April 23, 2026.
- The older portal-first proposal framing has been superseded by the vault-first recommendation.

**Current proposed phases:**
- **Phase 0:** Discovery closeout and proposal alignment. Package findings, align the team, and prepare the Progressive walkthrough.
- **Phase 1:** Secure card vault. Build a secure internal system for digital gift card inventory and fulfillment: paid-order queue, digital card inventory, merchant-aware workflows, customer-ready card files and emails, order history, access rules, and file cleanup rules.
- **Phase 2:** Order platform and customer portal. Replace the current Formidable Forms pseudo-commerce flow with a proper account and ordering experience: customer accounts, order submission, order history, status/card retrieval, and Progressive admin tools. QuickBooks integration may belong here depending on effort and business-rule complexity.
- **Phase 3:** Service expansion modules. Recipient delivery service, delivery/redemption reporting where technically possible, merchant-branded portals for partnerships like Save-on-Foods or Sequoia, and separate physical-card stickering automation.

**Merchant fulfillment patterns:**
- **Merchant-provided cards:** Most merchants provide URLs, PDFs, codes, or card files. Progressive pulls inventory, prepares a customer-ready file, encrypts it, and sends it.
- **Progressive-generated PDFs:** A small group require Progressive to generate customer-facing card files from raw card data using Lloyd's scripts/templates: **Amazon and Chapters-Indigo** (plus Walmart, below). Confirmed by Doug 2026-06-16. Loblaws/Shoppers are now URL/account+PIN allocation handled as merchant-provided pull, not generation.
- **Walmart:** Unique just-in-time activation flow using Walmart's virtual gift card activation tool, PDF generation, delivery, and monthly reconciliation.

**Current proposal alignment documents:**
- `projects/gift-cards/docs/plans/2026-05-21-progressive-roadmap-review.html` — primary internal recommendation review
- `projects/gift-cards/docs/plans/2026-05-21-current-state-workflow-map.html` — current-state workflow
- `projects/gift-cards/docs/plans/2026-05-21-merchant-fulfillment-matrix.html` — merchant fulfillment patterns
- `projects/gift-cards/docs/plans/2026-05-21-security-choices.html` — security architecture choices
- `projects/gift-cards/docs/plans/2026-05-21-phase-1-mvp-boundary.html` — Phase 1 in/out scope
- `projects/gift-cards/docs/plans/2026-05-21-progressive-proposal-alignment-brief.md` — Markdown companion brief
- `projects/gift-cards/docs/plans/2026-05-21-internal-alignment-document-preferences.md` — reusable writing preferences from Spencer's feedback

**Key constraints:**
- Payment stays external via Benji Pays — no credit card processing on-site
- Card numbers are cash-equivalent — security architecture, access rules, order activity records, and cleanup rules must be explicit
- Progressive's team is non-technical — solutions must be operable without developer support
- Use "merchant" rather than "vendor" or "supplier" unless quoting older source docs
- White-label / merchant-branded portals are deferred until merchant partnerships justify the investment
- Doug wants advisory, not just execution

## Second Brain Integration

Spencer maintains a personal knowledge base (Obsidian vault) at:
`~/projects-personal/second-brain/`

When starting a session or when context seems relevant:
- Check `Ideas/redstamp-*` for Redstamp strategy and client work patterns
- Check `Logs/action-items-*.md` for open tasks that may relate to this client
- Check `Meta/project-registry.md` for the full map of all repos and vault folders

This vault is the canonical location for cross-project ideas, strategic thinking, and context that doesn't belong in any single repo.
