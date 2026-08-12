# Dispatch record — design QA round 2 (pre-UAT)

- **Date:** 2026-08-12 (~13:10 PDT)
- **Prime:** `progressive design-qa · AUR2 · Fable`, workspace `w1V`, session `20260812T200317Z-42201`
- **Trigger:** Tim's 2026-08-12 update (Slack ts 1786561876.379329): Walmart prep step + Kaitlin-list
  fixes deployed; asked for agentic follow-up scan + focused design QA before the Progressive
  walkthrough. Kaitlin queued for a human pass after this run (ts 1786562864.456879).
- **Objective:** find P0/P1 blockers for client UAT, staging vs Figma.

## Lanes (all `recon`, live TUI, read-only floor per SHARED-CONTEXT.md)

| Lane | Pane | Fuel | Lens | Brief | Sentinel |
| --- | --- | --- | --- | --- | --- |
| design-qa-uat-codex | w1V:p2 | Codex (gpt-5.6-sol) | Figma fidelity + P0-closure verification | brief-codex.md | design-qa-codex.done/.blocked |
| design-qa-uat-claude | w1V:p3 | Claude (Fable 5) | Interaction states, consistency, responsive | brief-claude.md | design-qa-claude.done/.blocked |
| design-qa-uat-grok | w1V:p4 | Grok (4.6) | UAT walkthrough realism, workflow traps | brief-grok.md | design-qa-grok.done/.blocked |

Watchers: `lane-watch.sh` armed per lane (cap 5400s; Grok with `--auto-approve-safe`).

## Notes & deviations

- **Recon floor, not PR floor:** read-only recon lanes (no branch/PR); the dispatch-brief PR
  template is replaced by the recon lane floor in SHARED-CONTEXT.md, per prime-dispatch
  seat-work-admission recon-tier exception and the 2026-08-10 design-QA recon precedent.
- **Claude fuel = prime lineage:** allowed — `recon` is an advisory role, exempt from
  cross-family seating; the build under review is Tim's, not the seat's.
- **Grok lane:** operator explicitly requested Grok. Staging contains fake/disposable data only.
  Launched `--allow Read/Glob/Grep/Write`; TUI booted in `always-approve` mode (its own config)
  — noted, watcher armed. No live Figma/credentials handed to Grok; design canon via static
  exports in `figma-frames/` (9/9 nodes exported by Sonnet-pinned recon subagent, 20:06Z).
- **Codex submission:** first prompt swallowed by trust + hooks dialogs; cleared (`t`, Esc, Esc)
  and re-submitted per runbook fallback. Verified working.
- **Vault app checkout** synced `6241988 → 08c0c74` (Tim's latest, incl. `_testing-packages/2026-08-12/`).

## Results

- (pending — filled at collection)
