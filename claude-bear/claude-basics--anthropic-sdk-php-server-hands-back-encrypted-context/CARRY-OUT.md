# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **The readable summary is for your eyes; the encrypted blob is what
> actually carries the conversation's memory forward.**

## The wrong guess it defeats

That the human-readable summary — the part you can actually read — is what
"remembers" the conversation, so feeding it back into the next call should be
enough to keep context intact. It isn't: the summary is display/debug only,
and only the encrypted blob reconstructs the full compressed context.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (readable-for-you vs.
token-for-the-server) without smuggling in a claim about the encryption
algorithm or compaction thresholds.

## What it deliberately does not say

- Not how the token is encrypted, or what algorithm is used — the source
  excludes the encryption algorithm itself.
- Not when compaction triggers or how to configure it manually — the source
  excludes compaction thresholds and manual-compaction APIs.
- Not a verdict on whether this design is the "right" way to handle context
  overflow — that's a design judgment (Teardown's lane), not Plain's.

---
**GATE C — signed:** ______________________  (human)
