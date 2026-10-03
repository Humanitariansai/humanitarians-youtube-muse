# Claude, Creating Financial Models — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone wonders how you'd teach Claude to build financial models. But Claude isn't trained for this — it's pointed at a skill it reads before acting. So: how do you point it at one?" | BrutalistHesitantWriter — types "How do I teach Claude to build financial models?", corrects "teach" → "point" |
| B01 | 1 stakes / 2 wrong guess, falsified | A skill is a folder Claude reads before it works — not something it's trained on. This one is creating-financial-models: dcf_model.py, sensitivity_analysis.py, and a four-kilobyte SKILL.md holding the full instruction set, plain language, no hidden logic. Claude reads the file, then acts. The file is the program. | a folder opens into three files; SKILL.md highlighted; "not trained on it" callout crosses a brain glyph; "the file is the program" closer |
| B02 | 3 mechanism / **4 anchor planted** | The instructions sit in a Steps section: read each step in order, execute it, return the result — linear, no branching unless a step says so. Watch the anchor. Hand the skill a five-year revenue projection: it reads the assumptions, runs dcf_model.py, and hands back a valuation. Same three steps, every time. | three phase cards (read SKILL.md / execute / return result); THE ANCHOR — revenue projection → dcf_model.py → valuation out |
| B03 | **4 anchor payoff / 5 both directions** | Same input, same output, every run — hand it the identical revenue projection twice and dcf_model.py returns the identical valuation both times. That's the payoff of a file being the program. But the reverse holds too: hand it a projection the steps weren't written for, and it still runs those same steps — against numbers the SKILL.md never specified. The limit is the spec: DCF analysis, sensitivity testing, Monte Carlo simulations, scenario planning — and nothing outside it. | THE ANCHOR RETURNS — the same pipeline firing twice identically, then split: in-spec projection → clean valuation (the payoff); projection outside the spec → same steps run anyway (the limit) |
| **BCRY** | **6 carry-out** | A financial-modeling skill isn't Claude inventing a model from judgment — it's SKILL.md, a spec Claude reads and runs the same way against whatever numbers you hand it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I want to stress-test a five-year revenue projection. Read the creating-financial-models skill and walk me through what you will build before you touch a number. Watch for that clause — before you touch a number — that's the discipline the spec enforces: the plan is visible before the model runs. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Creating Financial Models. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder-not-training fact; the Steps/anchor mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (teach Claude); B01 falsifies it with a case — a skill is a folder Claude reads, not something it's trained on, and the file is the program |
| Exactly one inference flag | none needed — every claim is read directly off the source's own narrated description of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (hand the skill a five-year revenue projection; dcf_model.py runs the same three steps) |
| Both directions | B03 — the same projection twice returns identical valuations (the payoff); a projection outside the spec still runs the same steps (the limit) |
| No design judgment | B03 states spec precision as a property of running a fixed set of steps, never a verdict on whether the skill's SKILL.md should have covered more |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03 framed "what it gets
  right: repeatable results" and "what it bites: anything outside the
  spec" as Teardown language. Plain keeps the underlying fact — reliable
  inside the spec, indifferent to what's outside it — but states it as a
  property of running fixed steps, not a critique of the skill's
  documentation.
- **No specific formulas or parameters.** The source SKILL.md itself isn't
  available on this machine; this reel states only what the source's own
  narration already names ("DCF analysis, sensitivity testing, Monte Carlo
  simulations, and scenario planning for investment decisions") and
  invents nothing further.
- **Not a claim that the skill validates its input.** Only that it runs
  the same steps regardless of whether the projection fits what SKILL.md
  specifies.

## Handoff prompt (BHTF, read aloud)

> "I want to stress-test a five-year revenue projection. Read the
> creating-financial-models skill and walk me through what you will build
> before you touch a number."

Why it's worth running: this is the source's own worked example. Asking
Claude to explain first — before it runs the skill — is what surfaces
which parts of the suite (DCF, sensitivity, Monte Carlo, scenario
planning) it's about to use, and which assumptions it's about to build on,
rather than only seeing the finished numbers.

---
**GATE P — signed:** ______________________  (human)
