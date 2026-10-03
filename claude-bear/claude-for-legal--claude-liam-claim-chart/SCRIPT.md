# Claude, Claim Chart — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose
narration was already real — see QUESTION.md). Register: **Plain**. 7 beats
≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone building a claim chart assumes a filled cell means proof. It doesn't — the real value is which cells can't be filled. The real question: where does the evidence actually run out, element by element?" | BrutalistHesitantWriter — types "Can Claude prove\nmy case with\na claim chart?", corrects "prove" → "map" |
| B01 | 1 stakes / 2 wrong guess, falsified | A legal claim breaks into separate elements, and each one needs its own proof. Build the chart, and the easy move is to treat a full grid as a strong case — every box has an entry, so every element must be covered. But a filled cell only shows a citation was found. It says nothing about whether that citation actually proves the element. | a chart grid filling in, cell by cell, each one glowing "covered" as it fills |
| B02 | 3 mechanism / **4 anchor planted** | A claim chart works element by element: for every element, it finds the passage that could support it and pin-cites the exact page and line. Watch two elements from the same claim: "a locking mechanism" turns up a citation straight to the product manual, page twelve. "A temperature sensor" turns up nothing in the same manual — no citation exists to put in that cell. | THE ANCHOR — two element rows on one chart: one cell fills with a pin cite, the other stays empty, flagged |
| B03 | **4 anchor payoff / 5 both directions** | So on this chart, the locking-mechanism cell reads "supported — manual, page twelve," and the temperature-sensor cell reads "no citation found" — a gap, flagged on purpose. A filled cell doesn't decide the case: a citation can be weak, or cover only part of the element. And a gap doesn't decide it either — it isn't proof the element fails, only proof no evidence has turned up yet. Either way, the chart shows exactly where to look next. | THE ANCHOR RETURNS — the two rows resolve, then split into "filled ≠ proven" and "gap ≠ failed" |
| **BCRY** | **6 carry-out** | The point of a claim chart isn't a full grid — it's a pin cite for what's supported, and a flag, element by element, for what's missing. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Paste in the claim language, element by element, along with the accused product's documentation. Then ask: for each element, find the exact passage that supports it, cite it, and flag any element with no citation as a gap — don't guess to fill it in. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Claim Chart. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the element-by-element proof burden; the pin-cite mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (a filled chart proves the case); the B02→B03 anchor falsifies it directly — the locking-mechanism cell fills, the temperature-sensor cell can't, and the second is the useful signal |
| Exactly one inference flag | none needed — the account states the source sheet's own real facts (pin-cited cells, gap detection as priority output) rather than inferring undocumented behavior; see QUESTION.md |
| One anchor, planted early, paid off late | B02 → B03 (one claim, two elements: locking mechanism cited, temperature sensor gapped) |
| Both directions | B03 — a filled cell doesn't decide the case (a citation can be weak or partial); a gap doesn't decide it either (it isn't proof the element fails, only that evidence hasn't turned up yet) |
| No design judgment | B01–B03 state what the chart's output means, never a verdict on the skill's or any drafter's design choices |

## Deliberately not claimed

- **Not that a gap means the claim fails.** The reel states plainly that a
  gap is not proof of failure — only proof no citation has been found yet.
- **Not that a full chart proves infringement or a cause of action.** A
  filled cell is a found and pinned citation, not an adjudicated fact.
- **No accusation that anyone drafted or argued in bad faith.** Treating a
  full grid as a strong case is presented as an ordinary, understandable
  read of the output, not a failure by any named person or team.

## Handoff prompt (BHTF, read aloud)

> "Paste in the claim language, element by element, along with the accused
> product's documentation. For each element, find the exact passage that
> supports it, cite it, and flag any element with no citation as a gap —
> don't guess to fill it in."

Why it's worth running: the exercise surfaces the same distinction the
reel is built around — a chart is only useful once you can tell its filled
cells from its gaps, not by how full it looks.

---
**GATE P — signed:** reconstructed per QUESTION.md; source narration was
real (not placeholder) so no new facts were invented, only re-registered
from Teardown to Plain.
