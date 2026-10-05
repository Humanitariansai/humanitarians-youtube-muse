# ACTS.md — "AI that sees" (slug `ai-that-sees`)

Show-tell film. One drawn illustration per beat; Liam's narration carries every
idea. Persona: Liam ("Liam, in for Bear,"); Kokoro voice `am_onyx`; Teardown
register; channel `claude-liam`; watermark `@NikBearBrown`.

Companion to film 18 ("Just talk to it", voice mode): that film covered when
talking beats typing; this one covers when *showing* beats typing. An extra
film beyond the 24-film How-to-AI queue (all 24 Done) — the coordinator indexes
it.

## The argument (one paragraph)

You can show the AI things — screenshots, photos, forms — the way you'd send a
picture to a friend, and a photo often says in a second what five minutes of
typing cannot. It works like this: you attach the photo, the AI scans it, and
it answers in words. The use cases that beat typing are: the unreadable error
message (screenshot it and ask what it means), receipts (photograph and ask
for the total, date, biggest lines), a sick plant (photograph the leaves and
ask what it needs), paper forms (photograph and ask which box is which),
settling arguments of the eye (two swatches, which one goes with the room),
and handwriting (whiteboard, notebook — say "transcribe this"). Three photo
rules: take it like evidence (light on, held still, the thing big in frame);
if the photo is busy, point — crop in or name the spot; and always add a few
words, because the photo is the evidence and your words are the question.
Last: the AI reads everything you show it, so photograph the receipt, not the
bank statement.

## Acts

| Act | Beats | Job |
|---|---|---|
| the question | BIDEA | Greeting + naive question corrected ("What does multimodal mean" → "when should I show the AI a photo instead of typing") |
| terms | BDEFS | 3 terms: multimodal, vision, attach |
| show-tell | B00–B11 | The move (attach a photo), how vision works, six use cases, three photo rules, what not to share |
| your turn | BHTF | Claude composer: photograph something you'd retype, attach it, ask what it is and what to do; two self-checks |
| outro | BOUT | Spoken title + "At Nik Bear Brown" |

## Beat map

- B00 — the move itself (attach a photo to your message; hero object arrives)
- B01 — how it works: your photo travels to the AI, it scans, it answers in words
- B02 — use case: the error message (screenshot, ask what it means)
- B03 — use case: receipts (photograph, ask for total/date/biggest lines)
- B04 — use case: a sick plant (photograph the leaves, ask what it needs)
- B05 — use case: forms (photograph, ask which box is which)
- B06 — use case: settling arguments of the eye (two swatches, which one)
- B07 — use case: handwriting (whiteboard, notebook — "transcribe this")
- B08 — rule 1: take it like evidence (clear, lit, still, big in frame)
- B09 — rule 2: if the photo is busy, point (crop in or name the spot)
- B10 — rule 3: always add a few words (the photo is the evidence, your words are the question)
- B11 — what not to share (the AI reads everything you show it)

## Deliberate anti-rot choices

- The attach affordance is described as "a paperclip or plus button" and
  drag-and-drop is named once in SOURCES/FACTCHECK only — never a pixel
  position, never a version number, never a product-specific flow.
- No pricing, no model names, no availability claims in narration; the
  `modelLabel: "Opus 5.5"` in the BHTF composer chrome matches the companion
  film's house chrome (Bear's standard), not a factual claim.
- Narration hedges the mechanism: "The AI scans it the way you would — top to
  bottom" is an analogy, not a technical spec of any vision model.
- B11's privacy beat asserts no vendor data-retention policy; it teaches the
  durable rule (photograph the receipt, not the bank statement).
