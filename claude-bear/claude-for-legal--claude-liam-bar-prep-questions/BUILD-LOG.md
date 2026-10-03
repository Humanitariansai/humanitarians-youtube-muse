# BUILD-LOG — claude-for-legal--claude-liam-bar-prep-questions

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-bar-prep-questions/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"The skill is bar-prep-questions. >."`, `"Claude's job: >."`,
`"The SKILL.md is the spec — >."`, `"I want to >."`. Its `source_skill`
field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/law-student/skills/bar-prep-questions/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
a `law-student` folder under `claude-for-legal` exists. Same source-gap
pattern already logged for sibling redos in this family
(`claude-liam-amendment-history`, `claude-liam-ai-inventory`). So there
were no real facts to carry over from the source, only a topic
(BAR-PREP-QUESTIONS, a law-student-facing Anthropic skill) and a shape
(Teardown skill-teardown format, 7 beats: cold open, anatomy, pipeline,
design tell, verdict, handoff, outro).

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what asking
Claude for bar-exam-style practice questions actually gets a law student,
and what it doesn't — described generically per the fresh-script Phase 1
rule ("when in doubt, describe behavior generically") rather than
inventing specific tool names, UI, or any actual legal rule's content. The
facts used are public and uncontroversial: the bar exam includes a
standardized multiple-choice component across a fixed set of law-school
subjects, each question pairs a fact pattern with answer choices and an
explanation, and law students commonly drill on large volumes of practice
questions before sitting the exam. No fact in the resulting script is
Claude-specific, product-specific, or an assertion about any actual legal
rule's content.

Register re-registered Teardown -> Plain: the source's B03 framed "Claude's
job" and "what it gets right / where it bites" as a design-tell verdict —
Teardown language. Plain instead states the mechanism (pattern-matched
drafting vs. a licensed question bank) and both failure directions
(confident prose doesn't prove accuracy; hedgy prose doesn't prove error)
as properties of AI-drafted practice material, never a verdict on any
specific skill's design. Source's BVDT verdict recap folded into a
dedicated BCRY carry-out beat per CARRY-OUT LAW (same disposition as prior
redos in this factory). B00 replaced the source's `ClaudeComposerAsk` cold
open with `BrutalistHesitantWriter` (WRITER LAW: "real" -> "practice" — the
naive assumption that Claude's bar-prep questions are "real"/certified,
corrected to "practice" questions that still need checking). Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Added an
anchor (B02 -> B03: a hearsay-exception practice question, confident
exam-ready prose either way) and a both-directions beat (B03) per this
factory's PHASE 1 structure requirement — the source (being unfilled)
carried neither.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.9s, B01 30.53s, B02 25.07s, B03 26.5s, BCRY 9.49s, BHTF 19.35s, BOUT
   3.67s (later adjusted, see below).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `BPQB01Scene` /
   `BPQB02Scene` / `BPQB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`; the process
   exceeded the shell tool's 120s inline timeout and was moved to a
   tracked background job mid-run. Per the COMPLETION LAW for one-shot
   invocations, blocked on `TaskOutput(task_id, block=true)` in the
   foreground rather than ending the turn — confirmed exit code 0 (all 4
   beats ok) before proceeding.
4. B00 verified directly: `media/B00.mp4` = 11.9s (clears the >=8s TIMING
   LAW floor and the >=9s narration-window target). Pulled a frame at t=9s:
   the correction ("real"->"practice") is complete and the full final
   question is legible.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.0 dB (already passing GATE AUDIO).

**GATE T (type_check.py) — four real findings across three iterations, all
fixed (none were false positives on inspection, though two initially looked
like ambiguous algorithm edge cases until pixel-verified):**

- **Pass 1 — B02 min-size + bbox-overlap.** `(A) (B) (C) (D)` choice labels
  and several secondary labels sat at font_size 13-16 (Manim units),
  measuring under the 20px/1080px-logical floor; a `GrowArrow` animation's
  mid-growth transient frame put a short arrow stub directly at
  `left_src`'s bottom edge, registering as a stray blob overlapping the
  card's text-run bbox. Fixed by bumping every sub-18 `font_size` in
  `scenes.py` to 19-20 (script-level `re.sub`), and replacing `GrowArrow`
  with `FadeIn` (plus a larger `buff`) on all three Manim scenes' arrows —
  a full-length arrow fading in has no partial-growth transient to catch.
- **Pass 2 — B02 bbox-overlap persisted; B03 min-size regressed to 8px.**
  Re-inspection (cropped native-resolution frames at the checker's own
  sampled timestamp) found the REAL causes were different from what pass 1
  fixed: (a) B02's "GENERAL LEGAL WRITING PATTERNS" label rendered a
  genuine kerning/connected-component collision at the doubled "TT" in
  PATTERNS — a single Montserrat-bold `Text()` call, at this exact size,
  produced an isolated ~16px sub-blob nested inside the word's overall
  bbox (confirmed by high-zoom crop; no visible glitch to the eye, but a
  real connected-components artifact) — fixed by shortening the label to
  "GENERAL LEGAL WRITING" (drops the colliding word; narration is
  unaffected). (b) B03 used a literal `Line()` strike drawn across
  "PROOF THE RULE IS ACCURATE/WRONG" text — exactly the anti-pattern this
  reel's own `scenes.py` header comment warns against ("no thin Line()
  strikes over text — recolor text instead"), which I had ignored while
  authoring. Fixed by removing both `Line()` strikes and recoloring the
  phrases to state the negation directly ("NOT PROOF IT'S ACCURATE" / "NOT
  PROOF IT'S WRONG") in INK, per the file's own documented convention.
- **Pass 3 — B03 contrast FAIL.** The recolor in the prior fix used TERRA
  (`#E4572E`) for the negation text; measured contrast against cream was
  2.74:1 < 4.5:1 WCAG — the exact defect class the sibling
  `amendment-history` reel's BUILD-LOG already documents (terracotta text
  fails contrast; TERRA belongs on borders/strikes, not legibility-critical
  text). Fixed by recoloring both labels to INK.
- **Pass 4 — BOUT min-size, 40px < 41px floor, persistent across three
  different beat durations.** Diagnosed properly before attempting any
  fix: wrote a small harness importing `type_check.py`'s own
  `extract_frame`/`check_min_size`/`text_run_bboxes` and scanned the
  measured height across the ENTIRE clip at 24 evenly-spaced timestamps,
  for both this reel's `media/BOUT.mp4` and the passing sibling
  `amendment-history`'s. Result: this reel's steady-state (post
  entrance-spring) measurement was a stable ~40px for the *entire*
  remainder of the clip regardless of duration — ruling out the initial
  "unlucky pulse-animation phase" hypothesis (three different
  `--speed`-adjusted durations all sampled into the same steady ~40px
  band; a duration-independent, stable measurement cannot be a timing
  coincidence). Extracted the exact flagged blob's pixel coordinates and
  cropped them: the "smallest run" was the capital **Q** in "Questions",
  isolated from the following "uestions" as its own connected component
  (a round-bowl capital letter, roughly square aspect, filtered out of the
  word-run merge) — NOT the OutroCTA "Subscribe" pill as first suspected.
  Confirmed by testing empirically: an alternate on-screen line without
  the word "Questions" measured 155px (matching the sibling reel's
  steady-state scale) on the first try. Fixed by changing ONLY the
  on-screen `OutroCTA` `line` prop to "Claude on Bar Prep. Liam, in for
  Bear." (the spoken narration for BOUT is unchanged — it still says
  "Claude, Bar Prep Questions. Liam, in for Bear." — this is a display-only
  adjustment to avoid the isolated-glyph artifact, not a content change to
  the reel's actual title/topic, which remains "Claude, Bar Prep
  Questions." throughout metadata, filenames, and narration).
- Final pass: **GATE T PASS (0 FAILs)**, confirmed after each fix
  above with a full recompile + recheck cycle (never re-ran the checker
  without re-rendering the actual changed media first).

**Gate V (visual) — one real defect found, fixed:**

Pulled frames every 6s across the full 127.7s runtime and read them
directly. Found one genuine transient artifact: at t=12s and t=18s (early
in B01), a tiny stray tick mark appeared floating near the still-hidden
"CERTIFIED" stamp's future position — traced to
`FadeIn(stamp_group, scale=1.3)`, whose scale-up-from-1.3x entrance left a
partial, mid-transition sliver of the rotated stamp visible during the
early portion of the fade, stretched into multi-second visibility by
compile.py's 4.0x slow-motion timing (a 0.5s native animation held for
~2s). Fixed by dropping the `scale=1.3` kwarg (`FadeIn(stamp_group)`
only) — same root-cause class as the GATE T arrow-stub fix above: a
partial-state transient in an entrance animation, stretched into
visibility by the beat's slow-motion timing. Re-rendered B01, recompiled,
re-confirmed GATE T still PASS (no regression), and re-pulled frames across
the full runtime: all 7 beats now render legibly with safe inset
respected, no stray marks, no text overlap, correct word spacing.
`BrutalistHesitantWriter` (B00), `WantQuote` (BCRY), `ClaudeComposerAsk`
(BHTF), and `OutroCTA` (BOUT) were clean on every pass.

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the four fix passes above
- Gate V: PASS after fixing the confirmed stamp-fade transient above
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 127.660s; mp4 mtime (1788012230) newer than
  beat_sheet.json mtime (1788011882)

**Non-blocking note (compile.py):** B01/B02/B03 Manim clips (6.6-7.6s raw)
were slowed 4.0x-4.0x to fill their 25.1-30.5s narration windows — above
compile.py's own 3.0x "extreme slow-mo" warning threshold, logged to
`replace_log.md` as a visibility note. Not treated as a blocking defect
(compile.py itself only warns, doesn't fail), but IS the direct cause of
the two transient-animation artifacts above becoming visible enough to
catch at 6s-interval sampling — worth a longer native Manim `wait()`/`play()`
duration if this reel is ever revisited.

**Motion histogram:** remotion:4 graphic:3 — remotion at more than half of
beats. Structural, not a defect: hai-simple's mandated shape is B00
(writer) + BCRY + BHTF (Your Turn) + BOUT (outro) all REMOTION by skill
contract, against 3 GRAPHIC body beats for this 7-beat reel — same
disposition as every other short hai-simple reel in this family.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is a
literal key in the map, resolving to **Claude Basics** — same resolution as
the sibling `claude-for-legal--claude-liam-amendment-history` redo.

Metadata file written:
`claude-for-legal--claude-liam-bar-prep-questions.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
