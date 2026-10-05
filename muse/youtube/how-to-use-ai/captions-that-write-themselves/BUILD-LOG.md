# BUILD-LOG.md — Captions That Write Themselves

Dated build steps, including failures. Times in America/New_York.

## 2026-10-05

- 17:20 — Received subagent handoff: build "Captions that write
  themselves" (film #40, how-to-ai lane, Wave 6 "Making things", slug
  `captions-that-write-themselves`) as a pre-render package; pitch:
  AI-generated subtitles/captions for a normal person's phone-shot
  video, accessibility and reach; assigned skill show-tell; never
  render or publish. Film identity constants: Liam persona, Kokoro
  `am_onyx`, Teardown register, channel claude-liam, watermark
  @NikBearBrown.
- 17:25 — Read `skills/make/show-tell/SKILL.md` end to end (drawing
  laws, card test, bookend spine, the GATE A/T/V traps) and the worked
  sibling package `~/workspace/film-builds/how-to-ai/learn-anything-faster/`
  (12-file convention, narration style, FACTCHECK table, the seven-field
  FRICTIONAL format). **Skill decision: show-tell (keep the
  assignment).** The film is a practical walkthrough — steps
  demonstrated on a phone-shot video — which maps exactly onto
  show-tell's spine (hesitant writer → key terms → drawn body beats →
  Your Turn composer → spoken outro). The card test fails every body
  beat — the B07 numbers are one attributed figure carried better by
  bars and a hero number — so the film uses zero cards. [judgment]
- 17:35 — Fact-check research (web, 2026-10-05): Verizon Media /
  Publicis Media 2019 US survey — 92% view videos with the sound off
  on mobile, 83% watch with sound off, 69% without sound in public
  places (Next TV, PLOS ONE citation); WHO — 430 million with
  disabling hearing loss, 1.5 billion with some hearing loss
  (who.int); auto-caption workflows verified against CapCut's official
  docs and two 2026 guides (auto captions miss proper nouns,
  technical terms, fast speech — exactly the film's step-three check);
  export = burned-in or separate .srt; YouTube auto-captions every
  upload. Both quoted numbers are attributed aloud AND captioned on
  screen (thin-numbers law, SKILL.md law 8).
- 17:45 — Chose the structure: four steps (open a captioning tool /
  press the button / check names and odd words / burned-in or a
  caption file), tool-agnostic on purpose so the film cannot date, and
  a "for short feeds, burn them in; for YouTube, keep the file"
  decision framework instead of pricing tiers (standing preference).
  [judgment] Wrote ACTS.md, SHOTLIST.md (with the "why zero cards"
  card-test note), FACTCHECK.md (11-row claim table + judgments +
  cut/disclosed), SOURCES.md (verbatim URLs), PROMPTS.md ("no
  generation prompts" + the viewer's caption-check prompt).
- 18:00 — Wrote make_sheet.py in the canonical show-tell format
  (`narration_text` / `estimated_duration_s`, `remotion()` bookends,
  `bookend_exempt: ["cold-open", "bvdt"]`, per-beat sparse waivers,
  `"voice": "am_onyx"` on every beat — the Wave 5 voice-code lesson is
  asserted in the generator). Narration: Liam ("Hallo. This is Liam,
  in for Bear."), Teardown register, every term defined in-line,
  Kokoro-safe (no acronyms, no numerals — numbers spelled out:
  "nine in ten", "four hundred thirty million"). First full run
  FAILED on the BHTF assertion (narration "find" vs prompt "Find" —
  mid-sentence capitalization); fixed the assertion to
  case-insensitive on that check, keeping the full-prompt-word
  verification. Second run: beats=12 body=8 total=214.4s (~3m34s) —
  inside the 190–250 s band; all assertions pass (12 beats, 8 manim
  beats, class names match beat ids, BHTF reads the prompt in full,
  all voices am_onyx).
- 18:15 — Wrote scenes.py: pasted `templates/iso_kit.py` verbatim at
  the top, then 8 scene classes (B00_PhoneVideo, B01_WhatCaptions,
  B02_ThePass, B03_OpenIt, B04_PressButton, B05_CheckIt, B06_TwoWays,
  B07_WhoWatches). Cast kept whole film: the phone video, caption
  lines, the dark AI block, the captioning tool, check stamps.
  Midpoint-guard timing: every play lands before mid−0.3 s or starts
  after mid+0.3 s, paced by `until()` on verbatim narration phrases
  (all 24 verified present, script-checked, 0 misses).
- 18:20 — Gate: `python3 -m py_compile` clean on both files;
  `static_scene_check.py` per class from a scratch folder holding ONLY
  `scenes.py` (+ `beat_sheet.json` beside it): **8 clean · 0 warn ·
  0 error on the first full run.** No fixes were needed at the gate.
- 18:35 — Wrote CHECKS-REPORT.md (8 clean · 0 warn · 0 error,
  pacing-phrase audit 24/24, design-time guards listed),
  CLAUDE-CODE-RENDER.md (12-file fetch, Kokoro am_onyx voicing with
  the spelled-out-numbers note, deferred `manim_layout_audit.py
  --curve-strict` per class, review-cut and final commands), and
  README.md. Deleted the `__pycache__` that py_compile created in the
  package dir.
- 18:40 — PUSH BLOCKED (not retried further): all 12 `gh-put-file.py`
  PUTs to `muse/youtube/how-to-use-ai/captions-that-write-themselves/`
  returned HTTP 403 `policy_denied` (`hitl_domain_allow_github_com_...`,
  detail `proactivity_read_only_preparation`) — this subagent's egress
  policy allows Contents API GET but denies PUT in this proactive
  flow. A single-file retry failed identically: the block is
  deterministic, not transient. The 12 files are complete and
  QC-clean at
  `~/workspace/film-builds/how-to-ai/captions-that-write-themselves/`;
  a parent/root agent with write egress must run the 12 pushes and
  the Contents-API verification.
