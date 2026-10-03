# BUILD-LOG — claude-basics--claudeforfoundationmodels-same-api-key-shipped-prototype

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/claudeforfoundationmodels-same-api-key-shipped-prototype/beat_sheet.json`
(an unbuilt Teardown-register `ai-explainer` scaffold — `"filled": 0, "of": 8`,
no SCRIPT.md, CHECKS-REPORT.md shows `checks_green: False` and a BLOCKED
bookend gate: no `BrutalistHesitantWriter`/hesitant-writer cold open, no
`BVDT`/`BHTF` beats). Question, facts, and beat count (8) carried over
unchanged; the source's B00 (a `FormBCard` text card stating the concrete
`.apiKey`/`.proxied` case) and B04 (the same worked example, repeated in B03
and B05) were folded into this reel's B02/B04 anchor pair, since hai-simple's
spine plants a concrete case after stakes/wrong-guess and pays it off late,
rather than opening cold on it. B00 replaced with `BrutalistHesitantWriter`
(WRITER LAW: "hide" → "move"), register re-registered Teardown → Plain (the
source narration carried no actual verdict to strip), close/outro re-skinned
to `OutroCTA` / @HumanitariansAI with Liam's sign-off. No source beat was
`ai-video-prompt`, pantry, or a human-drop slot (all were already
`FormBCard`/`ClaudeComposerAsk`/`ClaudeTitleOutro` Remotion shapes, just
unbuilt), so NO-GENAI/NO-PANTRY LAW required no substitution beyond B00.

Wrote fresh: QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (8 beats:
B00 writer, B01–B04 GRAPHIC/Manim, BCRY/BHTF/BOUT Remotion). GATE T (`type_check.py`)
PASS on the first pass (0 FAILs, 8 beats checked). Generated audio
(`generate_audio_kokoro.py`, free/local) — all 8 measured durations written
back to the sheet: B00 9.92s, B01 15.57s, B02 15.85s, B03 13.85s, B04 18.45s,
BCRY 8.77s, BHTF 18.69s, BOUT 7.02s. B00 comfortably clears the ≥8s TIMING LAW
floor.

Wrote `scenes.py`/`render_scenes.py` (custom Manim, humanitarians palette
#F3EBDD/#2F2A26/#E4572E/#1F4E5F) for B01–B04, matched to the exact measured
durations, following the same pattern as the sibling reel
`hai-simple/claude-basics--anthropic-sdk-php-server-hands-back-encrypted-context`.
Rendered all four in the foreground. **First-pass QC caught three real text-
overlap defects** (checked via ffmpeg frame pulls, not assumed clean):
B01 "SHIP" label collided with "DECOMPILE" label; B02 "before release" arrow
caption was clipped by the release-card edge; B04's "no user ever holds this
binary" caption overlapped the SERVER YOU CONTROL card. Fixed all three by
repositioning labels/cards with more clearance, re-rendered the three
affected scenes, re-pulled frames, confirmed clean. Rendered the four
Remotion beats (`remotion_scenes.py`, foreground — one invocation ran past
the shell's 120s timeout and was moved to background by the harness; blocked
on it via TaskOutput rather than ending the turn, per the one-shot-invocation
rule, and confirmed exit code 0 with all four `media/*.mp4` written before
proceeding). Verified B00's correction ("hide" → "move") is legible on
screen well within the beat (frames pulled at 6.5s and 9.0s, both before the
9.9s end).

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `claude-basics--claudeforfoundationmodels-same-api-key-shipped-prototype.mp4`,
8/8 beats filled real (no slate), 109.1s, 3840×2160 (4K LAW forced the clean
master straight to 2160p).

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect, verified
  independently after compile), max -3.0 dB
- ffprobe: video 3840×2160, audio stream present, duration 109.125s; mp4
  mtime (1787908446) newer than beat_sheet.json mtime (1787908410)
- Gate V (visual): pulled 14 frames at 8s spacing across the full runtime
  and read every one directly (not sampled/skipped). All legible, correct
  sequence, no overlap, safe inset respected. The B02→B04 anchor pair (dev
  `.apiKey()` code card vs. release `.proxied()` + relay, paid off with the
  release path completing unbroken through the relay to Claude while a
  "SERVER YOU CONTROL" path reaches Claude directly with no relay) reads as
  the same composition returning, per ANCHOR LAW. No blockers.

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:4 — remotion at 50% of beats, over the ~40% pantry cap in MOTION.md.
Structural, not a defect: hai-simple's mandated shape is B00 (writer) + BCRY
+ BHTF (Your Turn) + BOUT (outro) all REMOTION by skill contract, against 4
GRAPHIC body beats for this 8-beat reel — the ratio is fixed by beat count,
identical to the sibling `anthropic-sdk-php-server` reel's logged warning.
Logged per the honesty rule rather than reworking beat count to dodge it.

Metadata file written:
`claude-basics--claudeforfoundationmodels-same-api-key-shipped-prototype.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `claude-basics` family
prefix — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4
(4K render + deliver.py) in this same invocation.

## 2026-08-28 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-basics--claudeforfoundationmodels-same-api-key-shipped-prototype.mp4 \
   claude-basics--claudeforfoundationmodels-same-api-key-shipped-prototype-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
