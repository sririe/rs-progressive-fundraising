---
module: System
date: 2026-03-02
problem_type: workflow_issue
component: tooling
symptoms:
  - "Claude Code does not recognize 'push to Proof' across projects — requires explanation dialog each session"
  - "Proof hooks are global but Claude's knowledge of Proof resets per conversation"
root_cause: incomplete_setup
resolution_type: tooling_addition
severity: medium
tags: [proof, global-config, claude-code, cross-project, slash-command]
---

# Troubleshooting: Proof Integration Not Discoverable Across Projects

## Problem

Claude Code didn't know what "Proof" (ProofEditor.ai) meant when asked to "push to Proof" in a project, despite Proof hooks already being configured globally in `~/.claude/settings.json`. Each new project conversation required a full explanation dialog.

## Environment

* Module: System (cross-project tooling)

* Affected Component: Claude Code global configuration

* Date: 2026-03-02

## Symptoms

* Asking Claude to "push to Proof" triggered a clarification question ("What is Proof?")

* The Proof pre/post write hooks in `~/.claude/settings.json` worked fine — but only for auto-opening files on write/edit

* No mechanism existed for Claude to know what Proof is, how to interact with it, or what "push to Proof" means

* The problem repeated in every new project context

## What Didn't Work

**Direct solution:** The problem was identified and fixed on the first attempt after the user flagged it.

## Solution

Created two global configuration files:

**1.** **`~/.claude/CLAUDE.md`** **— Global context (loaded in every project)**

Explains what Proof is, documents both interaction modes (native Mac app vs. web fallback), the detection logic, API endpoints, and terminology mapping ("push to Proof" = open in available mode).

```markdown
# Key sections:
- Mac (native app installed): `open -a Proof "<file_path>"`
- Windows/Web (no native app): open browser to proofeditor.ai
- Detection logic: curl localhost:9847/windows to check native availability
- Web API: /api/agent/{slug}/state, /edit, /ops, /presence with x-share-token auth
```

**2.** **`~/.claude/commands/proof.md`** **— Global slash command**

Provides `/proof <file>` across all projects. Resolves file descriptions to paths, detects which Proof mode is available, and opens accordingly.

## Why This Works

1. **Root cause:** Claude Code hooks (`PreToolUse`/`PostToolUse`) handle the *mechanical* integration (provenance tracking, auto-open on write). But Claude's *semantic* understanding of what Proof is had no persistence mechanism across projects.
2. **`~/.claude/CLAUDE.md`** is loaded into every conversation context regardless of project, so Claude always knows what Proof is and how to interact with it.
3. **`~/.claude/commands/proof.md`** gives a discoverable entry point (`/proof`) that doesn't require natural language explanation.
4. **Cross-platform handling:** Detection via localhost API check means the same config works on Mac (native app) and Windows (browser fallback) without platform-specific configuration.<span data-proof="suggestion" data-id="m1772489664844_2" data-by="ai:claude" data-kind="insert">
   Missed Signal
   During this session, the Proof web API was shared via a brainstorm document (https://www.proofeditor.ai/d/2s33mm8l) that explicitly discussed building global infrastructure — including a global CLAUDE.md. The document was about the system for cross-project discoverability, yet the follow-on work (setting up Proof's own discoverability) didn't fully connect to that higher-level framing.
   The learning: When a shared artifact describes a repeatable system, the work that follows should be evaluated at the system's altitude, not just the immediate task's. We solved "make Proof discoverable" but should have been thinking "what's the pattern for making any tool discoverable" from the start.</span>

## Prevention

* <span data-proof="suggestion" data-id="m1772489664832_1" data-by="ai:claude" data-kind="replace">When adding new tool integrations to Claude Code via hooks, always pair the hook with a global CLAUDE.md entry explaining the tool's purpose and interaction patterns</span>

* <span data-proof="suggestion" data-id="m1772489664832_1" data-by="ai:claude" data-kind="replace">Hooks handle mechanics; CLAUDE.md handles semantics — both are needed for full integration</span>

* <span data-proof="suggestion" data-id="m1772489664832_1" data-by="ai:claude" data-kind="replace">Global slash commands (`~/.claude/commands/`) provide discoverable entry points that don't depend on Claude inferring intent from natural language</span>

## Related Issues

No related issues documented yet.

<!-- PROOF
{
  "version": 2,
  "marks": {
    "m1772489664844_2": {
      "kind": "insert",
      "by": "ai:claude",
      "createdAt": "2026-03-02T22:14:24.844Z",
      "range": {
        "from": 2943,
        "to": 3649
      },
      "content": "\nMissed Signal\nDuring this session, the Proof web API was shared via a brainstorm document (https://www.proofeditor.ai/d/2s33mm8l) that explicitly discussed building global infrastructure — including a global CLAUDE.md. The document was about the system for cross-project discoverability, yet the follow-on work (setting up Proof's own discoverability) didn't fully connect to that higher-level framing.\nThe learning: When a shared artifact describes a repeatable system, the work that follows should be evaluated at the system's altitude, not just the immediate task's. We solved \"make Proof discoverable\" but should have been thinking \"what's the pattern for making any tool discoverable\" from the start.",
      "status": "pending"
    },
    "m1772489664832_1": {
      "kind": "replace",
      "by": "ai:claude",
      "createdAt": "2026-03-02T22:14:24.832Z",
      "range": {
        "from": 3667,
        "to": 4074
      },
      "content": "Macro > Micro: When building systems, skills, and workflows, always consider what altitude makes sense. A slash command that's globally present may carry enough context on its own — crowding CLAUDE.md with the same information adds bloat without value. Learn as we go; if /proof is sufficient, the CLAUDE.md section can be trimmed or removed.\nRight-size the surface area: Hooks handle mechanics, slash commands handle invocation, CLAUDE.md handles ambient knowledge. Not every tool needs all three — pick the lightest combination that works and iterate.\nConnect artifacts to systems: When a document describes a repeatable pattern, the implementation work should reference and extend that pattern — not just solve the local instance.",
      "status": "pending"
    }
  }
}
-->

<!-- PROOF:END -->
