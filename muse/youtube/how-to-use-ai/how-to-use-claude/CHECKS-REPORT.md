# CHECKS-REPORT.md — How to Use Claude

QC gate run 2026-10-03, package `muse/youtube/how-to-use-ai/how-to-use-claude/`.

## Gate 1 — py_compile

| file | result |
|---|---|
| `make_sheet.py` | clean |
| `scenes.py` | clean |

## Gate 2 — static_scene_check (Gate A simulation)

Run from `/tmp/gatea/` holding **only** `scenes.py` — exactly what `art run`'s
Gate A sees. Command per class:
`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`

| class | warnings | errors | steady states | distinct shape states |
|---|---|---|---|---|
| B00_ChatWindow | 0 | 0 | — | — |
| B01_ModelBehind | 0 | 0 | — | — |
| B02_Stranger | 0 | 0 | — | — |
| B03_ContextIn | 0 | 0 | — | — |
| B04_Project | 0 | 0 | 12 | 6 |
| B05_Artifact | 0 | 0 | — | — |
| B06_Analysis | 0 | 0 | — | — |
| B07_Rewrite | 0 | 0 | — | — |
| B08_CheckIt | 0 | 0 | — | — |

Also ran B04 with `beat_sheet.json` beside `scenes.py` to confirm the
`until()`/`finish()` pacing path executes: 0 warnings, 0 errors.

Additionally verified by script: every `until()` phrase appears verbatim in
its beat's `narration_text` (all present).

## Gate 3 — make_sheet.py asserts

All asserts passed at generation time: 13 beats in the show-tell spine order;
total 196.4 s inside the 180–220 s band; every manim beat carries a
`shot.manim.class` named for its beat id; BIDEA `triggerWords` ("one prompt")
verbatim in `text`, trigger/replacement free of trailing punctuation; all
BDEFS terms ≤ 17 chars; BHTF topic contains "YOUR TURN", greeting exactly
"Your turn.", two output checks, prompt read in full; BOUT `kind:
outro_voice` with 1.0 s tail ending "At Nik Bear Brown.".

## Known gaps (not failures — deferred to the Mac render pass)

1. `manim_layout_audit.py --curve-strict` not run — no Manim/pangocairo in
   this VM. Mitigation: hand-placed labels (≥0.3 leader gaps, no curve/label
   crossings, coords inside ±6.2 × ±3.3, type ≥ 32). **Run before the 4K render.**
2. Midpoint render-guard not verifiable without measured Kokoro audio.
   Mitigation: event phrases timed off the 45–55% window (see SHOTLIST.md).
   **Re-verify after audio measurement.**
3. Whisper transcript check of BIDEA ("Hallo") and acronyms — **at render time**.
