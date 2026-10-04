# CHECKS-REPORT.md — "The first answer is a draft"

QC gate run 2026-10-03, in `~/workspace/film-builds/how-to-ai/the-first-answer-is-a-draft/`.

## 1. py_compile
- `python3 -m py_compile make_sheet.py` — clean.
- `python3 -m py_compile scenes.py` — clean.

## 2. static_scene_check.py (render-free QA, one run per scene class)
`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <ClassName>`

| class | result |
|---|---|
| B00_DraftOne | clean · 0 warn · 0 error |
| B01_TooEarly | clean · 0 warn · 0 error |
| B02_FirstTry | clean · 0 warn · 0 error |
| B03_Shorter | clean · 0 warn · 0 error |
| B04_Concrete | clean · 0 warn · 0 error |
| B05_BusyParent | clean · 0 warn · 0 error |
| B06_SideBySide | clean · 0 warn · 0 error |
| B07_Drift | clean · 0 warn · 0 error |
| B08_Recipe | clean · 0 warn · 0 error |

**Total: 9 clean · 0 warnings · 0 errors.** First run; no failures to fix. (One pre-QC self-catch — the B01 stamp start position at y=3.6 — was corrected before the checker ran; see BUILD-LOG.md.)

## 3. Not run here (deferred to Bear's Mac)
- `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict` — cannot run in this VM (no Manim/pangocairo). Deferred to the render pass on Bear's Mac; CLAUDE-CODE-RENDER.md carries the instruction.
- Audio generation (Kokoro am_onyx), stills, 4K render, Gates A/B/V/T — all happen on Bear's Mac per CLAUDE-CODE-RENDER.md.

## 4. make_sheet.py self-assertions (run at generation)
13 beats · 9 manim classes matching beat ids · sparse_by_design waiver on all 9 manim beats · BIDEA trigger verbatim + punctuation-free · BDEFS terms ≤ 17 chars · BHTF reads the full prompt · BOUT 1.0 s tail · bookend_exempt ["cold-open","bvdt"] · total estimated duration 150 s. All passed.
