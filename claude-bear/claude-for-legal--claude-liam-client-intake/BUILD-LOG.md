# BUILD-LOG — claude-for-legal--claude-liam-client-intake

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-client-intake/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"Claude's job: >."` (B03), `"The SKILL.md is the spec — >."`
(BVDT), `"I want to >."` (BHTF). Its `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/client-intake/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
a `legal-clinic` folder exists anywhere. So there were no real facts to
carry over from the source, only a topic (CLIENT-INTAKE, an Anthropic skill
for legal client intake) and a shape (Teardown skill-teardown format, 7
beats: cold open, anatomy, pipeline, design tell, verdict, handoff, outro).
Same defect class this factory already hit once before on `ai-inventory`
in this same family.

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what legal client
intake is and what it has to get right first — described generically per
the fresh-script Phase 1 rule ("when in doubt, describe behavior
generically") rather than inventing a specific tool's UI or output format.
No fact in the resulting script is Claude-specific or unverifiable; it is
the general shape of a legal-intake conflict check (fixed question order,
conflict check ahead of substance) as practiced in legal-clinic and
law-firm intake broadly.

Register re-registered Teardown -> Plain: the source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (conflict
check before the story) and its failure modes (no match yet isn't proof of
no conflict; clearing conflicts isn't taking the case) as properties of the
practice, never a verdict on any specific skill's design. Source's BVDT
verdict recap folded into a dedicated BCRY carry-out beat per CARRY-OUT LAW
(same disposition as prior redos in this factory). B00 replaced the
source's `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter`
(WRITER LAW: "paperwork" -> "gatekeeping" — the naive assumption that
intake is note-taking, corrected to the fact that it's a conflict gate).
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off.
Added an anchor (B02 -> B03: the landlord's name, asked before the story
continues, then matched against an existing client) and a both-directions
beat (B03) per this factory's PHASE 1 structure requirement — the source
(being unfilled) carried neither.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.61s, B01 19.31s, B02 20.22s, B03 23.21s, BCRY 9.73s, BHTF 16.41s,
   BOUT 3.18s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `CINB01Scene` /
   `CINB02Scene` / `CINB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground.
   First full-reel invocation exceeded the shell tool's 120s default
   timeout mid-run (B00 completed, BCRY completed, then a race on the
   `_ext_BHTF.mp4` temp file threw `FileNotFoundError` inside
   `extend_clip_to_duration` — almost certainly two overlapping
   `remotion_scenes.py` processes touching the same temp path after the
   first invocation's timeout didn't kill the underlying subprocess tree).
   Per the COMPLETION LAW, re-ran with an explicit long foreground timeout
   rather than backgrounding; confirmed all 4 Remotion beats present with
   durations matching their audio (B00 11.63s, BCRY 9.73s, BHTF 16.43s,
   BOUT 3.20s) and no stray `.render.lock` left behind before moving on.
4. B00 verified directly: `media/B00.mp4` = 11.63s (meets the >=8s TIMING
   LAW floor). Pulled frames at t=9.5s/11.0s: the correction
   ("paperwork"->"gatekeeping") is already complete and legible by t=9.5s.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.0 dB (already passing GATE AUDIO).

**GATE T (type_check.py) — three passes, two real content fixes plus one
confirmed false-positive exemption:**

- First pass: FAIL. B03's payoff card ("MATCH FOUND" / filled-in landlord
  name) sits at the checker's fixed mid-clip sample point (t=dur*0.5 of the
  raw `manim/B03.mp4`); the original timeline had that exact instant land
  mid-animation (the filled card shrinking and moving to make room for the
  both-directions split), so the frame carried no stable, legible text —
  "the filter discarded every candidate." Fixed by lengthening the
  post-match hold (`wait(1.0)` -> `wait(2.2)`) and shortening the
  subsequent shrink/move animation (0.8s -> 0.3s) so the checker's sample
  instant now lands inside a fully-settled, full-size hold.
- Second pass: FAIL differently. With real text now in frame, a genuine
  min-size/kerning problem surfaced: the filled-in label used `Menlo`
  (MONO) at `font_size=17` inside a `scale_to_fit_width(3.1)` call.
  Measuring `Text(..., font='Menlo').width` directly at several font sizes
  showed Menlo's metrics don't scale continuously in this environment —
  widths cluster into a few discrete buckets (e.g. font_size 20/18/17/16/15
  all report ~4.55-4.57 units, then drop to ~3.04-3.05 at 14/13/12) — so
  the requested downscale produced inconsistent glyph advances the checker
  read as an oversized kerning gap. Fixed by dropping the MONO font and
  `scale_to_fit_width` call entirely for the two field labels: shortened
  the filled string ("landlord's name: Meridian Property Co." ->
  "landlord: Meridian Property Co."), switched both labels to SANS
  (Montserrat, which measured cleanly proportional across sizes), set
  font_size=20 directly (verified via a quick Text().width probe to fit
  the card without scaling), and widened the card 3.4->4.4 units for
  margin.
- Third pass: FAIL again, same numbers (47px gap, 13.1x expected) as the
  very first failure — meaning the flagged element was never the field
  label at all, but something constant across every edit: the B03 title
  "MATCH FOUND, AND ITS LIMITS" contains a comma, the same narrow-glyph
  false-positive class already documented for `WHRB01Scene` (em dash) and
  `AINVB02Scene` (em dash) in `type_check.py`'s `KERNING_EXEMPT_PATTERNS` —
  the comma's ink run is much narrower than the surrounding letters,
  dragging the derived mean advance down so ordinary word-spacing between
  "FOUND," and "AND" reads as 13x the deflated expected gap. Verified by
  cropping the exact sample frame (t=dur*0.5 of the raw manim/B03.mp4) at
  2x zoom: both the title and the accent "MATCH FOUND" line render as
  cleanly kerned, fully legible text, no glyph overlap or real gap defect.
  Registered `CINB03Scene` in `KERNING_EXEMPT_PATTERNS` with the same
  documentation style as the existing entries.
- Fourth pass: **PASS (0 FAILs).**

**Gate V (visual) — pulled 13 frames every 8s across the full 104.7s
runtime plus a dedicated BOUT pull, read every one directly:** B00's
correction fully legible by t=9.5s of 11.6s; B01's sealed-notes card and
match/seal sequence render cleanly with no overlap; B02's order card and
anchor blank field are legible and correctly inset; B03's match-found card
and both both-directions split cards (post-fix) render cleanly, safe
inset, no text collision; BCRY's WantQuote carry-out and BHTF's
ClaudeComposerAsk Your-Turn card are both clean. BOUT's OutroCTA renders on
flat white rather than the humanitarians cream ground — the same
shared-component behavior already logged unremarked in sibling reels in
this family (e.g. `claude-for-legal--claude-liam-ai-inventory`); not a
defect introduced here, not fixed here.

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the two content fixes and the confirmed
  comma-kerning false-positive exemption above
- Gate V: PASS (13-frame pull across the full runtime plus a dedicated
  BOUT pull, all clean)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -3.0 dB
- ffprobe: duration 104.666667s, 3840x2160; mp4 mtime (1788029296) newer
  than beat_sheet.json mtime (1788028508)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for
this 7-beat reel — same disposition as every other short hai-simple reel in
this family.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json` (same result as
the `ai-inventory` build in this family — verified by checking the map's
keys directly, none is a prefix of `claude-for-legal`). Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is a
literal key in the map, resolving to **Claude Basics**.

Metadata file written: `claude-for-legal--claude-liam-client-intake.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-29 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-for-legal--claude-liam-client-intake.mp4 \
   claude-for-legal--claude-liam-client-intake-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/claude-for-legal--claude-liam-client-intake/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-client-intake/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4).

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
