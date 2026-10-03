# BUILD-LOG — claude-basics--feature-list-checkpoint-persistence

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/feature-list-checkpoint-persistence/beat_sheet.json`
(a fully-scripted Teardown-register scaffold, never built — 0/8 beats
filled, all SLATE). Question, facts, and beat count (8) carried over
unchanged: an agent with 200 features fills its context window after
finishing 50 in session one; session two starts blank; the fix is
externalizing state to `feature_list.json` (200 entries, id + status
incomplete/passing) plus git as a commit ledger; every session opens the
file, finds the first incomplete entry, and starts there. The source's
concrete worked case (feature 51 as the resume point) was folded into this
reel's B02/B04 anchor pair — planted as the first-incomplete flag after
session 1, paid off as session 2 opening the same file at the same row —
since hai-simple's spine puts the concrete case after the question/stakes
beat rather than bundling it into the cold open. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"remembers" → "checks"). Register re-registered Teardown→Plain (the source
narration was already close to pure mechanism; no verdict language to
remove). Close/outro re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Source's honesty beat (scope exclusions: initializer agent, test
framework) moved to CARRY-OUT.md / the `.md` description's "Deliberately not
claimed" section rather than a dedicated on-screen beat, mirroring the
disposition used on sibling redos — the source's B05 verdict recap was
promoted to BCRY as the carry-out instead.

**Component note:** the source's body beats (B01–B04) used `ClaudeComposerAsk`
as a text-card body pattern, not the cold-open/handoff role it's reserved
for in hai-simple's spine. Rebuilt as custom Manim scenes (`scenes.py` +
`render_scenes.py`) carrying the identical facts and sequence, per the
standard GRAPHIC beat pipeline. Not a NO-GENAI/NO-PANTRY substitution — no
source beat was `ai-video-prompt`, pantry, or a human-drop slot.

Built from scratch this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (8 beats: B00 writer, B01–B04 Manim GRAPHIC, BCRY carry-out,
BHTF your-turn, BOUT outro), `scenes.py`/`render_scenes.py`. Ran
`generate_audio_kokoro.py` (8/8 beats, am_onyx, $0.00) — measured durations
became the clock; B00 came back at 10.6s.

**B00 TIMING LAW defect caught before first render:** the initial
`BrutalistHesitantWriter` props (mistakeRate 6, hesitateWithin 3,
hesitateBetween 22, charMs 55 — copied from a sibling reel) produced a
natural typing performance of ~13.6s against a 10.6s audio track;
`remotion_scenes.py`'s `extend_clip_to_duration` truncates at the audio
length via `-t`, so the render was cut off mid-typing ("How does it resume
at feature 5|") — the correction was visible but the final question never
finished, same failure class as the 2026-08-27 pilot. Root-caused by writing
a small Node harness that replicates `buildTimeline()`'s seeded-random
algorithm against `remotion/dist/cjs/random.js` to compute the natural
frame count for candidate prop values without rendering. Fixed by setting
mistakeRate/hesitateWithin/hesitateBetween to 0 (removing incidental
hesitations so only the one deliberate trigger-word correction remains) and
charMs to 42, giving a natural duration of ~9.27s — comfortably inside the
10.6s window. Re-rendered; verified by frame pull at 3.0s/7.0s/9.5s/10.5s
that "remembers" is struck and corrected to "checks" well before the
midpoint, and the full final question ("...not feature 1?") is fully typed
and holding steady by 9.5s, before the audio-driven freeze at 10.6s.

Rendered B01–B04 via Manim (foreground) and B00/BCRY/BHTF/BOUT via
`remotion_scenes.py`; the Remotion pass exceeded the shell's 120s foreground
timeout and was auto-backgrounded — per the no-orphaned-render rule, waited
on it synchronously via `TaskOutput(block=true)` rather than ending the turn,
and confirmed exit code 0 before proceeding.

**GATE T caught three real defects, all fixed at the root before the cut was
called done:**

1. **B01 contrast-local + min-size false-alarm chain, real root cause found
   underneath:** the first fix attempt (bumping font sizes) cleared the
   min-size number but not contrast-local; investigation traced it to a
   genuine palette collision — the scene's TEAL fill (#1F4E5F) sits within
   RGB-distance 75 of the checker's INK_HEX reference, so a large solid TEAL
   rectangle used as a "context full" fill panel gets misclassified as
   ink-colored text, and cream caption text sitting on top of it reads as a
   near-zero-contrast blob. Root-fixed by moving the "context full" caption
   off the TEAL fill entirely (below the box, on GROUND, in INK) rather than
   reversed-color text on the fill — the same TEAL fill still communicates
   "full" visually, just without text printed on it.
2. **B01 min-size (separate cause):** two TERRA strikethrough Lines bisect
   "RE-READ EVERYTHING" and "GUESS" into sub-floor letter-half fragments —
   confirmed via direct mask replication as the same rendering-geometry
   artifact documented for simple-watermark S02/S05/S15/S16 and
   computer-use-best-practices B04Scene; added `B01Scene` to
   `HAND_DRAWN_PATTERNS` in `type_check.py` with the same rationale.
3. **B03 bbox-overlap:** the four loop-step RoundedRectangle boxes' own
   border strokes were being detected as text-run blobs enclosing their
   interior labels — same box+label pattern as `B02_FiveProperties`,
   `B03_HookMechanism`, and this reel's own B01Scene; added `B03Scene` to
   `BBOX_OVERLAP_EXEMPT_PATTERNS`, verified by frame pull that labels sit
   cleanly inside their boxes with real margin.

GATE T: PASS, 0 FAILs after fixes.

**Gate V frame pull (12 frames, full 98.8s runtime, plus targeted crops)
caught two further real layout bugs, neither flagged by GATE T:**

4. **B02/B04 flag-label overlap:** the crimson "ring" meant to circle
   feature 51's badge was positioned a full 1.5 units left of the badge
   (`badge51.get_center() + LEFT * 1.5`), landing in the empty gutter between
   the id column and the badge column instead of around the badge, and the
   "first incomplete" / "SESSION 2 opens here" flag labels (positioned
   `next_to(ring, RIGHT)`) landed printing directly on top of the row's own
   "incomplete"/"passing" badge text. Fixed by centering the ring on the
   actual badge and moving the flag labels further right, past the commit-dot
   column, into open space.
5. **B04 stray dot on row 52:** a small teal dot sat fused into the "p" of
   row 52's "passing" text after the flip animation, visible in every frame
   from the transform onward. First suspected as a `Transform()` glyph-morph
   artifact between "incomplete"/"passing" (different letter counts) and
   switched to a FadeOut/FadeIn crossfade — the dot persisted unchanged,
   ruling that out. Root-caused by tracing `new_commit.move_to(commit.get_center())`:
   the pre-flip commit placeholder for every incomplete row is
   `Text("", font_size=1)` — an empty-string VMobject with no bounding box —
   so `.get_center()` on it degenerates to the scene origin (0,0,0) rather
   than the intended `RIGHT*2.1+UP*y` column position. Both row 51's and row
   52's misplaced dots landed at the origin, which happens to coincide with
   row 52's actual position (y≈0.02, nearest to 0 of the eight rows). Fixed
   by positioning `new_commit` directly via the same formula the placeholder
   itself was defined with, instead of copying a degenerate center. Also
   fixed in the same pass: `divider_lbl` ("session boundary") in B01Scene was
   positioned `buff=2.1` above the divider — off the top of the frame
   entirely, so the label never appeared on screen at all; corrected to
   `buff=0.15`.

All five defects fixed at the root and the affected beats (B01, B02, B03,
B04) re-rendered before recompiling. Recompiled and re-ran GATE T (PASS, 0
FAILs) and a full Gate V frame sweep after every fix round.

```
python3 runtime/scripts/compile.py --force <REEL_DIR>
```

Result: `claude-basics--feature-list-checkpoint-persistence.mp4`, 8/8 beats
filled real (no slate), 98.8s, 3840×2160.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py): PASS, 0 FAILs (after the fixes above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 (h264), audio stream present (aac), duration
  98.78s; mp4 mtime (1787918146) newer than beat_sheet.json mtime
  (1787918112)
- Gate V (visual): pulled 12 frames across the full runtime (8s spacing) plus
  targeted crops on every fixed region. B00's correction ("remembers" struck,
  "checks" typed in, final question complete) lands and holds well inside
  the beat's 10.6s duration. B02/B04 anchor pair uses the identical 8-row
  feature-list composition, so the payoff reads as the same object: row 51
  ringed as "first incomplete" in B02; the same ring/row opens session 2 in
  B04, with rows 51–100 (represented by 51–55 in the compact view) flipping
  to passing. B03's loop diagram is fully legible with labels clear of their
  box borders. BCRY/BHTF/BOUT text is centered, no overlap, safe inset
  respected throughout. No remaining blockers.

**Non-blocking warning (compile.py):** motion histogram remotion:4
manim:4 — remotion at 50% of beats, over the ~40% pantry cap in MOTION.md.
Structural, not a defect: hai-simple's mandated shape is B00 (writer) + BCRY
+ BHTF (Your Turn) + BOUT (outro) all REMOTION by skill contract, against 4
Manim body beats for this 8-beat reel — the ratio is fixed by beat count,
identical to the pattern already logged for multiple sibling
`claude-basics--*` redos. Logged per the honesty rule rather than reworking
beat count to dodge the warning.

Metadata file written: `claude-basics--feature-list-checkpoint-persistence.md`
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
cp claude-basics--feature-list-checkpoint-persistence.mp4 \
   claude-basics--feature-list-checkpoint-persistence-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
