# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **A hookify rule isn't a script you write — it's a markdown file Claude
> reads before every tool call, and it only catches exactly what its pattern
> says.**

## The wrong guess it defeats

That stopping something dangerous automatically means writing code — a
script, a program, something you run. A hookify rule is a markdown file with
a YAML frontmatter block on top and a plain message underneath, dropped in
`.claude/`. There's no build step and no restart: Claude reads the file
fresh on every tool call, so an edit takes effect on the very next one.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (a rule is a file
Claude reads, not a program) and it doesn't overstate what that file
guarantees: "exactly what its pattern says" also covers the source's real
gotcha — too broad a pattern fires on things nobody meant to catch, and too
narrow a pattern misses the identical danger typed a different way.

## What it deliberately does not say

- Not a verdict on whether the source skill's documentation should have
  demonstrated the `block` action, or documented the `stop`/`prompt`
  condition fields, or defined rule execution order (Teardown territory) —
  Plain states the mechanism and the failure mode, and stops.
- Not a claim that every rule needs the advanced `conditions` format — the
  simple single-`pattern` form is real and is the common case.
- Not a claim that a rule can block anything by default — `action` defaults
  to `warn`, which allows the operation; only an explicit `block` stops it.

---
**GATE C — signed:** ______________________  (human)
