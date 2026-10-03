# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Claude's click lands in the resized copy of your screenshot, not your
> native display — record the size you sent, then multiply back by
> original-over-sent to hit the real pixel.**

## The wrong guess it defeats

That a Retina screenshot reaches Claude pixel for pixel, so the coordinate it
clicks already matches your screen's real pixels. It doesn't: Claude's vision
budget caps every image at a 1568px long edge and 1568 tiles, so a native
Retina screenshot gets resized — by you, or by the server if you don't —
before the model ever looks at it. The click Claude reports lives in that
resized space.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (resized-image space vs.
native-display space, fixed by a ratio multiply) without smuggling in a claim
about specific hardware resolutions, non-macOS platforms, or other
computer-use optimizations.

## What it deliberately does not say

- Not a specific MacBook resolution — Retina native resolutions vary by
  model; the reel states the mechanism generically and uses one verified
  16:9 example (1920×1080 → 1456×819) for the arithmetic.
- Not non-macOS platforms, batched tool calls, or trajectory recording — the
  source names these as exclusions, and this reel keeps them as exclusions.
- No verdict on whether porting the API's resize algorithm client-side is the
  "right" design — that's a design judgment (Teardown's lane), not Plain's.

---
**GATE C — signed:** ______________________  (human)
