# SCRIPT — Why a 50-turn agent pays for the same screenshot 35 times unless it caches the pixels

Register: Plain. Voice: Liam (Kokoro am_onyx). Mode: redo of
`anthropics/youtube/claude-basics/claude-quickstarts-50-turn-agent-pays-same`
(source register: Teardown → re-registered here as Plain: same facts, no verdict).

## B00 — Hesitant writer (the question, typed and corrected)

On screen (typed, then corrected): "Why does a 50-turn\nagent waste bandwidth\nresending the same\nscreenshot?" — "bandwidth" is typed, reconsidered, and replaced with "tokens."

Narration (Liam):
> You might think this is a bandwidth problem — sending the same image over the wire again. It isn't. It's tokens: why does a 50-turn agent pay to reprocess the same screenshot over and over?

## S01 — Stakes / anchor planted

> A 50-turn form-filling task only ever shows 5 unique desktop states. Naive math: 50 screenshots at 2,000 tokens each is 100,000 image tokens for a task with 5 actual pictures.

## S02 — The wrong guess

> The natural assumption is that the model already saw a screenshot once, so showing it again should be nearly free — it's already in the conversation.

## S03 — Breaking it

> But an API call has no memory between requests. Every turn resends the *entire* conversation so far, images included, and the model reprocesses all of it from scratch, every single time.

## S04 — The mechanism

> The fix: hash the screenshot, and mark it `cache_control: {"type": "ephemeral"}` the first time it's sent. The next turn that sends the identical hash hits the cache instead of paying to reprocess it.

## S05 — Anchor payoff

> Back to the 50-turn task: only 5 states ever get tokenized in full, 2,000 tokens each — 10,000 total. The other 45 turns are cache hits. 10,000 instead of 100,000.

## S06 — Both directions (A)

> This helps exactly when a screen repeats byte-for-byte — an idle dialog, an unchanged form. A cursor that moved, or a field mid-type, is a different image and a different hash — full price again.

## S07 — Both directions (B)

> And it doesn't help a task that's genuinely novel every turn — a real navigation to a new page is a new state, tokenized like anything else. Caching can't invent savings where the screen actually changed.

## BCRY — Carry-out

> An unchanged screenshot isn't free just because the model already saw it — every turn resends everything from scratch. Marking it cached is what makes a repeat actually free.

## BHTF — Your turn (Claude prompt, read aloud)

> Your turn. Here's the prompt — read it with me. I'm building a 50-turn computer-use agent that revisits the same 5 desktop states repeatedly. Show me exactly where to place `cache_control` on the screenshot messages so each unique state is only billed once, and write the code that detects a repeated state and routes to the cached version instead of sending the raw image again.

## BOUT — Outro (Humanitarians AI skin)

OutroSeries:
> Why a 50-turn agent pays for the same screenshot 35 times unless it caches the pixels. This is Claude Basics, from Humanitarians AI.

OutroCTA:
> Find more at humanitarians.ai. …Liam, in for Bear.

## Six-move audit

| Move | Beat | Law |
|---|---|---|
| 1 stakes first | S01 | ✓ |
| 2 wrong guess, falsified by a case | S02 (planted) → S03 (broken by: API calls are stateless) | WRONG-GUESS LAW ✓ |
| 3 mechanism | S04 | ✓ |
| 4 anchor planted + paid off | S01 → S05 (the 50-turn / 5-state task, same numbers) | ANCHOR LAW ✓ |
| 5 both directions | S06 + S07 | BOTH-DIRECTIONS LAW ✓ |
| 6 carry-out | BCRY | CARRY-OUT LAW ✓ |
| one flag | none needed — no inference beyond the source's documented API mechanism | ONE-FLAG LAW ✓ (source's `one_flag` also empty) |

## What changed from source (redo-mode delta)

- B00 replaced: was a plain GRAPHIC cold-open card restating the numbers; now `BrutalistHesitantWriter` — the newcomer's actual wrong instinct (thinking in bandwidth/network terms rather than tokens) typed and corrected on screen.
- The source had no explicit wrong-guess beat (Teardown gap-form register). S02/S03 are new content, honestly derived from the source's own mechanism (`cache_control` only makes sense if repeat sends are otherwise NOT free) — not fabricated facts.
- S06/S07 (both directions) are new — derived from the source's own `exclusions` field ("full caching protocol, cache eviction policies" are out of scope) by stating the boundary of the win (byte-identical repeats only) plainly, without touching eviction/protocol internals.
- Carry-out (`WantQuote`) is new phrasing of the source's own `purpose` field.
- Your Turn (`ClaudeComposerAsk`) keeps the source's exact paste-ready prompt verbatim; `folderLabel`/`topic` swapped to @HumanitariansAI.
- Outro swapped the source's `ClaudeTitleOutro` → `OutroSeries` + `OutroCTA` (Humanitarians AI skin per `skills/make/hai`), closing narration "…Liam, in for Bear."
