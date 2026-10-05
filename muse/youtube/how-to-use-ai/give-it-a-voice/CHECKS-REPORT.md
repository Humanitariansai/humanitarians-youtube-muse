# CHECKS-REPORT.md — "Give it a voice"

QC gate run 2026-10-05, in the build VM (no Manim/pangocairo — the
`manim_layout_audit.py --curve-strict` pass is deferred to Bear's Mac
render pass per CLAUDE-CODE-RENDER.md).

## 1. py_compile

- `python3 -m py_compile make_sheet.py scenes.py` — clean, no output.

## 2. static_scene_check (per class)

`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py
scenes.py --class <ClassName>` — run for every scene class, twice:
once in the build dir (beat_sheet.json present, `until()`/`finish()`
pacing active) and once in a scratch dir holding ONLY scenes.py (the
exact Gate A sandbox; kit falls back to no-op pacing).

| Class | In build dir | Scratch only |
|---|---|---|
| B00_SilentSlides | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B01_SunoSpeech | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B02_TwoWays | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B03_Workflow | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B04_BetaRough | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B05_VidsBuiltIn | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B06_TheRule | clean · 0 warn · 0 error | clean · 0 warn · 0 error |

All 7 classes passed first try — 0 warnings, 0 errors, no fixes
needed. Distinctness check reports each scene's shape-states as
distinct from the others (no repeated-animation defect); all explicit
coordinates stay inside the 16:9 frame.

## 3. make_sheet.py self-assertions

- 11 beats, unique ids, BIDEA/BDEFS + B00–B06 + BHTF/BOUT ordering ✓
- every beat: non-empty narration, positive duration, voice
  `am_onyx`, engine `kokoro`, non-empty show block, a duration field ✓
- body beats: shot.type GRAPHIC, lane manim, class names match
  `scenes.py` (`B00_SilentSlides` … `B06_TheRule`) ✓
- bookends: shot.type REMOTION with remotion.pattern set ✓
- BIDEA: lead_silence_s 0.8; triggerWords verbatim in text; neither
  trigger nor replacement ends in punctuation (one failure caught and
  fixed during the build — the line break split the trigger phrase) ✓
- BDEFS: durationSeconds == estimated_duration_s; all terms ≤ 17
  chars ✓
- BHTF: topic contains "YOUR TURN"; the Claude prompt is read verbatim
  in the narration ✓
- BOUT: kind outro_voice, 1.0 s tail ✓
- total 181.6 s, inside the 150–240 s band ✓

## 4. Deferred

- `manim_layout_audit.py --curve-strict` — cannot run in this VM (no
  Manim/pangocairo); deferred to Bear's Mac render pass.
- Whisper-check of Kokoro narration (esp. "Hallo", "[excitedly]"
  spoken as "open bracket, excitedly, close bracket", "Suno") — at
  the audio stage on the Mac.
