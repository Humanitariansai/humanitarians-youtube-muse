# BUILD-LOG — books--claude-liam-productivity

## 2026-08-28 — review cut, DONE

Fresh build (redo mode) of `claude-liam-productivity` (Teardown,
"The Productivity Plugin" chapter of `claude-cowork-plugins`) as a
hai-simple reel. On pickup, the reel dir held only `SUBJECT.json` — nothing
else existed. Built end to end this invocation.

**Redo compression:** source is a 37-beat Teardown/deep-explainer chassis
(B00 puppet-ask + 6 act cards C01-C06 + 24 body beats B01-B24 + a Teardown
verdict-recap V01 + an old-style your-turn H01 + an old-style outro O01 + a
duplicate BOOKEND closing triad BVDT/BHTF/BOUT carrying explicit verdict
language — "the model's confidence is the model's, not the world's... The
plugin is the tool. The judgment is yours"). Per hai-simple's spine: dropped
the 6 act cards (titles now land as act headers in SCRIPT.md), dropped the
entire duplicate bookend triad and its verdict framing (Plain carries no
verdict), replaced the separate V01 recap with a single CARRY-OUT LAW
sentence, and merged 5 beat-pairs carrying one continuous idea
(B01+B02→NB01, B09+B10→NB08, B11+B12→NB09, B14+B15→NB11, B22+B23→NB18),
landing at 19 GRAPHIC body beats + B00 (BrutalistHesitantWriter) +
BCRY/BHTF/BOUT = 23 beats. Every fact and workflow from the source's 24 body
beats survives in the 19 merged beats. Full audit in SCRIPT.md.

**Build steps this session:**
1. Wrote QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (23 beats),
   scenes.py (generic chip-row Manim renderer + 19 beats' `BEAT_CONTENT`),
   render_scenes.py — following the established pattern from sibling
   `books--claude-liam-product` (same family, same skill, already DONE).
2. `generate_audio_kokoro.py` — all 23 beats, Kokoro `am_onyx`, cost $0.00.
3. `render_scenes.py` — 19 Manim body beats, foreground.
4. `remotion_scenes.py` — B00 (BrutalistHesitantWriter), BCRY (WantQuote),
   BHTF (ClaudeComposerAsk), BOUT (OutroCTA), foreground.
5. **B00 WRITER LAW bug caught and fixed before compile:** first attempt
   used a two-word `triggerWords` ("to-do app" → "foundation layer"). Pulled
   a late frame of `media/B00.mp4` and found the correction never fired —
   the component's trigger matching (`BrutalistHesitantWriter.tsx`) is
   per-whitespace-token, so a two-word phrase never matches a single token
   and silently falls through to plain typing with no hesitation at all.
   Reworded to a single-word swap ("tracks" → "runs": "The productivity
   plugin tracks your tasks for you." → "...runs your tasks for you."),
   regenerated B00's audio and Remotion render, and verified by frame at
   the correction point that "tracks" is typed, paused, backspaced, and
   replaced with "runs" on screen — matches TIMING LAW (9.6s window, well
   over the 9s floor).
6. `compile.py` — 4K master born natively (3840×2160, compile.py's 4K LAW),
   269.1s, `content-check`/`frame-check`/`lane-check` all PASS.
7. `type_check.py` (GATE T) — **FAIL, 3 pixel-beat findings** on first run:
   - NB07 kerning §8.4 (23px gap, threshold 16px) — traced to the bold
     title "LIVE ON INSTALL" containing "INSTALL" (double-L), the same
     class of bold-Garamond glyph-adjacency defect documented in sibling
     `books--claude-liam-product`'s log for "WALL" (double-L). Reworded the
     on-screen title only (not narration, not SCRIPT.md) to "ZERO SETUP" —
     passes clean.
   - NB08 min-size §8.1 (18px < 20px floor) — two long chip labels ("NO
     CALENDAR — USEFUL" / "CALENDAR — TIME-AWARE", 21-22 chars) were
     auto-scaled down by the chip-fit logic below the floor. Shortened to
     "NO CALENDAR" / "TIME-AWARE" (matches the established fix pattern:
     product's NB11 shortened "YOUR HOURS THIS MONTH"→"YOUR HOURS" for the
     same reason).
   - NB19 min-size §8.1 (same cause, chips "+ THE BASE THAT HOLDS" / "YOUR
     OPERATING SYSTEM") — shortened to "THE BASE HOLDS" / "OPERATING
     SYSTEM"; passed on re-check.
   - Re-render surfaced a **new** bbox-overlap §8.6b FAIL on NB08's
     shortened "TIME-AWARE" (18% overlap, bold "M"-"E" adjacency in
     "TIME-AWARE" — visually confirmed by frame crop: the bold glyphs were
     genuinely touching, not a detector false positive). Reworded again to
     single-word "SHARPER" (ties directly to the beat's own title, "STILL
     USEFUL, SHARPER CONNECTED") — re-rendered, recompiled, re-checked:
     **GATE T: PASS, 0 FAILs, 23/23 beats.**
8. Recompiled after all three content fixes: 4K master (3840×2160), 269.1s,
   mtime (18:43) newer than beat_sheet.json (18:40) and every re-rendered
   Manim clip. Non-blocking warning: motion histogram `graphic:19
   remotion:4` (82%, over the ~40% pantry cap) — structural, per
   hai-simple's mandated shape (B00 writer + BCRY + BHTF + BOUT all
   REMOTION against 19 Manim body beats for a 23-beat reel); same
   disposition as every sibling `books--` redo in this family.

**Gate V:** pulled frames at 1 fps (6s stride) across the full 269s master
and read a representative sample spanning every act plus the fixed beats
(B00's correction landing, NB01/NB03/NB06/NB08/NB10/NB12/NB14/NB16/NB18,
BCRY, BHTF, BOUT). All legible, safe-inset, palette-consistent
(humanitarians cream/ink/terracotta), no text overlap anywhere. BHTF
correctly shows `@HumanitariansAI`; BOUT shows the HAI outro skin
(OutroCTA, SUBSCRIBE + @HumanitariansAI), not the source's
ClaudeTitleOutro/@NikBearBrown. No remaining blockers.

**Audio:** `compile.py`'s own `GATE AUDIO` check and an independent
`ffmpeg -af volumedetect` pass agree: mean_volume **-23.9 dB**, well above
the -40 dB floor. Master mtime (18:43:57) newer than beat_sheet.json
(18:40:17).

Metadata file written: `books--claude-liam-productivity.md` (channel
@HumanitariansAI, **Playlist: Claude Basics**). Playlist note:
`SUBJECT.json`'s `family` is `"books"` (no literal map entry), but its
`skill` field is `"hai-simple"`, which *is* a direct key in
`skills/make/hai-simple/loop/playlists.json`'s map → "Claude Basics" — same
resolution as every sibling `books--` reel already delivered. Per the
DELIVERY CONTRACT format, the description also carries the direct code
link.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-28 — Phase 4 delivery

Master is already 3840×2160 natively (compile.py's 4K LAW), so the
Fellows-facing 4K file is the same render, copied to the `-4k` filename
`deliver.py` expects.

```
cp books--claude-liam-productivity.mp4 books--claude-liam-productivity-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```
