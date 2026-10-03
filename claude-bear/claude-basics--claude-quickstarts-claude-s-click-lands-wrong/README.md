# Why Claude's Click Lands in the Wrong Spot — and the One Ratio That Fixes It

A computer-use app sends Claude a downscaled screenshot — say 1456×819 — of a
full-size desktop, because that's the resolution the vision API accepts.
Claude picks a point on the screenshot it saw and returns those coordinates.
Sent straight to the OS input driver, the click lands somewhere else entirely
— not because Claude guessed wrong, but because its coordinates describe the
smaller image, not your real screen. This walks the one ratio that fixes it:
multiply by original-over-sent, per axis.

**Topic:** CLAUDE BASICS · COORDINATE SCALING
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--claude-quickstarts-claude-s-click-lands-wrong

---

## Chapters

0:00 The naive framing: is Claude just guessing?
0:10 The question: how do coordinates cross sizes?
0:22 The anchor: sent raw, it misses the button
0:38 The mechanism: the one scaling formula
0:48 The anchor returns: scaled, it lands dead center
1:11 Carry-out
1:21 Your turn
1:47 Outro

---

## YOUR TURN

My computer-use app sends Claude a 1456 by 819 view of a 1920 by 1080
screen. Claude returns click coordinates in the view's coordinate space.
Show me the two-line scaling formula I need before passing those
coordinates to the OS input driver, and explain what happens if I skip it
on a Retina display with a device pixel ratio of two.

Run that today, against your own computer-use setup.

---

## Deliberately not claimed

Not naming a specific resize algorithm — the source doesn't specify how the
vision API downscales the image, so the reel doesn't invent one. Not a claim
about every computer-use framework — the ratio generalizes mathematically,
but the reel demonstrates it on the source's one input/output pair plus its
own second resolution as confirmation. No verdict on whether sending a
downscaled screenshot is the "right" design for a vision API — explaining
why the coordinates need scaling is not the same as ruling on the design.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ComputerUse #CoordinateScaling #ClaudeBasics #LLM #HumanitariansAI #ProfessorBear

---
