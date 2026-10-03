# Claude, Applying Brand Guidelines — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone wonders how you'd get Claude to match your brand. But matching a vibe isn't it — this skill applies a written spec. So: how does that work?" | BrutalistHesitantWriter — types "How do I get Claude to match our brand?", corrects "match" → "apply" |
| B01 | 1 stakes / 2 wrong guess, falsified | A skill is a folder Claude reads before it works — not something it's trained on. This one is applying-brand-guidelines: apply_brand.py, validate_brand.py, REFERENCE.md, and a four-kilobyte SKILL.md holding the full instruction set, plain language, no hidden logic. Claude reads the file, then acts. The file is the program. | a folder opens into four files; SKILL.md highlighted; "not trained on it" callout crosses a brain glyph; "the file is the program" closer |
| B02 | 3 mechanism / **4 anchor planted** | The instructions sit in a Steps section: read SKILL.md, execute each step in order, return the result — linear, no branching unless a step says so. Watch the anchor. Hand the skill a slide deck: it reads the deck, applies your colors and fonts, and hands back a branded deck. Same three steps, every time. | three phase cards (read SKILL.md / execute / return result); THE ANCHOR — slide deck → apply_brand.py → branded deck |
| B03 | **4 anchor payoff / 5 both directions** | Same input, same output, every run — hand it the identical deck twice and apply_brand.py returns the identical branding both times. That's the payoff of a file being the program. But the reverse holds too: hand it a document outside the stated scope — external communications only — and it still runs the same steps, against material the SKILL.md never specified. validate_brand.py is the check: wrong colors, wrong fonts, wrong scope, all caught the same way. | THE ANCHOR RETURNS — the same pipeline firing twice identically, then split: in-scope document → clean branding (the payoff); out-of-scope document → same steps run anyway (the limit), with validate_brand.py's check named on both sides |
| **BCRY** | **6 carry-out** | Applying brand guidelines isn't Claude developing its own sense of style — it's SKILL.md, a spec Claude reads, applies, and validates the same way against whatever document you hand it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I want to apply brand guidelines to my team's documents. Read the applying-brand-guidelines skill and walk me through what you will do before you do it. Watch for that walk-through — explaining first is what surfaces which steps SKILL.md actually specifies, and where the scope stops. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Applying Brand Guidelines. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder-not-training fact; the Steps/anchor mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (match a vibe); B01 falsifies it with a case — a skill is a folder Claude reads, not something it's trained on, and the file is the program |
| Exactly one inference flag | none needed — every claim is read directly off the source's own narrated description of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (hand the skill a slide deck; apply_brand.py runs the same three steps) |
| Both directions | B03 — the same deck twice returns identical branding (the payoff); a document outside the stated scope still runs the same steps (the limit) |
| No design judgment | B03 states scope precision as a property of running a fixed, checked set of steps, never a verdict on whether the skill's SKILL.md should have covered more |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03 framed the scope
  constraint and `validate_brand.py`'s falsifying role as Teardown-flavoured
  "design tell" language. Plain keeps the underlying fact — reliable inside
  the spec, checked the same way regardless of what's outside it — but
  states it as a property of running fixed, validated steps, not a critique
  of the skill's documentation.
- **No specific color codes, font names, or layout rules.** The source
  `SKILL.md` itself isn't available on this machine; this reel states only
  what the source's own narration already names (colors, fonts, layouts,
  messaging — kept at that level of generality).
- **Not a claim that the skill decides what counts as "on brand."** Only
  that it runs the same steps and the same check regardless of whether the
  document fits the stated scope.

## Handoff prompt (BHTF, read aloud)

> "I want to apply brand guidelines to my team's documents. Read the
> applying-brand-guidelines skill and walk me through what you will do
> before you do it."

Why it's worth running: this is the source's own worked example. Asking
Claude to explain first — before running the skill — is what surfaces which
steps its `SKILL.md` actually specifies, and where the stated scope stops,
rather than only seeing the finished, rebranded document.

---
**GATE P — signed:** ______________________  (human)
