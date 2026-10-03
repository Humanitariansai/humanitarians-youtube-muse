# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **A plugin's settings aren't something you ask Claude to remember — they're
> a file it reads back every time, in a shape simple enough to parse, or not
> parsed at all.**

## The wrong guess it defeats

That you can get persistent plugin configuration by just telling Claude, in
conversation, to remember a setting ("always run in strict mode"). That
instruction lives in the conversation — a new Claude Code session starts
with none of it. A settings file is written once, to `.claude/plugin-name.local.md`,
and read back fresh by three different consumers — hooks, commands, agents
— every time one of them needs it, whether or not the conversation that
created it still exists.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (a plugin setting is a
file Claude reads, not a fact Claude remembers) without overstating what the
file guarantees: "in a shape simple enough to parse, or not parsed at all"
also covers the source's real gotcha — the `sed`-based frontmatter parser
handles flat fields reliably and silently mangles complex ones.

## What it deliberately does not say

- Not a verdict on whether the skill's documentation *should* have led with
  the restart requirement or enforced the gitignore recommendation
  (Teardown territory) — Plain states the mechanism and the failure mode,
  and stops.
- Not a claim that every consumer parses the file the same way — hooks use
  `sed`, commands use the Read tool, agents reference it in instructions;
  the reel keeps all three.
- Not a claim that settings changes apply immediately — the source is
  explicit that a restart is required; the reel does not imply hot-swapping.

---
**GATE C — signed:** ______________________  (human)
