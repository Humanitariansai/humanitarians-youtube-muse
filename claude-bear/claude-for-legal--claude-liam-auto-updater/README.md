# Claude, Auto Updater.

When Claude runs a Skill, is the logic that drives it baked into the model
itself, or is it written down somewhere a person could actually read? Every
Claude Skill is a folder with one file, `SKILL.md`, written in plain
sentences, not code — the file is the whole program. Claude reads it and
follows its steps in order, top to bottom, branching only where a step says
so. Delete a step from that file and it simply doesn't happen; nothing
hidden fills the gap. Run the same input through it twice and you get the
same steps and the same result both times — but that guarantee holds only
for input inside what the file describes. Step outside it, and Claude has
nothing written there to fall back on.

**Topic:** SKILLS · ANTHROPIC AGENT SKILLS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-for-legal--claude-liam-auto-updater

---

## Chapters

0:00 Claude's auto-updater — is the logic baked into the model?
0:11 SKILL.md is the file — the anchor
0:29 Linear, no hidden fallback
0:45 The anchor returns — same file, same result, then the edge
1:05 Carry-out
1:13 Your turn
1:31 Outro

---

## YOUR TURN

"Write me a SKILL.md with five short numbered steps for a repeatable task I
do often. Then read it back to me, step by step, before you run anything —
and follow only what's written, nothing else."

Watch whether every action Claude takes matches a line in that file, and
whether it stops the moment the steps run out.

---

## Deliberately not claimed

Not what the `auto-updater` skill this reel is named after specifically
automates — the original source video's own narration never actually says
(three of its seven beats carry an unfilled template placeholder exactly
where that content should be, a batch-build defect, not a stylistic
choice), and the real file lives on a machine this build can't reach. This
reel states only what's generically true of any Claude Skill's mechanism.
Not a verdict on the design — the source called this "the Teardown moment"
and framed it as "what it gets right / where it bites"; this reel keeps the
same underlying mechanism (repeatable inside the spec, unsupported outside
it) but states it as a boundary, not a critique. Not a claim that Claude
never reasons about anything — only that this mechanism, a Skill's Steps
section, is followed linearly.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgenticAI #AIagents #HumanitariansAI #ProfessorBear #ClaudeBasics

---
