# Why the Server Hands Back an Encrypted Context You're Only Going to Echo — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-basics/anthropic-sdk-php-server-hands-back-encrypted-context`).*
*Register: **Plain**. 8 beats, matching the source's beat count. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes the readable summary Claude hands back is what it remembers. It's not — it's just what's shown to you. So why does the server hand back an encrypted blob you're only going to echo?" | Writer types "The summary is what Claude remembers, right?..."; "remembers" hesitates and corrects to "shows you" |
| B01 | 1 stakes / wrong guess | When a chat gets long, compaction fires and hands you back two things: a readable summary, and an opaque encrypted blob. The natural guess is that the summary — the part you can read — is what carries the memory forward. Pass it alone into the next call, and the context breaks anyway. | a tall message stack; two outputs branch off; the readable-summary path dead-ends |
| B02 | setup — ANCHOR PLANTED | Here's the concrete case. A twenty-turn conversation overflows, and compaction fires. You get back `content`: "Earlier conversation summarized" in plain English, right next to `encrypted_content`: a sealed string starting "EpwBCioIDxgC…". Thread the readable text into the next call, and context breaks. Thread the blob back instead, and it holds. | THE ANCHOR — the stack collapsing into an open speech bubble and a sealed box; only the box's path continues |
| B03 | mechanism | Here's why. The readable text is display and debug only — it's for you, not for the model. The encrypted blob is a server-verifiable token: it reconstructs the full compressed context — turn boundaries, roles, metadata — everything the plain summary throws away. | speech bubble labelled "display only"; sealed box labelled "server-verifiable token" unpacking into turn boundaries / roles / metadata |
| B04 | ANCHOR PAYOFF / both directions | So on the next call, you pass only the blob. The server doesn't replay twenty messages — it rebuilds the full context straight from the token. Passing the blob restores everything compaction saved; it doesn't make the readable summary useless, since that text is still exactly what you'd show a user or a log. | THE ANCHOR RETURNS — 20 messages crossed out, replaced by one token feeding the next call; the speech bubble persists off to the side, labelled "still useful — for display" |
| **BCRY** | **carry-out** | The readable summary is for your eyes; the encrypted blob is what actually carries the conversation's memory forward. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. You're building a multi-turn PHP app with the Anthropic SDK. Show me how to detect a compaction block in the response, and write the code that threads the `encrypted_content` blob — not the human-readable summary — back into the next `messages` array. Explain what breaks if you send the summary text instead. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why the server hands back an encrypted context you're only going to echo. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, unbuilt scaffold) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Why the server hands back an encrypted context you're only going to echo" | unchanged |
| Facts | compaction returns a readable `content` summary AND an opaque `encrypted_content` blob; the blob is a server-verifiable token that reconstructs full compressed context (turn boundaries, roles, metadata) that plain prose throws away | unchanged |
| Beat count | 8 (B00–B05, YOURTURN, OUTRO) | 8 (B00–B04, BCRY, BHTF, BOUT) |
| B00 | `FormBCard` cold open stating the concrete `compaction`/`encrypted_content` case as a text card | `BrutalistHesitantWriter` (WRITER LAW) — the concrete case moves to B02 as the planted anchor |
| Register | Teardown (metadata), though narration carried no actual verdict | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Your Turn prompt | "You're building a multi-turn PHP app with the Anthropic SDK. Show me how to detect a compaction block…" | same prompt, carried over verbatim (the practical takeaway doesn't change with register) |

No beat in the source was `ai-video-prompt`, pantry, or a human-drop slot — the
source's beats were already `FormBCard`/`ClaudeComposerAsk`/`ClaudeTitleOutro`
(Remotion) shapes, just unbuilt — so the NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00 (which the WRITER LAW covers anyway). The source's
B00 cold open (the concrete `compaction` case) and B04 (the 20-turn example)
were merged into this reel's B02/B04 anchor pair, since hai-simple's spine
puts the concrete case after the stakes/wrong-guess beat rather than as the
very first thing on screen.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (summary = memory); B02's anchor is the falsifying case (thread the summary back, context breaks) |
| One anchor, planted early, paid off late | B02 plants the twenty-turn compaction case; B04 pays it off (blob alone rebuilds full context, no replay) |
| Both directions | B04 — passing the blob restores context; NOT passing it doesn't mean the summary is worthless, since it's still the right thing to show a user or a log |
| No design judgment | B03–B04 describe why the split behaves this way; nothing rules on whether this is the "right" way to handle overflow |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not how the token is encrypted.** The source excludes the encryption
  algorithm; the reel says "server-verifiable token" and never speculates on
  the scheme.
- **Not when or how to trigger compaction manually.** The source excludes
  compaction thresholds and manual-compaction APIs; the reel treats
  compaction firing as a given, not something to configure on screen.
- **No verdict on the design.** Explaining why the split exists is not the
  same as ruling on whether it's the best way to solve context overflow —
  that would be Teardown's lane.

## Handoff prompt (BHTF, read aloud)

> "You're building a multi-turn PHP app with the Anthropic SDK. Show me how
> to detect a compaction block in the response, and write the code that
> threads the `encrypted_content` blob — not the human-readable summary —
> back into the next `messages` array. Explain what breaks if you send the
> summary text instead."

Why it's worth running: it turns the reel's claim into working code against
the viewer's own PHP integration, not just the reel's description of it.

---
**GATE P — signed:** ______________________  (human)
