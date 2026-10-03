# Claude Code, Plugin Settings. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone wants Claude Code to remember a plugin's settings between sessions. It won't — each session starts blank. The real question: how does Claude Code read those settings back? One file holds the answer." | BrutalistHesitantWriter — types "How do I get Claude Code to remember my plugin's settings between sessions?", corrects "remember" → "read" |
| B01 | 1 stakes / 2 wrong guess, falsified | Telling Claude, in conversation, to remember a setting doesn't survive a new session — start over, and it's gone. What persists is a file: dot-claude-slash-plugin-name-dot-local-dot-m-d, sitting in the project root. Above the line, YAML frontmatter holds structured fields — enabled, mode, a retry count. Below it, a markdown body holds free text, read back later. | a conversation bubble scattering past a session-restart line; beside it a file icon staying fixed; the file splits into a frontmatter block on top and a body block below |
| B02 | 3 mechanism / **4 anchor planted** | Three consumers read that same file. A hook is a bash script — it parses the frontmatter with sed. A command uses the Read tool, in Claude's own context. An agent references it directly in its instructions. Watch the anchor: one field, enabled, drives a quick exit — check the file, check enabled, and stop before doing anything else if it's false. | three consumer icons pointing at one file; THE ANCHOR — enabled: true/false driving a hook through check-file, check-enabled, to run or exit 0 |
| B03 | **4 anchor payoff / 5 both directions** | Flip enabled again — false, true, false — and the hook obeys every time; a flat field like that is exactly what a bash sed extraction is built for. But hand it something else — a multiline value, a quoted colon, an indented block — and that same parser can silently mangle what it reads back. No error appears. The frontmatter just stops matching what's on the page. | THE ANCHOR RETURNS — enabled toggling the hook correctly three times; then a complex YAML block passing through the same sed scan and coming out wrong, no error shown |
| **BCRY** | **6 carry-out** | A plugin's settings aren't something you ask Claude to remember — they're a file it reads back every time, in a shape simple enough to parse, or not parsed at all. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Add a settings file to my plugin that stores an enabled flag and a validation mode, and have a hook check it before running. Watch three things when Claude answers: does it place the file at dot-claude-slash-plugin-name-dot-local-dot-m-d, not somewhere else? Does it use YAML frontmatter above a markdown body, instead of one flat format? And does the hook check whether the file exists, then check enabled, and exit zero before doing anything else if either check fails? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Code, Plugin Settings. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the file/persistence fact; the three-consumer / quick-exit mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (tell Claude to remember); B01 falsifies it with a case — a new session starts blank, a file on disk does not |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documentation of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the `enabled` field driving the quick-exit pattern) |
| Both directions | B03 — the field toggles reliably when it's flat (holds); the same parser silently mangles complex YAML shapes (flips) |
| No design judgment | B03 states the parser's fragility as a fact about how `sed` extraction works, never a verdict on whether the skill should have used a real YAML parser |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the restart
  requirement, the gitignore gap, and the fragile parser as "what it gets
  right" / "where it bites" — Teardown language, including a judgment that
  the skill's own docs bury the restart warning. Plain keeps the same
  underlying fact (flat fields parse reliably, complex ones don't) but
  states it as a mechanism boundary, not a critique of the skill file.
- **Not that all three usage patterns get equal airtime.** The source names
  hook toggle, agent state management, and config-driven behavior; this
  reel foregrounds the hook toggle (the one the anchor needs) and states
  the other two by name in QUESTION.md, rather than building a beat for
  each — compression for a 7-beat Plain cut, not a factual change.
- **No claim that settings hot-swap.** B01/B03 never imply a changed field
  takes effect without a restart; the source is explicit that it doesn't.

## Handoff prompt (BHTF, read aloud)

> "Add a settings file to my plugin that stores an enabled flag and a
> validation mode, and have a hook check it before running."

Why it's worth running: watching whether Claude places the file at
`.claude/plugin-name.local.md` (not a different directory or extension),
splits YAML frontmatter from a markdown body, and implements the quick-exit
pattern — three checks straight from the source's own file contract —
surfaces whether the anatomy from B01/B02 actually lands.

---
**GATE P — signed:** ______________________  (human)
