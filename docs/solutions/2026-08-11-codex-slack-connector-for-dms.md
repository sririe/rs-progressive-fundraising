---
title: Use Codex Slack connector for DMs; Grok has no Slack
date: 2026-08-11
type: solution
tags: [slack, codex, orchestration, progressive]
consult:
  keys: [slack dm, slack attachment, notify team]
  paths: []
---

# Codex Slack connector for agent-sent DMs

## Problem
AUR2 Prime on **Grok** cannot send Slack DMs or file attachments — no Slack MCP/plugin on that seat. Operators who previously “just sent Slack from the agent” were almost always on **Codex** or Claude web connectors.

## What worked (2026-08-11 Progressive design handoff)
1. Stage message + files under a run pack (`docs/runs/.../slack-dm-pack/`).
2. Dispatch **Codex** recon with `plugins.slack@openai-curated` enabled.
3. Resolve user (e.g. Kaitlin `U09EQMXF4HH`).
4. Expect **ChatGPT Slack OAuth reconnect** mid-run (browser).
5. Message send may succeed while **file upload is flaky** — operator can attach HTMLs manually from the pack.

## Do not
- Assume Grok can Slack.
- Block the session on perfect automated attachments if paste/drag is faster.

## Related
- Notify-operator (iMessage) for eyes-on-phone: `NOTIFY_OPERATOR_DIRECT=1` + `notify-operator/scripts/notify.sh`.
