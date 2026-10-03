# BUILD-LOG — claude-for-legal--claude-liam-board-minutes

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-board-minutes/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"the skill is board-minutes. >."`, `"Claude's job: >."`, `"The
SKILL.md is the spec — >."`, `"I want to >."` Its `source_skill` field
points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/board-minutes/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
a `corporate-legal` folder exists anywhere (identical defect class to the
`claude-for-legal--claude-liam-ai-tool-handoff`, `-ai-inventory`, and
`-dsar-response` siblings already built in this batch). So there were no
real facts to carry over from the source, only a topic (BOARD MINUTES) and
a shape (Teardown skill-teardown format, 7 beats: cold open, anatomy,
pipeline, design tell, verdict, handoff, outro).

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what board
minutes actually are and what a drafting handoff to Claude can and can't
finish by itself — described generically per the fresh-script Phase 1 rule
("when in doubt, describe behavior generically") rather than inventing
specific tool names, UI, or product claims. The one substantive fact this
script leans on — minutes record decisions/actions, not discussion, and
are approved by the board before becoming official — is ordinary
corporate-governance practice, not a Claude-specific or unverifiable claim.

Register re-registered Teardown -> Plain: the source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (a minutes
handoff's three parts: notes, draft, approval) and both failure directions
(silence is not a vote; a corrected draft is not a failure) as properties
of any board-minutes handoff, never a verdict on any specific skill's
design. Source's BVDT verdict recap folded into a dedicated BCRY carry-out
beat per CARRY-OUT LAW (same disposition as prior redos in this factory).
B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "TRANSCRIPT" -> "MINUTES" — the
newcomer assumption that minutes are a full transcript, corrected to the
fact that minutes record decisions, not discussion). Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off.

Added an anchor (B02 -> B03: a minutes draft stamped "DRAFT — PENDING
APPROVAL", returning stamped "APPROVED") and a both-directions beat (B03)
per this factory's PHASE 1 structure requirement — the source (being
unfilled) carried neither.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot.

## Built end to end this invocation

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   9.71s, B01 20.95s, B02 16.53s, B03 23.06s, BCRY 5.55s, BHTF 16.85s,
   BOUT 3.88s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `BMB01Scene` /
   `BMB02Scene` / `BMB03Scene`) and `render_scenes.py`; rendered all three
   in the foreground — clean single pass, no failures.
3. Rendered B00/BCRY/BHTF/BOUT (all Remotion) via `remotion_scenes.py` in
   the foreground. The invocation exceeded the shell tool's 120s inline
   timeout and was moved to background by the harness; rather than end the
   turn assuming it finished, blocked on it explicitly with `TaskOutput`
   (`block=true`) until exit code 0 landed — all 4 beats rendered clean in
   one pass, no stale-file defect this time.
4. B00 verified directly: pulled a frame at t=8.7s — the correction
   ("TRANSCRIPT" -> "MINUTES") is already complete and visible, full
   question legible: "Can Claude turn my notes into a full MINUTES of the
   meet[ing]". `ffprobe` confirms `media/B00.mp4` = 9.733s, clearing the
   >=8s TIMING LAW floor.
5. `compile.py --review` -> 7/7 real (no slate), review-cut master
   `claude-for-legal--claude-liam-board-minutes-slate.mp4`, 97.5s,
   mean_volume -23.8 dB (already passing GATE AUDIO).

## Gates

- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **9.71s** (rendered 9.733s), clears the
  >=8s floor. Correction visible on-screen by t=8.7s (confirmed via
  direct frame read).
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840×2160).
- **GATE T (type_check.py):** PASS — 0 FAILs, no findings to root-cause.
- **Gate V (frame QC):** pulled the auto-generated `qc-sheet.png` contact
  sheet plus 12 individual frames at 8s intervals across the full 97.5s
  runtime and read every one directly. All legible, safe inset respected,
  no text overlap, no defects found. Anchor pair (B02 draft-stamp -> B03
  approved-stamp) confirmed visually identical placement/composition
  before the payoff diverges it. `folderLabel` on BHTF's `ClaudeComposerAsk`
  correctly reads `@HumanitariansAI` (explicit prop set).
- **GATE AUDIO:** PASS, mean_volume **-23.8 dB** (ffmpeg volumedetect,
  well above the -40 dB floor), max -2.9 dB.
- ffprobe: master duration 97.538s; mp4 mtime (1788013423) newer than
  beat_sheet.json mtime (1788013391).

**Non-blocking note (compile.py motion histogram):** remotion:4 graphic:3
— remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

## Playlist resolution

`SUBJECT.json`'s `family: "claude-for-legal"` has no literal entry in
`skills/make/hai-simple/loop/playlists.json`'s map (verified directly
against the map file — no key is a prefix of `claude-for-legal`). Per the
map's documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to the skill name itself: `hai-simple` is a literal
key in the map, resolving to **Claude Basics** — same resolution as the
`ai-tool-handoff` sibling (this reel is a generic board-minutes-drafting
explainer, not specifically about Claude plugins/skills infrastructure).

Metadata file written: `claude-for-legal--claude-liam-board-minutes.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
