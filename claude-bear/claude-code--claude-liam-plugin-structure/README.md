# Claude Code, Plugin Structure.

A Claude Code plugin has exactly one file that lives inside `.claude-plugin/`
— the manifest, `plugin.json`, and it needs just one field: `name`, in
kebab-case. Everything else — `commands/`, `agents/`, `skills/`, `hooks/` —
sits one level up, at the plugin's own root. Drop a file in the right
directory and it's auto-discovered, no registration step. Commands and
agents are forgiving: any correctly-placed markdown file works. Skills are
not — each one needs its own subdirectory containing a file named exactly
`SKILL.md`. Rename that file to `readme.md` and nothing errors; the skill
just disappears from the list, silently.

**Topic:** PLUGIN STRUCTURE · CLAUDE CODE PLUGINS
**Playlist:** Claude Code
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-code--claude-liam-plugin-structure

---

## Chapters

0:00 My commands folder — does it go inside .claude-plugin?
0:12 One field, one level up
0:29 Five kinds of component — the anchor
0:48 The anchor returns — renamed, and gone
1:02 Carry-out
1:12 Your turn
1:36 Outro

---

## YOUR TURN

"Create a plugin called doc-linter with a lint-docs command, a doc-reviewer
agent, and a markdown-style skill."

Watch three things when Claude answers: is `plugin.json` placed inside
`.claude-plugin/`, not at the plugin's root? Are `commands/`, `agents/`, and
`skills/` sitting at the root, not nested inside `.claude-plugin/`? And
inside the skill's folder, is the file named exactly `SKILL.md` — not
`readme`, not lowercase?

---

## Deliberately not claimed

Not a verdict on whether the skill's own documentation should have led with
the placement rule or the buried `SKILL.md` filename requirement — that's
Teardown territory; this reel states the mechanism and its silent failure
mode, and stops. Not that every source gap gets a beat — the source also
names custom-path double-scanning, a restart-guidance inconsistency, and
undocumented command-name collisions; this reel foregrounds the placement
split and the `SKILL.md` filename as the anchor. Not a claim that
auto-discovery never works — commands and agents load from any
correctly-placed markdown file with no special naming beyond location.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #Plugins #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
