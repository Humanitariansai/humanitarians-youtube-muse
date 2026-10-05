# BUILD-LOG.md — Tame your inbox

## 2026-10-05 — pre-render package build (subagent)

### What I did
1. Read `skills/make/show-tell/SKILL.md` (the assigned skill — no skill
   switch; show-tell is the lane this general-audience explainer belongs
   in) and the finished sibling build `how-to-ai/talk-to-your-tools/`
   (this film's companion — its make_sheet/scenes/FACTCHECK as the house
   pattern). No mirror source exists — built from scratch per the brief.
2. Designed the spine from the brief's pitch (triage, summarize, draft
   replies; AI as your email first-pass; companion to talk-to-your-tools,
   referenced in B00, not re-taught; the safety angle: never auto-send,
   never auto-delete): the naive question ("How do I get Claude to answer
   my emails") corrected into the thesis ("use Claude as my email
   first-pass, safely"), three terms (inbox triage, summary, draft), the
   pile → triage → summary → draft → the two rules (never auto-send,
   never auto-delete). One cast throughout: the open tray, the pile of
   email cards, the sorted stacks, the brief card, the draft card, and —
   for the rules — the SEND pill, the lock, the bin, the archive tray.
   Greeting is "Ciao" (clean per the skill; the companion used "Hallo").
3. Fact-checked into FACTCHECK.md (web search 2026-10-05): Claude's Gmail
   connectors as the email-reading basis for the triage beat (PASS), the
   draft-only rule for autonomous assistants (PASS — theaidownside/Instinct
   case, n8n community, Inc.), the "Ciao" greeting (PASS — skill's clean
   list). Everything else is EXEMPT craft advice. No statistics invented
   anywhere; "a sent email mostly isn't [reversible]" is deliberately
   hedged to avoid overclaiming about undo-send windows.
4. Wrote `make_sheet.py` (asserts: 10 beats, beat-id order, 180–300 s
   total, **valid Kokoro voice code on every beat** — the Wave 5 lesson:
   `assert v in {"am_onyx"}` — manim class per body beat, hesitant-writer
   trigger mechanics, BDEFS term length ≤ 17, BHTF composer contract, BOUT
   outro contract). Ran it: **10 beats, 190.0 s (~3:10)**.
5. Wrote `scenes.py`: iso kit + shared helpers copied verbatim from the
   sibling build + film helpers (`pile_card`, `scan_line`, `stack_card`,
   `thread_stack`, `brief_card`, `draft_card`, `bin_can`,
   `archive_tray`) + 6 scene classes (`B00_ThePile` … `B05_NeverAutoDelete`),
   all `until()`/`finish()` paced. Every `until()` phrase verified verbatim
   against its beat's narration by script (all present); every sheet class
   name matches a class in scenes.py.
6. QC: `py_compile` clean on both files; `static_scene_check.py` run from
   a scratch folder holding ONLY `scenes.py` (Gate A simulation) for all 6
   classes — **0 warnings, 0 errors**; re-ran all 6 with `beat_sheet.json`
   beside the file to confirm the `until()`/`finish()` pacing path
   executes: 0 warnings, 0 errors.
7. Wrote the 10 doc files; pushed all 12 package files to
   `Humanitariansai/humanitarians-youtube-muse` under
   `muse/youtube/how-to-use-ai/tame-your-inbox/`; verified each with a
   Contents API read (HTTP 200).

### Failures and fixes
- First `static_scene_check` run on B00_ThePile warned: 12 coords outside
  the safe area — the pile cards started at y=3.4 (off-stage) before
  dropping in. Fixed by starting the drop at y=2.7 (inside ±6.2 × ±3.3);
  the drop motion still reads. Re-ran: 0 warnings, 0 errors.
- `manim_layout_audit.py --curve-strict` could not be run here (no Manim /
  pangocairo in this VM). Mitigations: labels hand-placed (≥ 0.3 leader
  gaps via the `tag()` helper, coords inside ±6.2 × ±3.3, type ≥ 32); the
  bin is a grey (BAR2) tapered body, not a near-black field; no curve
  crosses a label; the B05 card's flight path to the archive tray crosses
  no labels. **Must be run on Bear's Mac before the 4K render**
  (see CLAUDE-CODE-RENDER.md).
- No midpoint render-guard verification possible without measured audio;
  event phrases were placed to keep motion off the midpoint (see
  SHOTLIST.md), but the guard pass must be re-done after Kokoro audio is
  measured.

### What I did NOT do
- No audio generated, no MP4 rendered, nothing staged or published.
  Pre-render package only, per the film brief.
- `muse/FRICTIONAL.md` not touched (concurrent-edit policy); the seven-field
  entry is returned in the final report instead.
- `muse/README.md` and `muse/QUEUE.md` not touched (brief forbids it).
