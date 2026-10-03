# BUILD-LOG — claude-basics--anthropic-retrieval-demo-wrapping-same-text-xml-changes

## 2026-08-27 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/anthropic-retrieval-demo-wrapping-same-text-xml-changes/beat_sheet.json`
(an unbuilt Teardown-register scaffold — nothing there was previously rendered).
Question, facts, beat count (8), and the anchor (product-description
plain-vs-XML, paid off with the Robot Building Kit case) carried over
unchanged. B00 replaced `ClaudeComposerAsk` with `BrutalistHesitantWriter`
(WRITER LAW), register re-registered Teardown→Plain (no design judgment
added or removed — the source narration carried none), close/outro re-skinned
to `OutroCTA` / @HumanitariansAI with Liam's sign-off. No source beat was
ai-video-prompt, pantry, or a human-drop slot, so NO-GENAI/NO-PANTRY LAW
required no additional substitution beyond B00.

Picked up this build with SCRIPT.md, beat_sheet.json, all 8 mp3s
(`generate_audio_kokoro.py` already run — measured `actual_duration_s`
written back), 4 Manim renders (B01–B04 in `manim/`), and 4 Remotion renders
(B00, BCRY, BHTF, BOUT in `media/`) already in place from a prior session.
Verified those assets rather than re-rendering, then ran:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `claude-basics--anthropic-retrieval-demo-wrapping-same-text-xml-changes.mp4`,
8/8 beats filled real (no slate), 102.0s, 3840×2160.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160, audio present, duration 102.04s; mp4 mtime newer than beat_sheet.json mtime
- Gate V (visual): pulled 8 frames at 6s spacing across the full runtime and
  read them directly — B00's correction ("decoration" → "a constraint") is
  legible on screen well within the beat; B02/B04 anchor pair uses the same
  composition (plain block vs. tagged block) so the payoff is visually
  recognizable; B03's training-distribution curve is legible; BCRY/BHTF/BOUT
  text is centered, no overlap, safe inset respected throughout. No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.82s (≥8s requirement met); correction
  visible.

**Non-blocking warning (compile.py):** motion histogram remotion:4 graphic:4
— remotion at 50% of beats, over the ~40% pantry cap in MOTION.md. This is
structural, not a defect: hai-simple's mandated shape is B00 (writer) +
BCRY + BHTF (Your Turn) + BOUT (outro) all REMOTION by skill contract, against
4 GRAPHIC body beats for an 8-beat reel — the ratio is fixed by beat count,
not a choice made in this build. Left as-is; logging per the honesty rule
rather than suppressing or reworking beat count to dodge the warning.

Metadata file written: `claude-basics--anthropic-retrieval-demo-wrapping-same-text-xml-changes.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `claude-basics` family
prefix — and the direct code link per DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4
(4K render + deliver.py) next in this same invocation.
