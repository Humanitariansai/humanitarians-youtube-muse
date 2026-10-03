# BUILD-LOG — claude-code--claude-liam-plugin-settings

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-code/youtube/claude-liam-plugin-settings/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `source_skill`
pointing at `claude-code/plugins/plugin-dev/skills/plugin-settings/SKILL.md`).
7 beats: B00 cold open (`ClaudeComposerAsk`, REMOTION — not AI-video/pantry,
so NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW
swap), B01 anatomy (file structure + 3 consumers), B02 design (3 usage
patterns + parsing techniques), B05 teardown (gets-right/bites), BVDT
verdict, BHTF handoff, BOUT outro.

Facts carried over unchanged: the file is `.claude/plugin-name.local.md` —
fixed directory, naming, `.local.md` suffix; YAML frontmatter (structured
fields: `enabled`, `mode`, retry counts, lists) above a markdown body
(free-form prompts/context) in one file; three consumers — hooks (bash
`sed` parsing), commands (Read tool), agents (referenced in instructions);
quick-exit pattern (check file exists, check `enabled`, exit 0 for no-op);
three usage patterns in the source (hook toggle, agent state management
per `multi-agent-swarm`, config-driven `validation_level` branching); the
file is user-managed and should be gitignored (unenforced); changes require
a restart, not hot-swapped; the `sed`-based frontmatter parser is fragile
on multiline values, quoted colons, or indented blocks — corrupts silently,
no error.

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "remember" → "read" — the naive
assumption that telling Claude to remember a setting in conversation
persists it, corrected to the fact that a settings file is read back fresh
by three different consumers, regardless of what the conversation still
holds). Register re-registered Teardown → Plain: the source's B05 framed
the restart requirement, the gitignore gap, and the fragile parser as "what
it gets right" / "where it bites" — Teardown language, including a judgment
that the skill's own docs bury the restart warning — restated here as a
mechanism/failure-mode fact (B03) with no verdict on the skill's
documentation. Source's BVDT verdict recap folded into a dedicated BCRY
carry-out beat per CARRY-OUT LAW (same disposition as the `hook-development`
redo precedent in this family). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Added an anchor (B02 → B03: the
`enabled` field driving the quick-exit pattern, reliable when flat / silently
mis-parsed when the YAML gets complex) and a both-directions beat (B03) per
this factory's PHASE 1 structure requirement — the source didn't carry
these as distinct beats.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.29s, B01 18.79s, B02 18.54s, B03 19.01s, BCRY 8.49s, BHTF 26.43s,
   BOUT 3.61s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `PSVB01Scene` /
   `PSVB02Scene` / `PSVB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground. One real bug caught before it reached GATE T:
   `field.become(...)` was passed directly to `self.play()` (a Mobject,
   not an Animation) — `Scene.play` raised `TypeError: Unexpected argument
   VMobjectFromSVGPath`. Fixed by building the replacement Text and using
   `Transform(field, new_field)` instead.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground.
4. B00 verified directly: `media/B00.mp4` = 11.3s (meets the ≥8s TIMING LAW
   floor). Pulled frames at t≈6s/9.5s: the correction ("remember"→"read")
   is complete and visible by t≈9.5s ("How do I get Claude Code to read my
   plugin's...").
5. `compile.py` → `claude-code--claude-liam-plugin-settings.mp4`, 7/7 real
   (no slate), 3840×2160 (THE 4K LAW).

**GATE T (type_check.py): PASS on the first pass — 0 FAILs.** No pixel-level
defects found across all 7 beats (min-size, overflow, contrast, bbox-overlap,
card-clip, kerning all clean).

**Gate V (visual):** pulled frames every 8s across the full 107.2s runtime
plus a direct pull of the BOUT beat (not captured by the 8s grid), and read
all of them directly. B00's title correction, B01's file/session-divider
diagram, B02's three-consumer fan-in and `enabled`/quick-exit anchor, B03's
anchor-return (three correct toggles) and the YAML-scan-goes-wrong payoff,
BCRY's carry-out card, BHTF's Your Turn composer card, and BOUT's
outro/subscribe card all read legibly with safe inset respected and no text
overlap. **Noted, not a defect introduced here:** `OutroCTA` renders on flat
white rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family
(`hook-development`, `action-creator`, `screenshot-prompt-caching`).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs, first pass)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: duration 107.160333s; mp4 mtime (1787988015) newer than
  beat_sheet.json mtime (1787987914)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for
this 7-beat reel — same disposition as every other short hai-simple reel in
this family. Also noted: three body-beat Manim clips were time-stretched
1.57–1.76x by `compile.py` to fill their measured audio durations (B01
10.7s→18.8s, B02 11.6s→18.5s, B03 12.1s→19.0s) — checked by direct frame
read at multiple timestamps per beat; no visible artifacting from the
slowdown (static-camera Manim compositions, no fast motion to stretch).

Metadata file written: `claude-code--claude-liam-plugin-settings.md`
(channel @HumanitariansAI, Playlist: **Claude Code** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`claude-code` matches the map's `claude-code` prefix directly — plus the
direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
