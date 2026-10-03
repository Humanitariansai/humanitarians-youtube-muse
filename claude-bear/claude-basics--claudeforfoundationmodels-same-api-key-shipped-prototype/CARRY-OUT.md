# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence
survivable.

## The line

> **A key you can decompile isn't hidden, it's just harder to read — the
> real fix isn't a better hiding place, it's moving the key off the device
> entirely.**

## The wrong guess it defeats

That a bundled key can be made safe by hiding it harder — scrambling the
string, splitting it across files, loading it obfuscated. It can't: a
shipped binary is always decompilable, and every string inside it — however
it was scrambled — reads straight out. The fix isn't a better hiding place,
it's removing the key from the device.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still
true?*

Yes — it compresses the one distinction that matters (hiding vs. moving)
without smuggling in a claim about a specific obfuscation technique or a
specific relay implementation.

## What it deliberately does not say

- Not a specific obfuscation technique that fails — the point is that
  obfuscation as a *category* doesn't change what's extractable, not that
  one particular scheme is weak.
- Not OAuth, token refresh, or App Attest attestation mode — the source
  excludes those as a follow-on architecture, not this video's subject.
- Not a verdict on whether the relay pattern is the "best" architecture —
  that's a design judgment (Teardown's lane), not Plain's.

---
**GATE C — signed:** ______________________  (human)
