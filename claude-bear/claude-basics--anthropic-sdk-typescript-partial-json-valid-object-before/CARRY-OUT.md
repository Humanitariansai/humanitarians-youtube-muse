# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **The parser closes every open structure for you — so a valid snapshot
> tells you the shape is safe to read, not that the values inside it are
> finished.**

## The wrong guess it defeats

That a half-finished JSON string streaming in from a tool call must behave
like input to a standard parser: broken, or unusable, until the closing
brace lands. It doesn't — the vendored parser seals every open object and
array with a zero-value default the instant a chunk ends, so every prefix
of the stream is already syntactically valid.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (structurally valid vs.
value-complete) without smuggling in a claim about which zero-value default
gets used for which type, or about full JSON grammar edge cases.

## What it deliberately does not say

- Not which specific zero-value default applies to which JSON type (string,
  number, array) — the source excludes full JSON edge cases like numbers
  and unicode.
- Not how the accumulator or event loop wires `jsonSnapshot` into
  application state — the source excludes that wiring.
- Not a verdict on whether closing structures with defaults is the "right"
  way to build a streaming parser — that's a design judgment (Teardown's
  lane), not Plain's.

---
**GATE C — signed:** ______________________  (human)
