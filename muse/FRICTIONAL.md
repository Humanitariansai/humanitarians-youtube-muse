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
