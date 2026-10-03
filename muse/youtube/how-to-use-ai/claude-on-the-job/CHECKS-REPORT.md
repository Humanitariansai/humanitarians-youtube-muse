# CHECKS-REPORT.md — "Claude, On the Job."

QC gate results for the pre-render package, 2026-10-03.

## Gate 1 — `py_compile`

| File | Result |
|---|---|
| `make_sheet.py` | clean |
| `scenes.py` | clean |

## Gate 2 — `make_sheet.py` self-assertions

13 beats (expected 13); total estimated duration 176 s (bounds 120–360 s);
every beat has non-empty narration, voice `am_onyx`, engine `kokoro`,
positive duration; all 9 body beats `lane: manim`, `shot.type: GRAPHIC`,
`shot.source: own`, class name prefixed with the beat id, sparse-by-design
waiver present; BIDEA trigger "win the race" verbatim in the writer text,
no trailing punctuation on trigger/replacement, `lead_silence_s: 0.8`;
BDEFS has 4 terms, all ≤ 17 chars; BOUT `kind: outro_voice`,
`tail_silence_s: 1.0`. All passed on every run.

## Gate 3 — static scene check

`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <ClassName>`
(run in the build folder, `beat_sheet.json` beside `scenes.py`):

| Class | Result |
|---|---|
| B00_TierMap | 1 clean · 0 warn · 0 error |
| B01_TierOne | 1 clean · 0 warn · 0 error (after fix, see below) |
| B02_Contested | 1 clean · 0 warn · 0 error |
| B03_Judgment | 1 clean · 0 warn · 0 error |
| B04_Irreducible | 1 clean · 0 warn · 0 error |
| B05_Conducting | 1 clean · 0 warn · 0 error |
| B06_DailyLoop | 1 clean · 0 warn · 0 error |
| B07_NeverDelegate | 1 clean · 0 warn · 0 error |
| B08_YoursAlone | 1 clean · 0 warn · 0 error |

Total: 9/9 scenes, 0 warnings, 0 errors.

## Failures and fixes

1. **B01_TierOne — "shapes never change" (error).** The five output pages
   entered the scene via `animate.shift()` from off-stage positions; the
   stub snapshots only after each `play` and ignores moves, so no new shape
   ever registered, and the human→ghost swap was shape-identical. Fixed by
   having each page enter with `FadeIn(page, shift=DOWN*1.4)` — one genuinely
   new non-text shape per play, and the fast drop doubles as the beat's
   motion claim (superhuman recall speed). The beat's `visual_intent` in
   `make_sheet.py` was updated to match and the sheet regenerated. Re-ran:
   clean.
2. **Preventive fixes (before any checker run):** replaced all VGroup
   indexing with plain Python lists (`tasks_list`, `pill_list`, `cap_list`);
   replaced a `VGroup` iteration with the underlying list; all label
   coordinates are fixed literals (no `get_center()` arithmetic, per the
   skill's Gate-A stub traps); no `ease_in_quad`/`ease_out_cubic`,
   `path_arc`, `Indicate`, or group slices anywhere in the file.

## Not run (render-side gates)

Gates A, B, V, T, `manim_layout_audit.py`, `bookend_check.py`, and
`factcheck_check.py` run on Bear's Mac at render time; see
CLAUDE-CODE-RENDER.md. The static gate above is the package-time gate, and
it is green.
