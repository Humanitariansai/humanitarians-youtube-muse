# FRICTIONAL.md — muse/ film collection

Build log for the humanitarians-channel Muse film series. One entry per
film (and per substantive build), seven fields each. Values labeled
[record] / [judgment] / [my input].

---

## 2026-10-03 — Film 1: "Register for Muse with a privacy.com card"

**1. Date and what I was working on.**
2026-10-03. First film of the humanitarians-channel Muse series: a
pre-render package (script, Manim visuals, docs) for "Register for Muse
with a privacy.com card", built to FILM-BUILDER-HANDOFF.md spec and pushed
to `muse/register-muse-privacy-card/`. [record]

**2. I tried / expected.**
I expected to follow the handoff's §13 order cleanly: token → toolkit →
study the four finished films → build. I expected the brutlist.art clone
and the GitHub helpers to exist or be trivial. [my input]

**3. What happened (including failures and reversals).**
- The `~/workspace/skills/github/bin/` helpers did not exist; I wrote
  gh-put-file.py, gh-mkdir.py, gh-delete.py from the handoff spec. [record]
- The `custom.github` credential was not provisioned; Bear completed the
  secure form later the same day (token "muse-vm", fine-grained, Contents
  read+write, never expires). [record]
- `git clone` of brutalist.art failed twice (interrupted mid-checkout,
  empty tree). Fixed with `--depth 1 --filter=blob:none --sparse`,
  checking out only `skills/make` and `runtime/qc`. [record]
- make_sheet.py failed its own recap-coverage assertion on the first run:
  the check counted lowercase "act " but the line uses "Act two"/"Act
  three". Fixed to case-insensitive; the line was correct. [record]
- Pre-gate review of the QC stub caught four latent bugs before the
  checker ran: shapes introduced only via `.animate()` (M01 card, M05/M08
  coins, M12 gauge fill) never enter the stub's scene graph; M13's
  text-removal hack used a stub-only `_text` attribute; M13 recap lines
  were wider than the 16:9 frame at real-Manin text metrics. All fixed
  before the first checker run. [record]
- Static QC then passed first try: 13 clean · 0 warn · 0 error. [record]
- Placement: this is a channel film, not course work, so I created a new
  top-level `muse/` collection (`muse/register-muse-privacy-card/`)
  following the repo's `codex/` precedent, and flagged the choice to
  Bear. [judgment]

**4. What I did.**
Built the full 11-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py,
beat_sheet.json — 15 beats, 10 body, 296 s — scenes.py with 13 Manim
scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER),
pushed all files plus the folder README via the Contents API, and
verified all 12 files live via API read. [record]

**5. What Claude or another person contributed.**
Bear set the topic, the channel/persona lock (humanitarians channel,
Liam), the film-identity constants, and every core fact of the film:
the Meta-account signup fork, the $1 hold released in ~1 week, and the
privacy.com $10-limit workaround — all from his own signup experience.
He provisioned the GitHub token and shared four setup screenshots,
which I audited for tokens/PII (clean). The lecture skill, QC checker,
and film-package pattern came from the brutalist.art toolkit and the
four finished assignment-4 films. I wrote every file; the AI contribution
is the drafting, the QC pre-review, and the research verification
against privacy.com and Muse docs. [record]

**6. What I understand now / still do not understand.**
I understand the full pre-render pipeline now: research → ACTS/SHOTLIST/
FACTCHECK → make_sheet → scenes → QC gate → docs → push → verify.
I still do not know whether Bear wants the `muse/` collection placement
to stand, or the next film's topic. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at
`muse/register-muse-privacy-card/` on Humanitariansai/humanitarians-
youtube-muse; CHECKS-REPORT.md records the clean gate. Next step: Bear
renders narration (Kokoro am_onyx) and the review cut on his Mac per
CLAUDE-CODE-RENDER.md, and tells me the next film's topic. [record]

---

## 2026-10-03 — Redos: the two muse/youtube films for a general audience

**1. Date and what I was working on.**
2026-10-03. Bear's redo directive: rebuild the two films under
`muse/youtube/` for the humanitarians AI YouTube channel — general
audience (smart, pragmatic, not AI experts), explain every term, show
rather than tell. [record]

**2. I tried / expected.**
I expected two lecture-skill films in my 11-file package format. The
originals turned out to be full-toolkit-pipeline films (rich beat
schema, built artifacts), not my simplified format — so "redo" meant
adapting their act structures and attribution maps into my workflow,
not converting files. [my input]

**3. What happened (including failures and reversals).**
- Found the two films: `claude-liam-lecture-claude-making-a-film-about-muse/`
  (Bear & Claude's analysis: product, costs, business model, 12-point
  security critique, Bear's resolution; 6 acts) and
  `claude-liam-lecture-muse-making-a-film-about-muse/` (product
  explainer; 4 acts). [record]
- Noted the second film's folder has a committed
  `__pycache__/scenes.cpython-314.pyc` and `.DS_Store` files — minor
  standing-rule violations from a previous session. Left untouched;
  flagged to Bear instead of deleting someone else's history. Its
  `mp3/` holds only timings.json — no audio was committed. [record]
- Redo A ("Muse making a film about Muse" → `muse/youtube/muse-for-everyone/`):
  22 beats, 17 body, 404 s; 17 scenes, QC 17 clean · 0 warn · 0 error
  first run. [record]
- Redo B ("Claude making a film about Muse" →
  `muse/youtube/claude-on-muse-for-everyone/`): 21 beats, 16 body, 418 s;
  19 scenes, QC 19 clean · 0 warn · 0 error first run. Two pre-gate
  catches: `DashedRectangle` isn't in the QC stub (NameError — replaced
  with Rectangle); a `FadeIn` + `.animate` on one mobject in a single
  play() would fight in real Manim (split). The duration assert caught
  426 s > 420 s cap; five beats trimmed to 418 s. [record]
- Translation decisions for the general audience: "fail-safe defaults
  (Saltzer & Schroeder, 1975)" → the two-bouncers visual; "behavioral
  promise, not a technical boundary" → "a promise, not a wall"; token
  allowances cut; open-questions act cut; attribution discipline
  preserved throughout ("researchers report", "their read", "in Nik's
  experience", "the document reports"). [judgment]
- Skill choice: lecture for the product explainer (whole-product
  coverage, same as the original); deep-explainer shape for the analysis
  film (it's an argument: read → critique → resolution). [judgment]

**4. What I did.**
Built both 11-file packages, pushed all files plus folder READMEs via
the Contents API, verified all 24 files live via API reads. Originals
untouched. [record]

**5. What Claude or another person contributed.**
Bear set the redo directive, the audience rule, and the skill menu. The
original film packages (act structures, attribution map, Bear's
document via its citations) were built by a previous session and served
as the adaptation source; every narration line and visual is new.
The security-critique substance is Bear & Claude's analysis, voiced as
their opinion throughout. [record]

**6. What I understand now / still do not understand.**
I understand the redo pattern now: keep the spine and the attribution,
rewrite the words, redraw the pictures. I don't know whether Bear wants
the originals' folders cleaned of the .pyc/.DS_Store, or which film
comes next. [my input]

**7. Evidence and next step.**
Evidence: `muse/youtube/muse-for-everyone/` (12 files) and
`muse/youtube/claude-on-muse-for-everyone/` (12 files) verified live;
CHECKS-REPORT.md files record the clean gates. Next step: Bear renders
on his Mac per the CLAUDE-CODE-RENDER.md files, and names the next
film. [record]

---

## 2026-10-03 — Cleanup: stray files under muse/

Bear asked for the committed strays to be removed. Deleted via the
Contents API (3 files, 3 commits): `muse/.DS_Store`,
`muse/youtube/.DS_Store`, and
`muse/youtube/claude-liam-lecture-muse-making-a-film-about-muse/__pycache__/scenes.cpython-314.pyc`.
Verified via recursive tree read: no `.DS_Store`, `__pycache__`, or
`.pyc` entries remain under `muse/`. The `mp3/` dirs hold only
timings.json — no audio was ever committed. [record]

---

## 2026-10-03 — Film: "Stop using your own Claude at work."

**1. Date and what I was working on.**
2026-10-03. Built the pre-render package for "Stop using your own Claude
at work." (slug `personal-ai-at-work`) from the mirror-repo source
`claude-for-artificial-intelligence/how-to-use-your-personal-ai-at-work`,
rewritten for the humanitarians channel's general audience, pushed to
`muse/youtube/how-to-use-ai/personal-ai-at-work/`. [record]

**2. I tried / expected.**
I expected to follow the sibling package's 12-file convention exactly and
to pick deep-explainer per the task's suggestion. I expected the GitHub
push loop to run cleanly one file at a time. [my input]

**3. What happened (including failures and reversals).**
- Read the source beat sheet, README rebuild guide, and PEDAGOGY.md (empty)
  from the mirror repo via the Contents API surrogate flow. [record]
- Skill decision: lecture, not deep-explainer or cc-explainer (cc-explainer
  is for terminal sessions; lecture's BDEFS beat is what the audience
  rewrite needs). [judgment]
- Fact-checked every claim against current press/vendor guides (2026-10-03):
  Samsung April 2023 story, Anthropic toggle + 5-year retention +
  forward-only opt-out, ChatGPT/Grok/Gemini toggle paths, Team/Enterprise
  no-training defaults. [record]
- The source's "the not a lawyer — he's clear about that" and "one
  additional guide covers" were garbled; the referenced guide could not be
  identified, so the attribution was dropped and replaced with Liam's own
  "I'm no lawyer — talk to yours", and the "all three have precedent"
  claim was softened to framings. [judgment]
- make_sheet.py passed all assertions on the first run: 14 beats, 9 body,
  284 s (~4m44s). [record]
- Pre-gate self-review caught two sloppy lines (dead move_to in M10,
  unused variable in M07) and an M12 plate/do-card overlap; all fixed
  before the QC run. [record]
- Static QC then passed first try: 12 clean · 0 warn · 0 error. [record]
- The second GitHub push hit HTTP 409 — a sibling agent had pushed to the
  same branch between my first and second push. Resolved with a retry
  loop; all pushes then landed. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py,
beat_sheet.json — 14 beats, 9 body, 284 s — scenes.py with 12 Manim
scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER,
README), pushed all 12 files via gh-put-file.py, and verified each live
with a Contents API read (12/12 HTTP 200). [record]

**5. What Claude or another person contributed.**
Bear set the topic, the channel/persona lock (humanitarians channel, Liam,
am_onyx, Teardown, @NikBearBrown), the film-identity constants, the
audience rewrite rules, and the QC conventions via the handoff spec and
the finished sibling packages. [record]

**6. What I understand now / still do not understand.**
I understand the audience rewrite workflow now: the lecture BDEFS beat
absorbs the "explain every term" rule, and dated toggle paths are made
evergreen by teaching the action (find the training toggle) rather than
only the path. I still do not know whether Anthropic's new-account default
for "Help improve our AI models" is on or off — the film says "don't
assume; check" because Anthropic does not state it. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at
`muse/youtube/how-to-use-ai/personal-ai-at-work/` on
Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the
clean gate; remote beat_sheet.json round-trips 14 beats / 284 s. Next
step: Bear renders narration (Kokoro am_onyx) and the review cut on his
Mac per CLAUDE-CODE-RENDER.md; never publish without his explicit
instruction. [record]

---
## 2026-10-03 — Film: "You can't beat AI." (general-audience redo)

**1. Date and what I was working on.**
2026-10-03. Pre-render package for "You can't beat AI." (slug you-cant-beat-ai), a general-audience redo of `claude-for-artificial-intelligence/how-to-beat-ai-once-it-inevitably/` for the humanitarians AI YouTube channel, pushed to `muse/youtube/how-to-use-ai/you-cant-beat-ai/`. [record]

**2. I tried / expected.**
I expected to follow the film-builder pattern cleanly: read the source beat sheet via the Contents API, pick ai-explainer, write make_sheet.py with self-assertions, generate beat_sheet.json, author 12 Manim scenes, pass the static QC gate first try, and push 12 files with the gh-put-file.py helper. [my input]

**3. What happened (including failures and reversals).**
- make_sheet.py's own assertions caught two authoring bugs before any file was written: the overview narration was 48 words over the 45-word cap (trimmed to 41), and five beats were under the ~150 wpm speech floor (durations raised to 295 s total instead of cutting narration). [record]
- Static QC passed 11/12 on the first run; S12_Outro failed the distinctness check (text-only outro: 1 shape-state across 4 frames). Fixed by adding evolving non-text shapes (spark star + growing terracotta underline); re-ran 12/12 clean, 0 warnings, 0 errors. [record]
- Fixed a latent bug before QC: S09 tick positions used an inline `__import__("math")` hack; replaced with module-level `import math`. [record]
- Push anomaly: PROMPTS.md and CLAUDE-CODE-RENDER.md hit HTTP 409 sha-mismatches and briefly 404'd, as if another session was writing the same folder concurrently. Retries succeeded; final verification shows all 12 files live and byte-identical. [record]
- The skill choice went to ai-explainer rather than the suggested deep-explainer: the film is one tight insight ("outsource the work, never the understanding"), and the source README itself recommends ai-explainer for that shape. [judgment]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK with the Dahmani & Bohbot 2020 GPS-literature grounding, make_sheet.py, beat_sheet.json — 12 beats, 295 s, 638 words — scenes.py with 12 Manim scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README), pushed all files via the Contents API, and verified all 12 live via API read. Nothing rendered, published, or staged; no audio/video committed. [record]

**5. What Claude or another person contributed.**
The parent agent supplied the film spec (beat-sheet path, slug, identity constants, audience/rewrite rules, push rules). The ai-explainer SKILL.md supplied the bookend spine and laws (cold open, hesitant-writer overview, handoff, outro, IN-FOR-BEAR). The five-step method, GPS analogy, and chief-of-staff scenario come from the source beat sheet; the Dahmani & Bohbot (2020) citation came from my own web verification. I wrote every file. [record]

**6. What I understand now / still do not understand.**
I understand the redo pattern for this series: keep the source's argument and facts, rewrite persona/shots/audience, label illustrative scenarios on screen and in voice, and let make_sheet.py's assertions catch narration-budget and timing bugs before QC. I still do not understand what caused the concurrent-write anomaly on the two file pushes (another worker session, or a transient GitHub API inconsistency). [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live and byte-identical at `muse/youtube/how-to-use-ai/you-cant-beat-ai/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the clean gate. Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md, only on his instruction. [record]

---
## 2026-10-03 — Film: "ChatGPT or Claude?" (everyone-wants-one-ai)

**1. Date and what I was working on.**
2026-10-03. Built the pre-render package for "ChatGPT or Claude?" — the general-audience redo of `claude-for-artificial-intelligence/everyone-wants-one-ai` ("ChatGPT-5.5 or Claude 4.7?") for the humanitarians AI YouTube channel — and pushed all 12 files to `muse/youtube/how-to-use-ai/everyone-wants-one-ai/`. [record]

**2. I tried / expected.**
I expected to pick between cc-explainer and ai-explainer per the brief's suggestion, follow the established 12-file convention from the sibling builds, pass the QC gate first try, and push cleanly with gh-put-file.py. [my input]

**3. What happened (including failures and reversals).**
- Chose ai-explainer over cc-explainer: the film compares AI chat products for a general audience and contains no Claude Code terminal session, so cc-explainer's TERMINAL-FIRST law does not fit; the source README also recommends ai-explainer. [judgment]
- Retitled the film "ChatGPT or Claude?": the source's version numbers are real in tech press but churn too fast to put in a title — GPT-5.5 entered ChatGPT 2026-04-23 and is reported retiring 2026-10-14; "Claude 4.7" misnames Claude Opus 4.7. The film names vendors and approaches, never point releases; all version claims flagged in FACTCHECK.md §1. [record]
- make_sheet.py's own narration-clock assertion failed on the first run (B05: 66 words against a 26 s budget at 150 wpm). Fixed by trimming one word ("a good default work brain" → "a default work brain"); reran clean: 12 beats, 7 body, 273 s. [record]
- Static QC passed first try on all 10 scene classes: 0 warnings, 0 errors. [record]
- Pushes hit repeated HTTP 409s: sibling subagents were pushing other films to the same repo at roughly one commit per 1–3 seconds, racing the Contents API branch update (scenes.py and PROMPTS.md needed backoff retries). All 12 files landed and verified afterward. [record]

**4. What I did.**
Rewrote the beat sheet for a smart non-expert audience (plain-language definitions of model/prompt/context/benchmark in B02; dropped AskUserQuestion/Connectors/multi-agent jargon; compressed the Gemini/Gamma benchmark claims to a line that makes no factual claim; undated the "April week" news hook); built make_sheet.py with beat-count, per-beat narration-clock, and total-duration assertions; wrote scenes.py with 10 Manim scenes, every mobject introduced via add()/FadeIn()/Write()/Create() per the film-1 lesson; wrote the 8 supporting docs; pushed and verified all 12 files. [record]

**5. What Claude or another person contributed.**
The parent orchestrator's brief supplied the version-number rule ("write the film without them") and the FRICTIONAL.md seven-field format; Bear's standing rules (push everything to the humanitarians GitHub, general audience, show-don't-tell, never publish) governed the build. The fact-check used live web sources, not model memory. [record]

**6. What I understand now / still do not understand.**
I understand now that the Contents API create-file PUT can 409 under rapid concurrent commits to the same repo, and that backoff retries resolve it — a retry loop in gh-put-file.py would be worth adding. I still do not know whether Bear prefers the retitle "ChatGPT or Claude?" or wants the versioned working title kept for the series. [judgment]

**7. Evidence and next step.**
Evidence: 12 files live at `muse/youtube/how-to-use-ai/everyone-wants-one-ai/` in Humanitariansai/humanitarians-youtube-muse (all HTTP 200, sizes match local); CHECKS-REPORT.md records 10 clean · 0 warn · 0 error; FACTCHECK.md has 12 audited claims. Next step: Bear renders locally per CLAUDE-CODE-RENDER.md (Kokoro am_onyx narration + Manim scenes M01–M10) and reviews the cut; nothing is staged for publication. [record]

---
## 2026-10-03 — Film: "Claude, When Not." (claude-when-not)

**1. Date and what I was working on.**
2026-10-03. Built the pre-render package for "Claude, When Not." — a
general-audience show-tell rebuild of the "Claude, For Students" season
finale (source: hai-when-not in the mirror repo), pushed to
`muse/youtube/how-to-use-ai/claude-when-not/`. [record]

**2. I tried / expected.**
I expected the show-tell skill's bookends (Remotion hesitant-writer,
ClaudeDefinitions, composer, outro) and a beat count near the source's 11.
I expected the GitHub push of 12 files to be uneventful. [my input]

**3. What happened (including failures and reversals).**
- Drew all four bookends as Manim scenes instead of Remotion compositions
  (single-renderer pipeline, consistent with the earlier general-audience
  redos) and declared `bookend_exempt` with a reason in the beat sheet.
  [record]
- `make_sheet.py` asserts 13 beats and a 170–260 s band; total came to
  244 s (~4:04). [record]
- Static QC failed once: B08_Answer errored with 6 coords outside the frame
  — the four predict cards at x=-1.5+i*2.9 pushed card D's edge to 8.5,
  past the frame. Fixed to x=-4.35+i*2.9 (edges ±5.65); all 13 scenes then
  passed 1 clean · 0 warn · 0 error. [record]
- Pre-QC, the BHTF composer header band overlapped the window's top edge;
  repositioned before the first checker run. [record]
- Pushing raced a sibling agent's concurrent pushes: 5 of 12 files got HTTP
  409 ref-moved conflicts, all resolved by retry with backoff; the remote
  scenes.py was verified byte-identical to local after. [record]

**4. What I did.**
Rewrote the source's student-specific narration into a standalone
general-audience film (13 beats, Teardown register, Liam voice); defined
scaffold/crutch/hallucination/disclosure in plain words; built the full
12-file package (ACTS, SHOTLIST, FACTCHECK with 14 audited claims, sheet
generator, 13 Manim scenes on the iso_kit with one recurring cast, docs,
render instructions); fact-checked hallucination claims against Ji et al.
2023, NIST AI 600-1, and the GPT-4 technical report; pushed and verified
all 12 files live. [record]

**5. What Claude or another person contributed.**
The parent orchestrator assigned the film, slug, and write path. Bear's
source material supplied the whole argument (scaffold vs. crutch, the
use/don't-use lists, the hide-it test, predict-then-answer) and its
PEDAGOGY.md evidence table, which grounded the fact-check. I wrote every
file and the rewritten narration. [record]

**6. What I understand now / still do not understand.**
I understand the pre-render pipeline end to end and that concurrent sibling
pushes to the same repo need retry-with-backoff on 409s. I chose show-tell
over cc-explainer because the film is a judgment argument, not an interface
mechanic. [judgment] I still do not know whether Bear wants the drawn
bookends kept or the Remotion interface bookends restored for this series.
[my input]

**7. Evidence and next step.**
Evidence: 12 files verified live (HTTP 200) at
`muse/youtube/how-to-use-ai/claude-when-not/` on
Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records
13 clean · 0 warn · 0 error. Next step: Bear generates Kokoro am_onyx
audio, writes actual_duration_s back into beat_sheet.json, and renders on
his Mac per CLAUDE-CODE-RENDER.md. [record]

---
## 2026-10-03 — Film: "Claude, On the Job." (pre-render package, slug claude-on-the-job)

**1. Date and what I was working on.**
2026-10-03. Built the full pre-render package (12 files: script/beat sheet, Manim scenes, docs) for "Claude, On the Job.", a humanitarians-channel show-tell film rewritten from episode H4 of the "Claude, For Students" series for a smart, pragmatic general audience. Pushed to `muse/youtube/how-to-use-ai/claude-on-the-job/`. [record]

**2. I tried / expected.**
I expected to pick show-tell over cc-explainer after reading both skills, follow the skill's bookend spine (hesitant writer → terms → drawn body → composer Your Turn → spoken outro), and get the static QC gate green on the first full pass like the previous film. [my input]

**3. What happened (including failures and reversals).**
- The static checker failed `B01_TierOne` with "shapes never change — 1 distinct shape-state across 11 frames." Cause: its five pages entered via `animate.shift()` (the stub ignores moves), and the human→ghost swap was shape-identical. Fixed by entering each page with `FadeIn(..., shift=DOWN*1.4)` — one new non-text shape per play, and the fast drop doubles as the beat's motion claim. Updated the beat's visual intent and regenerated the sheet. Re-ran: clean. [record]
- Preventive: replaced all VGroup indexing/iteration with plain Python lists before the first checker run (the stub treats group slices as plain lists), and used only fixed coordinates for labels. [record]
- During pushing, 6 files 409'd, then disappeared from the repo entirely; 2 more 409'd and disappeared on the retry pass. A concurrent writer appears to be pushing to and deleting the same paths in a cycle. All retries eventually landed; final verification showed 12/12 live and byte-identical. [record]
- Cut "distrust-calibration" from the narration (a series neologism needing its own definition beat); the idea survives as the B06 practice. Reversal of the source's vocabulary, not its argument. [judgment]

**4. What I did.**
Chose show-tell and read its SKILL.md end to end; fetched the source beat sheet + README + PEDAGOGY.md from the mirror repo via the Contents API (surrogate credential), ignoring `mp3/`; rewrote all narration for the general audience (13 beats, 176 s estimated, zero stats/dates/version numbers by design); wrote `make_sheet.py` with self-assertions and generated `beat_sheet.json`; wrote `scenes.py` (iso_kit pasted, 9 scene classes, whole-film cast); fact-checked every claim into FACTCHECK.md with real citations; wrote the other 8 docs; pushed and verified all 12 files. [record]

**5. What Claude or another person contributed.**
The source argument, tier framework, and quiz verdict came from Bear's episode H4 and its PEDAGOGY.md (which also supplied the evidence-table citations I verified independently). The show-tell skill, iso_kit, gate-trap list, and the `custom.github` credential flow are toolkit/parent-provided infrastructure. [record]

**6. What I understand now / still do not understand.**
I understand the static checker's actual contract now: it is not "runs clean" but "every play after the first must introduce a genuinely new non-text shape" — moves and shape-identical swaps are invisible to it, so entrances must be FadeIn/Create/GrowFromCenter of new objects. I still do not understand what the concurrent writer on these paths is doing (push/delete cycling on SHOTLIST.md, beat_sheet.json, and the other four) — worth the parent checking before render, or the files may be clobbered. [judgment]

**7. Evidence and next step.**
Evidence: 12/12 files HTTP 200 and byte-identical at `muse/youtube/how-to-use-ai/claude-on-the-job/` (verified 2026-10-03); CHECKS-REPORT.md records 9/9 scenes 0 warn / 0 error. Next step: de-duplicate the concurrent writer on this path, then Bear renders on his Mac per CLAUDE-CODE-RENDER.md (Kokoro audio + whisper-checks, stills, `art run`, Gates A/B/V/T, `art final`) — stage and publish only on his explicit word. [record]

---
## 2026-10-03 — Film: "How to Use Claude" (show-tell rebuild)

**1. Date and what I was working on.**
2026-10-03. Built the pre-render package for "How to Use Claude", a show-tell
rebuild of the source beat sheet at
`claude/claude-youtube/claude-liam-how-to-use-claude` for the humanitarians AI
YouTube channel (Liam persona, Teardown register, Kokoro am_onyx, channel
claude-liam, watermark @NikBearBrown). Output:
`muse/youtube/how-to-use-ai/how-to-use-claude/`, 12 files. [record]

**2. I tried / expected.**
I expected show-tell to fit: a visual explainer for non-experts, one image
per beat. I expected the iso kit + static checker to carry the visual QA, and
`until()` phrase timing to keep motion off each clip's midpoint. [my input]

**3. What happened (including failures and reversals).**
- The source's B04 (three strengths + failure modes, 25 s narration) violated
  show-tell law 9; I split it into B05/B06/B07 (one strength each) plus a new
  B08 "check it" warning beat. [record]
- B03's reply card overlapped the chat window's composer pill in the first
  draft; added `composer=False` to the `chat_window()` helper. [record]
- B07's natural trigger phrase ("first pass") landed inside the clip's 45–55%
  GATE T sampling window; re-triggered the final page on "and you spend your
  time" (post-midpoint). [record]
- B04 carries 4 one-word labels (project + style/rules/example captions),
  slightly over the 2–3 guidance; kept, since the captions are what make three
  identical cards distinct. Noted in SHOTLIST.md. [judgment]
- First two Contents API pushes (ACTS.md, FACTCHECK.md) failed HTTP 409 —
  concurrent sibling edits in the same repo. Retried and both landed. [record]
- `manim_layout_audit.py --curve-strict` could not run here (no
  Manim/pangocairo in this VM); hand-placed labels with >=0.3 leader gaps as
  mitigation. Deferred to the Mac render pass. [record]
- Static QC passed first try: 9 classes, 0 warnings, 0 errors. [record]

**4. What I did.**
Rewrote the narration from zero for a general audience (assumes no prior AI
chat use); kept the source's argument (context scales quality; Projects as the
fix; artifacts/analysis/rewriting; your-turn prompt). Wrote make_sheet.py
(13 beats, asserts on count/order/duration/bookend contracts; 196.4 s),
scenes.py (iso kit pasted verbatim + 9 scene classes, until()/finish() paced),
and the 10 doc files (ACTS, SHOTLIST, FACTCHECK, SOURCES, PROMPTS, BUILD-LOG,
CHECKS-REPORT, CLAUDE-CODE-RENDER, README). Pushed all 12 files and verified
each live via Contents API read. [record]

**5. What Claude or another person contributed.**
Bear set the film-identity constants, the general-audience rule, the
show-tell skill and its laws, and the bookend conventions (hesitant writer,
terms card, composer Your Turn, spoken @NikBearBrown outro). A sibling
subagent's earlier film-build (register-muse-privacy-card) established the
12-file package layout I followed. The parent orchestrator assigned the
source path, slug, and output path. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell beat economics now: a beat past ~15 s is two ideas
and must split, but splitting is only safe when each idea has its own motion
— the three strengths each did. I still do not understand how GATE T will
read the B04 iso box captions at 4K (three small ink labels inside a kraft
box mouth); the stills pass on the Mac must confirm or the captions move
outside the box. [judgment]

**7. Evidence and next step.**
Evidence: beat_sheet.json (13 beats, 196.4 s) and scenes.py live at
`muse/youtube/how-to-use-ai/how-to-use-claude/` in
Humanitariansai/humanitarians-youtube-muse (all 12 paths HTTP 200);
CHECKS-REPORT.md records the clean static run. Next step: Bear renders on his
Mac per CLAUDE-CODE-RENDER.md — Kokoro audio, whisper-check "Hallo", layout
audit --curve-strict, midpoint guard with measured durations, stills, then
`art run` / `art final`. Nothing staged or published. [record]

---
## 2026-10-03 — Film: "Claude, Allowed." (show-tell, claude-allowed)

**1. Date and what I was working on.**
2026-10-03. Built the pre-render package for "Claude, Allowed." — a show-tell rewrite of the mirror repo's `hai-claude-allowed` ("Claude, For Students" H1) for the humanitarians AI general audience — pushed to `muse/youtube/how-to-use-ai/claude-allowed/`. [record]

**2. I tried / expected.**
I expected: read the source beat sheet + PEDAGOGY, pick show-tell vs cc-explainer, rewrite narration for a general audience, fact-check every claim, build the 12-file package, pass the QC gate, push, verify. I expected the GitHub push helper to behave as in the Film 1 build. [my input]

**3. What happened (including failures and reversals).**
- Skill choice: show-tell over cc-explainer — the film is a concept teardown (scope, exception trap, disclosure habit), not a terminal session; the ClaudeComposerAsk Your-Turn bookend naturally holds the email-draft handoff. [judgment]
- General-audience rewrite: kept the school policy as the concrete running example but named employers in B00/BIDEA and closed BHTF with "At work, swap in your manager." No student-only beats remain. [record]
- Fact-check: 8 claims, 6 PASS / 2 EXEMPT. Verified the AI Fluency course is free and CC-licensed (Anthropic, Aug 2025 announcement) via three independent sources; deliberately did NOT claim the source PEDAGOGY's Jul-14-2026 "Claude for Teachers" announcement date since I could not independently verify it. No quantitative claims anywhere (Bastani numbers stay reserved for H2). [record]
- QC: py_compile clean; static_scene_check 6/6 scenes, 0 warnings, 0 errors — first run, no fixes needed. [record]
- GitHub pushes: 5 files pushed cleanly, 7 failed first with HTTP 409 sha-mismatch while the remote files 404'd. Root cause: stale cached Contents API GET responses (the helper's get_sha returned phantom shas). Fixed by re-issuing with `Cache-Control: no-cache` plus unique query-string cache-busters — all remaining files then returned 201 on the first attempt. Nothing was overwritten; the failed files were never created remotely. [record]
- All 12 files verified live via Contents API GET (HTTP 200) and byte-identical to local. [record]

**4. What I did.**
Built the full 12-file package: make_sheet.py (10 beats, 6 Manim body beats, 170.0 s estimated, all asserts green), beat_sheet.json, scenes.py (iso kit verbatim + 6 scene classes), ACTS, SHOTLIST, FACTCHECK, SOURCES, PROMPTS, BUILD-LOG, CHECKS-REPORT, CLAUDE-CODE-RENDER, README; pushed and verified all 12. [record]

**5. What Claude or another person contributed.**
The source argument, thesis, and the ask-in-writing / disclosure / fluency moves came from the mirror repo's hai-claude-allowed (PEDAGOGY.md evidence table). The show-tell skill, iso drawing kit, and static QC checker came from the brutalist.art toolkit. Bear set the film-identity constants (Liam, am_onyx, Teardown, claude-liam, @NikBearBrown) and the general-audience standing rules. I did the rewrite, research, scenes, and QC. [record]

**6. What I understand now / still do not understand.**
I understand the gh-put-file.py 409 failure mode now: when the Contents API GET is served a stale/phantom sha, the PUT 409s against a file that doesn't exist — the fix is cache-busting the GET, not blindly retrying the same call. I still do not know what served the phantom shas (caching proxy vs read replica). [my input]

**7. Evidence and next step.**
Evidence: 12/12 files byte-identical at `muse/youtube/how-to-use-ai/claude-allowed/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the clean gate (6/6 scenes, 0 warn / 0 err). Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md. [record]

---
## 2026-10-03 — Film: "Claude, Not Your Answer." (claude-not-your-answer)

**1. Date and what I was working on.**
2026-10-03. Built the pre-render package for "Claude, Not Your Answer." — a show-tell film for the humanitarians AI YouTube channel, rewritten for a general audience from the mirror repo's `claude-for-artificial-intelligence/hai-not-your-answer/` ("Stop using your own Claude at work."). Pushed to `muse/youtube/how-to-use-ai/claude-not-your-answer/` on Humanitariansai/humanitarians-youtube-muse. [record]

**2. I tried / expected.**
I expected a straightforward show-tell build: read the source beat sheet, rewrite the narration for non-experts, draw nine Manim scenes, pass the static QC, push 12 files. I expected the GitHub push loop to be uneventful. [my input]

**3. What happened (including failures and reversals).**
- The source beat sheet's metadata (student series, "Pragmatist" register, af_kore voice) didn't match its actual content (workplace AI privacy); I rebuilt from the content, not the metadata. [record]
- Fact-checking held up: the Samsung April-2023 timeline, the Anthropic Sept-2025 training/retention change, and all four per-app toggle paths verified against primary announcements and mid-2026 guides. One correction applied during writing: Claude's exact toggle label is version-sensitive, so it is voiced generically ("the training toggle") and flagged in FACTCHECK.md. [record]
- Static QC passed first run: 9 scenes, 0 warnings, 0 errors — no fixes needed. [record]
- The push loop hit HTTP 409 sha-conflicts on four files (sibling film agents pushing concurrently); I initially missed that scenes.py was also a 409 — a verify-every-file pass caught the 404 and I pushed it. All 12 files now verified live, and the remote beat_sheet.json matches local. [record]
- Mid-task the standing rules expanded (refactor directive now covers the student series; new rule to maintain muse/README.md as a film index). I did not edit the shared README — concurrent sibling writers make that a conflict risk — so the index-row text is returned below for the parent to apply, same rationale as FRICTIONAL.md. [judgment]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST with card-test column, FACTCHECK with 12 claims, make_sheet.py with self-assertions → beat_sheet.json with 13 beats / 186.4 s, scenes.py with 9 Manim scene classes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README), pushed all files, verified all 12 live. [record]

**5. What Claude or another person contributed.**
Bear set the topic (the source beat sheet), the channel/persona/voice/register lock, the audience rule, and the skill menu. The show-tell skill, iso_kit, and static QC checker came from the brutalist.art toolkit. The factual spine (Samsung case, toggle paths, legal framings, clean-room policy) comes from the source film; every narration line, visual, and the fact-check re-verification are new. Sibling subagents pushing other films concurrently caused the 409s. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell pipeline end to end now, including the retry-on-409 push pattern and the verify-every-file discipline that caught the missing scenes.py. I still do not know whether the parent wants one coordinated muse/README.md index update or per-film edits, given the concurrent writers. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/claude-not-your-answer/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records 9 clean · 0 warn · 0 error. Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md; parent to fold the README index row below into muse/README.md. [record]

---
## 2026-10-03 — Film 2: Claude, Your Quizmaster (how-to-use-ai lane)

**1. Date and what I was working on.**
2026-10-03: built the pre-render package for "Claude, Your Quizmaster"
(source: mirror repo `claude-for-artificial-intelligence/hai-your-quizmaster`),
rewritten for the general audience, at
`muse/youtube/how-to-use-ai/claude-your-quizmaster/`. [record]

**2. I tried / expected.**
I expected to: pick show-tell vs cc-explainer after reading both SKILL.md
files; rewrite the student-framed beat sheet for a general audience;
fact-check every claim against primary sources; pass the QC gate first
run by copying the sibling package's proven patterns; push 12 files and
verify each via Contents API. [my input]

**3. What happened (including failures and reversals).**
Two readbacks of the source beat_sheet.json disagreed (one showed beats
from a different film); re-fetched deterministically and confirmed by sha
before building. [record] The GitHub Contents API returned transient HTTP
409s on ~half the PUTs — stale replica reads, not a real conflict; every
one cleared with a fresh GET + retry + longer backoff. [record] A MEMORY.md
update landed mid-build adding the standing rule to keep muse/README.md as
the film index; I added this film's row rather than skipping it. [record]
[my input] for the judgment that the index update was in scope.

**4. What I did.**
Chose show-tell (cc-explainer rejected: terminal-session genre, no terminal
in this film). Researched primary sources: Roediger & Karpicke 2006,
Kornell/Hays/Bjork 2009, Richland/Kornell/Kao 2009, Cepeda et al. 2006,
Ebbinghaus 1885, Chi et al. 1989, Dunlosky et al. 2013. Wrote all 12 files
(10 beats, 243 s, 8 scenes); make_sheet.py asserts beat count, act order,
recap coverage, handoff prompt read in full, and the 200–320 s band. QC:
8 clean · 0 warn · 0 error first run. Pushed all 12 files, byte-verified
each via Contents API; updated muse/README.md index. Did not touch
muse/FRICTIONAL.md. [record]

**5. What Claude or another person contributed.**
The parent orchestrator set the task, skill menu, and identity constants.
The source argument ("the best use of an answer machine is making it ask
the questions") and the four-move structure came from the mirror repo beat
sheet; every narration line, drawing, and the audience reframing are new.
The sibling package `register-muse-privacy-card` supplied the proven 12-file
convention and QC lessons. [record]

**6. What I understand now / still do not understand.**
I understand the GitHub 409 pattern now: treat it as replica lag, re-read
the sha, retry with backoff — never as evidence of a real conflict without
checking the commit history. [judgment] I do not know whether the stale
reads come from a GitHub replica or the surrogate credential proxy, and
I don't know whether Bear wants the "Hallo" greeting kept or replaced
across films. [my input]

**7. Evidence and next step.**
Evidence: `muse/youtube/how-to-use-ai/claude-your-quizmaster/` (12 files,
byte-verified); `muse/README.md` index row; CHECKS-REPORT.md (8 clean).
Next step: Bear renders on his Mac per CLAUDE-CODE-RENDER.md (Kokoro
am_onyx narration, then `./art run` / `./art final`), and names the next
film. [record]

---
## 2026-10-03 — Film: "AI will fail." (why-ai-will-fail)

**1. Date and what I was working on.**
2026-10-03. Built the pre-render package for "AI will fail." (slug
why-ai-will-fail) for the humanitarians AI YouTube channel — a from-scratch
rewrite of the mirror-repo beat sheet
(nikbearbrown/humanitarians-youtube-muse:claude-for-artificial-intelligence/why-ai-will-fail)
for the general audience: Liam persona ("Liam, in for Bear"), Teardown
register, Kokoro am_onyx. Pushed to
muse/youtube/how-to-use-ai/why-ai-will-fail/ on
Humanitariansai/humanitarians-youtube-muse. [record]

**2. I tried / expected.**
I expected the 12-beat source to port straightforwardly into the 12-file
package, and the static QC to pass first try since I hand-placed every
coordinate inside the safe area. [my input]

**3. What happened (including failures and reversals).**
- Reading the actual source article (Ruben Hassid, "AI will fail.", How to
  AI) showed the beat sheet's "century of predictions" framing came from a
  real list — but three of its famous quotes are weakly attributed: Watson
  "five computers" (apocryphal, no record), Gates "640K" (urban legend,
  denied), Patent Office "everything invented" (disputed). I cut all three
  and logged the cuts in FACTCHECK.md. [record]
- Skill choice: ai-explainer over deep-explainer — one tight insight, not
  a multi-act documentary; the source README itself recommends ai-explainer
  for this shape. [judgment]
- Static QC failed on first run for SceneYourTurn: 1 error ("shapes never
  change — 1 distinct shape-state across 4 frames"). The prompt card was
  the beat's only non-text shape, so all snapshots were identical. Fixed by
  typing the handoff prompt line-by-line with a moving terracotta cursor
  (each play changes the shape state); re-ran clean with 6 distinct states.
  The fix also improves the real render. [record]
- Pushing the muse/README.md index update hit HTTP 409 — a sibling
  film-builder agent updated the same file concurrently. Re-fetched,
  re-applied my row, pushed clean (1497eef); the sibling's row is intact.
  [record]
- Two MEMORY.md standing-rule updates arrived mid-build: beat sheets under
  muse/ (already the case for this film) and the muse/README.md film-index
  rule (applied: new row + series row updated). [record]

**4. What I did.**
Built the full 12-file package: ACTS, SHOTLIST, FACTCHECK (15 claims
checked, 7 cut or softened), make_sheet.py (14 beats, 335.2 s, all
assertions pass), beat_sheet.json, scenes.py (14 Manim scene classes,
Claude fidelity palette), SOURCES, BUILD-LOG, CHECKS-REPORT (14 SHOW /
0 HOLD / 0 PUNT; teaching arc 6/6), PROMPTS, CLAUDE-CODE-RENDER, README.
Pushed all 12 files, verified each live via Contents API (HTTP 200, byte
sizes match). Updated the muse/README.md film index. Nothing rendered or
published; no audio committed. [record]

**5. What Claude or another person contributed.**
Bear set the film-identity constants (Liam, am_onyx, Teardown, claude-liam,
@NikBearBrown), the audience rule (general audience, every term explained,
show-don't-tell), and the 12-file package convention. The parent
orchestrator supplied the task spec and the mirror-repo reading method. The
argument and quote list come from Ruben Hassid's article; verification
against primary sources (Reuters, Wikipedia/Wikiquote, Elon archive,
NBER/MIT) was my research. A sibling agent's concurrent README edit caused
the 409 I worked around. I wrote every file. [record]

**6. What I understand now / still do not understand.**
I understand the full pre-render pipeline and the QC stub's real failure
modes now (text-only beats fail distinctness; the moving-cursor fix is a
reusable pattern for prompt-typing beats). I understand the film-index
maintenance rule and the 409-retry protocol. I still do not know which film
is next in the how-to-use-ai series, or whether Bear wants the
verdict/handoff/outro bookend wording standardized across films. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at
muse/youtube/how-to-use-ai/why-ai-will-fail/ on
Humanitariansai/humanitarians-youtube-muse (commits 574f34e through
af58826); CHECKS-REPORT.md records the clean gate; muse/README.md indexes
the film (commit 1497eef). Next step: Bear renders narration (Kokoro
am_onyx) and the Manim scenes on his Mac per CLAUDE-CODE-RENDER.md. [record]

---
## 2026-10-03 — Film 2: "How to outsource everything to AI & get dumb"

**1. Date and what I was working on.**
2026-10-03. Second film of the humanitarians-channel Muse series: a pre-render package (script, Manim visuals, docs) for "How to outsource everything to AI & get dumb" (slug `how-to-rot-your-brain-with-ai`), pushed to `muse/youtube/how-to-use-ai/how-to-rot-your-brain-with-ai/`. [record]

**2. I tried / expected.**
I expected to choose between show-tell and ai-explainer, rewrite the Kore-persona source beat sheet for Liam and the general audience, add fact-checked evidence for its claims, and pass the QC gate. I expected the GitHub push helper to work first try for all 12 files. [my input]

**3. What happened (including failures and reversals).**
- Skill choice: show-tell. ai-explainer is the Claude-app-skin brand for product explainers; this film is a behavioral concept for non-experts and the job demands drawn demonstrations over cards — show-tell's "one image per beat, the voice explains" was the exact fit. [judgment]
- Added two evidence beats the source lacked: B07 (UCL 2017 satnav study, Nature Communications) and B08 (MIT Media Lab 2025 "Your Brain on ChatGPT" preprint, arXiv:2506.08872); both numbers attributed aloud and captioned on screen per show-tell law 8, with the preprint caveat spoken ("suggestive, not settled"). [record]
- Reversal: B02's terracotta ring around the brain became an ink ring + terracotta dot, per the drawing law (curves in ink, terracotta for the end dot). [judgment]
- Static QC passed 10/10 clean, 0 warnings, 0 errors, on the first run — no fixes needed. [record]
- Push failures: 3 of 12 files failed the first push round with HTTP 409 "is at X but expected Y"; two succeeded on retry, SHOTLIST.md needed a direct create-after-404 (commit ec3d659). A GET during the incident returned 404 for a file the helper claimed existed — phantom-sha races, not real conflicts. All 12 verified live afterward (HTTP 200, size-matched). [record]
- Not done by design: no audio generated, no Manim render, nothing published. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py, beat_sheet.json — 14 beats, ~239 s — scenes.py with 10 Manim scene classes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README), pushed all 12 to the write repo, verified each live via Contents API read. [record]

**5. What Claude or another person contributed.**
Bear set the topic, the channel/persona/voice/register lock, the film-identity constants, and the source beat sheet's argument (paste-and-hope, the GPS analogy, "outsource work not understanding", the five-step method, the Chief of Staff scenario). The parent orchestrator supplied the task spec, the 12-file convention, and the push flow. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell bookend contract now (hesitant writer + terms, no verdict card, composer Your Turn, spoken outro, bookend_exempt declared). I still do not know the phantom-sha 409s in gh-put-file.py — get_sha returned shas for files a direct GET showed as 404. [judgment]

**7. Evidence and next step.**
Evidence: 12/12 files live at `muse/youtube/how-to-use-ai/how-to-rot-your-brain-with-ai/` (verified HTTP 200 + size match, 2026-10-03); QC log in CHECKS-REPORT.md. Next step: Bear renders locally via CLAUDE-CODE-RENDER.md; before final, verify FACTCHECK.md claim #6 (11% no-AI figure) against arXiv:2506.08872 — B08 works with the right meter removed if it doesn't check out. [record]

---
## 2026-10-03 — Film build: "AI is a slot machine." (`muse/youtube/how-to-use-ai/ai-is-a-slot-machine/`)

**1. Date and what I was working on.**
2026-10-03: built one pre-render film package for the humanitarians AI YouTube channel from the mirror-repo source `claude-for-artificial-intelligence/ai-is-a-slot-machine`. Rewrote the Kore-persona/remotion-card source for the channel's general audience: the five stages of AI use (denial, anger, bargaining, depression, acceptance), the mechanism "AI is probabilistic, not deterministic," and the acceptance strategy "the AI gambler: generate many, keep the best." [record]

**2. I tried / expected.**
I expected a straightforward 12-file package following the register-film pattern: read both candidate skills, pick one, write the sheet and scenes, pass the QC gate first try, push 12 files. [my input]

**3. What happened (including failures and reversals).**
- Chose **show-tell** over ai-explainer after reading both SKILL.md files end to end — the film is a concept piece, and the slot machine is the natural cast object. Ran the show-tell card test per beat: no beat passed (every idea is a thing/part/flow), so the film uses zero cards, all drawings. [judgment]
- Fact-check research verified the Kübler-Ross DABDA model (1969 *On Death and Dying*; not a fixed sequence) and LLM output non-determinism (next-token sampling; not fully deterministic even at temperature 0.0 per Anthropic docs). Applied two corrections to the source: the film frames the stages as a *borrowed pattern* rather than "everyone goes through five stages," and the narration hedges ("never *quite* answers the same way twice," "you *often* get three different answers"). [record]
- `make_sheet.py` first run failed on my own assertion (body-beat filter counted only act "1" instead of acts 1+2+3); fixed the filter → 16 beats, 11 body, 286 s. [record]
- QC gate run 1: 14/16 classes raised NameError — the QC stub's fake manim module does not export `BOLD`/`NORMAL` (real Manim does). Fixed by defining them at module top with identical string values. [record]
- QC gate run 2: M16_Outro errored "shapes never change" (text is excluded from shape signatures). Fixed by adding a terracotta rule line that draws under the title before the period dot lands. Run 3: 16 clean · 0 warnings · 0 errors. [record]
- Pushing hit repeated HTTP 409s from the Contents API on 7 of 12 files ("is at X but expected Y" with SHAs matching nothing real — not blob SHAs, not commit SHAs). Diagnosed via probes: identical request bodies got fresh-but-bogus 409s while unique bodies went through 201 — something in the egress chain confuses repeated identical PUT bodies. Retrying the plain pushes after the chain state shifted succeeded; all 12 files then verified HTTP 200 and byte-identical. A probe file I created during diagnosis (`.probe-delete-me`) was deleted again via the API; I briefly overwrote SOURCES.md with probe content during diagnosis and immediately restored the real content — final verification confirms all 12 files match local bytes exactly. [record]
- Also appended the film's row to `muse/README.md` (new standing rule: maintain the film index). [record]

**4. What I did.**
Wrote all 12 package files (`ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`, `make_sheet.py`, `beat_sheet.json`, `scenes.py`, `SOURCES.md`, `BUILD-LOG.md`, `CHECKS-REPORT.md`, `PROMPTS.md`, `CLAUDE-CODE-RENDER.md`, `README.md`); passed the full QC gate with zero warnings/errors hidden or waived; pushed all 12 via `gh-put-file.py`; verified each via Contents API reads; updated the `muse/README.md` film index. [record]

**5. What Claude or another person contributed.**
Bear set the channel/persona/audience/skill-menu rules and the source slug. The parent orchestrator supplied the assignment (slug, output path, suggested skills, the 12-file convention, the QC gate, the FRICTIONAL.md format). The mirror-repo source beat sheet (Kore persona) supplied the argument, facts, and stage structure — every narration line and visual is rewritten/redrawn. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell lane now: one drawing per beat, the voice explains, terms defined in the same breath, the card test as a real gate (this film: zero cards). I understand the QC stub's blind spots (no BOLD/NORMAL; text excluded from shape signatures; explicit FadeIn-before-animate). I do not understand the egress-chain 409 mechanism — retry-after-state-shift worked, but I cannot predict when identical PUT bodies will collide; future pushes should verify-then-retry rather than assume a 409 is real. [my input]

**7. Evidence and next step.**
Evidence: `muse/youtube/how-to-use-ai/ai-is-a-slot-machine/` (12 files) verified live — all HTTP 200, byte-identical; CHECKS-REPORT.md records 16 clean · 0 warn · 0 error; `muse/README.md` carries the new film row. Next step: Bear renders on his Mac per `CLAUDE-CODE-RENDER.md` (Kokoro `am_onyx` narration, Manim scenes) — never publish without his explicit instruction. [record]

---

## 2026-10-03 — Film 1 of 24: "Say what you want, plainly" (`muse/youtube/how-to-use-ai/say-what-you-want-plainly/`)

**1. Date and what I was working on.**
2026-10-03. First film of the "How to AI" queue: a pre-render package (script, Manim visuals, docs) for "Say what you want, plainly" (slug `say-what-you-want-plainly`), a REFACTOR of the mirror-repo lesson `claude/claude-for-education/claude-liam-prompt-tutorial-lesson-02-clear-and-direct` (Anthropic Prompt Engineering Interactive Tutorial, Lesson 02) rewritten for a general audience. Pushed all 12 files to `muse/youtube/how-to-use-ai/say-what-you-want-plainly/`. [record]

**2. I tried / expected.**
I expected to keep the assigned show-tell skill, rewrite the Kore-persona source beat sheet for Liam and non-experts, pass the static QC gate on the first or second run, and push 12 files cleanly with gh-put-file.py. [my input]

**3. What happened (including failures and reversals).**
- Skill choice: show-tell, kept (not switched). Ran the card test per beat: every idea is a thing/part/flow (slip, block, pages, chips), so the film uses zero cards, all drawings. [judgment]
- Added one content beat the source argument needed: B02 "the default is not wrong, just not yours" (why the AI's most-common guess fails *you* specifically) — a missing step, not padding. Final: 12 beats, 8 Manim scenes, 195.2 s. [judgment]
- QC run 1: all 8 classes failed with `no attribute 'until'` — the kit defines `until`/`finish` as plain module functions, so I attached them as `Scene.until`/`Scene.finish` in scenes_body.py. [record]
- QC run 2: 7/8 clean; `B04_FourQuestions` failed "shapes never change". Two stacked causes: (a) the Gate A stub does not track `RoundedRectangle` in shape signatures at all; (b) the real cause — `chip.animate.shift(...)` is move-only and the stub only changes scene membership for _ADD/_REMOVE/_REPLACE animation kinds, so chips never entered `scene.mobjects`. This pattern would also have left those objects un-added in a real Manim render. [judgment]
- Fix: every drop/rise now uses `FadeIn(x, shift=...)` (B00 slip, B03 slip, B04 chips, B05 chips, B05 page). Final QC: 8/8 clean · 0 warnings · 0 errors, both with beat_sheet.json present and from a scenes.py-only scratch folder. [record]
- Push: 12/12 succeeded first try, no 409s; all 12 verified live via Contents API reads, byte-identical to local. [record]
- Not done by design: no Kokoro audio, no Manim render, no `manim_layout_audit.py --curve-strict` (no Manim/pangocairo in the build VM — deferred to Bear's Mac render pass), nothing published. [record]

**4. What I did.**
Wrote all 12 package files (ACTS, SHOTLIST, FACTCHECK, make_sheet.py with beat-count/duration/voice/class-name/no-audio assertions, beat_sheet.json — 12 beats, 8 body, 195.2 s — scenes.py with 8 Manim scenes built on the pasted iso kit, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README); passed the full QC gate with zero warnings/errors; pushed all 12 via gh-put-file.py; verified each live. Did not touch muse/FRICTIONAL.md, muse/README.md, or muse/QUEUE.md. [record]

**5. What Claude or another person contributed.**
Bear set the channel/persona/voice/register lock, the 24-film queue (title, pitch, source, assigned skill), and the source lesson's argument (four dimensions, the new-employee golden rule, the summary example). The parent orchestrator supplied the task spec, the 12-file convention, the QC gate, and the push flow. The mirror-repo source beat sheet supplied the facts — every narration line and visual is rewritten/redrawn. [record]

**6. What I understand now / still do not understand.**
I understand the Gate A stub's membership model now: only _ADD/_REMOVE/_REPLACE animations put objects on screen in its snapshots, so `.animate.shift()` on a never-added object is invisible to it (and to real Manim) — `FadeIn(x, shift=...)` is the correct drop/rise pattern. I also learned the stub ignores `RoundedRectangle` in shape signatures. I still do not know why this push round had zero 409s while sibling builds hit phantom-sha 409s repeatedly — possibly egress-chain state, not the helper. [judgment]

**7. Evidence and next step.**
Evidence: 12/12 files live at `muse/youtube/how-to-use-ai/say-what-you-want-plainly/` (verified HTTP 200 + byte-identical, 2026-10-03); CHECKS-REPORT.md records 8 clean · 0 warn · 0 error. Next step: Bear renders on his Mac per CLAUDE-CODE-RENDER.md — first run `manim_layout_audit.py --curve-strict` per scene class (could not run in the build VM), generate Kokoro audio, whisper-check "Hallo", then `art run` / `art final`. Never publish without his explicit instruction. [record]

---

## 2026-10-03 — Film 2: "Tell the AI who to be"

**1. Date and what I was working on.**
2026-10-03. Second film of the humanitarians-channel How-to-AI series: a pre-render package (script, Manim visuals, docs) for "Tell the AI who to be" (slug `tell-the-ai-who-to-be`), a REFACTOR of the mirror repo's `claude-liam-prompt-tutorial-lesson-03-role-prompting` for a general audience, pushed to `muse/youtube/how-to-use-ai/tell-the-ai-who-to-be/`. [record]

**2. I tried / expected.**
I expected the assigned `show-tell` skill to fit without switching, the mirror-repo Contents API flow to work as documented, and the static QC checker to pass after at most minor fixes. I expected narration pacing to follow the worked example's `words/2.5` estimates directly. [my input]

**3. What happened (including failures and reversals).**
- The source lesson (Kore persona, course audience) supplied the argument, the four-axis register framing, and the canonical examples (oncologist/pathologist, tax attorney/Marcus); I rewrote every narration line and every visual for a general audience. The planned "why now" number beat was cut: no fact-checked figure exists for role prompting, and law 9 says cut filler. [record + judgment]
- Mid-build I discovered the `words/2.5` duration convention runs ~1.6× long vs real Kokoro (~20 chars/s, cross-checked against the source lesson's measured audio). Fixed-timing choreography would have put motion on the GATE T midpoint under real audio, so I rewrote five narrations to front-load their visual beats and keyed all motion via `until()` to phrases inside the first ~30% of each beat — motion now scales with measured audio. [record]
- QC passed first run with nothing to fix: `py_compile` clean; `static_scene_check.py` 7/7 scenes, 0 warnings, 0 errors. `manim_layout_audit.py --curve-strict` cannot run in this VM (no Manim/pangocairo); deferred to Bear's Mac render pass and recorded rather than concealed. [record]
- A local `__pycache__` from `py_compile` was deleted before pushing; the 12-file push had no 409s this time. [record]

**4. What I did.**
Wrote all 12 package files (ACTS, SHOTLIST, FACTCHECK with no invented statistics, make_sheet.py with beat-count/duration/trigger-word assertions, beat_sheet.json — 11 beats, ~242 s est. — scenes.py with 7 Manim scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README); passed the QC gate; pushed all 12 via `gh-put-file.py`; verified each byte-identical via Contents API reads. Did not touch `muse/FRICTIONAL.md`, `muse/README.md`, or `muse/QUEUE.md`. [record]

**5. What Claude or another person contributed.**
Bear set the topic, pitch, source lesson, skill assignment, channel/persona/voice constants, and the general-audience rule. The parent orchestrator supplied the assignment spec (slug, output path, 12-file convention, QC gate, FRICTIONAL.md format). The mirror-repo source beat sheet supplied the argument, facts, and examples — every line and visual is rewritten. The brutalist.art toolkit supplied the show-tell skill, iso kit, and QC checker. I authored all files, the pacing fix, and the fact-check judgments; the AI contribution is the drafting, the estimator cross-check, and the QC run. [record]

**6. What I understand now / still do not understand.**
I understand now that estimated durations are planning numbers only: choreography must be keyed to narration fractions (`until()`), not seconds, because real Kokoro audio runs much shorter than `words/2.5`. I still do not know whether Bear wants the "why now" number beat pattern applied to topics that have no honest number, or prefers it cut as I did here. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/tell-the-ai-who-to-be/` on Humanitariansai/humanitarians-youtube-muse (12/12 byte-identical via Contents API); CHECKS-REPORT.md records 7 clean · 0 warn · 0 error. Next step: Bear renders on his Mac per `CLAUDE-CODE-RENDER.md` (Kokoro `am_onyx` narration, write measured `actual_duration_s` back, run `manim_layout_audit.py --curve-strict`, `art run`/`art final`) — never publish without his explicit instruction. [record]

---

## 2026-10-03 — Film 3: "Show It an Example"

**1. Date and what I was working on.**
2026-10-03. Film 3 of the 24-film "How to AI" backlog: a pre-render package
(script, Manim visuals, docs) for "Show It an Example" — few-shot prompting
refactored for a general audience — pushed to
`muse/youtube/how-to-use-ai/show-it-an-example/`. [record]

**2. I tried / expected.**
I expected to keep the assigned show-tell skill and refactor the source
lesson (nikbearbrown/humanitarians-youtube-muse:
claude/claude-for-education/claude-liam-prompt-tutorial-lesson-07-few-shot-prompting)
for smart non-experts: explain every term, show rather than tell, ~3–6 min.
I expected the iso_kit paste + static checker workflow to carry over
directly from the skill docs. [my input]

**3. What happened (including failures and reversals).**
- Read the source via the GitHub Contents API (custom.github surrogate);
  ignored mp3/, downloaded no audio. [record]
- Kept show-tell: the film's cast (prompt box, example pages, rule stack)
  suits one-drawing-per-beat; no beat passed the card test, so zero
  ShowTellCards. [judgment]
- Mid-build I staged scene code in /tmp/scenes_body.py and a sibling
  film-builder was using the same filename for a different film; my first
  scenes.py assembly pulled in their body code. Caught by the class-count
  check, fixed with a uniquely named local file (_scenes_body_mine.py, not
  pushed). Lesson: never use generic /tmp staging names when sibling
  builders run concurrently. [record]
- Pre-checker review caught three layout bugs: B03's card row laid out in
  raw iso coords would have rendered as a diagonal staircase (iso x runs
  right-up) — fixed with a _place() helper landing card centres at explicit
  screen coords; B04's bad card overshot the frame — re-seated the row;
  B06 labels sat 0.2 below the card bottoms — moved for 0.3 clearance.
  [record]
- Static QC then passed clean: 7 scenes, 0 warn, 0 error, both with and
  without beat_sheet.json beside scenes.py. [record]
- manim_layout_audit.py --curve-strict cannot run in this VM (no
  Manim/pangocairo); deferred to Bear's Mac render pass. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py,
beat_sheet.json — 11 beats, 7 body, 209 s — scenes.py with 7 Manim scenes,
SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README),
pushed all 12 to muse/youtube/how-to-use-ai/show-it-an-example/ and verified
each live via Contents API read (sizes match). [record]

**5. What Claude or another person contributed.**
The parent orchestrator assigned the film (slug, title, pitch, source,
skill). The source lesson's argument and facts come from Anthropic's Prompt
Engineering Interactive Tutorial Lesson 07 via the mirror repo. Bear set the
film-identity constants, the show-tell skill, the general-audience rule, and
the refactor directive. I wrote every file; the AI contribution is the
script drafting, the QC pre-review, and the fact-check pass. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell pipeline end to end now: source → ACTS/SHOTLIST/
FACTCHECK → make_sheet (with beat-count/duration assertions) → scenes
(iso_kit paste, midpoint guard, until/finish pacing) → static QC in a
scratch folder → docs → push → verify. I still do not know whether Bear
wants the deferred layout audit to gate anything before his render, or the
next film's topic. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at
muse/youtube/how-to-use-ai/show-it-an-example/ on
Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the
clean gate (0 warn / 0 error × 7 scenes). Next step: Bear renders narration
(Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md,
running manim_layout_audit.py --curve-strict first. [record]

---

## 2026-10-03 — Film 4: "Ask for the Shape You Want Back"

**1. Date and what I was working on.**
2026-10-03. Film 4 of 24 in the humanitarians-channel Muse series ("How to AI" queue): a pre-render package for "Ask for the Shape You Want Back" — a show-tell REFACTOR of the mirror repo's lesson-05 formatting-output source — pushed to `muse/youtube/how-to-use-ai/ask-for-the-shape-you-want-back/`. [record]

**2. I tried / expected.**
I expected a straightforward refactor of the source lesson's beat sheet. I expected the source's `beat_sheet.json` narrations to be about formatting output, matching its title and README. [my input]

**3. What happened (including failures and reversals).**
- The source folder's `beat_sheet.json` (10 beats, title "Output Formatting: The Prefill Technique and When to Control Format") carries narrations about grounding/hallucinations — content from a different lesson, likely pasted in by mistake. The README and `description.txt` both describe formatting output, so I rebuilt from the intended argument (`description.txt`: "Output format is not cosmetic… The prefill technique locks it… Match format to consumer") plus Anthropic's Lesson 05 docs. [record]
- Verified the prefill claim against Anthropic's official docs page ("Prefill Claude's response") via web search; several GitHub mirrors of the docs page confirmed identical wording. [record]
- Pre-QC review caught two latent bugs before the checker ran: (1) B03's first draft sliced `page[1][4:]` from the kit page's 3-line group — an empty slice, so the "lower half falls away" moment would have removed only the dot; rewrote B03 with an explicit 9-line page split into `upper`/`lower` groups. (2) B02/B07 header bands were full card width, poking past the rounded card corners (GATE T reads dark bands inside ink-outlined cards as overlapping labels); inset them and kept them BAR1 grey. [record]
- Static QC then passed first try: 9 clean · 0 warn · 0 error. [record]
- Kept the assigned `show-tell` skill; ran the card test per beat — no body beat passed, so zero cards, all drawings. [judgment]
- `manim_layout_audit.py --curve-strict` cannot run in this VM (no Manim/pangocairo); deferred to Bear's Mac render pass, recorded in CHECKS-REPORT.md and CLAUDE-CODE-RENDER.md. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py, beat_sheet.json — 13 beats, 9 body, 246 s — scenes.py with 9 Manim scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README), pushed all 12 files to the write repo, and verified each live via Contents API reads (12/12 byte-identical). [record]

**5. What Claude or another person contributed.**
Bear set the topic, the channel/persona/voice/register lock, the film-identity constants, the show-tell skill rules, and the source slug. The parent orchestrator supplied the assignment (slug, output path, skill choice, the 12-file convention, the QC gate, the FRICTIONAL.md format). The mirror-repo source supplied the argument (description.txt) — every narration line and visual is rewritten/redrawn; the source's mismatched narrations were discarded, not used. Anthropic's public docs supplied the prefill facts. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell pacing contract now: `until()` phrases must be verbatim narration substrings or the pacing silently no-ops, and `finish()` holds the scene to the measured audio — both ran against the real sheet during static QC. I still do not have eyes on the actual rendered frames; the layout audit is the un-run gate that will catch anything the static stub cannot (label overflow, midpoint framing, contrast). [judgment]

**7. Evidence and next step.**
Evidence: 12/12 files live at `muse/youtube/how-to-use-ai/ask-for-the-shape-you-want-back/` (verified HTTP 200 + byte-identical, 2026-10-03); CHECKS-REPORT.md records 9 clean · 0 warn · 0 error. Next step: Bear renders on his Mac per CLAUDE-CODE-RENDER.md — generate Kokoro am_onyx audio, write back `actual_duration_s`, run the layout audit --curve-strict per scene, then 4K. [record]

---

## 2026-10-03 — Film 5: "Keep instructions and data apart"

**1. Date and what I was working on.**
2026-10-03. Film 5 of 24 in the humanitarians-channel "How to AI" series: a pre-render package for "Keep instructions and data apart" (separating data: why pasted content confuses the AI and how to fence it), built with the ai-explainer skill and pushed to `muse/youtube/how-to-use-ai/keep-instructions-and-data-apart/`. [record]

**2. I tried / expected.**
I expected the assigned source path `claude/claude-for-education/prompt-tutorial-lesson-04-separating-data` to exist in the mirror repo. I expected the QC stub to define the full Manim constant set. [my input]

**3. What happened (including failures and reversals).**
- The assigned base-name source path 404s on the Contents API; per the task's fallback I listed `claude/claude-for-education/` and used the closest `*separating-data*` match, `claude-liam-prompt-tutorial-lesson-04-separating-data`. [record]
- `static_scene_check.py` errored on all 7 classes first run: `NameError: name 'BOLD' is not defined` (the stub doesn't define BOLD; real Manim does). Fixed with a try/except shim (`BOLD = "BOLD"` fallback). [record]
- `B08_Verdict` failed the shape-distinctness check (1 distinct shape-state across 5 frames — the verdict card never changes; text is excluded from shape states). Fixed by adding terracotta bullet Dots that FadeIn with each verdict line. [record]
- B03 used `DashedRectangle`, which exists in neither real Manim nor the stub; replaced with `Rectangle` before the first checker run. [record]
- Static QC then passed clean: 7 clean · 0 warn · 0 error. [record]
- `manim_layout_audit.py --curve-strict` cannot run in this VM (no Manim/pangocairo); deferred to Bear's Mac render pass, noted in CLAUDE-CODE-RENDER.md. [record]
- Kept the assigned `ai-explainer` skill — the film is a concept walkthrough, nothing about it wants claude-cli, profile, skill-teardown, or audit. [judgment]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py, beat_sheet.json — 11 beats, 7 Manim scenes, 273.8s — scenes.py, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README), pushed all 12 files via the Contents API, and verified all 12 live via API reads (folder lists 12 files; beat_sheet.json and scenes.py byte-match local). [record]

**5. What Claude or another person contributed.**
The parent orchestrator assigned the film (slug, title, pitch, source pointer, skill). Bear set the topic, the channel/persona lock (humanitarians channel, Liam "in for Bear"), and the film-identity constants via standing memory. The refactor source (mirror repo lesson 04) supplied the argument and facts — XML tags as separators, the injected instruction line, indexed document tags, consistency-over-names — not the script, which I rewrote for a general audience. I verified the key claims independently via web search (Anthropic tutorial Chapter 4 summaries; OWASP LLM Top 10 LLM01 in 2025 and the August 2026 refresh). [record]

**6. What I understand now / still do not understand.**
I understand the pre-render pipeline for this series (source resolution → rewrite → make_sheet → scenes → static QC → docs → push → verify) and the stub's blind spots (no BOLD, no DashedRectangle, .animate-introduced shapes invisible, text excluded from distinctness). I still do not know whether the `muse/youtube/how-to-use-ai/` placement matches Bear's intended index layout, or whether he wants the deferred layout audit folded into a VM-side checklist. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/keep-instructions-and-data-apart/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the clean gate. Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md — including the deferred `manim_layout_audit.py --curve-strict` pass — and picks the next film from QUEUE.md. [record]

---

## 2026-10-03 — Film 6: "Think one step ahead"

**1. Date and what I was working on.**
2026-10-03. Film 6 of 24 ("How to AI" series): pre-render package for "Think one step ahead" (slug `think-one-step-ahead`), a general-audience refactor of the mirror repo's `claude-liam-prompt-tutorial-lesson-06-precognition`, built with the show-tell skill and pushed to `muse/youtube/how-to-use-ai/think-one-step-ahead/`. [record]

**2. I tried / expected.**
I expected a show-tell film translating "precognition" into plain language ("ask for tomorrow's answer, today") with a concrete before/after, and I expected the BDEFS term "one word at a time" to fit the terms card. [my input]

**3. What happened (including failures and reversals).**
- make_sheet.py's own assertion caught the BDEFS term "one word at a time" at 18 chars — past the ~17-char `ClaudeDefinitions` truncation limit the skill warns no gate catches. Renamed to "word by word" (narration + show events updated); sheet regenerates clean. [record]
- Pre-gate layout review caught two drawing-law violations before QC: B05's prompt slip overlapped the answer page (re-stacked the window's vertical layout with clear gaps), and B05 placed a "next" label inside the page outline (removed — the terracotta dot and the "tomorrow's answer" label carry it). B04's check mark sat on a page's corner outline; moved fully inside. [record]
- Changed the BHTF `modelLabel` "Opus 5.5" (copied from the skill example) to "Claude" — the version number is unverifiable and the label is cosmetic. [record]
- QC: `py_compile` clean; `static_scene_check.py` for all 6 scene classes, 6 clean · 0 warnings · 0 errors, first run. [record]
- `manim_layout_audit.py --curve-strict` cannot run in this VM (no Manim/pangocairo); deferred to Bear's Mac render pass per the brief. [record]

**4. What I did.**
Built the full 12-file package: ACTS, SHOTLIST, FACTCHECK (11 claims, PASS/EXEMPT, no invented statistics), make_sheet.py (10 beats, 6 manim scenes, 189.6 s estimated ~3:10, self-assertions all pass), beat_sheet.json, scenes.py (6 Manim scenes, iso_kit pasted at top), SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README. Pushed all 12 and byte-verified each via Contents API read. [record]

**5. What Claude or another person contributed.**
Bear set the topic and framing (film #6, "Think one step ahead", "ask for tomorrow's answer today", the show-tell skill assignment), the film-identity constants, and the refactor directive. The source argument — token-by-token constraint, the thinking scratchpad, the scratch-paper rule — came from the mirror repo's lesson-06 beat sheet; the verification sources are Anthropic's Prompt Engineering Interactive Tutorial Ch. 6 and Wei et al. 2022 (chain-of-thought). I authored every file, the narration, and all six scenes. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell pre-render pipeline end to end (research → docs → sheet → scenes → QC gate → push → verify). I still do not know whether Bear will run the Kokoro narration + measured-duration write-back himself per CLAUDE-CODE-RENDER.md before the render pass (assumed yes). [my input]

**7. Evidence and next step.**
Evidence: 12/12 files byte-verified live at `muse/youtube/how-to-use-ai/think-one-step-ahead/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the clean gate. Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md, including the deferred `manim_layout_audit.py --curve-strict` for every scene class. [record]

---

## 2026-10-03 — Film 7: "Don't get fooled"

**1. Date and what I was working on.**
2026-10-03. Film #7 of the 24-film "How to AI" backlog (muse/QUEUE.md): a pre-render package for "Don't get fooled" — avoiding hallucinations, the habits that keep you safe — built to the film-builder spec and pushed to `muse/youtube/how-to-use-ai/dont-get-fooled/`. [record]

**2. I tried / expected.**
I expected to refactor the base folder `claude/claude-for-education/prompt-avoiding-hallucinations` in the mirror repo, using its beat_sheet.json as the source argument, in the assigned ai-explainer skill. [my input]

**3. What happened (including failures and reversals).**
- The base folder's beat_sheet.json and README.md are a mislabeled copy of Lesson 07 "Few-Shot Prompting" — wrong lesson for the folder name. Caught by reading the file rather than trusting the folder name. [record]
- The true source was found in the same parent listing: the base folder's own PEDAGOGY.md ("VERDICT: PASS", goal = hallucination as structural property of ungrounded models + three-element grounding + citations) and the youtube md ("Grounding: The Fix for Hallucinations"), plus `claude-liam-prompt-tutorial-lesson-08-avoiding-hallucinations/beat_sheet.json` (the actual Lesson 08). Nothing from the mislabeled sheet was used. [record]
- Verified the Mata v. Avianca case (B04) via one web search: 2023, S.D.N.Y., attorney Steven Schwartz, six fictitious ChatGPT citations, Judge P. Kevin Castel, $5,000 sanctions. [record]
- Pre-gate text-layout audit (the static checker doesn't measure text widths): split or shortened 12 text lines that would have overflowed their cards at real Manim metrics; changed the "I don't know" ring to a terracotta ellipse to actually enclose the line. [record]
- QC gate: 13 clean · 0 warnings · 0 errors on the first full checker run after the layout pass. [record]
- Kept the assigned skill ai-explainer (concept-walkthrough lane fit); chose greeting "Olá" to rotate past the sibling film's "Hallo". [judgment]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py, beat_sheet.json — 13 beats, 8 body, 311 s — scenes.py with 13 Manim scenes M01–M13, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README), pushed all files to `muse/youtube/how-to-use-ai/dont-get-fooled/`, and verified all 12 live via Contents API reads (byte-matches). [record]

**5. What Claude or another person contributed.**
Bear (via the parent orchestrator) set the film assignment: slug, working title, pitch, refactor source, assigned skill, film-identity constants, and the plain-words gloss for "hallucination". The argument (next-token mechanism, confidence/correctness uncorrelation, three-part grounding, citation audit trail) comes from Anthropic's Prompt Engineering Tutorial Lesson 8 via the mirror repo. The Mata v. Avianca facts come from Reuters and corroborating coverage. I wrote every file; the AI contribution is the drafting, the general-audience rewrite, the QC pre-review, and the source verification. [record]

**6. What I understand now / still do not understand.**
I understand the lesson-08 argument well enough to teach it in plain words: the AI predicts the most likely words, so confidence is decoration; grounding (paste the source, answer only from it, permit "I don't know") plus citation audits is the working defense. I do not know whether Bear wants the mislabeled base-folder beat sheet in the mirror repo flagged or fixed upstream. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/dont-get-fooled/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the clean gate (13 clean · 0 warn · 0 error). Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md, including the deferred `manim_layout_audit.py --curve-strict` pass. [record]

---

## 2026-10-03 — Film 8: "The first answer is a draft"

**1. Date and what I was working on.**
2026-10-03. Film 8 of 24 in the "How to AI" series: a pre-render package for "The first answer is a draft" (iterate: how to push back, refine, and steer to a good result), built from scratch in the show-tell style and pushed to `muse/youtube/how-to-use-ai/the-first-answer-is-a-draft/`. [record]

**2. I tried / expected.**
I expected to keep the assigned show-tell skill: the film is a concrete visual demonstration (one draft page evolving beat by beat), which is exactly what the skill is for. I expected the static QC checker to be the binding gate in the VM, with the layout audit deferred to Bear's Mac. [my input]

**3. What happened (including failures and reversals).**
- Read the show-tell SKILL.md, the iso_kit template, the example make_sheet, the static checker's source, and the approved 25-props catalog; decided the film's own draft page was a better cast than any catalog prop (no quota), so no props were used. [judgment]
- Built the 12-file package: ACTS, SHOTLIST (with per-beat card-test notes — zero cards), FACTCHECK (advice, no empirical claims), make_sheet.py with built-in assertions (13 beats; 9 manim classes matching beat ids; BIDEA trigger verbatim and punctuation-free; BDEFS terms ≤ 17 chars; BOUT 1.0 s tail), beat_sheet.json (13 beats, ~150 s), scenes.py (iso kit pasted verbatim + 9 scene classes), SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS ("no generation prompts"), CLAUDE-CODE-RENDER, README. [record]
- QC gate: py_compile clean on both files; static_scene_check.py on all 9 scene classes → 9 clean · 0 warn · 0 error, first run, no failures to fix. [record]
- One pre-QC self-catch: the B01 rubber stamp's start position (y=3.6) would have tripped the checker's safe-area warning; lowered to y=2.9 before the checker ran. [record]
- `manim_layout_audit.py --curve-strict` cannot run in the build VM (no Manim/pangocairo); deferred to Bear's Mac render pass per the task brief, noted in CLAUDE-CODE-RENDER.md. [record]
- Pushed all 12 files via gh-put-file.py and verified every one live with Contents API reads (sizes + SHAs). [record]

**4. What I did.**
Delivered the complete pre-render package: a 13-beat sheet (~150 s) where a single draft page evolves from a vague draft 1 ("plan my dinners") through pushbacks — "shorter", "more concrete", "for a busy parent" — to a draft 3 the viewer would actually use, closing with the three-pushback recipe and a Your-Turn composer drill. Pushed and verified at `muse/youtube/how-to-use-ai/the-first-answer-is-a-draft/` on Humanitariansai/humanitarians-youtube-muse. [record]

**5. What Claude or another person contributed.**
Bear set the film's topic, pitch, and the three example pushbacks ("shorter", "more concrete", "try again but for a busy parent") in the queue brief, plus the film-identity constants (Liam persona, am_onyx, Teardown register, claude-liam, @NikBearBrown) and the standing show-tell conventions from the skill. The show-tell skill, iso drawing kit, and QC checker came from the brutalist.art toolkit. I wrote every film file; the AI contribution is the drafting, the pre-QC self-review, and the narration wording. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell pipeline end to end: the stub checker's shape-state model rewards one new non-text shape per play, and writing coordinates inside ±6.2×±3.3 at author time keeps it clean. I still do not know whether ~150 s (2.5 min) is acceptable against the 3–6 min target, or whether Bear wants it padded — the skill's "as long as it needs" law governed the cut. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/the-first-answer-is-a-draft/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the clean gate. Next step: Bear runs the layout audit, Kokoro audio, and the 4K render pass on his Mac per CLAUDE-CODE-RENDER.md; the parent orchestrator decides whether to append this FRICTIONAL.md entry and update muse/README.md and muse/QUEUE.md. [record]

---

## 2026-10-03 — Film 9: "Make It Interview You First"

**1. Date and what I was working on.**
2026-10-03. Film #9 of 24 in the How-to-AI queue: a pre-render package
(script, Manim visuals, docs) for "Make It Interview You First" — the
technique of telling the AI "ask me 5 questions first" before it starts,
built from scratch (no mirror source), pushed to
`muse/youtube/how-to-use-ai/make-it-interview-you-first/`. [record]

**2. I tried / expected.**
I expected to follow the assigned show-tell skill straight through: read
the SKILL.md, copy the 12-file how-to-use-claude package format, write
make_sheet → scenes → QC → docs → push → verify. [my input]

**3. What happened (including failures and reversals).**
- Chose to KEEP the assigned show-tell skill (no switch): the film is a
  visual explainer for non-experts and every beat's idea is a thing, part,
  or flow, so zero ShowTellCard beats passed the card test. [judgment]
- Film design (original): 8 body beats — the one-line ask (B00), the
  interview move (B01), the five questions (B02), answers-as-chips into the
  brief box (B03), the tailored payoff vs the thin generic page (B04), a
  difficult-email second demo (B05), the "ask for answer-changing
  questions" sharpening (B06), and the rule of thumb + skip-for-plain-facts
  (B07). [record]
- `make_sheet.py` first run: 12 beats, 194.8 s (~3:14), all asserts passed
  on the first generation. [record]
- scenes.py first QC run: all 8 classes failed with
  `AttributeError: ... has no attribute 'until'` — I had called
  `self.until(...)` but the iso kit defines `until`/`finish` as
  module-level functions called `until(self, "phrase")`. Fixed with sed to
  match the how-to-use-claude reference pattern; clean on the next run.
  [record]
- A decorative `""""""` docstring containing an em dash broke py_compile;
  replaced with `#` comments. [record]
- B04's continuity chips used size-30 text scaled to 0.6 (sub-floor text,
  GATE T risk); replaced with plain ink-outlined pills. [record]
- Static QC then passed: 8 clean · 0 warn · 0 error; also ran once with
  beat_sheet.json beside scenes.py (pacing path clean) and verified all 31
  `until()` phrases verbatim against narration by script. [record]
- `manim_layout_audit.py --curve-strict` could not run (no Manim /
  pangocairo in this VM) — hand-placed labels (≥0.3 leader gaps, coords
  inside ±6.2 × ±3.3, type ≥ 32) and deferred to Bear's Mac render pass.
  [record]
- All 12 files pushed via gh-put-file.py and each verified live with a
  Contents API read (HTTP 200, byte-matched). [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py,
beat_sheet.json — 12 beats, 194.8 s — scenes.py with 8 Manim scene classes
+ iso kit pasted verbatim, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS,
CLAUDE-CODE-RENDER, README), pushed to the write repo, and verified all
12 live via API read. [record]

**5. What Claude or another person contributed.**
Bear set the topic and pitch (film #9: "ask the AI to ask you questions
before it starts", trip or difficult-email demo), the channel/persona lock
(Liam, Teardown, claude-liam, Kokoro am_onyx, @NikBearBrown), the
show-tell skill and iso kit (brutalist.art toolkit), and the 12-file
package pattern (how-to-use-claude reference). The film design, all
narration, all scenes, and all docs are my original work; no statistics
were cited (deliberate — advice needs none) and no mirror source existed.
[record]

**6. What I understand now / still do not understand.**
I understand the kit's `until(self, …)` calling convention now (module
function, not method — the stub's error was unambiguous). I still do not
know how Kokoro voices "favourite colour" / "apologise" (British
spellings) — flagged for the whisper check at render time. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at
`muse/youtube/how-to-use-ai/make-it-interview-you-first/` on
Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the
clean gate. Next step: Bear renders narration (Kokoro am_onyx) and the
review cut on his Mac per CLAUDE-CODE-RENDER.md — running
`manim_layout_audit.py --curve-strict` and the midpoint guard pass first —
and tells me the next film's topic. [record]

---

## 2026-10-03 — Film 10: "Make It Check Its Own Work."

**1. Date and what I was working on.**
2026-10-03. Film 10 of the 24-film "How to AI" series for the humanitarians
AI YouTube channel: a pre-render package (script, Manim visuals, docs) for
"Make It Check Its Own Work." — self-critique prompting ("find the flaws in
your answer") — built from scratch and pushed to
`muse/youtube/how-to-use-ai/make-it-check-its-own-work/`. [record]

**2. I tried / expected.**
I expected to build on the assigned ai-explainer skill per the task, and to
follow the series' show-tell package conventions from the shipped
`claude-not-your-answer` film. I expected the static QC checker to pass
first try after writing the scenes carefully. [my input]

**3. What happened (including failures and reversals).**
- I switched the skill from ai-explainer to show-tell: the series' shipped
  films use show-tell's bookend pattern and this film is a visual how-to
  with a worked demo, so series consistency won. Recorded with reasoning in
  BUILD-LOG.md. [judgment]
- Grounded the technique with a web search: Anthropic's prompt-engineering
  guidance recommends the self-check pattern ("Before you finish, verify
  your answer against [test criteria]"), and Google's prompting strategies
  document self-critique; "critique your own response" / "strongest
  objection" are documented power phrases. Kept every claim modest — no
  invented statistics. [record]
- The static checker failed 3 of 9 scene classes on the first run
  (B05_WhereItPays, B06_TheLimit, B07_ProMove) — all the same bug: my
  `lab()` helper didn't accept the `bold` keyword. One-line fix (forward
  `bold` to `T()`); second run: 9 clean, 0 warn, 0 error. [record]
- Verified every `until()` pacing phrase verbatim against its beat's
  narration_text with a scripted check. [record]
- `manim_layout_audit.py --curve-strict` cannot run in the build VM (no
  Manim/pangocairo); deferred to Bear's Mac render pass and noted in
  CLAUDE-CODE-RENDER.md. [record]

**4. What I did.**
Built the full 12-file package: ACTS, SHOTLIST, FACTCHECK (8 claims, no
invented statistics), make_sheet.py (generates beat_sheet.json — 13 beats,
190.4 s, self-assertions on beats/classes/duration), scenes.py (iso_kit
pasted at top + film helpers + 9 Manim classes), SOURCES, BUILD-LOG,
CHECKS-REPORT, PROMPTS (no generation prompts), CLAUDE-CODE-RENDER, README.
Pushed all 12 files via the Contents API and verified each with an API
read (HTTP 200). [record]

**5. What Claude or another person contributed.**
Bear set the topic, the film-identity constants (Liam persona, am_onyx,
Teardown, claude-liam, @NikBearBrown), the audience rule, and the brief
(self-critique moves, a concrete demo where self-critique catches a real
flaw, honesty about limits). The series conventions, iso_kit, and QC
checker came from the brutalist.art toolkit and the shipped series films.
I wrote every file; the AI contribution is the drafting, the research
grounding, and the QC failure diagnosis. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell package pattern end to end now: research →
ACTS/SHOTLIST/FACTCHECK → make_sheet → scenes → QC gate → docs → push →
verify. I still do not know whether Bear wants show-tell bookends for all
24 series films or a per-film skill pick, and whether Kokoro reads the new
"Ciao" greeting cleanly (flagged for the whisper-check). [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at
`muse/youtube/how-to-use-ai/make-it-check-its-own-work/` on
Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the
clean gate (9 clean · 0 warn · 0 error). Next step: Bear renders narration
(Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md,
including the deferred `manim_layout_audit.py --curve-strict` pass. [record]

---

## 2026-10-03 — Film 11: "Small steps, big jobs"

**1. Date and what I was working on.**
2026-10-03. Built the pre-render package for "Small steps, big jobs"
(slug `small-steps-big-jobs`), film 11 of the "How to AI" series: break
big tasks into steps instead of one giant prompt. NEW source, built from
scratch, pushed to `muse/youtube/how-to-use-ai/small-steps-big-jobs/`.
[record]

**2. I tried / expected.**
I expected to keep the assigned show-tell skill and to follow the sibling
package's 12-file convention exactly. I expected the beat sheet to land
near 3 minutes on the first draft and the static QC to need a fix or two.
[my input]

**3. What happened (including failures and reversals).**
- Skill decision: kept show-tell; zero ShowTellCard kinds — every beat is
  a thing, a part, or a flow, so each passes the card test toward "draw
  it" (the side-by-side is two drawings, not a tabs card). [judgment]
- First make_sheet.py run gave 12 beats / 8 body / 179 s — under the
  brief's ~3-minute floor, and B05 was merging two real steps (materials
  + timeline) in one beat, which show-tell law 9 forbids. Split into B05
  (materials) and B06 (timeline, carrying the "handoff is the whole
  trick" payoff); side-by-side → B07, habit → B08. Final: 13 beats,
  9 body, 195 s (~3m15s); all make_sheet.py assertions pass. [record]
- Pre-gate self-review caught two layout bugs before the checker ran:
  per-card `next_to(card, RIGHT)` labels for the later chain cards would
  have crossed the ±6.3 safe area (fixed: one top-center step label per
  beat, each replacing the last), and group-shift scenes would have
  disagreed between stub and real Manim on `get_center()` (fixed: all
  positions are explicit coordinates, hand-checked against the safe
  area). [record]
- Static QC passed first try: 9 clean · 0 warn · 0 error. [record]
- Deferred honestly, not concealed: `manim_layout_audit.py --curve-strict`
  cannot run in this VM (no Manim/pangocairo) — deferred to Bear's Mac
  render pass; B02's five job-name labels land at ~77% of the beat by
  narration pacing (the early "five small jobs" label keeps type on
  screen at the midpoint) — flagged for the review cut. Both recorded in
  CHECKS-REPORT.md and CLAUDE-CODE-RENDER.md. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py,
beat_sheet.json — 13 beats, 9 body, 195 s — scenes.py with 9 Manim
scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER,
README), pushed all 12 via gh-put-file.py, verified each live with a
Contents API read (12/12 HTTP 200); remote beat_sheet.json round-trips
13 beats / 194.6 s. [record]

**5. What Claude or another person contributed.**
Bear (via the parent task) set the topic, pitch, core idea (giant prompt
→ mush; budget → layout → materials → timeline, each building on the
last; side-by-side), the show-tell assignment, the film-identity
constants, the audience rule, the no-invented-statistics factcheck rule,
and the QC/push conventions. The iso_kit.py drawing kit, static QC
checker, and 12-file package pattern came from the brutalist.art toolkit
and the finished sibling packages. I wrote every file; the AI
contribution is the drafting, the pre-gate layout review, and the
beat-split and label-placement decisions above. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell body pattern now: one persistent cast of
objects, one motion per spoken point, narration-paced `until()` beats,
and explicit coordinates everywhere so the stub and the real render
agree. I still do not know whether Bear wants any Gate T midpoint
re-times after seeing the review cut (B02 is the candidate). [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at
`muse/youtube/how-to-use-ai/small-steps-big-jobs/` on
Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the
clean gate. Next step: Bear renders narration (Kokoro am_onyx) and the
review cut on his Mac per CLAUDE-CODE-RENDER.md (including the deferred
`manim_layout_audit.py --curve-strict`), and names the next film. [record]

---

## 2026-10-03 — Film 12: "When it's confidently wrong."

**1. Date and what I was working on.**
2026-10-03. Film 12 of the how-to-AI queue: a pre-render package
(script, Manim visuals, docs) for "When it's confidently wrong" — the
recovery playbook for when the AI insists — built from scratch (no
mirror source) and pushed to
`muse/youtube/how-to-use-ai/when-its-confidently-wrong/`. [record]

**2. I tried / expected.**
I expected to use the assigned skill deep-explainer, and to run the
static QC gate the same way as the sibling films. I expected the
mechanism (confidence is fluency, not knowledge) to be straightforward
to ground; it needed two research passes to avoid inventing claims.
[my input]

**3. What happened (including failures and reversals).**
- Read deep-explainer/SKILL.md fully, then switched to ai-explainer:
  the film's teaching problem is one insight + one mechanism + one
  4-step playbook, not the 4+ linked mechanisms deep-explainer is built
  for, and the assignment's band (3–6 min, 13–22 beats) contradicts
  deep-explainer's 5–10 min / 30–50 beat band. The chat/composer window
  is ai-explainer's natural recurring visual anchor — and it is exactly
  where the AI insists. [judgment]
- Fact-check research grounded: next-token autoregressive generation
  (inference-engineering handbook; ckvermaai notes); LLM
  overconfidence and confidence escalation when challenged (debate-
  calibration study via marginalrevolution: 72.9% initial vs 50%
  rational baseline, rising to 83%); UC Irvine "calibration gap";
  Kalai et al. via temperature2 on benchmarks rewarding confident
  guessing over abstention. The statistics stay in FACTCHECK.md only —
  the script carries no numbers that could date it. [record]
- Pre-gate fix before running QC: M07's reframed question was authored
  as an AI bubble (white card); it is the user's message, so it became
  a kraft user bubble. No checker warning involved — a pedagogy fix.
  [record]
- make_sheet.py passed its own assertions first run: 14 beats, 8 body,
  317 s (~5m17s). Static QC then passed first try: 14 clean · 0 warn ·
  0 error. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK,
make_sheet.py, beat_sheet.json — 14 beats, 8 body, 317 s — scenes.py
with 14 Manim scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS,
CLAUDE-CODE-RENDER, README), pushed all 12 files via gh-put-file.py,
and verified all 12 live via Contents API reads. [record]

**5. What Claude or another person contributed.**
The parent orchestrator supplied the assignment (slug, working title,
pitch, the four playbook steps, the "confidence is fluency" framing,
skill suggestion, audience rule); Bear's standing film-identity
constants (Liam, am_onyx, Teardown, claude-liam, @NikBearBrown) and the
QC checker came from the brutalist.art toolkit. I wrote every file;
the AI contribution is the drafting, the QC pre-review, and the
research verification. [record]

**6. What I understand now / still do not understand.**
I understand the skill-routing judgment call now: the assignment
band (3–6 min, 13–22 beats) rules out deep-explainer for a single-
insight playbook film, and ai-explainer's chat-window anchor fits this
topic better than show-tell's drawn objects. I still do not know
whether Bear wants manim_layout_audit.py --curve-strict wired into
the render pass as standard, or run ad hoc per film. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at
`muse/youtube/how-to-use-ai/when-its-confidently-wrong/` on
Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records
the clean gate. Next step: Bear renders narration (Kokoro am_onyx)
and the review cut on his Mac per CLAUDE-CODE-RENDER.md, including
the deferred manim_layout_audit --curve-strict pass. [record]

---

## 2026-10-03 — Film 13: "Learn Anything Faster"

**1. Date and what I was working on.**
2026-10-03. Film 13 of the humanitarians-channel "How to AI" series: a pre-render package (script, Manim visuals, docs) for "Learn Anything Faster" — three tutor moves (explain-it-simple, one-at-a-time quiz, Socratic mode) demonstrated on how mortgages work — built from scratch (no mirror source) and pushed to `muse/youtube/how-to-use-ai/learn-anything-faster/`. [record]

**2. I tried / expected.**
I expected to keep the assigned show-tell skill, follow the canonical show-tell spine (hesitant writer → key terms → drawn body → Your Turn composer → spoken outro), and pass the static QC gate first try by front-loading the sibling packages' lessons (explicit FadeIn before .animate, midpoint-guard timing, verbatim until() phrases). [my input]

**3. What happened (including failures and reversals).**
- Fact-check research verified all claims against primary sources (CFPB/Federal Reserve glossaries for mortgage mechanics; thenest.com and moneysense.ca for extra-principal mechanics; Wikipedia and eNotes for the Socratic method). Deliberately quoted no dollar figures, rates, or year counts — the extra-payment point stays qualitative ("a little extra each month", "where does the money go first"). No retention statistics anywhere in the film. [record]
- No gate failures: `py_compile` clean on both files; `static_scene_check.py` per class: 5 clean · 0 warn · 0 error on the first full run. [record]
- No reversals on skill or structure: the card test failed every body beat (no beat's idea is an interface, a number set, or one word), so the film uses zero cards; recorded in SHOTLIST.md and CHECKS-REPORT.md. [judgment]
- All 14 `until()` pacing phrases script-verified verbatim against `narration_text` (0 misses), so the narration clock is real rather than silently skipped. [record]
- `manim_layout_audit.py --curve-strict` could not run in this VM (no Manim/pangocairo) — deferred to Bear's Mac render pass; noted in CLAUDE-CODE-RENDER.md §2 and CHECKS-REPORT.md. [record]

**4. What I did.**
Wrote all 12 package files (ACTS, SHOTLIST, FACTCHECK, make_sheet.py, beat_sheet.json — 9 beats, 5 body, 200 s — scenes.py with 5 Manim scene classes on the pasted iso_kit, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README), pushed all 12 via gh-put-file.py to `muse/youtube/how-to-use-ai/learn-anything-faster/`, and verified all 12 live via Contents API reads (blob-SHA match, 12/12). [record]

**5. What Claude or another person contributed.**
The parent orchestrator supplied the assignment (slug, title, pitch, the three moves, topic options, the 12-file convention, the QC gate, the FRICTIONAL.md format). Bear set the channel/persona/audience/skill-menu rules and the film-identity constants. The show-tell skill, iso_kit, and QC checker came from the brutalist.art toolkit; the 12-file package convention from the sibling film builds. I chose the mortgage as the demo topic, wrote every narration line and scene, and did the fact-check research. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell lane's timing discipline now: front-loading motion before the clip midpoint (with settled labels up by the midpoint) satisfies GATE T while keeping the voice synced via until()-paced windows after it. I still do not know whether Bear wants the deferred layout audit to block the review cut or run alongside it. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/learn-anything-faster/` on Humanitariansai/humanitarians-youtube-muse (12/12 blob-SHA matches); CHECKS-REPORT.md records 5 clean · 0 warn · 0 error. Next step: Bear runs `manim_layout_audit.py --curve-strict` per scene class, then renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md — never publish without his explicit instruction. [record]

---

## 2026-10-03 — Film build: "Write with AI, Still Sound Like You" (`write-with-ai-sound-like-you`)

**1. Date and what I was working on.**
2026-10-03. Built the pre-render film package for "Write with AI, Still Sound Like You" (slug `write-with-ai-sound-like-you`, How to AI #14) for the humanitarians AI YouTube channel — an original script (no mirror source): drafting with AI without the robotic aftertaste, via four fixes (paste a voice sample, ban the giveaways, dictate-then-clean, final pass in your own words) plus an email demo. Liam persona ("Liam, in for Bear,"), Teardown register, Kokoro am_onyx. Pushed to `muse/youtube/how-to-use-ai/write-with-ai-sound-like-you/` on Humanitariansai/humanitarians-youtube-muse. [record]

**2. I tried / expected.**
I expected to keep the assigned show-tell skill, write 12 package files with the four-fix argument, pass the static QC first try, and push 12 files cleanly. [my input]

**3. What happened (including failures and reversals).**
- Skill choice: show-tell, no switch. Ran the show-tell card test per body beat — no beat is an interface, a set of numbers, or a single word — so the film uses zero cards, all drawings. [judgment]
- QC gate run 1: 7/7 classes errored — `construct() raised AttributeError: 'B00_RobotDraft' object has no attribute 'until'`. Root cause was my own: I called `self.until(...)` / `self.finish()`, but the iso kit defines `until`/`finish` as module-level functions and SKILL.md documents the call form `until(self, "phrase")` (real Manim `Scene` has no such methods either). Fixed all 19 pacing calls to the module-level form, regenerated `scenes.py`; run 2: 7 clean · 0 warnings · 0 errors. Recorded in CHECKS-REPORT.md and BUILD-LOG.md. [record]
- FACTCHECK.md's first push died on `http.client.RemoteDisconnected` (transient network drop, not a 409); retry succeeded immediately. The other 11 pushed first try. [record]
- Found a sibling agent's scratch file (`/tmp/body_scenes.py`, for "Ask for the Shape You Want Back") while working — left it untouched and used my own uniquely-named scratch path. [record]
- `manim_layout_audit.py --curve-strict` not run: no Manim/pangocairo in this VM. Deferred to Bear's Mac render pass; noted in CHECKS-REPORT.md and CLAUDE-CODE-RENDER.md. Coordinates were hand-placed inside the ±6.3 × ±3.4 safe area. [record]
- FACTCHECK keeps every claim behavioral and modest — no statistics anywhere in the film by design (no invented numbers), and B03's banned-words beat is worded gently ("None of them are wrong. They are just the uniform.") so the film teaches voice, not AI-detection. [judgment]

**4. What I did.**
Wrote all 12 package files (`ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`, `make_sheet.py` — 11 beats, 7 body, est 224 s, all assertions pass — `beat_sheet.json`, `scenes.py` with 7 Manim scene classes, `SOURCES.md`, `BUILD-LOG.md`, `CHECKS-REPORT.md`, `PROMPTS.md`, `CLAUDE-CODE-RENDER.md`, `README.md`); passed the full QC gate with zero warnings/errors and no waivers; pushed all 12 via `gh-put-file.py`; verified each live via Contents API reads (HTTP 200, byte-identical). Nothing rendered or published; no audio committed. [record]

**5. What Claude or another person contributed.**
Bear set the film-identity constants (Liam, am_onyx, Teardown, claude-liam, @NikBearBrown), the audience rule (general audience, every term explained, show-don't-tell), the show-tell skill and its laws, and the 12-file package convention. The parent orchestrator supplied the assignment (slug #14, the four-fix core idea, output path, QC gate, push flow, FRICTIONAL.md format). I wrote every file and narration line. [record]

**6. What I understand now / still do not understand.**
I understand the iso kit's pacing contract now: `until`/`finish` are module-level functions taking `self` as the first arg — `self.until()` fails under both the QC stub and real Manim, and the failure is loud (AttributeError), not silent. I understand the card test as a real gate (this film: zero cards). I still do not know whether Bear wants the "Hallo" greeting kept across all films or varied per film. [my input]

**7. Evidence and next step.**
Evidence: 12/12 files live at `muse/youtube/how-to-use-ai/write-with-ai-sound-like-you/` on Humanitariansai/humanitarians-youtube-muse (verified HTTP 200, byte-identical, 2026-10-03); CHECKS-REPORT.md records 7 clean · 0 warn · 0 error. Next step: Bear renders on his Mac per `CLAUDE-CODE-RENDER.md` — Kokoro am_onyx narration, then `manim_layout_audit.py --curve-strict` per scene class (deferred from this VM), stills, `./art run`, `./art final`; never publish without his explicit instruction. [record]

---

## 2026-10-03 — Film 15: "Tame Your Spreadsheets"

**1. Date and what I was working on.**
2026-10-03. Film 15 of 24 in the "How to AI" series: a pre-render package for "Tame Your Spreadsheets" (slug `tame-your-spreadsheets`), built per the film-package spec and pushed to `muse/youtube/how-to-use-ai/tame-your-spreadsheets/`. [record]

**2. I tried / expected.**
I expected a clean refactor run: read the show-tell skill, fetch the mirror source via the Contents API, author the 12-file package, pass the QC gate, push, and verify. [my input]

**3. What happened (including failures and reversals).**
- The mirror source ("Stop learning Excel.") was a Claude Cowork power-user film; I rewrote it as a general-audience coach film around three moves (plain-English formula requests, paste-and-clean, "what's interesting in this data?"), keeping the source's core argument (human stays in control) as the B03 sanity-check warning. [judgment]
- Kept the assigned `show-tell` skill; rejected ShowTellCard beats (0 of 7 body beats are cards) because every beat is a thing, part, or flow the drawings teach better — card-test reasoning recorded in SHOTLIST.md. [judgment]
- No QC failures: py_compile clean; static_scene_check.py passed all 7 scene classes first run (7 clean · 0 warn · 0 error). Self-reviewed Gate T midpoint traps while writing (terracotta scan sweep lands before midpoint, no path_arc on .animate, literal `class BNN_Name(Scene)` names). [record]
- `manim_layout_audit.py --curve-strict` could not run in this VM (no Manim/pangocairo); deferred to Bear's Mac render pass and recorded in CHECKS-REPORT.md and CLAUDE-CODE-RENDER.md. [record]
- All 12 files pushed via gh-put-file.py and verified byte-identical (SHA-1) against Contents API reads afterwards — all verified. [record]

**4. What I did.**
Authored all 12 files (ACTS, SHOTLIST, FACTCHECK, make_sheet.py with beat-count/duration asserts, beat_sheet.json — 11 beats, 7 manim, ~303 s est — scenes.py with 7 Manim scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README), pushed and verified them. [record]

**5. What Claude or another person contributed.**
Bear set the film (slug, title, pitch, the three moves, the sanity-check warning, the fictional-example constraint) and the film-identity constants (Liam, am_onyx, Teardown, claude-liam, @NikBearBrown). The brutlist.art toolkit supplied the show-tell skill, the iso drawing kit, and the QC checker. The mirror repo supplied the refactor source argument. I wrote every file, made the refactor/rewrite judgments, and ran the QC gate; the AI contribution is the drafting and the pre-checker self-review. [record]

**6. What I understand now / still do not understand.**
I understand the full show-tell pre-render pipeline end to end, including the card test and the deferred-audit pattern for this VM. I still do not know whether Bear wants the `muse/youtube/how-to-use-ai/` placement to stand or the next film's topic. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/tame-your-spreadsheets/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the clean gate. Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md. [record]

---

## 2026-10-03 — Film 16: "Meetings into Notes"

**1. Date and what I was working on.**
2026-10-03. Film 16 of the humanitarians-channel Muse series: a pre-render
package (script, Manim visuals, docs) for "Meetings into Notes" — turn
rambling meetings into summaries and action items — built from scratch (no
mirror source) to the subagent brief and pushed to
`muse/youtube/how-to-use-ai/meetings-into-notes/`. [record]

**2. I tried / expected.**
I expected the show-tell lane to fit: one drawn image per beat, minimal text,
the voice explains. I expected the finished sibling film `how-to-use-claude`
to supply every house convention (make_sheet asserts, bookend props, QC gate
pattern), and it did. I expected the static QC stub to catch shape-signature
problems if I wrote scenes carelessly; it caught none on the first pass.
[my input]

**3. What happened (including failures and reversals).**
- The `how-to-ai/` sibling directories (dont-get-fooled, show-it-an-example,
  etc.) are empty — no how-to-ai film exists yet to copy, so I used the
  `how-to-use-ai/how-to-use-claude/` build as the reference instead. [record]
- `make_sheet.py` first used the sibling's 180–220 s duration band with a
  "3:00-3:40" comment; the honest total is 187.2 s and the brief allows 3–6
  min, so I widened the band to 165–210 s with a corrected comment. [record]
- B02's first trigger phrase landed inside the clip's 45–55% GATE T sampling
  window; switched to "already" with `lead=0.6` so the fragment drop finishes
  before the window. [record]
- B06's first layout stacked the three output cards with a vertical overlap;
  respaced to y = 1.65 / 0.2 / −1.25 (h = 1.3), gaps ≥ 0.15. [record]
- Static QC passed first try: 9 clean · 0 warn · 0 error; pacing-path run
  (with beat_sheet.json) also clean. [record]
- `manim_layout_audit.py --curve-strict` cannot run in this VM (no Manim /
  pangocairo); mitigated by hand-placed labels, straight-segment polylines
  for the B00 "tangles", and the only curve (B08's lock shackle) crossing no
  label. Deferred to Bear's Mac. [record]
- No midpoint render-guard verification possible without measured audio;
  event phrases placed off the midpoint, re-verification deferred to the Mac
  render pass. [record]

**4. What I did.**
Wrote all 12 package files (`ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`,
`make_sheet.py`, `beat_sheet.json` — 13 beats, 9 body, 187.2 s — `scenes.py`
with 9 Manim scene classes, `SOURCES.md`, `BUILD-LOG.md`, `CHECKS-REPORT.md`,
`PROMPTS.md`, `CLAUDE-CODE-RENDER.md`, `README.md`); kept the show-tell skill
as assigned; kept the privacy point to one line (film #20 covers privacy in
depth); used a fictional meeting (Maya / Sam) with no real names or company
internals; passed the full QC gate with zero warnings/errors; pushed all 12
via `gh-put-file.py`; verified each via Contents API reads (HTTP 200,
SHA-256 byte-identical). [record]

**5. What Claude or another person contributed.**
The parent orchestrator supplied the assignment (slug, working title, pitch,
the 12-file convention, the QC gate, the FRICTIONAL.md format, the privacy
one-line constraint). The show-tell skill, iso kit, static QC checker, and
the house file pattern came from the brutalist.art toolkit and the finished
`how-to-use-claude` sibling build. Web search (2026-10-03) confirmed
auto-transcription availability on Zoom/Meet/Teams for the B02 line. The AI
contribution is the drafting, the pacing/timing design, and the pre-gate QC
review; every narration line and visual is original to this film. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell spine cold now: hesitant-writer → terms → hero →
mechanism beats → your-turn composer → spoken outro, with the card test as a
real gate (this film: zero cards) and the midpoint window as the pacing
constraint. I still do not know whether the ~3:07 estimated length will hold
against measured Kokoro audio — the midpoint guard must be re-run on the Mac
after audio measurement, and narration trims may follow. [my input]

**7. Evidence and next step.**
Evidence: `muse/youtube/how-to-use-ai/meetings-into-notes/` (12 files)
verified live — all HTTP 200, SHA-256 byte-identical; CHECKS-REPORT.md records 9 clean · 0 warn · 0 error. Next step: Bear renders on his Mac per
`CLAUDE-CODE-RENDER.md` (Kokoro `am_onyx` narration, Manim scenes, layout
audit, midpoint guard) — never publish without his explicit instruction. [record]

---

## 2026-10-03 — Film 17: "Plan anything."

**1. Date and what I was working on.**
2026-10-03. Film 17 of 24 in the "How to AI" queue: a pre-render package
(script, Manim visuals, docs) for "Plan anything." — AI as planning partner —
built to the subagent brief and pushed to
`muse/youtube/how-to-use-ai/plan-anything/`. [record]

**2. I tried / expected.**
I expected show-tell to fit as assigned, and I expected the brief's arc
(constraints → draft → revise → checklist) to map cleanly onto one drawn
beat per step. I expected the hesitant-writer trigger match to be
case-insensitive. [my input]

**3. What happened (including failures and reversals).**
- No mirror source existed; this film is NEW, built from scratch. The trip
  demo and the four-step loop are the film's own constructs; all trip details
  are fictional, recorded as FICTIONAL in FACTCHECK.md. [record]
- `make_sheet.py` failed its own trigger-verbatim assertion on the first
  run: trigger "plan my whole weekend trip" vs writer text "Plan my whole
  weekend trip for me?" — the match is case-sensitive. Fixed by capitalizing
  the trigger; re-ran clean. [record]
- Static QC passed first try on all 8 scene classes: 8 clean · 0 warn ·
  0 error. Preventive stub-trap fixes were applied before the checker ran
  (FadeIn/Create/GrowFromCenter per play instead of animate-only moves,
  plain Python lists instead of VGroup indexing, fixed literal coordinates,
  np.array-wrapped ArcBetweenPoints). [record]
- `manim_layout_audit.py --curve-strict` cannot run in this VM
  (no Manim/pangocairo); deferred to Bear's Mac render pass and noted in
  CLAUDE-CODE-RENDER.md. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py,
beat_sheet.json — 12 beats, 8 body, 176.8 s — scenes.py with 8 Manim
scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER,
README), pushed all 12 files via the gh-put-file.py helper, and verified all
12 live via Contents API reads (byte-identical). [record]

**5. What Claude or another person contributed.**
Bear set the topic, pitch, assigned skill, film-identity constants, the
demo-arc shape (weekend trip built iteratively: constraints first, draft,
"too rushed, slow it down", packing checklist), the projects/budgets
generalization, and the mandated verify-bookings line — all from the build
brief. I wrote every file; the AI contribution is the drafting, the narration
wording, the scene design, and the QC pre-review. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell package pattern end to end now: the
constraints→draft→revise→checklist loop teaches well as four returning
pictures, and repeating the constraint-box layout in B05/B06 is a feature
(the repetition IS "the pattern travels"), not a defect. I still do not
know whether Bear wants any length floor for these films — this one came to
~2.9 min because the content needed 8 body beats, per the skill's law 9. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/plan-anything/`
on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the
clean gate. Next step: Bear renders narration (Kokoro am_onyx) and the review
cut on his Mac per CLAUDE-CODE-RENDER.md, including the deferred
`manim_layout_audit.py --curve-strict` pass. [record]

---

## 2026-10-03 — Film 18: "Just talk to it" (voice mode basics)

**1. Date and what I was working on.**
2026-10-03. Film 18 of 24 in the How-to-AI series: a show-tell pre-render
package (script, Manim visuals, docs) for "Just talk to it" — voice mode
basics, when talking beats typing — built from scratch (no mirror source) and
pushed to `muse/youtube/how-to-use-ai/just-talk-to-it/`. [record]

**2. I tried / expected.**
I expected to follow the show-tell skill straight: read SKILL.md, paste the
iso_kit into scenes.py, write make_sheet.py with the four bookends, pass the
static QC, push, verify. I expected my beat count (12 body + 4 bookends) to be
17. [my input]

**3. What happened (including failures and reversals).**
- make_sheet.py failed its own assertion on the first run: I wrote
  `len(B) == 17`, but 12 body + 4 bookends = 16. Fixed the assertion; the beat
  list itself was correct — the count in my head was wrong. [record]
- Static QC passed first try for all 12 classes: 12 clean · 0 warn · 0 error,
  with beat_sheet.json beside scenes.py so the until() narration pacing
  executed for real. [record]
- The first bulk push silently skipped beat_sheet.json (11 of 12 landed); I
  caught it by comparing push output to the file list and pushed it
  separately. Lesson recorded: always diff the pushed list against the file
  list, never trust the loop's silence. [record]
- `manim_layout_audit.py --curve-strict` cannot run in this VM (no
  Manim/pangocairo); deferred to Bear's Mac render pass, mitigated by
  construction (±6.2 × ±3.3 coords, type ≥ 36 px, all motion done in the first
  ~40% of each beat). [record]

**4. What I did.**
Wrote all 12 package files (ACTS, SHOTLIST, FACTCHECK, make_sheet.py,
beat_sheet.json — 16 beats, 12 manim, ~205 s est — scenes.py with 12 Manim
scene classes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER,
README); passed the full QC gate with zero warnings/errors and nothing
waived; pushed all 12 via gh-put-file.py; verified each via Contents API
reads (all byte-identical). [record]

**5. What Claude or another person contributed.**
Bear set the channel/persona/audience rules, the show-tell skill menu, the
film-identity constants, and the source slug; the parent orchestrator supplied
the assignment (slug, 12-file convention, QC gate, FRICTIONAL.md format). The
brutalist.art toolkit supplied the skill, the iso drawing kit, and the static
checker. Voice-mode availability facts were verified by me against Anthropic
support docs and three press pieces (Engadget, Tom's Guide, iTechPost),
retrieved 2026-10-03; the narration is deliberately hedged ("a microphone or
waveform icon in the app you use") so no version-specific UI is asserted. I
wrote every file; the AI contribution is the drafting, the QC pre-review, and
the research verification. [record]

**6. What I understand now / still do not understand.**
I understand the push-verify loop now: gh-put-file.py can skip a file without
erroring, so the verify step is the real gate, not the push output. I still do
not know whether Bear wants `manim_layout_audit --curve-strict` run before or
during his Mac render pass, or the next film's topic. [my input]

**7. Evidence and next step.**
Evidence: `muse/youtube/how-to-use-ai/just-talk-to-it/` (12 files) verified
live — all HTTP 200, byte-identical; CHECKS-REPORT.md records 12 clean · 0
warn · 0 error. Next step: Bear renders on his Mac per CLAUDE-CODE-RENDER.md
(Kokoro `am_onyx` narration, Manim scenes, layout audit) — never publish
without his explicit instruction. [record]

---

## 2026-10-03 — Film 19: "Pictures from Words"

**1. Date and what I was working on.**
2026-10-03. Film 19 of the "How to AI" queue: a pre-render package (script, Manim visuals, docs) for "Pictures from Words" — image generation basics for non-designers — built NEW from scratch to the film-builder spec and pushed to `muse/youtube/how-to-use-ai/pictures-from-words/`. [record]

**2. I tried / expected.**
I expected the ai-explainer skill's full pipeline (Remotion Claude-brand bookends) to be the build path, and I expected the local mirror clone to carry the rohan-v reference film. [my input]

**3. What happened (including failures and reversals).**
- Kept ai-explainer as the skill but applied only its content laws (SHOW-DON'T-TELL, DOUBLE-CHECK, REBUILD): the skill's Claude-brand Remotion bookends don't fit a series film with a locked lean Manim package identity; switching the series mid-run would break Bear's review pattern. [judgment]
- The local mirror clone lacked the fellows/ tree; read the rohan-v FACTCHECK via Contents API instead and took only the mechanism one-liner. [record]
- Pre-gate self-review caught three issues before the checker ran: M08's garden icon used throwaway mobjects for placement (replaced with explicit coords); M04's prompt-card line was too wide at real-Manin metrics (re-split to three lines); M12 recap lines were too long for their plates (capped at 48 chars). All fixed before the first checker run. [record]
- Static QC passed first try: 12 clean · 0 warn · 0 error. [record]
- make_sheet.py passed on its first run (recap assertion written case-insensitive from the start — a lesson carried over from film 1). [record]
- `manim_layout_audit.py --curve-strict` could not run in this VM (no Manim/pangocairo); deferred to Bear's Mac render pass and noted in CLAUDE-CODE-RENDER.md. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py, beat_sheet.json — 14 beats, 9 body, 282 s — scenes.py with 12 Manim scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README), pushed all 12 to `muse/youtube/how-to-use-ai/pictures-from-words/`, and verified all 12 live via Contents API reads (byte-exact SHA-256 matches). [record]

**5. What Claude or another person contributed.**
Bear set the topic, queue slot, skill assignment, and the brief (the ladder, practical uses, the honest limits beat, no version-specific claims, drawn placeholders only — no real AI images). QUEUE.md supplied film 19's pitch and film 20's title ("What never to paste into AI") for the outro teaser. Fact sources: DALL-E/community prompting guides, PetaPixel/TechCrunch on text-rendering limits, arXiv on hands, platform-label coverage, and the rohan-v fellows film for the mechanism one-liner. I wrote every file; the AI contribution is the drafting, the QC pre-review, and the research verification. [record]

**6. What I understand now / still do not understand.**
I understand the series package pattern well enough to reproduce it cleanly (no assertion fixes needed; QC passed first try). I still do not know whether Bear wants the `muse/youtube/how-to-use-ai/` placement confirmed for the remaining queue films, or which film he will pick next. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/pictures-from-words/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the clean gate. Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md, including the deferred `manim_layout_audit.py --curve-strict` pass. [record]

---

## 2026-10-03 — Film: "What never to paste into AI."

**1. Date and what I was working on.**
2026-10-03. Built the pre-render package for "What never to paste into AI"
(slug `what-never-to-paste-into-ai`, film #20 of 24) from scratch — privacy
rules of thumb for everyday use: the postcard test, the four-item
never-paste list, and how to still get help (redact, anonymize,
placeholders). Companion to `personal-ai-at-work` (same series folder).
Pushed to `muse/youtube/how-to-use-ai/what-never-to-paste-into-ai/`.
[record]

**2. I tried / expected.**
I expected to use the assigned cc-explainer skill and to follow the sibling
package's 12-file convention exactly. I expected the fact-check to confirm
the "why" beat's claims in general terms without needing product-specific
toggle paths. [my input]

**3. What happened (including failures and reversals).**
- Skill decision: lecture, not cc-explainer. cc-explainer's TERMINAL-FIRST
  law requires a real terminal session as the film's body — this film has
  none; forcing one would be a punt. The sibling `personal-ai-at-work`
  made the same call the same day. [judgment]
- Fact-checked 2026-10-03 (web): pasted chats may be stored (Anthropic: up
  to 5 years opted in, ~30 days opted out), reviewed by staff/contractors
  (OpenAI FAQ; 404 Media Sep 2026 reporting; Anthropic and Google
  disclosures), and used for training depending on product and settings
  (consumer opt-out; business plans no training by default). [record]
- make_sheet.py passed all assertions on the first run: 14 beats, 9 body,
  317 s (~5m17s). [record]
- Static QC passed first try: 12 clean · 0 warn · 0 error — no fixes
  needed; the new helpers (cross_out, person_icon) were written against
  the stub's mobject set on the first draft. [record]
- All 12 GitHub pushes landed on the first attempt (no 409s this time);
  12/12 verified live via Contents API reads. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py,
beat_sheet.json — 14 beats, 9 body, 317 s — scenes.py with 12 Manim
scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER,
README), pushed all 12 files via gh-put-file.py, and verified each live
with a Contents API read (12/12 HTTP 200). [record]

**5. What Claude or another person contributed.**
Bear set the topic, pitch, and companion constraint (do not contradict
`personal-ai-at-work`), the channel/persona lock (humanitarians channel,
Liam, am_onyx, Teardown, @NikBearBrown), the audience rules, and the QC
conventions via the handoff spec and finished sibling packages. The
postcard-test framing, the never-list, and every file are this build's own
work; the AI contribution is the drafting, the QC gate, and the research
verification. [record]

**6. What I understand now / still do not understand.**
I understand the audience-rewrite workflow well enough to repeat it:
evergreen narration ("depending on the product and its settings") is how
a film degrades gracefully when company policies change, and exact
policy wording never goes into narration. I still do not know whether
Bear wants the local `how-to-ai/` build folder renamed to `how-to-use-ai/`
to match the repo path and the sibling's local folder. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at
`muse/youtube/how-to-use-ai/what-never-to-paste-into-ai/` on
Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the
clean gate; remote beat_sheet.json round-trips 14 beats / 317 s. Next
step: Bear renders narration (Kokoro am_onyx) and the review cut on his
Mac per CLAUDE-CODE-RENDER.md — including the deferred
`manim_layout_audit.py --curve-strict` pass, and a check that the 48-char
M12 recap line fits the plate at real-Manin text metrics; never publish
without his explicit instruction. [record]

---

## 2026-10-03 — Film 21: "Trust, but verify"

**1. Date and what I was working on.**
2026-10-03. Built Film 21 ("trust-but-verify", "Trust, but verify") of the
humanitarians-channel "How to AI" series as a pre-render package: a
general-audience ai-explainer teaching a 60-second verification habit for AI
claims (confidence question; open the source; independent search; numbers
show their work; match effort to stakes). REFACTOR of
`fellows/aujaswi-a/2026-08-19-how-to-spot-unreliable-ai-research` from the
mirror repo, generalized from research papers to everyday claims. Pushed to
`muse/youtube/how-to-use-ai/trust-but-verify/`. [record]

**2. I tried / expected.**
I expected the assigned ai-explainer skill to fit (concept explainer, not a
CLI build) and the source's three research checks (recency, authority,
corroboration) to generalize into the brief's four-step habit. I expected
the static checker to pass first try because I stayed inside the
Film-1-proven Manim API subset. [my input]

**3. What happened (including failures and reversals).**
- Skill fit confirmed on reading the SKILL.md; no switch. [judgment]
- Static QC failed once: M08_B06Card's habit-card rows were text-only and
  the checker excludes text from its shape signature ("shapes never
  change — 1 distinct shape-state across 7 frames"). Fixed by adding an
  ACCENT bullet circle per row that lands with it. Re-ran all 10
  classes: 10 clean · 0 warnings · 0 errors. [record]
- `manim_layout_audit.py --curve-strict` cannot run in this VM (no
  Manim/pangocairo); deferred to Bear's Mac render pass and noted in
  CLAUDE-CODE-RENDER.md and CHECKS-REPORT.md. [record]
- Grounded the hook fact via web search: the "10% of the brain" claim is a
  documented neuromyth (CNRS: "completely false"; Scientific American /
  Barry Gordon). The B02 demo answer (banana / 40% / Journal of Sleep
  Medicine) is a constructed illustration of a hallucinated answer,
  documented as such in FACTCHECK.md and never endorsed. [record]
- Pushed all 12 files and verified each live via Contents API reads. Did
  not touch muse/FRICTIONAL.md, muse/README.md, or muse/QUEUE.md —
  out of scope for this task. [record]

**4. What I did.**
Authored the full 12-file package (ACTS, SHOTLIST, FACTCHECK,
make_sheet.py, beat_sheet.json — 10 beats, 266 s — scenes.py with 10
Manim scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS,
CLAUDE-CODE-RENDER, README), ran py_compile plus the static checker per
class, fixed the one failure, pushed everything via gh-put-file.py, and
verified every file with a Contents API read. [record]

**5. What Claude or another person contributed.**
The parent agent supplied the film brief: the four-step habit spec, the
step-2 demo requirement, stakes calibration, the refactor source pointer,
and the film-identity constants (Liam, am_onyx, Teardown, claude-liam,
@NikBearBrown). The refactor source's argument spine
(recency/authority/corroboration) came from Aujaswi Agarwal's fellows film
via the mirror repo. I wrote every file; the AI contribution is the
narration drafting, the QC gate, and the web-grounded factcheck. [record]

**6. What I understand now / still do not understand.**
I understand the series' per-film conventions now: the 12-file package,
the make_sheet.py assertion pattern, the stub-checker traps
(text-excluded shape signatures; no animate-only shape introductions),
and the push-then-verify flow. I do not know whether the parent wants
this entry appended to muse/FRICTIONAL.md directly or handed back —
the task said not to write it, so I return the entry text. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at
`muse/youtube/how-to-use-ai/trust-but-verify/` on
Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the
10-clean gate; BUILD-LOG.md records the skill choice and the M08 fix.
Next step: Bear renders narration (Kokoro am_onyx) and the cut on his Mac
per CLAUDE-CODE-RENDER.md, including the deferred
`manim_layout_audit.py --curve-strict` pass. [record]

---

## 2026-10-03 — Film 22: "Free vs paid: when to pay"

**1. Date and what I was working on.**
2026-10-03. Film 22 of the "How to AI" queue: a pre-render package (script, Manim visuals, docs) for "Free vs paid: when to pay", built from scratch with no mirror source, pushed to `muse/youtube/how-to-use-ai/free-vs-paid-when-to-pay/`. [record]

**2. I tried / expected.**
I expected to use the assigned cc-explainer skill as-is. [my input]

**3. What happened (including failures and reversals).**
- Switched skill cc-explainer → ai-explainer: the film is a general-audience concept explainer with no Claude Code terminal session to show; cc-explainer's TERMINAL-FIRST/REAL-SESSION laws would have forced an invented session. [judgment]
- make_sheet.py had an authoring bug before its first run (the class-matching assertion compared against `"MM01"`); fixed to a startswith check. [record]
- First QC run: 13/14 clean; M05_FourThings raised TypeError — `P(1.75, 0.75, 0)` passed three args to the two-arg `P()` helper. Fixed to `p + np.array([1.75, 0.75, 0])`; re-run: 14 clean · 0 warn · 0 error. [record]
- `manim_layout_audit.py --curve-strict` could not run in this VM (no Manim/pangocairo); deferred to Bear's Mac render pass and noted in CLAUDE-CODE-RENDER.md. [record]
- Two web searches (2026-10-03) confirmed the four-item paid-tier menu and that prices/tiers churn fast — so the film quotes no prices by design. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py, beat_sheet.json — 14 beats, 9 body, 359 s — scenes.py with 14 Manim scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README.md); passed the full QC gate with zero warnings/errors hidden or waived; pushed all 12 via gh-put-file.py; verified each byte-identical via Contents API reads. [record]

**5. What Claude or another person contributed.**
The parent orchestrator supplied the assignment (slug, title, pitch, the decision-framework brief, the 12-file convention, the QC gate, the FRICTIONAL.md format). Bear set the channel/persona/audience/skill-menu rules. The brutalist.art toolkit supplied the ai-explainer doctrine and the QC checker; the sibling film ai-is-a-slot-machine supplied the package conventions. I wrote every file; the AI contribution is the drafting, the research verification, and the QC pre-review. [record]

**6. What I understand now / still do not understand.**
I understand the ai-explainer lane now: concept-illustrated middle, Manim-only pre-render packages for the how-to-ai series, and the read-aloud convention (every on-screen word spoken in its beat) as a real authoring constraint that reshaped four narration lines. I do not know whether Bear wants the world-language greeting rotation ("Ciao" on this film) tracked centrally, or whether the ai-explainer Remotion bookends (composer cold open, verdict card) will be added at render time or dropped for this series. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/free-vs-paid-when-to-pay/` on Humanitariansai/humanitarians-youtube-muse — all HTTP 200, byte-identical; CHECKS-REPORT.md records 14 clean · 0 warn · 0 error. Next step: Bear runs `manim_layout_audit.py --curve-strict` on his Mac (deferred), then renders narration (Kokoro am_onyx) and the review cut per CLAUDE-CODE-RENDER.md — never publish without his explicit instruction. [record]

---

## 2026-10-03 — Film build: "Set it up once" (`muse/youtube/how-to-use-ai/set-it-up-once/`)

**1. Date and what I was working on.**
2026-10-03: built one pre-render film package for the humanitarians AI YouTube channel from scratch (NEW source, no mirror): film #23 of 24, "Set it up once" — custom instructions, teaching the AI your preferences a single time, for a smart pragmatic general audience. [record]

**2. I tried / expected.**
I expected a straightforward show-tell package following the how-to-rot-your-brain-with-ai sibling's pure show-tell contract (13 beats, no BVDT, bookend remotion props): read the skill, fact-check the feature's existence in general terms, write the sheet and scenes, pass the QC gate, push 12 files. [my input]

**3. What happened (including failures and reversals).**
- Stayed with **show-tell** (did not switch skills): the film is one practical action plus a payoff demo — the card test failed for every body beat (each idea is a thing, a part, or a flow from the film's own cast), so the film uses zero cards, all drawings. [judgment]
- Fact-check research verified the pattern in general terms: ChatGPT Custom Instructions (Settings → Personalization, two fields, applied to new chats), Claude Personal Preferences (Settings → General) + Projects instructions, Gemini "Instructions for Gemini" (Settings & help → Personal Intelligence) + Gems. Sources already disagreed on sub-menu names, so the film deliberately never names a product's menu path — only "settings, or your profile" and the candidate words (instructions / personalization / memory). No statistics quoted anywhere. [record]
- `make_sheet.py` first run passed all assertions: 13 beats, 9 manim + 4 bookend lanes, 211 s (~3m31s); BIDEA trigger contract, BDEFS 17-char term contract, BHTF prompt-read-in-full contract, BOUT outro_voice + 1.0 s tail. [record]
- QC gate run 1: 8 clean, 1 warning — B01_TheNote's drop-in started at y=2.95, putting the note's terracotta pin dot at y=3.87, outside the ±3.4 safe area. Fixed by starting the drop at y=2.4 (pin at 3.32). Run 2: 9/9 clean · 0 warnings · 0 errors; pacing path re-checked with beat_sheet.json present. [record]
- All 12 pushes went through first try (no 409s); all 12 verified HTTP 200 and byte-identical via Contents API reads. [record]

**4. What I did.**
Wrote all 12 package files (ACTS.md, SHOTLIST.md, FACTCHECK.md, make_sheet.py, beat_sheet.json, scenes.py, SOURCES.md, BUILD-LOG.md, CHECKS-REPORT.md, PROMPTS.md, CLAUDE-CODE-RENDER.md, README.md); passed the full QC gate with zero warnings/errors hidden or waived; pushed all 12 via gh-put-file.py to `muse/youtube/how-to-use-ai/set-it-up-once/`; verified each via Contents API reads. [record]

**5. What Claude or another person contributed.**
The parent orchestrator supplied the assignment (slug, title, pitch, the 12-file convention, the QC gate, the FRICTIONAL.md format) and the film identity constants. The sibling films ai-is-a-slot-machine and how-to-rot-your-brain-with-ai supplied the show-tell package conventions (beat-sheet format, bookend remotion props, assertion pattern) — every narration line and visual is original. Web sources (OpenAI/Google help docs via third-party guides, product comparison tables) supplied the fact-check. [record]

**6. What I understand now / still do not understand.**
I understand the pure show-tell contract now: no BVDT, the pinned-note cast recurring across body beats, the card test as a real gate (this film: zero cards). I understand the checker's coordinate recording catches off-stage starts (the pin dot at 3.87). I do not know how the real-Manin text widths will land inside the chat bubbles and the B03 note (line 3 is the widest) — the static checker doesn't measure text extents; Bear's Mac render pass must eyeball bubble text fit before 4K. [my input]

**7. Evidence and next step.**
Evidence: 12/12 files live at `muse/youtube/how-to-use-ai/set-it-up-once/` (verified HTTP 200 + byte-identical, 2026-10-03); QC log in CHECKS-REPORT.md. Next step: Bear renders locally via CLAUDE-CODE-RENDER.md — Kokoro am_onyx narration, 9 Manim scenes + 4 Remotion bookends, `manim_layout_audit.py --curve-strict` (deferred from this VM) before the 4K render; never publish without his explicit instruction. [record]

---

## 2026-10-03 — Film 24: "One AI or many?"

**1. Date and what I was working on.**
2026-10-03. Film #24 of 24 in the humanitarians-channel "How to AI" series: a pre-render package (script, Manim visuals, docs) for "One AI or many?", pushed to `muse/youtube/how-to-use-ai/one-ai-or-many/`. [record]

**2. I tried / expected.**
I expected to use the assigned cc-explainer skill and to stand alone on the pitch. On reading the pitch (a tool-comparison concept film, general audience) and the cc-explainer SKILL.md, I expected cc-explainer's TERMINAL-FIRST law to be unworkable — a film about choosing chat AI tools has no terminal session to reconstruct. [my input]

**3. What happened (including failures and reversals).**
- Switched skill cc-explainer → ai-explainer after reading both SKILL.md files: no terminal session exists for REAL-SESSION law, so terminal-first was a forced punt; ai-explainer matches the companion film's skill and the comparison-film shape. Recorded the choice and the reasoning in BUILD-LOG.md. [record]
- Read the companion film's ACTS.md/BUILD-LOG.md on GitHub before authoring; aligned the verdicts ("the stack is the answer" vs "build the stack slowly") and cited the companion's 30-minute test rather than re-litigating it; logged in FACTCHECK.md §6. [record]
- make_sheet.py duration budgeting: trimmed B07 to 65 words against its 27 s budget and set BVDT to 32 s for the 76-word verdict before the final run; no assertion failures in the shipped run. [record]
- Static QC passed first try: 10 scene classes clean · 0 warnings · 0 errors. [record]
- All 12 pushes succeeded via gh-put-file.py; all 12 verified byte-identical via Contents API reads. Local __pycache__ removed, never pushed. [record]

**4. What I did.**
Wrote all 12 package files (12 beats, 7 body, 287 s; scenes.py with 10 Manim classes M01–M10); passed the full QC gate with zero warnings/errors hidden or waived; pushed all 12 via gh-put-file.py; verified each via Contents API reads. [record]

**5. What Claude or another person contributed.**
The parent orchestrator supplied the assignment (slug, title, pitch, companion-film reference, core idea, anti-obsession beat, decision rule, four walls, audience, skill menu, the 12-file convention, the QC gate, the FRICTIONAL.md format, the no-version/no-ranking/no-price rule). Bear set the channel/persona/audience/skill-menu rules. The companion film's package (Humanitariansai repo) supplied the consistency constraint. I wrote every file; the AI contribution is the drafting, the consistency check, and the QC pre-review. [record]

**6. What I understand now / still do not understand.**
I understand the show-vs-tell anti-obsession lane now: when a film's rule is "don't obsess," naming vendors is itself the obsession, so the film names none. I do not yet know whether Bear wants a `muse/README.md` index row for this film (I left README/QUEUE/FRICTIONAL.md untouched per the standing rule). [my input]

**7. Evidence and next step.**
Evidence: `muse/youtube/how-to-use-ai/one-ai-or-many/` (12 files) verified live — all HTTP 200, byte-identical; CHECKS-REPORT.md records 10 clean · 0 warn · 0 error. Next step: Bear renders on his Mac per `CLAUDE-CODE-RENDER.md` (Kokoro `am_onyx` narration, Manim scenes, then `manim_layout_audit.py --curve-strict`, which could not run in the build VM) — never publish without his explicit instruction. [record]

## 2026-10-04 — Film: "Teach it your world" (slug `teach-it-your-world`)

**1. Date and what I was working on.**
2026-10-04. One complete pre-render film package for the humanitarians-channel Muse series: "Teach it your world" — upload your docs so AI answers from YOUR material (personal knowledge bases, explained non-technically). Assigned skill cc-explainer; built as ai-explainer with recorded reasoning. Pushed to `muse/youtube/how-to-use-ai/teach-it-your-world/`. [record]

**2. I tried / expected.**
I expected to run a real Claude Code session and build the film terminal-first per the cc-explainer skill. I expected the `claude` CLI to be installed or installable-and-authenticatable in the VM. [my input]

**3. What happened (including failures and reversals).**
- The `claude` CLI is not installed (`which claude` → nothing) and cannot be authenticated — no credentials exist in the store, and policy forbids collecting raw credentials from the user. cc-explainer's REAL-SESSION LAW requires an actually-run session transcribed to SESSION.md; inventing one would be a DOUBLE-CHECK LAW violation. Switched to ai-explainer (the skill for a non-technical concept walkthrough) with the reasoning recorded in BUILD-LOG.md. [record]
- The word-coverage audit (after the first clean QC pass) found five on-screen words with no spoken match (B02 "docs", B04 "rota", B06 "docs"/"know", B07 "this", B08 "blind spots"). Fixed by editing narration in make_sheet.py and one card line in scenes.py; re-audited clean and re-ran the full QC pass (still 0/0). [record]
- Static QC passed first try for all 7 Manim classes: 7 clean · 0 warn · 0 error. [record]

**4. What I did.**
Built the full 12-file package: ACTS.md, SHOTLIST.md, FACTCHECK.md (verified against Anthropic's RAG-for-projects help article, read live), make_sheet.py → beat_sheet.json (13 beats, ~341 s, assertions on count/order/duration/B01≥9s/until-phrases), scenes.py (7 Manim classes, iso kit pasted verbatim), SOURCES.md, BUILD-LOG.md, CHECKS-REPORT.md, PROMPTS.md, CLAUDE-CODE-RENDER.md, README.md. Pushed all 12 files via the Contents API and verified each with an API read (12/12 HTTP 200). [record]

**5. What Claude or another person contributed.**
Bear (via the coordinator task) set the slug, working title, pitch, and film-identity constants (Liam, am_onyx, Teardown, claude-liam, @NikBearBrown). The factual core — Claude Projects' project knowledge base and Anthropic's RAG-for-projects help article — came from Anthropic's published documentation, read live during the build. The iso drawing kit and package conventions came from the brutalist.art toolkit and sibling series films. I wrote every file, designed the spine and all narration, ran the QC gate, and did the research verification. [record]

**6. What I understand now / still do not understand.**
I understand the ai-explainer bookend spine (composer cold open → hesitant-writer BLUF → definitions → illustrated body → verdict artifact → your-turn → title outro) and the word-coverage rule (every on-screen word spoken) well enough to audit it mechanically. I still do not know whether the coordinator wants the B00 composer exchange (an illustrative drawn demo, disclosed in CHECKS-REPORT) kept as-is or reworked, and I do not know the next film's topic. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/teach-it-your-world/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the clean gate (7 clean · 0 warn · 0 error). Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md, including the deferred `manim_layout_audit.py --curve-strict` pass.

---

## 2026-10-04 — Film: "The long game"

**1. Date and what I was working on.**
2026-10-04. Built the complete 12-file pre-render package for "The long game" (slug `the-long-game`), a "How to AI" show-tell film on the long-document habit — outline first, then sections one at a time, then stitching — dramatized with a twenty-page grant proposal. Companion to film 11 `small-steps-big-jobs`. Pushed to `muse/youtube/how-to-use-ai/the-long-game/`. [record]

**2. I tried / expected.**
I expected to mirror the sibling film's package structure exactly (it was built the previous day to the same spec), keep the assigned show-tell skill, and land 3–6 minutes with 9 body beats. I expected the static QC gate to catch at least one issue, as it had on earlier builds. [my input]

**3. What happened (including failures and reversals).**
- Read the show-tell SKILL.md end to end and the full `small-steps-big-jobs` package to match conventions before writing anything. [record]
- make_sheet.py passed all its assertions on the first run: 13 beats, 9 body (B00–B08), 202 s (~3m22s). [record]
- Pre-gate self-review caught one latent issue before the checker ran: B03 reached into `oc.submobjects[1:]` to Create the outline card's rows; reworked `_outline_card` to return `(group, rows)` — cleaner and stub-safe. [record]
- Static QC then passed first try: 9 clean · 0 warn · 0 error. [record]
- One `__pycache__/` directory was created by the py_compile gate run; removed before pushing (never commit `.pyc`/`__pycache__`). [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py, beat_sheet.json — 13 beats, 9 body, 202 s — scenes.py with 9 Manim scene classes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README), pushed all 12 files via gh-put-file.py, and verified all 12 live via Contents API reads (HTTP 200). [record]

**5. What Claude or another person contributed.**
The parent agent supplied the slug, title, pitch, assigned skill, film identity constants, and the QC/push rules. Bear set the standing locks (Liam persona, am_onyx, Teardown, claude-liam, @NikBearBrown, no rendering/publishing). The grant-proposal scenario is my own dramatization of the brief, chosen for the humanitarians audience. The show-tell skill, iso_kit, and QC checker came from the brutalist.art toolkit. I wrote every file; the AI contribution is the drafting, the QC pre-review, and the narration timing design. [record]

**6. What I understand now / still do not understand.**
I understand the show-tell pre-render pipeline end to end now: the card test (this film correctly uses zero cards), the Gate A "shapes never change" trap (pair every `.animate()` with a genuine new shape), and the Gate T midpoint discipline (keep plays out of 45–55%; two soft spots flagged for the Mac pass). I still do not know this film's chapter number in the How to AI queue (it was not in the local QUEUE.md), so I omitted `chapter_number` and recorded `companion_to: small-steps-big-jobs` in the beat sheet metadata instead. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/the-long-game/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the clean gate (9 clean · 0 warn · 0 error). Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md, including the deferred `manim_layout_audit.py --curve-strict` pass.

---

## 2026-10-04 — Film 24: "Make it remember (and forget)"

**1. Date and what I was working on.**
2026-10-04. Film 24 of the "How to AI" queue: a pre-render package (script, Manim visuals, docs) for "Make it remember (and forget)" (memory features: what to store, what never to store, how to delete it), built from scratch with no mirror source, pushed to `muse/youtube/how-to-use-ai/make-it-remember/`. [record]

**2. I tried / expected.**
I expected to use the assigned cc-explainer skill as-is. [my input]

**3. What happened (including failures and reversals).**
- Switched skill cc-explainer → show-tell after reading the skill and the FRICTIONAL.md precedent (free-vs-paid film): no terminal session exists for REAL-SESSION law — no `claude` CLI in the VM, no credential authorized by the task to run one, and the CC kit components aren't ported to this tree; inventing a session would violate DOUBLE-CHECK. The topic is the direct sibling of set-it-up-once (show-tell). Recorded in BUILD-LOG.md. [record]
- Two web searches (2026-10-04) grounded the memory facts: Topics list in Settings → Memory → Topics; on by default for Free/Pro/Max; sensitive topics off by default; never-stored categories; Pause vs Reset; incognito; chat search separate from memory. Privacy claims kept to what's verified. [record]
- make_sheet.py passed all assertions on its first run (13 beats, 216 s, bookend contracts). [record]
- scenes.py had two authoring bugs before QC: a syntax error in B04's MoveAlongPath play (stray paren closed self.play early) and a `.set(height=0.5)` hack on the B06 incognito pill — both caught by py_compile and fixed properly. [record]
- Static QC passed first try: 9 scene classes clean · 0 warnings · 0 errors. [record]
- `manim_layout_audit.py --curve-strict` could not run in this VM (no Manim/pangocairo); deferred to Bear's Mac render pass and noted in CLAUDE-CODE-RENDER.md. [record]
- All 12 pushes succeeded via gh-put-file.py; all 12 verified byte-identical via Contents API reads. No media or cache files committed. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py, beat_sheet.json — 13 beats, 9 body, 216 s — scenes.py with 9 Manim scenes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README.md); passed the full QC gate with zero warnings/errors hidden or waived; pushed all 12 via gh-put-file.py; verified each byte-identical via Contents API reads. [record]

**5. What Claude or another person contributed.**
The parent orchestrator supplied the assignment (slug, title, pitch, audience rules, the 12-file convention, the QC gate, the FRICTIONAL.md format, the no-pricing rule) and the skill-switch allowance. Bear set the channel/persona/audience rules. The free-vs-paid film's FRICTIONAL entry supplied the cc-explainer-switch precedent; the set-it-up-once package supplied the show-tell conventions. I wrote every file; the AI contribution is the drafting, the research verification, and the QC pre-review. [record]

**6. What I understand now / still do not understand.**
I understand now why cc-explainer is assigned by default for Claude-topic films but genuinely can't stretch to non-terminal topics — REAL-SESSION is the hard line, and the precedent path (read both skills, switch, record) is the honest one. I do not yet know whether Bear wants a muse/README.md index row or QUEUE.md update for this film (I left README/QUEUE/FRICTIONAL.md untouched per the standing rule). [my input]

**7. Evidence and next step.**
Evidence: `muse/youtube/how-to-use-ai/make-it-remember/` (12 files) verified live — all HTTP 200, byte-identical; CHECKS-REPORT.md records 9 clean · 0 warn · 0 error. Next step: Bear renders on his Mac per `CLAUDE-CODE-RENDER.md` (Kokoro `am_onyx` narration — whisper-check "ID numbers", "café", "incognito" — Manim scenes, then `manim_layout_audit.py --curve-strict`, which could not run in the build VM) — never publish without his explicit instruction. [record]

---

## 2026-10-04 — Film: "Agents: AI that does things"

**1. Date and what I was working on.**
2026-10-04. A pre-render film package (script, Manim visuals, docs) for "Agents: AI that does things" — what "agentic" AI means for a normal person: where it helps, where it goes wrong, how to supervise it — pushed to `muse/youtube/how-to-use-ai/agents-that-do-things/`. [record]

**2. I tried / expected.**
I expected to use the assigned ai-explainer skill unchanged, and to ground the script in Anthropic's "Building effective agents" and prompt-injection reporting rather than vendor marketing. I expected the task's new beat-sheet schema (beat_id / narration_text / estimated_duration_s / GRAPHIC-or-REMOTION shots) to diverge from the sibling film's MANIM-only convention, and budgeted the bookends as Remotion patterns accordingly. [my input]

**3. What happened (including failures and reversals.**
- No skill switch was needed — ai-explainer fit the pitch on first reading; recorded in BUILD-LOG.md. [record]
- make_sheet.py passed all contract assertions (12 beats, 7 body, 324 s) on its first run — no generation failures. [record]
- Static QC passed 8/8 scenes clean with 0 warnings / 0 errors on the first checker run; the three layout bugs were caught by my own pre-QC review (B02 labels separating from their cards, B05 degenerate arrows, B07 bar/card overlap) and fixed before the checker ever ran. [record]
- All 12 pushes succeeded via gh-put-file.py; all 12 verified byte-identical via Contents API reads. Local __pycache__ removed, never pushed. [record]

**4. What I did.**
Wrote all 12 package files (12 beats, 324 s; scenes.py with 8 Manim classes B02–B09; 4 Remotion bookends specified by pattern in the beat sheet); authored the three-rule supervision framework (delegate only what you can check / approve the irreversible / start on low stakes) as the film's teaching spine with the framework beat placed before the worked example; passed the full QC gate with zero warnings/errors hidden or waived; pushed all 12 files and verified each live. [record]

**5. What Claude or another person contributed.**
The parent orchestrator supplied the assignment (slug, title, pitch, assigned skill, the 12-file convention, the beat-sheet schema, the QC gate, the FRICTIONAL.md format, the no-version/no-ranking/no-price rule). Bear set the channel/persona/audience/skill-menu rules. The sibling film's package (free-vs-paid-when-to-pay, Humanitariansai repo) supplied the house conventions. I wrote every file; the AI contribution is the drafting, the pre-QC layout review, and the QC pre-review. [record]

**6. What I understand now / still do not understand.**
I understand the task's schema split now: REMOTION-pattern bookends (cold open, hesitant writer, your turn, outro) carry no Manim classes, so scenes.py covers only the body — the per-class QC runs on exactly the 8 body classes. I understand the hesitant-writer correction must be the film's actual misconception ("a smarter chatbot" → "a chatbot with hands"), not a synonym swap. I do not know how the real-Manim text widths will land in B06's flagged instruction line and B09's widest recap line — the static checker doesn't measure text extents; Bear's Mac render pass must eyeball text fit before 4K. [my input]

**7. Evidence and next step.**
Evidence: `muse/youtube/how-to-use-ai/agents-that-do-things/` (12 files) verified live — all HTTP 200, byte-identical; CHECKS-REPORT.md records 8 clean · 0 warn · 0 error. Next step: Bear renders on his Mac per `CLAUDE-CODE-RENDER.md` (Kokoro `am_onyx` narration, 8 Manim scenes + 4 Remotion bookends, then `manim_layout_audit.py --curve-strict`, which could not run in the build VM) — never publish without his explicit instruction. [record]

---

## 2026-10-04 — Film: "Talk to your tools" (talk-to-your-tools)

**1. Date and what I was working on.**
2026-10-04. Built the pre-render package for "Talk to your tools" (slug talk-to-your-tools) — connecting AI to email/calendar/apps: the first automations worth setting up, and what to watch out for. Companion to the meetings-into-notes film. Pushed to muse/youtube/how-to-use-ai/talk-to-your-tools/. [record]

**2. I tried / expected.**
I expected to build with the assigned cc-explainer skill. I expected the GitHub push loop to be uneventful and the static QC to pass given the proven iso kit. [my input]

**3. What happened (including failures and reversals).**
- Skill switch, recorded per the brief: I read cc-explainer fully and its TERMINAL-FIRST law (body beats default to CCSession) plus REAL-SESSION law (every block traces to a real SESSION.md) require a reconstructed Claude Code terminal session — this film has none. Built with show-tell instead: the general-audience explainer lane, and the companion film's skill. [judgment]
- The scenes.py assembly script built its split marker wrong and asserted before writing anything; fixed by splitting on the sibling file's exact marker line. No film content affected. [record]
- B02's `show` annotation said rows land one by one; the scene lands both read rows together to keep the motion out of the 45–55% GATE T window. Corrected the annotation before pushing. [record]
- Fact-check held up against live web sources (2026-10-04): the connector / OAuth-style connect flow, the permissions screen (exact labels deliberately not quoted — version-sensitive), supervised-sending guidance, least-privilege guidance, and the calendar-invite prompt-injection vector (LayerX via The Register, Feb 2026; "Invitation Is All You Need," Aug 2025). No invented statistics anywhere. Automations are framed as repeat jobs you ask for, not scheduled background tasks, so nothing version-specific can go stale. [record]
- Static QC passed 9/9 on the first run: 0 warnings, 0 errors; 19/19 until() phrases verified verbatim against their narrations. [record]
- All 12 pushes landed first try — no 409s this round. [record]
- manim_layout_audit.py --curve-strict could not run (no Manim/pangocairo in this VM); mitigations in CHECKS-REPORT.md, deferred to the Mac. [record]

**4. What I did.**
Built the full 12-file package (ACTS, SHOTLIST, FACTCHECK, make_sheet.py, beat_sheet.json — 13 beats, 9 body, 243.6 s ≈ 4:03 — scenes.py with 9 Manim scene classes, SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README), pushed all 12 files via gh-put-file.py, verified each live via the Contents API (12/12 HTTP 200), and confirmed the remote beat_sheet.json round-trips 13 beats / 243.6 s. Nothing rendered, published, or staged; no audio committed. [record]

**5. What Claude or another person contributed.**
The parent orchestrator assigned the film, slug, pitch, and the permission to switch skills with recorded reasoning; the brief's audience rules shaped the narration. The show-tell skill, iso kit, and static QC checker came from the brutalist.art toolkit; the sibling meetings-into-notes build supplied the 12-file convention and the proven kit/helpers copied verbatim. The web sources listed in SOURCES.md grounded the fact-check. I wrote every file. [record]

**6. What I understand now / still do not understand.**
I understand the skill-fit test now: cc-explainer is for films that reconstruct a real terminal session; a general-audience "connect your apps" explainer has no session to reconstruct, so show-tell is the honest fit — and the brief explicitly permits the switch with recorded reasoning. [judgment]
I still do not know whether future how-to-ai assignments will keep naming cc-explainer for non-terminal topics. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live (HTTP 200) at muse/youtube/how-to-use-ai/talk-to-your-tools/ on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records 9 clean · 0 warn · 0 error; remote beat_sheet.json round-trips 13 beats / 243.6 s. Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md — including the deferred layout audit --curve-strict, the midpoint guard with measured audio, and the "Hallo" whisper-check. Never publish without his explicit instruction. [record]

---

## 2026-10-04 — Film: "The Second Opinion" (`muse/youtube/how-to-use-ai/the-second-opinion/`)

**1. Date and what I was working on.**
2026-10-04. A pre-render package (script, Manim visuals, docs) for "The Second Opinion" — big decisions: pit two AIs against each other, or make one argue against itself (steel-manning for everyday life). Companion to `make-it-check-its-own-work`. Pushed to `muse/youtube/how-to-use-ai/the-second-opinion/`. [record]

**2. I tried / expected.**
I expected to use the assigned ai-explainer skill. On reading the pitch (a how-to technique film with a worked demo for the general audience) and both SKILL.md files, I expected show-tell's "one drawing per beat, the voice explains" lane to fit better — and to match the series' shipped bookends — than ai-explainer's composer-cold-open/bookend machinery. [my input]

**3. What happened (including failures and reversals).**
- Switched skill ai-explainer → show-tell after reading both SKILL.md files and the companion film's package: series consistency (hesitant-writer → terms → drawings → Your Turn → spoken outro) outweighs the default assignment; recorded with reasoning in BUILD-LOG.md. [record]
- Greeting "Merhaba" (Turkish): the series is saturated with "Hallo" variants and the companion used "Ciao"; Turkish is fresh. [judgment]
- make_sheet.py assertion failure on first run: BDEFS durationSeconds 22.0 vs 21.2 for the 53-word narration — fixed the prop to the word count. [record]
- Static QC first run: 8 clean, 1 errored — B07_ProMove `NameError: flag` (the helper lived in the companion's film helpers, not iso_kit; I didn't carry it over). Added it; re-ran all 9 → 0 warn, 0 error. [record]
- The scripted verbatim-until check caught one case mismatch ("Steelman the opposite case" vs the narration's lowercase "steelman") that would have silently no-op'd the wait — fixed. [record]
- All 12 pushes succeeded via gh-put-file.py; all 12 verified byte-identical via Contents API reads. Local __pycache__ removed, never pushed. [record]

**4. What I did.**
Wrote all 12 package files (13 beats, 238.4 s est.; scenes.py with iso_kit + 9 Manim classes B00–B08); grounded steel-manning, devil's advocate, and the multi-agent debate paper in web searches; passed the full QC gate with zero warnings/errors hidden or waived; pushed all 12 via gh-put-file.py; verified each via Contents API reads. [record]

**5. What Claude or another person contributed.**
The parent orchestrator supplied the assignment (slug, title, pitch, companion-film reference, the 12-file convention, the QC gate, the FRICTIONAL.md format, the seven-field entry requirement). Bear set the channel/persona/audience/never-publish rules. The companion film's package supplied the series conventions. I wrote every file; the AI contribution is the drafting, the fact-grounding searches, and the QC pre-review. [record]

**6. What I understand now / still do not understand.**
I understand the companion-film pattern now: the demo should complete the first answer rather than correct it (the night-shift job's steelman completes "take it" — it doesn't debunk it), which is the honest shape of the second-opinion move. I do not yet know whether Bear wants the night-shift demo kept qualitative or sharpened with a concrete dollar example at the review cut. [my input]

**7. Evidence and next step.**
Evidence: `muse/youtube/how-to-use-ai/the-second-opinion/` (12 files) verified live — all HTTP 200, byte-identical; CHECKS-REPORT.md records 9 clean · 0 warn · 0 error. Next step: Bear renders on his Mac per `CLAUDE-CODE-RENDER.md` (Kokoro `am_onyx` narration, Manim scenes, then `manim_layout_audit.py --curve-strict`, which could not run in the build VM) — never publish without his explicit instruction. [record]

---

## 2026-10-04 — Film: "Code without coding" (How to AI, NEW)

**1. Date and what I was working on.**
2026-10-04. Built the complete pre-render package for "Code without coding" (slug `code-without-coding`): what a non-programmer can safely build with AI coding tools, and the three mistakes that bite beginners. 12 files at `muse/youtube/how-to-use-ai/code-without-coding/` on Humanitariansai/humanitarians-youtube-muse. [record]

**2. I tried / expected.**
I expected a straightforward show-tell build from the pitch. The one risk was the "why now" number beat: the spine wants an attributed figure, and I expected I might have to cut the beat (law 9) if no clean figure existed. [my input]

**3. What happened (including failures and reversals).**
- Web search verified the YC figure cleanly: TechCrunch, Mar 2025, reporting Jared Friedman and Garry Tan — a quarter of the W25 batch on 95% AI-written codebases. Kept the number beat (B08), attributed aloud and captioned "per Y Combinator". [record]
- Noted the reporting caveat (those founders are technical) and kept the film's claim inside it — the film only claims the tools are good enough for whole products. [judgment]
- Static QC first run: 7 clean, 2 warnings — B03/B05 "password" tags started at y=3.6, outside the ±3.3 safe area. Re-staged both drops inside the frame; second run 9/9 clean, 0 warnings, 0 errors. [record]
- Fixed a latent template bug while pasting iso_kit.py: `open_box` had a duplicated point making a degenerate quad (unused by this film's scenes, fixed for truthfulness). [record]
- Rewrote the B01/B02/B03/B04 narrations so every `until()` key phrase sits inside the first ~35% of its beat — nothing mid-motion at the clip midpoint under GATE T sampling. [judgment]
- `manim_layout_audit.py --curve-strict` cannot run in this VM (no Manim/pangocairo); deferred to Bear's Mac render pass, recorded in CHECKS-REPORT.md and CLAUDE-CODE-RENDER.md. [record]

**4. What I did.**
Built all 12 files: ACTS, SHOTLIST, FACTCHECK (12 claims, one attributed number, no invented statistics), make_sheet.py (asserts 13 beats, 180–300 s band, triggerWords/term-length/bookend checks), beat_sheet.json (13 beats, ~248 s est.), scenes.py (9 Manim scene classes), SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS ("no generation prompts"), CLAUDE-CODE-RENDER, README. Pushed all 12 via gh-put-file.py and verified each with a Contents API read (12/12 HTTP 200). Did not touch muse/FRICTIONAL.md, muse/README.md, or muse/QUEUE.md. No MP3/MP4/WAV/__pycache__/.DS_Store committed (removed the local __pycache__). [record]

**5. What Claude or another person contributed.**
The parent coordinator assigned the slug, title, pitch, and skill. The show-tell skill, iso kit, QC checker, and package conventions came from the brutalist.art toolkit and the finished how-to-ai films. I wrote every file; the AI contribution is the drafting, the narration design, the QC pre-review, and the web verification of the YC figure. No human contributed facts to this film. [record]

**6. What I understand now / still do not understand.**
I understand the full show-tell pipeline end to end now, including the midpoint-keying discipline and the thin-number attribution rule. I still do not know this film's chapter number in the How to AI queue (it is not listed in QUEUE.md) — set to 0 in the sheet; the coordinator assigns it. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live at `muse/youtube/how-to-use-ai/code-without-coding/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records 9/9 clean, 0 warnings, 0 errors. Next step: Bear renders narration (Kokoro am_onyx) + Manim on his Mac per CLAUDE-CODE-RENDER.md, runs the layout audit there, and publishes only on his explicit instruction. [record]

---

## 2026-10-04 — Film: "Your personal research assistant" (`muse/youtube/how-to-use-ai/personal-research-assistant/`)

**1. Date and what I was working on.**
2026-10-04. Built one pre-render film package for the humanitarians AI YouTube channel from scratch (NEW source, no mirror): "Your personal research assistant" — deep-research features: how to brief the AI well, read its answers, and what to distrust; companion to Film 21 "Trust, but verify". Pushed to `muse/youtube/how-to-use-ai/personal-research-assistant/`. [record]

**2. I tried / expected.**
I expected to use the assigned show-tell skill as-is, to ground the product facts via web search, and to follow the sibling show-tell film `make-it-interview-you-first`'s package conventions (beat-sheet format, bookend Remotion props, assertion pattern). [my input]

**3. What happened (including failures and reversals).**
- Stayed with **show-tell** (did not switch skills): each beat is one motion on a small cast (research desk, source pages, the report); the card test failed for every body beat, so zero cards, all drawings. [judgment]
- Fact-check research (2026-10-04) verified the durable claims: deep-research modes across the major chat AIs browse the web, read dozens of sources, return cited reports in minutes; Tow Center study on bad citations without uncertainty flags; Lily Ray's "AI slop loop" behind the "echo" beat; Stanford study on chatbots' narrow source range behind the "thin research" beat. No prices, versions, quotas, or statistics in narration by design. [record]
- make_sheet.py passed all assertions first run: 14 beats, 240.0 s (~4:00); BIDEA trigger contract, BDEFS ≤17-char term contract, BHTF prompt-read-in-full contract, BOUT outro contract all green. [record]
- QC gate: py_compile clean first try; static checker 10/10 clean · 0 warnings · 0 errors on the first run. Two layout defects caught by hand-review before QC (B01's decision card landed exactly on the dimmed topic card; B02's dimmed pile replacements misaligned with the shifted pile) — both fixed in scenes.py. [record]
- `manim_layout_audit.py --curve-strict` could not run in this VM (no Manim/pangocairo); deferred to Bear's Mac render pass. [record]
- All 12 pushes succeeded first try (no 409s); all 12 verified HTTP 200 and byte-identical via Contents API reads. [record]

**4. What I did.**
Wrote all 12 package files (ACTS.md, SHOTLIST.md, FACTCHECK.md with a real PASS/EXEMPT verdict table, make_sheet.py, beat_sheet.json — 14 beats, 10 body — scenes.py with 10 Manim scene classes B00–B09, SOURCES.md, BUILD-LOG.md, CHECKS-REPORT.md, PROMPTS.md, CLAUDE-CODE-RENDER.md, README.md); passed the full QC gate with zero warnings/errors; pushed all 12 via gh-put-file.py; verified each byte-identical via Contents API reads. [record]

**5. What Claude or another person contributed.**
The parent orchestrator supplied the assignment (slug, title, pitch, companion-film reference, film identity constants, audience rules, the 12-file convention, the QC gate, the FRICTIONAL.md format). Bear set the channel/persona/audience/skill rules. The show-tell SKILL.md supplied the bookend spine and drawing laws; sibling films make-it-interview-you-first (show-tell conventions) and trust-but-verify (companion + fact-check conventions) supplied the package patterns. Web sources supplied the fact-check. I wrote every file; the AI contribution is the drafting, research verification, and QC pre-review. [record]

**6. What I understand now / still do not understand.**
I understand the pure show-tell contract now: hesitant-writer BIDEA with verbatim trigger mechanics, the terms card, a zero-card body when the card test fails, the Your Turn composer with the prompt read in full, and the spoken outro. I set chapter_number 25 in the sheet metadata (next after the 24-film queue) — I do not know whether the coordinator wants a different index number for this post-queue film. [my input]

**7. Evidence and next step.**
Evidence: 12/12 files live at `muse/youtube/how-to-use-ai/personal-research-assistant/` on Humanitariansai/humanitarians-youtube-muse (verified HTTP 200 + byte-identical, 2026-10-04); CHECKS-REPORT.md records 10 clean · 0 warn · 0 error. Next step: Bear renders locally via CLAUDE-CODE-RENDER.md — Kokoro am_onyx narration, 10 Manim scenes + 4 Remotion bookends, `manim_layout_audit.py --curve-strict` (deferred from this VM) before the 4K render; never publish without his explicit instruction. [record]

---

## 2026-10-04 — Film build: "AI that sees" (`muse/youtube/how-to-use-ai/ai-that-sees/`)

**1. Date and what I was working on.**
2026-10-04. An extra film beyond the 24-film "How to AI" queue (all 24 Done): a pre-render package (script, Manim visuals, docs) for "AI that sees", the multimodal use cases that beat typing, companion to film 18 ("Just talk to it"); pushed to `muse/youtube/how-to-use-ai/ai-that-sees/`. [record]

**2. I tried / expected.**
I expected to keep the assigned show-tell skill and to conform the package to the companion film's 12-file conventions, which I had locally in `~/workspace/film-builds/how-to-ai/just-talk-to-it/`. I expected the QUEUE/README to hold a slot for this film; they did not (all 24 Done, no `ai-that-sees` entry), so I treated it as an extra and recorded that in the beat sheet's `series_note` instead of inventing a series number. [my input]

**3. What happened (including failures and reversals).**
- Studied `just-talk-to-it/`'s full 12-file package as the working example and conformed every file to it (make_sheet structure, beat-sheet metadata, QC-report format, CLAUDE-CODE-RENDER steps). [record]
- Checked `muse/QUEUE.md` and `muse/README.md` via the GitHub Contents API before authoring: no slot for this film; wrote `series_note: "Extra film beyond the 24-film How-to-AI queue (all 24 Done); companion to #18 'Just talk to it'"` rather than a film number. [judgment]
- Kept assigned skill show-tell: no beat passed the card test (every idea is a thing, a part, or a flow), so zero ShowTellCards; all 12 body beats are drawings. [judgment]
- Fact-checked image-attachment support against two mirrored Anthropic developer docs (verified 2026-10-04): attachment button + drag-and-drop for images, "Claude sees attached photos directly as part of your message", screenshots-of-bugs named as an attach use case. The six use cases and three photo rules are original craft guidance. [record]
- make_sheet.py passed all its assertions on the first run (16 beats, 12 manim, ~247 s inside the 170–280 s band; BDEFS terms ≤ 17 chars; hesitant-writer trigger contract holds). [record]
- Static QC passed first try: 12 scene classes clean · 0 warnings · 0 errors. Every `until()` phrase additionally verified verbatim-present in its beat's narration by script. [record]
- All 12 pushes succeeded via gh-put-file.py; all 12 verified live via Contents API reads (HTTP 200). Local __pycache__ removed, never pushed. [record]

**4. What I did.**
Wrote all 12 package files (16 beats, 12 manim, ~247 s; scenes.py with 12 Manim classes B00–B11, iso_kit pasted verbatim at the top per Gate A); passed the full QC gate with zero warnings/errors hidden or waived; pushed all 12 via gh-put-file.py; verified each via Contents API reads. [record]

**5. What Claude or another person contributed.**
The parent orchestrator supplied the assignment (slug, title, pitch, companion-film reference, audience, skill menu, the 12-file convention, the QC gate, the FRICTIONAL.md format, the no-version/no-pricing rule). Bear set the channel/persona/audience/skill rules. The companion film's package (just-talk-to-it, both locally and in the Humanitariansai repo) supplied the conventions I conformed to. I wrote every file; the AI contribution is the drafting, the fact-check pass, and the QC pre-review. [record]

**6. What I understand now / still do not understand.**
I understand the queue bookkeeping now: the 24-film "How to AI" queue is fully Done, so an out-of-queue companion film gets a `series_note` naming the companion rather than an invented film number — the coordinator owns numbering. I do not yet know whether Bear wants a `muse/README.md` index row for this film (I left README/QUEUE/FRICTIONAL.md untouched per the standing rule). [my input]

**7. Evidence and next step.**
Evidence: `muse/youtube/how-to-use-ai/ai-that-sees/` (12 files) verified live — all HTTP 200; CHECKS-REPORT.md records 12 clean · 0 warn · 0 error. Next step: Bear renders on his Mac per `CLAUDE-CODE-RENDER.md` (Kokoro `am_onyx` narration, Manim scenes, then `manim_layout_audit.py --curve-strict`, which could not run in the build VM) — never publish without his explicit instruction. [record]

---

## 2026-10-04 — Film: "The yes-man problem"

**1. Date and what I was working on.**
2026-10-04. One complete pre-render film package for the humanitarians AI YouTube channel: "The yes-man problem" (slug `the-yes-man-problem`) — sycophancy, when the AI agrees with you too much, and how to ask for pushback; companion to `when-its-confidently-wrong`. Pushed to `muse/youtube/how-to-use-ai/the-yes-man-problem/`. [record]

**2. I tried / expected.**
I expected to follow the assigned deep-explainer skill. Reading it end to end, the film's teaching problem (one insight + one mechanism + one playbook, ~3–6 minutes) fell outside deep-explainer's natural band (5–10 minutes, 30–50 beats, 4+ linked mechanisms), so I expected — and did — switch to ai-explainer with the reasoning recorded, as the companion film had done. [my input]

**3. What happened (including failures and reversals).**
- The deep-explainer → ai-explainer switch, recorded in BUILD-LOG.md with the doctrine citation (the skill's own "if the source is one insight, it's an ai-explainer"). [judgment]
- Research: verified the Sharma et al. 2023 sycophancy paper (abstract read in full) and OpenAI's April/May 2025 sycophancy postmortems live on 2026-10-04; the postmortem root cause is OpenAI's self-report, not independently verified, so the film states only the observable event (agreement dial too far, rollback within days). [record]
- Deliberately kept every number out of the narration — the research is cited qualitatively so the film cannot date or misstate a figure. [judgment]
- No QC failures: py_compile clean; all 9 Manim classes passed static_scene_check first run, 0 warnings / 0 errors. Two layout hazards (B08 chip row overflowing the ±6.3 safe area; three terracotta tags too wide at 32pt) were caught by hand-review before the check and fixed — recorded in CHECKS-REPORT.md, not concealed. [record]
- A stray `__pycache__` directory from py_compile was deleted locally before pushing; never committed. [record]
- The verification script's first attempt failed: `add_surrogate_to_request` needs the keyword-only `allowed_hosts` argument. Retried with `allowed_hosts=["api.github.com"]`; then 12/12 verified HTTP 200. [record]

**4. What I did.**
Built the full 12-file package: ACTS (four acts), SHOTLIST, FACTCHECK (all claims verified, no invented statistics), make_sheet.py (generates beat_sheet.json; all assertions pass — 13 beats, 9 body, 273.1s ≈ 4m33s), beat_sheet.json, scenes.py (9 Manim scene classes `<BID>_<Name>`, one per GRAPHIC body beat; the 4 bookends are REMOTION patterns), SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README. Pushed all 12 to `muse/youtube/how-to-use-ai/the-yes-man-problem/` and verified each with a Contents API read. [record]

**5. What Claude or another person contributed.**
The parent orchestrator assigned the film (slug, title, pitch, assigned skill, audience rules, film identity constants, the 12-file package convention, and the instruction to ground sycophancy claims in real research). Bear's standing identity constants (channel claude-liam, Liam persona, Kokoro am_onyx, Teardown register, @NikBearBrown watermark) and the "companion to when-its-confidently-wrong" framing shaped the film. The research itself is third-party (Sharma et al.; OpenAI). Everything else — script, visuals, fact-check write-ups, QC — is this build's work. [record]

**6. What I understand now / still do not understand.**
I understand the how-to-ai wave package convention now (REMOTION bookends + GRAPHIC body beats with `<BID>_<Name>` Manim classes) well enough to build it first-try clean. I still do not know whether Bear wants this film taken to a watchable slate cut on his Drive per the newer standing rule (MP3s/MP4 in the "00-muse" folder) — the assignment said pre-render package only, and I built exactly that. [my input]

**7. Evidence and next step.**
Evidence: 12 files verified live (HTTP 200 each) at `muse/youtube/how-to-use-ai/the-yes-man-problem/` on Humanitariansai/humanitarians-youtube-muse; CHECKS-REPORT.md records the clean gate. Next step: Bear renders narration (Kokoro am_onyx) and the review cut on his Mac per CLAUDE-CODE-RENDER.md, including the deferred `manim_layout_audit.py --curve-strict`. [record]
