# TYPECHECK.md — GATE T

Reel: `claude-liam-madison-brand-guidebook`  |  Checked: 2026-08-28T01:58  |  Overall: **FAIL**  |  Beats checked: 40  |  FAILs: 8

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 52px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B06 | ? | light | min-size §8.1: no text-run blobs above noise threshold — the filter discarded every candid… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B07 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | ? | light | min-size §8.1: no text-run blobs above noise threshold — the filter discarded every candid… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B12 | ? | light | min-size §8.1: min text-run height 54px >= floor 41px | PASS | — |
| B13 | ? | light | min-size §8.1: no text-run blobs above noise threshold — the filter discarded every candid… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B14 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | ? | light | min-size §8.1: min text-run height 58px >= floor 41px | PASS | — |
| B17 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | ? | light | min-size §8.1: min text-run height 68px >= floor 41px | PASS | — |
| B19 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | ? | light | min-size §8.1: smallest text run 40px < floor 41px (1.9% of 2160px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B22 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B23 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B24 | ? | light | min-size §8.1: no text-run blobs above noise threshold — the filter discarded every candid… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B25 | ? | light | min-size §8.1: no text-run blobs above noise threshold — the filter discarded every candid… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B26 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B27 | ? | light | min-size §8.1: no text-run blobs above noise threshold — the filter discarded every candid… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B28 | ? | light | min-size §8.1: min text-run height 60px >= floor 41px | PASS | — |
| B29 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B31 | ? | light | min-size §8.1: smallest text run 35px < floor 41px (1.9% of 2160px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B32 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B33 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B34 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B35 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B36 | ? | light | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| B37 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B39 | ? | light | min-size §8.1: min text-run height 52px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

### B06 (?)
- **min-size §8.1**: no text-run blobs above noise threshold — the filter discarded every candidate, which is what sub-floor type looks like; cannot verify (SHOW-LESS.md)
- **Fix:** Increase font_size in scenes.py or Remotion component

### B11 (?)
- **min-size §8.1**: no text-run blobs above noise threshold — the filter discarded every candidate, which is what sub-floor type looks like; cannot verify (SHOW-LESS.md)
- **Fix:** Increase font_size in scenes.py or Remotion component

### B13 (?)
- **min-size §8.1**: no text-run blobs above noise threshold — the filter discarded every candidate, which is what sub-floor type looks like; cannot verify (SHOW-LESS.md)
- **Fix:** Increase font_size in scenes.py or Remotion component

### B21 (?)
- **min-size §8.1**: smallest text run 40px < floor 41px (1.9% of 2160px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B24 (?)
- **min-size §8.1**: no text-run blobs above noise threshold — the filter discarded every candidate, which is what sub-floor type looks like; cannot verify (SHOW-LESS.md)
- **Fix:** Increase font_size in scenes.py or Remotion component

### B25 (?)
- **min-size §8.1**: no text-run blobs above noise threshold — the filter discarded every candidate, which is what sub-floor type looks like; cannot verify (SHOW-LESS.md)
- **Fix:** Increase font_size in scenes.py or Remotion component

### B27 (?)
- **min-size §8.1**: no text-run blobs above noise threshold — the filter discarded every candidate, which is what sub-floor type looks like; cannot verify (SHOW-LESS.md)
- **Fix:** Increase font_size in scenes.py or Remotion component

### B31 (?)
- **min-size §8.1**: smallest text run 35px < floor 41px (1.9% of 2160px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 30 | 0 |
| min-size §8.1 | 40 | 8 |
| overflow §8.2 | 40 | 0 |
| contrast §8.3 | 40 | 0 |
| contrast-local §8.3b | 40 | 0 |
| bbox-overlap §8.6b | 40 | 0 |
| card-clip §8.13 | 40 | 0 |
| kerning §8.4 | 6 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
