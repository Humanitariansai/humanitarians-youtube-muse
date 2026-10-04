# BUILD-LOG.md — "Ask for the Shape You Want Back" (How to AI #4)

## 2026-10-03

- Read the assigned skill `show-tell` (SKILL.md, 2026-09-26 lineage). Kept it: the
  film is a one-idea-per-beat illustrated explainer — exactly the show-tell shape.
  No cards used; every body beat is a drawing, and none passed the card test.
- Fetched the refactor source from the mirror repo via the Contents API. Found the
  anomaly: `beat_sheet.json` in the lesson-05 folder carries grounding/hallucination
  narrations under a formatting-output title (mismatched, likely pasted from another
  lesson). Rebuilt from the intended argument in `description.txt` + Anthropic's
  Lesson 05 docs ("Prefill Claude's response"). [record]
- Verified the prefill claim against Anthropic's docs via web search (multiple
  mirrors of the official docs page agree). Marked everything in FACTCHECK.md;
  no invented statistics, no open [VERIFY] items.
- Wrote `make_sheet.py`: 13 beats (BIDEA, BDEFS, B00–B08, BHTF, BOUT), estimated
  246 s (~4.1 min). Assertions: 13 beats, 9 manim, 4 bookends, total within
  200–360 s, beat order, all voices am_onyx, non-empty narration. Passed first run.
- Wrote `scenes.py`: iso_kit.py pasted verbatim at top (no import — Gate A copies
  only scenes.py), then 9 scene classes `B00_BlocksBox` … `B08_ThenStop`, one per
  visual beat. `until()` phrases copied verbatim from the narration texts.
- Pre-QC review caught two latent bugs before running the checker: (1) B03 first
  draft sliced `page[1][4:]` from the kit page's 3-line group — an empty slice, so
  the "lower half falls away" moment would have removed only the dot; rewrote B03
  with an explicit 9-line page split into `upper`/`lower` groups. (2) B02/B07 header
  bands were full card width; inset them so they sit inside the rounded card
  corners (skill note: dark header bands read as overlapping labels under GATE T).
- QC: `python3 -m py_compile` clean on make_sheet.py and scenes.py;
  `static_scene_check.py --class <C>` for all 9 classes: 9 clean · 0 warn · 0 error.
  (beat_sheet.json was beside scenes.py, so until()/finish() pacing ran for real.)
- `manim_layout_audit.py --curve-strict` could NOT run in this VM (no Manim /
  pangocairo) — deferred to Bear's Mac render pass; noted in CLAUDE-CODE-RENDER.md
  and CHECKS-REPORT.md.
- Pushed all 12 files to `Humanitariansai/humanitarians-youtube-muse` under
  `muse/youtube/how-to-use-ai/ask-for-the-shape-you-want-back/` via gh-put-file.py;
  every file verified live with a Contents API read afterwards. Did not touch
  muse/FRICTIONAL.md, muse/README.md, or muse/QUEUE.md.

Open for the render pass (Bear's Mac): generate Kokoro am_onyx audio, write back
`actual_duration_s`, layout audit --curve-strict per scene, 4K render, ffprobe clips
against audio (clip-longer-than-audio gets centre-cut — keep plays within the
measured durations).
