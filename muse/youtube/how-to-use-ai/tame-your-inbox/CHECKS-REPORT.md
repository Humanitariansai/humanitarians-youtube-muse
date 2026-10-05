# CHECKS-REPORT.md — Tame your inbox

QC gate run 2026-10-05, package `muse/youtube/how-to-use-ai/tame-your-inbox/`.

## Gate 1 — py_compile

| file | result |
|---|---|
| `make_sheet.py` | clean |
| `scenes.py` | clean |

## Gate 2 — static_scene_check (Gate A simulation)

Run from `/tmp/gatea-tyi/` holding **only** `scenes.py` — exactly what `art run`'s
Gate A sees. Command per class:
`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`

| class | warnings | errors |
|---|---|---|
| B00_ThePile | 0 | 0 |
| B01_Triage | 0 | 0 |
| B02_TheSummary | 0 | 0 |
| B03_TheDraft | 0 | 0 |
| B04_NeverAutoSend | 0 | 0 |
| B05_NeverAutoDelete | 0 | 0 |

Also ran all 6 with `beat_sheet.json` beside `scenes.py` to confirm the
`until()`/`finish()` pacing path executes: 0 warnings, 0 errors.

Additionally verified by script: every `until()` phrase (14) appears verbatim
in its beat's `narration_text` (all present), and every manim class named in
the sheet exists in `scenes.py`.

## Gate 3 — make_sheet.py asserts

All asserts passed at generation time: 10 beats in the show-tell spine order;
total 190.0 s inside the 180–300 s band; **every beat carries voice
`am_onyx`** (the Wave 5 lesson — asserted in the generator); every manim beat
carries a `shot.manim.class` named for its beat id; BIDEA `triggerWords`
("get Claude to answer my emails") verbatim in `text`, trigger/replacement
free of trailing punctuation; all BDEFS terms ≤ 17 chars; BHTF topic contains
"YOUR TURN", greeting exactly "Your turn.", two output checks, prompt read in
full; BOUT `kind: outro_voice` with 1.0 s tail ending "At Nik Bear Brown.".

## Known gaps (not failures — deferred to the Mac render pass)

1. `manim_layout_audit.py --curve-strict` not run — no Manim/pangocairo in
   this VM. Mitigation: hand-placed labels (≥ 0.3 leader gaps, no curve/label
   crossings), all coords inside ±6.2 × ±3.3, type ≥ 32; the bin is grey
   (BAR2), not near-black, so it can't read as giant text under GATE T.
   **Run before the 4K render.**
2. Midpoint render-guard not verifiable without measured Kokoro audio.
   Mitigation: event phrases timed off the 45–55% window (see SHOTLIST.md).
   **Re-verify after audio measurement.**
3. Whisper transcript check of BIDEA ("Ciao") and the hyphenated
   "first-pass" — **at render time**.
