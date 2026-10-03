# QUESTION

**The question:** "MCP Integration" — when a Claude Code plugin needs to
reach an external service (a task tracker, a REST API, a local script),
is that something you tell Claude to use, or something you configure? And
if it's configuration, how precise does that configuration have to be?
Answered using the `mcp-integration` plugin skill's own worked example — an
Asana MCP server — as the concrete case.

**Mode:** redo — source is
`anthropics/claude-code/youtube/claude-liam-mcp-integration/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`claude-code/plugins/plugin-dev/skills/mcp-integration/SKILL.md`. 6 beats —
B00 cold open, B01 anatomy, B02 design, B05 teardown, BVDT verdict, BHTF
handoff, BOUT outro — B00 was already `ClaudeComposerAsk` REMOTION, not
AI-video/pantry, so NO-GENAI/NO-PANTRY LAW required no substitution beyond
the WRITER LAW swap). This reel keeps the question and the source's body
facts, re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, restates the source's B05 "gets right / bites" as a
both-directions mechanism fact instead of a design judgment, and closes with
the Humanitarians AI skin.

**Why it earns a reel:** MCP (Model Context Protocol) lets a Claude Code
plugin reach an external service through structured tool access. Two
configuration methods in the source: a dedicated `.mcp.json` at the plugin
root (recommended for multiple servers) or an inline `mcpServers` field in
`plugin.json` (fine for one simple server). Four server types, each keyed to
how the service is actually reached: `stdio` (Claude Code spawns a local
process, terminates it on exit), `SSE` (a hosted service with OAuth handled
automatically), `HTTP` (a REST API with token auth in headers), `WebSocket`
(a persistent real-time stream). Always `${CLAUDE_PLUGIN_ROOT}` for local
paths, always HTTPS/WSS, never a hardcoded credential in the config. Tool
naming is exact and mechanical: `mcp__plugin_{plugin}_{server}__{tool}` —
Asana's `create_task` tool becomes
`mcp__plugin_asana_asana__asana_create_task`, precisely that string, two
underscores between each section. A wrong underscore is a silent failure —
Claude Code does not report a tool-name mismatch. Pre-allowing a specific
tool name is the described safe pattern; a wildcard (`mcp__plugin_asana_asana__*`)
also works, at the cost of opening every tool the server offers. Lifecycle:
servers start when the plugin enables (stdio spawns, SSE/HTTP connect
on-demand at first use); configuration changes require restarting Claude
Code.

**Naive framing (B00, corrected on screen):** "How do I add an app to my
plugin so it can use Asana?" → corrects "app" to "MCP server" (there is no
app-install step; you write a config entry naming a connection type, and
the wrong type simply can't reach the service).

**Body facts carried from source (unchanged):**
- MCP gives a plugin structured tool access to an external service
- two configuration methods: dedicated `.mcp.json` (recommended, multiple
  servers) vs inline `mcpServers` in `plugin.json` (single server)
- four server types: `stdio` (local child process), `SSE` (hosted, OAuth),
  `HTTP` (REST, token auth), `WebSocket` (real-time streaming)
- always `${CLAUDE_PLUGIN_ROOT}` for paths, always HTTPS/WSS, never a
  hardcoded credential
- tool naming: `mcp__plugin_{name}_{server}__{tool}`, exact match, two
  underscores between each section — `mcp__plugin_asana_asana__asana_create_task`
- a tool-name mismatch is a silent failure, no error reported
- pre-allow specific tool names; a wildcard (`__*`) also matches but widens
  scope to every tool the server exposes
- lifecycle: servers start on plugin enable; config changes need a Claude
  Code restart
- source's Your Turn worked example: an MCP server connecting a plugin to
  Asana for task management; checks include config location (`.mcp.json`
  vs `plugin.json`), server type (`SSE` for a hosted OAuth service), and
  exact tool naming vs a wildcard
