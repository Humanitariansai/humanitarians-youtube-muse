# CHECKS-REPORT.md — Make It Interview You First

QC gate run 2026-10-03, package `muse/youtube/how-to-use-ai/make-it-interview-you-first/`.

## Gate 1 — py_compile

| file | result |
|---|---|
| `make_sheet.py` | clean |
| `scenes.py` | clean |

## Gate 2 — static_scene_check (Gate A simulation)

Run from `/tmp/gatea/` holding **only** `scenes.py` — exactly what `art run`'s
Gate A sees. Command per class:
`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`

| class | warnings | errors | distinct shape states |
|---|---|---|---|
| B00_AskOnce | 0 | 0 | 3 |
| B01_AskFirst | 0 | 0 | 3 |
| B02_FiveQuestions | 0 | 0 | 5 |
| B03_BriefBuilt | 0 | 0 | 7 |
| B04_TailoredPlan | 0 | 0 | 5 |
| B05_SecondDemo | 0 | 0 | 4 |
| B06_SharpQuestions | 0 | 0 | 2 |
| B07_TheRule | 0 | 0 | 3 |

Also ran B03 with `beat_sheet.json` beside `scenes.py` to confirm the
`until()`/`finish()` pacing path executes: 0 warnings, 0 errors.

Additionally verified by script: every `until()` phrase appears verbatim in
its beat's `narration_text` (all 31 present).

## Gate 3 — make_sheet.py asserts

All asserts passed at generation time: 12 beats in the show-tell spine order;
total 194.8 s inside the 170–220 s band; every manim beat carries a
`shot.manim.class` named for its beat id; BIDEA `triggerWords` ("write the
perfect prompt") verbatim in `text`, trigger/replacement free of trailing
punctuation; all BDEFS terms ≤ 17 chars; BHTF topic contains "YOUR TURN",
greeting exactly "Your turn.", two output checks, prompt read in full; BOUT
`kind: outro_voice` with 1.0 s tail ending "At Nik Bear Brown.".

## Known gaps (not failures — deferred to the Mac render pass)

1. `manim_layout_audit.py --curve-strict` not run — no Manim/pangocairo in
   this VM. Mitigation: hand-placed labels (≥0.3 leader gaps, no curve/label
   crossings, coords inside ±6.2 × ±3.3, type ≥ 32). **Run before the 4K render.**
2. Midpoint render-guard not verifiable without measured Kokoro audio.
   Mitigation: event phrases timed off the 45–55% window (see SHOTLIST.md;
   B03's later chips flagged for re-check). **Re-verify after audio measurement.**
3. Whisper transcript check of BIDEA ("Hallo") and the British spellings
   ("favourite colour", "apologise") — **at render time**.
