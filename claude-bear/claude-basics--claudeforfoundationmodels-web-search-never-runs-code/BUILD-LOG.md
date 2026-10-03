# BUILD-LOG — claude-basics--claudeforfoundationmodels-web-search-never-runs-code

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/claudeforfoundationmodels-web-search-never-runs-code/beat_sheet.json`
(unbuilt `ai-explainer` scaffold: `"filled": 0, "of": 8`, no SCRIPT.md,
Teardown register, CHECKS-REPORT.md `checks_green: False`, BLOCKED on the
bookend gate — no hesitant-writer/BVDT/BHTF). Question, facts, and beat
count (8) carried over unchanged: `.webSearch(maxUses: 5)` in `serverTools`
and a Swift `lookupFavorites()` in `tools` are declared identically, yet web
search finishes inside one request while `lookupFavorites()` forces a
second — the split is set by who can execute, not how the tool looks.

Built end to end this invocation:

1. Wrote QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (8 beats:
   B00 hesitant writer, B01–B04 GRAPHIC/Manim body, BCRY carry-out, BHTF
   your-turn, BOUT outro). B00 (WRITER LAW): naive framing "A tool call
   should always round-trip through my code — so why didn't web search?",
   `always` -> `sometimes`, matching the source's own wrong-guess framing.
   Register re-registered Teardown -> Plain (source narration carried no
   actual verdict, so no judgment-language needed cutting). Close re-skinned
   from `ClaudeTitleOutro`/`@NikBearBrown` to `OutroCTA`/`@HumanitariansAI`
   with Liam's sign-off. `FormBCard` (the source's body component) is now a
   retired/banned component (SlateCard composition deleted 2026-08-26), so
   B01–B04 use custom Manim scenes instead, per the disposition already
   established on sibling `claudeforfoundationmodels-same-api-key-shipped-prototype`.
   No beat in the source was `ai-video-prompt`, pantry, or a human-drop slot,
   so NO-GENAI/NO-PANTRY LAW required no substitution beyond B00.
2. GATE T (`type_check.py`): PASS, 0 FAILs, before any rendering.
3. Audio: `generate_audio_kokoro.py` (foreground) — 8 beats, $0.00, measured
   durations written back (B00 10.43s … BOUT 7.21s, total narration ≈114.5s).
4. Wrote `scenes.py` (B01Scene–B04Scene, humanitarians palette) using the
   measured durations for wait-fill timing, and `render_scenes.py`. Rendered
   all 4 Manim beats in the foreground.
5. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` (foreground).
   B00 extended to 10.4s — TIMING LAW's >=8s window met; verified the
   "always" -> "sometimes" correction visible on screen by t≈6.5s (confirmed
   again at t≈9.5s: "A tool call should sometimes round-trip through").
6. Compiled. First pass wrote the mp4 under the WRONG filename
   (`claudeforfoundationmodels-web-search-never-runs-code.mp4`, missing the
   `claude-basics--` prefix) because `metadata.slug` in beat_sheet.json had
   been set to the short source slug instead of the full reel-folder slug.
   Fixed the slug field and recompiled — per COMPLETION LAW this is a
   pre-final sheet fix followed immediately by a recompile, not a
   post-compile edit.
7. Gate V: pulled 15 frames at 8s spacing across the full 122.7s runtime and
   read every one. Found one real defect: B01's "✕" (U+2715) crack mark
   rendered as literal hex-codepoint tofu ("27" over "15" stacked) because
   the SANS font (Montserrat) has no glyph for that code point — a genuine
   legibility blocker, not a false positive. Fixed at the root by replacing
   the Unicode glyph with two drawn `Line` mobjects forming an X, re-rendered
   B01 only, recompiled, and re-verified the fix on the recompiled master
   (clean X mark, no tofu, at the same timestamp). All other 14 frames
   (B00 open/correction, B02 anchor plant, B03 mechanism, B04 anchor payoff,
   BCRY carry-out, BHTF composer, BOUT outro) were legible, humanitarians
   palette, safe inset respected, no text overlap. No other blockers.
8. Confirmed master mtime newer than beat_sheet.json mtime after the final
   recompile (1787909973 > 1787909932).

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840x2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py): PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840x2160, audio present, duration 122.75s; mp4 mtime newer
  than beat_sheet.json mtime (confirmed above)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:4 — remotion at 50% of beats, over the ~40% pantry cap in MOTION.md.
Structural: hai-simple's fixed spine (writer cold open + carry-out + your-turn
+ outro are always REMOTION) puts a floor of 4 REMOTION beats on any 8-beat
reel matching the source's beat count; the same disposition was already
logged on sibling redos of this size. Not reworked, since redo-mode's
beat-count contract doesn't authorize inflating the body just to dilute the
ratio.

Metadata file written: `claude-basics--claudeforfoundationmodels-web-search-never-runs-code.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `claude-basics` family
prefix — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-28 — Phase 4 delivery

Master is already 3840x2160 (compile.py's 4K LAW forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.
