# BUILD-LOG.md — Tame Your Spreadsheets

## 2026-10-03 — pre-render package built

**Skill choice.** Kept the assigned `show-tell`. The film is exactly what the
skill is for: one drawing per beat (the sheet, the formula, the scan, the
bars), minimal labels, Liam's voice carrying the explanation. No switch
needed; no ShowTellCard beats passed the card test (0 of 7 body beats are
cards — documented in SHOTLIST.md).

**Refactor decisions.**
- Source film ("Stop learning Excel.") was a Claude Cowork power-user film
  (Pro account, Cowork tab, Opus 4.7, board-ready Excel). Rewrote for the
  general-audience brief: the AI is a patient spreadsheet *coach*, not a
  file-builder; the three moves are plain-English formula requests,
  paste-and-clean, and "what's interesting in this data?".
- Kept the source's core argument — human stays in control while the AI does
  the mechanics — recast as the B03 sanity-check warning and the B05/BHTF
  "the AI proposes, you decide" line.
- All example data fictional (Lena's Bake Shop); no real personal financial
  data anywhere.
- Narration reads "B 2" / "B 31" as separate tokens and says "equals, sum,
  open bracket" so Kokoro voices the formula cleanly; no acronym spelling
  traps (per skill: plain "API"-style words only where verified).
- Bookends follow the house pattern: BIDEA hesitant writer (trigger "learn
  Excel" → "tame this spreadsheet", verbatim, no trailing punctuation),
  BDEFS three short terms, BHTF Claude.ai composer with two viewer checks,
  BOUT spoken "Tame Your Spreadsheets. At Nik Bear Brown." + 1.0 s tail.
  `bookend_exempt: ["cold-open", "bvdt"]` declared with reason, as in the
  worked example.

**QC.** `python3 -m py_compile` clean on `make_sheet.py` and `scenes.py`.
`static_scene_check.py` run for all 7 scene classes: 7 clean · 0 warn ·
0 error, first run — no failures to fix. (Full detail in CHECKS-REPORT.md.)
`manim_layout_audit.py --curve-strict` could not run in this VM (no
Manim/pangocairo) — deferred to Bear's Mac render pass; noted in
CLAUDE-CODE-RENDER.md.

**Push.** All 12 files pushed to
`Humanitariansai/humanitarians-youtube-muse`
`muse/youtube/how-to-use-ai/tame-your-spreadsheets/` via
`gh-put-file.py`, each verified with a Contents API read afterwards.
