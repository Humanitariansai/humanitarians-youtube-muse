# PROMPTS.md — "Shop smarter"

No generation prompts. This is a show-tell film: every visual is a
hand-authored Manim drawing in `scenes.py` (isometric kit + local helpers),
and the bookends are Remotion compositions (`BrutalistHesitantWriter`,
`ClaudeDefinitions`, `ClaudeComposerAsk`, `ClaudeTitleOutro`) driven by the
props in `beat_sheet.json`. Nothing was or will be produced by an image or
video generation model.

The only prompt-like text in the package is the Your-Turn composer prompt in
`beat_sheet.json` (BHTF), which is a prompt for the *viewer* to paste into
Claude, read aloud in full by the narration:

> I'm choosing between two options: [A] and [B]. My priorities are: [X, Y, Z].
> Lay them out side by side, one row per priority, then tell me what I'd be
> giving up with each.

The narration also quotes two shorter asks the viewer can reuse: "read the
reviews and tell me what the unhappy buyers agree on" (B04) and "what's the
catch here?" (B05).
