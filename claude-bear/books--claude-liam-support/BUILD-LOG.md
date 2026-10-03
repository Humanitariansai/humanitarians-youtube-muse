# BUILD-LOG — books--claude-liam-support

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/books/claude-cowork-plugins/youtube/claude-liam-support/beat_sheet.json`
(Ch.10 "Support", Teardown/deep-explainer source, already fully built, no
SCRIPT.md — source `beats[*].narration_text` served as the locked script).
Built entirely fresh this invocation — only SUBJECT.json existed on
pickup. Question, facts, and full four-act body argument carried over
unchanged: if you have customers you have support and it arrives anytime
(reactive burden vs. an ordered process; five voices become one); the
four jobs — triage into now/later/known, draft from tone+knowledge
base+request, flag at-risk sentiment, build a knowledge base from your
own inbox and past answers; the setup step (tone, escalation triggers);
the morning-triage-to-thirty-minutes payoff; the angry three-failed-
payments two-year customer as the anchor; the "draft, don't autosend"
rule and "patterns are feedback" idea from the source's Act IV. B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "answer" → "draft" — the
newcomer's wrong guess that the plugin answers customers fully on its
own, corrected toward the actual mechanism). Register re-registered
Teardown→Plain: the source's V01 bulleted verdict recap and its
"reactive burden"/"draft, don't autosend" framing were re-expressed as a
single CARRY-OUT sentence and a genuine BOTH-DIRECTIONS pair rather than
kept as separate rule beats. Close re-skinned to `WantQuote` /
`ClaudeComposerAsk` / `OutroCTA` with @HumanitariansAI and Liam's
sign-off.

Source's 31-beat deep-explainer chassis (4 act-title cards C01–C04 + 20
numbered body beats B01–B20 + V01 verdict recap + H01 your-turn + O01
outro + a duplicate blank-narration BVDT/BHTF/BOUT bookend tail — same
"duplicate close" pattern already logged on several `books--claude-liam-*`
siblings) was compressed to this skill's spine: the 4 act cards dropped
(their titles now land as narration transitions); B20 (already a
spark/summary line — "the plugin drafts, you decide what sends" — not a
distinct fact) folded into the carry-out instead of being kept as a
separate beat; 4 beat-pairs merged where they carried one continuous idea
(B08+B09→NB10, B11+B12→NB12, B13+B14→NB13, B15+B16→NB14); the source's
"draft, don't autosend" (B17/B18) and "patterns are feedback" (B19) rules
were re-expressed as the BOTH-DIRECTIONS pair NB15/NB16 (review-before-
send holds for a live reply, flips for a published FAQ entry that then
serves unsupervised) rather than kept as three separate rule-listing
beats; and the source's own body-close (V01/H01/O01) was kept as the
reel's one close (BCRY/BHTF/BOUT), dropping the duplicate blank-narration
bookend triad — landing at 16 GRAPHIC body beats + B00 (BrutalistHesitant
Writer) + BCRY/BHTF/BOUT = 20 beats total. Full audit in SCRIPT.md's
"Beat-count note (redo)" section. No source beat was ai-video-prompt,
pantry, or a human-drop slot — the source's final build was already
entirely REMOTION (ChipGrid/SegmentCard/SourceFlow/FormACard patterns)
and MANIM (four "doodle" stills carrying a leftover `pantry_note` in
planning metadata but actually built as rendered Manim scenes, not
photos) — NO-GENAI/NO-PANTRY LAW required no substitution beyond B00.

All 16 GRAPHIC beats built on one shared generic "chip row" Manim
template (`scenes.py`/`render_scenes.py`, one title + up to 4 labeled
chips + optional arrows/accent/strike + caption, parametrized per beat
from a `BEAT_CONTENT` table) — same pattern as the `books--claude-liam-
installing-plugins` sibling. THE ANCHOR is NB05 (the angry, three-failed-
payments customer, planted as the case that breaks the "fully automatic"
wrong guess) → NB13 (the same customer, the reply actually drafted,
personalized, and sent). B00 hesitant-writer correction ("answer" →
"draft") verified on screen: "answer" visibly typed in terracotta by
t≈2.5s and corrected to "draft" by t≈4s, full clip 9.97s (≥8s TIMING LAW
window met, no `lead_silence_s` padding needed — Kokoro's own narration
length already cleared it).

Audio generated fresh (`generate_audio_kokoro.py`, all 20 beats, free/
local, `am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`;
all 16 GRAPHIC beats rendered via `render_scenes.py`. First `type_check.py`
pass was FAIL (1 defect) — fixed at the root:

- **bbox-overlap §8.6b, NB07** — the bold EB Garamond title "SORT THE
  WALL" was flagged as two overlapping text-run blobs at the "E WALL"
  boundary. Verified by direct frame crop/zoom at the checker's own
  sample point: the title is correctly kerned, no glyphs touch — the
  same glyph-level false-positive class `KERNING_EXEMPT_PATTERNS` exists
  for elsewhere in `type_check.py`, just tripping the bbox-overlap check
  here instead. Registered `BDNB07Scene` in `BBOX_OVERLAP_EXEMPT_PATTERNS`
  with a comment recording the verification — the toolkit's own
  sanctioned exemption mechanism for a confirmed structural non-bug, not
  a validator loosening.

`type_check.py` went 1→**PASS, 0 FAILs**. Separately, Gate V's own frame
pull caught a second, *real* legibility defect that GATE T's pixel
heuristics had not flagged: NB13's chip label "ADD THE HUMAN LINE"
rendered with the space between "THE" and "HUMAN" collapsing under bold
EB Garamond at that chip width, reading as "ADD THETHEHUMAN LINE" /
"THEHUMAN" — a real word-fusion, not a false positive. Fixed at the root
by rewording the chip label to "ADD A HUMAN LINE" (same meaning, no
"THE"+word adjacency), re-rendered NB13 only, recompiled, reconfirmed
clean by direct frame crop and reconfirmed GATE T still PASS. `beat_sheet.
json`'s `graphic.production_viz.chips` for NB13 was synced to the fixed
wording before the recompile, per COMPLETION LAW (sheet edits happen
before compiling, never after — this fix landed before the final
compile, and the sheet was not touched again afterward). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `books--claude-liam-support.mp4`, 20/20 beats filled real (no
slate), 219.4s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (20 beats, no violations)
- frame-check: PASS (3840×2160, 20 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see defect + exemption above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 219.44s; mp4
  mtime newer than beat_sheet.json mtime
- Gate V (visual): pulled frames at 12s spacing across the full runtime
  plus targeted checks of B00 (correction visible by t≈4s), NB07 (title
  kerning verified clean by direct crop), NB13 pre/post fix, and BHTF/BOUT
  (correct @HumanitariansAI handle, correct title/subline, HAI outro
  skin). No blockers: legible everywhere, safe inset respected, no
  remaining text overlap or word-fusion, em dashes and arrows render
  correctly.
- B00 TIMING LAW: `actual_duration_s` 9.97s (≥8s requirement comfortably
  met); the "answer" → "draft" correction lands on screen by t≈4s.

**Non-blocking warning (compile.py):** motion histogram graphic:16
remotion:4 — graphic at 80%, over the ~40% pantry cap in MOTION.md. This
is structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as
REMOTION against a 16-beat GRAPHIC body carried over from the source's
four-act argument — the ratio follows beat count, not a choice made in
this build. Same disposition as every sibling in HAILOOP-LOG.md. Logged
per the honesty rule rather than reworking beat count to dodge the
warning.

**Cosmetic note carried from sibling precedent:** `OutroCTA` renders on
its own hardcoded off-white ground, not the humanitarians cream — no
color props exist on the component. Same known seam already logged on
multiple `books--claude-liam-*` siblings; not fixed here for the same
reason (no prop to fix it with).

Metadata file written: `books--claude-liam-support.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per playlists.json, neither SUBJECT.json's family ("books")
nor the "books--" slug prefix has a literal map entry, and the skill-name
fallback ("hai-simple" → "Claude Basics") would misfile this — multiple
sibling redos from this same source book (`books--claude-liam-building-
plugins`, `-installing-plugins`, `-data`, and others) already established
and logged this exact reasoning, content-matching to "Extending Claude —
Skills, Plugins & Connectors" instead of falling through to `_default` or
the skill-name match. Followed that precedent for consistency across the
family. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
