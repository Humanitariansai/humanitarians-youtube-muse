# BUILD-LOG.md — Muse proves it scales

2026-10-03, film 3 of 4 for Assignment 4.

1. Ran honest scale tests first (assignment requirement): scale_test.py
   replicated real Anthropic records with unique ids at 1x/10x/50x; measured
   wall time and peak RSS; timed a live Greenhouse fetch separately.
   Results written to assignment-4/SCALE-TESTS.md and pushed.
2. Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md.
3. Wrote make_sheet.py; generated beat_sheet.json: 14 beats, 294 s (~4m54s).
4. Wrote scenes.py (12 Manim scenes, M01–M12).
5. First QC pass: 2 errors (M09, M11) for repeated animation — all reveals
   text-only. Fixed with progressive non-text shapes (coin dots, verdict
   cards + arrow). Second pass: **12 clean, 0 warnings, 0 errors**.
6. Wrote SOURCES.md, BUILD-LOG.md, CHECKS-REPORT.md, PROMPTS.md,
   CLAUDE-CODE-RENDER.md.

No narration audio or video rendered here.
