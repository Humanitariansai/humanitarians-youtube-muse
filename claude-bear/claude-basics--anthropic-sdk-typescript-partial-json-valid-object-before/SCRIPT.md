# Why Partial JSON Can Be a Valid Object Before the Closing Brace Arrives — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-basics/anthropic-sdk-typescript-partial-json-valid-object-before`).*
*Register: **Plain**. 8 beats, matching the source's beat count. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a half-finished JSON string must be broken until the brace arrives. It isn't — the SDK hands back a usable object after every chunk. So how does a partial string already parse as one?" | Writer types "This half-finished string must be broken, right?..."; "broken" hesitates and corrects to "usable" |
| B01 | 1 stakes / wrong guess | When Claude streams a tool call, `JSON.parse` demands a complete document — feed it a half-finished string and it throws. So the natural guess is that a streaming snapshot behaves the same way: broken, or empty, until the brace lands. Read it early, and you'd expect an error, not an object. | a single string splitting into a THROWS path (standard parser) and a question-marked path (streaming snapshot) |
| B02 | setup — ANCHOR PLANTED | Here's the concrete case. A search tool streams the argument `{"q": "solar` across four chunks. `.on('inputJson')` fires with `jsonSnapshot` equal to `{}`, then `{"q":""}`, then `{"q":"sol"}`, then `{"q":"solar"}` — four snapshots, and every single one already a complete, parseable object. | THE ANCHOR — four snapshots ticking across a timeline, each stamped VALID |
| B03 | mechanism | Here's why. The parser keeps a stack of every object and array it has opened. The instant a chunk ends, it closes each open structure with a zero-value default — an empty string, an empty object — and hands back whatever that produces. Nothing waits for the real closing brace; the parser supplies its own. | a token stream feeding a stack; the stack sealing shut into a complete tree at each cut point |
| B04 | ANCHOR PAYOFF / both directions | So back to the search call: `{}` isn't an empty query — it's a query string that hasn't started arriving yet. And `{"q":"sol"}` isn't the final query either — three more characters are still on the wire. A valid snapshot tells you the shape is safe to read; it doesn't tell you the value inside has stopped changing. | THE ANCHOR RETURNS — the same four snapshots, now each split into "shape: safe" and "value: still growing" |
| **BCRY** | **carry-out** | The parser closes every open structure for you — so a valid snapshot tells you the shape is safe to read, not that the values inside it are finished. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. I'm streaming a tool call with the Anthropic TypeScript SDK and I see partial JSON arriving via the inputJson event. Walk me through why each chunk's jsonSnapshot is already a valid JS object before the closing brace arrives, and show me how to read a field from it safely mid-stream without waiting for the tool_use_delta done event. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why partial JSON can be a valid object before the closing brace arrives. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, unbuilt scaffold) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Why partial JSON can be a valid object before the closing brace arrives" | unchanged |
| Facts | `.on('inputJson')` fires per chunk with a `jsonSnapshot` that is already a valid JS object though the source string has no closing brace; the parser keeps a token stack and closes open structures with zero-value defaults at each boundary; the `{"q": "solar` / four-snapshot example | unchanged |
| Beat count | 8 (B00–B05, YOURTURN, OUTRO) | 8 (B00–B04, BCRY, BHTF, BOUT) |
| B00 | `FormBCard` cold open stating the concrete `search_database` case as a text card | `BrutalistHesitantWriter` (WRITER LAW) — the concrete case moves to B02 as the planted anchor |
| Register | Teardown (metadata), though narration carried no actual verdict | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Your Turn prompt | "I'm streaming a tool call with the Anthropic TypeScript SDK and I see partial JSON arriving via the inputJson event…" | same prompt, carried over verbatim (the practical takeaway doesn't change with register) |

No beat in the source was `ai-video-prompt`, pantry, or a human-drop slot —
the source's beats were already `FormBCard`/`ClaudeComposerAsk`/`ClaudeTitleOutro`
(Remotion) shapes, just unbuilt — so the NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00 (which the WRITER LAW covers anyway). The source's
B00 cold open (the concrete `search_database` case) and B04 (the four-chunk
example) were merged into this reel's B02/B04 anchor pair, since hai-simple's
spine puts the concrete case after the stakes/wrong-guess beat rather than as
the very first thing on screen.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (partial = broken/unusable); B02's anchor is the falsifying case (four snapshots, each already a valid object) |
| One anchor, planted early, paid off late | B02 plants the four-chunk `{"q": "solar` case; B04 pays it off (shape-safe vs. value-still-growing) |
| Both directions | B04 — `{}` looking empty doesn't mean no args are coming; `{"q":"sol"}` looking complete doesn't mean the value has stopped changing |
| No design judgment | B03–B04 describe why the parser behaves this way; nothing rules on whether closing with defaults is the "right" design |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not which zero-value default applies to which type.** The source
  excludes full JSON edge cases (numbers, unicode); the reel says "a
  zero-value default — an empty string, an empty object" without cataloguing
  every type's default.
- **Not how the accumulator or event loop wires this into application
  state.** The source excludes that wiring; the reel stops at the snapshot
  itself.
- **No verdict on the design.** Explaining why every prefix parses cleanly
  is not the same as ruling on whether closing structures with defaults is
  the best way to build a streaming parser — that would be Teardown's lane.

## Handoff prompt (BHTF, read aloud)

> "I'm streaming a tool call with the Anthropic TypeScript SDK and I see
> partial JSON arriving via the `inputJson` event. Walk me through why each
> chunk's `jsonSnapshot` is already a valid JS object before the closing
> brace arrives, and show me how to read a field from it safely mid-stream
> without waiting for the `tool_use_delta` done event."

Why it's worth running: it turns the reel's claim into working code against
the viewer's own streaming tool-call handler, not just the reel's
description of it.

---
**GATE P — signed:** ______________________  (human)
