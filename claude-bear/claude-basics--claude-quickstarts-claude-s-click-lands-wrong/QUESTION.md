# QUESTION

**The question:** "Why does Claude's click land in the wrong spot — and what's
the one ratio that fixes it?"

**Mode:** redo — source is
`anthropics/youtube/claude-basics/claude-quickstarts-claude-s-click-lands-wrong/beat_sheet.json`
(scaffold only, never built: 0/8 beats filled, Teardown register). This reel
keeps its question, facts, and body argument, re-registers the narration to
Plain, replaces the cold open with the Brutalist Hesitant Writer, and closes
with the Humanitarians AI skin.

**Why it earns a reel:** a computer-use app sends Claude a downscaled
screenshot (say 1456×819) of a full-size desktop (1920×1080), because that's
the resolution the vision API accepts. Claude picks a point on the screenshot
it saw and returns those coordinates. Sent straight to the OS input driver,
the click lands somewhere else entirely — because Claude's coordinates
describe the smaller image, not the real screen. The fix is one line of
arithmetic: scale each axis by original-resolution ÷ sent-resolution before
you click.

**Naive framing (B00, corrected on screen):** "Claude's click is just random
guessing" → corrects "guessing" to "scaling."
