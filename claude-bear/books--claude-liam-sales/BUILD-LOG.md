# BUILD LOG — hai-simple/books--claude-liam-sales

Redo of `anthropics/books/claude-cowork-plugins/youtube/claude-liam-sales` (Teardown/
deep-explainer register) as `hai-simple` (Plain register, Humanitarians AI skin). Source
folder untouched. This invocation picked up a reel that was already substantially built
(SCRIPT.md, beat_sheet.json, all 22 beats' audio, 18 Manim body renders, 3 of 4 Remotion
beats) and carried it to a verified review cut.

## State on pickup

- `beat_sheet.json`, `SCRIPT.md`, `QUESTION.md`, `CARRY-OUT.md` already written (22 beats:
  B00 hesitant-writer cold open, NB01–NB18 Manim body, BCRY carry-out, BHTF your-turn,
  BOUT outro).
- Audio: all 22 beats generated via Kokoro `am_onyx`, `actual_duration_s` measured and
  stamped.
- Video: `manim/NB01.mp4`–`manim/NB18.mp4` rendered. `media/B00.mp4`, `media/BCRY.mp4`,
  `media/BOUT.mp4` rendered. **`media/BHTF.mp4` missing** — the only unrendered beat.

## What this invocation did

1. Rendered the missing `BHTF` beat (`ClaudeComposerAsk`, "Your turn") via
   `remotion_scenes.py --only BHTF`.
2. Ran `compile.py` → `books--claude-liam-sales.mp4`, 4K (3840×2160), 252.1s, 22/22 beats
   real, `content-check`/`frame-check`/`lane-check` all PASS, GATE AUDIO PASS
   (mean_volume −23.7 dB).
3. **Gate V caught a real defect in B00** (see below) — fixed at the root, B00
   re-rendered, master recompiled.
4. Wrote `books--claude-liam-sales.md` (YouTube metadata) and this log.
5. Packaged 4K delivery.

## One defect found and fixed during Gate V (frame QC)

**B00's WRITER LAW correction never fired — silent, not a crash.** The authored props
were `triggerWords: "professional salespeople"` / `replacementWords: "anyone who needs
clients"`, a two-word phrase. `BrutalistHesitantWriter.tsx`'s `buildActs()` matches
`triggerWords` against `core.toLowerCase()` **per single whitespace-delimited token**
(the text is tokenized on `\s+`, and each trigger is compared against one token at a
time) — a multi-word trigger string can never match a single token, so the "hesitate,
delete, retype" sequence silently never triggers and the writer just types the original
wrong sentence straight through, uncorrected, for the entire beat.

Caught by pulling a frame late in B00 per the WRITER LAW's own verification instruction:
at 11.44s of an 11.46s beat, the on-screen text still read "…professional salespeople…"
with the caret already past the sentence — the correction was never visible, exactly the
failure mode the SKILL.md timing note warns about (though here the cause was a prop
mismatch, not a timing budget). Confirmed root cause by reading
`runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` directly and by diffing against
a working prior reel (`hai-simple-what-is-claude-actually/beat_sheet.json`), which uses a
single-word pair (`"search"` → `"language"`) — the component's actual, intended contract.

**Fix:** rewrote B00's text/props to a single-word swap that keeps the same wrong-guess
concept and ties directly into the anchor: `triggerWords: "salespeople"` →
`replacementWords: "freelancers"`, text now "The sales plugin / is only for /
salespeople. / Who's it actually for?" → corrects to "…is only for freelancers…". Chosen
over other single-word options because it lands on the exact word NB02's anchor pays off
("a freelancer with one lead"). Re-rendered `media/B00.mp4` (11.47s, matches
`actual_duration_s`), verified via frame grabs at 6.0s and 11.0s that "freelancers" is
on screen and stable well before the beat ends. Master recompiled after the fix — final
`books--claude-liam-sales.mp4` reflects the corrected B00.

**Process note:** the very first re-render attempt was cut off by an over-eager local
`timeout` wrapper before Chrome/Remotion had finished; the resulting file was a stale
20s partial artifact. Re-ran clean in the foreground with no external timeout and
verified the process's own exit code (0) plus `ffprobe` duration (11.466667s, exactly the
beat's `actual_duration_s`) before trusting the output — a real render succeeded, the
first apparent anomaly was a harness artifact, not a second defect.

## Gates

- **TIMING LAW (B00):** narration "People assume the sales plugin is built for
  professional salespeople with a CRM. It isn't — it's for anyone who needs clients:
  consultants, freelancers, agency owners. So who's it actually for?" (35 words) +
  `lead_silence_s` 0.8 → measured `actual_duration_s` **11.46s**, clears the ≥8s floor.
  Correction verified on screen (see above).
- **GATE AUDIO:** PASS, mean_volume **−23.7 dB** (well above the −40 dB floor), max
  −2.9 dB.
- **Gate V (frame QC):** 21 frames sampled at 12s intervals across the full 4:12 cut,
  plus targeted B00 frame grabs (6.0s, 10.5s, 11.0s, 11.2s, 11.35s, 11.44s). Palette
  consistent (`#F3EBDD`/`#2F2A26`/`#E4572E`), safe insets held, no text overlap or
  overflow, `@HumanitariansAI` handle present on B00 and BHTF. One defect found (B00
  correction, above) and fixed; nothing else flagged.
- **content-check / frame-check / lane-check:** all PASS per `compile.py` (22/22 beats,
  no violations).
- **motion-histogram WARNING (graphic 81%, over the ~40% pantry cap):** expected and
  accepted. NO-GENAI/NO-PANTRY LAW forces every body beat to GRAPHIC or REMOTION; this
  reel's spine is 4 REMOTION beats (B00, BCRY, BHTF, BOUT) against 18 GRAPHIC (Manim)
  body beats — same disposition as every other redo in this book's series (e.g.
  `books--claude-liam-legal-finance`).

## Output

`books--claude-liam-sales.mp4` — 252.1s, 22/22 beats real (no slates), audible narration
throughout, 3840×2160. This is the review cut (COMPLETION LAW satisfied: newer than
`beat_sheet.json`, audible audio verified via ffprobe: mean_volume −23.7 dB).

**Playlist:** Extending Claude — Skills, Plugins & Connectors. `SUBJECT.json`'s
`family: "books"` and the `books--` slug prefix have no literal entry in
`playlists.json`'s map; falling straight to the `hai-simple`→"Claude Basics" fallback (or
`_default`) would be wrong for a reel that is squarely about one Claude plugin. Every
prior sibling redo of this same source book (`books--claude-liam-legal-finance` and
others) already established, and logged, the same content-match to "Extending Claude —
Skills, Plugins & Connectors" — followed that precedent here for consistency across the
book's reel family.

## Phase 4 (4K + delivery)

- **4K master:** `compile.py` (no `--review`) enforces its 4K LAW automatically — wrote
  `books--claude-liam-sales.mp4` natively at 3840×2160, 252.1s, 22/22 beats real,
  mean_volume −23.7 dB. Copied to `books--claude-liam-sales-4k.mp4` so `deliver.py`'s
  `newest_master()` picks it as the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox `DELIVERY/books--claude-liam-sales/` (4K
  master + description, this machine's `DELIVERY/` is a symlink directly into the Drive
  `Claude_Bear/` mount); repo
  `humanitarians-youtube/claude-bear/books--claude-liam-sales/` (README.md +
  beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md + CARRY-OUT.md + QUESTION.md
  — no media).

**Status: DELIVERED.**
