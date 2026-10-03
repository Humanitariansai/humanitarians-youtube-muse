# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Adding an MCP server isn't an app install — it's a config entry with
> the right connection type and an exact tool name. Get either wrong, and
> it fails quietly, not loudly.**

## The wrong guess it defeats

That connecting a plugin to an external service is a single universal
step, like installing an app — one setting that works the same way every
time. It isn't: the config has to name one of four connection types, and
the right type depends entirely on how the service is actually reached — a
local script Claude spawns itself needs `stdio`; a hosted service
authenticating with OAuth, like Asana, needs `SSE` instead. Pick the wrong
type and Claude can't reach the service at all.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (MCP integration is a
precise declaration, not a fuzzy request) without overstating what gets
caught: "fails quietly, not loudly" covers the source's real gotcha — a
tool-name typo is never reported as an error, and a wildcard pre-allow
"works" too, just by matching everything.

## What it deliberately does not say

- Not a verdict on whether Claude Code *should* report a tool-name
  mismatch, or whether the wildcard pattern is a bad design choice
  (Teardown territory) — Plain states the mechanism and the failure mode,
  and stops.
- Not a claim that every plugin needs a dedicated `.mcp.json` — the inline
  `mcpServers` field is a real, valid choice for a single simple server.
- Not a claim that all three integration patterns (simple wrapper,
  autonomous agent, multi-server) get equal airtime — this reel compresses
  to the config + naming mechanism the anchor needs.

---
**GATE C — signed:** ______________________  (human)
