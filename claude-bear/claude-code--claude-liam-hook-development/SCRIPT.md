# Claude Code, Hook Development. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:45.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone asks Claude Code to just remember to skip the dot-env file. But a reminder can slip. The real fix is a hook — a script tied to one exact moment. What's inside one?" | BrutalistHesitantWriter — types "How do I set a reminder for Claude Code to skip my .env file?", corrects "reminder" → "hook" |
| B01 | 1 stakes / 2 wrong guess, falsified | A reminder lives inside the conversation — once the context scrolls away or a new session starts, it's gone. A hook lives in a config file that Claude Code reads before it acts, whether or not those words are still nearby. It fires at fixed moments — nine of them — from before a tool runs to when a session starts or ends. | a reminder bubble scattering as text scrolls past; a config file staying fixed; nine tick marks lighting along a line |
| B02 | 3 mechanism / **4 anchor planted** | Two ways to write a hook. A command hook is a bash script — the same deterministic check, every time. A prompt-based hook hands the decision to Claude's own judgment instead. Watch PreToolUse handle the dot-env case: before any tool runs, it checks the file path, and returns one of three answers — allow, deny, or ask — stopping the write before it happens. | two cards, command vs prompt-based; THE ANCHOR — PreToolUse checking `.env`, branching to allow / deny / ask, deny lights up |
| B03 | **4 anchor payoff / 5 both directions** | Get the shape right and that block fires every single time — reliable, because a hook doesn't forget. But there are two ways to write the config, and they're not interchangeable: a plugin's hooks.json wraps its events inside a hooks key; a project's settings.json puts those same events directly at the top level. Swap the shapes and the hook doesn't error — it simply never fires, and nothing tells you why. | THE ANCHOR RETURNS — the same deny firing three times reliably; then two config shapes side by side, swapped shape fades to silence, no error shown |
| **BCRY** | **6 carry-out** | A hook isn't something you ask Claude to remember — it's a script wired to one exact moment, and it fires exactly as configured, or not at all. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Create a PreToolUse hook for my plugin that blocks writes to dot-env files and system paths. Watch three things when Claude answers: does hooks.json wrap the event inside a hooks key, the way a plugin's config needs, instead of sitting directly at the top level the way a project's settings.json would? Does the script path use dollar CLAUDE_PLUGIN_ROOT instead of a hardcoded path, so the hook still works once the plugin moves? And is there a timeout set, instead of leaning on the sixty-second default? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Code, Hook Development. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the config-file fact; the two-hook-type / PreToolUse mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (tell Claude to remember); B01 falsifies it with a case — a reminder scrolls out of context, a hook lives in a file Claude reads regardless |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documentation of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the PreToolUse hook blocking `.env` writes) |
| Both directions | B03 — the hook fires reliably in the right config shape (holds); the same event in the wrong config shape never fires, silently (flips) |
| No design judgment | B03 states the format mismatch as a fact about how the two config files are read, never a verdict on whether the skill's documentation should have led with the warning |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the config-format
  gotcha, the no-hot-swap constraint, and the parallel-coordination gap as
  "what it gets right" / "where it bites" — Teardown language, including a
  judgment that the skill's own documentation buries the warning. Plain
  keeps the same underlying fact (format mismatch is a silent failure) but
  states it as a mechanism boundary, not a critique of the skill file.
- **Not that all nine events get equal airtime.** The source names all nine;
  this reel foregrounds `PreToolUse` (the one the anchor needs) and states
  the total count and a couple of others by name, rather than reciting all
  nine — compression for a 7-beat Plain cut, not a factual change.
- **No claim that hooks can coordinate.** B01/B03 never imply one hook can
  depend on another's output; the source is explicit that they run in
  parallel and can't.

## Handoff prompt (BHTF, read aloud)

> "Create a PreToolUse hook for my plugin that blocks writes to .env files
> and system paths."

Why it's worth running: watching whether Claude wraps the event in the
plugin's `hooks` key (not the settings.json top-level shape), reaches for
`${CLAUDE_PLUGIN_ROOT}` instead of a hardcoded path, and sets an explicit
timeout — three checks straight from the source's own worked example —
surfaces whether the config-format distinction from B03 actually lands.

---
**GATE P — signed:** ______________________  (human)
