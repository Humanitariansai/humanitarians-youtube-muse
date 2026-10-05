# BUILD-LOG.md — "Shop smarter" (film 43)

## Skill choice

Assigned skill: `show-tell`. Kept — the film is a plain explainer (one idea
per beat, the voice carries the explanation, minimal labels), which is exactly
the show-tell brief. No beat passed the card test: the table (B02/B03) is a
drawn ink grid, not data on a card; the B08 numbers are ink step markers, not
a metric. So the film uses zero ShowTellCards; all nine body beats are
drawings. Recorded as required.

## 2026-10-05 — build session

1. Read `show-tell/SKILL.md` end to end, plus the finished film
   `just-talk-to-it/` (its `make_sheet.py` format, `scenes.py` helper
   patterns, and doc conventions were the working template).
2. Fact-checked the one external claim (fake/bought reviews are real) against
   the FTC's Trade Regulation Rule on Consumer Reviews and Testimonials
   (announced 14 Aug 2024, effective 21 Oct 2024) via two public write-ups,
   retrieved 2026-10-05. Everything else is method advice or structural AI
   limitations; no product endorsements, no pricing tiers, per the brief.
3. Authored `make_sheet.py` (13 beats: BIDEA, BDEFS, 9 manim body, BHTF,
   BOUT; 205 s estimated). First run passed all its own assertions —
   including the voice check (`am_onyx` on every beat; the exact bug that
   broke two Wave 5 films) and the new terms-length guard (≤17 chars).
4. Authored `scenes.py`: iso_kit pasted verbatim from
   `skills/make/show-tell/templates/iso_kit.py` (diffed against the template
   film's copy — identical) + local helpers (labels, heads, X marks, pages,
   ghost lines, table grid) + 9 scene classes. Midpoint discipline: all motion
   completes in the first ~40% of each beat, fully opaque; `until()` holds on
   a settled labelled frame (every `until()` phrase verified verbatim-present
   in its beat's narration).
5. QC gate: `py_compile` clean on both files. `static_scene_check.py` for all
   9 classes: 8 passed first try; B02_TheTable failed with "shapes never
   change" because a single `Create(grid)` didn't register as a membership
   change in the stub. Fixed by splitting the grid into two plays (verticals
   then horizontals) — the motion is unchanged visually, still fully drawn
   well before the midpoint. Re-ran: 9 clean · 0 warnings · 0 errors.
   (see CHECKS-REPORT.md).
6. `manim_layout_audit.py --curve-strict` cannot run in this VM (no
   Manim/pangocairo) — deferred to Bear's Mac render pass per the assignment.
   Coordinates were kept inside ±6.2 × ±3.3 and type ≥ 40 px by construction;
   terracotta only for dots/checks/rings/X-marks; ink numerals; leaders ≥0.3
   gap from their labels.
7. Wrote docs: ACTS, SHOTLIST, FACTCHECK, SOURCES, PROMPTS ("no generation
   prompts"), BUILD-LOG, CHECKS-REPORT, CLAUDE-CODE-RENDER, README.
8. Pushed all 12 files to
   `muse/youtube/how-to-use-ai/shop-smarter/` on
   Humanitariansai/humanitarians-youtube-muse via `gh-put-file.py`; verified
   every file live with a Contents API read afterwards.

Did NOT touch: FRICTIONAL.md, muse/README.md, muse/QUEUE.md (per assignment).
No MP3/MP4/WAV/.pyc/__pycache__/.DS_Store committed. No secrets or PII in any
file.
