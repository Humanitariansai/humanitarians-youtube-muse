# BUILD-LOG — claude-for-legal--claude-liam-amendment-history

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-amendment-history/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"The skill is amendment-history. >."`, `"Claude's job: >."`,
`"The SKILL.md is the spec — >."`, `"I want to >."`. Its `source_skill`
field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/commercial-legal/skills/amendment-history/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
a `commercial-legal` folder exists anywhere. Same source-gap pattern
already logged for the sibling `claude-for-legal--claude-liam-ai-inventory`
redo in this family. So there were no real facts to carry over from the
source, only a topic (AMENDMENT-HISTORY, an Anthropic skill for legal AI
governance) and a shape (Teardown skill-teardown format, 7 beats: cold
open, anatomy, pipeline, design tell, verdict, handoff, outro).

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what "amendment
history" means for a legal document and why the original document alone
can't answer what's currently in force — described generically per the
fresh-script Phase 1 rule ("when in doubt, describe behavior generically")
rather than inventing specific tool names, UI, or product claims. No fact
in the resulting script is Claude-specific or unverifiable.

Register re-registered Teardown -> Plain: the source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (clause-
level supersession through an amendment chain) and its failure modes (an
untouched clause isn't missing; an amendment existing doesn't prove it
touched a given clause) as properties of tracking amendments, never a
verdict on any specific skill's design. Source's BVDT verdict recap folded
into a dedicated BCRY carry-out beat per CARRY-OUT LAW (same disposition as
prior redos in this factory). B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` (WRITER LAW: "original" ->
"current" — the naive assumption that the original signed document still
governs, corrected to the fact that the current state depends on every
amendment since). Close re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off. Added an anchor (B02 -> B03: a lease's notice-period
clause, 30 -> 60 -> 45 days, resolved to 45 and only for that clause) and a
both-directions beat (B03) per this factory's PHASE 1 structure requirement
— the source (being unfilled) carried neither.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.09s, B01 17.49s, B02 17.43s, B03 20.12s, BCRY 11.37s, BHTF 14.68s,
   BOUT 3.43s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `AMHB01Scene` /
   `AMHB02Scene` / `AMHB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`; the process
   exceeded the shell tool's 120s inline timeout and was moved to a
   tracked background job mid-run. Per the COMPLETION LAW for one-shot
   invocations, blocked on `TaskOutput(task_id, block=true)` in the
   foreground rather than ending the turn — confirmed exit code 0 (all 4
   beats ok) before proceeding.
4. B00 verified directly: `media/B00.mp4` = 11.1s (meets the >=8s TIMING
   LAW floor, and clears the >=9s narration-window target). Pulled a frame
   at t=9s: the correction ("original"->"current") is complete and the
   full final question is legible.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.0 dB (already passing GATE AUDIO).

**GATE T (type_check.py) — one real finding, fixed (not a false positive):**

- First pass: FAIL (1 pixel beat, contrast). B03's mid-clip sample frame
  (t=dur*0.5 of the raw `manim/B03.mp4`, a transitional frame mid-Transform)
  measured fg/bg contrast 3.27:1 < 4.5:1 WCAG for the terracotta
  (`#E4572E`) "NOTICE: 45 DAYS" text on the cream ground — computed the
  WCAG relative-luminance contrast by hand from the reported RGB samples
  and confirmed the finding is real (terracotta text genuinely fails 4.5:1
  against this ground; verified computation ≈3.27:1). Traced two more
  instances of the same terracotta-on-cream text-legibility defect by
  grepping `scenes.py` for `color=TERRA`: B01's "DAY ONE" stamp label and
  B03's "check its own chain" split-card label. Fixed all three by
  recoloring the text to `INK`, keeping `TERRA` only on borders/strikes
  (the accent element, not the legibility-critical text) — consistent with
  "one terracotta moment per beat" already being satisfied by the border.
- Second pass: **PASS (0 FAILs)**.

**Gate V (visual) — one real defect found across two beats, fixed:**

Pulled frames every 5s across the full 96.6s runtime and read them
directly. Found a genuine text-rendering defect, not a false positive:
Manim's `Text()` rendered the inter-word space as ~0 width for two short
ALL-CAPS BOLD SANS labels — B01's "DAY ONE" stamp rendered as "DAYONE", and
B02/B03's "AMENDMENT 1"/"AMENDMENT 2" card headers rendered as
"AMENDMENT1"/"AMENDMENT2" — confirmed on multiple frames across both
beats. Other multi-word labels in the same scenes, at other sizes/weights/
cases (e.g. "ORIGINAL CONTRACT", "check its own chain", "original still
governs"), rendered with normal spacing, so this reads as a font/size/
weight/case-specific Pango-level space-collapse rather than a universal
font problem. Root-caused to no clear single cause; fixed pragmatically by
adding a `_spaced_text()` helper in `scenes.py` that splits a multi-word
label into separate `Text()` mobjects and `arrange(RIGHT, buff=...)`s them
— a guaranteed physical gap independent of the font's internal space-glyph
metrics — and applied it everywhere a short ALL-CAPS BOLD label carries an
embedded space (B01's "DAY ONE", B02/B03's "AMENDMENT 1"/"AMENDMENT 2").
Re-rendered all three Manim beats, recompiled, re-ran GATE T (still PASS
after the fix — no regression, since the terracotta-text fix above was
folded into the same re-render pass), and re-pulled frames across the full
runtime: all 7 beats now render legibly with safe inset respected, correct
word spacing, and no text overlap anywhere. B00's `BrutalistHesitantWriter`
writer card, BCRY's `WantQuote` carry-out, BHTF's `ClaudeComposerAsk`
composer card, and BOUT's `OutroCTA` outro were clean on both passes.

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component behavior
already logged unremarked in sibling reels in this family (e.g.
`claude-for-legal--claude-liam-ai-inventory`,
`claude-code--claude-liam-writing-rules`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after fixing the confirmed terracotta-on-cream
  contrast defect above
- Gate V: PASS after fixing the confirmed inter-word space-collapse defect
  above
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: duration 96.617s; mp4 mtime (1788006531) newer than
  beat_sheet.json mtime (1788005954)

**Non-blocking note (compile.py):** B01/B02/B03 Manim clips (8.0-8.8s raw)
were slowed 1.97x-2.53x to fill their 17.4-20.1s narration windows — under
compile.py's own 3.0x "extreme slow-mo" warning threshold (which would have
logged a REPLACE-LOG entry), so not flagged as a defect by the tool itself;
noted here for visibility rather than as a blocking finding.

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
the sibling `claude-for-legal--claude-liam-ai-inventory` redo.

Metadata file written:
`claude-for-legal--claude-liam-amendment-history.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
