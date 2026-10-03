# BUILD-LOG — claude-code--claude-liam-mcp-integration

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-code/youtube/claude-liam-mcp-integration/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `source_skill`
pointing at `claude-code/plugins/plugin-dev/skills/mcp-integration/SKILL.md`).
6 source beats: B00 cold open (`ClaudeComposerAsk`, REMOTION — not
AI-video/pantry, so NO-GENAI/NO-PANTRY LAW required no substitution beyond
the WRITER LAW swap), B01 anatomy, B02 design, B05 teardown, BVDT verdict,
BHTF handoff, BOUT outro.

Facts carried over unchanged: MCP gives a plugin structured tool access to
an external service; two config methods — dedicated `.mcp.json`
(recommended, multiple servers) vs inline `mcpServers` in `plugin.json`
(single server); four server types — `stdio` (local child process), `SSE`
(hosted, OAuth), `HTTP` (REST, token auth), `WebSocket` (real-time); always
`${CLAUDE_PLUGIN_ROOT}` for paths, always HTTPS/WSS, never a hardcoded
credential; tool naming `mcp__plugin_{name}_{server}__{tool}` with two
underscores between each section (`mcp__plugin_asana_asana__asana_create_task`);
a tool-name mismatch is a silent failure, no error reported; pre-allow
specific tool names vs a wildcard (`__*`) that also matches but widens scope
to every tool the server exposes; lifecycle (servers start on plugin
enable, config changes need a Claude Code restart); source's Your Turn
Asana worked example.

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "app" → "MCP server" — the naive
assumption that connecting a service is an app-install step, corrected to
the fact that it's a config entry naming a connection type). Register
re-registered Teardown → Plain: the source's B05 framed the tool-naming
precision, no-hot-swap constraint, and thin multi-server docs as "what it
gets right" / "where it bites" — Teardown language — restated here as a
mechanism/failure-mode fact (B03) with no verdict on the skill's
documentation. Source's BVDT verdict recap folded into a dedicated BCRY
carry-out beat per CARRY-OUT LAW (same disposition as the `hook-development`
redo precedent in this family). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Anchor: B02 → B03, the exact Asana
tool name `mcp__plugin_asana_asana__asana_create_task` (exact match fires
precisely, one underscore off fires silently, a wildcard also fires but
widens scope). Both-directions in B03: exact-and-correct works quietly;
exact-and-wrong fails quietly; wildcard "works" too, at the cost of the
precision the specific name was there to provide. Compressed the source's
three integration patterns (simple wrapper / autonomous agent / multi-server)
out of the 7-beat Plain cut — logged in SCRIPT.md's "Deliberately not
claimed."

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   10.11s, B01 19.31s, B02 34.82s, B03 26.13s, BCRY 10.24s, BHTF 28.67s,
   BOUT 3.41s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `MIVB01Scene` /
   `MIVB02Scene` / `MIVB03Scene`) and `render_scenes.py`; rendered all three
   in the foreground. First render of B02 (11.0s raw) against its 34.82s
   audio would have needed 3.2x slow-mo (compile.py's own >3.0x warning) —
   extended the scene with a worked `.mcp.json` snippet card and
   per-segment labelled reveal of the tool-name build to bring the raw
   clip to 23.1s (1.5x conform, no warning) instead of stretching a short
   clip.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground.
4. B00 verified directly: `media/B00.mp4` = 10.13s (meets the ≥8s TIMING LAW
   floor). Pulled frames at t≈4s/8.5s/9.8s: the correction ("app"→"MCP
   server") is complete and visible well before the beat ends.
5. `compile.py` → `claude-code--claude-liam-mcp-integration.mp4`, 7/7 real
   (no slate), 3840×2160 (THE 4K LAW).

**GATE T (type_check.py) — two real defects found and fixed, plus two
verified false positives added to the checker's established exemption
sets:**

- B01: a Unicode "✕" (U+2715) glyph in the `Montserrat` font wasn't
  resolvable — Manim/Pango silently fell back to rendering the codepoint
  digits ("27"/"15" stacked) as visible text at the X-mark's position. This
  was both the reported bbox-overlap FAIL and a real visual defect (garbage
  digits on screen). Fixed by replacing the Text glyph with two crossed
  `Line()` mobjects.
- B01 (separate, same FAIL after the glyph fix): a `Create(root)` +
  `FadeIn(root_txt)` combo animated the RoundedRectangle border stroke
  drawing progressively while the label was already visible — a
  disconnected corner-arc fragment appeared mid-draw and was picked up as a
  phantom nested text blob overlapping the "external service" label.
  Verified by frame pull at t≈1.2s of the raw clip. Fixed by switching to
  `FadeIn(root)` (no partial-stroke state).
- Remaining B01 FAIL (identical coordinates, persisted after both fixes):
  confirmed via direct frame crop at the checker's own sample point
  (raw `manim/B01.mp4` at duration×0.5) that this is the same
  box-border-encloses-label false-positive class already documented in
  `type_check.py`'s `BBOX_OVERLAP_EXEMPT_PATTERNS` (see `B01Scene`,
  `B02_FiveProperties`, etc. in that file) — the "external service" card's
  closed-stroke bbox trivially encloses its own centered label's bbox by
  design. Added `MIVB01Scene` to that set with the same verification
  comment convention.
- B03: `mean_w`-derived kerning threshold FAIL on the MONO tool-name string
  with heavy underscore runs — same documented false-positive class as
  `B03Doodle`/`SERB04Scene` in `KERNING_EXEMPT_PATTERNS` (underscores sit
  low and thin, dragging the mean glyph width down so normal advance reads
  as an oversized gap). Verified by direct frame pull at the checker's own
  sample point: the string renders as one cleanly kerned, fully legible
  mono run. Added `MIVB03Scene` to that set.
- Also replaced a `Transform(exact, broken)` between two differently-shaped
  MONO strings in B03 with a `FadeOut`/`FadeIn` pair — a Transform between
  texts of different glyph structure interpolates through a distorted
  intermediate frame, which is what the checker's kerning gate is
  specifically designed to catch, and is bad practice regardless of the
  checker.
- GATE T: **PASS (0 FAILs)** after the fixes and the two exemption
  additions (edits committed directly to
  `runtime/scripts/type_check.py`, the shared toolkit script — not a
  reel-local file).

**Gate V (visual):** pulled frames every 4s across the full 133.7s runtime
and read them directly. Caught one real defect GATE T's single mid-clip
sample didn't: B01's "connects" label from the first (local-script→stdio)
example was never cleared before the second (hosted-OAuth→SSE) example
played, so their labels landed on top of each other ("connectsconnects") at
~t=24s. Fixed by fading out the first example's text/arrow/label group
before starting the second. Re-rendered, recompiled, re-ran GATE T (still
PASS), and re-pulled all 33 frames across the full master: B00's title
correction, B01's four-types branch + both-directions comparison (now
clean), B02's two-config-file cards + the anchor's segment-by-segment
tool-name build, B03's anchor payoff (exact string firing cleanly, then
dimming to silence) and the wildcard fan-out, BCRY's carry-out card, BHTF's
Your Turn composer card, and BOUT's outro/subscribe card all read legibly
with safe inset respected and no text overlap. **Noted, not a defect
introduced here:** `OutroCTA` renders on flat white rather than the
humanitarians cream ground — same shared-component behavior already logged
unremarked in sibling reels in this family (`hook-development`,
`action-creator`).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the fixes above
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: duration 133.666667s; mp4 mtime (1787986776) newer than
  beat_sheet.json mtime (1787985431)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for
this 7-beat reel — same disposition as every other short hai-simple reel in
this family.

Metadata file written: `claude-code--claude-liam-mcp-integration.md`
(channel @HumanitariansAI, Playlist: **Claude Code** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`claude-code` matches the map's `claude-code` prefix directly — plus the
direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
