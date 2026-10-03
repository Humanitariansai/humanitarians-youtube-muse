# TYPECHECK.md — GATE T

Reel: `review-satwika`  |  Checked: 2026-08-16T23:30  |  Overall: **FAIL**  |  Beats checked: 14  |  FAILs: 7

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: min text-run height 43px >= floor 35px | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: prose element 'body': 22 words > 12 pull-quote limit. The screen shoul… | **FAIL** | De-wordify → Manim diagram or Remotion build-on |
| B02 | ? | — | no video | SKIP | — |
| B03 | ? | — | no video | SKIP | — |
| B04 | ? | light | no-wordy-card §8.5: prose element 'body': 17 words > 12 pull-quote limit. The screen shoul… | **FAIL** | De-wordify → Manim diagram or Remotion build-on |
| B05 | ? | — | no video | SKIP | — |
| B06 | ? | light | no-wordy-card §8.5: prose element 'body': 20 words > 12 pull-quote limit. The screen shoul… | **FAIL** | De-wordify → Manim diagram or Remotion build-on |
| B07 | ? | light | no-wordy-card §8.5: prose element 'body': 28 words > 12 pull-quote limit. The screen shoul… | **FAIL** | De-wordify → Manim diagram or Remotion build-on |
| B08 | ? | light | no-wordy-card §8.5: prose element 'body': 30 words > 12 pull-quote limit. The screen shoul… | **FAIL** | De-wordify → Manim diagram or Remotion build-on |
| B09 | ? | light | no-wordy-card §8.5: prose element 'body': 23 words > 12 pull-quote limit. The screen shoul… | **FAIL** | De-wordify → Manim diagram or Remotion build-on |
| B10 | ? | light | no-wordy-card §8.5: prose element 'body': 25 words > 12 pull-quote limit. The screen shoul… | **FAIL** | De-wordify → Manim diagram or Remotion build-on |
| BVDT | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | ? | light | min-size §8.1: min text-run height 43px >= floor 35px | PASS | — |
| BOUT | ? | dark | min-size §8.1: min text-run height 66px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

### B01 (?)
- **no-wordy-card §8.5**: prose element 'body': 22 words > 12 pull-quote limit. The screen should show structure, not sentences. De-wordify: shorten to a label or rebuild beat as a Manim/Remotion visual.
- **Fix:** De-wordify → Manim diagram or Remotion build-on

### B04 (?)
- **no-wordy-card §8.5**: prose element 'body': 17 words > 12 pull-quote limit. The screen should show structure, not sentences. De-wordify: shorten to a label or rebuild beat as a Manim/Remotion visual.
- **Fix:** De-wordify → Manim diagram or Remotion build-on

### B06 (?)
- **no-wordy-card §8.5**: prose element 'body': 20 words > 12 pull-quote limit. The screen should show structure, not sentences. De-wordify: shorten to a label or rebuild beat as a Manim/Remotion visual.
- **Fix:** De-wordify → Manim diagram or Remotion build-on

### B07 (?)
- **no-wordy-card §8.5**: prose element 'body': 28 words > 12 pull-quote limit. The screen should show structure, not sentences. De-wordify: shorten to a label or rebuild beat as a Manim/Remotion visual.
- **Fix:** De-wordify → Manim diagram or Remotion build-on

### B08 (?)
- **no-wordy-card §8.5**: prose element 'body': 30 words > 12 pull-quote limit. The screen should show structure, not sentences. De-wordify: shorten to a label or rebuild beat as a Manim/Remotion visual.
- **Fix:** De-wordify → Manim diagram or Remotion build-on

### B09 (?)
- **no-wordy-card §8.5**: prose element 'body': 23 words > 12 pull-quote limit. The screen should show structure, not sentences. De-wordify: shorten to a label or rebuild beat as a Manim/Remotion visual.
- **Fix:** De-wordify → Manim diagram or Remotion build-on

### B10 (?)
- **no-wordy-card §8.5**: prose element 'body': 25 words > 12 pull-quote limit. The screen should show structure, not sentences. De-wordify: shorten to a label or rebuild beat as a Manim/Remotion visual.
- **Fix:** De-wordify → Manim diagram or Remotion build-on

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 7 | 7 |
| min-size §8.1 | 11 | 0 |
| overflow §8.2 | 11 | 0 |
| contrast §8.3 | 11 | 0 |
| contrast-local §8.3b | 11 | 0 |
| bbox-overlap §8.6b | 11 | 0 |
| card-clip §8.13 | 11 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
