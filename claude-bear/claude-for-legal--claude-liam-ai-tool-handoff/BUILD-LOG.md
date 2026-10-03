# BUILD-LOG — claude-for-legal--claude-liam-ai-tool-handoff

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-ai-tool-handoff/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"the skill is ai-tool-handoff. >."`, `"Claude's job: >."`,
`"The SKILL.md is the spec — >."`, `"I want to >."` Its `source_skill` field
points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/ai-tool-handoff/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
a `corporate-legal` folder exists anywhere (identical defect class to the
`claude-for-legal--claude-liam-ai-inventory` and
`claude-for-legal--claude-liam-dsar-response` siblings already built in this
batch). So there were no real facts to carry over from the source, only a
topic (AI TOOL HANDOFF) and a shape (Teardown skill-teardown format, 7
beats: cold open, anatomy, pipeline, design tell, verdict, handoff, outro).

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what actually
finishes a handoff between a person and an AI tool — described generically
per the fresh-script Phase 1 rule ("when in doubt, describe behavior
generically") rather than inventing specific tool names, UI, or product
claims. No fact in the resulting script is Claude-specific or unverifiable.

Register re-registered Teardown -> Plain: the source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (a
handoff's three parts: scope, boundary, record) and both failure directions
(silence is not approval; a rewrite is not a failure) as properties of any
AI-tool handoff, never a verdict on any specific skill's design. Source's
BVDT verdict recap folded into a dedicated BCRY carry-out beat per
CARRY-OUT LAW (same disposition as prior redos in this factory). B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "finish" -> "start" — the naive
assumption that a returned result is a finished job, corrected to the fact
that delivery only starts the review). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off.

Added an anchor (B02 -> B03: a redlined contract page stamped
"MARKED — NOT ACCEPTED", returning stamped "FINAL" with a signature) and a
both-directions beat (B03) per this factory's PHASE 1 structure requirement
— the source (being unfilled) carried neither.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot.

## Built end to end this invocation

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   9.43s, B01 19.29s, B02 17.41s, B03 22.63s, BCRY 5.50s, BHTF 17.90s,
   BOUT 4.27s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `AITHB01Scene` /
   `AITHB02Scene` / `AITHB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00 (BrutalistHesitantWriter) via `remotion_scenes.py`.
   **One defect found and fixed:** the first invocation exceeded the
   shell's inline timeout and was killed mid-pipeline — after the raw
   fixed-length (606 frames / 30fps = 20.2s) composition had rendered but
   *before* the post-render head-trim (`extend_clip_to_duration`, which
   crops/pads the raw render to `actual_duration_s`) ran. This left a
   stale, un-trimmed 20.245s `media/B00.mp4` on disk; because the file
   already existed, the next `remotion_scenes.py` invocation skipped B00
   entirely ("filled already") rather than re-conforming it — silently
   leaving a 20s clip in a 9.43s-audio beat. Caught by explicitly probing
   `media/B00.mp4`'s duration against `actual_duration_s` per the
   TIMING LAW self-check (not by the pipeline itself). Fixed by deleting
   the stale file and re-running with `--force` and a longer foreground
   timeout so render + trim completed as one atomic step in a single
   invocation; confirmed `media/B00.mp4` = 9.43s.
4. B00 verified directly: pulled frames at t=8.5s/9.2s — the correction
   ("finish" -> "start") is already complete and visible, full question
   legible: "Can I just have Claude start this contract redline?"
5. Rendered BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground —
   clean single pass, no timeout issues (smaller compositions).
6. `compile.py --review` -> 7/7 real (no slate), review-cut master
   `claude-for-legal--claude-liam-ai-tool-handoff-slate.mp4`, 97.4s,
   mean_volume -24.0 dB (already passing GATE AUDIO).

## Gates

- **TIMING LAW (B00):** narration 30 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **9.43s**, clears the ≥8s floor. Correction
  visible on-screen by t=8.5s (confirmed via direct frame read).
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840×2160).
- **GATE T (type_check.py):** PASS — 0 FAILs, no findings to root-cause.
- **Gate V (frame QC):** pulled frames every 5s across the full 97.4s
  runtime (19 frames) and read every one directly. All legible, safe
  inset respected, no text overlap, no defects found. `folderLabel` on
  BHTF's `ClaudeComposerAsk` correctly reads `@HumanitariansAI` (explicit
  prop set — avoiding the hardcoded-default-handle defect logged in
  sibling `books--claude-liam-legal-finance`'s BUILD-LOG).
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg volumedetect,
  well above the -40 dB floor), max -3.0 dB.
- ffprobe: master duration 97.438s; mp4 mtime (1788002539) newer than
  beat_sheet.json mtime (1788002503).

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family (e.g.
`claude-for-legal--claude-liam-ai-inventory`).

**Non-blocking note (compile.py motion histogram):** remotion:4 graphic:3
— remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

## Playlist resolution

`SUBJECT.json`'s `family: "claude-for-legal"` has no literal entry in
`skills/make/hai-simple/loop/playlists.json`'s map (verified directly
against the map file — no key is a prefix of `claude-for-legal`). Per the
map's documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to the skill name itself: `hai-simple` is a literal
key in the map, resolving to **Claude Basics** — same resolution as the
`ai-inventory` sibling (this reel is a generic AI-tool-handoff explainer,
not specifically about Claude plugins/skills infrastructure the way the
`books--*` family's "Extending Claude" precedent was).

Metadata file written: `claude-for-legal--claude-liam-ai-tool-handoff.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
