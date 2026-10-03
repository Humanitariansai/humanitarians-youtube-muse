# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Auditing a cookbook notebook isn't Claude forming its own opinion of
> quality — it's SKILL.md, a rubric Claude reads, applies, and checks the
> same way against whatever notebook you hand it.**

## The wrong guess it defeats

That reviewing a notebook is Claude exercising some general sense of
quality, picked up from training. It isn't: `cookbook-audit` is a folder —
`SKILL.md`, `style_guide.md`, `validate_notebook.py` — holding the full
instruction set in plain language. Claude reads the steps in order and
executes them, then `validate_notebook.py` checks the result against the
rubric. The file is the program.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still
true?*

Yes — it compresses the one distinction that matters (a cookbook-audit skill
is a rubric Claude reads, applies, and checks, not built-in editorial taste)
and it doesn't overstate what that rubric guarantees: "the same way against
whatever notebook you hand it" also covers the source's own limit — a
notebook with something outside the stated rubric still runs the same
steps, checked only against what `SKILL.md` names.

## What it deliberately does not say

- Not a verdict on whether the source skill's `SKILL.md` should have covered
  more rubric items (Teardown territory) — Plain states the mechanism and
  the limit, and stops.
- Not a claim about which specific rubric line items or scoring weights the
  skill applies beyond what the source itself names — the source
  `SKILL.md` isn't available on this machine, so nothing beyond its own
  narrated description is invented.
- Not a claim that the skill decides what counts as "good" beyond the
  rubric — only that it runs the same steps and the same check regardless
  of what the notebook contains.

---
**GATE C — signed:** ______________________  (human)
