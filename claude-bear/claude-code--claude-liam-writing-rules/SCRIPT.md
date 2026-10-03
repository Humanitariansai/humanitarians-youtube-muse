# Writing Hookify Rules — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:45.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone wants Claude to catch a dangerous command automatically. Their first thought: write a script. But hookify needs no code — just a rule. So: how do you write one that blocks rm -rf?" | BrutalistHesitantWriter — types "How do I write a script to stop Claude from running rm -rf?", corrects "script" → "rule" |
| B01 | 1 stakes / 2 wrong guess, falsified | A hookify rule isn't code — it's a markdown file. Save it at dot-claude slash hookify dot name dot local dot md, with a YAML frontmatter block on top and a message underneath. There's no build step and no restart: Claude reads the file fresh on every single tool call, so an edit takes effect on the very next one. | a script/gears card receding; a markdown file card with a frontmatter divider growing in its place; the file path underneath; a "read fresh, every call" tag |
| B02 | 3 mechanism / **4 anchor planted** | Five frontmatter fields sit above the message: name, kebab-case verb-first; enabled, true or false; event — bash, file, stop, prompt, or all; and pattern, a regex to match. Action defaults to warn; block stops the operation outright. Watch the anchor: event bash, pattern matching rm -rf, action block — Claude reaches for the command, the pattern matches, and it never runs. | five field chips lighting in turn; THE ANCHOR — a rule card (event: bash / pattern: rm -rf / action: block), a command attempt arrow into it, BLOCKED lighting in terracotta |
| B03 | **4 anchor payoff / 5 both directions** | Get that pattern exact and the block fires every time — reliable, because the check is a straight regex match. But precision cuts both ways. Pattern the word log, and you also catch catalog and login — blocking things nobody asked about. Pattern only rm -rf slash tmp, and the identical danger typed against a different path sails straight through. | THE ANCHOR RETURNS — the same rule blocking three times in a row; then split: "log" lighting up catalog/login as a false block, "rm -rf /tmp" letting "rm -rf ~" pass as a false miss |
| **BCRY** | **6 carry-out** | A hookify rule isn't a script you write — it's a markdown file Claude reads before every tool call, and it only catches exactly what its pattern says, no more, no less. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Create a hookify rule that blocks rm -rf commands, and one that warns when editing .env files. Watch two things when Claude answers. Does the rm rule set action to block, not warn — warn still lets the command run. And does the .env rule check file_path directly, in a conditions block, rather than only the new text being written — a path check catches the edit itself, not just what's typed inside it. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Writing Hookify Rules. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the file-not-code fact; the frontmatter/anchor mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (write a script); B01 falsifies it with a case — a hookify rule is a markdown file Claude reads fresh on every call, no build, no restart |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documentation of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the rule blocking `rm -rf`) |
| Both directions | B03 — a precise pattern fires reliably (holds); an imprecise one fails in *either* direction: too broad over-fires, too narrow lets the danger through unnoticed |
| No design judgment | B03 states pattern precision as a property of regex matching, never a verdict on whether the skill's documentation should have warned about it harder |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the undemonstrated
  `block` action, the undocumented `stop`/`prompt` condition fields, and the
  undefined rule-execution order as "what it gets right" / "where it bites"
  — Teardown language. Plain keeps the underlying fact that precisely two
  pitfalls sit on either side of pattern-writing (too broad, too narrow) but
  states it as a property of regex matching, not a critique of the skill's
  documentation.
- **Not that every rule needs `conditions`.** The source is explicit that
  the simple single-`pattern` field is the common case; the advanced
  `conditions` array (field + operator + pattern, all must match) is for
  when one field alone can't say it. This reel keeps both, foregrounding the
  simple form since the anchor only needs it.
- **No claim that `warn` blocks anything.** `action` defaults to `warn`,
  which still lets the operation through — only an explicit `block` stops
  it, exactly as the source states.

## Handoff prompt (BHTF, read aloud)

> "Create a hookify rule that blocks rm -rf commands, and one that warns
> when editing .env files."

Why it's worth running: watching whether Claude sets `action: block` (not
the default `warn`) on the dangerous rule, and reaches for a `conditions`
check on `file_path` rather than only the new text being written on the
`.env` rule, surfaces whether the pattern-precision distinction from B03
actually lands — this is the source's own worked example.

---
**GATE P — signed:** ______________________  (human)
