# CHECKS-REPORT.md — Make it remember (and forget)

Date: 2026-10-04. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Gate 1 — py_compile
- `python3 -m py_compile make_sheet.py` → clean.
- `python3 -m py_compile scenes.py` → clean (after fixing a syntax error in
  B04's MoveAlongPath play and a `.set(height=…)` hack on the B06 pill —
  both caught by py_compile, recorded in BUILD-LOG.md).

## Gate 2 — make_sheet.py self-assertions (run 2026-10-04)
All passed: 13 beats in exact order (BIDEA, BDEFS, B00–B08, BHTF, BOUT);
9 manim + 4 bookend lanes; total estimated duration 216 s (~3m36s, inside
the 200–320 s band); every manim class name starts with its beat id;
BIDEA triggerWords verbatim in text and punctuation-free; all BDEFS terms
≤ 17 chars; BHTF prompt read in full in the narration; BOUT is outro_voice
with 1.0 s tail; every beat voice am_onyx / engine kokoro with a non-empty
show block; "Liam, in for Bear" named in BIDEA.

## Gate 3 — static_scene_check.py (one run per class, 2026-10-04)
Run from the film folder with beat_sheet.json beside scenes.py (real
until()/finish() pacing — exactly what Gate A sees, minus the render).
Bookend beats (BIDEA/BDEFS/BHTF/BOUT) are Remotion, not Manim —
no scene classes, nothing to check.

| Class | Result |
|---|---|
| B00_TheNotebook | clean · 0 warn · 0 error |
| B01_KeepWorthy | clean · 0 warn · 0 error |
| B02_NeverIn | clean · 0 warn · 0 error |
| B03_WhereItLives | clean · 0 warn · 0 error |
| B04_FixOne | clean · 0 warn · 0 error |
| B05_TwoLevers | clean · 0 warn · 0 error |
| B06_Incognito | clean · 0 warn · 0 error |
| B07_ChatDelete | clean · 0 warn · 0 error |
| B08_NotArchive | clean · 0 warn · 0 error |

**9 clean · 0 warn · 0 error** — first checker run, no warnings or errors
found or fixed at this gate.

No checker warnings or errors were hidden or waived. The
`manim_layout_audit.py --curve-strict` pass cannot run in this VM (no
Manim/pangocairo installed) and is deferred to Bear's Mac render pass —
recorded in CLAUDE-CODE-RENDER.md.

## Gate 4 — manual pre-gate review (author's pass before the checker ran)
- Every explicit coordinate in helpers and scenes verified inside ±6.2 × ±3.3
  (checker SAFE bounds ±6.3 × ±3.4; hard frame ±7.12 × ±4.05).
- Text floor: all `T()` calls size ≥ 32 (labels 32–34; bubble/pill/card content 32).
- Labels sit beside objects, never inside outlines, never on terracotta fill.
- Terracotta budget per beat: one seal dot, X marks, one check accent only —
  cables edged in deep kraft #9C8462 (never ink); closed-notebook strap is
  DIM grey with a single terracotta seal (per the skill's tape rule).
- No `rate_functions.ease_in_quad` / `ease_out_cubic`; no `animate(path_arc=…)`
  (MoveAlongPath + Line used, alongside fades of other objects only —
  MoveAlongPath and .animate are never on the same object in one play);
  `get_center()` not used on groups; no group slices; no bare BOLD/NORMAL
  weight constants (kit's `T()` only).
- Every `until()` phrase verified verbatim in its beat's narration_text.
- Class names literally `class BNN_Name(Scene):` (run.sh discovery).
- Every scene adds new non-text shapes in its own play calls (FadeIn/Create/
  MoveAlongPath of new objects); no scene relies on moves alone; no beat
  creates a shape only to remove it in the same span (per the Gate A trap).
- Continuity: the open notebook is the recurring cast member B00→B05 and
  B07→B08; chat windows recur B00/B06/B07/B08; the settings panel is B03's.
