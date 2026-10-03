# TYPECHECK.md — GATE T

Reel: `ogilvy-xinchen`  |  Checked: 2026-08-01T04:51  |  Overall: **FAIL**  |  Beats checked: 10  |  FAILs: 3

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B01 | ? | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| B02 | ? | min-size §8.1: smallest text run 32px < floor 35px (3.2% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B03 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B04 | ? | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| B05 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B06 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| BVDT | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 97px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

### B01 (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

### B02 (?)
- **min-size §8.1**: smallest text run 32px < floor 35px (3.2% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Increase font_size in scenes.py or Remotion component

### B04 (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 10 | 1 |
| overflow §8.2 | 10 | 0 |
| contrast §8.3 | 10 | 3 |
| contrast-local §8.3b | 10 | 0 |
| bbox-overlap §8.6b | 10 | 0 |
| kerning §8.4 | 6 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
