# Caching Pixels You've Already Seen — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-basics/screenshot-prompt-caching`).*
*Register: **Plain**. 8 beats. Source had all 8 primary beats fully narrated
under `simple`'s old `ClaudeComposerAsk`/`FormBCard` shape (register:
Teardown), plus 3 unfilled BOOKEND slates (BVDT/BHTF/BOUT) carrying only
placeholder text, never reconciled with the earlier beats. Carry-out written
first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes an identical screenshot costs nothing extra to resend. It doesn't work that way — every repeat gets billed again, unless you tell the API to remember it. So what actually stops the re-billing?" | Writer types "It's the same screenshot, so sending it again is free, right?"; "free" hesitates and corrects to "billed" |
| B01 | 1 stakes / wrong guess | A fifty-turn computer-use task takes a screenshot on every turn. Thirty-five of those turns, the desktop hasn't changed at all — the exact same image goes out again. The natural assumption is that repeating an image costs nothing extra, since the model has already seen it. It doesn't work that way: the API re-tokenizes every screenshot from scratch, identical or not. At two thousand tokens each, that's seventy thousand tokens spent re-reading pictures Claude has already read. | the naive loop: 50 turn-slots in a row, 35 marked as duplicates, a token counter climbing beside them toward seventy thousand |
| B02 | setup — ANCHOR PLANTED | Here's the concrete case. A fifty-turn task, but only five different things the screen actually looks like — call them A through E. Without caching, every one of those fifty screenshots is billed at full price: fifty times two thousand tokens is one hundred thousand tokens, for a screen that only changed five times. | THE ANCHOR — a filmstrip of 50 frames, five states A-E repeating, every frame billed the same, a counter climbing to "100,000 tokens" |
| B03 | 3 mechanism | The fix is one field: cache underscore control, type ephemeral. Attach it to a screenshot the first time you send it, and the API caches that exact image. Send the identical screenshot again with the same flag, and it's a cache hit — the API recognizes it and skips re-tokenizing, for next to nothing. You still send the picture; you just stop paying full price for the ones it's already seen. | the JSON field appearing on an image block; a "first sighting" screenshot flagged, a repeat of it landing as a green "HIT" |
| B04 | 4 ANCHOR PAYOFF — both directions | Back to that fifty-turn task: five unique states, cached, means five misses and forty-five hits — five times two thousand is ten thousand tokens, not one hundred thousand. Ninety percent saved. But this is the screenshot case only. It doesn't cover the full caching protocol — minimum cacheable size, eviction rules — and the cache doesn't survive forever: switch API keys, or leave it idle too long, and the next screenshot is a miss again, cache or no cache. | THE ANCHOR RETURNS — the same 50-frame filmstrip, now 5 miss-frames in terracotta and 45 hit-frames in teal, counter dropping to "10,000 tokens"; beside it, a struck card: "not the full protocol · not permanent" |
| **BCRY** | **6 carry-out** | A repeated screenshot doesn't get cheaper on its own — you have to flag it as one you've already shown, and the discount lasts only until the picture actually changes. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. "My computer-use agent re-sends an identical screenshot up to thirty-five times in a fifty-turn task — add ephemeral prompt caching and show me the token savings, before and after." Ask Claude to write the caching wrapper, then check: does it handle a screenshot that changed only slightly, not identically? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Caching Pixels You've Already Seen. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown metadata) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Caching Pixels You've Already Seen." | unchanged |
| Facts | 50-turn task, 35 identical repeats; ~2,000 tokens/screenshot; `cache_control: {"type":"ephemeral"}`; concrete case 5 unique states A-E → 10,000 tokens cached vs. 100,000 uncached, 90% savings; exclusions (full protocol, minimum thresholds, eviction, session-only persistence, ephemeral not persistent tier) | unchanged |
| Beat count | 8 primary beats fully filled (B00 cold open, B01-B04 body, B05 verdict, YOURTURN, B07 outro) under `ClaudeComposerAsk`/`FormBCard`; 3 more (BVDT/BHTF/BOUT) drafted as bookend slates but never filled | 8 (B00 writer + 4 body + BCRY + BHTF + BOUT) — source's B05 (verdict recap) and YOURTURN content split/carried into a dedicated BCRY and BHTF per hai-simple structure; the abandoned bookend slates are not carried forward (their content duplicates B05/YOURTURN) |
| B00 | `ClaudeComposerAsk` cold open stating the token-savings numbers directly, no wrong-guess framing | `BrutalistHesitantWriter` (WRITER LAW) — reframed to state the wrong guess the body falsifies (resending an identical image is free vs. billed) |
| Register | Teardown (metadata `register: "Teardown"`), though the narration itself carried no verdict beyond stating the mechanism | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Handoff prompt | YOURTURN's screenshot-caching-wrapper prompt | same prompt, carried to BHTF near-verbatim |

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — every
filled beat was already `ClaudeComposerAsk`/`FormBCard`/`ClaudeTitleOutro`
(Remotion) shapes, just built under the wrong register and skin — so the
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00 (covered by WRITER
LAW anyway).

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced, falsified by a case | B00/B01 state the guess (repeats are free); B02's anchor is the falsifying case (50 billed screenshots for a screen that changed 5 times) |
| One anchor, planted early, paid off late | B02 plants the 100,000-token uncached bill (5 states, 50 turns); B04 pays it off (10,000 tokens, 90% saved) |
| Both directions | B04 — caching this screenshot case doesn't cover the full protocol (a savings result here doesn't prove the general protocol is covered); the cache not surviving forever means a miss on a later turn doesn't prove the picture changed |
| No design judgment | B03-B04 describe why the flag works; nothing rules on whether computer-use is the right tool for a task |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not a savings guarantee.** The 90% figure is this reel's worked case (5
  unique states out of 50 turns), not a promise for every deployment.
- **Not the full caching protocol.** Minimum cacheable token thresholds and
  eviction policy are explicitly out of scope (B04's both-directions clause).
- **Not permanent.** The cache holds for a session; an API-key switch or a
  long idle gap empties it regardless of whether the screenshot changed.

## Handoff prompt (BHTF, read aloud)

> "My computer-use agent re-sends an identical screenshot up to thirty-five
> times in a fifty-turn task — add ephemeral prompt caching and show me the
> token savings, before and after."

Why it's worth running: it turns the reel's one-field fix into working code,
and a good answer should surface the harder case the reel flags but doesn't
solve — a screenshot that changed only slightly, not identically, which a
naive cache check will still call a miss.

---
**GATE P — signed:** ______________________  (human)
