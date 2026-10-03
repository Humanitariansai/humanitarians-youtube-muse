# PROMPTS.md — "How to outsource everything to AI & get dumb"

No generation prompts. Nothing in this film was made with a generative image,
video, or audio model:

- All body visuals are deterministic Manim vector drawings authored in `scenes.py`
  (isometric kit + the film's own cast), rendered locally.
- The four bookends are deterministic house Remotion patterns
  (BrutalistHesitantWriter, ClaudeDefinitions, ClaudeComposerAsk, ClaudeTitleOutro).
- Narration is synthesized locally with Kokoro (voice `am_onyx`) from the fixed
  narration text in `beat_sheet.json` — no prompt engineering involved.

The only prompt a viewer ever sees is the Your Turn handoff prompt, which is
content of the film (a prompt for the viewer to paste into their own AI), not a
production prompt.
