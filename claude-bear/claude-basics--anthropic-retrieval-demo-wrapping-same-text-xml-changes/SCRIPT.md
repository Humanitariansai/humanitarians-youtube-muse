# Why Wrapping the Same Text in XML Changes the Answer Claude Gives — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-basics/anthropic-retrieval-demo-wrapping-same-text-xml-changes`).*
*Register: **Plain**. 8 beats, matching the source's beat count. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes XML tags are just decoration. They're not — they're a constraint the model was trained to expect. So why does wrapping the same text in XML change the answer Claude gives?" | Writer types "XML tags are just decoration, right?..."; "decoration" hesitates and corrects to "a constraint" |
| B01 | 1 stakes / the puzzle | The words are identical. So the answer should be too. But formatting alone shifts the quality of what comes back — and that's strange, because nothing about the content changed. | one content block branching into two differently-shaped outputs, a question mark between them |
| B02 | setup — the concrete case | Take one product description. Paste it in as plain text, and Claude's summary is generic. Wrap the exact same words in XML tags, and the summary gets sharp — it pulls the right details out. Same content. Different result. | plain-text block → generic summary; XML-tagged block → sharp summary, side by side |
| B03 | mechanism | Here's why. Claude was trained on huge amounts of consistently tagged, structured text — documents where title, content, and category always sat inside predictable markup. That built a strong expectation for those shapes. Text that matches the shape it learned gets processed more coherently. Text that doesn't, gets processed less well. | before/after pane: plain block on the left, tagged block on the right, a training-distribution curve behind both; terracotta marks the match point |
| B04 | anchor example | Look at the difference directly. Plain text: Product Name, Robot Building Kit, two hundred pieces. Tagged: title, content, and category, each wrapped in its own field. Same words. But the tagged version tells Claude exactly where the title ends and the description begins — because that's the shape it was trained to expect. | two code-style blocks side by side: plain sentence vs. `<item><title>…</title><content>…</content><category>…</category></item>` |
| **BCRY** | **carry-out** | Wrapping text in XML isn't a trick — it's speaking the shape Claude was trained to expect. Same words, matched structure, a sharper answer. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Open a Claude conversation. Paste in any short paragraph of product or document text, once as plain text, and ask for a summary. Then paste the identical text again, wrapped in XML tags — title, content, category, whatever fields fit — and ask for the same summary. Compare the two answers. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why wrapping the same text in XML changes the answer Claude gives. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, unbuilt scaffold) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Why wrapping the same text in XML changes the answer Claude gives" | unchanged |
| Facts | training on consistently formatted data builds statistical expectations; tagged inputs match the distribution better | unchanged |
| Beat count | 8 (B00–B05, YOURTURN, OUTRO) | 8 (B00–B04, BCRY, BHTF, BOUT) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card) | `BrutalistHesitantWriter` (WRITER LAW) |
| Register | Teardown (metadata), though narration carried no actual verdict | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| B04 skin | source specified a `ClaudeWindow` "code" view/`CodeViewer` skin that doesn't exist in the current component schema (scaffold was never rendered) | rebuilt as a GRAPHIC (Manim) side-by-side, same content (Robot Building Kit example) |

No beat in the source was `ai-video-prompt`, pantry, or a human-drop slot — the
source itself was already all-Remotion/Manim-shaped, just unbuilt — so the
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00 (which the WRITER
LAW covers anyway).

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01–B02; mechanism waits until B03 |
| Wrong guess surfaced | B00 (decoration → constraint) and B01 ("the answer should be too") |
| One anchor | B02 plants the plain-vs-XML product description; B04 pays it off with a second, more granular concrete case (Robot Building Kit) |
| No design judgment | B03–B04 describe why the model behaves this way; nothing rules on whether XML tagging is the "best" prompting technique |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not "XML is the only structure that works."** The source's own exclusions
  rule out schema specifics; the reel says "consistently tagged" and
  "predictable markup," never claims XML is uniquely required.
- **Not a tokenization or attention-internals claim.** The source explicitly
  excludes tokenization/attention internals; the reel stays at the level of
  training-distribution expectation.
- **No verdict on whether to always tag prompts.** That would be a
  Teardown-register judgment; Plain explains the mechanism and stops.

## Handoff prompt (BHTF, read aloud)

> "Open a Claude conversation. Paste in any short paragraph of product or
> document text, once as plain text, and ask for a summary. Then paste the
> identical text again, wrapped in XML tags — title, content, category,
> whatever fields fit — and ask for the same summary. Compare the two
> answers."

Why it's worth running: it's the reel's own claim, testable in under two
minutes, on the viewer's own text rather than the reel's example.

---
**GATE P — signed:** ______________________  (human)
