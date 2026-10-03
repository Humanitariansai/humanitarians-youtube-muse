# BUILD-LOG — claude-for-legal--claude-liam-chronology

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-chronology/beat_sheet.json`.

**Source-fidelity finding (logged, not asked):** unlike sibling redos in this
family (`claude-liam-amendment-history`, `claude-liam-aia-generation`), this
source sheet's narration is genuinely written — no unfilled `>` template
placeholders. It describes the `chronology` Anthropic skill in its own words:
"Build or update a chronology from declared document sources and uploads —
dated events extracted, de-duped, and tagged by significance per the matter
theory." Its `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/chronology/SKILL.md`
— searched the whole `books/` tree on this machine; neither that file nor a
`litigation-legal` folder exists here, so nothing beyond the already-written
source narration/description could be independently re-verified. Carried the
source's two real mechanics forward (declared-source extraction + de-dup;
significance tagging by matter theory) rather than treating this as a gap to
reconstruct from title alone.

Register re-registered Teardown → Plain: the source's B03 framed "Claude's
job" and "what it gets right / where it bites" as a design-tell verdict —
Teardown language. Plain instead states the mechanism (event de-dup across
sources; significance tagged by matter theory, not universally) and its
both-directions properties (a low tag isn't a wrong or missing event; one
entry instead of many doesn't mean fewer sources mentioned it) as properties
of chronology building, never a verdict on the skill's design. Source's BVDT
verdict recap folded into a dedicated BCRY carry-out beat per CARRY-OUT LAW
(same disposition as prior redos in this factory). B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"sort" → "weigh" — the naive assumption that building a chronology means
sorting every date, corrected to weighing which events actually matter).
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Added
an anchor (B02 → B03: a late-payment event named in an email, an invoice, and
a deposition transcript, collapsed to one entry, then tagged high by one
matter's theory and low by another's) and a both-directions beat (B03) per
this factory's PHASE 1 structure requirement — the source (skill-anatomy
framing) carried neither.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.01s, B01 19.54s, B02 17.11s, B03 25.37s, BCRY 8.75s, BHTF 17.19s,
   BOUT 3.03s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `CHRB01Scene` /
   `CHRB02Scene` / `CHRB03Scene`) and `render_scenes.py`; rendered all three
   in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`; the process exceeded
   the shell tool's 120s inline timeout and was moved to a tracked background
   job mid-run. Per the COMPLETION LAW for one-shot invocations, blocked on
   `TaskOutput(task_id, block=true)` in the foreground rather than ending the
   turn — confirmed exit code 0 (all 4 beats ok) before proceeding.
4. B00 verified directly: `media/B00.mp4` = 11.03s (meets the ≥8s TIMING LAW
   floor and clears the ≥9s narration-window target). Pulled a frame at
   t=10s: the correction ("sort" → "weigh") is complete and the full final
   question ("Just weigh every date?") is legible.
5. First `compile.py` pass caught a real pacing defect the tool itself
   flags: B03's Manim clip (6.7s raw) was slowed 3.8x into its 25.4s beat —
   over the 3.0x "extreme slow-mo" warning threshold (logged to
   `replace_log.md`). Fixed by lengthening B03's holds/waits (raw 6.7s →
   9.5s), bringing the ratio to 2.66x, in line with B01/B02 (2.33x–2.43x).
   Recompiled: 7/7 real, no slate, 3840×2160 (THE 4K LAW), mean_volume
   -24.1 dB.

**GATE T (type_check.py) — three real findings across four passes, all
fixed (none were loosened checks):**

- Pass 1: FAIL — B02 min-size (19px < floor 20, the "ONE ENTRY" caption) and
  B03 min-size (18px) + bbox-overlap (a small blob nested inside a larger
  one). Bumped `collapsed_sub`/`collapsed_txt` font sizes and card
  buff/height in both scenes.
- Pass 2: FAIL — B03 bbox-overlap persisted at a different sub-region.
  Direct frame crop/zoom (ffmpeg crop+scale on the exact flagged bbox)
  showed the "small blob" was the natural enclosed counter-hole inside the
  letter "A" in "LATE" — a font-rendering artifact of the glyph itself, not
  two overlapping labels. Root-caused to insufficient card height letting
  the text run touch the card's border stroke, fusing text+border into one
  oversized blob (h=164px, "6.3× med") that made the counter-hole
  detectable. Fixed by growing the card (3.6×1.2 → 3.8×1.7) so text no
  longer touches the border — not by adding a validator exemption, since
  the underlying geometry was the actual fixable cause.
- Pass 3: FAIL — B02 contrast: "terracotta accent on cream 2.74:1" flagged
  against the checker's fixed reference hex, but grep of `scenes.py`
  confirmed **zero** B02 text uses TERRA (only the `collapsed` card's
  border). Frame-pulled the exact raw-clip sample point (t=dur×0.5 of
  `manim/B02.mp4`) and found it lands mid-`ReplacementTransform`, where the
  three source cards were morphing point-by-point into the collapsed card —
  producing scrambled, illegible glyph shapes and a double-exposed border
  ghost. The anti-aliased edge pixels of that transient morph blend toward
  the checker's terracotta reference within its color tolerance. Considered
  registering `CHRB02Scene` in `STRUCTURAL_TERRACOTTA_PATTERNS`
  (`runtime/scripts/type_check.py`) as prior sibling reels do for genuine
  structural-accent false positives, but reverted that edit: this wasn't a
  structural accent, it was a fixable animation defect (a morph that reads
  as garbage mid-transition), so the shared validator was left untouched.
  Fixed at the content level instead — replaced the point-by-point
  `ReplacementTransform(cards, collapsed_full)` with a clean
  `FadeOut(cards)` / `FadeIn(collapsed_full, scale=0.9)` crossfade. Re-pulled
  the same sample point: clean, both card states fully legible, no garbled
  intermediate glyphs.
- Pass 4: **PASS (0 FAILs).**

**Gate V (visual, own 5s-interval scan across the full 103s runtime) — one
additional real defect found that GATE T's single per-beat sample point
didn't catch, fixed:** B03 also used `TransformFromCopy` to split the
collapsed anchor card into its two tagged copies (`BREACH-OF-CONTRACT
MATTER` / `A DIFFERENT MATTER`); GATE T's mid-clip sample happened to land
after that split completed, but the broader 5-second scan caught the same
class of garbled mid-morph glyphs during the split, a few seconds off from
GATE T's sample point. Fixed identically: replaced the two
`TransformFromCopy` calls with a `move_to` (keep the anchor card, no morph)
followed by a clean `FadeIn` of both new tagged cards. Re-rendered, re-pulled
frames at 0.5s resolution across the entire B03 clip (19 frames): clean at
every sampled point, no garbled text anywhere. Recompiled; GATE T re-run:
still PASS. Re-scanned the full master at 5s intervals (21 frames, all seven
beats): B00's writer correction legible, B01's duplicate-date callout clean,
B02/B03's cards and captions all legible with correct humanitarians palette,
BCRY's carry-out quote clean, BHTF's composer card and prompt text clean and
correctly branded (@HumanitariansAI), BOUT's title/subscribe/handle clean.

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component behavior
already logged unremarked in sibling reels in this family (e.g.
`claude-for-legal--claude-liam-amendment-history`,
`claude-code--claude-liam-writing-rules`,
`claude-code--claude-liam-hook-development`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after fixing the three confirmed defects above
- Gate V: PASS — full-runtime 5s scan (21 frames) plus a full 0.5s scan of
  B03 specifically (19 frames), all beats legible, no garbled/overlapping
  text, correct palette and branding throughout
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 103.000s, 3840x2160; mp4 mtime (1788022772) newer than
  beat_sheet.json mtime (1788021506)

**Motion histogram:** remotion:4 graphic:3 — remotion at more than half of
beats. Structural, not a defect: hai-simple's mandated shape is B00
(writer) + BCRY + BHTF (Your Turn) + BOUT (outro) all REMOTION by skill
contract, against 3 GRAPHIC body beats for this 7-beat reel — same
disposition as every other short hai-simple reel in this family.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is a
literal key in the map, resolving to **Claude Basics** — same resolution as
the sibling `claude-for-legal--claude-liam-amendment-history` redo.

Metadata file written:
`claude-for-legal--claude-liam-chronology.md` (channel @HumanitariansAI,
Playlist: **Claude Basics**, plus the direct code link per the DELIVERY
CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## Phase 4 — delivery, DONE

`compile.py`'s own 4K LAW already produced a native 3840x2160 master (no
separate upscale needed), so `claude-for-legal--claude-liam-chronology.mp4`
was copied to `claude-for-legal--claude-liam-chronology-4k.mp4` and packaged
via:

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged to `DELIVERY/claude-for-legal--claude-liam-chronology/` (4K master +
description) and committed the text artifacts (README.md = description,
beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md,
QUESTION.md — no mp3/mp4) to `humanitarians-youtube/claude-bear/` at commit
`132c9727`, then pushed. **Reel fully DONE end to end this invocation.**
