# CHECKS-REPORT.md — Posters and Flyers

QC gate run 2026-10-05, package `muse/youtube/how-to-use-ai/posters-and-flyers/`.

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
| B00_Hero | 0 | 0 | — | 4 |
| B01_Companion | 0 | 0 | — | 12 |
| B02_Facts | 0 | 0 | — | 8 |
| B03_ExactWords | 0 | 0 | — | 4 |
| B04_Layout | 0 | 0 | — | 4 |
| B05_Split | 0 | 0 | — | 3 |
| B06_PrintCheck | 0 | 0 | — | 4 |
| B07_Label | 0 | 0 | — | 4 |
| BVDT_Recap | 0 | 0 | — | 5 |

**Total: 9 classes, 0 warnings, 0 errors — all clean on the first run.**

## Pre-check hand-review fixes (recorded, not concealed)

1. **Short leader lines removed/repositioned.** B01 ("the recipe"), B04 zone
   3 ("room for facts"), and B06 (check labels) initially had leader lines
   under ~0.6 units long; per the skill notes a short leader reads as
   sub-floor text under GATE T. The leaders were dropped and the labels
   placed with clear gaps (≥ 0.3 units) instead.
2. **B02 chip sizing.** The three fact chips were first fixed-width and the
   longest text ("Saturday, 9 a.m.") would have overflowed; chips now
   auto-size to text length (`len(text) * 0.21 + 0.9`) and are right-aligned
   so every chip stays inside the ±6.2 safe area.

## make_sheet.py assertions

All assertions passed: 13 beats in the house order
(BIDEA, BDEFS, B00–B07, BVDT, BHTF, BOUT); 9 GRAPHIC + 4 REMOTION; every
beat `voice == "am_onyx"` and `engine == "kokoro"`; hesitant-writer trigger
contract holds ("design" appears verbatim in the text, no trailing
punctuation); BDEFS terms all ≤ 17 chars; IN-FOR-BEAR law holds; BHTF
greeting/output contract holds; BOUT `outro_voice` + 1.0 s tail; total
254.2 s inside the 200–360 s band.

## Deferred to Bear's Mac render pass

`manim_layout_audit.py --curve-strict` cannot run in this VM (no
Manim/pangocairo) — deferred per the standing rule; see
CLAUDE-CODE-RENDER.md.
