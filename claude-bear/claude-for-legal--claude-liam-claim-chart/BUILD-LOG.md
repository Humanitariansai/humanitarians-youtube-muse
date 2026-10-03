# BUILD-LOG — claude-for-legal--claude-liam-claim-chart

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-claim-chart/beat_sheet.json`.

**Source check (logged, not asked — full detail in QUESTION.md):** unlike
sibling redos in this family (`amendment-history`, `ai-inventory`), this
source sheet's narration carried REAL, already-written facts at every
skill-specific point — no unfilled `>` placeholders. The `claim-chart`
Anthropic Skill: builds or reviews an element chart (a patent claim chart
for infringement/invalidity/review, or a civil element chart for any
cause of action or defense), every cell pin-cited, gap detection as the
priority output. `source_skill`'s path
(`/Users/bear/...litigation-legal/skills/claim-chart/SKILL.md`) still
doesn't exist on this machine, but it wasn't needed — the facts were
already in the source's own narration text, so nothing here is
reconstructed from a bare title the way the placeholder-sheet siblings
were.

**The redo, register Teardown -> Plain:** source B03 ("design tell") and
BVDT ("verdict") carried explicit Teardown language — "what it gets
right... what it bites," "know the limit." Re-registered to Plain by
keeping the same mechanism (element-by-element pin citation, gap
detection prioritized) and stating its failure modes as ordinary
properties of the chart's output, never a verdict on the skill's design:
a filled cell doesn't decide the case (a citation can be weak or partial);
a gap doesn't decide it either (it isn't proof the element fails, only
that evidence hasn't turned up yet). B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"prove" -> "map" — the naive assumption that a claim chart's job is to
prove the case, corrected to mapping each element to its evidence). Source
BVDT verdict recap folded into a dedicated BCRY carry-out beat per
CARRY-OUT LAW. Close re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off. Added an anchor (B02 -> B03: one claim, two elements — "a
locking mechanism" cited to the manual page 12, "a temperature sensor"
gapped) and a both-directions beat (B03) per this factory's PHASE 1
structure requirement — the source (Teardown skill-anatomy format) carried
neither in this shape.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.07s, B01 17.98s, B02 19.80s, B03 22.04s, BCRY 7.53s, BHTF 16.58s,
   BOUT 2.88s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `CLCB01Scene` /
   `CLCB02Scene` / `CLCB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`; the process
   exceeded the shell tool's 120s inline timeout and moved to a tracked
   background job. Per the COMPLETION LAW for one-shot invocations,
   blocked on `TaskOutput(task_id, block=true)` in the foreground rather
   than ending the turn — confirmed exit code 0 (all 4 beats ok) before
   proceeding.
4. B00 verified directly: `media/B00.mp4` = 11.1s (clears the >=9s
   narration-window target). Pulled a frame at t=9s: the correction
   ("prove"->"map") is complete and the full final question ("Can Claude
   map my case with a claim chart?") is legible.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -23.9 dB (already passing GATE AUDIO).

**GATE T (type_check.py) — two rounds of real findings, both fixed (not
false positives):**

- First pass: FAIL (3 pixel beats). (a) B02's header labels
  ("ELEMENT: A LOCKING MECHANISM" / "ELEMENT: A TEMPERATURE SENSOR")
  rendered with the same inter-word space collapse already logged in the
  sibling `amendment-history` build — confirmed visually on a pulled frame
  ("ELEMENT:ALOCKING MECHANISM"). (b) B01 and B02 both flagged
  bbox-overlap: a label and a nested inner "cell" card were being read as
  one connected blob. Compared against B03, which uses one card per row
  with header/value stacked as plain text (no nested card) and passed
  clean on the first pass — confirmed the nested card-in-card layout is
  the structural cause, not a rendering fluke. (c) B03 flagged min-size
  (no text-run blobs above noise threshold): traced to a `.scale(0.7)`
  shrink applied to already-small anchor-payoff text after repositioning
  it, pushing it under the floor.
  **Fix:** rewrote B01 and B02 to drop the nested-card layout (single card
  per row, stacked plain text, matching B03's proven-safe pattern);
  applied `_spaced_text` universally to multi-word SANS BOLD labels;
  removed B03's post-position `.scale(0.7)` (repositioned without
  scaling).
- Second pass: FAIL (1 pixel beat) — B02 still flagged bbox-overlap even
  after the layout fix, because the long header "ELEMENT: A TEMPERATURE
  SENSOR" was triggering `scale_to_fit_width` (forced to fit near the
  full card width), unlike B03's shorter, never-scaled headers. Cropped
  and viewed the exact flagged pixel region directly rather than guessing
  further — confirmed the header and the value line below it were being
  read as one tall fused blob only on the beat using forced-width
  scaling. **Fix:** dropped the "ELEMENT:" prefix (redundant with the
  visible context) and reduced the header font to match B03's proven
  values, eliminating the forced scale entirely.
- Third pass: **PASS (0 FAILs)**.

**Gate V (visual) — 23 frames sampled across the full 98.9s runtime**
(computed from actual beat durations: one frame near the start of each
beat, one at its midpoint, plus transition points), read directly. All 7
beats render legibly with safe inset respected, correct word spacing (the
B02 fix holds), and no text overlap anywhere — including the anchor
plant/payoff pair (B02 -> B03), the carry-out quote card, the composer
Your-Turn card, and the outro. No new defects found at this pass.

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family (e.g.
`claude-for-legal--claude-liam-amendment-history`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after fixing the two confirmed defect classes
  above (word-space collapse; nested-card bbox-overlap / forced-scale
  fused-run)
- Gate V: PASS — 23 frames across the full runtime, no defects
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max
  -3.3 dB
- ffprobe: duration 98.875s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking note (compile.py):** B03's Manim clip (7.0s raw) was
slowed 3.1x to fill its 22.0s narration window — logged to
`replace_log.md` as the tool's own "extreme slow-mo" warning (>3.0x
threshold); not treated as a blocking finding since it's the tool's own
advisory mechanism, same disposition as the sibling `amendment-history`
build's non-blocking slow-mo note.

**Motion histogram:** remotion:4 graphic:3 — remotion at more than half of
beats. Structural, not a defect: hai-simple's mandated shape is B00
(writer) + BCRY + BHTF (Your Turn) + BOUT (outro) all REMOTION by skill
contract, against 3 GRAPHIC body beats for this 7-beat reel — same
disposition as every other short hai-simple reel in this family.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same resolution
as the sibling `claude-for-legal--claude-liam-amendment-history` redo.

Metadata file written:
`claude-for-legal--claude-liam-claim-chart.md` (channel @HumanitariansAI,
Playlist: **Claude Basics**, plus the direct code link per the DELIVERY
CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
