# BUILD-LOG — claude-agent-sdk-demos--claude-liam-listener-creator

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-agent-sdk-demos/youtube/claude-liam-listener-creator/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `source_skill`
pointing at the `listener-creator` Anthropic Skill from the email-agent SDK
demo). 7 beats: B00 cold open, B01 anatomy, B02 pipeline, B03 design tell,
BVDT verdict, BHTF handoff, BOUT outro — all already REMOTION patterns
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond the WRITER LAW swap at B00 — no beat in the
source planned as `ai-video-prompt`, pantry, or a human-drop slot. Same
family shape as the `action-creator` and `executive-briefing` siblings
already delivered under this skill.

Facts carried over unchanged: `listener-creator` creates event-driven email
listeners that monitor for specific conditions (urgent emails from boss,
newsletters to archive, package tracking are the source's own worked
examples) and execute custom actions; used when someone wants to be
notified about emails, automatically handle certain emails, or set up email
automation; anatomy is `SKILL.md` (~9k) + a `templates` folder, 2 files;
the Steps section executes top to bottom — read the request, run the step,
return the result, linear, no branching unless a step says so; same input
produces the same output every run; the boundary is anything outside what
the file specifies.

B00 replaced the source's `ClaudeComposerAsk` cold open (which read the
skill's raw description aloud, no wrong-guess framing) with
`BrutalistHesitantWriter` (WRITER LAW: "watcher" → "template" — the naive
assumption that a listener is a live process actively scanning the inbox,
corrected to the fact that it's a template/definition Claude writes to a
file). Register re-registered Teardown → Plain: the source's B03 framed the
same two facts (reliable on repeat, bounded to spec) as "what it gets
right" / "what it bites" — Teardown trade-off language — restated here as
mechanism/boundary facts with no verdict on the design. Source's BVDT
verdict recap folded into a dedicated BCRY carry-out beat per CARRY-OUT LAW
(same disposition as the `action-creator`/`executive-briefing` precedents
in this family). Close re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off. Added an anchor (B02 → B03: a listener defined for
"from boss + urgent → forward", reliable on the exact written condition,
silent on an equally urgent email from a client) and a both-directions beat
(B03) that the source didn't carry explicitly, per this factory's PHASE 1
structure requirement.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   12.31s, B01 17.26s, B02 19.37s, B03 16.83s, BCRY 10.92s, BHTF 15.62s,
   BOUT 3.31s.
2. Wrote `scenes.py` (3 Manim scenes, B01–B03, reel-unique names
   `LCRB01Scene`/`LCRB02Scene`/`LCRB03Scene` per the naming-collision lesson
   documented in sibling BUILD-LOGs) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground.
   First invocation hit the tool's own 120s window mid-render; B00's render
   had completed but the freeze-hold extend-to-narration-duration step
   (`extend_clip_to_duration`) had not yet run when the process was cut off,
   leaving `media/B00.mp4` at the component's natural ~20.2s length instead
   of the narration's 12.31s. Caught by direct ffprobe (duration mismatch
   against `actual_duration_s`), fixed by re-running
   `remotion_scenes.py --only B00 --force` to completion in one call —
   confirmed `media/B00.mp4` = 12.33s afterward.
4. B00 verified directly: pulled frames at t≈6s/9s/11.5s/12.1s — the
   correction ("watcher"→"template") is fully typed and legible by t≈9s,
   well inside the ≥8s TIMING LAW floor, with the final "Is that it?" line
   still typing at the freeze-hold frame (acceptable — the correction itself
   is the pedagogical point and lands with margin).
5. `compile.py` → `claude-agent-sdk-demos--claude-liam-listener-creator.mp4`,
   7/7 real (no slate), 96.6s, 3840×2160 (THE 4K LAW).

**GATE T (type_check.py) — one real bug found and fixed, confirmed by direct
frame inspection:**

- First pass: FAIL — B02 min-size §8.1 + bbox-overlap §8.6b, "two labels
  printing on top of each other." Root cause was NOT the checker's generic
  suggestion (font_size) but a genuine defect: the envelope glyph
  (`Text("✉", font=SANS, ...)`) rendered as a tiny fallback notdef box
  directly on top of the "IF: from boss + urgent / THEN: forward" card text
  — this system's Montserrat has no envelope glyph. Fixed by replacing the
  Unicode glyph with a drawn `Triangle` shape and moving the fire animation
  to a point above the card (`card_group.get_top() + UP*0.35`) instead of
  its center.
- Second pass: FAIL — same bbox-overlap coordinates, unchanged. Direct crop
  of the checker's own flagged region revealed the actual cause was
  unrelated to the envelope: the "Write the condition" phase box (height
  0.85 units) sat too close to its own text and border stroke, so the
  checker's blob-merge treated the rounded-rectangle border as a separate
  text-run overlapping the label inside it. Fixed by increasing all three
  phase-box heights 0.85→1.15 and re-spacing them (1.1→1.4 units apart) for
  more padding between border and glyph ink.
- Re-ran GATE T: PASS (0 FAILs).

**Gate V (visual) — caught three legibility defects GATE T's pixel checks
didn't (thin-line/text crossings and off-camera-frame caption stacking,
below its detection floor), all fixed and reverified by direct frame pulls:**

- B01: "no watcher running" and "Two files." were both on screen
  simultaneously with only ~0.25 units of vertical separation, visually
  colliding into one run-on line. Fixed by sequencing them as single-focus
  captions in the same screen slot (fade one out as the next fades in)
  rather than stacking two independently-timed captions in nearby positions
  — same fix pattern applied to the callout/spark pair below it.
- B03: the three "condition matched" result chips (width 2.0, spacing 2.4)
  were narrower than their own label text at font_size 18, so neighboring
  chips' text visibly overlapped. Fixed by widening chips to 2.55 and
  spacing to 2.8.
- B03: the "reliable" sentence, the arrow, and its cross mark shared the
  same vertical band (arrow ran from the "urgent, from a client" quote
  straight up through the card), so the cross literally struck through the
  reliability sentence's text. Fixed by fading the reliable sentence out
  before the ask/arrow/cross sequence begins (temporal separation) instead
  of trying to route the arrow around it spatially — also caught and fixed
  a follow-on version of the same issue where the vertical arrow instead
  passed straight through the middle result chip; resolved by fading out
  the whole chip row (`result_row`) at the same cut, since its job (showing
  reliability) was already done.
- Re-pulled frames every 8s across the full 96.6s runtime plus a direct
  seek at t=94s for the outro, and read all of them directly after each
  fix: B00's correction, B01's folder/two-files/no-watcher/callout/spark
  sequence, B02's Steps pipeline + THE ANCHOR (boss+urgent→forward
  listener, one fire), B03's THE ANCHOR RETURNS (three clean fires, then
  the client email crossed out with no overlap anywhere), BCRY's carry-out
  card, BHTF's Your Turn composer card, and BOUT's outro/subscribe card all
  read cleanly with safe inset respected.
- **Noted, not a defect introduced here:** `OutroCTA` hardcodes a flat-white
  background rather than the humanitarians cream ground — same shared-
  component behavior already unremarked in the `action-creator` and
  `executive-briefing` sibling reels' delivered masters; not fixed here
  since it's outside this reel's scope.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the fixes above
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840x2160 h264, audio aac present, duration 96.6s; mp4
  mtime (1787976358) newer than beat_sheet.json mtime (1787975311)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for
this 7-beat reel — same disposition as every other short hai-simple reel in
this family. Logged per the honesty rule rather than reworking beat count
to dodge the warning.

Metadata file written: `claude-agent-sdk-demos--claude-liam-listener-creator.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`claude-agent-sdk-demos` matches no prefix in the map, so resolution fell
through to the `hai-simple` skill prefix, which maps to "Claude Basics" —
plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-29 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-agent-sdk-demos--claude-liam-listener-creator.mp4 \
   claude-agent-sdk-demos--claude-liam-listener-creator-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
