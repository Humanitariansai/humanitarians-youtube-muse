# Stable Reference IDs Survive Viewport Chaos.

Browser automation that clicks by pixel coordinate ties a command to one spot
in one viewport. Resize the window and the page reflows — the button moves,
the coordinate doesn't, and the click lands somewhere else, every time. The
fix runs before Claude ever looks at the page: a script walks every clickable
element and stamps it with a stable reference id (a `data-ref` attribute, e.g.
`ref="confirm_order_1"`) baked into the page itself. Claude then targets
elements by that name instead of by pixel — the ref is attached to the
element, not to a screen position, so it survives a resize. This video walks
through a concrete case — a "Confirm Order" button at (960, 540) on a
1920×1080 window that moves to (720, 405) after a resize to 1440×900, while
its ref stays exactly the same.

**Topic:** BROWSER AUTOMATION · COMPUTER USE
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--stable-element-refs

---

## Chapters

0:00 Pixel position is a stable way to find a button, right?
0:12 The wrong guess: pixel ties to one viewport
0:25 The anchor: Confirm Order, before and after
0:43 The fix: stamped before Claude looks
0:56 The anchor returns: the ref stays, the click lands
1:15 Carry-out
1:24 Your turn
1:39 Outro

---

## YOUR TURN

Assign stable refs to every clickable element on this page so my automation
survives a resize.

See what naming scheme it picks, whether it handles iframes, and whether it
guards against assigning the same ref twice — run it today against your own
browser automation or computer-use setup.

---

## Deliberately not claimed

Not the JavaScript injection mechanics or CSS specificity rules that affect
ref injection. Not dynamic elements added to the page after the ref pass ran
— those need their own re-injection pass. Not a verdict on whether ref-based
targeting is the "right" way to build browser automation — that's a design
judgment this video doesn't make.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #BrowserAutomation #ComputerUse #LLM #HumanitariansAI #ProfessorBear #ClaudeBasics

---
