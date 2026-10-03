# BUILD-LOG — claude-for-legal--claude-liam-build-guide

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-build-guide/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `build-guide`.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its skill-specific
"Claude's job: ___" fill — the literal placeholder `>` survives verbatim in
four beats (B00, B03, BVDT, BHTF), confirmed by comparing against sibling
sheets in the same family (`claude-liam-legal-hold` DID get its fill;
`claude-liam-nda-review` shows the identical unfilled `>` bug). The SKILL.md
build-guide was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/build-guide/SKILL.md`)
does not exist on this machine — confirmed by `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`legal-clinic/` directory). This is NOT a "genuine blocker that halts the
build" per the completion law, because the source DOES establish real,
generic, true facts about how a Claude skill works (a folder Claude reads
before it acts, one file — SKILL.md — read top to bottom and executed step
by step, and the specification semantics: repeatable results in exchange
for a hard limit at the file's edge) — those facts are what carried over.
What did NOT carry over, because it was never actually present in the
source: any specific claim about what build-guide's legal procedure
actually does. This redo treats "build-guide" literally and generically —
the named example of a skill-shaped folder — and never asserts an invented
legal-specific process. Logged in QUESTION.md and SCRIPT.md as well.

**Facts kept unchanged (from the source, where present):** a skill is a
folder Claude reads before it acts; the whole routine lives in one file
(SKILL.md); Claude reads it and executes the file's steps in order, with no
branching unless the file itself branches; a skill is a specification, not
a capability — its payoff is repeatable results, its limit is anything the
file never covers.

**New content added to meet hai-simple's spine (not in the source, but not
invented legal-specific fact either):** the source has no explicit
wrong-guess, anchor, or both-directions beat (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW all require their own beat). Added: B01 (stakes —
"a new skill" sounds like an upgrade), B02 (wrong guess broken with a
falsifying case — delete the skill's folder, nothing is forgotten, because
there was nothing to learn), B06 (anchor payoff — restates the design tell
against the named anchor), B07 (both directions — following a file exactly
proves nothing about the routine's quality; improvising proves nothing
about breakage). B03/B04/B05 carry the source's anatomy/pipeline/design-tell
facts forward, with B03 now also serving as the anchor plant (build-guide's
single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion to satisfy hai-simple's mandatory six-move spine, not a scale
mismatch (contrast the 37-beat deep-explainer sources redone at 26 beats on
other siblings in this loop).

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a new
skill" means the model itself learned something. Typed text: "Claude
learned a new / skill called build-guide. / What is a skill?", trigger
"learned" → replacement "was given", ending on the real question. Audio
9.81s (Remotion extended to 9.8s) — clears the ≥8s WRITER LAW floor with
margin; verified on a late frame that the correction resolves and the full
question types out to "What is a skill?" before the beat ends.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" renderer pattern from the `books--claude-liam-building-plugins`
sibling redo (title + labeled chips, optional arrows/strike/accent +
caption), adapted in this reel's own `scenes.py`. Anchor pair: B03 plants
`build-guide/` + `SKILL.md` as two plain chips; B06 returns the identical
composition with `SKILL.md` accented. Close: BCRY `WantQuote` (carry-out),
BHTF `ClaudeComposerAsk` (explicit `folderLabel: "@HumanitariansAI"` — the
known ClaudeComposerAsk-defaults-to-@NikBearBrown bug, worked around per
precedent), BOUT `OutroCTA` (@HumanitariansAI). All four Remotion + WantQuote
component prop schemas verified renderable via `./art scenes --check` before
authoring the sheet (GATE L).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (11 beats), `scenes.py`, `render_scenes.py`. Ran
`generate_audio_kokoro.py` (11/11 beats, am_onyx, $0.00) — measured
durations became the clock. Rendered 7 Manim beats and 4 Remotion beats via
`remotion_scenes.py`, both in the foreground, waiting on exit code each time
(the `remotion_scenes.py` call auto-backgrounded past the tool's 120s
timeout; blocked on it explicitly with TaskOutput rather than ending the
turn, per the COMPLETION LAW — exit 0, all 4 beats confirmed rendered
before moving on).

**GATE T (type_check.py) first pass: 3 FAILs**, diagnosed by calling the
checker's own `text_run_bboxes`/`labeled_blobs`/`check_kerning_sanity`
functions directly against rendered frames rather than guessing from the
report text:

1. **B01 bbox-overlap + B05 bbox-overlap/min-size**: both traced to a
   single isolated word rendering as its own disconnected pixel blob,
   nested inside the larger text run's bounding box, which the checker
   reads as "two labels printing on top of each other." B01's cause: the
   lone single-letter word "A" in "CLAUDE HAS A NEW SKILL" sits with
   unusually wide Pango word-spacing on both sides at this chip's font
   size, isolating it into its own tiny run. B05's cause: the long label
   "OFF THE MAP OUTSIDE THE FILE" was compressed to fs=17 (below the 20px
   floor) to fit the chip, and a letter run inside it (near "OUTSIDE")
   similarly detached. **Fixed at the root** by rewording, not by touching
   the checker: B01's chip → "CLAUDE HAS NEW SKILLS" (drops the bare "A");
   B05's second chip → "OFF THE MAP" (short enough to render at full
   size). Re-verified via direct `text_run_bboxes` call: both chips now
   produce exactly one run each, no stray blobs.
2. **B07 kerning**: a single row of 4 chips (2 claim→conclusion pairs, no
   arrow across the middle gap) put a long blank horizontal span on the
   frame's single densest text row; the checker's pixel-level inter-glyph
   gap analysis has no concept of "separate chip labels sharing a row" and
   read the blank span as a Pango gappy-letter defect. Tried adding arrows
   across each pair (still failed — the arrow line is too thin to reliably
   register across the exact scanline the checker samples). **Root-cause
   fix**: replaced the single 4-chip row with a new `render_chip_stack`
   layout — each claim/conclusion pair stacked vertically with its own
   arrow, both pairs in one column — so no two chip labels ever share a
   horizontal text row. Re-verified: `check_kerning_sanity` now returns
   PASS ("too few letter runs for gap analysis," i.e. each row has only
   one short phrase, exactly the intended diagram). Visually this reads
   *better* than the original side-by-side layout, not just gate-clean.
   No change was made to `type_check.py` or its exemption tables — every
   fix was a content/layout change in this reel's own `scenes.py`.

**GATE T second pass: PASS** (0 FAILs, 0 sweep, 0 shape).

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media). `claude-for-legal--claude-liam-build-guide.mp4`,
101.9s. One non-blocking WARNING carried through both compiles: GRAPHIC
beats are 7/11 (63%), over the toolkit's ~40% "pantry cap" motion-diversity
guidance (MOTION.md) — noted, not treated as a gate; this reel is
legitimately diagram-heavy (a skill's anatomy/mechanism/spec argument reads
naturally as labeled-chip diagrams) and every GRAPHIC beat is original,
locally-rendered Manim, not pantry/stock footage.

**Gate V (visual QC):** pulled ~2fps frames across the full runtime and read
one frame per beat by hand — all legible, correct chip content, safe insets,
no overlapping text, the B03→B06 anchor pair visually identical as intended,
B07's restructured stack reads cleanly. B00's correction frame confirmed
twice (mid-type and final).

**Audio presence:** `ffmpeg -af volumedetect` on the compiled master:
mean_volume **−24.1 dB**, max_volume −3.0 dB — comfortably clears the
−40 dB floor.

**`./art final` re-run:** GATE T PASS confirmed a second time on the final
master; same 3840×2160 output, same audio gate. Master mtime (11:29) is
newer than beat_sheet.json's last content edit (11:16) — beat_sheet.json was
NOT touched after this point, per the "never touch beat_sheet.json after
compile" law; any further fix from here would require a full recompile.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent directory),
which resolves to **"Claude Basics."** Not the bare "Claude," per the
PLAYLIST LAW.

**Delivery:** `claude-for-legal--claude-liam-build-guide-4k.mp4` created —
a copy of the compiled master, which was already genuine 3840×2160 (the
Remotion beats are natively 4K; the Manim beats are 1080p source upscaled
into the 4K canvas by the compile step itself, the same as every other
GRAPHIC beat in this pipeline). Wrote `claude-for-legal--claude-liam-build-guide.md`
(YouTube description, @HumanitariansAI, playlist "Claude Basics", direct
code link, AI disclosure). Ran `deliver.py --push` to stage
`DELIVERY/claude-for-legal--claude-liam-build-guide/` and commit text
artifacts to the humanitarians-youtube clone under
`claude-bear/claude-for-legal--claude-liam-build-guide/`.

**Status: DONE.** Review cut passes every gate (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Source-fidelity gap logged
above and in QUESTION.md/SCRIPT.md/the description's "Deliberately not
claimed" section — nothing about the actual legal-clinic build-guide
procedure is asserted anywhere in this reel.
