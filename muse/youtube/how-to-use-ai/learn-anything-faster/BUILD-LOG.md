# BUILD-LOG.md — Learn Anything Faster

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 21:45 — Received subagent handoff: build "Learn anything faster"
  (film #13 of 24, how-to-ai lane, slug `learn-anything-faster`) as a
  pre-render package at
  `muse/youtube/how-to-use-ai/learn-anything-faster/`; source NEW
  (build from scratch); assigned skill show-tell; never render or
  publish.
- 21:50 — Read `skills/make/show-tell/SKILL.md` end to end (drawing
  laws, card test, bookend spine, the GATE A/T/V traps) and the
  `show-tell` reference `example-make_sheet.py` plus `templates/iso_kit.py`.
  **Skill decision: show-tell (keep the assignment).** The film is a
  technique explainer — three concrete moves demonstrated on one topic —
  which maps exactly onto show-tell's spine (hesitant writer → key
  terms → drawn body beats → Your Turn composer → spoken outro). No
  interface, number set, or single word in any body beat passes the card
  test, so the film uses zero cards. [judgment]
- 21:55 — Studied the sibling package
  `~/workspace/film-builds/how-to-use-ai/claude-your-quizmaster/` end
  to end (12-file convention, narration style, FACTCHECK table format,
  BUILD-LOG/CHECKS-REPORT conventions). This film copies that 12-file
  package convention exactly.
- 22:00 — Fact-check research (web, primary sources where reachable):
  CFPB mortgage key-terms glossary (mortgage = agreement to borrow to
  buy/refinance a home); CFPB + Federal Reserve glossaries (interest
  rate = the cost/price of borrowing); extra-principal mechanics
  (interest charged on the remaining balance; extra payments cut future
  interest and can shorten the loan by years — thenest.com,
  moneysense.ca); Socratic questioning named after Socrates
  (Wikipedia, eNotes). Deliberately quoted NO dollar figures, rates, or
  year counts in the film — the extra-payment point stays qualitative
  ("a little extra each month", "where does the money go first")
  because exact savings depend on the loan. No retention statistics
  anywhere: the film promises no percentages.
- 22:10 — Chose the demo topic: how mortgages work — universally
  recognized, widely signed without being understood; the ideal "smart
  but new" subject. The mortgage is the demo only: no rates, no
  lenders, no advice. [judgment]
- 22:15 — Wrote ACTS.md (hook + 5-beat show-tell body + closing),
  SHOTLIST.md (with the "why zero cards" card-test note), FACTCHECK.md
  (7-row claim table + judgments + cut/disclosed), SOURCES.md (verbatim
  URLs), PROMPTS.md ("no generation prompts" + the viewer's tutor
  prompt).
- 22:25 — Wrote make_sheet.py in the canonical show-tell format
  (`narration_text` / `estimated_duration_s`, `remotion()` bookends,
  `bookend_exempt: ["cold-open", "bvdt"]`, per-beat sparse waivers).
  Narration: Liam ("Hallo. This is Liam, in for Bear."), Teardown
  register, every term defined in-line, Kokoro-safe (no acronyms, no
  version numbers, no numerals; "Hallo" greeting). First run:
  beats=9 body=5 total=200s (~3m20s) — inside the 170–240 s band;
  assertions pass (9 beats, 5 manim beats, class names match beat ids,
  BHTF reads the prompt in full, B04 says the moves transfer).
- 22:35 — Wrote scenes.py: pasted `templates/iso_kit.py` verbatim at
  the top, then 5 scene classes (B00_House, B01_ExplainSimple,
  B02_QuizMode, B03_Socratic, B04_YourTopic). Cast kept whole film:
  the kraft house, the tutor card, the learner ("you"), question pills,
  checks. Midpoint-guard timing: every play lands before mid−0.3 s or
  starts after mid+0.3 s, paced by `until()` on verbatim narration
  phrases (all 14 verified present in `narration_text`).
- 22:40 — Gate: `python3 -m py_compile` clean on both files;
  `static_scene_check.py` per class: **5 clean · 0 warn · 0 error on
  the first full run.** No fixes were needed at the gate.
- Next: write CHECKS-REPORT.md, CLAUDE-CODE-RENDER.md, README.md; push
  all 12 files via gh-put-file.py; verify each via Contents API;
  return the FRICTIONAL.md entry text in the final report.
