# CHECKS-REPORT.md — "Just talk to it"

QC gate run 2026-10-03, in `~/workspace/film-builds/how-to-ai/just-talk-to-it/`.

## 1. `python3 -m py_compile`

- `make_sheet.py` — clean.
- `scenes.py` — clean.

## 2. `static_scene_check.py scenes.py --class <ClassName>` (all 12 classes)

| Class | Result |
|---|---|
| B00_MicHero | 1 clean · 0 warn · 0 error |
| B01_StartTalk | 1 clean · 0 warn · 0 error |
| B02_Brainstorm | 1 clean · 0 warn · 0 error |
| B03_KitchenHands | 1 clean · 0 warn · 0 error |
| B04_ToughTalk | 1 clean · 0 warn · 0 error |
| B05_Language | 1 clean · 0 warn · 0 error |
| B06_KeepIt | 1 clean · 0 warn · 0 error |
| B07_Precise | 1 clean · 0 warn · 0 error |
| B08_PublicPlaces | 1 clean · 0 warn · 0 error |
| B09_FullThoughts | 1 clean · 0 warn · 0 error |
| B10_Interrupt | 1 clean · 0 warn · 0 error |
| B11_Summarize | 1 clean · 0 warn · 0 error |

**Total: 12 clean · 0 warnings · 0 errors.** The check ran with
`beat_sheet.json` beside `scenes.py`, so the `until()` narration pacing
executed against the real sheet (no fallbacks, no missing-phrase silences —
every `until()` phrase was additionally verified present verbatim in its
beat's narration; see BUILD-LOG.md).

## 3. Failures and fixes

- One self-inflicted failure: `make_sheet.py`'s beat-count assertion said 17;
  the true count is 16 (12 body + BIDEA + BDEFS + BHTF + BOUT). Fixed the
  assertion; the beat list was already correct. No checker failures at all —
  the first `static_scene_check` pass was clean for every class, so there was
  nothing to fix and nothing was waived.

## 4. Deferred (cannot run in this VM)

- `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict` —
  requires Manim/pangocairo, not installed here. Deferred to Bear's Mac render
  pass (see CLAUDE-CODE-RENDER.md). Mitigation: all explicit coordinates are
  inside ±6.2 × ±3.3, all type ≥ 36 px, labels sit beside objects with leader
  gaps, terracotta is used only for dots/checks/glow, and every scene's motion
  completes in the first ~40% of its beat (GATE T samples the midpoint).
