# BUILD LOG — hai-simple/books--claude-liam-enterprise-search

Redo of `anthropics/books/claude-cowork-plugins/youtube/claude-liam-enterprise-search`
(Teardown-register deep-explainer, 36 beats, ~330s) as `hai-simple` (Plain register,
Humanitarians AI skin). Source folder untouched. This invocation picked up a prior
session's in-progress artifacts (beat_sheet.json, SCRIPT.md, CARRY-OUT.md, QUESTION.md,
audio for all 8 beats, manim B01–B04, and media/B00.mp4, BHTF.mp4, BOUT.mp4 already
rendered) and continued to completion rather than rebuilding from scratch.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Body compressed from the source's six acts (36 beats)
  to one idea per beat (8 beats: B00 writer + B01–B04 body + BCRY + BHTF + BOUT). Acts IV
  (five workflows) and VI (habits) are referenced in the carry-out/Your Turn instead of
  given their own beats, to fit the Plain-register 2–3 minute runtime.
- **Cold open:** source's `ClaudeComposerAsk` direct-answer ask → `BrutalistHesitantWriter`.
  Writer types "Can Claude search everywhere for it?", hesitates on "everywhere", corrects
  to "only what I can see" — the reel's actual wrong guess, picked up and falsified by B01's
  anchor (a "Q3 notes" file that hides a payment-processor decision from a filename search).
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of source's
  `ClaudeTitleOutro`/`@NikBearBrown`.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** unchanged. Buried-answer problem, filename-vs-content mismatch,
  reads-content-across-sources mechanism, context-injection (grounded vs. generic), and the
  access-boundary both-directions clause all carried from the source, reworded for register.

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this compression was AI-VIDEO, pantry, or a human-drop slot; the
source's `pantry_note`/doodle-still beats (B03/B05/B09/B13/B14/B17/B20/B23) were
illustrative padding for the fuller cut and are dropped rather than substituted. Every
beat in this reel is REMOTION (B00, BCRY, BHTF, BOUT) or bespoke GRAPHIC/Manim (B01–B04,
humanitarians palette `#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`).

## Three real defects found and fixed (not just re-run)

1. **B00 TIMING LAW near-miss — the correction never completed on first render.** The
   inherited beat_sheet.json's B00 render (`media/B00.mp4`, 10.27s, matching the measured
   audio) ended mid-pause on "everywhere" highlighted for deletion — the replacement
   "only what I can see" never got typed. Root cause: `BrutalistHesitantWriter`'s
   deterministic timeline (given `charMs:55, hesitateWithin:3, hesitateBetween:22,
   mistakeRate:6`) for this text + a 4-word replacement phrase ran longer than the 10.26s
   audio window, so `remotion_scenes.py`'s freeze-hold truncation (`-t <duration>`) cut it
   off before the swap. Fixed by speeding up the typing performance (`charMs 55→42,
   mistakeRate 6→3, hesitateWithin 3→1, hesitateBetween 22→10, jitter 26→22`) — narration
   text and duration untouched, per TIMING LAW's 20–35-word / ≥9s-window contract (already
   satisfied at 32 words / 10.27s). Re-rendered; verified via frame grabs at 9.5s/10.0s/
   10.2s/last-frame that "everywhere" is fully replaced by "only what I can see" and the
   corrected question sits settled well before the clip ends.
2. **B02 overlap + invisible text.** `scenes.py`'s `hit_group` (the "...switched to Stripe
   because..." highlight) was centered directly on the file card's own center, stacking a
   terracotta highlight on top of the "Q3 notes" title/subtitle text. The highlight's
   background rectangle was also a fixed `width=3.4` while the text inside it was wider,
   and the text color matched the page background — so the portion of the text overhanging
   the box rendered invisibly (cream-on-cream), reading as clipped ("vitched to Stripe
   becaus..."). Fixed by auto-sizing `hit_bg` to `hit_line.get_width()+0.4` and repositioning
   `hit_group` below the file card (`file_card.get_bottom() + DOWN*0.55`) instead of on top
   of it. Re-rendered, reverified in frame grabs — full sentence legible, no overlap.
3. **B03 vertical, garbled text.** `doc_txt` and `chat_txt` were built as a single
   multi-line `Text(...)` (using `\n`) and then had `.arrange(DOWN, buff=...)` called on
   them. `Text`'s submobjects are individual glyphs, not lines, so `.arrange(DOWN)` restacked
   every character one-per-line instead of respecting the existing line breaks — rendered as
   an unreadable vertical column of single letters overlapping the title and the "grounded in
   your own decisions" label. Fixed by removing the erroneous `.arrange()` calls (`Text`
   already lays out `\n` correctly on its own). A second, related overlap surfaced once the
   text was legible: `grounded_lbl.next_to(grounded_arrow, UP, ...)` positioned the label
   relative to the whole diagonal arrow's bounding box, landing it on top of the chat card's
   text. Fixed by anchoring it to the target circle instead (`grounded_lbl.next_to(target,
   UP, buff=0.35)`). Re-rendered, reverified — text horizontal, readable, no overlap with the
   title or either card.

All three fixes were applied and reverified with full-resolution frame grabs (`ffmpeg -ss
<t> -frames:v 1`) before recompiling, not assumed from a duration match alone.

## Gates

- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **10.27s** (≥9s floor); correction verified complete and settled by
  ~9.5s, well inside the window, after the typing-speed fix above.
- **GATE AUDIO:** PASS, mean_volume **-23.8 dB** (well above the -40 dB floor), max_volume
  -2.9 dB.
- **Gate V (frame QC):** full-cut frame sweep (32 frames at 4s spacing) plus dense
  re-checks (1–2s spacing) across every beat boundary and both defect windows (B02 ~35–53s,
  B03 ~53–76s) after each fix. Two real defects found (B02, B03, detailed above) and fixed
  at the root, not papered over; B00, B01, B04, BCRY, BHTF, BOUT all clean on first review —
  legible, safe inset, no overlap.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (8/8 beats,
  no violations).
- **Motion histogram:** WARNING, remotion 4/8 (50%, over the ~40% pantry cap). Non-blocking
  and structural for this skill: B00 (writer), BCRY, BHTF, BOUT are REMOTION by the
  hai-simple spine itself (WRITER LAW + CARRY-OUT/Your-Turn/outro), and at only 4 body beats
  this 8-beat reel necessarily runs higher than 40% Remotion. Same disposition as sibling
  `books--` redos' graphic-heavy warnings on the other side of the ratio.

## Output

`books--claude-liam-enterprise-search.mp4` — 129.7s, 8/8 beats real (no slate), audible
narration throughout. This is the review cut (COMPLETION LAW satisfied: newer than
`beat_sheet.json`, mean_volume -23.8 dB verified via ffprobe/compile GATE AUDIO).

**Playlist:** Extending Claude — Skills, Plugins & Connectors. `SUBJECT.json`'s `family`
("books") and this reel's `books--` slug prefix have no literal entry in
`skills/make/hai-simple/loop/playlists.json`'s map; the beat_sheet.json inherited from the
prior session had stamped the mechanical skill-name fallback ("hai-simple" → "Claude
Basics") into `metadata.playlist`, but three immediately-preceding sibling redos of this
same source book (`books--claude-liam-building-plugins`, `books--claude-liam-combining-
plugins`, `books--claude-liam-data`) already established and logged the precedent of
content-matching instead of using that fallback, landing on "Extending Claude — Skills,
Plugins & Connectors" every time. For consistency this reel's `<slug>.md` uses that same
playlist. Per COMPLETION LAW, `beat_sheet.json` was not re-touched post-compile to fix its
stale `metadata.playlist` value — this note documents the discrepancy instead.

## Phase 4 (4K + delivery)

- **4K master:** already born native 3840×2160 from `compile.py`'s 4K LAW (no `--review`
  flag used). Copied to `books--claude-liam-enterprise-search-4k.mp4` so `deliver.py`'s
  `newest_master()` picks it as the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/books--claude-liam-enterprise-search/` (4K master + description, syncs to
  Drive `Claude_Bear/` on this machine's Drive-for-desktop mount); repo
  `humanitarians-youtube/claude-bear/books--claude-liam-enterprise-search/` (README.md +
  beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md + CARRY-OUT.md + QUESTION.md —
  no media). Commit `3d0cfd51`.

**Status: DELIVERED.**
