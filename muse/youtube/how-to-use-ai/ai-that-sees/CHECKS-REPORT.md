# CHECKS-REPORT.md — "AI that sees"

QC gate run 2026-10-04, in `~/workspace/film-builds/how-to-ai/ai-that-sees/`.

## 1. `python3 -m py_compile`

- `make_sheet.py` — clean.
- `scenes.py` — clean.

## 2. `static_scene_check.py scenes.py --class <ClassName>` (all 12 classes)

| Class | Result |
|---|---|
| B00_PhotoHero | 1 clean · 0 warn · 0 error |
| B01_HowVision | 1 clean · 0 warn · 0 error |
| B02_ErrorShot | 1 clean · 0 warn · 0 error |
| B03_Receipt | 1 clean · 0 warn · 0 error |
| B04_Plant | 1 clean · 0 warn · 0 error |
| B05_Form | 1 clean · 0 warn · 0 error |
| B06_WhichOne | 1 clean · 0 warn · 0 error |
| B07_Handwriting | 1 clean · 0 warn · 0 error |
| B08_ClearPhoto | 1 clean · 0 warn · 0 error |
| B09_PointIt | 1 clean · 0 warn · 0 error |
| B10_SayWhat | 1 clean · 0 warn · 0 error |
| B11_KeepItPrivate | 1 clean · 0 warn · 0 error |

**Total: 12 clean · 0 warnings · 0 errors.** The check ran with
`beat_sheet.json` beside `scenes.py`, so the `until()` narration pacing
executed against the real sheet (no fallbacks, no missing-phrase silences —
every `until()` phrase was additionally verified present verbatim in its
beat's narration; see BUILD-LOG.md).

## 3. Failures and fixes

None. `make_sheet.py` passed its own assertions on the first run (16 beats,
12 manim, ~247 s total inside the 170–280 s band; BDEFS terms all ≤ 17
characters; hesitant-writer trigger contract holds), and the first
`static_scene_check` pass was clean for every class, so there was nothing to
fix and nothing was waived.

## 4. Deferred (cannot run in this VM)

- `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict` —
  requires Manim/pangocairo, not installed here. Deferred to Bear's Mac render
  pass (see CLAUDE-CODE-RENDER.md). Mitigation: all explicit coordinates are
  inside ±6.2 × ±3.3, all type ≥ 40 px, labels sit beside objects with leader
  gaps, terracotta is used only for the pupil spark / scan line / checks /
  the sun dot, and every scene's motion completes in the first ~40% of its
  beat (GATE T samples the midpoint).
