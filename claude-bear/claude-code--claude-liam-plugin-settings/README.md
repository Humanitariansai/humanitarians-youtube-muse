# Claude Code, Plugin Settings.

Getting a Claude Code plugin's settings to survive between sessions isn't a
thing you ask Claude to remember — it's a thing you write down. The pattern
is one file, `.claude/plugin-name.local.md`: YAML frontmatter on top for
structured fields (`enabled`, `mode`, retry counts), a markdown body below
for free text. Three consumers read it — hooks parse the frontmatter with
`sed`, commands use the Read tool, agents reference it in their
instructions — and the `enabled` field drives a quick-exit: check the file,
check the field, stop before doing anything else if it's false. Flip that
field and the hook obeys every time, because a flat value is exactly what a
`sed` extraction is built for. Hand the same parser a multiline value, a
quoted colon, or an indented block, though, and it can silently mangle what
it reads back — no error, just a mismatch.

**Topic:** PLUGIN SETTINGS · CLAUDE CODE PLUGINS
**Playlist:** Claude Code
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-code--claude-liam-plugin-settings

---

## Chapters

0:00 How do I get Claude Code to remember my plugin's settings between sessions?
0:11 A file, not a memory
0:30 Three consumers, one file — the anchor
0:49 Reliable — then silent
1:09 Carry-out
1:18 Your turn
1:47 Outro

---

## YOUR TURN

"Add a settings file to my plugin that stores an enabled flag and a
validation mode, and have a hook check it before running."

Watch three things when Claude answers: does it place the file at
`.claude/plugin-name.local.md`, not somewhere else? Does it use YAML
frontmatter above a markdown body, instead of one flat format? And does the
hook check whether the file exists, then check `enabled`, and exit zero
before doing anything else if either check fails?

---

## Deliberately not claimed

Not a verdict on whether the skill's own documentation should have led with
the restart requirement or enforced the gitignore recommendation — that's
Teardown territory; this reel states the mechanism and the failure mode,
and stops. Not a claim that all three usage patterns (hook toggle, agent
state, config-driven behavior) get equal airtime — the reel foregrounds the
hook toggle. Not a claim that settings hot-swap — a restart is required.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #Plugins #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
