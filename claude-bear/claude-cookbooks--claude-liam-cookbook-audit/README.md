# Claude, Cookbook Audit

Does auditing a cookbook notebook mean Claude is exercising some general
sense of editorial quality? No — the cookbook-audit skill is a folder
Claude reads before it works: `SKILL.md`, `style_guide.md`, and
`validate_notebook.py` holding the full instruction set in plain language.
Claude reads the steps, executes them in order, then `validate_notebook.py`
checks the result against a rubric — the same way, every time, even
against a notebook with something outside the skill's stated rubric.

**Topic:** COOKBOOK-AUDIT · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-cookbooks--claude-liam-cookbook-audit

---

## Chapters

0:00 The naive framing: "judge my notebook"
0:08 A skill is a folder Claude reads — not trained on it
0:25 The anchor: three steps, a notebook through validate_notebook.py
0:41 The anchor returns: same input twice, then the rubric's limit
1:04 Carry-out
1:15 Your turn
1:32 Outro

---

## YOUR TURN

I want to audit an anthropic cookbook notebook based on a rubric. Use
whenever a notebook review or audit is requested. Read the cookbook-audit
skill and walk me through what you will do before you do it.

Watch for that walk-through — explaining first is what surfaces which
rubric items `SKILL.md` actually checks, and where the stated scope stops,
rather than only seeing the finished score.

---

## Deliberately not claimed

- Not a verdict on whether the source skill's `SKILL.md` should have
  covered more rubric items — that's Teardown territory; this reel states
  the mechanism and the limit, then stops.
- No specific rubric line items or scoring weights beyond what the
  source's own narrated description already names — the source `SKILL.md`
  isn't available on this machine, so nothing beyond that is invented.
- Not a claim that the skill decides what counts as "good" — only that it
  runs the same steps and the same check regardless of whether the
  notebook fits the stated rubric.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear
