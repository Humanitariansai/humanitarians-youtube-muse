# Claude Code, Plugin Structure. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes their commands folder goes inside dot-claude-plugin, right beside the manifest. It doesn't — only the manifest lives there. Everything else sits at the plugin's root. So where does the rest actually go?" | BrutalistHesitantWriter — types "My commands folder — does it go inside .claude-plugin?", corrects "inside" → "outside" |
| B01 | 1 stakes / 2 wrong guess, falsified | The manifest — plugin.json — lives inside .claude-plugin, and it needs exactly one field: name, in kebab-case. Everything else lives at the plugin's root, one level up: commands, agents, skills, hooks. Drop a file in the right directory, and it's auto-discovered — no registration, no import step. | a manifest card fixed inside a `.claude-plugin` folder icon; four component folders drawn at the root level beside it, one level up |
| B02 | 3 mechanism / **4 anchor planted** | Five kinds of component can live at that root. Commands and agents are just markdown files — drop one in the right folder and it works. Skills are pickier: each one needs its own subdirectory, and inside it, a file named exactly SKILL.md — not readme, not skill dot m d in lowercase. Get that filename right, and the skill shows up automatically. | five component slots filling in one by one; THE ANCHOR — a skills/ subdirectory, a file renaming itself into place as exactly "SKILL.md", the skill card lighting up |
| B03 | **4 anchor payoff / 5 both directions** | Rename that same file to readme dot m d, and nothing errors — the skill just disappears from the list, silently. Auto-discovery holds exactly as advertised when the name is right; get it wrong, in this one specific way, and it fails without a word. | THE ANCHOR RETURNS — the same file renamed to "readme.md"; the skill card goes dark, no error text, just gone |
| **BCRY** | **6 carry-out** | Only the manifest lives inside .claude-plugin. Everything else lives at the plugin's root, and it only loads automatically if the filename is exactly right. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Create a plugin called doc-linter with a lint-docs command, a doc-reviewer agent, and a markdown-style skill. Watch three things when Claude answers: is plugin.json placed inside .claude-plugin, not at the plugin's root? Are the commands, agents, and skills folders sitting at the root, not nested inside .claude-plugin? And inside the skill's folder, is the file named exactly SKILL.md — not readme, not lowercase? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Code, Plugin Structure. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the manifest/root split; the five-component mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (commands live inside .claude-plugin); B01 falsifies it directly — the manifest lives there, components live at the root |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documentation of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the skills subdirectory requiring a file named exactly SKILL.md) |
| Both directions | B03 — auto-discovery holds exactly as advertised when the filename is right (holds); the same mechanism fails silently, with no error, when the filename is wrong in this one specific way (flips) |
| No design judgment | B03 states the filename requirement and its silent failure mode as a fact about how discovery works, never a verdict on whether the skill's documentation should have led with the warning |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the placement
  rule, custom-path behavior, a restart-guidance inconsistency with a
  sibling skill, and undocumented command-name collisions as "what it gets
  right" / "where it bites" — Teardown language. Plain keeps the same
  underlying facts where they're used (placement is silent when wrong;
  SKILL.md must be spelled exactly) but states them as mechanism
  boundaries, not a critique of the skill file.
- **Not that every source gap gets a beat.** The source names five gaps:
  placement-rule silence, custom-path double-scanning, the restart
  inconsistency, the buried SKILL.md filename requirement, and command
  collisions. This reel foregrounds the placement split and the SKILL.md
  filename as the anchor — compression for a 7-beat Plain cut, not a
  factual change.
- **No claim that auto-discovery never works.** B02 states plainly that
  commands and agents load from any correctly-placed markdown file with no
  special naming beyond location, before showing where the skills case
  gets stricter.

## Handoff prompt (BHTF, read aloud)

> "Create a plugin called doc-linter with a lint-docs command, a
> doc-reviewer agent, and a markdown-style skill."

Why it's worth running: watching whether Claude places `plugin.json` inside
`.claude-plugin/` rather than at the plugin root, puts `commands/`,
`agents/`, and `skills/` at the root rather than nested inside
`.claude-plugin/`, and names the skill file exactly `SKILL.md` — three
checks straight from the source's own worked example — surfaces whether the
placement split and the filename rule from B01–B03 actually land.

---
**GATE P — signed:** ______________________  (human)
