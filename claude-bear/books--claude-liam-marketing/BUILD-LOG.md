# BUILD-LOG — books--claude-liam-marketing

Reel: `Claude, On Message` (The Marketing Plugin) — hai-simple redo of
`anthropics/books/claude-cowork-plugins/youtube/claude-liam-marketing/beat_sheet.json`.

## State at pickup

This invocation found a prior session's work already substantially complete:
`SUBJECT.json`, `QUESTION.md`, `CARRY-OUT.md`, `SCRIPT.md`, `beat_sheet.json`
(23 beats, all `actual_duration_s` measured), audio for all 23 beats in `mp3/`,
all 19 GRAPHIC body beats rendered in `manim/NB01.mp4`–`NB19.mp4`, and 3 of 4
REMOTION beats rendered in `media/` (B00, BCRY, BOUT). `TYPECHECK.md` (GATE T)
already read PASS, 0 FAILs, 23/23 beats checked. No BUILD-LOG.md existed yet
and no master mp4 had been compiled — picked up here per COMPLETION LAW rather
than rebuilding.

## What this invocation did

1. Rendered the one missing beat, `BHTF` (ClaudeComposerAsk — Your Turn), via
   `remotion_scenes.py --only BHTF`, foreground, waited on exit code.
2. Compiled: `compile.py` → `books--claude-liam-marketing.mp4`, 295.2s,
   3840×2160 (4K LAW — master born native 4K), 23/23 slots filled
   (`B00:VIDEO NB01–NB19:MANIM BCRY:VIDEO BHTF:VIDEO BOUT:VIDEO`).
   `content-check`, `frame-check`, `lane-check` all PASS. GATE AUDIO PASS,
   mean_volume −23.7 dB.
3. Gate V: pulled 25 frames at 12s spacing across the full runtime + a direct
   late-frame pull from `media/B00.mp4` alone. No layout defects — legible
   text, safe insets, no overlap, correct humanitarians cream/ink/terracotta
   skin throughout, correct @HumanitariansAI marks, correct outro line
   ("Claude, On Message — the marketing plugin. Liam, in for Bear.").
4. WRITER LAW check: `media/B00.mp4` = 10.5s (≥ 8s). Pulled a frame at
   t=9.0s (sseof −1.5s) and confirmed the correction is on screen and
   settled: "to get **a plan** written." replacing the naive "to get
   content written." — TIMING LAW and WRITER LAW both satisfied.
5. Re-verified independently with ffprobe/ffmpeg (not just compile.py's own
   report): master mp4 is newer than `beat_sheet.json` (16:24 vs 16:28),
   carries both video (h264) and audio (aac) streams, duration 295.25s,
   mean_volume −23.7 dB, max_volume −2.7 dB — audible, comfortably above the
   −40 dB floor.

## Non-blocking warning

`compile.py` logged: `'graphic' carries 19/23 beats (82%) — over the ~40%
pantry cap`. This is structural, not a defect to chase here: the source
sheet's body is uniformly GRAPHIC (manim chip-row scenes), and hai-simple's
own spine only supplies 4 REMOTION beats (B00/BCRY/BHTF/BOUT) regardless of
body content. Same disposition as every other `books--claude-liam-*` sibling
redo in this log. Both GRAPHIC and REMOTION satisfy the NO-GENAI/NO-PANTRY LAW;
no beat is ai-video-prompt or a pantry/request-card slot.

## Facts kept from the source (redo mode)

Five capabilities under one install (content, campaigns, competitors,
performance, brand); "write me a post" vs. plan/analyze/refine; specificity
lever anchor ("professionals" vs. "small-business owners considering AI tools
but not technical"), planted NB10, paid off NB12 (80%-vs-50%-right); content
calendar, 5-email launch sequence, repurposing-one-post-into-five, monthly
metrics reckoning; four habits (frontload brand, ask variations, delegate the
dreaded, review everything); hard limit — drafts well, won't replace a CMO,
judgment stays yours. Register re-registered Plain (source was Teardown);
voice is Liam `am_onyx` regardless of source; humanitarians skin throughout;
no beat is a human-drop or paid-generation slot.

## Gates

- GATE T (type_check.py): PASS, 0 FAILs, 23/23 beats checked (pre-existing,
  reconfirmed unchanged since no beat visuals were altered this session).
- GATE AUDIO: PASS, mean_volume −23.7 dB (compile.py) / −23.7 dB (independent
  ffmpeg volumedetect).
- Gate V (visual QC, frame pulls): PASS, no blockers.
- WRITER LAW / TIMING LAW (B00): PASS, correction visible, clip ≥ 8s.

## Result

`books--claude-liam-marketing.mp4` — 295.2s, 3840×2160, audible audio,
newer than `beat_sheet.json`. Review cut DONE. `beat_sheet.json` not touched
after this compile, per COMPLETION LAW.

## Phase 4 (delivery)

Master was already born native 3840×2160 (compile.py's 4K LAW), so
`books--claude-liam-marketing-4k.mp4` was produced as a direct copy of the
master (verified 3840×2160 via ffprobe before copying) — no separate re-render
needed. Ran:

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

- Drive outbox: `DELIVERY/books--claude-liam-marketing/` —
  `books--claude-liam-marketing-4k.mp4` + `books--claude-liam-marketing-description.md`.
- Repo: `humanitarians-youtube/claude-bear/books--claude-liam-marketing/` —
  README.md (= description), beat_sheet.json, SCRIPT.md, SUBJECT.json,
  BUILD-LOG.md, CARRY-OUT.md, QUESTION.md. No mp3/mp4 in the repo copy.
- Committed + pushed: `1e524158c9cbdc727599a6a440bea7eb19c35e4e`.

Reel status: DELIVERED.
