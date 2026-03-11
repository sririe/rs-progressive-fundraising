# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Project Overview

This is a knowledge work repository for the **Progressive Gift Cards** client engagement. Progressive is a corporate bulk gift card fulfillment business. Red Stamp (the development agency) is engaged as a long-term technology partner.

**Status:** Discovery/planning phase — no codebase yet.

## Repository Structure

This project follows [compound engineering](https://github.com/EveryInc/compound-engineering-plugin) conventions adapted for knowledge work:

```
progressive-fundraising/
├── AGENTS.md                  # This file — agent context (always loaded)
├── docs/
│   ├── discovery/             # Meeting transcripts, notes, requirements gathering
│   ├── solutions/             # Categorized knowledge base (compounded learnings)
│   ├── plans/                 # Implementation plans and proposals
│   └── brainstorms/           # Ideation and exploration output
└── todos/                     # Actionable tasks and follow-ups
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

When creating new documents, follow the naming pattern: `YYYY-MM-DD-descriptive-slug.md`

## Key Business Context

**Core problem:** Digital gift card fulfillment is manual, fragile, and bottlenecked on one contractor (Lloyd). Custom scripts handle card generation for Walmart, Amazon, Loblaws, and Chapters. A 600-card Loblaws order takes ~3+ hours (20 sec/card). If digital order volume matched physical, they couldn't keep up.

**Current tech stack:** WordPress + Formidable Forms (website), BenjaPay (payment processing, external to site), email-based encrypted delivery, Google Docs/spreadsheets for inventory.

**Vendor card types:**
- **Pass-through:** Best Buy, Starbucks — just forward URLs
- **Generate from data:** Walmart, Amazon, Chapters, some Loblaws — receive card numbers + PINs, generate PDFs via custom scripts
- **Integrated APIs:** Tim Hortons (via Cash Star), Amazon and Walmart integrations in progress

## Proposed Solution Phases

**Phase 1 (MVP):** Customer portal for digital card retrieval
- Keep existing ordering flow (no login required to order)
- Add account creation link in invoice (post-order, as Tim suggested)
- Customers log in to retrieve pre-generated cards
- Lloyd/Mario still manually generate and upload cards to portal
- No payment processing on the site (stays with BenjaPay)

**Phase 2:** White-label portals for bulk clients (Save-on-Foods, Sequoia Group, White Spot)
- Three tiers: direct link to Progressive site → single-brand portal → fully branded white-label
- Architecturally different from Phase 1 — likely WordPress custom post types or a full rebuild
- Contingent on Progressive winning these contracts

**Phase 3:** Operational automation
- Streamline Lloyd's card generation scripts into a user-friendly internal tool
- Reduce knowledge concentration risk (bus factor)
- Longer-term: direct merchant backend integrations (3-5 year horizon)

## Key Constraints and Decisions

- **No credit card storage on the site** — payment stays external via BenjaPay to avoid PCI compliance burden and margin erosion
- **Security around card numbers** — Tim flagged risk of storing unsold inventory on web infrastructure; gift card numbers are like cash
- **Progressive's team is non-technical** — solutions must be maintainable by staff; Doug, Gord, and most employees are not developers
- **White-label timing is uncertain** — avoid investing in Tier 3 architecture until contracts are secured; don't create technical debt that blocks it later
- **URLs preferred over PDFs** — Doug agreed to standardize on URL delivery to simplify automation
- **Doug wants advisory, not just execution** — explicitly asked Red Stamp to recommend what they *should* do

## People

- **Doug B.** — Owner, decision-maker, open to investment but needs guidance
- **Gord S.** — Advisor, involved in sales pitches to vendors
- **Lloyd S.** — Technical contractor, built all card generation scripts, sole knowledge holder for digital fulfillment
- **Mario** — Being trained as Lloyd's backup for digital card processes
- **Red Stamp team:** Spencer R. (primary contact), Tim L. (dev lead), Brontë B. (dev), Stephanie L., Danny (AI/automation)

## Open Questions

- Technical deep-dive with Lloyd needed — Danny/Spencer to walk through card generation workflow
- Validate whether Mario can realistically take over Lloyd's processes with better tooling
- Confirm whether white-label sales (Save-on-Foods, Sequoia, White Spot) are actively progressing
- "Front Street" mentioned re: Amazon card display time limits — unclear if vendor or contact
- Two-factor authentication for portal access flagged by Lloyd as important
