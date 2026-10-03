# Claude, Closing Checklist.

Does Claude apply its own legal judgment to build a closing checklist, or
does it follow a written instruction file? A skill is a folder Claude reads
before it works; `closing-checklist` is one file, `SKILL.md`, holding the
whole instruction set in plain language — no hidden logic. The pipeline
lives in the file's Steps section: Claude reads each step in order and runs
it, linear, with no branching unless a step itself says so. Ask for a step
that's written there, and it runs the same way every time — reliable,
because it's spec, not judgment. Ask for something the file never mentions,
and nothing fills the gap: that step simply isn't part of the run.

**Topic:** CLOSING-CHECKLIST · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-for-legal--claude-liam-closing-checklist

---

## Chapters

0:00 Does Claude just know how to build a closing checklist?
0:11 A skill is a folder
0:24 The steps section — the anchor
0:35 Same steps, every time — the anchor returns
0:51 Carry-out
1:00 Your turn
1:16 Outro

---

## YOUR TURN

"I'm closing a transaction and want to use the closing-checklist skill. Read
the SKILL.md and walk me through each step you'll run, in order, before you
run any of them."

Why it's worth running: watching Claude name its steps before running any of
them, in the order the file specifies, surfaces the same fact directly — the
file is the program, and the order is the whole spec.

---

## Deliberately not claimed

Not a verdict on whether `closing-checklist` was well designed — that's
Teardown territory; this reel states the mechanism (spec-bound execution,
repeatable results, a hard edge at what the file says) and stops. Not a
claim about what specific legal task the skill performs beyond building and
tracking a transaction's closing checklist — the source reel's own narration
left its most specific clauses as unfilled placeholders, and this redo does
not invent what they would have said. Not that Claude goes silent outside
the spec — the reel states only that an unwritten step isn't part of the
run, not that Claude has nothing to say about a request outside it.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #LegalTech #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
