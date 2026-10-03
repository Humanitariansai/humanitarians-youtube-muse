# BUILD LOG — hai-simple/books--claude-liam-legal-finance

Redo of `anthropics/books/claude-cowork-plugins/youtube/claude-liam-legal-finance`
(Teardown register, 37 beats) as `hai-simple` (Plain register, Humanitarians AI skin).
Source folder untouched.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. No verdict recap (source's `V01` dropped); every
  hand-off beat states what each plugin does and what it doesn't, never a design
  judgment on Anthropic's plugin architecture.
- **Cold open:** source's `ClaudeComposerAsk` ask → `BrutalistHesitantWriter`. Writer
  types the newcomer's wrong-guess word "DO" (implying Claude does the legal/financial
  work itself), hesitates, corrects to "screen" → lands the real question: *"Can Claude
  screen your legal and financial work?"* The correction is picked up directly by Act III
  ("Not a Lawyer") and Act V ("Not a CFO").
- **Close:** source's 6-beat close (`V01, H01, O01, BVDT, BHTF, BOUT`) → 4-beat close
  (`BCRY, BHTF, BOUT, BCTA`). `BVDT`/`BHTF`/`BOUT` in the source were BOOKEND-lane beats
  (`BHTF`/`BOUT` narration empty as authored — dead scaffold) — dropped, not compressed.
  `V01`'s verdict-recap content ("Both screen and accelerate; neither one is the lawyer or
  the CFO") is redundant with the body under Plain register — compressed into the single
  CARRY-OUT sentence (BCRY) instead. `H01`'s prompt is carried into BHTF, reworded only to
  the standard hai-simple "read it with me" framing. `O01`'s title narration is preserved,
  split across the new two-part Humanitarians AI outro (`OutroSeries` + `OutroCTA`).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** unchanged. Every mechanism, chip list, and example (green/yellow/red
  flags, hours-to-minutes, burn/runway, best/likely/worst scenario modeling, the four legal
  limits, the four finance limits) is the source's, reworded only for register, not
  substance. Beat-count delta (37 → 35) is entirely inside the close restructuring above;
  the body (B00→B24) is a 1:1 carry of the source's B00–B24 substance.
- **ANCHOR (new, not in source):** the source had no running anchor image. This build adds
  one within the redo's own body — B01 plants two folders ("Contracts", "Finances"),
  closed and unopened; B24 (the source's own closing lever, "keep a folder... consistently
  kept") pays it off with the same two folders, now open and labelled. Same fact as the
  source, staged as a visual anchor pair per ANCHOR LAW.

## NO-GENAI / NO-PANTRY LAW

Source's `pantry_note` fields (Tier-1 illustrative photography briefs on B02, B05, B11,
B12, B14, B20, B24) were never actually filled with pantry stills in the source's own
review cut — it fell back to bespoke Manim "Doodle" scenes (documentary-duotone
approximations). This build keeps that resolution: all 24 body beats + 6 act cards + BCRY
are bespoke Manim in the humanitarians palette (`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`),
never sourced from any pantry/human-drop asset. The two mid-body "ask Claude" beats (B06,
B15) are stylized generic prompt bars (rounded input + send arrow), NOT the literal
`ClaudeComposerAsk` component — per hai-simple's COLD OPEN LAW override, the Claude UI
does not appear mid-body, only at the Your Turn handoff (BHTF). No beat in this reel is
AI-VIDEO, pantry, or a human-drop slot.

## Two defects found and fixed during Gate V (frame QC)

1. **Wrong channel handle on BHTF.** `ClaudeComposerAsk`'s Root.tsx `<Composition>`
   `defaultProps` hardcodes `folderLabel: '@NikBearBrown'` (same defect as the
   `combining-plugins` sibling); the beat sheet didn't set the prop, so the rendered frame
   showed `@NikBearBrown` on a Humanitarians AI video. Fixed by adding an explicit
   `"folderLabel": "@HumanitariansAI"` to BHTF's props and re-rendering. Verified in a
   full-resolution frame grab post-fix.
2. **Overlapping bottom captions on B12 and B21.** Both scenes placed an italic `note`
   Text AND the shared `_spark()` caption at the identical `to_edge(DOWN, buff=0.5)`
   position, so the two strings rendered on top of each other (confirmed via full-res
   frame grabs — garbled overlapping serif text). Fixed by dropping the redundant `note`
   in both scenes (the spark line alone carries the point; the narration already states
   the fuller idea), re-rendered, reverified clean.
3. **B11 carried no on-screen text at all.** The magnifier/clause scene had no spark line
   authored — a real SPARK-LINE LAW gap (and the direct cause of a GATE T "no text-run
   blobs" fail, see below). Fixed by adding "The screen catches." as the beat's spark.

## GATE T — root-caused to 7 confirmed false positives, 0 real defects remaining

First pass: 12 pixel-beat FAILs (plus the B11 gap above, folded into the count). Diagnosed
by calling `type_check.py`'s own `extract_frame` / `visible_text_mask` / `labeled_blobs` /
`text_run_bboxes` functions directly against the flagged frames (same method the
`building-plugins` and `data` siblings used), rather than guessing from the summary line.

**Root causes found and fixed (6 beats moved from FAIL to PASS):**

- **C01/C06 (`_act_card` shared helper, min-size):** the checker samples the *middle* of
  each raw beat clip. At the original animation timing, the italic subline's `FadeIn` was
  only 58% complete at that exact midpoint — nearly the whole subline was too faint to
  detect, except (for C01/C06 specifically) a solid terminal period surviving as an
  isolated ~8–11px blob. Root cause is timing, not size: fixed by compressing the
  `_act_card` animation sequence (eyebrow/heading/rule/subline all complete by t≈1.8s
  instead of t≈2.5s) so the subline is fully opaque well before the sample point — a
  single shared-helper fix that benefits all six act cards at once.
- **B06 (min-size):** confirmed via pixel crop — the flagged 18px blob was the dot of the
  "i" in "this" (prompt-bar text), detached from its stem by the font's anti-aliasing at
  that size. Fixed by bumping `_prompt_bar`'s default font size 24→28, which also lifted
  the dot fragment's own pixel height above the floor. Reused by B15.
- **B07/B08/B10/B13 (min-size):** same isolated-fragment class (a "t" crossbar or "i" dot
  a few px below the 20px floor) confirmed via pixel crop showing the full word perfectly
  legible in every case. Fixed by bumping the affected chip/caption font sizes 3–6pt
  (`_flag_chip` 24→28, B07 tally captions 22→30, B10 chips 26→30, B13's `routine`/
  `high-stakes`/`highstakes`-chip labels 20–26→26–30), which pushed every fragment's own
  height past the floor without changing the compositions' legibility.
- **B23 (min-size, empty-run fallback):** the y-axis label "cost to fix" was rendered
  rotated 90° (`.rotate(PI/2)`); the rotation transform introduces enough anti-aliasing
  seam that ndimage connected-component labeling fragmented the word into several ~8–9px
  slivers — none of which recombined into a real text run. Fixed by dropping the rotation
  entirely (the label now sits horizontally above the y-axis, still fully legible) — a
  genuine authoring fix, not a size bump.
- **BCRY (contrast §8.3):** the carry-out's second line was set in CRIMSON on cream,
  measuring 2.74:1 — a real WCAG contrast deficiency for body-sized text (visually still
  readable, but a legitimate accessibility gap, not a false positive). Fixed by setting
  both lines of the carry-out to INK/BOLD, matching CARRY-OUT LAW's plain "one idea, one
  frame" treatment rather than relying on the accent color for a full sentence.

**7 confirmed false positives, left as-is (verified by direct pixel inspection at the
checker's own exact sample coordinates — every case shows a fully legible, correctly
composed frame with no visual defect):**

- **C06 (min-size, 11px):** an isolated dot-of-"i" in the heading word "Routine" (large,
  BOLD, 60pt title text — "Make It Routine" reads perfectly clean in the full frame).
  Identical class to the fixed cases above, but here the fragment sits inside the fixed
  act-card *title* itself, which can't be reworded without changing the act's name, and a
  further font-size increase to the whole title family would distort house style for a
  sub-pixel dot. Confirmed cosmetic-only via full-resolution crop.
- **B02 (kerning) / B07 (kerning, second pass) / B06/B08/B13 (bbox-overlap, second pass):**
  after the min-size fixes above (larger fonts), the checker's fragment/kerning/overlap
  heuristics re-triggered on different sub-glyph fragments (an ellipsis "…" in B06's prompt
  text, a crossbar in B08/B13's chip labels) at the new sizes. Each was checked against a
  full frame grab (`Review this agreement and flag any issues…`, `Contract review / NDA
  triage / Vendor terms / Compliance checks`, `A contract → Screen it / Escalate to a
  lawyer`) — all render as complete, non-overlapping, correctly kerned prose. Chasing
  these further moves the failure to a different fragment rather than resolving it (the
  same fragment-detection class the tool's own code already documents exemption lists for
  in `KERNING_EXEMPT_PATTERNS`/`BBOX_OVERLAP_EXEMPT_PATTERNS` for other scenes); diminishing
  returns reached without a matching exemption mechanism for `min-size`, so left logged
  rather than chased into a fourth iteration.
- **B17 (contrast §8.3):** the only CRIMSON element in this scene is a solid data-fill
  rectangle (the draining cash bar), not text — the same "data fill, not text" false-
  positive class the checker's own code documents elsewhere (e.g. the profit/loss OUTFLOW
  color comment). No CRIMSON `Text` mobject exists in `B17Scene`.

GATE T: 12 FAILs → 7 FAILs, all confirmed false positives per the evidence above; every
finding that pointed at a real, visible defect was fixed at the root and reverified.

## Gates

- **TIMING LAW (B00):** narration 35 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **11.14s**, clears the ≥8s floor.
- **GATE AUDIO:** PASS, mean_volume **-23.8 dB** (well above the -40 dB floor), max -2.7 dB.
- **Gate V (frame QC):** full contact sheet (`qc-sheet.png`) reviewed beat-by-beat twice
  (before and after fixes), plus full-resolution frame grabs of B00, B11, B12, B21, BHTF,
  BOUT, and every GATE T-flagged beat. Three defects found and fixed (above); nothing else
  flagged — no text overflow, no unsafe inset, no overlap remaining after the fixes.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (35/35
  beats, no violations).
- **motion-histogram WARNING (graphic 88%, over the ~40% pantry cap):** expected and
  accepted. NO-GENAI/NO-PANTRY LAW forces every body beat to GRAPHIC or REMOTION; the
  hai-simple spine itself is only 4 REMOTION beats (B00, BHTF, BOUT, BCTA) against 24 body
  + 6 card + 1 carry-out GRAPHIC beats. Same disposition as every prior sibling in this
  book's redo series.

## Output

`books--claude-liam-legal-finance-slate.mp4` — 332.5s, 35/35 beats real (no slates),
audible narration throughout. This is the review cut (COMPLETION LAW satisfied: newer than
`beat_sheet.json`, audible audio verified via ffprobe/compile GATE AUDIO).

**Playlist:** Extending Claude — Skills, Plugins & Connectors. `SUBJECT.json`'s
`family: "books"` and the `books--` slug prefix have no literal entry in
`playlists.json`'s map; falling straight to `_default` would be wrong for a reel that is
squarely about two Claude plugins. Every prior sibling redo of this same source book
(`building-plugins`, `combining-plugins`, `data`, `enterprise-search`,
`installing-plugins`) already established, and logged, the same content-match to
"Extending Claude — Skills, Plugins & Connectors" instead of the skill-name
("hai-simple"→"Claude Basics") fallback or `_default` — followed that precedent here for
consistency across the book's reel family.
