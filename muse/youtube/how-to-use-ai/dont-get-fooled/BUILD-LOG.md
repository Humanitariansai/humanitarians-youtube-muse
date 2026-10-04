# BUILD-LOG.md — Don't get fooled.

2026-10-03 — film #7 of 24 ("How to AI" backlog, muse/QUEUE.md). Skill:
ai-explainer (kept, not switched — the film is a Claude-branded concept
walkthrough, exactly the ai-explainer lane: mechanism → judgment → working
practice, with the Claude composer as bookend cast object).

## Steps

1. Read `~/workspace/brutalist.art/skills/make/ai-explainer/SKILL.md` in
   full (bookends, register, greeting lexicon, illustration/show-don't-tell
   laws, handoff/outro laws).
2. Fetched the refactor source via the Contents API (custom.github
   surrogate): `claude/claude-for-education/prompt-avoiding-hallucinations/`.
   **Found a mislabeled beat sheet**: the base folder's beat_sheet.json
   (and its README.md) are a copy of Lesson 07 "Few-Shot Prompting"
   metadata and narration — wrong lesson for the folder name. The folder's
   PEDAGOGY.md ("VERDICT: PASS", goal = hallucination-as-structural +
   three-element grounding + citations) and the youtube md ("Grounding:
   The Fix for Hallucinations") are the true Lesson-08 content. Listed the
   parent and found the true source:
   `claude-liam-prompt-tutorial-lesson-08-avoiding-hallucinations/`
   (10 beats, Lesson 08, Avoiding Hallucinations). Used its beat sheet,
   PEDAGOGY-adjacent verdict, and description.txt as the argument source.
   Nothing from the mislabeled sheet was used. Also pulled the true
   source's scenes.py for visual ideas (confidence/correctness bars,
   three-part grounding cards, citation flow).
3. Verified the Mata v. Avianca case via one web search (Reuters
   2023-06-22 + corroborating coverage): 2023, S.D.N.Y., Schwartz,
   six fictitious cases, Judge Castel, $5,000 sanctions. All film claims
   trace to the search results.
4. Authored make_sheet.py (13 beats, 8 body, asserts: beat count band
   13–22, body 45–70 words, B01 BLUF 20–35 words + lead_silence_s 0.8,
   IN-FOR-BEAR naming, handoff reads the prompt aloud, recap keywords,
   total 180–360 s). Generated beat_sheet.json: 13 beats, 311 s
   (~5m11s).
5. Authored scenes.py: 13 Manim classes M01–M13, one per beat, with the
   sibling films' QC-safe conventions (BOLD/NORMAL shim, bug() watermark,
   new non-text shape per play, safe-area coords, no .animate() before
   FadeIn/Create).
6. QC gate: `python3 -m py_compile` clean on make_sheet.py and scenes.py;
   `static_scene_check.py scenes.py --class <Class>` for all 13 classes.
   (Results recorded in CHECKS-REPORT.md.)
7. Wrote the doc files: ACTS, SHOTLIST, FACTCHECK, SOURCES, PROMPTS,
   BUILD-LOG, CHECKS-REPORT, CLAUDE-CODE-RENDER, README.
8. Pushed all 12 files to
   `muse/youtube/how-to-use-ai/dont-get-fooled/` on
   Humanitariansai/humanitarians-youtube-muse via gh-put-file.py; verified
   each with a Contents API read afterwards.
9. `manim_layout_audit.py --curve-strict` could not run in this VM (no
   Manim/pangocairo installed); deferred to Bear's Mac render pass per
   the task spec and noted in CLAUDE-CODE-RENDER.md.

## Decisions

- Skill kept as ai-explainer (assigned): concept walkthrough lane; the
  spine (composer cold open → hesitant-writer BLUF ≥ 9 s → body → verdict
  → handoff → title-restate outro) fits the lesson's argument shape.
- The source lesson's "hallucination rate drops to near zero" is carried
  as the lesson's conclusion and hedged in the film ("the guessing mostly
  stops"); no statistics are invented (FACTCHECK.md).
- B04's court-case beat uses only reported facts; the second and third
  citation rows are labeled "invented" rather than inventing more fake
  case names.
- Greeting "Olá" (Portuguese) chosen from the world-language lexicon to
  rotate past the sibling film's "Hallo".
