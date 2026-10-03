# BUILD-LOG — claude-basics--computer-use-best-practices

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/computer-use-best-practices/beat_sheet.json`
— a partially-filled legacy scaffold: Teardown-register metadata, B00-B06
narrated and built under the old `simple` puppet-ask shape, plus three
additional bookend slates (BVDT/BHTF/BOUT) drafted but never filled or
reconciled with B00-B06 (its own `CHECKS-REPORT.md` recorded `checks_green:
False` and `NEEDS-REVIEW.md` recorded a failed GATE T). Question and body
facts carried over unchanged: naive computer-use loop (screenshot -> full
image to Claude -> action -> repeat); ~1,200 tokens per full-resolution
screenshot; a 20-step task with no changes burns ~40,000 screenshot tokens
before any action token; seven production changes (resize to ~1568px wide,
prune old screenshots, batch tool calls, cache system prompt, compact
server-side, sandbox execution, structured trajectory recording); resize +
prune cuts the bill 70-80%; trajectory recording logs every action with
timestamp/tool/args/result and is replayable.

One deliberate content change beyond the register/skin swap: the source's
B00 asked the narrator to "stress-test the gap" with modal-handling tests,
verification steps, and guardrails — a framing the source's own B01-B06 never
answers (they cover screenshot cost and trajectory logging instead). Carrying
that mismatched cold open forward would open on a question the reel doesn't
answer, so B00 was reauthored (per WRITER LAW: the correction must be "the
reel's actual misconception") to state the wrong guess the body actually
falsifies — that going to production just means running the demo longer,
corrected to leaner. Logged here rather than silently dropped, per the
redo-contract's requirement to keep facts/argument unchanged while flagging
any substitution.

B00 replaced a `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter`
(WRITER LAW: "longer" -> "leaner"). Register re-registered Teardown -> Plain
(no design judgment added; the source's own narration carried none to
remove). Source's bundled B05 beat (carry-out sentence + Your Turn prompt in
one beat) split into a dedicated BCRY (carry-out) and BHTF (Your Turn) per
hai-simple's CARRY-OUT LAW; the source's B05 trajectory-logging-schema prompt
carried to BHTF verbatim. Close re-skinned to `OutroCTA` / @HumanitariansAI
with Liam's sign-off. The three abandoned bookend slates (BVDT/BHTF/BOUT)
were not carried forward — their content duplicates B05/B06 and they were
never filled in the source. No source beat was `ai-video-prompt`, pantry, or
a human-drop slot (all were already Remotion/graphic shapes), so NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00 (covered by WRITER LAW).

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`. Durations: B00
   10.94s, B01 20.42s, B02 13.99s, B03 19.99s, B04 18.65s, BCRY 8.23s, BHTF
   17.45s, BOUT 3.93s.
2. Wrote `scenes.py` (4 Manim scenes, B01-B04) sized to the measured
   durations, and `render_scenes.py`; rendered all four in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. One invocation
   tripped the shell's 2-minute default timeout and was auto-moved to a
   tracked background task by the harness; per the one-shot-invocation rule,
   never treated as done on that basis alone — blocked on it with a
   foreground polling loop (checking for all 4 output files, then confirming
   via the harness's own completion notification and `ps`/log inspection
   that the process had exited 0) before proceeding.
4. **B00 TIMING LAW failure and fix:** the first B00 render (text: "My
   computer-use demo works. Going to production just means running it
   longer, right?", ~88 chars) truncated mid-typing at the audio's 10.94s
   mark, well before the "longer"->"leaner" correction — the component's own
   typing+hesitation performance needed roughly 15s against a 10.94s audio
   track, so `remotion_scenes.py`'s `ffmpeg -t` truncation cut it off early
   (same failure class the pilot hit). Fixed by shortening the typed text to
   "Production just means running it longer, right?" (~50 chars, close to
   the proven browser-coordinate-scaling reel's ~64-char text) with the same
   hesitation params. Re-rendered; verified `media/B00.mp4` = 10.97s (>=8s
   TIMING LAW) and pulled frames at t=6s/8s/10.5s showing "longer" still
   typed in terracotta at 6s and the correction to "leaner" already landed
   and holding from 8s through 10.5s — comfortable margin before the clip
   ends.
5. `compile.py` -> `claude-basics--computer-use-best-practices.mp4`, 8/8
   real (no slate), 114.6s, 3840x2160 (THE 4K LAW).

**GATE T (type_check.py) — real defects found and fixed, plus two confirmed
false positives added to the exemption lists (not loosening the check):**
- B01Scene: `CurvedArrow` loop-back arc (angle=-TAU/6) sagged down ~1.13 units
  and visually crossed through the "about 1,200 tokens / screenshot" label
  below it — genuine layout bug. Fixed by shrinking the arc angle to -TAU/12
  and adding vertical clearance between the arc, the cost label, the token
  counter, and the footer.
- B03Scene: the "shrinks the bill" bracket `Line()` was built from
  `lines.get_top()`/`get_bottom()` (the group's center-x) offset by only
  LEFT*0.5, so it cut vertically through the middle of the list items instead
  of sitting to their left — genuine positioning bug (wrong anchor point).
  Fixed by computing the bracket from `lines.get_left()` minus a buffer and
  moving the list group right to make room.
- B04Scene: the "70-80% cut" / "drops to about 10,000" labels sat almost
  directly on top of the "about 40,000" bar label (only ~0.3 units apart) —
  genuine spacing bug. Fixed with an explicit fixed position for the bar
  label and more vertical clearance for the labels above it.
- Three genuine min-size defects (11px/9px/9px vs the 20px floor at 1080p
  logical), all isolated tilde ("~") glyphs — confirmed by cropping the exact
  flagged pixel regions: the tilde's squat wave shape renders well under the
  floor regardless of the surrounding text's font_size, the same class of
  defect the browser-coordinate-scaling build documented for `x`/checkmark
  glyphs. Fixed per that precedent: replaced every "~" with "about" (B01
  cost label, B02 bill label for consistency, B03 first list item, B04 bar
  label) and replaced "-> ~10,000"/"70-80%" with words ("drops to about
  10,000" / "70 to 80 percent cut") rather than bumping font_size (which
  doesn't fix a symbol glyph's inherent aspect ratio).
- One confirmed false positive on bbox-overlap (§8.6b): B01Scene's four
  RoundedRectangle loop-step boxes each contain a centered label; the
  border's bbox structurally encloses the label's bbox at ~9-11x aspect,
  passing the "text run" shape filter and triggering a spurious 100% overlap.
  This is the exact documented pattern already exempted for six other
  reels' scenes (`B02_FiveProperties`, `B03_HookMechanism`, `S02Scene`, etc.)
  in `BBOX_OVERLAP_EXEMPT_PATTERNS` — verified by frame pull (no real
  text-on-text overlap), added `B01Scene` to that set with justification.
- One confirmed false positive on min-size (§8.1): B04Scene's terracotta
  strikethrough `Line()` (corner-to-corner X) sliced the apex of a letter in
  "WHETHER" into an ~11px disconnected fragment — the same documented
  rendering-geometry artifact as `simple-watermark` S05/S15/S16 (strikethrough
  bisecting letter bodies). Added `B04Scene` to `HAND_DRAWN_PATTERNS` with
  justification, after first trying to fix it directly (thickened the strike
  stroke_width 3->8, which reduced but did not eliminate the fragment).
- Re-ran `type_check.py` to GATE T: PASS (0 FAILs) after the fixes above.

**Gate V (visual):** pulled 19 frames at 6s spacing across the full 114.6s
runtime and read them directly, plus targeted crops of every fixed region.
B00's correction ("longer" -> "leaner") is legible with margin. B01's naive
loop reads cleanly with no arc/label collision. B02's anchor (~40,000
screenshot tokens, action tokens at 0) and B04's payoff (same bar cut to
~10,000, the "proves WHAT / not WHETHER" card pair) are visually recognizable
as the same object, per ANCHOR LAW. BCRY's carry-out card echoes "leaner"
from B00 as a deliberate callback. BHTF's Your Turn prompt and BOUT's
@HumanitariansAI outro/subscribe card render legibly with safe inset
respected. No blockers remaining.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840x2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the fixes above
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840x2160 h264, audio aac present, duration 114.6s; mp4
  mtime (1787912346) newer than beat_sheet.json mtime (1787912307)

**Non-blocking warning (compile.py):** motion histogram remotion:4 graphic:4
— remotion at 50% of beats, over the ~40% pantry cap. Structural, not a
defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn)
+ BOUT (outro) all REMOTION by skill contract, against 4 GRAPHIC body beats
for this 8-beat reel — the ratio is fixed by beat count, same as every other
8-beat hai-simple reel. Logged per the honesty rule rather than reworking
beat count to dodge the warning.

Metadata file written: `claude-basics--computer-use-best-practices.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `claude-basics` family
prefix — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
