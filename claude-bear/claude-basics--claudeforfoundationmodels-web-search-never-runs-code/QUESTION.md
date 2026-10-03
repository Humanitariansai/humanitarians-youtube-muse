# QUESTION

**The question:** "Why does web search never run your code, but your own
tool always does — with identical syntax?"

**Mode:** redo — source is
`anthropics/youtube/claude-basics/claudeforfoundationmodels-web-search-never-runs-code/beat_sheet.json`
(scaffold only, never built: build shows `"filled": 0, "of": 8`, no SCRIPT.md,
Teardown register, CHECKS-REPORT.md shows `checks_green: False`, BLOCKED on
the bookend gate — no hesitant-writer/BVDT/BHTF). This reel keeps its
question, facts, and body argument, re-registers the narration to Plain,
replaces the cold open with the Brutalist Hesitant Writer, and closes with
the Humanitarians AI skin.

**Why it earns a reel:** `.webSearch(maxUses: 5)` in `serverTools` and a
Swift `lookupFavorites()` in `tools` are declared the same way, in the same
file — yet web search's result lands inside the same turn, while
`lookupFavorites()` forces the model to stop and wait for a second request.
The split isn't about how the tool is declared; it's about who can execute
it. Web search runs on infrastructure Anthropic already owns (a web index,
a sandbox), so Anthropic finishes the call itself, in-turn. `lookupFavorites`
is arbitrary code on the caller's device — only the caller can run it, which
forces an exit-and-return.

**Naive framing (B00, corrected on screen):** "A tool call should always
round-trip through my code" → corrects "always" to "sometimes."
