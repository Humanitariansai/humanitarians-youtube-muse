# PROMPTS.md — Say what you want, plainly

No generation prompts were used in this build. There was no image, video,
or audio generation step: the visuals are hand-written Manim scenes
(`scenes.py`), the bookends are Remotion compositions driven by
`beat_sheet.json`, and narration audio is generated at render time on
Bear's Mac via `generate_audio_kokoro.py` (see `CLAUDE-CODE-RENDER.md`).

The prompts that shaped the film are the standing ones:

- The parent task spec (slug, title, pitch, REFACTOR source, assigned
  skill, the 12-file package convention, the QC gate, the push flow).
- The `show-tell` skill (`~/workspace/brutalist.art/skills/make/show-tell/SKILL.md`),
  read end to end before writing: one image per beat, the voice explains,
  the fixed bookends, the drawing laws, the card test.
- The mirror-repo source lesson's own argument (four dimensions, the new
  employee, the summary example) — refactored, not quoted.
- The `ClaudeComposerAsk` Your Turn prompt (in `make_sheet.py` as
  `YT_PROMPT`) is the film's handoff text, written for this film.
