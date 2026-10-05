# CHECKS-REPORT.md — "Fix your photos"

QC gate run 2026-10-05, in `~/workspace/film-builds/how-to-ai/fix-your-photos/`.

## 1. `python3 -m py_compile`

- `make_sheet.py` — clean.
- `scenes.py` — clean.

## 2. `static_scene_check.py scenes.py --class <ClassName>` (all 10 classes)

| Class | Result |
|---|---|
| B00_PhotoHero | 1 clean · 0 warn · 0 error |
| B01_Companion | 1 clean · 0 warn · 0 error |
| B02_Remove | 1 clean · 0 warn · 0 error |
| B03_Invent | 1 clean · 0 warn · 0 error |
| B04_Light | 1 clean · 0 warn · 0 error |
| B05_Straighten | 1 clean · 0 warn · 0 error |
| B06_Copy | 1 clean · 0 warn · 0 error |
| B07_Check | 1 clean · 0 warn · 0 error |
| B08_MadeThing | 1 clean · 0 warn · 0 error |
| B09_Print | 1 clean · 0 warn · 0 error |

**Total: 10 clean · 0 warnings · 0 errors.** The check ran with
`beat_sheet.json` beside `scenes.py`, so the `until()` narration pacing
executed against the real sheet (no fallbacks, no missing-phrase silences —
every `until()` phrase was additionally verified present verbatim in its
beat's narration; see BUILD-LOG.md).

## 3. Failures and fixes

None. `make_sheet.py` passed its own assertions on the first run (14 beats,
10 manim, ~216 s total inside the 170–280 s band; BDEFS terms all ≤ 17
characters; hesitant-writer trigger contract holds), and the first
`static_scene_check` pass was clean for every class, so there was nothing to
fix and nothing was waived.

## 4. Deferred (cannot run in this VM)

- `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict` —
  requires Manim/pangocairo, not installed here. Deferred to Bear's Mac render
  pass (see CLAUDE-CODE-RENDER.md). Mitigation: all explicit coordinates are
  inside ±6.2 × ±3.3, all type ≥ 40 px, labels sit beside objects with leader
  gaps, terracotta is used only for the eraser rings / sun dots / checks /
  the invented-region outline, and every scene's motion completes in the
  first ~40% of its beat (GATE T samples the midpoint).
