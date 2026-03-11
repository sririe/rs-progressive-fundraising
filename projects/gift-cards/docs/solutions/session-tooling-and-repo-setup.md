---
title: "Repository Setup and Tooling Decisions"
type: solution
category: tooling
date: 2026-02-23
tags: [compound-engineering, repo-structure, yaml-frontmatter, cursor, claude-code, bun]
problem_type: project-setup
resolved: true
---

# Repository Setup and Tooling Decisions

## What was done

- Reorganized flat file structure into compound engineering conventions (`projects/gift-cards/docs/discovery/`, `docs/solutions/`, `projects/gift-cards/docs/plans/`, `projects/gift-cards/docs/brainstorms/`, `todos/`)
- Added YAML frontmatter to all three discovery documents with structured metadata (participants, tags, key_decisions, key_insights, related docs, blockers)
- Created CLAUDE.md with project context, business domain knowledge, and document conventions
- Installed compound engineering plugin (v2.35.2) for Claude Code
- Installed bun (v1.3.9) via Homebrew as a dependency

## Key decisions

- **Compound engineering adapted for knowledge work**: No codebase exists yet, so the plugin's value is in the `/compound` workflow — capturing meeting insights as tagged, searchable docs in `docs/solutions/`
- **YAML frontmatter schema**: Settled on `type`, `category`, `date`, `tags`, `participants`, `key_decisions`/`key_insights`, `related`, `blockers`, `status` as the standard fields
- **File naming**: `YYYY-MM-DD-descriptive-slug.md` for chronological sorting

## Discovered limitations

- **Compound engineering plugin has no Cursor target** — `--to cursor` is in the help text but not implemented in the targets registry (v0.1.0 of the CLI). Closest workaround is `--to copilot` then manually adapting `.github/` output to `.cursor/rules/*.mdc`
- **Plugin CLI requires bun** — `npx` can download the package but the entrypoint calls `env bun`, so bun must be installed as a runtime

## Session-level context not captured elsewhere

- Doug wants Red Stamp in an advisory role, not just execution — this shapes how recommendations and plans should be framed
- The "faux commerce" pattern (order capture without on-site payment) is unusual and means standard e-commerce platforms (WooCommerce, Square, Shopify) are a poor fit
- Tim's WordPress custom post type idea for white-label MVP was the team's consensus pragmatic starting point
- Lloyd's generation scripts are the single biggest operational risk — this should be the focus of the Danny/Lloyd technical deep-dive
