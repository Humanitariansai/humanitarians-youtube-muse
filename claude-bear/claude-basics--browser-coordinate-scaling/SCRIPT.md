# Bridging the Pixel Gap in Browser Automation — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-basics/browser-coordinate-scaling`).*
*Register: **Plain**. 8 beats, matching the source's beat count. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude's click coordinates land on your screen's exact pixels. They don't — they're scaled from a resized copy of your screenshot. So how do you turn Claude's numbers into a real screen coordinate?" | Writer types "Claude's click coordinates are my screen's exact pixels, right?"; "exact" hesitates and corrects to "scaled" |
| B01 | 1 stakes / wrong guess | The browser tool screenshots your screen and sends it to Claude, but Claude's vision encoder resizes every 16:9 image to exactly 1456 by 819 before it looks at anything. The natural guess is that the coordinates Claude reports back are already in your screen's pixels. Click there, and you miss the button. | a small screenshot rectangle and a larger real-screen rectangle; a dot maps straight across at the same raw numbers and misses |
| B02 | setup — ANCHOR PLANTED | Here's the concrete case. Claude's screenshot is 1456 by 819, and it reports a click at 728, 409 — dead center of that image. Your real viewport is 2560 by 1440. Click at that same pixel on your actual screen, and you land near the top-left corner, nowhere close to the button. | THE ANCHOR — screenshot rect labelled 1456×819 with a dot at (728,409); the same raw pixel plotted on the larger 2560×1440 rect lands near the corner, marked with a miss |
| B03 | mechanism | The fix is the inverse of the resize ratio. Multiply Claude's x by your viewport width over 1456, and its y by your viewport height over 819. Clamp both to the screen's edges so you never click off-screen. That's the whole trick — coordinate_scaling.py does it in twenty lines. | formula card: real_x = x × (viewport_w / 1456), real_y = y × (viewport_h / 819), then a clamp note |
| B04 | ANCHOR PAYOFF / both directions | Back to the anchor: 2560 over 1456 is about 1.76, and so is 1440 over 819 — because both are 16:9. Multiply 728 and 409 by that ratio and you land at 1280, 720, dead center of the real screen. But that single ratio only works because the viewport is 16:9 like the screenshot. A different aspect ratio needs a different lookup table, not this one multiply. | THE ANCHOR RETURNS — same two rectangles; the scaled dot now lands on the target at (1280,720) with a check; a mismatched-aspect rectangle beside it is struck through, captioned "different lookup table" |
| **BCRY** | **carry-out** | Claude's coordinates live in a resized copy of your screen — multiply by the ratio back to real pixels, or the click lands nowhere near the button. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. My model clicks at seven hundred, four ten on a 1456 by 819 screenshot, but my screen is 1920 by 1080 — write the scaling and land the click exactly. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Bridging the Pixel Gap in Browser Automation. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, unbuilt scaffold) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Bridging the Pixel Gap in Browser Automation." | unchanged |
| Facts | Claude's vision encoder resizes 16:9 screenshots to 1456×819; `coordinate_scaling.py` scales by `viewport_w/1456`, `viewport_h/819`, then clamps; example: claude (728,409) on a 2560×1440 viewport → real (1280,720); exclusions: DOM navigation, CSS-selector clicking, non-16:9 aspect ratios (`match_aspect_ratio=True`, a different lookup table) | unchanged |
| Beat count | 8 (B00–B05, YOURTURN, B07) | 8 (B00–B04, BCRY, BHTF, BOUT) |
| B00 | `ClaudeComposerAsk` cold open stating the full scaling prompt as a text card | `BrutalistHesitantWriter` (WRITER LAW) — the (700,410)/1920×1080 worked example moves to BHTF as the Your Turn prompt, verbatim |
| Register | Teardown (metadata), though narration carried no actual verdict | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Your Turn prompt | "My model clicks at (700, 410) on a 1456x819 screenshot but my screen is 1920x1080 — write the scaling and land the click exactly." | same prompt, carried over verbatim |

No beat in the source was `ai-video-prompt`, pantry, or a human-drop slot —
the source's beats were already `ClaudeComposerAsk`/`FormBCard`/
`ClaudeTitleOutro` (Remotion) shapes, just unbuilt — so the NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00 (which the WRITER LAW
covers anyway). The source's B05 verdict/recap beat is dropped as a
restatement; its content (the ratio formula and "twenty lines, not magic"
line) is already carried by B03/B04. The source's B04 exclusions beat
("DOM navigation, CSS selectors, non-16:9") is folded into B04's
both-directions clause rather than kept as a separate beat, since this
reel's body runs four beats instead of the source's five.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (Claude's numbers = your screen's pixels); B02's anchor is the falsifying case (same raw pixel, wrong screen, missed button) |
| One anchor, planted early, paid off late | B02 plants the 728,409 / 2560×1440 case; B04 pays it off (scaled to 1280,720, dead center) |
| Both directions | B04 — the ratio lands the click when the viewport is 16:9 like the screenshot; a non-16:9 viewport needs a different lookup table, not this multiply |
| No design judgment | B03–B04 describe why the scaling behaves this way; nothing rules on whether coordinate scaling is the "right" way to do browser automation |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not how non-16:9 scaling works.** The source excludes the
  `match_aspect_ratio` lookup table's internals; the reel names it as an
  exclusion (B04) and never speculates on its mechanics.
- **Not DOM navigation or CSS-selector clicking.** Source exclusions,
  untouched.
- **No verdict on the design.** Explaining why the ratio multiply works is
  not the same as ruling on whether coordinate scaling is the best way to
  do browser automation — that would be Teardown's lane.

## Handoff prompt (BHTF, read aloud)

> "My model clicks at (700, 410) on a 1456x819 screenshot but my screen is
> 1920x1080 — write the scaling and land the click exactly."

Why it's worth running: it turns the reel's formula into working code
against a fresh set of numbers, and a good answer should also mention
clamping to bounds — a detail the reel names but doesn't dwell on.

---
**GATE P — signed:** ______________________  (human)
