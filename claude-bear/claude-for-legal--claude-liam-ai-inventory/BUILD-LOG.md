# BUILD-LOG — claude-for-legal--claude-liam-ai-inventory

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-ai-inventory/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"the skill is ai-inventory. >."`, `"Claude's job: >."`, `"The
SKILL.md is the spec — >."`, `"I want to >."`. Its `source_skill` field
points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ai-governance-legal/skills/ai-inventory/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
an `ai-governance-legal` folder exists anywhere. So there were no real facts
to carry over from the source, only a topic (AI-INVENTORY, an Anthropic
skill for legal AI governance) and a shape (Teardown skill-teardown format,
7 beats: cold open, anatomy, pipeline, design tell, verdict, handoff,
outro).

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what an
AI-inventory governance practice is and why a legal team needs one before
writing a policy — described generically per the fresh-script Phase 1 rule
("when in doubt, describe behavior generically") rather than inventing
specific tool names, UI, or product claims. No fact in the resulting script
is Claude-specific or unverifiable.

Register re-registered Teardown -> Plain: the source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (an
inventory's four fields) and its failure modes (logged is not safe;
complete is not permanent) as properties of the practice, never a verdict
on any specific skill's design. Source's BVDT verdict recap folded into a
dedicated BCRY carry-out beat per CARRY-OUT LAW (same disposition as prior
redos in this factory). B00 replaced the source's `ClaudeComposerAsk` cold
open with `BrutalistHesitantWriter` (WRITER LAW: "policy" -> "inventory" —
the naive assumption that governance starts with a written rule, corrected
to the fact that governance starts with a list of what's actually running).
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off.
Added an anchor (B02 -> B03: the contract-review tool quietly adopted with
no policy entry, then logged with the same four fields as everything else)
and a both-directions beat (B03) per this factory's PHASE 1 structure
requirement — the source (being unfilled) carried neither.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   9.94s, B01 18.01s, B02 17.39s, B03 20.27s, BCRY 8.70s, BHTF 16.53s,
   BOUT 3.37s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `AINVB01Scene` /
   `AINVB02Scene` / `AINVB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (the process exceeded the shell's 120s inline timeout and was moved to a
   tracked background job mid-run; per the COMPLETION LAW for one-shot
   invocations, polled the job's own output file in a blocking foreground
   loop rather than ending the turn — confirmed exit code 0 before
   proceeding).
4. B00 verified directly: `media/B00.mp4` = 9.97s (meets the >=8s TIMING LAW
   floor). Pulled frames at t=6.5s/9s: the correction ("policy"->"inventory")
   is already complete and visible by t=6.5s, full question legible by t=9s.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -23.8 dB (already passing GATE AUDIO).

**GATE T (type_check.py) — one finding, confirmed false positive, not a
real defect:**

- First pass: FAIL (1 pixel beat). B02's kerning check flagged the SANS
  title "FOUR FIELDS — THE ANCHOR" (max inter-glyph gap 90px vs. threshold
  15px). Same documented false-positive class as the `WHRB01Scene`
  exemption in this file's `KERNING_EXEMPT_PATTERNS`: the em-dash glyph
  renders as a much narrower ink run than the surrounding letters, dragging
  the derived `mean_w` down so ordinary inter-glyph advance elsewhere in
  the title reads as an oversized gap. Pulled the exact frame the checker
  samples (t=dur*0.5 of the raw `manim/B02.mp4`) and read it directly: the
  title renders as one cleanly kerned, fully legible run. Registered
  `AINVB02Scene` in `KERNING_EXEMPT_PATTERNS` with the same documentation
  style as the existing entries.
- Second pass: **PASS (0 FAILs)**.

**Gate V (visual) — first pass found two real defects, both fixed:**

Pulled frames every 5s across the full 95s runtime and read them directly.
Found:
1. **B01**: the three "named tool" chips (`research tool` / `drafting aid`
   / `e-discovery`) had text wider than their 1.4-unit chips — labels
   overflowed and overlapped the neighboring chip's border and text.
2. **B03**: the four filled-in field lines (`what it does: ...`, `data
   touched: ...`, etc.) were wider than the 4.4-unit dim card — text spilled
   past the card's left/right borders.

Root-caused to hardcoded `Text()` widths never checked against their
container. Fixed in `scenes.py`: added a `_fit_text()` helper that scales
any label down to fit its container, widened B01's chips (1.4->1.5 units,
tighter buff) and B03's card (4.4->5.8 units) to reduce how much scaling is
needed, and repositioned B02's "nobody wrote it down anywhere" note below
the (now-centered) dim card instead of beside it, removing a second latent
horizontal-collision risk from the same width change. Re-rendered all three
Manim beats, recompiled, re-ran GATE T (still PASS after the fix — no
regression), and re-pulled frames across the full runtime: all 7 beats now
render legibly with safe inset respected and no text overlap anywhere.
BHTF's `ClaudeComposerAsk` composer card and BOUT's `OutroCTA` outro were
clean on both passes.

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component behavior
already logged unremarked in sibling reels in this family (e.g.
`claude-code--claude-liam-writing-rules`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after registering the confirmed em-dash kerning
  false-positive exemption above
- Gate V: PASS after fixing the two chip/card text-overflow defects above
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 95.217s; mp4 mtime (1788001266) newer than
  beat_sheet.json mtime (1788001224)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for
this 7-beat reel — same disposition as every other short hai-simple reel in
this family.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json` (verified by
running the match algorithm directly — no key is a prefix of
`claude-for-legal`). Per the map's documented fallback ("match SUBJECT.json's
family, or the hai-simple prefix"), fell through to matching the skill name
itself: `hai-simple` is a literal key in the map, resolving to **Claude
Basics**. (First draft of this metadata guessed "AI for Professionals" by
topic-vibe before the algorithm was actually run against the map file —
corrected before delivery, and `beat_sheet.json`/`<slug>.md` both carry the
corrected value. `beat_sheet.json` was recompiled after this one correction
so the master stays newer than the sheet, per the COMPLETION LAW.)

Metadata file written: `claude-for-legal--claude-liam-ai-inventory.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
