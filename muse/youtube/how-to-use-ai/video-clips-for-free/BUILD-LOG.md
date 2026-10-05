# BUILD-LOG.md — "Video clips for free" (How to AI #35)

## Decisions

1. **Skill: show-tell, as assigned.** The film is a visual how-to with a
   decision framework — exactly show-tell's "one drawing per beat, the voice
   explains" lane. No skill switch needed. [record]
2. **Greeting: "Hallo".** The show-tell skill lists Hallo among greetings
   that come out clean from Kokoro am_onyx (no re-voicing needed).
   [judgment]
3. **No hard numbers in the film.** The assignment explicitly required it:
   the free-tier quota churns. Build-time research (2026-10-05) found
   10 clips/month, 1080p, ~8 s per clip — recorded in FACTCHECK.md and
   SOURCES.md only. The narration says "a free monthly allowance" and
   "check vids.new for the current limit"; B08's gauge shows a needle
   moving with no digits. No pricing tiers quoted anywhere (standing
   rule). [judgment, per assignment]
4. **Zero ShowTellCards.** The card test was run for B00 (vids.new as a
   `player` card): the beat's claim is "Vids *grew* an AI clip maker", and
   a window with a clip emerging from it — drawn from the film's own
   cast — says it as clearly as the card. Per the test, all nine body
   beats are drawings. Documented in SHOTLIST.md. [judgment]
5. **The reset-rule hedge.** Two sources disagree on the reset (every 30
   days vs. 12 a.m. PT on the first). The film says only "refills each
   month" (FACTCHECK #5). [judgment]
6. **The jar is the film's cast anchor.** The "free tier" budget jar
   introduced in B02 reappears in B04, B06, B07, B08 — same object, whole
   film (show-tell law 4). [record]
7. **Wave 5 voice bug avoided.** Every beat's `voice` field is the Kokoro
   code `am_onyx` — enforced by a generation-time assertion in
   `make_sheet.py` (the Wave 5 bug wrote a persona name there).
   [judgment]

## Timeline (2026-10-05)

- Read show-tell SKILL.md, the iso kit, and the worked example; studied
  the shipped `ask-for-the-shape-you-want-back` package for How-to-AI
  series conventions.
- Ran grounding web searches on the Google Vids free tier (Veo 3.1,
  April 2026 update, scene extension/parallel generation, reset rules,
  music/avatar extras). Saved to SOURCES.md; claims to FACTCHECK.md.
- Wrote `make_sheet.py` (13 beats, contract assertions) → generated
  `beat_sheet.json`: 13 beats, est. 190.0 s.
- Wrote `scenes.py` (iso_kit paste-in + 9 scene classes).
- QC: `py_compile` clean; static_scene_check 8/9 clean on first run.
- Fixed B01 "shapes never change" (frame-first, play-triangle-second —
  a real membership change after the first play); re-ran: 9/9 clean.
- Scripted verbatim check: every `until()` phrase appears verbatim in
  its beat's narration; manim class names match the beat sheet. All OK.
- Session ended with the two remaining docs
  (`CLAUDE-CODE-RENDER.md`, `README.md`) still missing. No push: GitHub
  writes are policy-blocked in worker sessions — the coordinator pushes.

## 2026-10-05 — docs-completion session

- Read `make_sheet.py`, `beat_sheet.json`, and `scenes.py` end to end;
  verified every doc against the actual beats, scenes, and timings.
- Re-ran `make_sheet.py`: contract assertions pass; regenerated
  `beat_sheet.json` byte-identical (deterministic). 13 beats, est. 190.0 s.
- Re-ran the QC gate: `py_compile` clean on both .py files;
  `static_scene_check.py` clean for all 9 scene classes — 9 clean · 0 warn
  · 0 error on the first pass (the B01 membership-change fix from the
  build session is confirmed in place in `scenes.py`).
- Scripted verbatim check: all 13 `until()` phrases present verbatim in
  their beats' `narration_text`.
- Ran independent live web research on the Google Vids free tier
  (2026-10-05); findings are consistent with FACTCHECK.md: 10 free
  generations/month for personal accounts since April 2, 2026 (Veo 3.1);
  reset monthly; 1080p reported by third-party sources (Google has not
  published official free-tier resolution specs); scene extension and
  parallel generation added June 17, 2026; permanence of the free quota
  unconfirmed by Google. The film's anti-rot hedges (no hard-coded quota,
  "check vids.new") stand.
- Corrected this BUILD-LOG's last timeline bullet (it had prematurely
  claimed all 9 docs were written and 12 files pushed — neither had
  happened); corrected `CLAUDE-CODE-RENDER.md` §0 file list, §1 to the
  `generate_audio_kokoro.py` convention, §2 to the per-class
  `manim_layout_audit.py --curve-strict` invocation, and the "Veo"
  pronunciation note ("VAY-oh").
- Deleted `__pycache__/` (regenerated locally by the QC run; it must never
  be pushed). All 12 files present locally; package ready for the
  coordinator's push.
