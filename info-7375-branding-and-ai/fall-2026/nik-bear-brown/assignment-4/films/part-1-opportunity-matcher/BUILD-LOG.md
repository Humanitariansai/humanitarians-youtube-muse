# BUILD-LOG.md — "Muse builds the opportunity matcher"

Reel: `.../assignment-4/films/part-1-opportunity-matcher/`
Built on Muse's Linux VM, 2026-10-03. No audio/video generated here.

## What was built

| File | Status |
|---|---|
| ACTS.md | 6 acts, 17 body beats |
| SHOTLIST.md | 17 beats routed, all Manim |
| FACTCHECK.md | Gate F: every number traced to assignment-4 files |
| make_sheet.py / beat_sheet.json | 22 beats, ~321 s (~5.4 min) |
| scenes.py | 17 Manim classes M01–M17 |
| CLAUDE-CODE-RENDER.md | render prompt for Bear's Mac |
| SOURCES.md / PROMPTS.md / CHECKS-REPORT.md | paperwork |

## Fixes during the build

- M05: "shapes never change" — added terracotta underlines drawing beneath
  each evidence line.
- M11: text-only warning — added badge circles; the confirmed pairing now
  draws a terracotta ring.
- M17: avoided the stub `get_x()` bug (index-based positions).

## Handoff

Bear pulls the repo and pastes `CLAUDE-CODE-RENDER.md` into Claude Code:
Kokoro narration → `./art run` review cut → `./art final` 4K master.
Never publish.
