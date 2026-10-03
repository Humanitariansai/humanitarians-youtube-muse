# QUESTION

**The question:** "Why can partial JSON be a valid object before the closing brace arrives?"

**Mode:** redo — source is
`anthropics/youtube/claude-basics/anthropic-sdk-typescript-partial-json-valid-object-before/beat_sheet.json`
(scaffold only, never built: 0/8 beats filled, no SCRIPT.md, Teardown register).
This reel keeps its question, facts, and body argument, re-registers the
narration to Plain, replaces the cold open with the Brutalist Hesitant
Writer, and closes with the Humanitarians AI skin.

**Why it earns a reel:** streaming a `search_database` tool call through the
Anthropic TypeScript SDK, `.on('inputJson')` fires on every chunk with a
`jsonSnapshot` that is already a valid JS object — even though the source
string it was built from has no closing brace yet. A standard JSON parser
throws on anything incomplete, so the natural assumption is that a
half-finished string must be unusable too. It isn't: the vendored parser
keeps a stack of every structure it has opened and, the instant a chunk
ends, closes each one with a zero-value default (an empty string, an empty
object) — so every prefix of the stream comes back syntactically complete.

**Naive framing (B00, corrected on screen):** "This half-finished string
must be broken, right?" → corrects "broken" to "usable."

**Source:** `anthropic-sdk-typescript/src/_vendor/partial-json-parser/README.md`
(as recorded in the source scaffold's `metadata.source` field).
