# CHECKS-REPORT.md — "Plan anything."

QC gate results for the pre-render package, 2026-10-03.

## Gate 1 — `py_compile`

| File | Result |
|---|---|
| `make_sheet.py` | clean |
| `scenes.py` | clean |

## Gate 2 — `make_sheet.py` self-assertions

12 beats (expected 12); total estimated duration 176.8 s (bounds 120–360 s);
every beat has non-empty narration, voice `am_onyx`, engine `kokoro`,
positive duration; all 8 body beats `lane: manim`, `shot.type: GRAPHIC`,
`shot.source: own`, class name prefixed with the beat id, sparse-by-design
waiver present; BIDEA trigger "Plan my whole weekend trip" verbatim in the
writer text, no trailing punctuation on trigger/replacement,
`lead_silence_s: 0.8`; BDEFS has 3 terms, all ≤ 17 chars; BOUT
`kind: outro_voice`, `tail_silence_s: 1.0`; BHTF composer greeting
"Your turn.", topic contains "YOUR TURN". All passed on the first run except
one fix, below.

## Gate 3 — static scene check

`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <ClassName>`
(run in the build folder, `beat_sheet.json` beside `scenes.py`):

| Class | Result |
|---|---|
| B00_TheLoop | 1 clean · 0 warn · 0 error |
| B01_Constraints | 1 clean · 0 warn · 0 error |
| B02_DraftItinerary | 1 clean · 0 warn · 0 error |
| B03_Revise | 1 clean · 0 warn · 0 error |
| B04_Checklist | 1 clean · 0 warn · 0 error |
| B05_Projects | 1 clean · 0 warn · 0 error |
| B06_Budgets | 1 clean · 0 warn · 0 error |
| B07_YouVerify | 1 clean · 0 warn · 0 error |

Total: 8/8 scenes, 0 warnings, 0 errors.

## Failures and fixes

1. **make_sheet.py self-assertion — BIDEA trigger not verbatim (error, first
   run).** The trigger `"plan my whole weekend trip"` (lowercase p) did not
   appear verbatim in the writer text `"Plan my whole weekend trip for me?"`
   (capital P). Fixed by capitalizing the trigger to match the text exactly;
   the component strips punctuation but not case, so the correction now fires.
   Re-ran: all assertions passed. [record]
2. **Preventive fixes (before any checker run):** all per-play changes use
   `FadeIn`/`Create`/`GrowFromCenter`/`FadeOut` of new shapes (never
   `.animate()`-only moves — the stub ignores moves); plain Python lists for
   `blocks`, `chips`, `stops`, `bars`, `segs`, `pills`, `caps`, `ticks` (no
   VGroup indexing or group slices); all label placement uses fixed literal
   coordinates (no `get_center()` arithmetic); no `rate_functions` easings,
   no `path_arc`, no `Indicate`; `ArcBetweenPoints` positions wrapped in
   `np.array(...)` per the Gate-A stub trap. [record]

## Not run (render-side gates)

Gates A, B, V, T, `manim_layout_audit.py` (`--curve-strict` cannot run in this
VM — no Manim/pangocairo), `bookend_check.py`, and `factcheck_check.py` run on
Bear's Mac at render time; see CLAUDE-CODE-RENDER.md. The static gate above is
the package-time gate, and it is green.
