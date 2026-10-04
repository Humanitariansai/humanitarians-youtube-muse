# BUILD-LOG.md — "Just talk to it" (film 18/24)

## Skill choice

Assigned skill: `show-tell`. Kept — the film is a plain explainer (one idea
per beat, voice carries the explanation, minimal labels), which is exactly the
show-tell brief. No beat passed the card test (every idea is a thing, a part,
or a flow), so the film uses zero ShowTellCards; all twelve body beats are
drawings. Recorded as required.

## 2026-10-03 — build session

1. Read `show-tell/SKILL.md` end to end, plus `reference/example-make_sheet.py`
   and `templates/iso_kit.py` (pasted verbatim into `scenes.py` — Gate A
   copies only that file).
2. Fact-checked voice-mode availability against Anthropic support docs and
   three press pieces (Engadget, Tom's Guide, iTechPost), all retrieved
   2026-10-03. Findings: voice mode on Claude mobile/desktop/web; entered via
   a waveform icon next to the microphone icon; hands-free (default) and
   push-to-talk modes; free voice↔text switching with shared context. The
   narration deliberately says "a microphone or waveform icon in the app you
   use" so no version-specific UI is asserted (anti-rot; see ACTS.md).
3. Authored `make_sheet.py` (16 beats: BIDEA, BDEFS, 12 manim body, BHTF,
   BOUT; ~205 s estimated). First run failed its own assertion: I wrote
   `len(B) == 17` but 12 body + 4 bookends = 16. Fixed the assertion to 16 —
   the beat list itself was correct; the count in my head was wrong. [record]
4. Authored `scenes.py`: iso_kit pasted verbatim + local helpers (wave arcs,
   mic button, heads, labels) + 12 scene classes. Midpoint discipline: all
   motion completes in the first ~40% of each beat, fully opaque; `until()`
   holds on a settled labelled frame (every `until()` phrase verified
   verbatim-present in its beat's narration by script).
5. QC gate: `py_compile` clean on both files; `static_scene_check.py` run for
   all 12 classes — 12 clean · 0 warnings · 0 errors, first pass. No failures
   to fix; nothing concealed (see CHECKS-REPORT.md).
6. `manim_layout_audit.py --curve-strict` cannot run in this VM (no
   Manim/pangocairo) — deferred to Bear's Mac render pass per the assignment.
   Coordinates were kept inside ±6.2 × ±3.3 and type ≥ 36 px by construction.
7. Wrote docs: ACTS, SHOTLIST, FACTCHECK, SOURCES, PROMPTS ("no generation
   prompts"), BUILD-LOG, CHECKS-REPORT, CLAUDE-CODE-RENDER, README.
8. Pushed all 12 files to
   `muse/youtube/how-to-use-ai/just-talk-to-it/` on
   Humanitariansai/humanitarians-youtube-muse via `gh-put-file.py`; verified
   every file live with a Contents API read afterwards.

Did NOT touch: FRICTIONAL.md, muse/README.md, muse/QUEUE.md (per assignment).
No MP3/MP4/WAV/.pyc/__pycache__/.DS_Store committed. No secrets or PII in any
file.
