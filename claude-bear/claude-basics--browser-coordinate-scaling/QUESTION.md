# QUESTION

**The question:** "Bridging the Pixel Gap in Browser Automation." — how do you
turn the coordinates Claude reports after looking at a screenshot into a
click that actually lands on your real screen?

**Mode:** redo — source is
`anthropics/youtube/claude-basics/browser-coordinate-scaling/beat_sheet.json`
(scaffold only, never built: 0/8 beats filled, no SCRIPT.md, Teardown
register). This reel keeps its question, facts, and body argument,
re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, and closes with the Humanitarians AI skin.

**Why it earns a reel:** Claude's vision encoder normalizes every 16:9
screenshot to exactly 1456×819 before it looks at it. The natural assumption
is that the (x, y) Claude reports back is already in your screen's real
pixel coordinates. It isn't — clicking at that raw pixel on a different
viewport misses the target. The fix is the inverse of the resize ratio:
multiply Claude's x by viewport-width-over-1456 and its y by
viewport-height-over-819, then clamp to the screen's edges.

**Naive framing (B00, corrected on screen):** "Claude's click coordinates
are my screen's exact pixels, right?" → corrects "exact" to "scaled."
