# Claude, Action Creator.

A Claude Skill isn't special code Claude runs — it's a folder Claude reads
before it acts. The `action-creator` skill is two files: a `SKILL.md`
instruction set (plain text, no executable) and a `templates` folder.
`SKILL.md` has a Steps section Claude works through top to bottom: read the
request, run the step, return the result. Ask for a one-click button that
sends a payment reminder to a specific vendor, and the skill turns that into
a saved action — click it once, and the same email goes out every time you
press it, because the steps in the file don't change between clicks. Ask
that same button to do something the file never described — say, negotiate
the invoice instead of just sending it — and nothing happens beyond what's
already there. A Skill only does what the page in front of it says.

**Topic:** SKILLS · ACTION-CREATOR
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-agent-sdk-demos--claude-liam-action-creator

---

## Chapters

0:00 A Skill must be some code Claude runs automatically. Is that it?
0:09 A folder, not a program
0:24 Steps, top to bottom — the anchor
0:42 Reliable — then out of scope
1:01 Carry-out
1:11 Your turn
1:26 Outro

---

## YOUR TURN

"I want a one-click action that archives newsletters from a specific
sender. Read the action-creator skill and walk me through what you'll do
before you do it — show me each step in order, so I can see exactly what
the button will run."

Why it's worth running: asking Claude to narrate the steps before it builds
the action surfaces the constraint logic directly — you see the Steps
section working exactly as this reel describes, on your own request.

---

## Deliberately not claimed

Not a verdict on whether this design is good or limiting — that's Teardown
territory; this reel states the mechanism and the boundary, and stops. Not
a claim that every Skill shares this exact file layout — `action-creator`'s
`SKILL.md` + `templates` folder is this reel's worked example. Not a claim
that Skills can never be extended — only that a given button does only what
its own file currently specifies.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
