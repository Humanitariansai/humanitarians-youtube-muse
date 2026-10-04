# CHECKS-REPORT.md — Tame Your Spreadsheets

QC gate per the show-tell skill (step 4 of the workflow). 2026-10-03.

## 1. py_compile

```
python3 -m py_compile make_sheet.py scenes.py
```
Result: clean, no output. [record]

## 2. static_scene_check.py (per scene class)

```
python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <ClassName>
```

| Class | Result |
|---|---|
| B00_MessySheet | 1 clean · 0 warn · 0 error |
| B01_Coach | 1 clean · 0 warn · 0 error |
| B02_Formula | 1 clean · 0 warn · 0 error |
| B03_Check | 1 clean · 0 warn · 0 error |
| B04_Cleanup | 1 clean · 0 warn · 0 error |
| B05_Insight | 1 clean · 0 warn · 0 error |
| B06_Payoff | 1 clean · 0 warn · 0 error |

Total: 7 clean · 0 warn · 0 error. No failures, no fixes needed — the scenes
passed on the first run. The checker confirmed: every `construct()` executes
start→finish, no generic-art repetition (distinct shape states per beat),
all coordinates inside the 16:9 frame.

Pre-run self-review notes (applied while writing, before the checker ran):
- Class names written literally as `class BNN_Name(Scene):` (run.sh lookup).
- No `rate_functions.ease_in_quad` / `ease_out_cubic`; kit `ease_in` only.
- No `path_arc` on `.animate`; the one `.animate` (B04 scan sweep) is a plain
  shift. No `MoveAlongPath` + `.animate` on the same object in one play.
- `triggerWords`/`replacementWords` ("learn Excel" → "tame this spreadsheet")
  contain no trailing punctuation; trigger appears verbatim in `text`.
- Every scene adds ≥1 new non-text shape after its first frame
  (Create/GrowFromCenter/FadeIn of a new shape).
- Terracotta used only for dots and the scan line (never text, never thin
  bars); the scan sweep lands well before the beat midpoint (GATE T samples
  at midpoint).
- Labels sit beside objects with clear leader lines; all text ≥32; all
  coordinates inside ±6.2 × ±3.3.
- `until()` phrases copied verbatim from each beat's `narration_text`.

## 3. Deferred

`runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict` could
not run in this VM (no Manim/pangocairo installed). Deferred to Bear's Mac
render pass — see CLAUDE-CODE-RENDER.md step 5.
