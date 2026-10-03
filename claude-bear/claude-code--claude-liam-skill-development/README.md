# Claude Code, Skill Development.

Getting Claude to reliably repeat a task your way isn't a thing you ask for
in conversation — it's a thing you build and hand it. A skill is
`SKILL.md`: YAML frontmatter (`name` + `description`, required) plus an
imperative body, and three optional folders — `scripts/` (code), `references/`
(docs), `assets/` (output files). Progressive disclosure runs in three
levels: the name and description sit in context for every conversation; the
body loads only once the description matches what's being asked; the
resource folders load only when Claude decides it needs them. Picture a
`pdf-editor` skill: get the description right — naming the trigger phrase
directly — and it fires exactly when someone asks to rotate a PDF, every
time. Write a vague description instead, and it won't fire reliably at all.
Paste the rotation script straight into the body instead of its own file,
and the whole skill loads in full on every single trigger — the lean file
you wrote becomes the thing progressive disclosure was built to avoid.

**Topic:** SKILLS · CLAUDE CODE PLUGINS
**Playlist:** Claude Code
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-code--claude-liam-skill-development

---

## Chapters

0:00 How do I add a reminder so Claude always follows my PDF workflow?
0:12 Always visible, loaded as needed
0:31 Built to be found — the anchor
0:54 Found — then lost two ways
1:20 Carry-out
1:30 Your turn
2:01 Outro

---

## YOUR TURN

"Create a skill for my plugin called pdf-editor that handles rotating PDFs
and converting pages to images."

Watch three things when Claude answers: does the description read in third
person with a specific trigger phrase — not something vague like "use this
for PDF tasks"? Is the body written as direct steps, not advice? And does
the actual rotation code live in its own `scripts/rotate_pdf.py` file,
referenced by name, instead of pasted into the body?

---

## Deliberately not claimed

Not a verdict on whether the 1,500–2,000 word target should have been a
hard limit, or whether the skill's own documentation should explain how the
trigger match actually works — that's Teardown territory; this reel states
the mechanism and the failure mode, and stops. Not a claim that every skill
needs scripts, references, and assets — all three are optional. Not a claim
that Claude reads the whole skill on every turn — only the name and
description are always in context.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #Skills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
