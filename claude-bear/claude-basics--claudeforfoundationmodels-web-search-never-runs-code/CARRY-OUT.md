# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence
survivable.

## The line

> **It isn't the syntax that decides the round trip — it's who can execute.
> Anthropic runs its own tools inside the turn; only you can run yours, so
> the model has to stop and come back for the answer.**

## The wrong guess it defeats

That every tool call round-trips through the caller's code the same way,
because every tool is declared the same way. It doesn't: web search's
result appears in the very next turn with no callback into anything the
caller wrote, because Anthropic already owns the infrastructure (a web
index, a sandbox) the call needs. A client-side tool like `lookupFavorites()`
is arbitrary code on the caller's device — only the caller can run it, which
is what forces the exit-and-return.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still
true?*

Yes — it compresses the one distinction that matters (who executes, not how
the tool looks) without smuggling in a claim about a specific SDK, language,
or tool-result schema.

## What it deliberately does not say

- Not a claim about domain filtering, `maxUses` rate limiting, or the
  tool-result schema — the source excludes these explicitly as follow-on
  questions, not this video's subject.
- Not a verdict on which pattern is "better" — server-side tools trade
  flexibility for speed, client-side tools trade speed for reach; explaining
  why the split exists is not the same as ruling on which one you should
  prefer. That's Teardown's lane.
- Not a claim that this is the only kind of tool split — the source's own
  case (`.webSearch` vs. a device function) is one instance of the general
  rule, not the whole rule.

---
**GATE C — signed:** ______________________  (human)
