# BUILD-LOG — books--claude-liam-installing-plugins

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/books/claude-cowork-plugins/youtube/claude-liam-installing-plugins/beat_sheet.json`
(Ch.2 "Installing and Customizing Plugins", Teardown/deep-explainer source,
already fully built, no SCRIPT.md — source `beats[*].narration_text` served
as the locked script). Question, facts, and full five-act body argument
carried over unchanged (browsing/installing is trivial; customization is a
plain-language conversation, not a settings panel; the ask/answer/calibrate
loop; the anchor — a web design studio whose marketing plugin learns its
professional-services clients, paid off with the tuned output diverging
from generic; self-contained vs. connected plugins, and the CRM/live-database
reach that connecting buys; disable-preserves, ongoing updates, the
two-or-three-active habit, and the local-to-your-machine boundary). B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "install" → "customize" — the
newcomer's wrong guess that clicking install already gives you a tailored
tool). Register re-registered Teardown→Plain: the source's narration was
already close to descriptive/mechanical throughout, so the only real
register work was replacing the closing `ClaudeVerdictArtifact` bullet
recap with a single CARRY-OUT LAW sentence (BCRY, `WantQuote`). Close
re-skinned to `WantQuote` / `ClaudeComposerAsk` / `OutroCTA` with
@HumanitariansAI and Liam's sign-off.

Source's 34-beat deep-explainer chassis (5 act-title cards C01–C05 + 23
numbered body beats B01–B23 + V01 verdict recap + H01 your-turn + O01 outro
+ a duplicate blank-narration BVDT/BHTF/BOUT bookend tail) was compressed to
this skill's spine: the 5 act cards dropped (their titles now land as
narration transitions); B23 (already a spark/summary line duplicating the
reel's own carry-out) folded directly into BCRY instead of being kept as a
separate beat that would say the same thing twice; 3 beat-pairs merged where
they carried one continuous idea (B02+B03→NB02, B10+B11→NB09,
B15+B16→NB13); and the source's own body-close (V01/H01/O01) was kept as the
reel's one close (BCRY/BHTF/BOUT), dropping the duplicate blank-narration
bookend triad rather than rendering two closes back to back — landing at 19
GRAPHIC body beats + B00 + BCRY/BHTF/BOUT = 23 beats total. Full audit in
SCRIPT.md's "Beat-count note (redo)" section. No source beat was
ai-video-prompt, pantry, or a human-drop slot — the source's final build was
already entirely REMOTION (ChipGrid/SegmentCard/SourceFlow/FormACard
patterns, no vox stills actually used despite an earlier PLAN.md lane
allocation) — NO-GENAI/NO-PANTRY LAW required no substitution beyond B00.

All 19 GRAPHIC beats built on one shared generic "chip row" Manim template
(`scenes.py`/`render_scenes.py`, one title + up to 4 labeled chips +
optional arrows/accent/strike + caption, parametrized per beat from a
`BEAT_CONTENT` table) — same pattern as the `books--claude-liam-data`
sibling redo. B00 hesitant-writer correction ("install" → "customize")
verified on screen: "install" visibly typed in terracotta and struck by
t≈2.5s, replaced with "customize" by t≈3.8s, full clip 8.4s (≥8s TIMING LAW
window met with `lead_silence_s: 0.8`).

Audio generated fresh (`generate_audio_kokoro.py`, all 23 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`; all 19
GRAPHIC beats rendered via `render_scenes.py`. First `type_check.py` pass was
FAIL (7 defects, later 1) — fixed at the root across three iterations:

- **Kerning §8.4, 7 beats** — chip/title `Text()` calls used `font=SANS`
  (Montserrat); this environment has no calibrated expected-advance table
  for Montserrat, so real inter-glyph spacing at several word/letter
  combinations read as a false-positive Pango-fallback defect. Fixed at the
  root: switched every `Text()` in `scenes.py` (title, chip label) to
  `font='EB Garamond'` — the toolkit's calibrated serif used everywhere
  else. Not a validator change; the fix the checker itself recommends.
- **Min-size §8.1, 6 beats** — several chip labels were too long for their
  box at 4-chip-row width (e.g. "SKILLS · COMMANDS · CONNECTORS" at 30
  chars, "A SECOND MACHINE: STARTS OVER" at 29 chars), forcing the
  auto-shrink scale factor below the 20px floor. Fixed by shortening the
  labels and, where a merged idea needed the words, moving the second half
  into the caption instead of cramming it into one chip (NB02, NB10, NB11,
  NB13, NB18, NB19).
- **Kerning §8.4, NB08 (2 more root causes, same beat)** — (1) the bold
  accented chip "PRO-SERVICES CLIENTS" rendered a visible ~intra-word gap
  between "FIRM" and a trailing "S" (confirmed by direct frame crop, not
  just the pixel heuristic) — an EB Garamond Bold ligature/kerning defect
  specific to that letter pair; fixed by rewording to "PRO SERVICES" (no
  "...MS" ending). (2) After that fix, the checker's peak-ink-row detector
  picked up NB08's own caption, whose word-count and casing produced enough
  inter-word gaps to itself read as a false positive; shortened and
  lowercased the caption. (3) With the caption lightened, peak-row shifted
  to the 3-chip arrow row itself — EB Garamond's open-bowl letters at this
  font size fragment into short sub-glyph ink runs in the narrow scan band,
  driving the measured "expected gap" far below normal word-spacing. This
  is the exact documented false-positive class `KERNING_EXEMPT_PATTERNS`
  exists for (a dozen prior scenes across other reels are already listed
  there for the identical reason); registered `BDNB08Scene` in that list in
  `runtime/scripts/type_check.py` with a comment, after confirming by direct
  frame inspection that "WEB DESIGN STUDIO" / "PRO SERVICES" /
  "NO MARKETING TEAM" are correctly kerned. This is the toolkit's own
  sanctioned exemption mechanism for a confirmed structural non-bug, not a
  threshold/logic change to the validator.

`type_check.py` went from 8→1→**PASS, 0 FAILs**. `beat_sheet.json`'s
`graphic.production_viz` metadata (chips/caption/label) was synced to match
the final `scenes.py` content before the last compile, per COMPLETION LAW
(no post-compile sheet edits — this sync happened before, not after, the
final `compile.py` run). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `books--claude-liam-installing-plugins.mp4`, 23/23 beats filled real
(no slate), 264.46s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (23 beats, no violations)
- frame-check: PASS (3840×2160, 23 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see defect fixes above)
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 264.46s; mp4
  mtime (14:57) newer than beat_sheet.json mtime (14:54)
- Gate V (visual): pulled 22 frames at 12s spacing across the full runtime,
  plus targeted checks of B00 (correction visible), NB08/NB09 (arrow
  rendering confirmed clean at full resolution — a compressed preview had
  made one arrowhead look like a dash; the actual frame is correct), and
  BOUT (its ~5s window fell between two 12s samples, checked directly from
  media/BOUT.mp4). No blockers: legible everywhere, safe inset respected,
  no text overlap, em dashes and arrows render correctly, @HumanitariansAI
  handle correct on BHTF/BOUT.
- B00 TIMING LAW: `actual_duration_s` 8.4s (≥8s requirement met); the
  "install" → "customize" correction lands on screen by t≈3.8s.

**Non-blocking warning (compile.py):** motion histogram graphic:19
remotion:4 — graphic at 82%, over the ~40% pantry cap in MOTION.md. This is
structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as REMOTION
against a 19-beat GRAPHIC body carried over from the source's five-act
argument — the ratio follows beat count, not a choice made in this build.
Logged per the honesty rule rather than reworking beat count to dodge the
warning.

**Cosmetic note carried from sibling precedent:** `OutroCTA` renders on its
own hardcoded off-white ground, not the humanitarians cream — no color
props exist on the component. Same known seam already logged on the
`books--claude-liam-combining-plugins` sibling; not fixed here for the same
reason (no prop to fix it with).

Metadata file written: `books--claude-liam-installing-plugins.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per playlists.json, neither SUBJECT.json's family ("books")
nor the "books--" slug prefix has a literal map entry, and the skill-name
fallback ("hai-simple" → "Claude Basics") would misfile this — four
immediately-preceding sibling redos from this same source book
(`books--claude-liam-building-plugins`, `-combining-plugins`, `-data`,
`-enterprise-search`, all Ch.7/12/13/Enterprise-Search of the same
claude-cowork-plugins book) already established and logged this exact
reasoning, content-matching to "Extending Claude — Skills, Plugins &
Connectors" instead of falling through to `_default` or the skill-name
match. Followed that precedent for consistency across the family, and set
it correctly in `beat_sheet.json` from the start (no mechanical-fallback
discrepancy to log this time). Direct code link per DELIVERY CONTRACT
format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
