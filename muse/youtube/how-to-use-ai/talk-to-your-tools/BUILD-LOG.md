# BUILD-LOG.md — Talk to your tools

## 2026-10-04 — pre-render package build (subagent)

### What I did
1. Read `skills/make/cc-explainer/SKILL.md` (the assigned skill), the
   `show-tell` SKILL.md, and the finished sibling build
   `how-to-ai/meetings-into-notes/` (this film's companion — its
   make_sheet/scenes/FACTCHECK/CLAUDE-CODE-RENDER as the house pattern).
   No mirror source exists for this film — built from scratch per the brief.
2. **Skill switch (recorded per the brief): assigned `cc-explainer`,
   built with `show-tell`.** Reasoning: cc-explainer's TERMINAL-FIRST law
   (body beats default to `CCSession`) and REAL-SESSION law (every block
   traces to a real `SESSION.md`) require a reconstructed Claude Code
   terminal session — this film has none. It is a general-audience
   explainer about connecting AI to email/calendar/apps, the exact lane
   show-tell serves ("minimal text, the voice explains"), and the
   companion film used show-tell. The brief's own audience rules
   (explain every term, show rather than tell) match show-tell's
   description word for word.
3. Designed the spine from the brief's pitch (connect AI to
   email/calendar/apps; first automations; what to watch out for): the
   plug thesis (BIDEA correction: "give Claude my passwords" →
   "connect Claude to my tools safely"), three terms (connector,
   permissions, automation), the gap → the plug → the permissions screen,
   three automations (morning brief, inbox triage, meeting prep — B05 is
   the explicit companion beat to meetings-into-notes), three warnings
   (the send button stays yours; smallest key, pull unused plugs;
   strangers' invites). One cast throughout: the chat window, the plug on
   its kraft cable, the email card, the calendar page.
4. Fact-checked into FACTCHECK.md (web search 2026-10-04): the connector
   model and OAuth-style connect flow (PASS), the permissions screen
   (PASS — exact labels deliberately not quoted, version-sensitive),
   supervised sending (PASS), least privilege (PASS), calendar-invite
   prompt injection (PASS — LayerX/The Register Feb 2026, the "Invitation
   Is All You Need" study). Everything else is EXEMPT craft advice. No
   statistics invented anywhere. Automations are framed as repeat jobs
   you ask for (not scheduled background tasks) so nothing version-specific
   can go stale.
5. Wrote `make_sheet.py` (asserts: 13 beats, beat-id order, 200–300 s
   total, manim class per body beat, hesitant-writer trigger mechanics,
   BDEFS term length ≤ 17, BHTF composer contract, BOUT outro contract).
   Ran it: **13 beats, 243.6 s (~4:03)**.
6. Wrote `scenes.py`: iso kit + shared helpers (chat window, doc cards,
   labels, email card, lock) copied verbatim from the sibling build +
   film helpers (`calendar_card`, `plug_head`, `socket_slot`, `cable`,
   `shield`, `perm_row`, `send_pill`, `tray`, `invite_card`,
   `inbox_card`, `x_stamp`) + 9 scene classes (`B00_TheGap` …
   `B08_StrangerInvite`), all `until()`/`finish()` paced. Every `until()`
   phrase verified verbatim against its beat's narration by script
   (19/19 present).
7. QC: `py_compile` clean on both files; `static_scene_check.py` run from
   a scratch folder holding ONLY `scenes.py` (Gate A simulation) for all 9
   classes — **0 warnings, 0 errors**; re-ran all 9 with `beat_sheet.json`
   beside the file to confirm the `until()`/`finish()` pacing path
   executes: 0 warnings, 0 errors.
8. Wrote the 10 doc files; pushed all 12 package files to
   `Humanitariansai/humanitarians-youtube-muse` under
   `muse/youtube/how-to-use-ai/talk-to-your-tools/`; verified each with a
   Contents API read (HTTP 200).

### Failures and fixes
- The first `scenes.py` assembly script built its split marker wrong and
  asserted before writing; fixed by splitting on the exact marker line
  (line 270 of the sibling file). No film content affected.
- B02's original three-step `show` annotation (rows landing one by one)
  did not match the scene's two-play structure (both read rows land on
  "read your email", keeping the motion out of the 45–55% window); the
  annotation was corrected before the first push.
- `manim_layout_audit.py --curve-strict` could not be run here (no Manim /
  pangocairo in this VM). Mitigations: labels hand-placed (≥ 0.3 leader
  gaps via the `tag()` helper, coords inside ±6.2 × ±3.3, type ≥ 32);
  cables are straight lines edged in deep kraft (`#9C8462`) so they never
  fuse with the dark socket under GATE T; no curve crosses a label; the
  lock shackle (B06) sits over the SEND pill, clear of all labels.
  **Must be run on Bear's Mac before the 4K render**
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
