# CHECKS-REPORT.md — "How to outsource everything to AI & get dumb"

QC gate record, 2026-10-03. Pre-render package: static checks only (no render yet).

## Gate 1 — py_compile
- `python3 -m py_compile make_sheet.py` → clean.
- `python3 -m py_compile scenes.py` → clean.

## Gate 2 — make_sheet.py self-assertions (run 2026-10-03)
All passed: 14 beats in exact order (BIDEA, BDEFS, B00–B09, BHTF, BOUT); 10 manim +
4 bookend lanes; total estimated duration 238.8 s (inside the 200–320 s band); every
manim class name starts with its beat id; BIDEA triggerWords verbatim in text and
punctuation-free; all BDEFS terms ≤ 17 chars; BOUT is outro_voice with 1.0 s tail;
every beat voice am_onyx / engine kokoro with a non-empty show block.

## Gate 3 — static_scene_check.py (one run per class, 2026-10-03)
`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`

| Class | Result |
|---|---|
| B00_Hero | clean · 0 warn · 0 error |
| B01_PasteHope | clean · 0 warn · 0 error |
| B02_OneLine | clean · 0 warn · 0 error |
| B03_ThinkFirst | clean · 0 warn · 0 error |
| B04_HandOver | clean · 0 warn · 0 error |
| B05_YouDecide | clean · 0 warn · 0 error |
| B06_ThreeDomains | clean · 0 warn · 0 error |
| B07_GPSBrain | clean · 0 warn · 0 error |
| B08_EightyThree | clean · 0 warn · 0 error |
| B09_FastTrap | clean · 0 warn · 0 error |

**10 clean · 0 warn · 0 error. No failures, no fixes needed** — first run was clean.

## Gate 4 — manual pre-gate review (author's pass before the checker ran)
- Every explicit coordinate in helpers and scenes verified inside ±6.2 × ±3.3
  (checker SAFE bounds ±6.3 × ±3.4; hard frame ±7.12 × ±4.05).
- Text floor: all `T()` calls size ≥ 32 (captions at 32, labels 32–36, hero numbers 64–96).
- Labels sit beside objects, never inside outlines, never on terracotta fill.
- Terracotta budget per beat: spark / brain dots / one ring dot only; gauges and
  chart segments use BAR1/ghost greys; B02's ring drawn in ink (curve rule).
- No `rate_functions.ease_in_quad` / `ease_out_cubic` (kit's `ease_in` unused here —
  no eased anims); no `animate(path_arc=…)` (MoveAlongPath + ArcBetweenPoints used);
  `get_center()` wrapped in `np.array(...)` before arithmetic; no group slices.
- Every `until()` phrase verified verbatim in its beat's narration text.
- Class names literally `class BNN_Name(Scene):` (run.sh discovery).
- Continuity: AI box + worker recur B00→B02→B04→B09; draft + constraints B03→B04.

## Open / deferred to render time
- manim_layout_audit + real 4K render happen on Bear's Mac (see CLAUDE-CODE-RENDER.md).
- FACTCHECK.md claim #6 (11% no-AI figure): verify against arXiv:2506.08872 before final;
  the B08 beat works with the right meter removed if it doesn't check out.
