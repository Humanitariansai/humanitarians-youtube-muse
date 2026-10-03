# Bridging the Pixel Gap in Browser Automation.

When Claude looks at a screenshot during browser automation or computer use,
its vision encoder resizes every 16:9 image to exactly 1456×819 before it
looks at anything. The natural assumption is that the (x, y) coordinates
Claude reports back are already in your screen's real pixels. They aren't —
click at that raw pixel on your actual viewport and you miss the button
entirely. The fix is the inverse of the resize ratio: multiply Claude's x by
your viewport width over 1456, and its y by your viewport height over 819,
then clamp to the screen's edges. This video walks through a concrete case —
a click reported at (728, 409) on the resized screenshot, scaled to land
exactly on target at (1280, 720) on a real 2560×1440 screen.

**Topic:** BROWSER AUTOMATION · COMPUTER USE
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--browser-coordinate-scaling

---

## Chapters

0:00 Claude's coordinates — my screen's exact pixels?
0:11 The wrong guess: same raw pixel, wrong screen
0:30 The anchor: (728, 409) on the wrong canvas
0:50 The fix: the inverse resize ratio
1:07 The anchor returns: scaled, and it lands
1:38 Carry-out
1:46 Your turn
2:02 Outro

---

## YOUR TURN

My model clicks at (700, 410) on a 1456x819 screenshot but my screen is
1920x1080 — write the scaling and land the click exactly.

Run that today, against your own browser automation or computer-use setup.

---

## Deliberately not claimed

Not how non-16:9 viewport scaling works (a different lookup table). Not DOM
navigation or CSS-selector clicking. Not a verdict on whether coordinate
scaling is the "right" way to do browser automation — that's a design
judgment this video doesn't make.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #BrowserAutomation #ComputerUse #LLM #HumanitariansAI #ProfessorBear #ClaudeBasics

---
