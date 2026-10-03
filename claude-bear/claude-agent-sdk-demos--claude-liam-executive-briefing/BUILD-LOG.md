# BUILD-LOG — claude-agent-sdk-demos--claude-liam-executive-briefing

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-agent-sdk-demos/youtube/claude-liam-executive-briefing/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `source_skill`
pointing at the `executive-briefing` Anthropic Skill from the email-agent
SDK demo). 7 beats: B00 cold open, B01 anatomy, B02 pipeline, B03 design
tell, BVDT verdict, BHTF handoff, BOUT outro — all already REMOTION patterns
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond the WRITER LAW swap at B00 — no beat in the
source planned as `ai-video-prompt`, pantry, or a human-drop slot.

Facts carried over unchanged: `executive-briefing` transforms research
findings into executive-ready briefings and is "automatically activated when
user mentions 'executive', 'briefing', 'C-suite', 'board', 'leadership', or
'presentation'" (the source's own description); anatomy is one file,
`SKILL.md` (~4k), no other files; the pipeline is linear — read SKILL.md,
execute each step in order, return the result; same input produces the same
output every run; the boundary is anything outside what the file specifies.

B00 replaced the source's `ClaudeComposerAsk` cold open (which read the
skill's raw description aloud, no wrong-guess framing) with
`BrutalistHesitantWriter` (WRITER LAW: "judgment" → "list" — the naive
assumption that the skill senses intent, corrected to the fact that it
matches a fixed, printed trigger-word list). Register re-registered
Teardown → Plain: the source's B03 framed the same underlying fact
(activation bounded to a literal spec) as "what it gets right" / "what it
bites" — Teardown trade-off language — which this reel restates as
mechanism/boundary facts with no verdict on the design. Source's BVDT
verdict recap folded into a dedicated BCRY carry-out beat per CARRY-OUT LAW
(same disposition as the `claude-liam-action-creator` redo precedent in this
family). Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Added an anchor not explicit in the source but dramatizing its own
stated activation rule: B02 → B03, the same research memo requested two
ways — "turn this into a board presentation" (hits the list, fires) vs.
"make this shorter for my boss" (identical intent, misses the list, silent)
— and a both-directions beat (B03: reliable when the words match / silent
when they don't, regardless of meaning) per this factory's PHASE 1
structure requirement. No inference flag was needed — every claim is read
directly off the source's own stated activation rule and Steps section.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.14s, B01 15.40s, B02 16.23s, B03 15.34s, BCRY 10.18s, BHTF 13.67s,
   BOUT 3.58s.
2. Wrote `scenes.py` (3 Manim scenes, B01-B03, reel-unique names
   `EBRB01Scene`/`EBRB02Scene`/`EBRB03Scene` per the naming-collision lesson
   documented in sibling BUILD-LOGs in this family) and `render_scenes.py`;
   rendered all three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground.
   The invocation exceeded the tool's 120s default window twice and was
   re-run with an explicit longer timeout rather than backgrounded — per
   the one-shot-invocation law, every render step stayed in the foreground
   and the turn never ended mid-render; all 4 beats completed, exit 0 on
   the final run (`[remotion] done`).
4. B00 verified directly: `media/B00.mp4` = 11.17s (comfortably clears the
   ≥8s TIMING LAW floor). Pulled frames at t≈4.5s/7s/9.5s: the correction
   ("judgment"→"list") is complete and legible by t≈9.5s.
5. `compile.py` → first pass 7/7 real (no slate), 3840×2160 (THE 4K LAW),
   86.5s.

**GATE T (type_check.py) — real bugs found and fixed by direct frame
inspection, not by trusting the checker's generic boilerplate fix text:**

- First pass: FAIL (2). **B01** kerning: a real layout bug, not a font
  issue — the code scaled/moved `skill_box` to the left edge but forgot to
  move `skill_card` (the SKILL.md text) with it, leaving an empty
  terracotta box on the left while the stranded text overlapped the
  trigger-word chip grid in the center, producing the "glyph gap" the
  checker flagged. Fixed by grouping `VGroup(skill_box, skill_card)` before
  animating. **B03** contrast + kerning: the strikethrough `Cross` mobject
  was drawn directly on top of the three pipeline-step boxes' text
  (rendering as literal crossed-out, partially-occluded words — "Run th✕e
  steps"), and the bottom "ordinary rewrite" card visually collided with
  the closing spark sentence beneath it. Fixed by replacing the
  overlapping Cross with a `set_opacity(0.3)` dim on the pipeline boxes
  (paired with an existing "stays dark" label) and re-deriving the rewrite
  card's position from `next_to(dark_label, DOWN, ...)` with a bigger
  gap before the spark line. Also switched three prose-text elements from
  TERRA to INK (`type_check.py`'s §8.3 flags ANY terracotta-colored
  multi-character text run against cream at a fixed reference ratio
  ~2.74:1, regardless of the exact hex used — confirmed by reading the
  checker's source; terracotta remains on non-text structural elements
  only, per the "one terracotta moment" rule).
- Second pass: FAIL (1, B01 only) — kerning again, but the layout bug was
  already fixed. Traced to a genuinely different root cause: `type_check.py`
  samples a FIXED frame at dead-middle of the beat's un-slowed source clip
  duration, and that exact timestamp landed mid-way through a `LaggedStart`
  staggered chip fade-in, catching a chip at ~55% opacity. Partially
  transparent glyphs drop thin strokes below the checker's dark-pixel
  threshold unevenly across a word, fragmenting the detected text run and
  reading as an oversized inter-glyph gap — confirmed by extracting the
  checker's exact sample frame and visually inspecting the faded chip.
  Fixed by replacing the staggered `LaggedStart` with a single simultaneous
  `FadeIn(chips)` and restructuring the beat's timeline so a ~3s fully-
  settled static hold straddles the checker's fixed sample point with
  comfortable margin on both sides — a general lesson for any Manim beat
  in this factory: never leave a multi-second staggered/partial-opacity
  animation spanning the clip's exact midpoint.
- Re-ran GATE T after each fix; final run: PASS (0 FAILs).

**Gate V (visual):** pulled frames every 8s across the full 86.5s runtime
and read them directly. B00's title correction reads with margin. B01's
one-file card (SKILL.md, ~4k plain text) and the six-word trigger list read
cleanly, fully settled, no overlap. B02's THE ANCHOR (research memo → "board
presentation" → two words lighting up → three-phase pipeline firing →
structured executive brief) reads cleanly. B03's ANCHOR RETURNS (same memo,
"make this shorter for my boss," no words lit, pipeline dimmed to "stays
dark," ordinary-rewrite card, spark line) reads cleanly with no overlap.
BCRY's carry-out card, BHTF's Your Turn composer card (prompt legible,
`@HumanitariansAI` folder label correct), and BOUT's outro/subscribe card
all render legibly with safe inset respected. **Noted, not a defect
introduced here:** `OutroCTA` renders on a flat-white background rather
than the humanitarians cream ground — same shared-component behavior
already unremarked in sibling `hai-simple` reels' delivered masters; not a
regression from this build, not fixed here (outside this reel's scope).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the fixes above
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), well
  above the -40 dB floor
- ffprobe: video 3840x2160 h264 24fps, audio aac 48kHz present, duration
  86.54s; mp4 mtime (1787974058) newer than beat_sheet.json mtime
  (1787973275)

Metadata file written: `claude-agent-sdk-demos--claude-liam-executive-briefing.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`claude-agent-sdk-demos` matches no prefix in the map, so resolution fell
through to the `hai-simple` skill prefix, which maps to "Claude Basics" —
plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
