# BUILD-LOG — claude-agent-sdk-demos--claude-liam-action-creator

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-agent-sdk-demos/youtube/claude-liam-action-creator/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `source_skill`
pointing at the `action-creator` Anthropic Skill from the email-agent SDK
demo). 7 beats: B00 cold open, B01 anatomy, B02 pipeline, B03 design tell,
BVDT verdict, BHTF handoff, BOUT outro — all already REMOTION patterns
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond the WRITER LAW swap at B00 — no beat in the
source planned as `ai-video-prompt`, pantry, or a human-drop slot.

Facts carried over unchanged: `action-creator` creates user-specific
one-click action templates that execute email operations when clicked in
the chat interface (payment reminders, bug forwarding, newsletter archiving
are the source's own worked examples); anatomy is `SKILL.md` (~12k) + a
`templates` folder, 2 files; the Steps section executes top to bottom —
read the request, run the step, return the result, linear, no branching
unless a step says so; same input produces the same output every run; the
boundary is anything outside what the file specifies.

B00 replaced the source's `ClaudeComposerAsk` cold open (which read the
skill's raw description aloud, no wrong-guess framing) with
`BrutalistHesitantWriter` (WRITER LAW: "code" → "file" — the naive
assumption that a Skill is compiled/executable code, corrected to the fact
that it's a plain-text file of instructions Claude reads). Register
re-registered Teardown → Plain: the source's B03 framed the same two facts
(reliable on repeat, bounded to spec) as "what it gets right" / "what it
bites" — Teardown trade-off language — which this reel restates as
mechanism/boundary facts with no verdict on the design. Source's BVDT
verdict recap folded into a dedicated BCRY carry-out beat per CARRY-OUT LAW
(same disposition as the `screenshot-prompt-caching` redo precedent in this
family). Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Added an anchor (B02 → B03: the one-click payment-reminder
button, reliable on repeat clicks, silent on "negotiate the invoice") and a
both-directions beat (B03) that the source didn't carry explicitly, per
this factory's PHASE 1 structure requirement.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   8.73s, B01 15.47s, B02 17.51s, B03 18.79s, BCRY 9.90s, BHTF 14.98s, BOUT
   3.22s.
2. Wrote `scenes.py` (3 Manim scenes, B01-B03, reel-unique names
   `ACRB01Scene`/`ACRB02Scene`/`ACRB03Scene` per the naming-collision lesson
   documented in the `screenshot-prompt-caching` sibling BUILD-LOG) and
   `render_scenes.py`; rendered all three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (the first invocation exceeded the tool's 120s window and was moved to a
   background task by the harness; blocked on it directly with `TaskOutput`
   rather than ending the turn, per the one-shot-invocation law — all 4
   beats completed, exit 0).
4. B00 verified directly: `media/B00.mp4` = 8.73s (meets the ≥8s TIMING LAW
   floor). Pulled frames at t≈5s/7s/8.5s: the correction ("code"→"file") is
   already complete and visible by t≈5s and stays visible through the end
   of the clip — comfortable margin.
5. `compile.py` → `claude-agent-sdk-demos--claude-liam-action-creator.mp4`,
   7/7 real (no slate), 89.6s, 3840×2160 (THE 4K LAW).

**GATE T (type_check.py) — one real bug found and fixed, confirmed by direct
frame inspection, not by trusting the checker's generic suggestion:**

- First pass: FAIL — B01 kerning §8.4, max inter-glyph gap 52px > threshold
  20px. The checker's boilerplate fix text ("add font='EB Garamond'") was
  misleading — B01's title `Text()` already had `font=SANS` set. Pulled and
  zoomed the actual title frame ("A FOLDER, NOT A PROGRAM") and found a
  genuine glyph-touching defect: the second, later occurrence of the
  standalone word "A" (immediately before "PROGRAM") rendered with zero
  advance width, merging into "APROGRAM", while the first "A" (before
  "FOLDER") rendered fine. Root cause: this system's only installed
  "Montserrat" font file is the *italic* variable font (`fc-match
  "Montserrat"` resolves to `Montserrat-Italic-VariableFont_wght.ttf`); no
  upright Montserrat is installed, and Pango's synthetic-upright path for
  this file appears to mishandle the advance width of a repeated
  single-letter word within one `Text()` string. Fixed by rewording the
  title to avoid a duplicate standalone "A" ("A FOLDER, NOT CODE" — a single
  occurrence). Re-rendered B01; re-zoomed the title frame and confirmed even
  spacing throughout.
- Re-ran GATE T: PASS (0 FAILs).
- While in Gate V (below), also caught and fixed a *sub-floor* legibility
  issue GATE T didn't flag (text too small to be checked): B03's three
  "same email" chip labels at `font_size=16` rendered with visible
  mid-word letter-spacing artifacts ("sam e em ail") — the same broken-font
  class as the B01 bug, just below the pixel-check floor. Fixed by
  bumping the chip to `font_size=20` / chip width 1.3→1.7 units; re-rendered
  B03 and confirmed clean spacing directly.
- Recompiled after both fixes; re-ran GATE T: PASS (0 FAILs) again.

**Gate V (visual):** pulled frames every 8s across the full 89.6s runtime
plus a direct-seek frame at t=86s for the outro, and read them directly. B00
title correction reads with margin. B01's two-file folder (SKILL.md, plain
text / templates) and "no program to run" / "The file is the instruction
set" read cleanly after the title fix. B02's Steps pipeline and THE ANCHOR
(the payment-reminder button, clicked once, envelope flies out) read
cleanly. B03's ANCHOR RETURNS (button clicked three times reliably, then
"negotiate the invoice" struck through with "not in the file") reads
cleanly after the chip-size fix. BCRY's carry-out card, BHTF's Your Turn
composer card, and BOUT's outro/subscribe card render legibly with safe
inset respected. **Noted, not a defect introduced here:** `OutroCTA`
hardcodes a flat-white background (`VOX.CREAM = #FFFFFF` in
`tokens/vox.ts`) rather than the humanitarians cream ground (`#F3EBDD`) —
same behavior already shipped unremarked in the `screenshot-prompt-caching`
sibling reel's delivered master; not a regression from this build, and not
fixed here since it's shared-component behavior outside this reel's scope.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the fixes above
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840x2160 h264, audio aac present, duration 89.6s; mp4
  mtime (1787972154) newer than beat_sheet.json mtime (1787971564)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for
this 7-beat reel — same disposition as every other short hai-simple reel in
this family. Logged per the honesty rule rather than reworking beat count
to dodge the warning.

Metadata file written: `claude-agent-sdk-demos--claude-liam-action-creator.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`claude-agent-sdk-demos` matches no prefix in the map, so resolution fell
through to the `hai-simple` skill prefix, which maps to "Claude Basics" —
plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-28 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.
