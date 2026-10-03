# Claude Code, Hook Development.

Getting Claude Code to automatically stop or react to something isn't a
thing you ask for in conversation — it's a thing you configure. A hook is
an event-driven script wired to a fixed moment: `PreToolUse` fires before
any tool runs and can return allow, deny, or ask; nine event types exist in
total. Two ways to write one — a bash "command" hook (deterministic) or a
"prompt-based" hook (Claude's own judgment). Watch `PreToolUse` block a
write to `.env`: it fires reliably every time, because a hook doesn't
forget. But there are two config shapes and they're not interchangeable —
a plugin's `hooks/hooks.json` wraps events inside a `hooks` key; a
project's `.claude/settings.json` puts the same events directly at the top
level. Swap the shapes and the hook doesn't error — it simply never fires.

**Topic:** HOOKS · CLAUDE CODE PLUGINS
**Playlist:** Claude Code
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-code--claude-liam-hook-development

---

## Chapters

0:00 How do I set a reminder for Claude Code to skip my .env file?
0:10 A file, not a memory
0:28 Two ways to write one — the anchor
0:47 Reliable — then silent
1:07 Carry-out
1:17 Your turn
1:46 Outro

---

## YOUR TURN

"Create a PreToolUse hook for my plugin that blocks writes to .env files and
system paths."

Watch two things when Claude answers: does `hooks.json` wrap the event
inside a `hooks` key, the way a plugin's config needs — not sitting
directly at the top level, the way a project's `settings.json` would? And
does the script path use `${CLAUDE_PLUGIN_ROOT}` instead of a hardcoded
path, so the hook still works once the plugin moves?

---

## Deliberately not claimed

Not a verdict on whether the two config formats should have been made
interchangeable, or whether the skill's own documentation buries the
warning — that's Teardown territory; this reel states the mechanism and the
failure mode, and stops. Not a claim that every hook is a bash script —
command hooks and prompt-based hooks are both real. Not a claim that hooks
can coordinate with each other — they run in parallel.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #Hooks #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
