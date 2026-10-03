# Why Web Search Never Runs Your Code but Your Own Tool Always Does — Narration Script (GATE P)

*Skill: `hai-simple` (redo of
`claude-basics/claudeforfoundationmodels-web-search-never-runs-code`).*
*Register: **Plain**. 8 beats, matching the source's beat count. Carry-out
written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a tool call always comes back through their own code. Wrong guess — sometimes it does, sometimes it doesn't. Why web search never runs your code, but your own tool always does." | Writer types "A tool call should always round-trip through my code — so why didn't web search?"; "always" hesitates and corrects to "sometimes" |
| B01 | 1 stakes / 2 wrong guess | Declaring a tool feels uniform — you list it, Claude can call it, so every call should behave the same way afterward. The natural guess: the model emits a call, your code runs it, you send the result back. That's true for your own tools. It is not true for web search. | A single "declare a tool" card branching into two identical-looking call shapes; one keeps its "emit → run → send back" loop, the other's loop breaks open |
| B02 | setup — ANCHOR PLANTED | Here's the concrete case. `.webSearch(maxUses: 5)` sits in `serverTools`; a Swift function called `lookupFavorites()` sits in `tools` — same file, same declaration style. Web search runs on Anthropic's servers and its results land inside that same turn. `lookupFavorites` triggers a tool-use block that only your own app can act on. | THE ANCHOR — two declaration cards side by side, `serverTools`/`.webSearch` and `tools`/`lookupFavorites()`; one path closes on itself, the other exits to a labelled "your app" box |
| B03 | 3 mechanism | Round-trip count comes down to who can execute. Web search needs a live index and a sandbox — infrastructure Anthropic already runs, so it finishes the call itself, in that same turn. `lookupFavorites()` is arbitrary code on your device — only your app can run it, which forces the model to stop and wait for a second request. | Two lanes: ANTHROPIC'S SERVERS (index + sandbox icons) closing its own loop; YOUR DEVICE, its arrow exiting the frame and re-entering as a second request |
| B04 | 4 ANCHOR PAYOFF / both directions | Say to Claude, "search osmosis, then check my notes." The search resolves inside that request — no callback into your code. `checkNotes()` can't: the model emits the call, your code runs it, and a second request carries the answer back. It doesn't matter how trivial your function is — even one line forces that round trip. And it doesn't matter how often web search fires — every call still resolves in-turn, because Anthropic still holds the execution. | THE ANCHOR RETURNS — the osmosis search closes its own loop; `checkNotes()` exits and re-enters; two captions: "trivial function — still round-trips" / "fires twice — still in-turn" |
| **BCRY** | **6 carry-out** | It isn't the syntax that decides the round trip — it's who can execute. Anthropic runs its own tools inside the turn; only you can run yours, so the model has to stop and come back for the answer. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. In my Claude app, I have one tool declared as a server-side tool, like web search, and one declared as a client-side tool that calls my own code. Walk me through what happens at the network level for each — how many round-trips, who executes the tool, and where the result enters the conversation — so I can reason about latency budgets in my app. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why web search never runs your code but your own tool always does — with identical syntax. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, unbuilt scaffold) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Why web search never runs your code but your own tool always does — with identical syntax" | unchanged |
| Facts | `.webSearch(maxUses: 5)`/`serverTools` vs. Swift `lookupFavorites()`/`tools`; server-side tools finish in-turn (infrastructure Anthropic runs), client-side tools force an exit-and-return (arbitrary device code only the caller can run) | unchanged |
| Beat count | 8 (B00–B05, YOURTURN, OUTRO) | 8 (B00–B04, BCRY, BHTF, BOUT) |
| B00 | `FormBCard` cold open stating the concrete `.webSearch`/`lookupFavorites` case as a text card | `BrutalistHesitantWriter` (WRITER LAW) — the concrete case moves to B02 as the planted anchor |
| Register | Teardown (metadata), though narration carried no actual verdict | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Your Turn prompt | "In the Anthropic Swift SDK I have both `.webSearch` declared in `serverTools` and a local Swift function declared in `tools`. Walk me through what happens at the network level for each…" | same idea, generalized off the Swift-specific framing to "my Claude app" since the underlying `serverTools`/`tools` split is a general SDK concept, not Swift-only |

No beat in the source was `ai-video-prompt`, pantry, or a human-drop slot —
the source's beats were already `FormBCard`/`ClaudeComposerAsk`/
`ClaudeTitleOutro` (Remotion) shapes, just unbuilt (0/8 filled) — so the
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00 (which the WRITER
LAW covers anyway). `FormBCard` is a retired/banned component (SlateCard
composition deleted 2026-08-26); this reel's body (B01–B04) uses custom
Manim scenes instead, matching the disposition already established on
sibling `claude-basics--claudeforfoundationmodels-same-api-key-shipped-prototype`.
The source's B00 (a text card stating the concrete `.webSearch`/
`lookupFavorites` case) and B04 (the osmosis/checkNotes worked example) were
kept as this reel's B02/B04 anchor pair — planted then paid off — which the
source never had (it stated the same recap sentence twice, in B03 and B05,
instead of a plant/payoff structure).

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (every call round-trips through your code); B02's concrete case is the falsifying case (web search's result lands in the same turn, no callback) |
| One anchor, planted early, paid off late | B02 plants the `.webSearch`/`lookupFavorites` declaration pair; B04 pays it off with the osmosis/checkNotes worked example |
| Both directions | B04 — it doesn't matter how trivial the client function is (still round-trips); it doesn't matter how often web search fires (still resolves in-turn) |
| No design judgment | B03–B04 describe why the split behaves this way; nothing rules on whether server-side or client-side tools are the "better" choice |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |
| One inference flag | None needed — every claim here is architectural fact (what infrastructure a server-side tool needs, what a client-side tool is), not an inference the reel has to flag |

## Deliberately not claimed

- **No claim about domain filtering, `maxUses` rate limiting, or the
  tool-result schema.** The source excludes these explicitly as follow-on
  questions.
- **No verdict on which pattern is "better."** Explaining why the round-trip
  split exists is not the same as ruling on whether you should prefer
  server-side or client-side tools — that's Teardown's lane.
- **Not the only kind of split.** The `.webSearch`/`lookupFavorites` pair is
  one concrete instance of the general rule (who can execute), not an
  exhaustive list of every tool-calling pattern.

## Handoff prompt (BHTF, read aloud)

> "In my Claude app, I have one tool declared as a server-side tool, like
> web search, and one declared as a client-side tool that calls my own
> code. Walk me through what happens at the network level for each — how
> many round-trips, who executes the tool, and where the result enters the
> conversation — so I can reason about latency budgets in my app."

Why it's worth running: it turns the reel's claim into an actual latency
accounting for the viewer's own tool mix, not just the reel's description of
one example pair.

---
**GATE P — signed:** ______________________  (human)
