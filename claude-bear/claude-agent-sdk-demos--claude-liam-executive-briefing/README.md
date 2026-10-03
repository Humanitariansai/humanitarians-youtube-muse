# Claude, Executive Briefing.

Does Claude sense on its own when writing needs boardroom polish? No — the
`executive-briefing` skill is one file, `SKILL.md`, and it activates only
when a request touches its printed list of trigger words: executive,
briefing, C-suite, board, leadership, presentation. Ask for a board
presentation on a research memo and two of those words light up, so the
skill fires: read `SKILL.md`, run its steps in order, return a structured
executive brief. Ask for the identical outcome in words that miss that list
— "make this shorter for my boss" — and the skill stays silent, even though
the memo and the intent are the same. The list decides, not the meaning
behind your request.

**Topic:** SKILLS · EXECUTIVE-BRIEFING
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-agent-sdk-demos--claude-liam-executive-briefing

---

## Chapters

0:00 A Skill must be some judgment Claude applies automatically. Is that it?
0:11 One file, a printed list
0:27 Words match — the pipeline fires
0:43 No match — no fire
0:59 Carry-out
1:09 Your turn
1:24 Outro

---

## YOUR TURN

"I want to turn my research findings into an executive-ready briefing. Read
the executive-briefing skill and walk me through what you'll do before you
do it — and tell me which of my words made it fire."

Why it's worth running: asking Claude to name which words triggered the
skill surfaces the activation rule directly — you see the trigger-word
match working exactly as this reel described, on your own request.

---

## Deliberately not claimed

Not a verdict on whether keyword-triggered activation is a good or bad
design — that's Teardown territory; this reel states the mechanism and the
boundary, and stops. Not a claim that every Skill activates on a keyword
list — `executive-briefing`'s trigger words are this reel's worked example.
No claim about what specific content or tone choices the executive-brief
structure contains once the skill does fire.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
