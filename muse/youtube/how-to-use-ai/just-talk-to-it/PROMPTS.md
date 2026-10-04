# PROMPTS.md — "Just talk to it"

No generation prompts. This is a show-tell film: every visual is a
hand-authored Manim drawing in `scenes.py` (isometric kit + local helpers),
and the bookends are Remotion compositions (`BrutalistHesitantWriter`,
`ClaudeDefinitions`, `ClaudeComposerAsk`, `ClaudeTitleOutro`) driven by the
props in `beat_sheet.json`. Nothing was or will be produced by an image or
video generation model.

The only prompt-like text in the package is the Your-Turn composer prompt in
`beat_sheet.json` (BHTF), which is a prompt for the *viewer* to paste into
Claude, read aloud in full by the narration:

> Open voice mode in the AI app you use, and brainstorm out loud with me for
> two minutes: a weekend trip, a project, or a gift idea. Then say: summarize
> our plan in text.
