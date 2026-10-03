# BUILD-LOG.md — Claude, Your Quizmaster

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 17:21 — Received subagent handoff: build "Claude, Your Quizmaster"
  (source `hai-your-quizmaster` in the mirror repo) as a pre-render
  package at `muse/youtube/how-to-use-ai/claude-your-quizmaster/`;
  skill show-tell or cc-explainer; rewrite for the general audience;
  fact-check everything; never render or publish.
- 17:25 — Fetched the source `beat_sheet.json` via the Contents API
  (11 beats, thesis: "The best use of an answer machine is making it ask
  the questions."). The first two readbacks of the file disagreed (one
  dump showed beats from a different film); re-fetched deterministically
  and confirmed the quizmaster content by sha before proceeding.
  Lesson: when two tool reads of the same file disagree, re-fetch and
  verify by sha — do not build from the ambiguous copy.
- 17:30 — Read `skills/make/show-tell/SKILL.md` and
  `skills/make/cc-explainer/SKILL.md` end to end. **Skill decision:
  show-tell.** The film is a technique explainer about the chat product;
  cc-explainer is a terminal-session genre (REAL-SESSION LAW, CCSession
  body, Boondoggle/HUMAN closing block) and fits nothing in this film.
  show-tell's spine (hesitant writer → key terms → drawn body → Your Turn
  composer → spoken outro) maps onto the source structure beat for beat.
  [judgment]
- 17:35 — Read the sibling package
  `~/workspace/film-builds/register-muse-privacy-card/` end to end
  (make_sheet.py, scenes.py, FACTCHECK, CHECKS-REPORT, SHOTLIST, BUILD-LOG,
  CLAUDE-CODE-RENDER, PROMPTS, SOURCES, ACTS). This film copies that
  12-file package convention exactly (prior builds shipped 11 files +
  no README; the handoff asks for 12 including README.md).
- 17:40 — Fact-check research (web, primary sources where reachable):
  Roediger & Karpicke 2006 (testing effect, 61% vs 40% at 1 week);
  Karpicke & Roediger 2008; Dunlosky et al. 2013 (high-utility ratings);
  Kornell, Hays & Bjork 2009 and Richland, Kornell & Kao 2009
  (pretesting effect); Cepeda et al. 2006 (distributed practice
  meta-analysis); Ebbinghaus 1885; Chi et al. 1989 (self-explanation).
  Deliberately did NOT quote popular "forget 70% in 24 hours" style
  figures — those come from savings scores for nonsense syllables, not
  recall of real material.
- 17:55 — Wrote ACTS.md (hook + Act 1 the four moves + Act 2 the moves at
  work), SHOTLIST.md, FACTCHECK.md (11-row claim table), SOURCES.md,
  PROMPTS.md ("no generation prompts" + the viewer's your-turn prompt).
- 18:00 — Wrote make_sheet.py. Narration: Liam ("Hallo. This is Liam, in
  for Bear."), Teardown register, all terms defined in-line. Durations at
  ~150 wpm + a breath. First run: beats=10 body=5 total=243s — inside the
  200–320 s band; recap covers Act 1 and Act 2 (asserted).
- 18:10 — Wrote scenes.py (M01–M08). Pre-gate review applied the sibling
  package's lessons: every shape gets an explicit FadeIn/Create/
  GrowFromCenter before any `.animate()`; no stub-only attributes; recap
  lines ≤44 chars at font_size 20 inside the 12.4 plate; composer prompt
  lines ≤30 chars at font_size 18.
- 18:15 — Gate: `python3 -m py_compile` clean on both files;
  `static_scene_check.py` per class: **8 clean · 0 warn · 0 error on the
  first full run.** No fixes were needed.
- Next: write CHECKS-REPORT.md, CLAUDE-CODE-RENDER.md, README.md; push
  all 12 files via gh-put-file.py; verify each via Contents API;
  return the FRICTIONAL.md entry text in the final report.
