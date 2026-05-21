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
- **Gord S.** — Advisor, involved in sales pitches to vendors
- **Lloyd S.** — Technical contractor, built all card generation scripts, sole knowledge holder for digital fulfillment
- **Mario** — Being trained as Lloyd's backup for digital card processes
- **Redstamp team:** Spencer R. (primary contact), Tim L. (dev lead), Brontë B. (dev), Stephanie L., Danny (Director of Operations)

## Active Projects

### Gift Cards (`projects/gift-cards/`)

**Status:** Discovery/planning phase — proposal drafted, pending client walkthrough and team pricing session.

**Core problem:** Digital gift card fulfillment is manual, fragile, and bottlenecked on one contractor (Lloyd). Custom scripts handle card generation for Walmart, Amazon, Loblaws, and Chapters. A 600-card Loblaws order takes ~3+ hours (20 sec/card). If digital order volume matched physical, they couldn't keep up.

**Proposed phases:**
- **Phase 1:** Lloyd hand-off session + vendor runbooks + technical specification (April 2026)
- **Phase 2:** Card generation tool — secure web application replacing Lloyd's scripts (May–Sept 2026, ship before holiday season)
- **Phase 3:** Order platform rebuild in 3 stages — MVP with QuickBooks integration, digital card delivery, white-label architecture

**Key constraints:**
- Payment stays external via Benji Pays — no credit card processing on-site
- Card numbers are cash-equivalent — security architecture must be solid
- Progressive's team is non-technical — solutions must be operable without developer support
- White-label deferred until vendor contracts (Save-on-Foods, Sequoia) are secured
- Doug wants advisory, not just execution

## Second Brain Integration

Spencer maintains a personal knowledge base (Obsidian vault) at:
`~/projects-personal/second-brain/`

When starting a session or when context seems relevant:
- Check `Ideas/redstamp-*` for Redstamp strategy and client work patterns
- Check `Logs/action-items-*.md` for open tasks that may relate to this client
- Check `Meta/project-registry.md` for the full map of all repos and vault folders

This vault is the canonical location for cross-project ideas, strategic thinking, and context that doesn't belong in any single repo.
