# Computer Use: Demo to Production — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-basics/computer-use-best-practices`).*
*Register: **Plain**. 8 beats. Source had 7 filled beats (B00–B06); its
handoff beat (B05) bundled a carry-out sentence and a Your Turn prompt
together, which this reel splits into a dedicated BCRY + BHTF per hai-simple's
CARRY-OUT LAW and Your Turn block. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a working computer-use demo is production-ready if you just let it run longer. It isn't — the real fix is leaner. So what actually changes between a demo and a system you can trust?" | Writer types "Going to production just means running the demo longer, right?"; "longer" hesitates and corrects to "leaner" |
| B01 | 1 stakes / wrong guess | The naive computer-use loop: take a screenshot, send the full image to Claude, get an action, repeat. Screenshots are not free — a full-resolution screenshot costs around twelve hundred tokens. The natural assumption is that a working demo just runs longer once it's in production. It doesn't scale for free: a ten-step loop already spends twelve thousand tokens on screenshots before Claude does anything. | the loop diagram (screenshot → Claude → action → repeat) with a token counter climbing beside it |
| B02 | setup — ANCHOR PLANTED | Here's the concrete case. A twenty-step task, no changes made, burns something like forty thousand tokens on screenshots alone — before a single action token is spent. That's the demo's real bill, and it only gets worse as the task gets longer. | THE ANCHOR — a bar building to "~40,000 screenshot tokens" against a 20-step task, "$0 action tokens yet" beside it |
| B03 | 3 mechanism | The production version makes seven changes to that loop. Resize every screenshot to about fifteen sixty-eight pixels wide — the size Claude's vision already works best at. Drop screenshots older than the last few steps. Batch tool calls. Cache the system prompt. Compact the history server-side. Run actions in a sandbox. And record every action as a structured trajectory event. | seven items listing down a card, six bracketed "shrinks the bill," the seventh set apart |
| B04 | 4 ANCHOR PAYOFF — both directions | Back to that twenty-step task: resize and prune alone cut the screenshot bill seventy to eighty percent, because the savings compound rather than add. But the seventh change, recording, isn't about cost — a logged run proves what the agent did, not that it did the right thing, and a run with no log doesn't mean nothing went wrong. It means you can't tell. | THE ANCHOR RETURNS — the same bar, now cut down 70-80%, target "$40,000 -> ~$10,000"; beside it, two log cards: one checked "proves WHAT happened," one struck "not WHETHER it was right" |
| **BCRY** | **6 carry-out** | Production isn't the demo running longer — it's every screenshot made leaner and every action logged, so the cost holds up and so does the record. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Design a trajectory logging schema for a computer-use agent: action type, target element, screenshot hash before and after, confidence score, and whether human confirmation was requested. Then ask: what else does the log need to make oversight meaningful, not just nominal? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Computer Use: Demo to Production. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown metadata, GATE T failed) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Computer Use: Demo to Production." | unchanged |
| Facts | naive loop (screenshot/send/action/repeat); ~1,200 tokens/screenshot; 20-step task ~40,000 screenshot tokens unoptimized; seven production changes (resize to ~1568px, prune, batch, cache, compact, sandbox, record); resize+prune cuts the bill ~70–80%; trajectory recording logs every click/keypress/screenshot with timestamp, tool, args, result, and is replayable | unchanged |
| Beat count | 7 filled (B00 cold open, B01–B04 body, B05 handoff, B06 outro); 3 more (BVDT/BHTF/BOUT) drafted as bookend slates but never filled or reconciled | 8 (B00 writer + 4 body + BCRY + BHTF + BOUT) — B05's bundled carry-out/prompt content split into a dedicated BCRY and BHTF per hai-simple structure; the abandoned bookend slates are not carried forward (their content duplicates B05/B06) |
| B00 | `ClaudeComposerAsk` cold open reciting a three-part stress-test request (modal handling, verification steps, guardrails) that the body never actually answers | `BrutalistHesitantWriter` (WRITER LAW) — reframed to state the wrong guess the body *does* answer (run it longer vs. make it leaner); the source's mismatched stress-test framing is dropped, not carried, since nothing downstream answers it |
| Register | Teardown (metadata `style_preset: teardown`), though the narration itself carried no verdict | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Handoff prompt | B05's trajectory-logging-schema prompt | same prompt, carried to BHTF verbatim |

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — B00–B06
were already `ClaudeComposerAsk`/`FormBCard`/`ClaudeTitleOutro` (Remotion)
shapes, just built under the wrong register and skin — so the NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00 (covered by WRITER LAW
anyway). B00's original narration asked about a "gap between a scripted
screenshot loop and a real workflow" and requested modal-handling tests,
verification steps, and guardrails — none of which B01–B06 ever address (they
answer screenshot cost and trajectory logging instead). Carrying that mismatch
forward would open on a question the reel doesn't answer, so B00 is
reauthored to state the wrong guess the body actually falsifies, per WRITER
LAW's requirement that the correction match "the reel's actual
misconception." The three-item stress-test request itself is not otherwise
used or discarded as a *fact* — it never was one; it was an unanswered
framing device.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (production = run the demo longer); B02's anchor is the falsifying case (a 20-step task burns ~40,000 screenshot tokens before any action) |
| One anchor, planted early, paid off late | B02 plants the ~40,000-token bill; B04 pays it off (cut 70-80%) |
| Both directions | B04 — a logged run proves what the agent did (not that it was right); an unlogged run's absence of evidence isn't evidence of a clean run |
| No design judgment | B03–B04 describe why the seven changes work; nothing rules on whether computer-use is the right tool for a task |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not a cost guarantee.** The 70–80% figure is the source's reported range
  for resize + prune on one kind of task, not a promise for every deployment.
- **Not that logging prevents mistakes.** B04's both-directions clause is
  explicit: a trajectory log proves what happened, not that it was correct.
- **No verdict on computer-use as an approach.** Explaining why the seven
  changes work is not a ruling on whether computer-use is the right way to
  automate a given task — that's Teardown's lane.

## Handoff prompt (BHTF, read aloud)

> "Design a trajectory logging schema for a computer-use agent: action type,
> target element, screenshot hash before and after, confidence score, and
> whether human confirmation was requested. What else does the log need to
> make oversight meaningful — not just nominal?"

Why it's worth running: it turns the reel's "log everything" line into an
actual schema, and a good answer should surface what nominal-but-not-meaningful
oversight looks like — a log nobody reads is not the same as a log someone
can act on.

---
**GATE P — signed:** ______________________  (human)
