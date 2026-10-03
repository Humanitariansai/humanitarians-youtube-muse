# BUILD-LOG — claude-basics--anthropic-sdk-typescript-partial-json-valid-object-before

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/anthropic-sdk-typescript-partial-json-valid-object-before/beat_sheet.json`
(an unbuilt Teardown-register scaffold — 0/8 beats filled, no SCRIPT.md, one
`FormBCard` beat rendered as a slate). Question, facts, and beat count (8)
carried over unchanged; the source's concrete four-chunk `{"q": "solar` case
(originally its own B00 cold open and B04 example) was folded into this
reel's B02/B04 anchor pair, since hai-simple's spine puts the concrete case
after the stakes/wrong-guess beat rather than as the very first thing on
screen. B00 replaced the `FormBCard` text-card cold open with
`BrutalistHesitantWriter` (WRITER LAW: "broken" → "usable"), register
re-registered Teardown→Plain (no design judgment added or removed — the
source narration carried none), close/outro re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. No source beat was `ai-video-prompt`,
pantry, or a human-drop slot (all were already `FormBCard`/`ClaudeComposerAsk`/
`ClaudeTitleOutro` Remotion shapes, just unbuilt), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00 (which the WRITER LAW covers anyway).

Built end to end in this invocation:

1. Wrote `QUESTION.md`, `CARRY-OUT.md` (GATE C — the parser closes every
   open structure for you, so valid means shape-safe, not value-finished),
   `SCRIPT.md` (GATE P, register audit, redo audit against the source), and
   `beat_sheet.json` (8 beats: B00 writer / B01 stakes-wrong-guess / B02
   anchor planted / B03 mechanism / B04 anchor payoff-both-directions / BCRY
   carry-out / BHTF your-turn / BOUT outro).
2. `generate_audio_kokoro.py` — 8/8 mp3s generated, `am_onyx`, $0.00. B00
   measured 12.01s (TIMING LAW: ≥8s required, ≥9s window from the
   `lead_silence_s: 0.8` narration design — met with margin).
3. `scenes.py` + `render_scenes.py` — 4 Manim scenes (B01–B04) authored
   against the measured `actual_duration_s` values and rendered to
   `manim/*.mp4`. THE ANCHOR (B02: four-card snapshot timeline, `{}` →
   `{"q":""}` → `{"q":"sol"}` → `{"q":"solar"}`, each stamped VALID) returns
   at B04 with the same four-card composition split into SHAPE: SAFE /
   VALUE: STILL GROWING (VALUE: DONE on the last card only).
4. `remotion_scenes.py` — 4 Remotion beats (B00 `BrutalistHesitantWriter`,
   BCRY `WantQuote`, BHTF `ClaudeComposerAsk`, BOUT `OutroCTA`) rendered in
   the foreground (one invocation ran past the shell's 120s default and was
   picked up via `TaskOutput` with a longer block timeout rather than ending
   the turn — the render itself completed cleanly, exit 0, all four
   `media/*.mp4` written).
5. Verified B00 directly: `ffprobe` measured 12.03s; pulled frames at 9s and
   11s and read them — "broken" is fully replaced by "usable" on screen with
   no stray characters, well before the beat ends.
6. `compile.py` → `claude-basics--anthropic-sdk-typescript-partial-json-valid-object-before.mp4`,
   8/8 beats filled real (no slate), 112.6s, 3840×2160.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.7 dB
- GATE T (type_check.py): PASS — 0 FAILs across 8 beats (see GATE T fix pass below)
- ffprobe: video 3840×2160, audio stream present, duration 112.58s; mp4 mtime
  (1787890567) newer than beat_sheet.json mtime (1787890528)
- Gate V (visual): pulled 19 frames at 6s spacing across the full runtime and
  read them directly. B00's correction ("broken" struck, "usable" typed in)
  is legible well within the beat. B02/B04 anchor pair uses the same
  four-card snapshot-timeline composition so the payoff reads as the same
  object. B01's THROWS/X cross slightly overlaps the "TH" of "THROWS" —
  text stays fully readable, cosmetic only, not a blocker (same class of
  finding as the sibling reel's B03 arrow/label overlap). B04's "VALUE:
  DONE" label sits close under the widest card's text but does not clip or
  overlap it. BCRY/BHTF/BOUT text is centered, no overlap, safe inset
  respected. No blockers.

**GATE T (kerning/type-spec) fix pass:** `type_check.py` first flagged 3 real
issues that a naive frame-read missed: B01's "HALF-FINISHED STRING" caption
bled 43px past the left title-safe edge (shifted the source-string group from
`LEFT*4.6` to `LEFT*3.9`, narrowed the card); B02's title had a literal
double-space (`streams  {`) that pixel-measured as an 89px kerning gap
(replaced the whole compound header with a plain-word sentence, no embedded
JSON punctuation, avoiding the token-fragmentation false-positive); B03's
bold ALL-CAPS multi-word title tripped the checker's 30%-of-gaps statistical
heuristic for word-spacing vs. letter-spacing (switched to Title Case EB
Garamond, matching B00/B04's already-passing titles); B04's two smallest
caption labels measured 19px, 1px under the 20px (1.9% of 1080) floor
(bumped 15pt to 17pt). Re-rendered the four affected Manim beats, reran
`type_check.py` to a clean PASS, then recompiled. Root-caused each finding
against the actual rendered pixels (`ffmpeg` frame extraction + a Python
port of the checker's own row/run/gap logic) rather than guessing from the
generic "add font=" hint alone — the hint was right for none of the four
individual causes.

**Non-blocking warning (compile.py):** motion histogram remotion:4 graphic:4
— remotion at 50% of beats, over the ~40% pantry cap in MOTION.md. Structural,
not a defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your
Turn) + BOUT (outro) all REMOTION by skill contract, against 4 GRAPHIC body
beats for this 8-beat reel — the ratio is fixed by beat count. Logged per the
honesty rule rather than reworking beat count to dodge the warning.

Metadata file written: `claude-basics--anthropic-sdk-typescript-partial-json-valid-object-before.md`
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
cp claude-basics--anthropic-sdk-typescript-partial-json-valid-object-before.mp4 \
   claude-basics--anthropic-sdk-typescript-partial-json-valid-object-before-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
