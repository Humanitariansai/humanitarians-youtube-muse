# BUILD-LOG — claude-code--claude-liam-hook-development

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-code/youtube/claude-liam-hook-development/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `source_skill`
pointing at `claude-code/plugins/plugin-dev/skills/hook-development/SKILL.md`).
7 beats: B00 cold open (`ClaudeComposerAsk`, REMOTION — not AI-video/pantry,
so NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW
swap), B01 anatomy, B02 design, B05 teardown, BVDT verdict, BHTF handoff,
BOUT outro.

Facts carried over unchanged: hooks are event-driven automation scripts,
nine event types (`PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`,
`SubagentStop`, `SessionStart`, `SessionEnd`, `PreCompact`, `Notification`);
two hook types — command (bash, deterministic) vs prompt-based (LLM
judgment, only on Stop/SubagentStop/UserPromptSubmit/PreToolUse);
`PreToolUse` returns allow/deny/ask via `permissionDecision` and can rewrite
the call via `updatedInput`; two config formats — plugin `hooks/hooks.json`
(wrapped in a `hooks` key) vs `.claude/settings.json` (events at the top
level), mixing them is a silent failure with no error message; matchers
(exact/pipe/wildcard/regex, case-sensitive); hooks matching the same event
run in parallel and can't see each other's output; exit code 0 = success,
exit code 2 = blocking error fed back to Claude; source's Your Turn worked
example (a PreToolUse hook blocking `.env`/system-path writes, checking the
plugin wrapper shape, `${CLAUDE_PLUGIN_ROOT}`, and a set timeout).

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "reminder" → "hook" — the naive
assumption that telling Claude to remember something in conversation is
equivalent to configuring an event trigger, corrected to the fact that a
hook lives in a config file read regardless of conversation state).
Register re-registered Teardown → Plain: the source's B05 framed the
config-format gotcha, the no-hot-swap constraint, and the parallel-gap as
"what it gets right" / "where it bites" including a judgment that the
skill's own docs bury the warning — Teardown language — restated here as a
mechanism/failure-mode fact (B03) with no verdict on the skill's
documentation. Source's BVDT verdict recap folded into a dedicated BCRY
carry-out beat per CARRY-OUT LAW (same disposition as the `action-creator`
redo precedent in this family). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Added an anchor (B02 → B03: the
`PreToolUse` hook blocking `.env` writes, reliable in the right config
shape / silent in the wrong one) and a both-directions beat (B03) per this
factory's PHASE 1 structure requirement — the source didn't carry these as
distinct beats.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   10.11s, B01 17.62s, B02 18.58s, B03 20.39s, BCRY 8.23s, BHTF 29.10s
   (later re-rendered visually without narration change), BOUT 3.50s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `HDVB01Scene` /
   `HDVB02Scene` / `HDVB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground.
4. B00 verified directly: `media/B00.mp4` = 10.13s (meets the ≥8s TIMING LAW
   floor). Pulled frames at t≈6s/9.5s: the correction ("reminder"→"hook")
   is complete and visible by t≈9.5s.
5. `compile.py` → `claude-code--claude-liam-hook-development.mp4`, 7/7 real
   (no slate), 3840×2160 (THE 4K LAW).

**GATE T (type_check.py) — three real defects found on the first pass, all
fixed and confirmed by direct frame inspection:**

- First pass: FAIL (3 pixel beats). B01: a decorative "..." placeholder
  text scaled to 0.55× rendered at 9px, below the 20px floor — replaced
  with plain `Dot()` mobjects (no text run to measure) and stopped scaling
  the left-side group to near-zero (was `scale(0.01)`, leaving a visible
  stray artifact; switched to a clean `FadeOut`). B02: the two hook-type
  cards were shrunk to 0.4× and kept on screen as persistent thumbnails
  (subtitle text hit 6.4px, plus the shrunk group visually overlapped the
  title and pushed `write → .env` past the left title-safe edge, an actual
  overflow confirmed by a direct frame pull) — redesigned to `FadeOut` both
  cards completely instead of shrink-and-persist, and recentered the
  PreToolUse/outcomes diagram on-axis instead of offset left. B03: a
  bbox-overlap between two stacked `Text()` lines inside `plugin_box` — the
  GATE T advisory ("possible fused run") on the parallel B02 issue pointed
  at insufficient `arrange(DOWN, buff=...)` spacing; increased buff on all
  stacked two-line labels from 0.15–0.2 to 0.5–0.55.
- Second pass: FAIL (2 pixel beats) — B02 still showed a min-size (10px)
  + bbox-overlap + "fused run" advisory together at the exact location of
  a thin terracotta `Line()` I'd drawn across the `write → .env` text to
  represent the block; the strike line itself was being read as a small
  nested text-like blob. Removed the strike line entirely and recolored
  the text to terracotta instead. B03's wrapped-copy choreography (a 0.5×
  scaled copy of the 2-line `plugin_box` VGroup) risked re-introducing the
  same fused-text defect at the smaller scale, so it was replaced with a
  single-line label built via `TransformFromCopy`, sidestepping the tiny
  two-line case altogether.
- Third pass: **PASS (0 FAILs)**.
- **Gate V caught a defect GATE T doesn't check**: pulling frames across
  the full master showed BHTF's `ClaudeComposerAsk` `output` list (3
  "Watch: ..." bullets) wrapping to more lines than the card's height
  allows — the third bullet was clipped off the bottom of frame entirely,
  with the second bullet's wrapped continuation sitting flush against the
  frame edge. `type_check.py` explicitly skips deep checks on this
  component ("hand-drawn pattern (ClaudeComposerAsk)"), so this only
  surfaced on manual visual read. The verified `action-creator` precedent
  in this family didn't use the `output` prop at all on this component —
  removed the `output` array entirely (the three watch-points are already
  spoken in narration) rather than trying to fit less text into the same
  card; re-rendered BHTF alone, recompiled, and confirmed the card now
  fits cleanly within frame at multiple timestamps.

**Gate V (visual):** pulled frames every 8s across the full 108.5s runtime
and read them directly. B00's title correction, B01's file/timeline
diagram, B02's PreToolUse/allow-deny-ask anchor, B03's anchor-return and
config-shape comparison, BCRY's carry-out card, BHTF's Your Turn composer
card (post-fix), and BOUT's outro/subscribe card all read legibly with safe
inset respected and no text overlap. **Noted, not a defect introduced
here:** `OutroCTA` renders on flat white rather than the humanitarians
cream ground — same shared-component behavior already logged unremarked in
sibling reels in this family (`action-creator`, `screenshot-prompt-caching`).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the three fixes above
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: duration 108.538333s; mp4 mtime (1787984251) newer than
  beat_sheet.json mtime (1787984185)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for
this 7-beat reel — same disposition as every other short hai-simple reel in
this family.

Metadata file written: `claude-code--claude-liam-hook-development.md`
(channel @HumanitariansAI, Playlist: **Claude Code** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`claude-code` matches the map's `claude-code` prefix directly — plus the
direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-29 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-code--claude-liam-hook-development.mp4 \
   claude-code--claude-liam-hook-development-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
