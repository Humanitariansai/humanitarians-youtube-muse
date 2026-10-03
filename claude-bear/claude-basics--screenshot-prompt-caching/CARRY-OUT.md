# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **A repeated screenshot doesn't get cheaper on its own — you have to flag
> it as one you've already shown, and the discount lasts only until the
> picture actually changes.**

## The wrong guess it defeats

That sending the identical screenshot again is automatically free, or at
least cheaper, because "it's the same image" and the model has already seen
it. It isn't automatic: the API re-tokenizes every screenshot from scratch,
identical pixels or not, unless the request explicitly marks the image
`cache_control: {"type": "ephemeral"}`. Without that flag, a 50-turn task
with 35 repeated screenshots pays full price 50 times over.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (caching is requested,
not assumed, and it's conditional on the picture staying the same) without
overstating the savings for every deployment or claiming caching handles
near-identical-but-not-exact screenshots.

## What it deliberately does not say

- Not a savings guarantee for every task — the 90% figure is this reel's
  worked case (5 unique states out of 50 turns), not a universal number.
- Not the full caching protocol — minimum cacheable token thresholds and
  eviction policy aren't covered (both-directions clause, carried in B04).
- Not that the cache is permanent — it persists for a session; switching API
  keys or leaving it idle too long empties it, and the next screenshot is a
  miss again regardless of whether the picture changed.

---
**GATE C — signed:** ______________________  (human)
