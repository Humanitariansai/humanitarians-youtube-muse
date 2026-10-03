# Writing Hookify Rules

Stopping Claude from running a dangerous command automatically doesn't need
custom code — a hookify rule is a markdown file with YAML frontmatter, saved
at `.claude/hookify.{name}.local.md`, read fresh on every tool call. Five
fields: `name`, `enabled`, `event` (bash / file / stop / prompt / all),
`pattern` (a regex, or a `conditions` array for the advanced form), and
`action` — `warn` by default, or `block`. Watch the anchor: `event: bash`,
`pattern: rm -rf`, `action: block` — the pattern matches, and the command
never runs. But precision cuts both ways: pattern the word `log` and you also
catch `catalog` and `login`; pattern only `rm -rf /tmp` and the identical
danger typed against a different path sails straight through.

**Topic:** HOOKIFY RULES · CLAUDE CODE PLUGINS
**Playlist:** Claude Code
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-code--claude-liam-writing-rules

---

## Chapters

0:00 How do I write a script to stop Claude from running rm -rf?
0:11 A rule, not a script
0:29 Five fields — the anchor
0:49 Precision cuts both ways
1:09 Carry-out
1:19 Your turn
1:42 Outro

---

## YOUR TURN

"Create a hookify rule that blocks rm -rf commands, and one that warns when
editing .env files."

Watch two things when Claude answers: does the `rm` rule set `action: block`,
not `warn` — `warn` still lets the command run? And does the `.env` rule
check `file_path` directly, in a `conditions` block, rather than only the new
text being written — a path check catches the edit itself, not just what's
typed inside it?

---

## Deliberately not claimed

Not a verdict on whether the source skill's documentation should have
demonstrated the `block` action, documented the `stop`/`prompt` condition
fields, or defined rule execution order — that's Teardown territory; this
reel states the mechanism and the failure mode, and stops. Not a claim that
every rule needs the `conditions` array — the simple single-`pattern` field
is the common case. Not a claim that `warn` blocks anything — it defaults to
`warn`, which still allows the operation; only an explicit `block` stops it.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
