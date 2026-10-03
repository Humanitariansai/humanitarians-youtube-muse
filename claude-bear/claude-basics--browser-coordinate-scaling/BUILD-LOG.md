# BUILD-LOG — claude-basics--browser-coordinate-scaling

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/browser-coordinate-scaling/beat_sheet.json`
(an unbuilt Teardown-register scaffold — 0/8 beats filled, no SCRIPT.md).
Question, facts, and beat count (8) carried over unchanged: Claude's vision
encoder resizes 16:9 screenshots to exactly 1456×819; `coordinate_scaling.py`
scales by `viewport_w/1456`, `viewport_h/819`, then clamps; anchor example
(728, 409) on a 2560×1440 viewport scales to (1280, 720). B00 replaced a
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"exact" → "scaled"); the source's worked (700,410)/1920×1080 prompt moved
verbatim to BHTF as the Your Turn prompt. Register re-registered
Teardown→Plain (no design judgment added or removed — the source narration
carried none). Close/outro re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off. Source's B05 verdict/recap beat dropped as a restatement
(its content already carried by B03/B04); source's B04 exclusions beat
folded into B04's both-directions clause. No source beat was
`ai-video-prompt`, pantry, or a human-drop slot (all were already
Remotion-shaped, just unbuilt), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`. Durations: B00
   11.54s, B01 18.67s, B02 20.20s, B03 17.34s, B04 30.66s, BCRY 8.87s,
   BHTF 15.42s, BOUT 4.57s.
2. Wrote `scenes.py` (4 Manim scenes, B01–B04) sized to the measured
   durations, and `render_scenes.py`; rendered all four in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` (foreground; one
   invocation tripped the shell's 2-minute timeout and was moved to a
   tracked background task — waited on its exit code before continuing,
   never treated it as done until the notification confirmed exit 0).
   B00 verified: `media/B00.mp4` = 11.57s (≥8s TIMING LAW), and a frame
   pulled at 9.5s shows "scaled" mid-type in terracotta — the correction
   lands well inside the beat.
4. `compile.py` → `claude-basics--browser-coordinate-scaling.mp4`, 8/8 real
   (no slate), 128.3s, 3840×2160 (THE 4K LAW).

**GATE T (type_check.py) — two real defects found and fixed, not
suppressed:**
- B01: layout bug — the "raw (x, y), unscaled" arrow label was long enough
  to be occluded by the screen rectangle drawn after it (z-order clip).
  Fixed by widening the gap between the two rectangles and shortening the
  label to "same (x, y)".
- B04: a caveat box (the non-16:9 exclusion) sat too close to the frame's
  right edge, and its caption partially collided with the box — genuine
  overlap, not a false positive. Repositioned and resized both.
- Two contrast false positives, confirmed by pulling frames before
  touching the validator: a compact `Cross()` "miss" mark in B01 and B02
  (near-square bounding box, same false-positive pattern as
  `claude-liam-enterprise-search` B04 already documented in
  `type_check.py`). Added `B01Scene`, `B02Scene` to
  `STRUCTURAL_TERRACOTTA_PATTERNS` with the same justification — the marks
  carry no readable text, only the Cross shape itself. All genuine
  full-sentence text that had been colored TERRA (B01/B02 footers, B02's
  "same (728, 409)" label) was switched to INK, which is the correct fix
  per the house rule, independent of the exemption.
- Also bumped several B04 text runs (shot/screen labels, coordinate digits,
  the caveat caption) above the 20px floor, and replaced the `×`/`✓` glyphs
  with plain words ("times about 1.76", "YES") after bumping font_size
  alone didn't clear the floor — those symbol glyphs render smaller than
  their font_size at this font, a real min-size defect, not a validator bug.
- Re-ran `type_check.py` to GATE T: PASS (0 FAILs) before compiling final.

**Gate V (visual):** pulled 21 frames at 6s spacing across the full 128s
runtime and read them directly. B00's correction is legible mid-beat. B01's
"same (x,y), miss" composition reads cleanly with no occlusion after the
fix. B02's anchor (728,409 dead center → same raw pixel misses on the real
viewport) and B04's payoff (same rectangle pair, scaled dot lands exactly on
target, non-16:9 caveat clean of the frame edge) are visually recognizable
as the same object, per ANCHOR LAW. BCRY/BHTF/BOUT text is centered, legible,
no overlap, safe inset respected. No blockers remaining.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the fixes above
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio aac present, duration 128.28s; mp4
  mtime (1787893742) newer than beat_sheet.json mtime (1787893700)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:4 — remotion at 50% of beats, over the ~40% pantry cap in MOTION.md.
Structural, not a defect: hai-simple's mandated shape is B00 (writer) + BCRY
+ BHTF (Your Turn) + BOUT (outro) all REMOTION by skill contract, against 4
GRAPHIC body beats for this 8-beat reel — the ratio is fixed by beat count.
Logged per the honesty rule rather than reworking beat count to dodge the
warning.

Metadata file written: `claude-basics--browser-coordinate-scaling.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `claude-basics` family
prefix — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-28 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.
