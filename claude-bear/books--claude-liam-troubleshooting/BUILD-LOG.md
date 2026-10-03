# BUILD-LOG — books--claude-liam-troubleshooting

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/books/claude-cowork-plugins/youtube/claude-liam-troubleshooting/beat_sheet.json`
(Ch.14 "Troubleshooting and Staying Current", Teardown/deep-explainer
source, no SCRIPT.md — source `beats[*].narration_text` served as the
locked script). Picked up a prior session's in-progress artifacts on
arrival: `beat_sheet.json`, `SCRIPT.md`, `QUESTION.md`, `CARRY-OUT.md`,
audio for all 19 beats, Manim renders for all 15 GRAPHIC body beats
(NB01–NB15), and Remotion renders for B00/BCRY/BOUT already in place.
Only `media/BHTF.mp4` (the your-turn handoff) was missing — rendered it
via `remotion_scenes.py --only BHTF` and continued from there rather than
rebuilding.

Question, facts, and full four-act body argument carried over unchanged
per the prior session's SCRIPT.md: the surface-vs-concept discipline;
five failure shapes (won't appear, won't authenticate, generic results,
too slow, command not found) each with a durable cause; the four-step
loop (active, authorized, simpler, restart); the anchor pair NB08→NB09/
NB10 (checking `/plugins` is both the command-not-found fix and the
opening move of the four-step loop); both-directions NB12/NB13 (updates
keep the plugin current, but also mean the interface itself keeps
shifting). B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter`. Source's 24-beat deep-explainer chassis (4
act-title cards + 16 numbered body beats + V01 verdict recap + H01
your-turn + O01 outro, plus a duplicate blank-narration BVDT/BHTF/BOUT
bookend tail) was compressed to 19 beats (B00 + 15 GRAPHIC body beats +
BCRY/BHTF/BOUT) — full accounting already in SCRIPT.md's "Beat-count
note (redo)" section, carried over unchanged from the prior session.

**Two real defects found and fixed this invocation, both at the root:**

1. **GATE T min-size FAIL, 4 beats (NB03/NB04/NB11/NB13).** Diagnosed by
   reproducing the checker's `Text()` metrics offline (not guessing): the
   shared `_chip()` renderer in `scenes.py` picks a chip label font_size
   by character count (26/22/18), then uniformly scales the whole label
   down to fit the chip's width — and for the longer labels in narrow
   (5-up) or long-word chips ("COMMAND NOT FOUND" at 5-across, "BREAKS
   HERE = THE CAUSE" at fs=18), that scale-to-fit shrank the rendered
   glyph height below GATE T's floor (measured final ink heights
   0.105–0.18 manim units, vs. ~0.25–0.6 for the passing chips — confirmed
   by instantiating `Text()` offline with the exact per-beat chip lists
   before touching the renderer). Fixed by wrapping long labels onto two
   lines at a fixed, un-shrunk font_size (trying every word-boundary
   split, keeping the one with the narrowest longer line) instead of
   scaling a single line down further, and raising the smallest font
   tier from 18→20. Verified offline (recomputed final heights, all now
   0.25–0.6) before re-rendering; re-rendered NB03/NB04/NB11/NB13 only;
   `type_check.py` went FAIL(4)→PASS(0). (A parallel fix was also applied
   to the shared caption renderer for long captions, wrapping instead of
   over-shrinking — not itself a measured GATE T failure at the time, but
   the same latent defect class, cheap to close alongside the chip fix.)

2. **B00 WRITER LAW correction never landed on screen — a real,
   silent-failure bug, not a false positive.** Per skill instruction, I
   pulled a late frame in B00 to verify the "my screen"→"the concept"
   correction and found the writer typed straight through with no
   hesitation or accent color at all, at every timestamp checked (2s
   through 9.5s). Root cause, traced in
   `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx`: the writer
   splits its text into individual whitespace-delimited tokens and
   matches `triggerWords` against a single token's core word — but the
   prop was set to the two-word phrase `"my screen"`, which can never
   equal any single-word token, so the replacement logic silently never
   fired (no error, no warning — it just typed the naive sentence and
   stopped). Fixed by rewording the writer's line so the hesitation lands
   on one word — `"matches the screen?"` correcting to `"matches the
   concept?"` (trigger `"screen"` → replacement `"concept"`, single word,
   multi-word replacement is fine) — same pedagogical correction, just
   expressed so the component's actual matching rule can fire. Re-rendered
   B00, reverified: "screen" now visibly typed in terracotta and doomed by
   t≈9s, backspaced and replaced with "concept" by t≈11s of the fixed
   clip's natural (pre-truncation) timeline.

   That surfaced a second layer: the fixed clip still didn't show the
   completed correction, because `BrutalistHesitantWriter` renders a
   **fixed 606-frame (20.2s) composition** (`Root.tsx`) regardless of
   text length, and `remotion_scenes.py`'s post-render `extend_clip_to_
   duration` step truncates (never re-extends) that to the beat's
   `actual_duration_s` (10.56s here) by simply cutting the first N
   seconds — it does not know or care where in the performance the
   trigger-word swap happens. With the original hesitation dials
   (`mistakeRate:6, hesitateWithin:2, hesitateBetween:14, charMs:48`),
   the accumulated random pause time pushed the swap's completion past
   the 10.56s truncation point even after the wording fix. Fixed by
   zeroing the three probabilistic hesitation dials (they were flavor,
   not the pedagogical point — the trigger-word pause/backspace/retype
   *is* the hesitation this beat exists to show) and dropping `charMs`
   48→38: re-rendered, reverified the corrected question ("matches the
   concept?") completes and holds by t≈7s of the 10.56s clip, comfortably
   inside the window. Logged here rather than worked around, since this
   is a component-level gap (silent no-op on a malformed multi-word
   `triggerWords` prop, plus a fixed-duration composition with no
   duration-aware truncation) that will recur on any future
   `BrutalistHesitantWriter` beat authored with a multi-word trigger.

Recompiled after both fixes. Result: `books--claude-liam-troubleshooting.mp4`,
19/19 beats filled real (no slate), 223.1s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (19 beats, no violations)
- frame-check: PASS (3840×2160, 19 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (after the chip-wrap fix above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.7 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 223.1s; mp4
  mtime newer than beat_sheet.json mtime
- Gate V (visual): pulled frames at 6s spacing across the full runtime
  (37 frames) plus targeted checks of B00 (correction verified landing
  and holding by t≈7s, both pre- and post-fix), NB07 (confirmed a
  mid-fade-in frame that looked wrong was just an animation-timing
  artifact — verified clean at a stable later frame), BCRY, BHTF, BOUT.
  No blockers: legible everywhere, safe inset respected, no text overlap,
  correct @HumanitariansAI handle and HAI outro skin throughout.
- B00 TIMING LAW: `actual_duration_s` 10.56s (≥8s requirement met); the
  "screen"→"concept" correction lands on screen and holds by t≈7s.

**Non-blocking warning (compile.py):** motion histogram graphic:15
remotion:4 — graphic at 78%, over the ~40% pantry cap in MOTION.md.
Structural, same disposition as every `books--claude-liam-*` sibling in
HAILOOP-LOG.md: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as
REMOTION against a 15-beat GRAPHIC body carried over from the source's
argument. Logged per the honesty rule rather than reworking beat count to
dodge the warning.

Metadata file written: `books--claude-liam-troubleshooting.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per playlists.json, neither SUBJECT.json's family ("books")
nor the "books--" slug prefix has a literal map entry, and the skill-name
fallback ("hai-simple" → "Claude Basics") would misfile this — multiple
sibling redos from this same source book already established and logged
this exact reasoning, content-matching to "Extending Claude — Skills,
Plugins & Connectors" instead of falling through to `_default`. Followed
that precedent for consistency across the family. Direct code link per
DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
