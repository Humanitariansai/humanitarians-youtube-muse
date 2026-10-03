# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Claude's coordinates live in a resized copy of your screen — multiply by
> the ratio back to real pixels, or the click lands nowhere near the button.**

## The wrong guess it defeats

That the (x, y) Claude reports back after looking at a screenshot already
matches your screen's real pixel coordinates. It doesn't: Claude's vision
encoder resizes every 16:9 screenshot to exactly 1456×819 before it looks at
anything, so the coordinates it returns live in that resized image's space,
not your actual viewport's.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (resized-image space vs.
real-screen space, fixed by a ratio multiply) without smuggling in a claim
about aspect ratios, DOM navigation, or CSS selectors.

## What it deliberately does not say

- Not how to handle non-16:9 viewports — the source routes those through a
  separate `match_aspect_ratio` lookup table, which this reel names as an
  exclusion (B04) but doesn't build.
- Not DOM navigation or CSS-selector clicking — out of scope per the source.
- No verdict on whether coordinate scaling is the "right" way to do browser
  automation — that's a design judgment (Teardown's lane), not Plain's.

---
**GATE C — signed:** ______________________  (human)
