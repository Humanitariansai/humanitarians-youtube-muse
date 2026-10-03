# TYPECHECK.md — GATE T

Reel: `ogilvy-tanaka`  |  Checked: 2026-08-01T15:51  |  Overall: **FAIL**  |  Beats checked: 10  |  FAILs: 1

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B01 | ? | contrast-local §8.3b: per-blob contrast 1.09:1 < 3.0:1 — text unreadable on actual local b… | **FAIL** | Use INK on cream; add backing plate under accent text |
| B02 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B03 | ? | min-size §8.1: min text-run height 357px >= floor 35px | PASS | — |
| B04 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B05 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B06 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| BVDT | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 97px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

### B01 (?)
- **contrast-local §8.3b**: per-blob contrast 1.09:1 < 3.0:1 — text unreadable on actual local background (blob@(1508,540)–(2331,612) fg≈(66, 63, 63) bg≈(73, 68, 66)); move label off its background or change text color
- **Fix:** Use INK on cream; add backing plate under accent text

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 10 | 0 |
| overflow §8.2 | 10 | 0 |
| contrast §8.3 | 10 | 0 |
| contrast-local §8.3b | 10 | 1 |
| bbox-overlap §8.6b | 10 | 0 |
| kerning §8.4 | 6 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
