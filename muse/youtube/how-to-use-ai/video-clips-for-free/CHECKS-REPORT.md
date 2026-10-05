# CHECKS-REPORT.md — "Video clips for free"

QC gate run 2026-10-05, before pushing. Requirement: 0 warnings and
0 errors on every scene class.

## 1. py_compile

```
python3 -m py_compile make_sheet.py scenes.py   -> clean (no output)
```

## 2. make_sheet.py self-assertions (run at generation)

- 13 beats, unique ids, BIDEA first / BOUT last
- every beat: non-empty narration, duration > 0, voice `am_onyx` (Kokoro code, never a persona name), engine kokoro, non-empty `shot.show`
- body beats exactly B00–B08, each with `shot.manim.class` matching the scenes.py class name
- BIDEA: lead_silence_s 0.8; triggerWords "a whole video" verbatim in text, no trailing punctuation
- BDEFS: durationSeconds (15.6) matches narration estimate; all terms ≤ 17 chars
- BHTF topic contains "YOUR TURN"; the prompt is read verbatim in narration
- BOUT: kind outro_voice, tail_silence_s 1.0
- metadata: bookend_exempt ["cold-open","bvdt"], channel claude-liam, voice am_onyx, register Teardown
- total estimated duration 190.0 s, inside the 150–260 s band
- result: all assertions passed on first run

## 3. Static scene QC (manim-stub, render-free)

`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`

**First run:** 8 clean, 1 errored — B01_OneClip raised
"shapes never change — 1 distinct shape-state across 5 frames". Root cause:
the shadow (`self.add`) and the clip (first `play`) were both present from
the first stub snapshot, and the only later addition was the text label
(excluded from shape counting). Fix: split the clip — the frame and
sprocket holes grow first, the play triangle fades in with the label, a
genuine membership change after the first play (and a nicer visual beat).
No design change otherwise.

**Second run:**

| Class | Result |
|---|---|
| B00_VidsWindow | clean · 0 warn · 0 error |
| B01_OneClip | clean · 0 warn · 0 error |
| B02_TheBudget | clean · 0 warn · 0 error |
| B03_AIWins | clean · 0 warn · 0 error |
| B04_Stock | clean · 0 warn · 0 error |
| B05_ScriptFirst | clean · 0 warn · 0 error |
| B06_Extend | clean · 0 warn · 0 error |
| B07_PaidExtras | clean · 0 warn · 0 error |
| B08_CheckTheNumber | clean · 0 warn · 0 error |

**9 clean · 0 warn · 0 error.**

**Verbatim-until check (scripted):** all 13 `until()` phrases appear
verbatim (case-sensitive) in their beats' `narration_text`; all 9
`shot.manim.class` names match the `scenes.py` class names. All OK.

**Midpoint guard (by construction):** every scene's last `play` completes
before 45% of its beat's estimated duration (checked per beat against
`estimated_duration_s`), so no animation is mid-flight where GATE T
samples. New shapes always enter via Create / FadeIn / GrowFromCenter,
never via `.animate()` alone.

## 4. Deferred to Bear's Mac render pass

`manim_layout_audit.py --curve-strict` could not run in the build VM (no
Manim/pangocairo installed) — deferred per the assignment; see
CLAUDE-CODE-RENDER.md §2. Whisper-checks for Kokoro are also deferred to
the audio pass.
