# BUILD-LOG — claude-code--claude-liam-plugin-structure

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of a fully-built Teardown "skill-teardown"
sheet (`anthropics/claude-code/youtube/claude-liam-plugin-structure/beat_sheet.json`,
7 beats, Claude Code plugin-dev `plugin-structure` skill, brand `claude-liam`,
`@NikBearBrown`). SUBJECT.json's `source_sheet`/`source_dir` pointed at a
nonexistent `/Users/bear/Documents/CoWork/...` path; found the equivalent
source locally under `anthropics/claude-code/youtube/claude-liam-plugin-structure/`
and read it plus its `.md`/`.srt` in full.

Kept beat count (7) and every fact: the manifest `plugin.json` lives inside
`.claude-plugin/` and needs exactly one field, `name` (kebab-case); every
other component — `commands/`, `agents/`, `skills/`, `hooks/` — lives at the
plugin's own root, one level up; auto-discovery needs no registration step;
commands/agents are permissive (any correctly-placed markdown file works);
skills are strict — each needs its own subdirectory containing a file named
exactly `SKILL.md`; renaming that file to `readme.md` fails silently, no
error, the skill just disappears from the list. Remapped the source's B05
Teardown "gets right / where it bites" framing into B03's both-directions
beat (auto-discovery holds exactly as advertised when the filename is right;
fails silently when it's wrong in this one specific way — same facts, no
verdict), and its BVDT verdict into a single BCRY carry-out sentence per
CARRY-OUT LAW. Anchor B02→B03: the skills subdirectory requiring a file
named exactly `SKILL.md`, planted with the filename typing itself into
place and the skill card lighting up, paid off with the same sequence
renaming to `readme.md` and the card going dark with no error.

B00 WRITER LAW: naive guess "inside" .claude-plugin → corrected to "outside"
(the actual misconception the source calls its single most common mistake);
36-word narration + `lead_silence_s: 0.8`, measured 11.86s (clears the
TIMING LAW ≥9s window); verified on a frame pull mid-beat that the writer's
final text reads "does it go outside .claude" — correction confirmed on
screen well before the beat ends.

Picked up a prior session's near-complete artifacts on this invocation
(beat_sheet.json, SCRIPT.md, CARRY-OUT.md, QUESTION.md, Kokoro audio for all
7 beats, all 3 Manim GRAPHIC renders in `manim/`, 3 of 4 REMOTION renders —
B00/BCRY/BOUT already in `media/`) and continued rather than rebuilding, per
COMPLETION LAW:

1. Rendered the one missing beat, BHTF (`ClaudeComposerAsk`, Your Turn), via
   `remotion_scenes.py --only BHTF` in the foreground — `ok: ClaudeComposerAsk
   -> media/BHTF.mp4 (extended to 24.6s)`.
2. `compile.py` — 7/7 slots filled (B00/BCRY/BHTF/BOUT VIDEO, B01/B02/B03
   MANIM), content-check/frame-check/lane-check all PASS, GATE AUDIO PASS
   mean_volume -23.8 dB. THE 4K LAW forced the clean master natively to
   3840×2160 (no `--review` flag used).
3. Independently reverified with ffprobe/ffmpeg rather than trusting
   compile.py's own report: master mtime (1787989420) newer than
   beat_sheet.json mtime (1787989335); h264 3840×2160 + aac streams present,
   duration 101.08s; `ffmpeg -af volumedetect` mean_volume **-23.8 dB**, max
   -2.9 dB — independently confirms GATE AUDIO.
4. GATE T (`type_check.py`): **PASS, 0 FAILs, first pass** — all 7 beats
   §8.10 SKIP (no kerning issues flagged).
5. Gate V: pulled 10 frames at 6s spacing across the full 102s runtime and
   read all of them directly — B00's writer-open correction, B01's
   manifest-card/root-level-folders diagram, B02's five-component anchor
   plant (SKILL.md typing into place, card lighting up), B03's anchor
   payoff (renamed to readme.md, card going dark, "no error. no warning.
   just gone." caption), BCRY's carry-out quote card, BHTF's Your Turn
   composer card, and BOUT's outro/subscribe card all read legibly with
   safe inset respected and no text overlap. No defects found — no fixes
   needed this pass.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, first pass)
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: duration 101.08s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4 graphic:3
— remotion at more than half of beats. Structural, not a defect: hai-simple's
mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT (outro) all
REMOTION by skill contract, against 3 GRAPHIC body beats for this 7-beat
reel — same disposition as every other short hai-simple reel in this family.
Three body-beat Manim clips were time-stretched by compile.py to fill their
measured audio durations (B01 9.3s→17.0s at 1.83x, B02 9.4s→18.9s at 2.01x,
B03 8.4s→14.7s at 1.75x); spot-checked in the Gate V frame pull, no visible
artifacting (static-camera Manim compositions, no fast motion to stretch).

Metadata file written: `claude-code--claude-liam-plugin-structure.md`
(channel @HumanitariansAI, Playlist: **Claude Code** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`claude-code` matches the map's `claude-code` prefix directly — plus the
direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-29 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.
