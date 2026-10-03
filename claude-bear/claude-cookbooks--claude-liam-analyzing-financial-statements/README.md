# Claude, Analyzing Financial Statements

Analyzing a balance sheet isn't Claude reasoning about finance on its own —
it's a skill folder: `calculate_ratios.py`, `interpret_ratios.py`, and a
two-kilobyte `SKILL.md` holding the full instruction set in plain language.
Claude reads the file, then acts — the file is the program. The
instructions sit in a Steps section: read `SKILL.md`, execute each step in
order, return the result, linear, no branching unless a step says so. Watch
the anchor: hand the skill a balance sheet and it reads the numbers, runs
`calculate_ratios.py`, and hands back the ratios — same three steps, every
time. Same input, same output, every run. But the reverse holds too: hand
it a statement the steps weren't written for, and it still runs those same
steps against numbers `SKILL.md` never specified. The limit is the spec:
only what it names.

**Topic:** ANALYZING-FINANCIAL-STATEMENTS · ANTHROPIC SKILL
**Playlist:** Claude Across the Curriculum
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-cookbooks--claude-liam-analyzing-financial-statements

---

## Chapters

0:00 How do I teach Claude to analyze financial statements?
0:10 A skill is a folder
0:29 Three steps, in order
0:53 Same input, same output
1:17 Carry-out
1:30 Your turn
1:53 Outro

---

## YOUR TURN

"I want to analyze financial statements for investment insights. Read the
analyzing-financial-statements skill and walk me through what you will do
before you do it."

Watch for that walk-through — explaining first is what surfaces which
ratios it's about to run, and which steps `SKILL.md` actually specifies,
rather than only seeing the finished numbers.

---

## Deliberately not claimed

Not a verdict on whether the source skill's documentation should have
covered more statement formats or ratio types — that's Teardown territory;
this reel states the mechanism and the limit, and stops. Not a claim about
specific ratios or formulas beyond what the source's own narration names
("key financial ratios and metrics ... for investment analysis") — the
source `SKILL.md` isn't available on this machine, so nothing beyond its
own narrated description is invented. Not a claim that the skill validates
its input — only that it runs the same steps regardless of whether the
statement fits the spec.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics #FinancialAnalysis

---
