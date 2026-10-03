# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Only the manifest lives inside .claude-plugin. Everything else lives at
> the plugin's root, and it only loads automatically if the filename is
> exactly right.**

## The wrong guess it defeats

That a Claude Code plugin's commands, agents, and skills all live inside the
`.claude-plugin` folder, since that's the folder with "plugin" in the name.
They don't — `.claude-plugin/` holds only the manifest, `plugin.json`.
Commands, agents, skills, and hooks all live in directories at the plugin's
ROOT, a level up. The source's own documentation calls this the single most
common mistake, and it fails silently: nothing loads, and nothing tells you
why.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (manifest inside,
components at root) and it also covers the second real gotcha without
needing a separate sentence: "loads automatically only if the filename is
exactly right" is true of the whole auto-discovery system, but it's the
skills case — `SKILL.md`, spelled exactly — where getting it wrong costs you
the most, because the failure is silent.

## What it deliberately does not say

- **Not a verdict on the design.** The source's B05 framed the placement
  rule, the custom-path behavior, the restart inconsistency, and the
  command-collision gap as "what it gets right" / "where it bites" —
  Teardown language, including a judgment that the skill's own
  documentation buries these warnings. Plain keeps the underlying facts
  (placement is silent when wrong; `SKILL.md` must be spelled exactly) but
  states them as mechanism boundaries, not a critique of the skill file.
- **Not that every gap gets equal airtime.** The source names five gaps:
  placement-rule silence, custom-path double-scanning, a restart-guidance
  inconsistency with a sibling skill, the buried `SKILL.md` filename
  requirement, and undocumented command-name collisions. This reel
  foregrounds the placement split and the `SKILL.md` filename as the
  anchor — compression for a 7-beat Plain cut, not a factual change.
- **Not a claim that auto-discovery never works.** Commands and agents load
  from any correctly-placed `.md` file with no special naming beyond
  location — the reel states that plainly before showing where the skills
  case gets stricter.

---
**GATE C — signed:** ______________________  (human)
