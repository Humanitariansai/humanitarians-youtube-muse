# Why partial JSON can be a valid object before the closing brace arrives

Streaming a `search_database` tool call through the Anthropic TypeScript SDK,
`.on('inputJson')` fires on every chunk with a `jsonSnapshot` that is already
a valid JS object — even though the source string it was built from has no
closing brace yet. A standard JSON parser throws on anything incomplete, so
the natural assumption is that a half-finished string must be unusable too.
It isn't: the vendored parser keeps a stack of every structure it has opened
and, the instant a chunk ends, closes each one with a zero-value default —
so every prefix of the stream comes back syntactically complete. This video
walks through a four-chunk case (`{"q": "solar` arriving piece by piece)
where every single snapshot is already a valid object, and unpacks the
distinction that actually matters: shape-safe versus value-finished.

**Topic:** CLAUDE BASICS · STREAMING TOOL INPUTS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--anthropic-sdk-typescript-partial-json-valid-object-before

---

## Chapters

0:00 This half-finished string must be broken, right?
0:12 The natural guess: it behaves the same way
0:27 The anchor: four chunks of one query
0:43 Why: the stack seals itself shut
0:59 The anchor returns: shape safe, value still growing
1:16 Carry-out
1:24 Your turn
1:46 Outro

---

## YOUR TURN

I'm streaming a tool call with the Anthropic TypeScript SDK and I see
partial JSON arriving via the `inputJson` event. Walk me through why each
chunk's `jsonSnapshot` is already a valid JS object before the closing
brace arrives, and show me how to read a field from it safely mid-stream
without waiting for the `tool_use_delta` done event.

Run that today, against your own streaming tool-call handler.

---

## Deliberately not claimed

Not which zero-value default applies to which JSON type — the source
excludes full JSON edge cases like numbers and unicode. Not how the
accumulator or event loop wires this into application state. Not a verdict
on whether closing structures with defaults is the "right" way to build a
streaming parser — that's a design judgment this video doesn't make.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AnthropicSDK #LLM #HumanitariansAI #ProfessorBear #ClaudeBasics

---
