# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **An agent's context window isn't its memory — it's a workspace.
> Externalize the state to a file plus git, and each new session just reads
> it, finds the first gap, and fills it.**

## The wrong guess it defeats

That the agent somehow remembers its own progress across sessions — some
hidden model memory that carries forward — when it actually has zero
persistent memory. The persistence lives entirely outside the model: in an
external file plus a git history, which any fresh session can read cold.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (context window as a
disposable workspace vs. externalized state as the actual memory) without
smuggling in a claim about how the initial feature list gets written or how
tests decide "passing."

## What it deliberately does not say

- Not how the initial 200-item feature list is generated — the source
  attributes that to a separate initializer session, so this reel doesn't
  invent a mechanism for it.
- Not the detailed test framework that marks an item "passing" — out of
  scope per the source, and this reel doesn't guess at one.
- No verdict on whether `feature_list.json` + git is the "right" way to
  build a checkpoint system — explaining how the mechanism works is not the
  same as ruling on the design, which is Teardown's lane, not Plain's.

---
**GATE C — signed:** ______________________  (human)
