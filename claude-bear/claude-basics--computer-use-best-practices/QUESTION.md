# QUESTION

**The question:** "Computer Use: Demo to Production." — what actually has to
change to take a computer-use agent from a working demo to something you'd
trust running unattended?

**Mode:** redo — source is
`anthropics/youtube/claude-basics/computer-use-best-practices/beat_sheet.json`
(a partially-filled legacy scaffold: Teardown-register metadata, B00–B06
narrated and built, three additional bookend slates — BVDT/BHTF/BOUT — left
unbuilt and never reconciled with the earlier beats; GATE T failed per its
NEEDS-REVIEW.md). This reel keeps the question and the source's body facts,
re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's handoff/outro into a proper
carry-out + Your Turn + outro closing block, and closes with the
Humanitarians AI skin.

**Why it earns a reel:** the naive computer-use loop — screenshot, send the
full image to Claude, get an action, repeat — burns tokens fast: a
full-resolution screenshot costs roughly 1,200 tokens, so a 20-step task can
spend on the order of 40,000 screenshot tokens before a single action token.
The production version makes seven changes to that loop (resize to ~1568px
wide, prune old screenshots, batch tool calls, cache the system prompt,
compact server-side, sandbox execution, and record every action as a
structured trajectory event); resizing and pruning alone cut the screenshot
bill roughly 70–80%. The seventh change, trajectory recording, answers a
different question — not cost, but whether you can tell what an autonomous
run actually did.

**Naive framing (B00, corrected on screen):** "Going to production just
means running the demo longer, right?" → corrects "longer" to "leaner."

**Body facts carried from source (unchanged):**
- naive loop: screenshot → full image to Claude → action → repeat
- ~1,200 tokens per full-resolution screenshot
- 20-step task, no optimization: ~40,000 screenshot tokens before any action
- seven production changes: resize to ~1568px wide, prune old screenshots,
  batch tool calls, cache-control on system prompts, server-side compaction,
  sandboxed execution, structured trajectory recording
- resize + prune cuts the screenshot bill ~70–80%
- trajectory recording: every click/keypress/screenshot logged with
  timestamp, tool, arguments, result — replayable exactly
