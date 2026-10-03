# MCP Integration.

Connecting a Claude Code plugin to an external service isn't an app install —
it's a config entry. Two places to write it: a dedicated `.mcp.json` at the
plugin root (recommended for multiple servers) or an inline `mcpServers`
field in `plugin.json` (fine for one). Four connection types, one per each
service's actual shape: `stdio` for a local process, `SSE` for a hosted
OAuth service, `HTTP` for token-authenticated REST, `WebSocket` for
real-time streaming — pick the wrong one and Claude simply can't reach the
service. Tool names are exact and mechanical:
`mcp__plugin_{plugin}_{server}__{tool}`. Get it exactly right and Claude
calls precisely that tool; get one underscore wrong and nothing happens — no
error, just silence, because a name mismatch is never reported.

**Topic:** MCP INTEGRATION · CLAUDE CODE PLUGINS
**Playlist:** Claude Code
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-code--claude-liam-mcp-integration

---

## Chapters

0:00 How do I add an app to my Claude plugin so it can use Asana?
0:10 One declaration, four types
0:29 Two places to write it — the anchor
1:04 Exact — or silent
1:30 Carry-out
1:41 Your turn
2:09 Outro

---

## YOUR TURN

"Add an MCP server to my plugin that connects to Asana for task management."

Watch three things when Claude answers: does the configuration land in
`.mcp.json`, not inline inside `plugin.json`? Is the type set to `SSE` — not
`stdio`, not `HTTP` — since Asana is a hosted service using OAuth? And does
the command's allowed-tools list the exact tool name,
`mcp__plugin_asana_asana__asana_create_task`, rather than a wildcard?

---

## Deliberately not claimed

Not a verdict on whether Claude Code should report a tool-name mismatch, or
whether the wildcard pre-allow pattern is a bad design choice — that's
Teardown territory; this reel states the mechanism and the failure mode, and
stops. Not a claim that every plugin needs a dedicated `.mcp.json` — the
inline `mcpServers` field is a real, valid choice for a single simple
server. Not a claim that all three integration patterns (simple wrapper,
autonomous agent, multi-server) get equal airtime here.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #MCP #ModelContextProtocol #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
