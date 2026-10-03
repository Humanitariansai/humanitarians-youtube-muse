# Stable Reference IDs Survive Viewport Chaos — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-basics/stable-element-refs`).*
*Register: **Plain**. 8 beats, matching the source's beat count. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a button's pixel position is a stable way to find it. It isn't — resize the window and the pixel moves, even though the button hasn't. So how do you give Claude a handle that survives the resize?" | Writer types "Pixel position is a stable way to find a button, right?"; "stable" hesitates and corrects to "fragile" |
| B01 | 1 stakes / wrong guess | Browser automation that clicks by pixel coordinate ties a command to one spot in one viewport. Resize the window, and the page reflows — the button moves, the coordinate doesn't, and the click lands somewhere else. Every single time. | a browser frame resizing; the same raw pixel plotted after the resize misses the button, marked with a cross |
| B02 | setup — ANCHOR PLANTED | Here's the concrete case. A "Confirm Order" button sits at 960, 540 on a 1920 by 1080 window. Resize down to 1440 by 900, and that same button is now at 720, 405 — the old coordinate lands on empty page. | THE ANCHOR — browser frame at 1920×1080 with the button at (960,540); resized to 1440×900, the button now at (720,405), old coordinate crossed out |
| B03 | mechanism | The fix runs before Claude ever looks at the page. A script walks every clickable element and stamps it with a stable reference id — "confirm order one" — baked into the page itself. Claude then clicks by that name, not by a pixel. | code card: element.setAttribute assigns the ref; "Claude targets: ref=confirm_order_1" |
| B04 | ANCHOR PAYOFF / both directions | Back to the button: after the resize its pixel moved to 720, 405, but its ref, confirm order one, never changed — it's attached to the element, not the spot. Claude clicks the ref and lands every time. But that only covers elements the script already saw; anything added to the page afterward needs its own pass to get a ref at all. | THE ANCHOR RETURNS — same browser frame pair; the ref label stays glued to the button through the resize, click lands; a dashed, struck-through element beside it captions "added after load — no ref yet" |
| **BCRY** | **carry-out** | A pixel coordinate describes a moment in one viewport; a stable ref describes the button itself — that's why the ref survives a resize and the coordinate doesn't. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Assign stable refs to every clickable element on this page so my automation survives a resize. See what naming scheme it picks, whether it handles iframes, whether it guards against duplicate ids. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Stable Reference IDs Survive Viewport Chaos. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, unbuilt scaffold) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Stable Reference IDs Survive Viewport Chaos." | unchanged |
| Facts | pixel automation breaks on resize (960,540 → 720,405 across a 1920×1080 → 1440×900 resize); fix is a JS-injected stable ref (`data-ref`, e.g. `ref="confirm_order_1"`) attached to each clickable element before Claude reads the page; Claude targets by ref name; exclusions — injection/CSS specificity mechanics, and dynamic elements added after page load (need a re-injection pass) | unchanged |
| Beat count | 8 (B00–B05, YOURTURN, B07) | 8 (B00–B04, BCRY, BHTF, BOUT) |
| B00 | `ClaudeComposerAsk` cold open stating the full ref-assignment prompt as a text card | `BrutalistHesitantWriter` (WRITER LAW) — the source's exact prompt moves to BHTF as the Your Turn prompt, condensed |
| Register | Teardown (metadata), though narration carried no actual verdict | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Your Turn prompt | "Assign stable refs to every clickable element on this page so my automation survives a resize." plus discussion of naming scheme / iframes / duplicate-id guarding | same prompt and discussion, carried over |

No beat in the source was `ai-video-prompt`, pantry, or a human-drop slot —
the source's beats were already `ClaudeComposerAsk`/`FormBCard`/
`ClaudeTitleOutro` (Remotion) shapes, just unbuilt — so the NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00 (which the WRITER LAW
covers anyway). The source's B05 verdict/recap beat is dropped as a
restatement; its content (pixel expires, ref survives because it's attached
to the element) is already carried by B02–B04. The source's B04 exclusions
beat (JS/CSS mechanics, dynamic post-load elements) is folded into B04's
both-directions clause rather than kept as a separate beat, since this
reel's body runs four beats instead of the source's five. The source's B03
"morph" centerpiece (viewport shrinking while the ref stays glued to the
button) is what B04 dramatizes as the anchor payoff.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (pixel position is a stable handle); B02's anchor is the falsifying case (960,540 → resize → 720,405, old coordinate now wrong) |
| One anchor, planted early, paid off late | B02 plants the Confirm Order button / 960,540 / 720,405 case; B04 pays it off (ref unchanged, click lands) |
| Both directions | B04 — the ref survives a resize of elements already on the page; an element added to the page after the ref pass needs its own re-injection, not covered by the same mechanism |
| No design judgment | B03–B04 describe why the ref persists; nothing rules on whether ref-based targeting is the "right" way to build browser automation |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not the injection mechanics.** The source excludes the JavaScript
  execution details and CSS specificity rules that affect ref injection; the
  reel names this as an exclusion (B04) and never speculates on the
  internals.
- **Not dynamic elements added after load.** Source exclusion, untouched —
  stated as a limit, not solved on screen.
- **No verdict on the design.** Explaining why the ref persists across a
  resize is not the same as ruling on whether ref-based targeting is the
  best way to do browser automation — that would be Teardown's lane.

## Handoff prompt (BHTF, read aloud)

> "Assign stable refs to every clickable element on this page so my
> automation survives a resize."

Why it's worth running: it turns the reel's mechanism into a real injection
script, and a good answer should also say something about its naming
scheme, whether it handles elements inside iframes, and whether it guards
against assigning the same ref twice — details the reel names but doesn't
resolve.

---
**GATE P — signed:** ______________________  (human)
