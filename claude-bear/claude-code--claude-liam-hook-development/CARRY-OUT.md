# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **A hook isn't something you ask Claude to remember — it's a script wired
> to one exact moment, and it fires exactly as configured, or not at all.**

## The wrong guess it defeats

That you can get the same effect by just telling Claude, in conversation, to
always remember to check something ("never touch my .env file"). That
instruction lives in the conversation — once the context scrolls away or a
new session starts, it's gone. A hook lives in a config file Claude Code
reads before it acts, whether or not those words are still nearby, and it
fires at the same fixed event every time: before a tool runs, when a prompt
is submitted, when the session starts or ends.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (a hook is a configured
event trigger, not a conversational request) without overstating what a hook
guarantees: "fires exactly as configured, or not at all" also covers the
source's real gotcha — the two config shapes are not interchangeable, and
getting the shape wrong means the hook silently never fires.

## What it deliberately does not say

- Not a verdict on whether the two config formats *should* have been made
  interchangeable, or whether the skill's documentation buries the warning
  (Teardown territory) — Plain states the mechanism and the failure mode,
  and stops.
- Not a claim that every hook is a bash script — command hooks and
  prompt-based hooks are both real, and the reel keeps both.
- Not a claim that hooks can coordinate with each other — they run in
  parallel and the reel never implies otherwise.

---
**GATE C — signed:** ______________________  (human)
