# Computer Use: Demo to Production.

The naive computer-use loop — screenshot, send the full image to Claude, get
an action, repeat — burns tokens fast: a full-resolution screenshot costs
around 1,200 tokens, so a 20-step task with no changes can spend on the order
of 40,000 screenshot tokens before a single action token. The production
version makes seven changes to that loop: resize every screenshot to about
1568px wide, drop screenshots older than the last few steps, batch tool
calls, cache the system prompt, compact the history server-side, run actions
in a sandbox, and record every action as a structured trajectory event.
Resize and prune alone cut the screenshot bill 70 to 80 percent. The seventh
change, trajectory recording, answers a different question — not cost, but
whether you can tell what an autonomous run actually did: a logged run proves
what the agent did, not that it did the right thing.

**Topic:** COMPUTER USE · CLAUDE BASICS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--computer-use-best-practices

---

## Chapters

0:00 Going to production just means running it longer, right?
0:11 The naive loop and its running bill
0:31 The concrete case: ~40,000 screenshot tokens
0:45 Seven changes
1:06 Cut down, and a second question
1:24 Carry-out
1:32 Your turn
1:50 Outro

---

## YOUR TURN

Design a trajectory logging schema for a computer-use agent: action type,
target element, screenshot hash before and after, confidence score, and
whether human confirmation was requested. What else does the log need to make
oversight meaningful — not just nominal?

Run that today, against your own computer-use or agentic-loop setup.

---

## Deliberately not claimed

Not a cost guarantee for any specific deployment — the 70-80% figure is the
source's reported range for resize + prune, not a promise. Not that
trajectory logging prevents mistakes — a fully logged run still proves only
what happened, not that it was the right action. No verdict on whether
computer-use is the right approach for a given task — that's a design
judgment this video doesn't make.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ComputerUse #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
