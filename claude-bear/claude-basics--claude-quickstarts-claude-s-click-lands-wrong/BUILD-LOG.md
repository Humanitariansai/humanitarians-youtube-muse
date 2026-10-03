# BUILD-LOG — claude-basics--claude-quickstarts-claude-s-click-lands-wrong

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/claude-quickstarts-claude-s-click-lands-wrong/beat_sheet.json`
(an unbuilt Teardown-register scaffold — 0/8 beats filled, no SCRIPT.md).
Question, facts, and beat count (8) carried over unchanged: a computer-use
app sends Claude a downscaled screenshot (1456×819) of a full-size desktop
(1920×1080); Claude's returned click coordinates describe the smaller image,
not the real screen; the fix is to scale each axis by original÷sent before
the OS input driver ever sees the coordinates. The source's concrete worked
case (originally its own B00, a (700,410)→(960,540) walkthrough) was folded
into this reel's B02/B04 anchor pair — planted as the sent-raw miss, paid off
as the scaled dead-center hit — since hai-simple's spine puts the concrete
case after the question/stakes beat rather than as the very first thing on
screen. B00 replaced a `FormBCard` cold open with `BrutalistHesitantWriter`
(WRITER LAW: "guessing" → "scaling"). Register re-registered Teardown→Plain
(the source narration was already pure arithmetic with no judgment language
to remove). Close/outro re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off.

**Component note:** the source's body beats used `FormBCard`, which
`./art scenes --check FormBCard` confirmed is now retired ("SlateCard
composition deleted 2026-08-26 — banned card form, never to return"). This
was not a NO-GENAI/NO-PANTRY substitution (FormBCard was never AI-video,
pantry, or human-drop) — it's a retired-component swap, so B01–B04 were
rebuilt as custom Manim scenes (`scenes.py` + `render_scenes.py`) carrying
the identical facts and sequence, per the standard GRAPHIC beat pipeline. No
source beat was `ai-video-prompt`, pantry, or a human-drop slot, so
NO-GENAI/NO-PANTRY LAW required no substitution beyond the component swap.

Built from scratch this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (8 beats: B00 writer, B01–B04 Manim GRAPHIC, BCRY carry-out,
BHTF your-turn, BOUT outro), `scenes.py`/`render_scenes.py`. GATE T passed
before generating audio. Ran `generate_audio_kokoro.py` (8/8 beats, am_onyx,
$0.00) — measured durations became the clock; B00 came back at 9.66s,
clearing the ≥9s TIMING LAW window on the first pass. Rendered B01–B04 via
Manim (foreground) and B00/BCRY/BHTF/BOUT via `remotion_scenes.py`
(foreground; the shell auto-backgrounded the 120s+ Remotion run — waited on
it synchronously via `TaskOutput(block=true)` rather than ending the turn,
per the no-orphaned-render rule). Pulled a frame at 9.3s into media/B00.mp4
and confirmed the correction ("guessing" struck, "scaling" typed in, final
question landing) is visible well within the beat.

**Two defects found and fixed during Gate V, before the reel was called
done:**

1. **B03's formula card rendered garbled glyphs for "sent_w"** while
   "screen_w" (identical LaTeX structure) rendered correctly — a Manim
   MathTex bug with mixed word+symbol subscripts, not a content error.
   Root-caused (not routed around): rewrote the formula as plain monospace
   `Text` (`x' = x * (screen_w / sent_w)`) instead of `MathTex`, matching the
   rest of the deck's typographic style. Re-rendered, confirmed legible.
   While in there, also caught the accompanying "inverse of the resize"
   bracket label running past the frame's right edge (a Brace positioned
   `RIGHT` of an already-wide formula block) — replaced the side bracket
   with a centered label below the formula, re-rendered, confirmed within
   safe inset.
2. **GATE T (type_check.py) failed on B04**: "smallest text run 15px <
   floor 20px." Traced to a `→` arrow glyph in the B04 confirmation line
   ("1456 × 819 → 2560 × 1440 …") — isolated by spaces, the arrow's glyph
   bounding box is far shorter than surrounding letters, so the blob
   detector measured it as its own undersized text run. Rewrote the line to
   avoid the special glyph ("same ratio, a 2560 x 1440 screen: still a
   perfect hit"). Also bumped several sub-20px INK/TEAL label sizes in
   B02/B04 (16–18px → 20–22px) for margin. Re-rendered B02 and B04,
   recompiled, GATE T: PASS.

Both fixes were applied to `scenes.py` and the affected beats re-rendered
before the master was ever called final — no post-hoc "close enough."

```
python3 runtime/scripts/compile.py --force <REEL_DIR>
```

Result: `claude-basics--claude-quickstarts-claude-s-click-lands-wrong.mp4`,
8/8 beats filled real (no slate), 113.1s, 3840×2160.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py): PASS, 0 FAILs (after the B04 arrow-glyph fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160, audio stream (aac) present, duration 113.08s;
  mp4 mtime (1787907051) newer than beat_sheet.json mtime (1787907014)
- Gate V (visual): pulled frames across the full runtime and read them
  directly. B00's correction ("guessing" struck, "scaling" typed in) lands
  well inside the beat's 9.7s duration. B02/B04 anchor pair uses the
  identical two-rectangle SENT/SCREEN composition, so the payoff reads as
  the same object: (700,410) plotted raw misses the button in B02; the same
  point run through the formula lands dead-center at (960,540) in B04. B03's
  fixed formula card and B04's fixed confirmation line are both fully
  legible with no edge clipping. BCRY/BHTF/BOUT text is centered, no
  overlap, safe inset respected throughout. No remaining blockers.

**Non-blocking warning (compile.py):** motion histogram remotion:4
manim:4 — remotion at 50% of beats, over the ~40% pantry cap in MOTION.md.
Structural, not a defect: hai-simple's mandated shape is B00 (writer) + BCRY
+ BHTF (Your Turn) + BOUT (outro) all REMOTION by skill contract, against 4
Manim body beats for this 8-beat reel — the ratio is fixed by beat count,
identical to the pattern already logged for the
`anthropic-sdk-php-server-hands-back-encrypted-context` sibling reel. Logged
per the honesty rule rather than reworking beat count to dodge the warning.

Metadata file written: `claude-basics--claude-quickstarts-claude-s-click-lands-wrong.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `claude-basics` family
prefix — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-28 — Phase 4 delivery

Master is already 3840×2160 (compile.py's 4K LAW forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-basics--claude-quickstarts-claude-s-click-lands-wrong.mp4 \
   claude-basics--claude-quickstarts-claude-s-click-lands-wrong-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
