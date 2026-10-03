# QUESTION

**The question:** "Claude Code, Hook Development." — if you want Claude Code
to automatically stop or react to something (block a dangerous write, check
a prompt before it's used, run cleanup when a session ends), is that a thing
you ask for in conversation, or a thing you configure? Answered using the
`hook-development` plugin skill's own worked example — a `PreToolUse` hook
that blocks writes to `.env` files — as the concrete case.

**Mode:** redo — source is
`anthropics/claude-code/youtube/claude-liam-hook-development/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`claude-code/plugins/plugin-dev/skills/hook-development/SKILL.md`. 7 beats —
B00 cold open, B01 anatomy, B02 design, B05 teardown, BVDT verdict, BHTF
handoff, BOUT outro — B00 was already `ClaudeComposerAsk` REMOTION, not
AI-video/pantry, so NO-GENAI/NO-PANTRY LAW required no substitution beyond
the WRITER LAW swap). This reel keeps the question and the source's body
facts, re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, restates the source's B05 "gets right / bites" as a
both-directions mechanism fact instead of a design judgment, and closes with
the Humanitarians AI skin.

**Why it earns a reel:** Hooks are event-driven automation scripts that fire
at fixed points in a Claude Code session — nine event types in the source
(`PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SubagentStop`,
`SessionStart`, `SessionEnd`, `PreCompact`, `Notification`). Two ways to
write one: a command hook (a bash script, deterministic) or a prompt-based
hook (hands the decision to Claude's own judgment; supported on `Stop`,
`SubagentStop`, `UserPromptSubmit`, `PreToolUse`). `PreToolUse` can approve,
deny, or ask before a tool runs, and can rewrite the tool call via
`updatedInput`. Two config shapes exist and are not interchangeable: a
plugin's `hooks/hooks.json` wraps events inside a `hooks` key; a project's
`.claude/settings.json` puts the same events directly at the top level.
Mixing the two up is a silent failure — no error, the hook just never
fires. Matchers narrow which tool triggers a hook (exact, pipe-separated,
wildcard, regex — case-sensitive); hooks matching the same event run in
parallel and can't see each other's output. A hook communicates back via
exit code: 0 is success, 2 is a blocking error whose stderr feeds back to
Claude.

**Naive framing (B00, corrected on screen):** "How do I set a reminder for
Claude Code to skip my .env file?" → corrects "reminder" to "hook" (telling
Claude to remember something in conversation is not the same as wiring a
script to a specific event — a reminder can scroll out of context; a hook
lives in a config file Claude Code reads before it acts, every time).

**Body facts carried from source (unchanged):**
- hooks are event-driven automation scripts, nine event types
- two hook types: command (bash, deterministic) vs prompt-based (LLM
  judgment; only on Stop/SubagentStop/UserPromptSubmit/PreToolUse)
- `PreToolUse` fires before a tool runs, returns allow/deny/ask via
  `permissionDecision`, can rewrite the call via `updatedInput`
- two config formats: plugin `hooks/hooks.json` (wrapped in a `hooks` key)
  vs `.claude/settings.json` (events at the top level) — mixing them is a
  silent failure, no error message
- matchers: exact, pipe-separated, wildcard `*`, regex (case-sensitive);
  MCP tool namespaces match via regex like `mcp__.*__delete.*`
- hooks matching the same event run in parallel, cannot depend on each
  other's output
- exit code 0 = success (stdout to transcript); exit code 2 = blocking
  error (stderr fed back to Claude)
- source's Your Turn worked example: a `PreToolUse` hook for a plugin that
  blocks writes to `.env` files and system paths; checks include the
  plugin `hooks.json` wrapper shape, use of `${CLAUDE_PLUGIN_ROOT}` instead
  of a hardcoded path, and a set timeout instead of the 60s default
