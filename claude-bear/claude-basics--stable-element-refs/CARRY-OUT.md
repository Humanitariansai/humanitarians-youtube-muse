# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **A pixel coordinate describes a moment in one viewport; a stable ref
> describes the button itself — that's why the ref survives a resize and the
> coordinate doesn't.**

## The wrong guess it defeats

That a button's pixel position is a stable enough handle to click by. It
isn't: resizing a browser window reflows the page, the button moves to a new
pixel, and the old coordinate now points at empty space (or a different
element).

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (a coordinate names a
spot; a ref names a thing) without smuggling in a claim about how the
injection script works or what happens to elements added after page load.

## What it deliberately does not say

- Not the JavaScript injection mechanics or CSS specificity rules that affect
  how a ref gets attached — the source excludes those, and this reel names
  the exclusion (B04) without building it.
- Not dynamic elements added after the ref pass ran — those need their own
  re-injection pass, stated as a limit, not solved on screen.
- No verdict on whether ref-based targeting is the "right" way to build
  browser automation — that's a design judgment (Teardown's lane), not
  Plain's.

---
**GATE C — signed:** ______________________  (human)
