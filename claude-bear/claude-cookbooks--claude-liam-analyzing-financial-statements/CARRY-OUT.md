# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **A financial-analysis skill isn't Claude reasoning about finance on its
> own — it's SKILL.md, a spec Claude reads and runs the same way against
> whatever statement you hand it.**

## The wrong guess it defeats

That analyzing a balance sheet is Claude exercising some general financial
judgment, trained in from the model itself. It isn't: `analyzing-financial-
statements` is a folder — `calculate_ratios.py`, `interpret_ratios.py`, and a
`SKILL.md` holding the full instruction set in plain language. Claude reads
the steps in order and executes them. The file is the program.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still
true?*

Yes — it compresses the one distinction that matters (a skill is a spec
Claude reads and re-runs, not built-in financial reasoning) and it doesn't
overstate what that spec guarantees: "the same way against whatever
statement you hand it" also covers the source's own limit — a statement
the steps weren't written for still runs the same steps, against data
outside what `SKILL.md` names.

## What it deliberately does not say

- Not a verdict on whether the source skill's `SKILL.md` should have covered
  more statement formats or ratio types (Teardown territory) — Plain states
  the mechanism and the limit, and stops.
- Not a claim about which specific ratios or formulas the skill computes
  beyond what the source itself names ("key financial ratios and metrics ...
  for investment analysis") — the source `SKILL.md` isn't available on this
  machine, so nothing beyond its own narrated description is invented.
- Not a claim that the skill validates its input — only that it runs the
  same steps regardless of whether the statement fits the spec.

---
**GATE C — signed:** ______________________  (human)
