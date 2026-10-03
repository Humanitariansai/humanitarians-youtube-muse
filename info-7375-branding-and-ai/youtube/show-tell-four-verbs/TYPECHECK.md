# TYPECHECK.md — GATE T

Reel: `show-tell-four-verbs`  |  Checked: 2026-09-27T21:12  |  Overall: PASS  |  Beats checked: 14  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B07] narration recites the card (1.00) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | bookend | light | min-size §8.1: min text-run height 60px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B00 | manim | light | min-size §8.1: min text-run height 485px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B01 | manim | light | min-size §8.1: min text-run height 297px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B02 | manim | light | min-size §8.1: min text-run height 177px >= floor 41px | PASS | — |
| B03 | manim | light | min-size §8.1: min text-run height 66px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B04 | manim | light | min-size §8.1: min text-run height 113px >= floor 41px | PASS | — |
| B05 | card | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | manim | light | min-size §8.1: min text-run height 66px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B07 | card | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | card | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | manim | light | min-size §8.1: min text-run height 66px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | dark | min-size §8.1: min text-run height 239px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 4 | 0 |
| min-size §8.1 | 14 | 0 |
| overflow §8.2 | 14 | 0 |
| contrast §8.3 | 14 | 0 |
| contrast-local §8.3b | 14 | 0 |
| bbox-overlap §8.6b | 14 | 0 |
| card-clip §8.13 | 14 | 0 |
| kerning §8.4 | 7 | 0 |
| redundancy §8.10 (advisory) | 3 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
