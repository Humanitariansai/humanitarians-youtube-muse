# BUILD-LOG — Your song in a minute

## 2026-10-05 — package built (film-build worker subagent)

**Skill choice:** kept `show-tell` (assigned). The film is a textbook
show-tell: one simple isometric drawing per beat, minimal labels, Liam's
narration carrying every idea. No beat passed the card test (every beat is a
thing/part/flow best drawn with the film's own cast — a record landing, tags
dropping into a window, a playhead sweeping a waveform, a track wandering and
fizzling), so zero ShowTellCards. [judgment]

**Source:** NEW film, not a refactor — no mirror-repo source exists for this
pitch. Written from scratch: the trick (a birthday song in a minute), the
pipeline (description → music tool → song), the three ingredients (occasion,
subject, style), the loop (describe, listen, fix), the sweet spot (birthday,
jingle, lullaby), the limits (long songs wander; voices mangle words; under
three minutes), and the why-now number. [record]

**Beat design (12 beats, ~254 s est.):** BIDEA hesitant writer (naive "make
me a song" corrected into "a happy birthday song about dinosaurs" — the
correction is the three-ingredient ask), BDEFS (AI music tool / prompt /
synthetic voice), B00 hero (the finished song arrives as a vinyl record), B01
the pipeline, B02 the three ingredients (tags drop in one by one), B03 listen
to the draft (playhead sweeps the waveform), B04 the fix loop (arrow back to
the tool, fixed card + check), B05 the sweet spot (three small song cards),
B06 the limits (a long track wanders and fizzles; "under three minutes"),
B07 why now (44%, attributed, hero number + curve), BHTF composer exercise
(birthday song for Mia), BOUT spoken outro. [judgment]

**Fact work:** the one number (44% of new Deezer uploads fully AI-generated,
~75,000/day) verified via web search 2026-10-05 — Deezer newsroom Apr 2026,
corroborated by TechCrunch Jul 2026 (>50% on peak days). Attributed aloud
AND captioned ("per Deezer") per the thin-numbers law. The film deliberately
names no specific product in the narration (stays generic "an AI music tool")
so it doesn't go stale; Suno/Udio appear only in the SOURCES.md detection
note. No pricing tiers anywhere. [record]

**Pacing decision:** narrations were written so every `until()` key phrase
sits inside the first ~35% of its beat — nothing is mid-motion at the clip
midpoint under GATE T sampling. Four beats land their payoff after the
midpoint (B03's label ~88%, B04's fix ~71%, B06's "under three minutes"
~68%, B02's banner ~54%); each starts motion well clear of the 50% ± margin
window. The house `words/2.5` estimate runs ~1.6× long vs real Kokoro, so
phrase-keyed motion scales with the measured audio. [judgment]

**Voice-code guard:** make_sheet.py asserts every beat's `voice` is exactly
`am_onyx` — the "Muse"-as-voice bug that broke two Wave 5 films cannot
recur here. [record]

**New helpers in scenes.py:** `note()` (ink eighth note, drawn large enough
to read), `disc()` (vinyl record: dark disc for Gate V contrast, kraft label
ring, terracotta center dot), `song_card()` (finished-song card), `music_window()`
(generic AI music-tool window, grey title band per the house pattern),
`waveform()` (grey bars with gaps per GATE T). All drop starts were staged
inside the ±3.3 safe area (no off-stage starts for the static checker to
flag). [record]

**QC:** `py_compile` clean; `static_scene_check.py` 8/8 scenes clean,
0 warnings, 0 errors after one fix round (B03_ListenFirst failed first run
with "shapes never change": the MoveAlongPath sweep is move-only, which Gate
A's stub ignores — added the playhead to the opening FadeIn and a terracotta
ring that grows then fades after the sweep, a membership change after the
first play per the skill's documented fix). `manim_layout_audit.py
--curve-strict` cannot run in this VM (no Manim/pangocairo); deferred to
Bear's Mac render pass, recorded in CHECKS-REPORT.md and
CLAUDE-CODE-RENDER.md. [record]

**Push:** all 12 files pushed to `Humanitariansai/humanitarians-youtube-muse`
`muse/youtube/how-to-use-ai/your-song-in-a-minute/` via `gh-put-file.py`,
each verified with a Contents API read afterwards. Did not touch
`muse/FRICTIONAL.md`, `muse/README.md`, or `muse/QUEUE.md`. [record]

**Open for Bear:** render narration (Kokoro `am_onyx`) + Manim on his Mac per
CLAUDE-CODE-RENDER.md; run the layout audit there; never publish without his
explicit instruction.
