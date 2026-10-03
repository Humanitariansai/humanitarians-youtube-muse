# BUILD-LOG — books--claude-liam-data

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/books/claude-cowork-plugins/youtube/claude-liam-data/beat_sheet.json`
(Ch.7 "The Data Plugin", Teardown/deep-explainer source). Question, facts,
and full five-act body argument carried over unchanged (natural-language
querying; the four kinds of work — explore, clean, visualize, compare; the
anchor: three clients / sixty percent / one sliding since September, paid
off with the follow-up that catches it early; the honesty beat — the
plugin's read is only as trustworthy as the data and assumptions under it,
and it surfaces the number, never the call). B00 replaced the source's
puppet-ask framing with `BrutalistHesitantWriter` (WRITER LAW: "formulas" →
"a plain question"), register re-registered Teardown→Plain (no design
judgment added; the source's own honesty beats — NB18–NB20 — already
carried the "your data, your assumptions, your judgment" caveat without
verdict language, so nothing needed removing), close re-skinned to
`WantQuote`/`ClaudeComposerAsk`/`OutroCTA` with @HumanitariansAI and Liam's
sign-off. Source's 33-beat deep-explainer chassis (5 act-title cards +
24 numbered body beats, incl. a duplicate blank-narration bookend triad)
was compressed to this skill's spine: act cards dropped (titles now land as
narration transitions), 3 beat-pairs merged where they carried one
continuous idea (B02+B03→NB02, B10+B11→NB09, B15+B16→NB13), landing at 21
GRAPHIC body beats + B00 + BCRY/BHTF/BOUT = 25 beats total. Full audit in
SCRIPT.md's "Beat-count note (redo)" section. No source beat was
ai-video-prompt, pantry, or a human-drop slot — NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00.

Picked up this build already at SCRIPT.md, beat_sheet.json, all 25 mp3s
(`generate_audio_kokoro.py` already run, `actual_duration_s` written back),
B00 Remotion render, and all 21 GRAPHIC beats rendered via a shared
generic "chip row" Manim template (`scenes.py`/`render_scenes.py`, one
title + up to 5 labeled chips + optional arrows/accent/strike + caption,
parametrized per beat from a `BEAT_CONTENT` table) — in place from a prior
session, but `TYPECHECK.md` was FAIL with 3 real defects, so the review cut
had never actually passed Gate T:

- **NB06/NB13 contrast §8.3 FAIL** — accented chips used a solid TERRA fill
  with reversed GROUND text. Direct pixel sample of the rendered frame
  showed pure TERRA (#E4572E) renders at mean gray ≈119 — *under* GATE T's
  gray<120 dark/light split — so the fill itself, not the text, was being
  counted as "foreground text" and averaged against the cream ground. Fixed
  at the root: accented chips are now INK-on-cream (identical to every
  passing non-accented chip) marked instead by a small TERRA
  underline/border, small enough in area that it can't dominate the
  frame's dark-pixel population the way a filled block does.
- **NB16 bbox-overlap §8.6b FAIL** — a stroked box border is itself a
  connected blob spanning the whole chip; an isolated 2-letter fragment
  ("IF" in "NO PLAN IF THEY LEAVE") happened to survive the text-run shape
  filter too and landed fully nested inside it, tripping the check on a
  border that was never printing over anything (verified by frame pull —
  no real text-on-text collision). Fixed at the root, not by exemption:
  removed the stroked border from every chip (accented and not) in favor of
  a faint INK-tinted fill (`fill_opacity`, gray comfortably >200) — no
  closed stroke loop exists anymore to misdetect.
- Also tightened the chip label auto-scale from sequential
  `set_width`/`set_height` calls (which could re-expand a just-shrunk long
  label back past the box edge) to a single uniform scale factor with more
  margin, reducing the odds of a future label touching the border.

Re-rendered all 21 GRAPHIC beats after the `_chip()` fix; `type_check.py`
went from 3 FAILs to **PASS, 0 FAILs**. Re-rendered the 3 non-B00 REMOTION
beats (BCRY `WantQuote`, BHTF `ClaudeComposerAsk`, BOUT `OutroCTA` — B00 was
already correct and untouched) via `remotion_scenes.py`, then compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `books--claude-liam-data.mp4`, 25/25 beats filled real (no slate),
305.0s, 3840×2160.

**Gates:**
- content-check: PASS (25 beats, no violations)
- frame-check: PASS (3840×2160, 25 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see defect fixes above)
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio present, duration 304.98s; mp4 mtime
  (13:02) newer than beat_sheet.json mtime (12:57)
- Gate V (visual): pulled 25 frames at 12s spacing across the full runtime
  and read them directly — B00's correction ("formulas" → "a plain
  question") is legible; every chip beat reads cleanly (no overlap, no
  contrast issue, safe inset respected); the NB06→NB17 anchor pair uses the
  same three-chip composition and label order so the payoff is visually
  recognizable as the same object returning; BHTF/BOUT carry the
  @HumanitariansAI handle and Liam sign-off correctly. No blockers.
- B00 TIMING LAW: `actual_duration_s` 9.83s (≥8s requirement met); the
  "formulas" → "a plain question" correction lands on screen.

**Non-blocking warning (compile.py):** motion histogram graphic:21
remotion:4 — graphic at 84%, over the ~40% pantry cap in MOTION.md. This is
structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as REMOTION
against a 21-beat GRAPHIC body carried over from the source's 5-act
argument — the ratio follows beat count, not a choice made in this build.
Logged per the honesty rule rather than reworking beat count to dodge the
warning.

Metadata file written: `books--claude-liam-data.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per playlists.json, neither SUBJECT.json's family ("books")
nor the "books--" slug prefix has a literal map entry, and the skill-name
fallback ("hai-simple" → "Claude Basics") would misfile this — the two
immediately-preceding sibling redos from this same source book
(`books--claude-liam-building-plugins`, `books--claude-liam-combining-plugins`,
both Ch.12/13 of the same claude-cowork-plugins book) already established
and logged this exact reasoning, content-matching to "Extending Claude —
Skills, Plugins & Connectors" instead of falling through to `_default` or
the skill-name match. Followed that precedent for consistency across the
family. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
