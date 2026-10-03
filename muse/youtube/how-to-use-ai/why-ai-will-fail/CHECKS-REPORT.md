# CHECKS-REPORT.md — "AI will fail." (why-ai-will-fail)

Written before the push (pre-render gate). 14 SHOW / 0 HOLD / 0 PUNT.

## Beat classification (SHOW / HOLD / CARD)

Every beat classifies SHOW: each beat's narration makes factual or
structural claims AND names its on-screen artifact in `shot.show` /
`shot.visual_intent`, with ≥2 shape-state changes per beat. No justified
HOLDs, no PUNT-flagged beats. Legibility contract: one idea per beat,
comparisons side-by-side and held (B04, B08, B09, B10), negative space
via the cream stage, single terracotta accent per beat.

| Beat | Class | On-screen artifact |
|---|---|---|
| B00 | SHOW | Quote card + WRONG stamp (SceneColdOpen) |
| B01 | SHOW | Century timeline + pattern equation (SceneOverview) |
| B02 | SHOW | 4 evidence cards: year/expert/quote/outcome (SceneTheList) |
| B03 | SHOW | Keyes quote card + 300M+ counter + Bend dot (SceneBlockbuster) |
| B04 | SHOW | 2 quote cards + outcome banners (SceneEllisonValenti) |
| B05 | SHOW | BMJ journal page → lives-saved dot field (ScenePenicillin) |
| B06 | SHOW | Old-axis bars vs new-axis curve diagram (SceneInsiderTrap) |
| B07 | SHOW | Logistic toy curve + skeptic pins + trajectory arrow (SceneToyCurve) |
| B08 | SHOW | THEN/NOW card pairs with wiring arrows (SceneFamiliarForm) |
| B09 | SHOW | Snapshot frame vs trajectory film strip (SceneHonestPart) |
| B10 | SHOW | 2×2 payoff matrix + checks + banner (SceneAsymmetricBet) |
| B11 | SHOW | Four-line verdict card, checked off (SceneVerdict) |
| B12 | SHOW | Handoff prompt card, typed with cursor (SceneYourTurn) |
| B13 | SHOW | Title restate + handle (SceneOutro) |

## Teaching-arc checklist

- FRAMEWORK ✓ — B01 states the whole pattern (BLUF) before any evidence.
- WORKED EXAMPLE ✓ — B07 (toy curve) and B03 (Blockbuster/Netflix) are
  worked instances of the mechanism, not just claims.
- FALSIFIABILITY ✓ — B09 states the honest counter-case (skeptics describe
  the present accurately) and B12's handoff asks what would prove each
  skeptic argument right or wrong.
- SCAFFOLDED TASK ✓ — B12: a concrete prompt to run the pattern on today's
  skepticism, read aloud and discussed.
- BOOKENDS ✓ — cold open (B00), overview (B01), verdict (B11),
  handoff (B12), title outro (B13).
- NO-SOURCE-NO-VERDICT ✓ — every verdict line in B11 traces to sourced
  beats (B02–B05 evidence, B06–B07 mechanism, B10 bet).

## QC gate results

- `python3 -m py_compile make_sheet.py scenes.py` — clean.
- `make_sheet.py` assertions — pass: 14 beats; every beat has narration +
  an existing scene class; per-beat 3.8–29.0 s; total 335.2 s (240–420 s band).
- `static_scene_check.py scenes.py --class <each>` — 14/14 clean,
  0 warnings, 0 errors (run 2026-10-03).

### Failure recorded and fixed

- First run: SceneYourTurn → 1 ERROR ("shapes never change — 1 distinct
  shape-state across 4 frames"). Root cause: the prompt card was the beat's
  only non-text shape, so all snapshots were identical — the exact
  repeated-animation defect the checker guards against. Fix: prompt types
  line-by-line with a moving terracotta cursor (each play changes shape
  state); cursor fades as the footer appears. Re-run: 6 distinct states,
  0 warnings, 0 errors. Logged in BUILD-LOG.md.

## Pre-push file inventory (12 files)

ACTS.md, SHOTLIST.md, FACTCHECK.md, make_sheet.py, beat_sheet.json,
scenes.py, SOURCES.md, BUILD-LOG.md, CHECKS-REPORT.md, PROMPTS.md,
CLAUDE-CODE-RENDER.md, README.md.
No MP3/MP4/WAV, no .pyc/__pycache__, no .DS_Store, no secrets.
