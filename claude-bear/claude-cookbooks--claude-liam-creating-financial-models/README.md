# Claude, Creating Financial Models

Building a DCF or running a sensitivity table isn't Claude reasoning about
finance on its own — it's a skill folder: `dcf_model.py`,
`sensitivity_analysis.py`, and a four-kilobyte `SKILL.md` holding the full
instruction set in plain language. Claude reads the file, then acts — the
file is the program. The instructions sit in a Steps section: read
`SKILL.md`, execute each step in order, return the result, linear, no
branching unless a step says so. Watch the anchor: hand the skill a
five-year revenue projection and it reads the assumptions, runs
`dcf_model.py`, and hands back a valuation — same three steps, every time.
Same input, same output, every run. But the reverse holds too: hand it a
projection the steps weren't written for, and it still runs those same
steps against numbers `SKILL.md` never specified. The limit is the spec:
DCF analysis, sensitivity testing, Monte Carlo simulations, and scenario
planning — and nothing outside it.

**Topic:** CREATING-FINANCIAL-MODELS · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-cookbooks--claude-liam-creating-financial-models

---

## Chapters

0:00 How do I teach Claude to build financial models?
0:10 A skill is a folder
0:28 Three steps, in order
0:45 Same input, same output
1:11 Carry-out
1:21 Your turn
1:39 Outro

---

## YOUR TURN

"I want to stress-test a five-year revenue projection. Read the
creating-financial-models skill and walk me through what you will build
before you touch a number."

Watch for that clause — before you touch a number — that's the discipline
the spec enforces: the plan is visible before the model runs.

---

## Deliberately not claimed

Not a verdict on whether the source skill's documentation should have
covered more scenario types or discount conventions — that's Teardown
territory; this reel states the mechanism and the limit, and stops. Not a
claim about specific formulas, discount rates, or Monte Carlo parameters
beyond what the source's own narration names ("DCF analysis, sensitivity
testing, Monte Carlo simulations, and scenario planning for investment
decisions") — the source `SKILL.md` isn't available on this machine, so
nothing beyond its own narrated description is invented. Not a claim that
the skill validates its input — only that it runs the same steps
regardless of whether the projection fits the spec.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics #FinancialModeling

---
