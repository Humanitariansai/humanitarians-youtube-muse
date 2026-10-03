# Claude, Analyzing Financial Statements — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:55.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone wonders how you'd teach Claude to analyze financial statements. But Claude isn't trained for this — it's pointed at a skill it reads before acting. So: how do you point it at one?" | BrutalistHesitantWriter — types "How do I teach Claude to analyze financial statements?", corrects "teach" → "point" |
| B01 | 1 stakes / 2 wrong guess, falsified | A skill is a folder Claude reads before it works — not something it's trained on. This one is analyzing-financial-statements: calculate_ratios.py, interpret_ratios.py, and a two-kilobyte SKILL.md holding the full instruction set, plain language, no hidden logic. Claude reads the file, then acts. The file is the program. | a folder opens into three files; SKILL.md highlighted; "not trained on it" callout crosses a brain glyph; "the file is the program" closer |
| B02 | 3 mechanism / **4 anchor planted** | The instructions sit in a Steps section: read each step in order, execute it, return the result — linear, no branching unless a step says so. Watch the anchor. Hand the skill a balance sheet: it reads the numbers, runs calculate_ratios.py, and hands back the ratios. Same three steps, every time. | three phase cards (read SKILL.md / execute / return result); THE ANCHOR — balance sheet → calculate_ratios.py → ratios out |
| B03 | **4 anchor payoff / 5 both directions** | Same input, same output, every run — hand it the identical balance sheet twice and calculate_ratios.py returns the identical ratios both times. That's the payoff of a file being the program. But the reverse holds too: hand it a statement the steps weren't written for, and it still runs those same steps — against numbers the SKILL.md never specified. The limit is the spec: only what it names. | THE ANCHOR RETURNS — the same pipeline firing twice identically, then split: in-spec statement → clean ratios (the payoff); statement outside the spec → same steps run anyway (the limit) |
| **BCRY** | **6 carry-out** | A financial-analysis skill isn't Claude reasoning about finance on its own — it's SKILL.md, a spec Claude reads and runs the same way against whatever statement you hand it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I want to analyze financial statements for investment insights. Read the analyzing-financial-statements skill and walk me through what you will do before you do it. Watch for that walk-through — explaining first is what surfaces which ratios it's about to run, and which steps SKILL.md actually specifies. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Analyzing Financial Statements. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder-not-training fact; the Steps/anchor mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (teach Claude); B01 falsifies it with a case — a skill is a folder Claude reads, not something it's trained on, and the file is the program |
| Exactly one inference flag | none needed — every claim is read directly off the source's own narrated description of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (hand the skill a balance sheet; calculate_ratios.py runs the same three steps) |
| Both directions | B03 — the same statement twice returns identical ratios (the payoff); a statement outside the spec still runs the same steps (the limit) |
| No design judgment | B03 states spec precision as a property of running a fixed set of steps, never a verdict on whether the skill's SKILL.md should have covered more |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03 framed "what it gets
  right: repeatable results" and "what it bites: anything outside the spec"
  as Teardown language. Plain keeps the underlying fact — reliable inside
  the spec, indifferent to what's outside it — but states it as a property
  of running fixed steps, not a critique of the skill's documentation.
- **No specific ratio names or formulas.** The source SKILL.md itself isn't
  available on this machine; this reel states only what the source's own
  narration already names ("key financial ratios and metrics ... for
  investment analysis") and invents nothing further.
- **Not a claim that the skill validates its input.** Only that it runs the
  same steps regardless of whether the statement fits what SKILL.md
  specifies.

## Handoff prompt (BHTF, read aloud)

> "I want to analyze financial statements for investment insights. Read the
> analyzing-financial-statements skill and walk me through what you will do
> before you do it."

Why it's worth running: this is the source's own worked example. Asking
Claude to explain first — before running the skill — is what surfaces which
ratios it's about to compute and which steps its `SKILL.md` actually
specifies, rather than only seeing the finished numbers.

---
**GATE P — signed:** ______________________  (human)
