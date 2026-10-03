# Two Resolutions, One Click — The macOS Coordinate Roundtrip.

When Claude looks at a screenshot during macOS computer use, its vision
budget caps every image at a 1568px long edge and 1568 tiles of 28×28
patches — well below what a native Retina screenshot captures. The natural
assumption is that the (x, y) coordinate Claude reports back is already in
your screen's real pixels. It isn't: skip the resize and the server resizes
the image anyway, in a space you never observed — click drift. The reference
implementation ports the API's own resize algorithm as `target_image_size()`
so you can resize first, record what you sent, and invert the transform once
Claude clicks: real equals model coordinate times original over sent. This
video walks through a concrete case — a native 1920×1080 screen with a
button at (960, 540), resized to 1456×819 so Claude sees the button at
(728, 409), inverted back to land exactly at (960, 540).

**Topic:** COMPUTER USE · macOS · COORDINATE SCALING
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--macos-computer-use-coordinate-roundtrip

---

## Chapters

0:00 My Retina screenshot reaches Claude exactly, right?
0:12 The wrong guess: over budget, resized either way
0:35 The anchor: one button, two numbers
0:59 The fix: the forward call
1:25 The anchor returns: inverted, and it lands
1:57 Carry-out
2:08 Your turn
2:22 Outro

---

## YOUR TURN

On macOS my screenshot gets resized to 1456x819 before Claude sees it —
write the inverse transform so the click hits the native display.

Run that today, against your own macOS computer-use setup.

---

## Deliberately not claimed

Not a specific MacBook resolution — Retina native resolutions vary by model;
the arithmetic uses one verified 16:9 example. Not non-macOS platforms,
batched tool calls, or trajectory recording — the source names these as
exclusions. Not a verdict on whether porting the API's resize algorithm
client-side is the "right" design — that's a design judgment this video
doesn't make.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ComputerUse #macOS #LLM #HumanitariansAI #ProfessorBear #ClaudeBasics

---
