# PROMPTS.md — "Fix your photos"

No generation prompts. This is a show-tell film: every visual is a
hand-authored Manim drawing in `scenes.py` (isometric kit + local helpers),
and the bookends are Remotion compositions (`BrutalistHesitantWriter`,
`ClaudeDefinitions`, `ClaudeComposerAsk`, `ClaudeTitleOutro`) driven by the
props in `beat_sheet.json`. Nothing was or will be produced by an image or
video generation model.

The only prompt-like text in the package is the Your-Turn composer prompt in
`beat_sheet.json` (BHTF), which is a prompt for the *viewer* to paste into
Claude, read aloud in full by the narration. It asks Claude only for a
described opinion (its verified see-and-describe ability, per the companion
film's FACTCHECK) — never to edit the photo itself:

> Attach a photo you want to fix and write: tell me what you would change
> about this photo before I print it, from most to least important. Then I
> will make the changes in my photo app, one at a time.
