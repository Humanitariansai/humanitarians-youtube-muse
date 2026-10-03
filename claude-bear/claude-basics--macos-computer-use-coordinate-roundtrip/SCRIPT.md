# Two Resolutions, One Click — The macOS Coordinate Roundtrip — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-basics/macos-computer-use-coordinate-roundtrip`).*
*Register: **Plain**. 8 beats, matching the source's beat count. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes their Retina screenshot reaches Claude pixel for pixel. It doesn't — the API resizes it first, into a different coordinate space. So how do you get Claude's click back onto your real screen?" | Writer types "My Retina screenshot reaches Claude exactly, right?"; "exactly" hesitates and corrects to "resized" |
| B01 | 1 stakes / wrong guess | Your Mac's Retina display captures screenshots well above Claude's vision budget: every image gets tiled into 28 by 28 patches, capped at 1568 pixels on the long edge and 1568 tiles total. The natural guess is that the coordinate Claude reports back already matches your screen's real pixels. Click there without resizing first, and the server resizes it anyway — in a space you never saw. | a native screenshot far larger than a capped tile grid; the same raw coordinate carried across misses |
| B02 | setup — ANCHOR PLANTED | Here's the concrete case. Your screen is 1920 by 1080, and the button sits at 960, 540. Before Claude ever sees the screenshot, the reference implementation's target underscore image underscore size resizes it to 1456 by 819. On that resized image, the very same button now sits at 728, 409 — a different number, for the same pixel. | THE ANCHOR — native rect 1920×1080 with the button at (960,540); resized rect 1456×819 with the same button now at (728,409) |
| B03 | mechanism | target underscore image underscore size runs a binary search: the largest width and height that keep the long edge under 1568 pixels and the tile count under 1568, while preserving the aspect ratio. You call it yourself, before you ever send the screenshot, and you record what it returns — 1456 by 819. Those sent dimensions are the denominator of every inverse you'll ever compute. | formula/algorithm card: binary search → (1456, 819); "record sent_w, sent_h" |
| B04 | ANCHOR PAYOFF / both directions | Now invert it. Real equals model coordinate times original over sent. 728 times 1920 over 1456 is 960. 409 times 1080 over 819 is 540 — the click lands exactly on the button. That inverse only works because you recorded genuine sent dimensions from your own resize. Skip that step, or let a screenshot that was already inside budget pass through unresized, and there's nothing to invert — target underscore image underscore size just hands the input straight back. | THE ANCHOR RETURNS — same two rectangles; the (728,409) dot carried back by the ratio lands exactly on the (960,540) button; a third, already-in-budget rectangle shown passing through unchanged, struck through with "nothing to invert" |
| **BCRY** | **carry-out** | On macOS, Claude's click lands in the resized copy of your screenshot, not your native display — record the size you sent, then multiply back by original over sent to hit the real pixel. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. On macOS my screenshot gets resized to 1456 by 819 before Claude sees it — write the inverse transform so the click hits the native display. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Two Resolutions, One Click — The macOS Coordinate Roundtrip. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, partly-built scaffold) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Two Resolutions, One Click — The macOS Coordinate Roundtrip." | unchanged |
| Facts | `target_image_size()` binary search (long-edge ≤1568px, tile-count ≤1568, 28×28 patches); native 1920×1080 → sent 1456×819; anchor (960,540)→(728,409)→(960,540); exclusions: batched tool calls, trajectory recording, non-macOS platforms, no-op case | unchanged (SOURCES.md) |
| Beat count | 8 (B00–B05, YOURTURN, B07 — the source also carried three unfilled/blank `BOOKEND`-lane placeholders, BVDT/BHTF/BOUT, never populated; dropped as dead scaffold, not content) | 8 (B00–B04, BCRY, BHTF, BOUT) |
| B00 | `ClaudeComposerAsk` cold open, never built (SLATE), stating the full 2560×1600 puzzle as a text card | `BrutalistHesitantWriter` (WRITER LAW) — the source's B00 example (2560×1600 → 728,410 → 1280,800) used a different, unverified aspect-ratio pairing than the source's own B03 centerpiece (1920×1080 → 1456×819 → 728,409 → 960,540, verified 16:9-to-16:9 in SOURCES.md); this redo keeps only the verified example and drops the inconsistent one, per "facts must be true and current" |
| Register | Teardown (metadata), narration carried no actual verdict | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Your Turn prompt | "On macOS my screenshot gets resized to 1456x819 before Claude sees it — write the inverse transform so the click hits the native display." (source YOURTURN beat) | same prompt, carried over verbatim |

No beat in the source was `ai-video-prompt`, pantry, or a human-drop slot —
the source's beats were already `ClaudeComposerAsk`/`FormBCard`/
`ClaudeTitleOutro` (Remotion) shapes, just mostly unbuilt — so the NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00 (which the WRITER LAW
covers anyway). The source's B05 verdict/recap beat is dropped as a
restatement; its content (the resize-then-invert recap) is already carried
by B03/B04. The source's B04 honesty/exclusions beat is folded into B04's
both-directions clause rather than kept as a separate beat, since this
reel's body runs four beats instead of the source's five.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (Claude's coordinate = your screen's real pixels); B02's anchor is the falsifying case (same button, two different numbers depending on which image you're looking at) |
| One anchor, planted early, paid off late | B02 plants the 960,540 / 728,409 case; B04 pays it off (inverted back to 960,540, exactly) |
| Both directions | B04 — the inverse lands the click when you recorded genuine sent dimensions from your own resize; it has nothing to invert when a screenshot was already inside budget and passed through unresized |
| No design judgment | B03–B04 describe why the algorithm behaves this way; nothing rules on whether porting the API's resize client-side is the "right" design |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not a specific MacBook model's native resolution.** Retina resolutions
  vary by model; B01 describes the mismatch generically and the anchor uses
  one verified 16:9 example.
- **Not non-macOS platforms, batched tool calls, or trajectory recording.**
  Source exclusions, untouched.
- **No verdict on the design.** Explaining why the resize-then-invert pattern
  works is not the same as ruling on whether porting the API's algorithm
  client-side is the best approach — that would be Teardown's lane.

## Handoff prompt (BHTF, read aloud)

> "On macOS my screenshot gets resized to 1456x819 before Claude sees it —
> write the inverse transform so the click hits the native display."

Why it's worth running: it turns the reel's formula into working code
against your own numbers, and a good answer should also handle the no-op
case (sent equals original) — a detail the reel names but doesn't dwell on.

---
**GATE P — signed:** ______________________  (human)
