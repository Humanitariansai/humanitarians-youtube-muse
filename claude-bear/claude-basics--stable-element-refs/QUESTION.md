# QUESTION

**The question:** "Stable Reference IDs Survive Viewport Chaos." — you tell
Claude to click a button by pixel coordinate; the window gets resized; how do
you make the click still land on the right button?

**Mode:** redo — source is
`anthropics/youtube/claude-basics/stable-element-refs/beat_sheet.json`
(scaffold only, never built: 0/8 beats filled, Teardown register/audience
metadata, no SCRIPT.md). This reel keeps its question, facts, and body
argument, re-registers the narration to Plain, replaces the cold open with
the Brutalist Hesitant Writer, and closes with the Humanitarians AI skin.

**Why it earns a reel:** Pixel-based browser automation ties a click command
to one location in one viewport. Resize the window and the page reflows —
the button moves, the coordinate doesn't, and the click misses. The fix runs
before Claude ever looks at the page: a script walks every clickable element
and stamps a stable reference id onto it (a `data-ref` attribute, e.g.
`ref="confirm_order_1"`). Claude targets elements by that name instead of by
pixel. The ref is attached to the element, not to a screen position, so it
survives a resize; a pixel coordinate does not.

**Naive framing (B00, corrected on screen):** "Pixel position is a stable
way to find a button, right?" → corrects "stable" to "fragile."
