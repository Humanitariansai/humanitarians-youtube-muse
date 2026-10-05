# PROMPTS.md — "AI that sees"

No generation prompts. This is a show-tell film: every visual is a
hand-authored Manim drawing in `scenes.py` (isometric kit + local helpers),
and the bookends are Remotion compositions (`BrutalistHesitantWriter`,
`ClaudeDefinitions`, `ClaudeComposerAsk`, `ClaudeTitleOutro`) driven by the
props in `beat_sheet.json`. Nothing was or will be produced by an image or
video generation model.

The only prompt-like text in the package is the Your-Turn composer prompt in
`beat_sheet.json` (BHTF), which is a prompt for the *viewer* to paste into
Claude, read aloud in full by the narration:

> Take a photo of something you would normally retype: a receipt, an error
> message, a plant. Attach it and write: what is this, and what should I do
> about it?
