# BUILD-LOG — Tell the AI who to be

## 2026-10-03 — package built (subagent, film #2 of 24)

**Skill choice:** kept `show-tell` (assigned). The film is a textbook show-tell:
one simple isometric drawing per beat, minimal labels, Liam's narration carrying
every idea. No beat passed the card test (every beat is a thing/part/flow best
drawn with the film's own cast), so zero ShowTellCards. [judgment]

**Source:** REFACTOR of the mirror repo's
`claude/claude-for-education/claude-liam-prompt-tutorial-lesson-03-role-prompting`
(Kore persona, technical/course audience). Kept the argument — role as register
calibration across four axes, role vs persona, the "does the role change what
counts as a good answer?" test — and the source's canonical examples
(pediatric oncologist / pathologist; tax attorney / Marcus). Rewrote every
narration line and every visual for a smart general audience; dropped the
verdict card and the technical framing. [record]

**Beat design (11 beats, ~242 s est.):** BIDEA hesitant writer (naive request
corrected into a role prompt — the correction is the subject), BDEFS (role
prompt / register / persona), B00 hero (the tag lands on the prompt, slides
into Claude), B01 four dials = register (not a costume), B02 mechanism demo
(tutor swings the dials, answer changes, no new facts), B03 the two-doctors
experiment, B04 role vs persona (tag vs costume), B05 the two-piles test,
B06 specific-beats-vague, BHTF composer exercise, BOUT spoken outro. No
"why now" number beat — no fact-checked figure exists for this topic, and law 9
says cut filler. [judgment]

**Pacing decision:** narration drafts were rewritten twice so that every visual
beat keys (via `until()`) to a phrase inside the first ~30% of its narration.
The house `words/2.5` duration estimate runs ~1.6× long vs real Kokoro
(~20 chars/s, confirmed against the source lesson's measured audio), so fixed
run-time choreography would have put motion on the GATE T midpoint under real
audio. Phrase-keyed motion scales with the measured audio instead. [judgment]

**QC:** `py_compile` clean; `static_scene_check.py` 7/7 scenes clean, 0 warnings,
0 errors, first run — no failures to fix. `manim_layout_audit.py --curve-strict`
cannot run in this VM (no Manim/pangocairo); deferred to Bear's Mac render
pass, recorded in CHECKS-REPORT.md and CLAUDE-CODE-RENDER.md. [record]

**Push:** all 12 files pushed to
`Humanitariansai/humanitarians-youtube-muse`
`muse/youtube/how-to-use-ai/tell-the-ai-who-to-be/` via `gh-put-file.py` and
each verified with a Contents API read afterwards. Did not touch
`muse/FRICTIONAL.md`, `muse/README.md`, or `muse/QUEUE.md`. [record]

**Open for Bear:** render narration (Kokoro `am_onyx`) + Manim on his Mac per
CLAUDE-CODE-RENDER.md; run the layout audit there; never publish without his
explicit instruction.
