# TYPECHECK.md — GATE T

Reel: `ogilvy-duc`  |  Checked: 2026-07-31T21:48  |  Overall: PASS  |  Beats checked: 10  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B01 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B02 | ? | min-size §8.1: min text-run height 80px >= floor 35px | PASS | — |
| B03 | ? | min-size §8.1: min text-run height 73px >= floor 35px | PASS | — |
| B04 | ? | min-size §8.1: min text-run height 96px >= floor 35px | PASS | — |
| B05 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B06 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| BVDT | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 97px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 10 | 0 |
| overflow §8.2 | 10 | 0 |
| contrast §8.3 | 10 | 0 |
| contrast-local §8.3b | 10 | 0 |
| bbox-overlap §8.6b | 10 | 0 |
| kerning §8.4 | 6 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
