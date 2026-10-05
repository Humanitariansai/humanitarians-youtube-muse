# SOURCES.md — Slides without the slog

This film is NEW (built from scratch; no mirror source). Its facts are
behavioral and modest by design; the source table below traces every
checkable element.

| # | Fact used in the film | Source |
|---|----------------------|--------|
| 1 | Series identity: "How to AI" film, Wave 6 "Making things"; slug slides-without-the-slog; title "Slides without the slog"; pitch "Turn rough notes into a real deck: outline first, then slides, then polish. Companion to the existing film the-long-game — reference it as the companion, don't re-teach it. Never quote pricing tiers." | Parent-agent task, 2026-10-05 |
| 2 | Core idea: outline first (one line per slide), then one slide per prompt, then polish (cut words, speaker notes, back-row test); the one-prompt deck comes back as walls of text; the meeting-notes scenario is the film's own dramatization | Parent-agent task, 2026-10-05 + film's own framing (see ACTS.md) |
| 3 | Companion: the-long-game (outline → sections → stitching); referenced once by name in B03, never re-taught | ~/workspace/film-builds/how-to-ai/the-long-game/ |
| 4 | Skill: show-tell (assigned; see BUILD-LOG.md for the fit decision); style, bookends, bookend exemptions, card test, drawing laws, QC gates | `~/workspace/brutalist.art/skills/make/show-tell/SKILL.md` |
| 5 | Drawing kit: iso_kit.py (isometric projection, box, page, check, T, until, finish, palette) — pasted verbatim at the top of scenes.py, never imported | `~/workspace/brutalist.art/skills/make/show-tell/templates/iso_kit.py` |
| 6 | Static QC checker (render-free, per-class mode) | `~/workspace/brutalist.art/runtime/qc/static_scene_check.py` |
| 7 | Film identity: channel claude-liam; persona "Liam, in for Bear"; Kokoro am_onyx; Teardown register; watermark @NikBearBrown; no rendering, publishing, or staging for publication; 12-file pre-render package | Parent-agent task + channel lock, 2026-10-03 |
| 8 | Channel: humanitarians AI YouTube, https://www.youtube.com/@humanitariansai | Bear, 2026-10-03 (standing lock) |
| 9 | GitHub push target: Humanitariansai/humanitarians-youtube-muse, folder `muse/youtube/how-to-use-ai/slides-without-the-slog/`; credential: secure connector custom.github / access_token via surrogate on api.github.com | Parent-agent task, 2026-10-05 |

No generation prompts were used. No external press, papers, or vendor docs
are cited; nothing in the film rests on a third-party claim. Nothing on
screen is presented as a screenshot of a real AI conversation.
