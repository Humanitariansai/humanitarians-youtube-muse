# BUILD-LOG — claude-basics--macos-computer-use-coordinate-roundtrip

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/macos-computer-use-coordinate-roundtrip/beat_sheet.json`
(a Teardown-register scaffold, 4/8 beats had Manim graphics filled but no
B00/B05/B06/B07 media, no SCRIPT.md, and CHECKS-REPORT.md showed
checks_green: False). Question, facts, and beat count (8) carried over:
macOS Retina screenshots exceed Claude's per-image tile budget (28×28
patches, long edge ≤1568px, ≤1568 tiles); the reference implementation
(`computer_use/image.py`) ports the API's own resize as `target_image_size()`
so you resize first, record the sent dimensions, and invert once Claude
clicks (`real = model × original / sent`). Anchor: native 1920×1080, button
at (960, 540); `target_image_size(1920, 1080)` → (1456, 819); Claude sees
the button at (728, 409); inverted back it lands exactly at (960, 540) — this
is the source's own B03 centerpiece example, verified 16:9-to-16:9 in
SOURCES.md. The source's B00 puzzle example (2560×1600 → (728,410) →
(1280,800)) mixed an 8:5-aspect native size with a 16:9-aspect sent size,
which is not internally consistent — dropped in favor of the one verified
example, per "facts must be true and current."

B00 replaced a `ClaudeComposerAsk` cold open (never built, SLATE) with
`BrutalistHesitantWriter` (WRITER LAW: "exactly" → "resized"); the source's
YOURTURN prompt moved verbatim to BHTF. Register re-registered
Teardown→Plain (no design judgment added or removed — the source narration
carried none, describing the mechanism only). Close/outro re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Source's B05
verdict/recap beat dropped as a restatement (its content already carried by
B03/B04's forward-call and payoff); source's B04 honesty/exclusions beat
folded into B04's both-directions clause. Source's three unfilled `BOOKEND`
placeholders (BVDT, a duplicate BHTF, a duplicate BOUT — all blank
narration, dead scaffold from an older sheet template) were dropped, not
content. No source beat was `ai-video-prompt`, pantry, or a human-drop slot
(all were Remotion/GRAPHIC shapes, just unbuilt), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`. Durations: B00
   11.84s, B01 23.27s, B02 24.15s, B03 25.39s, B04 32.17s, BCRY 11.22s,
   BHTF 14.17s, BOUT 5.55s.
2. Wrote `scenes.py` (4 Manim scenes, B01–B04) sized to the measured
   durations, and `render_scenes.py`; rendered all four in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The invocation
   exceeded the shell's 2-minute timeout and was moved to a tracked
   background task; waited on its exit code (TaskOutput, block=true) before
   continuing — never treated it as done until the notification confirmed
   exit 0, per the one-shot-invocation rule. B00 verified: `media/B00.mp4`
   = 11.87s (≥8s TIMING LAW), and a frame pulled at 9.5s shows "resized"
   mid-type in terracotta, replacing "exactly" — the correction lands well
   inside the beat.
4. `compile.py` → first pass: 8/8 real (no slate), 3840×2160 (THE 4K LAW),
   GATE AUDIO PASS at -23.9dB.

**GATE T (type_check.py) — one real finding chased down, not suppressed:**
- First pass: B03 min-size + kerning FAIL on the bottom caption
  ("image.py — binary search, long edge under 1568px, tiles under 1568").
  Bumped font_size and dropped `≤`/arrow glyphs (`↓`, `→`) for plain words
  ("gives", "under") — same fix pattern as the browser-coordinate-scaling
  sibling build. Shortened the caption.
- Second pass still FAILed on kerning (89px gap, threshold 9px). Ran the
  checker's own pixel logic standalone against the extracted frame to find
  the exact offending row instead of guessing: peak-ink row was the
  "record sent_w, sent_h — the denominator of the inverse" line — TWO
  underscored mono identifiers in one long TERRA row. Rewrote it as plain
  SANS prose with no underscores.
- Third pass still FAILed, same 89px number. Reran the standalone pixel
  probe again: after the caption shortened, peak-ink row moved to that same
  "record..." prose line — its mean run width (~12-19px, from per-touching-
  glyph run splitting) makes ordinary word-spacing in a normal sentence
  exceed the mean_w-derived threshold. Confirmed by reading the frame
  directly: spacing is visually normal, legible, no actual defect. This is
  the same false-positive class already documented for
  `B31_LabelVsFunction`, `Scene_B06_ClaudeLiamSales`, etc. in
  `type_check.py`'s `KERNING_EXEMPT_PATTERNS`.
- Rather than add the bare, collision-prone name `B03Scene` (reused as
  boilerplate across many other reels' scenes.py files) to that global
  exemption set, renamed this reel's Manim class to the reel-unique
  `B03_MacosCoordinateRoundtrip` (updated in `scenes.py`, `render_scenes.py`,
  and `beat_sheet.json`'s `graphic.manim` field) and added *that* name to
  `KERNING_EXEMPT_PATTERNS` with the confirmed rationale — scoped to this
  reel only, zero risk of exempting a genuine future bug in some other
  reel's generically-named `B03Scene`.
- Re-ran `type_check.py` to GATE T: PASS (0 FAILs) before recompiling final.

**Gate V (visual):** pulled 25 frames at 6s spacing across the full 148.8s
runtime and read them directly. B00's correction ("resized" replacing
"exactly") is legible mid-beat. B01's over-budget/miss composition reads
cleanly. B02's anchor ((960,540) native → (728,409) sent, "a different
number, for the same pixel") and B04's payoff (same rectangle pair, inverted
dot lands exactly on the button with a "YES" mark, the already-in-budget
caveat clear of the frame edge with "nothing to invert") are visually
recognizable as the same object, per ANCHOR LAW. B03's algorithm card reads
cleanly post-fix. BCRY's carry-out, BHTF's Your Turn prompt (verbatim from
the source), and BOUT's title/outro are centered, legible, no overlap, safe
inset respected. No blockers remaining.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the fixes above
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe (independently re-verified after final compile): video 3840×2160
  h264, audio aac present, duration 148.78s; mp4 mtime (1787920232) newer
  than beat_sheet.json mtime (1787920184)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:4 — remotion at 50% of beats, over the ~40% pantry cap in MOTION.md.
Structural, not a defect: hai-simple's mandated shape is B00 (writer) + BCRY
+ BHTF (Your Turn) + BOUT (outro) all REMOTION by skill contract, against 4
GRAPHIC body beats for this 8-beat reel — the ratio is fixed by beat count,
identical to the browser-coordinate-scaling sibling's same warning. Logged
per the honesty rule rather than reworking beat count to dodge the warning.

Metadata file written: `claude-basics--macos-computer-use-coordinate-roundtrip.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `claude-basics` family
prefix — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
