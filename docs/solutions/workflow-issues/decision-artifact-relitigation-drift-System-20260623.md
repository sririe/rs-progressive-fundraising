---
title: "Decision artifacts drifted from the client's actual answers (re-litigation)"
type: solution
category: workflow-issue
date: 2026-06-23
status: resolved
tags:
  - decision-artifact
  - drift
  - re-litigation
  - source-of-truth
  - client-correspondence
related:
  - projects/gift-cards/docs/plans/2026-06-18-phase1-vault-decision-artifact.html
  - projects/gift-cards/docs/discovery/2026-06-16-phase1-annotated-qa-thread.md
---

# Trap: a decision artifact re-opened items the client had already answered

**What happened (2026-06-23).** The Phase 1 decision board was built from an internal synthesis
(the design note) plus an adversarial reviewer's "you're missing rows X/Y/Z" completeness check.
Several of those "missing" rows — roles & access, the fixture package, the SystemBind name — had
**already been answered in Doug's 2026-06-16 email**. They got added to the board as *open
questions*, so the artifact re-litigated settled decisions. Spencer caught it: "a bunch of
re-litigation of things that were answered in their emails."

**Why it happened.** The completeness checker compared the artifact against the internal
*decision sheet* (which lists items as decisions to make) and flagged absent rows. Adding them as
"open" without checking the *client's actual correspondence* re-opened things the client had
closed. The drift source was building from internal synthesis, not from the client's sent emails.

**The fix (reusable).** When building or reviewing a client-facing decision artifact:

1. **Ground each row in the client's actual answers first** — the sent/received emails and the
   captured Q&A thread (here: `2026-06-16-phase1-annotated-qa-thread.md`), not just the internal
   design note or decision sheet.
2. **Treat a completeness check as "is this *present*," not "is this *open*."** If a reviewer says
   a row is missing, the next step is to check whether the client already answered it — a missing
   row is often a *resolved* item to record, not an open question to ask.
3. **Status discipline:** mark items the client answered as resolved (with their answer), only the
   genuinely unanswered ones as open/for-the-call.

Captured because the same trap will hit any future agent assembling a client decision artifact
from internal docs + a completeness pass.
