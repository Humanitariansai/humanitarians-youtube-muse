# BUILD-LOG.md — "Claude making a film about Muse"

Reel: `muse/youtube/claude-liam-lecture-claude-making-a-film-about-muse/`
Built on Muse's Linux VM, 2026-10-03. No audio/video generated here.

## What was built

| File | Status |
|---|---|
| ACTS.md | coverage map: 6 acts, 23 body beats, whole-document pass |
| SHOTLIST.md | 23 body beats routed (all Manim), bookends library |
| FACTCHECK.md | Gate F: attribution map (Meta / third-party / Nik's take / doc figures) |
| make_sheet.py | beat sheet generator |
| beat_sheet.json | 28 beats, ~444 s estimated (~7.4 min) |
| scenes.py | 23 Manim classes M01–M23 |
| CLAUDE-CODE-RENDER.md | render prompt for Bear's Mac |
| SOURCES.md / PROMPTS.md / CHECKS-REPORT.md | paperwork |

## Decisions

- **Framing:** the film presents Bear and Claude's opinion, narrated by
  Liam. Contested claims stay attributed in voice and on screen.
- **Narration trim:** first draft estimated ~502 s; tightened 17 beats to
  land at ~444 s without dropping any section of the source.
- **M18 split:** business conflicts + platform dependence in one beat, the
  phone's permissions in its own — the triptych was too dense.
- **No paid generation:** all visuals are Manim or library Remotion
  components. No Higgsfield or other paid beats.

## Handoff

Bear pulls the repo and pastes `CLAUDE-CODE-RENDER.md` into Claude Code
on his Mac: Kokoro narration → `./art run` review cut → `./art final`
4K master. Never publish.
