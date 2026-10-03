# BUILD-LOG — claude-basics--claude-constitution-one-narrow-safety-rule-make

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/claude-constitution-one-narrow-safety-rule-make/beat_sheet.json`
(an unbuilt Teardown-register scaffold — 0/8 beats filled, no SCRIPT.md).
Question, facts, and beat count (8) carried over unchanged: training a
narrow behavioral constraint implicitly trains an identity claim ("I am the
kind of thing that does X"), and that identity acts as a prior over every
later behavior; anchor case: a rule to always recommend a licensed
professional in mental-health conversations teaches Claude "I protect
myself first, not this person" — a belief that leaks into unrelated
interactions; second case (folded into the anchor payoff beat): a model
trained never to give medication dosages hedges unrelated first-aid
questions. B00 replaced a `FormBCard` cold open with `BrutalistHesitantWriter`
(WRITER LAW: "behavior" -> "identity"); the source's audit prompt moved
verbatim to BHTF as the Your Turn prompt. Register re-registered
Teardown->Plain (the source narration carried no actual verdict, so no
judgment needed removing). Close/outro re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Source's B05 beat dropped as a
verbatim restatement of B03 (identical narration text in the source); its
content is already carried by B03/B04. No source beat was `ai-video-prompt`,
pantry, or a human-drop slot (all were already `FormBCard`/`ClaudeComposerAsk`/
`ClaudeTitleOutro` Remotion shapes, just unbuilt), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00 (WRITER LAW covers that anyway).

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`. Durations: B00
   12.03s, B01 19.33s, B02 21.03s, B03 32.28s, B04 25.26s, BCRY 6.59s,
   BHTF 19.84s, BOUT 5.89s.
2. Wrote `scenes.py` (4 Manim scenes, B01-B04) sized to the measured
   durations, and `render_scenes.py`; rendered all four in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` (foreground; one
   invocation exceeded the shell's 2-minute default and was auto-moved to a
   tracked background task — blocked on `TaskOutput` for its exit code
   rather than ending the turn or guessing at the result).
   B00 TIMING LAW check found a real defect on the first pass: at the
   original hesitation params (mistakeRate 6, hesitateBetween 22, charMs 55)
   the writer's full performance (typing + the trigger-word swap) needed
   longer than the 12.03s beat, and `remotion_scenes.py`'s
   `extend_clip_to_duration` truncates with `ffmpeg -t`, so the render cut
   off mid-typing — "behavior" was fully typed but the correction to
   "identity" never appeared, confirmed by pulling frames at 10.5s/11.9s/the
   clip's last frame. Fixed by speeding up the performance (mistakeRate 2,
   hesitateWithin 1, hesitateBetween 6, charMs 36) and re-rendering; verified
   `media/B00.mp4` = 12.03s (>= 8s TIMING LAW) and the correction
   ("behavior" -> "identity") settles on screen by 9.5s, well inside the
   beat.
4. `compile.py` -> `claude-basics--claude-constitution-one-narrow-safety-rule-make.mp4`,
   8/8 real (no slate), 143.2s, 3840x2160 (THE 4K LAW).

**GATE T (type_check.py) — one real defect found and fixed via Gate V frame
pulls, not the validator:**
- B03: the FLAG box's text ("FLAG -- interpretive framing, not a literal
  readout") overflowed both the left and right borders of its container —
  confirmed by cropping a frame at the box's exact location, not merely
  inferred. Fixed by widening the box from 6.2 to 7.8 units; re-rendered and
  confirmed the text sits fully inside with margin on both sides.
- B04: the "flip" case (the both-directions clause) was originally drawn as
  a small box+dot+line glyph positioned at the frame's right edge — it ran
  off-screen entirely (only its left portion was in frame), and a first fix
  attempt (recentring it as a horizontal row) produced a new vertical
  misalignment where the icon box drifted up into the node-caption row.
  Root cause: absolute right-edge positioning plus an unconstrained
  arrange() of mismatched-height sub-groups. Fixed by dropping the
  decorative icon entirely and rendering the flip case as a single centred
  text line built with `.move_to(DOWN * 3.6)` — a layout that cannot drift
  off either edge or misalign vertically because there is only one mobject.
  Also recentred the B04 node graph and RULE/IDENTITY boxes on x=0 (removed
  an asymmetric `LEFT * 1.0` offset that existed only to reserve room for
  the since-removed right-side glyph).
- Re-ran `type_check.py` after both fixes: GATE T PASS, 0 FAILs across all
  eight checks (min-size, overflow, contrast, contrast-local, bbox-overlap,
  card-clip, kerning, no-wordy-card).

**Gate V (visual):** pulled 18 frames at 8s spacing across the full 143.2s
runtime plus targeted crops of the two fixed regions, and read them
directly. B00's correction is legible well before the beat ends. B02's
anchor (rule -> identity bubble -> one faint reach toward "first aid") and
B04's payoff (identical composition, the reach now solid to all five nodes,
"first aid" ringed and captioned "hedged, unrelated", the flip case stated
cleanly below) are visually recognizable as the same object, per ANCHOR LAW.
BCRY/BHTF/BOUT text is centered, legible, no overlap, safe inset respected.
No blockers remaining.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840x2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the two fixes above
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840x2160 h264, audio aac present, duration 143.25s; mp4
  mtime (1787895671) newer than beat_sheet.json mtime (1787895622)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:4 — remotion at 50% of beats, over the ~40% pantry cap in MOTION.md.
Structural, not a defect: hai-simple's mandated shape is B00 (writer) + BCRY
+ BHTF (Your Turn) + BOUT (outro) all REMOTION by skill contract, against 4
GRAPHIC body beats for this 8-beat reel — the ratio is fixed by beat count,
matching the same documented non-blocking warning on prior hai-simple
redo builds (e.g. `claude-basics--browser-coordinate-scaling`). Logged per
the honesty rule rather than reworking beat count to dodge the warning.

Metadata file written: `claude-basics--claude-constitution-one-narrow-safety-rule-make.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `claude-basics` family
prefix — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
