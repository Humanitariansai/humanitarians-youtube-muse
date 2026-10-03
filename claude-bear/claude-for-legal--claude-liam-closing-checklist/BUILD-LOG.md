# BUILD-LOG — claude-for-legal--claude-liam-closing-checklist

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-filled Teardown "skill-teardown"
sheet (`anthropics/claude-for-legal/youtube/claude-liam-closing-checklist/beat_sheet.json`,
7 beats, corporate-legal `closing-checklist` Anthropic Skill, brand
`claude-liam`, `audience: "Claude"`). SUBJECT.json's `source_sheet`/
`source_dir` pointed at a nonexistent `/Users/bear/Documents/CoWork/...`
path; found the equivalent source locally under
`anthropics/claude-for-legal/youtube/claude-liam-closing-checklist/` and
read it in full (no `SCRIPT.md` existed there — only `beat_sheet.json`,
`PEDAGOGY.md`, `clips/`, `mp3/timings.json`).

**Same defect class as the `amendment-history`/`aia-generation`/
`ai-inventory` siblings already in this loop's log:** the source's own
narration carries two literal, never-filled `>` placeholders — B03
("Claude's job: >") and BHTF ("I want to >") — meaning the skill's specific
legal task was never recorded on this machine. Per the honesty rule against
inventing UI or unconfirmed specifics, did not fabricate what those
placeholders would have said. Kept every fact the source states outright
about the mechanism: a skill is a folder Claude reads before it works;
`closing-checklist` holds one file total, `SKILL.md`, the whole instruction
set in plain language, no hidden logic; the pipeline lives in the file's
Steps section, read and executed in order, linear, no branching unless a
step says so; the skill is a specification written as an instruction set,
not legal judgment; what it gets right is repeatable results (same input →
same output, every run); what it bites is anything outside what the file
specifies. Reconstructed the checklist's domain purpose only in the generic
terms the title itself gives (building/tracking a transaction's closing
checklist), and remapped the source's B03/BVDT Teardown framing ("the
interesting constraint," "gets right / bites") into a Plain mechanism fact
plus a proper CARRY-OUT beat per CARRY-OUT LAW — no design verdict.

**New anchor (not in the source, added per ANCHOR LAW):** a dashed "?" card
representing a step never written in the `SKILL.md`'s Steps section, planted
at B02 sitting outside the linear step chain, paid off at B03 when an "ask"
arrow points at it and it stays dark — "not written here. doesn't run."
Both-directions beat (B03): spec-bound execution holds exactly as advertised
when the step is written (reliable, repeatable); the same mechanism draws a
flat line when a step is not written (nothing fills the gap) — no verdict on
whether that boundary is a good design choice.

**B00 WRITER LAW:** naive guess "know" (Claude has built-in legal knowledge)
→ corrected to "read" (Claude reads a written file) — the actual
misconception the source's narration implies ("A SKILL.md tells Claude
exactly how"). First-draft narration measured only 8.68s (< the 9s TIMING
LAW floor); lengthened from 29 to 36 words, re-measured 10.67s, clears the
window. Verified on a frame pull (f01/f02 at t=0s/6s) that the writer's text
reads "Does Claude just know" → "Does Claude just read how to build a
closing checklist?" — correction confirmed on screen.

**Build sequence (fresh build, no prior artifacts in this reel dir beyond
SUBJECT.json):**
1. Wrote QUESTION.md, CARRY-OUT.md (GATE C), SCRIPT.md (GATE P draft),
   beat_sheet.json (7 beats, structure mirrored from the
   `claude-code--claude-liam-plugin-structure` sibling — a redo of the same
   skill-teardown source shape, already published in this same directory),
   scenes.py (3 Manim scenes: CCKB01Scene anatomy, CCKB02Scene anchor plant,
   CCKB03Scene anchor payoff), render_scenes.py.
2. `generate_audio_kokoro.py` — 7/7 beats, am_onyx, $0.00. B00 remeasured
   after the narration fix (see above).
3. Manim render (`render_scenes.py`, foreground) — 3/3 GRAPHIC beats ok
   first pass.
4. `remotion_scenes.py` (foreground) — 4/4 REMOTION beats ok (B00 10.7s,
   BCRY 8.6s, BHTF 15.7s, BOUT 3.5s+1.0s tail). Note: the render ran long
   enough that the Bash tool's own timeout backgrounded the shell command
   mid-render; confirmed via `pgrep` that the underlying
   `npx remotion render` / chrome-headless-shell processes were still
   actively working (not orphaned) and waited on process exit rather than
   ending the turn, per COMPLETION LAW — the render completed cleanly and
   its own log showed all 4 beats ok before compiling.
5. `compile.py` — 7/7 slots filled, content-check/frame-check/lane-check
   PASS, GATE AUDIO PASS -24.0 dB, master born natively 3840×2160 (THE 4K
   LAW).
6. GATE T (`type_check.py`) — **1 FAIL first pass**: B01's caption
   "plain language. no hidden logic." at 16px, below the 20px floor. Fixed
   font_size 16→24 in scenes.py, re-rendered, recompiled — GATE T PASS 0
   FAILs.
7. Gate V — pulled 13 frames at 6s spacing across the full 77.4s runtime and
   read them directly. Caught a real defect GATE T's bbox-overlap check
   didn't flag: the same B01 caption fix (font_size 24) made the two-line
   caption wider than its containing card, spilling text past the
   SKILL.md card's border and visibly overlapping the outer folder box
   edge. Fixed by widening the folder (4.4→5.8) and SKILL.md card
   (2.8×1.3→3.2×1.9) and splitting the caption into two shorter lines at
   font_size 20 (still clears the GATE T floor). Re-rendered, recompiled,
   re-ran GATE T (still PASS), re-pulled all 13 frames — B00's writer-open
   correction, B01's now-clean anatomy card, B02's anchor plant (three
   step cards executing in order + the dashed "?" card sitting apart),
   B03's anchor payoff ("ask" arrow, card staying dark, "not written here.
   doesn't run.", "spec, not judgment."), BCRY's carry-out quote, BHTF's
   Your Turn composer card, and BOUT's outro/subscribe card all read
   legibly with safe inset respected and no further text overlap.
8. Independently reverified with ffprobe/ffmpeg rather than trusting
   compile.py's own report: master mtime (1788034218) newer than
   beat_sheet.json mtime (1788033553); h264 3840×2160 + aac streams
   present, duration 77.375s; `ffmpeg -af volumedetect` mean_volume
   **-24.0 dB**, max -3.0 dB — independently confirms GATE AUDIO.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs after 1 fix)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: duration 77.375s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking, noted (shared-component, matches sibling reels' shipped
behavior):** BOUT's `OutroCTA` renders on flat white rather than the
humanitarians cream ground (`#F3EBDD`) — the same cosmetic gap already
logged against several other reels in this loop; not fixed here since it is
a shared Remotion component, not a defect introduced by this build.

Metadata file written:
`claude-for-legal--claude-liam-closing-checklist.md` (channel
@HumanitariansAI, Playlist: **Claude Basics** — `family: "claude-for-legal"`
matches no prefix in `playlists.json`; resolved via the `hai-simple`
skill-key fallback — plus the direct code link per the DELIVERY CONTRACT
format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
