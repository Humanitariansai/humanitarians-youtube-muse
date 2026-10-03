# QUESTION

**The question:** "Two Resolutions, One Click — The macOS Coordinate
Roundtrip." — Claude's click coordinates come back in the space of a resized
screenshot. How do you get that click to land on your Mac's real, native
display?

**Mode:** redo — source is
`anthropics/youtube/claude-basics/macos-computer-use-coordinate-roundtrip/beat_sheet.json`
(scaffold, mostly unbuilt: 4/8 beats had Manim graphics but no B00/B05/B06/B07
media, no SCRIPT.md, Teardown register). This reel keeps its question, facts,
and body argument, re-registers the narration to Plain, replaces the cold
open with the Brutalist Hesitant Writer, and closes with the Humanitarians AI
skin.

**Why it earns a reel:** macOS Retina screenshots are routinely larger than
Claude's per-image budget — every screenshot gets tiled into 28×28 patches,
capped at a 1568px long edge and 1568 tiles total. The reference
implementation (`computer_use/image.py`) ports the API's own resize algorithm
as `target_image_size()` so you can pre-resize yourself, record what you
sent, and invert the transform once Claude clicks. Skip the pre-resize and
the server resizes again in a space you never observed — click drift.

**Naive framing (B00, corrected on screen):** "My Retina screenshot reaches
Claude exactly, right?" → corrects "exactly" to "resized."

**The anchor (verified, SOURCES.md):** native screen 1920×1080, button at
(960, 540). `target_image_size(1920, 1080)` → (1456, 819) — same 16:9 aspect
ratio, so the resize is consistent. On the resized image the button appears
at (728, 409). The inverse — `real = model × original / sent` — recovers
(960, 540) exactly.
