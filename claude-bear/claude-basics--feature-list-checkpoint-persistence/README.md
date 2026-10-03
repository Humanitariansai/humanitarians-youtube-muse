# Persisting Progress Across Context Windows

A coding agent working through a long feature list will eventually fill its
context window — and the next session opens blank. Naively, the agent either
re-reads everything already done (burns half the new context) or guesses
where it left off (wrong). The fix: externalize progress to a
`feature_list.json` file (one entry per feature, each with an id and a
status — incomplete or passing) plus git as an immutable commit ledger.
Every new session's whole job is: open the file, find the first entry still
marked incomplete, and start exactly there.

**Topic:** CLAUDE BASICS · AGENT CHECKPOINTING
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--feature-list-checkpoint-persistence

---

## Chapters

0:00 The naive framing: does the agent just remember?
0:11 The problem: context resets, two bad options
0:26 The anchor: feature 51, first incomplete
0:44 The mechanism: open, find the gap, fill it
0:57 The anchor returns: session two resumes at 51
1:13 Carry-out
1:24 Your turn
1:38 Outro

---

## YOUR TURN

Externalize my agent's progress to a feature_list.json plus git, so it can
resume across sessions — then prove it picks up exactly where it left off,
without replaying finished work.

Run that today, against your own long-running agent task.

---

## Deliberately not claimed

Not how the initial feature list gets generated — that's a separate
initializer session's job, and this reel doesn't invent a mechanism for it.
Not the detailed test framework that decides "passing" — out of scope, same
as the source. No verdict on whether `feature_list.json` + git is the "right"
way to build a checkpoint system — explaining how the mechanism works is not
the same as ruling on the design.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #Agents #Checkpointing #ClaudeBasics #LLM #HumanitariansAI #ProfessorBear

---
