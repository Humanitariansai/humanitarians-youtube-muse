# BUILD-LOG.md — Meetings into Notes

## 2026-10-03 — pre-render package build (subagent)

### What I did
1. Read `skills/make/show-tell/SKILL.md`, the iso kit
   (`skills/make/show-tell/templates/iso_kit.py`), and the finished sibling
   build `how-to-ai/how-to-use-claude/` (its make_sheet/scenes/FACTCHECK/
   CLAUDE-CODE-RENDER as the house pattern). No mirror source exists for this
   film — built from scratch per the brief.
2. Chose the **show-tell** skill as assigned: the film is a step-by-step
   visual explainer — one image per beat, minimal text, the voice explains.
   Recorded here per the brief: no skill switch needed.
3. Designed the spine from the brief's core idea (paste the mess → 3-line
   summary + decisions with owners + unresolved) with the three exact prompts
   as beats B03/B04/B05, a fictional end-to-end example (B06: Maya / Sam /
   the release notes), a follow-up beat (B07: keep asking), and the privacy
   line kept to one sentence (B08; film #20 covers privacy in depth). One
   cast throughout: the transcript page → the chat window → the three output
   cards. Zero ShowTellCard beats (every beat fails the card test at
   question 1).
4. Fact-checked into FACTCHECK.md (web search 2026-10-03): auto-transcription
   availability on Zoom/Meet/Teams (PASS, worded as "probably"); everything
   else is EXEMPT craft advice or the fictional example. No statistics
   invented anywhere.
5. Wrote `make_sheet.py` (asserts: 13 beats, beat-id order, 165–210 s total,
   manim class per body beat, hesitant-writer trigger mechanics, BDEFS term
   length ≤ 17, BHTF composer contract, BOUT outro contract). Ran it:
   **13 beats, 187.2 s (~3:07)**.
6. Wrote `scenes.py`: iso kit pasted verbatim + film helpers
   (`chat_window`, `doc_card`, `tag`, `transcript_page`, `scribbles`,
   `bubble`, `fragment_card`, `owner_pill`, `email_card`, `lock`) + 9 scene
   classes (`B00_RamblingMeeting` … `B08_CheckRules`), all `until()`/`finish()`
   paced. Every `until()` phrase verified verbatim against its beat's
   narration by script (18/18 present).
7. QC: `py_compile` clean on both files; `static_scene_check.py` run from a
   scratch folder holding ONLY `scenes.py` (Gate A simulation) for all 9
   classes — **0 warnings, 0 errors**. Re-ran B03 and B06 with
   `beat_sheet.json` beside the file to confirm the `until()`/`finish()`
   pacing path executes: 0 warnings, 0 errors.
8. Wrote the 10 doc files; pushed all 12 package files to
   `Humanitariansai/humanitarians-youtube-muse` under
   `muse/youtube/how-to-use-ai/meetings-into-notes/`; verified each with a
   Contents API read (HTTP 200).

### Failures and fixes
- `make_sheet.py` first draft set the duration band at 180–220 s (copied from
  the sibling); the honest total is 187.2 s, inside it — but the band's floor
  comment said "3:00-3:40" while the brief allows 3–6 min. Kept the assert
  band at 165–210 s with a corrected comment; 187.2 s passes.
- B02's first trigger phrase ("Your own rough notes work too") landed inside
  the clip's 45–55% GATE T sampling window; switched to "already" with
  `lead=0.6` so the fragment drop finishes before the window. Noted in
  SHOTLIST.md timing notes.
- B06's first layout stacked the three output cards with a vertical overlap
  (card bottoms/tops crossed); respaced to y = 1.65 / 0.2 / −1.25 with
  h = 1.3 so gaps are ≥ 0.15.
- `manim_layout_audit.py --curve-strict` could not be run here (no Manim /
  pangocairo in this VM). Mitigations: labels hand-placed (≥ 0.3 leader gaps,
  coords inside ±6.2 × ±3.3, type ≥ 32); the only curve is B08's lock shackle,
  which crosses no label; B00's "tangles" are straight-segment polylines, not
  curves. **Must be run on Bear's Mac before the 4K render**
  (see CLAUDE-CODE-RENDER.md).
- No midpoint render-guard verification possible without measured audio;
  event phrases were placed to keep motion off the midpoint (see SHOTLIST.md),
  but the guard pass must be re-done after Kokoro audio is measured.

### What I did NOT do
- No audio generated, no MP4 rendered, nothing staged or published.
  Pre-render package only, per the film brief.
- `muse/FRICTIONAL.md` not touched (concurrent-edit policy); the seven-field
  entry is returned in the final report instead.
- `muse/README.md` and `muse/QUEUE.md` not touched (brief forbids it).
