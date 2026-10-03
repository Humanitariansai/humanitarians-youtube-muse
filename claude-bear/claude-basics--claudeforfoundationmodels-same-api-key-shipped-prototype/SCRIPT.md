# Why the Same API Key That Shipped Your Prototype Becomes a Critical Bug in Production — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-basics/claudeforfoundationmodels-same-api-key-shipped-prototype`).*
*Register: **Plain**. 8 beats, matching the source's beat count. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone asks how to hide their API key better before shipping. Wrong fix — you don't hide it, you move it. Why the same key that shipped your prototype becomes a bug in production." | Writer types "How do I hide my API key better before I ship?..."; "hide" hesitates and corrects to "move" |
| B01 | 1 stakes / wrong guess | A bundled key works perfectly in development, and turns into a shipping vulnerability the moment you release the app. The instinct is to hide it harder — scramble the string, split it in pieces. None of that holds: a shipped binary can always be decompiled, string and all, however well it was scrambled. | DEV card and SHIP card holding the same key; a decompile arrow cracks the SHIP card open; a scrambled variant is still read straight through |
| B02 | setup — ANCHOR PLANTED | Here's the concrete case. In development, the app calls Claude directly: `.apiKey("sk-ant-...")`, right there in the source. Before release, that line has to change to `.proxied(headers:[...])`, and a small relay server at yourcompany.com sits in between, injecting the real key on the server side. | THE ANCHOR — DEV code card vs. RELEASE code card, with a relay box injecting the real key on the path to Claude |
| B03 | mechanism | Here's why. The threat model changed. On your own machine, the key just needs to work. On a device someone else holds, the key needs to survive them taking the binary apart — and no amount of scrambling changes that; only removing the key from the device does. | a lock that stays closed on YOUR MACHINE; the same lock pried open on SOMEONE ELSE'S DEVICE; a scramble icon struck through, changing nothing |
| B04 | ANCHOR PAYOFF / both directions | So on release, the app never holds the real key — it sends a request token, and the relay injects the actual key server-side before forwarding to Claude. That boundary isn't needed everywhere: a server you fully control, that no user ever touches, can keep using the bundled key directly. The moment a user could hold the binary, the key has to move. | THE ANCHOR RETURNS — the RELEASE path completes unbroken through the relay to Claude; a SERVER YOU CONTROL path reaches Claude directly, unbroken, no relay |
| **BCRY** | **carry-out** | A key you can decompile isn't hidden, it's just harder to read. The real fix isn't a better hiding place — it's moving the key off the device entirely. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. I'm building an app that calls the Claude API directly with a bundled key, and I need to ship it. Walk me through the backend relay pattern I need: what my app should send instead of the key, what the minimum relay server needs to do, and how it keeps the real key safe even if someone decompiles my app. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why the same API key that shipped your prototype becomes a critical bug in production. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, unbuilt scaffold) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Why the same API key that shipped your prototype becomes a critical bug in production" | unchanged |
| Facts | a bundled key works locally and is extractable from a shipped binary; production forces the key behind a backend relay (`.apiKey(...)` in source → `.proxied(headers:[...])` + relay that injects the real key server-side) | unchanged |
| Beat count | 8 (B00–B05, YOURTURN, OUTRO) | 8 (B00–B04, BCRY, BHTF, BOUT) |
| B00 | `FormBCard` cold open stating the concrete `.apiKey`/`.proxied` case as a text card | `BrutalistHesitantWriter` (WRITER LAW) — the concrete case moves to B02 as the planted anchor |
| Register | Teardown (metadata), though narration carried no actual verdict | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Your Turn prompt | "I'm shipping a Claude-powered iOS app and my API key is currently baked into the binary. Walk me through the backend relay architecture…" | same idea, tightened to a general app rather than iOS-specific, since the source's own example app in `video-ideas.md` is a generic "small weather app," not iOS-only |

No beat in the source was `ai-video-prompt`, pantry, or a human-drop slot —
the source's beats were already `FormBCard`/`ClaudeComposerAsk`/
`ClaudeTitleOutro` (Remotion) shapes, just unbuilt (0/8 filled) — so the
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00 (which the WRITER
LAW covers anyway). The source's B00 (a text card stating the concrete
`.apiKey`/`.proxied` case) and B04 (the same worked example) were merged into
this reel's B02/B04 anchor pair, since hai-simple's spine puts the concrete
case after the stakes/wrong-guess beat rather than as the very first thing
on screen — and B02→B04 gives it a planted-then-paid-off shape the source
never had (it stated the same recap sentence twice, in B03 and B05, instead).

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (hide it harder); B01's own decompile case is the falsifying case (a shipped binary is always readable, scrambled or not) |
| One anchor, planted early, paid off late | B02 plants the dev/release code swap; B04 pays it off (the release path completes to Claude through the relay) |
| Both directions | B04 — the backend boundary is needed once a user can hold the binary; it is NOT needed on a server you fully control that no user ever touches |
| No design judgment | B03–B04 describe why the split behaves this way; nothing rules on whether the relay pattern is the "best" way to solve it |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |
| One inference flag | None needed — every claim here is architectural fact (what a compiled binary exposes, what a relay does), not an inference the reel has to flag |

## Deliberately not claimed

- **No specific obfuscation technique named as broken.** The point is that
  obfuscation as a category doesn't change what's extractable from a shipped
  binary, not that one particular scrambling scheme is weak.
- **Not OAuth, token refresh, or App Attest attestation mode.** The source
  excludes these explicitly as a follow-on architecture question.
- **No verdict on the relay pattern being the "right" architecture.**
  Explaining why the boundary exists is not the same as ruling on whether
  it's the best way to solve it — that's Teardown's lane.

## Handoff prompt (BHTF, read aloud)

> "I'm building an app that calls the Claude API directly with a bundled
> key, and I need to ship it. Walk me through the backend relay pattern I
> need: what my app should send instead of the key, what the minimum relay
> server needs to do, and how it keeps the real key safe even if someone
> decompiles my app."

Why it's worth running: it turns the reel's claim into an actual relay design
against the viewer's own app, not just the reel's description of one.

---
**GATE P — signed:** ______________________  (human)
