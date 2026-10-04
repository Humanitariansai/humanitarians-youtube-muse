# CHECKS-REPORT.md — "Think one step ahead"

QC gate run 2026-10-03, in the build folder
`~/workspace/film-builds/how-to-ai/think-one-step-ahead/`.

## Gate 1 — py_compile

`python3 -m py_compile make_sheet.py scenes.py` — **clean**, no output.

## Gate 2 — static scene check (render-free, Manim stub)

`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <ClassName>`,
run from a scratch folder holding ONLY `scenes.py` + `beat_sheet.json`
(the exact Gate A sandbox view), per the show-tell skill's pre-audit rule.

| Scene class | Beat | Result |
|---|---|---|
| `B00_Window` | B00 | clean · 0 warnings · 0 errors |
| `B01_Before` | B01 | clean · 0 warnings · 0 errors |
| `B02_Scratchpad` | B02 | clean · 0 warnings · 0 errors |
| `B03_After` | B03 | clean · 0 warnings · 0 errors |
| `B04_When` | B04 | clean · 0 warnings · 0 errors |
| `B05_Ahead` | B05 | clean · 0 warnings · 0 errors |

**Total: 6 clean · 0 warnings · 0 errors — first run, no fixes needed.**
(Every construct() executes against the stub; every beat adds new non-text
shapes after its first frame; all explicit coordinates sit inside the safe
area ±6.3 × ±3.4.)

## Gate 3 — make_sheet.py self-assertions

`python3 make_sheet.py` regenerates `beat_sheet.json` and asserts: 10 beats
in order (BIDEA, BDEFS, B00–B05, BHTF, BOUT); 6 manim body beats with matching
scene classes; total 189.6 s inside the 170–260 s band; every manim beat
carries `sparse_by_design` + `audio_file`; BIDEA trigger words verbatim in
text with no trailing punctuation; all BDEFS terms ≤ 17 chars. **All pass.**

## Deferred (cannot run in this VM)

- `manim_layout_audit.py --curve-strict` needs Manim + pangocairo, which this
  VM does not have. Deferred to the render pass on Bear's Mac; recorded in
  CLAUDE-CODE-RENDER.md step 4. [record]
- Kokoro narration + whisper checks happen at render time on Bear's Mac.
