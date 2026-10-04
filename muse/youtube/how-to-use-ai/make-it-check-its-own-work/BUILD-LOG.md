# BUILD-LOG.md — "Make It Check Its Own Work."

## Decisions

1. **Skill switch: ai-explainer → show-tell.** The assignment named
   ai-explainer but allowed switching. This film is #10 of the 24-film
   "How to AI" series, and the shipped films in
   `muse/youtube/how-to-use-ai/` use the show-tell bookend pattern
   (BIDEA hesitant writer → BDEFS terms → B00–B08 drawings → BHTF Your Turn
   → BOUT spoken outro). The film is a visual how-to technique with a
   concrete worked demo — exactly show-tell's "one drawing per beat, the
   voice explains" lane — and series consistency matters more than the
   default assignment. [judgment]
2. **Greeting: "Ciao" (Italian).** The skill rotates the world-language
   hello per reel; recent series films used "Hallo" variants, so Italian is
   fresh here. [judgment]
3. **The demo.** Needed a flaw self-critique can genuinely catch on camera.
   Chose the "which months have 28 days?" riddle: the first-pass answer
   ("February") is the classic confident-wrong answer, and the critique
   pass visibly corrects it ("all twelve"). No invented scenario, no
   staged AI output that couldn't really happen. [judgment]
4. **Second domain.** B04 (the email tone) exists so the film doesn't teach
   "this only works on quiz questions" — self-critique works on writing,
   plans, and arguments too. The redraft is written for the film and
   labeled as illustrative in SOURCES.md. [judgment]
5. **The limit beat (B06) is the film's honesty.** The task brief required
   it; FACTCHECK.md keeps the claim at "reduces errors" with no invented
   statistics. The over-correction visual (terracotta patch on a fine line)
   shows the failure mode the guides warn about: vague critique prompts
   produce churn. [judgment]
6. **B07's pro move** ("is this right?" vs "what's wrong?") extends the
   guides' warning that vague prompts underperform specific ones — framed
   as practical advice, not a lab result (FACTCHECK.md #6). [judgment]

## Timeline (2026-10-03)

- Read ai-explainer and show-tell SKILL.md; studied the shipped
  `claude-not-your-answer` package for series conventions; ran a grounding
  web search on self-critique prompting.
- Authored ACTS / SHOTLIST / FACTCHECK / make_sheet.py; generated
  beat_sheet.json (13 beats, 190.4 s) — make_sheet self-assertions passed.
- Authored scenes.py (iso_kit pasted at top + film helpers + 9 classes).
- QC: py_compile clean; static checker flagged 3 classes (B05, B06, B07)
  — all the same bug: `lab()` didn't accept `bold`. Fixed by passing
  `bold` through to `T()`; re-ran all 9 → 0 warn, 0 error.
- Verified every `until()` phrase verbatim against narration_text.
- Wrote SOURCES / BUILD-LOG / CHECKS-REPORT / PROMPTS /
  CLAUDE-CODE-RENDER / README; pushed all 12 files; verified each via
  Contents API read.

## What I don't know yet

Whether Bear wants the series to keep the show-tell bookends for all 24
films, or vary the skill per film per the standing rule — this film assumes
consistency. Whether the Kokoro voice reads "Ciao" cleanly (flagged in
CLAUDE-CODE-RENDER.md for the whisper-check).
