# QUESTION

**The question:** "An agent has 200 features to implement. It finishes 50 in
session one and the context window fills. Session two starts blank. How does
it know to resume at feature 51 — without replaying the first 50?"

**Mode:** redo — source is
`anthropics/youtube/claude-basics/feature-list-checkpoint-persistence/beat_sheet.json`
(fully-scripted Teardown-register scaffold, never built: 0/8 beats filled,
all SLATE). This reel keeps its question, facts, and body argument, re-
registers the narration to Plain, replaces the cold open with the Brutalist
Hesitant Writer, and closes with the Humanitarians AI skin.

**Why it earns a reel:** a coding agent working through a long feature list
will fill its context window and get a fresh, blank session. Naively, either
it re-reads everything already done (burns half the new context) or it
guesses where it left off (wrong). The source's fix: externalize progress to
`feature_list.json` (200 entries, each with an id and a status — incomplete
or passing) plus git as an immutable commit ledger. Every session's whole
job is: open the file, find the first entry still marked incomplete, and
start exactly there.

**Naive framing (B00, corrected on screen):** "An agent with 200 features
just remembers where it left off" → corrects "remembers" to "checks" (a
file, not a memory).
