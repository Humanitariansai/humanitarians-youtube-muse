# BUILD-LOG.md — "The Second Opinion"

## Decisions

1. **Skill switch: ai-explainer → show-tell.** The assignment named
   ai-explainer but allowed switching. This film joins the "How to AI"
   series, whose shipped films (including its direct companion,
   `make-it-check-its-own-work`) use the show-tell bookend pattern (BIDEA
   hesitant writer → BDEFS terms → B00–B08 drawings → BHTF Your Turn →
   BOUT spoken outro). The film is a visual how-to technique with a worked
   demo — exactly show-tell's "one drawing per beat, the voice explains"
   lane — and series consistency matters more than the default assignment.
   [judgment]
2. **Greeting: "Merhaba" (Turkish).** The skill rotates the world-language
   hello per reel; recent series films are saturated with "Hallo" variants
   and the companion film used "Ciao" — Turkish is fresh here. [judgment]
3. **The demo.** Needed a decision where a second opinion genuinely changes
   what the viewer sees. Chose the night-shift job: the first answer ("take
   it — the pay is real") is reasonable, not wrong, so the steelman doesn't
   "correct" it — it completes it (sleep, health, the drive home). That
   models the real use case better than a riddle with one right answer, and
   it differentiates the film from its companion (which used the
   February riddle). The scenario is staged and labeled illustrative in
   SOURCES.md. [judgment]
4. **Steel-manning is shown, not just named.** BDEFS defines it in one line;
   B03 performs it: the steelman card grows a terracotta rim and the three
   cost pills pop one per spoken cost — the strongest version of the other
   side, not a straw version. [judgment]
5. **The limit beat (B06) carries two honesties.** Shared blind spots
   (same training, same gaps) and opinion-shopping (asking around until an
   AI tells you what you wanted to hear — "that's a cheerleader"). The
   shopping-row visual ends with the glowing card taking the X, one
   terracotta moment at a time. [judgment]
6. **The medical guardrail.** B05 lists "a medical question" among
   high-stakes decisions but explicitly says to take it to a real doctor —
   a deliberate channel guardrail, recorded as judgment in FACTCHECK.md.
   [judgment]
7. **No statistics, by rule.** The multi-agent debate paper (Du et al.,
   arXiv:2305.14325) is the research cousin of this film's move, but its
   measured gains are deliberately not quoted — they date fast, and the
   audience needs the habit, not the numbers. FACTCHECK.md #7 confirms by
   inspection that no percentage appears anywhere. [judgment]

## Timeline (2026-10-04)

- Read ai-explainer and show-tell SKILL.md; studied the companion
  `make-it-check-its-own-work` package for series conventions; ran grounding
  web searches on steel-manning (Reason/Volokh, Discourse, Dennett/Big
  Think), devil's advocate (Wikipedia, Britannica), and multi-agent debate
  (arXiv:2305.14325).
- Authored ACTS / SHOTLIST / FACTCHECK / SOURCES / make_sheet.py; generated
  beat_sheet.json (13 beats, 238.4 s) — make_sheet self-assertions passed
  after one fix (BDEFS durationSeconds 22.0 → 21.2 to match the 53-word
  narration).
- Authored scenes.py (iso_kit pasted at top + film helpers + 9 classes).
- QC: py_compile clean; static checker flagged B07_ProMove
  (`NameError: flag` — the helper wasn't carried over from my draft);
  added it, re-ran all 9 → 0 warn, 0 error. The verbatim-until check caught
  one case mismatch ("Steelman the opposite case" vs narration's lowercase
  "steelman") — fixed.
- Wrote BUILD-LOG / CHECKS-REPORT / PROMPTS / CLAUDE-CODE-RENDER / README;
  pushed all 12 files; verified each via Contents API read.

## What I don't know yet

Whether the Kokoro voice reads "Merhaba" cleanly (flagged in
CLAUDE-CODE-RENDER.md for the whisper-check). Whether Bear wants the
night-shift demo kept qualitative or sharpened with a concrete dollar
example at the review cut.
