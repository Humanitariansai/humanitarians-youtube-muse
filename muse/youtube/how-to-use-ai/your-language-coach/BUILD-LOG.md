# BUILD-LOG.md — Your Language Coach

Dated build steps, including failures. Times in America/New_York.

## 2026-10-05

- 17:20 — Received subagent handoff: build "Your language coach"
  (film #44, how-to-ai lane, Wave 6 "Making things", slug
  `your-language-coach`) as a pre-render package at
  `~/workspace/film-builds/how-to-ai/your-language-coach/`; companion
  to `learn-anything-faster` (reference, don't re-teach); assigned skill
  show-tell; never render, publish, upload, or stage anything.
- 17:25 — Read `skills/make/show-tell/SKILL.md` end to end (drawing
  laws, card test, bookend spine, the GATE A/T/V traps), the
  `show-tell` reference `example-make_sheet.py`, and
  `templates/iso_kit.py`. **Skill decision: show-tell (keep the
  assignment).** The film is a technique explainer — four coach moves
  demonstrated on one demo language — which maps exactly onto
  show-tell's spine. No interface, number set, or single word in any
  body beat passes the card test, so the film uses zero cards (recorded
  in SHOTLIST.md). [judgment]
- 17:30 — Studied the companion package
  `~/workspace/film-builds/how-to-ai/learn-anything-faster/` end to end
  (12-file convention, narration style, FACTCHECK/SOURCES/BUILD-LOG/
  CHECKS-REPORT/PROMPTS/CLAUDE-CODE-RENDER formats, the
  `until()`/`finish()` pacing pattern, midpoint-guard timing). This
  film copies that 12-file package convention exactly, including the
  cast pattern (tutor card → coach bubble) and the "every on-screen
  word is spoken" rule.
- 17:35 — Fact-check research (web): French age takes avoir not être
  ("J'ai douze ans", never "Je suis douze ans" — a classic beginner
  mistake from literal English translation), confirmed across three
  French grammar references. Deliberately quoted NO language counts,
  no fluency timelines, no pricing — the film says "name the language"
  and the viewer's own run is the evidence. Companion film verified
  present in the write repo.
- 17:40 — Key narration decision: the narration speaks NO French.
  Kokoro voices foreign words with English phonemes (per the skill's
  greeting notes), so the one French rule is stated in English ("I
  have twelve years") and the hello pills use only greetings the voice
  says cleanly (hola, bonjour, konnichiwa, salaam — all on the skill's
  clean list). [judgment]
- 17:45 — Wrote ACTS.md (hook + 7-beat show-tell body + closing),
  SHOTLIST.md (with the "why zero cards" card-test note), FACTCHECK.md
  (9-row claim table + judgments + cut/disclosed), SOURCES.md (verbatim
  URLs), PROMPTS.md ("no generation prompts" + the viewer's coach
  prompt).
- 17:50 — Wrote make_sheet.py in the canonical show-tell format
  (`narration_text` / `estimated_duration_s`, `remotion()` bookends,
  `bookend_exempt: ["cold-open", "bvdt"]`, per-beat sparse waivers,
  `voice: "am_onyx"` on EVERY beat — the exact bug that broke two
  Wave 5 films at the audio stage). Assertions: 11 beats, 7 manim,
  class names match beat ids, BHTF reads the prompt in full,
  hesitant-writer trigger verbatim in text, terms ≤ 17 chars, total in
  the 3–6 min band. First run: 11 beats, 7 manim, 224 s (~3m44s) —
  assertions pass.
- 17:55 — Wrote scenes.py: pasted `templates/iso_kit.py` verbatim at
  the top (via cp, not retyping), then 7 scene classes
  (B00_Coach, B01_Patience, B02_Correction, B03_Rule, B04_Roleplay,
  B05_Level, B06_Languages). Cast kept whole film: your kraft bubble,
  the coach's white bubble (terracotta lamp), word pills, the
  terracotta caret + check, the rule card, the café awning + counter,
  hello pills. Midpoint-guard timing: every play lands before
  mid−0.35 s or starts after mid+0.35 s, paced by `until()` on
  verbatim narration phrases (all verified present in
  `narration_text` by script, 0 misses). A timing simulation of every
  play span vs each beat's midpoint caught 4 straddles (B02 tag,
  B03 rule line, B04 order pill, B06 second pill pair); all fixed by
  re-anchoring plays to earlier/later phrases — recorded in
  CHECKS-REPORT.md.
- 18:00 — Design fixes during writing (before any checker ran): B02's
  no-op MoveAlongPath removed; B04's unspoken "bien sur" reply pill
  replaced with a wordless pill + dot (every on-screen word must be
  spoken); B01's try-pills made wordless for the same reason; B03's
  rule card widened to 5.2 so "I have twelve years" fits inside at
  34pt; B05's long reply bubble fades out instead of sliding
  off-screen.
- 18:05 — Gate: `python3 -m py_compile` clean on both files;
  `static_scene_check.py` per class: **7 clean · 0 warn · 0 error.**
  No checker failures; the midpoint simulation fixes above were
  design-time, pre-gate.
- Next: write CHECKS-REPORT.md, CLAUDE-CODE-RENDER.md, README.md; push
  all 12 files via gh-put-file.py; verify each via Contents API;
  return the FRICTIONAL.md entry text in the final report.
