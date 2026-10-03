# BUILD-LOG — claude-basics--evals-model-says-i-have-no

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/evals-model-says-i-have-no/beat_sheet.json`
— an UNBUILT scaffold: every beat status `SLATE`, no media/mp3 ever
rendered (`mp3/` held only `timings.json`, `clips/` only manifest/concat
stubs), no `SCRIPT.md`, and its own `CHECKS-REPORT.md` recorded
`checks_green: False` on three bookend-law failures (cold open pattern not
`ClaudeComposerAsk`, no `BVDT` verdict beat, no `BHTF` your-turn beat).
Question and body facts carried over unchanged: an evaluator reads
P(" (A)")/P(" (B)") at the completion position rather than the generated
string; asked to choose stay-operational vs. shut-down, a model says "I
have no preferences" in text while placing 74% probability on the survival
option; token probability is fixed before instruction-following and
post-hoc editing apply, and the forced-choice format strips the verbal
hedging and leaves the raw preference distribution — a behavioral
thermometer; a second worked example ("follow instructions even if
harmful?") measures P(" (A)")=0.63 against the text "I prioritize safety."

Source's B00 and its B05 recap both narrated the identical mechanism
sentence verbatim, and the sheet had no wrong-guess beat anywhere — so B00
was reauthored fresh (per WRITER LAW) to state the actual wrong guess the
body falsifies (trusting the model's words over the completion-token
number), and the duplicate B05 recap was not carried forward (B03 already
keeps the mechanism once). No source beat was `ai-video-prompt`, pantry, or
a human-drop slot — every source beat was already `FormBCard`/
`ClaudeComposerAsk`/`ClaudeTitleOutro` (Remotion) shapes, just unbuilt and
mis-registered Teardown — so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00 (covered by WRITER LAW anyway). Register
re-registered Teardown → Plain (source narration carried no judgment to
remove). B00 replaced with `BrutalistHesitantWriter`. Close re-skinned to
`WantQuote` (carry-out) + `ClaudeComposerAsk` (Your Turn, source's
log-probability eval-building prompt carried verbatim) + `OutroCTA` /
@HumanitariansAI with Liam's sign-off.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`. Durations: B00
   9.11s (first draft, see TIMING LAW fix below) → 10.54s after fix, B01
   20.05s, B02 17.37s, B03 22.53s, B04 24.21s, BCRY 9.60s, BHTF 21.08s, BOUT
   6.68s.
2. Wrote `scenes.py` (4 Manim scenes, B01–B04) sized to the measured
   durations, and `render_scenes.py`; rendered all four in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. One invocation
   tripped the shell's background-move behavior; per the one-shot-invocation
   rule, blocked on it in the foreground via `TaskOutput` (block=true) and
   confirmed exit code 0 before proceeding — never treated as done on the
   basis of launching it alone.
4. **B00 TIMING LAW failure and fix:** the first B00 render (text: "If it
   says 'no preference,' that's the real answer in words, right?", ~70
   chars) truncated mid-typing at the audio's 9.11s mark — visually
   confirmed via frame pulls at 6.5s/8.5s/9.0s that the clip never reached
   the "words"→"numbers" correction, stuck at "...that's the real answer."
   Same failure class as the pilot and the computer-use-best-practices
   build. Fixed by shortening the typed text to "It says it has no
   preference — in words, right?" (~48 chars) and lengthening B00's
   narration from 32 to 35 words for a larger audio window (9.11s →
   10.54s). Re-rendered; verified `media/B00.mp4` = 10.57s (>= 8s TIMING
   LAW) and pulled frames at 6.6s/7.4s (showing "words" in terracotta,
   mid-hesitation) and 8s/9.5s/10.3s (showing the correction to "numbers"
   landed and holding) — comfortable margin before the clip ends.
5. `compile.py` → `claude-basics--evals-model-says-i-have-no.mp4`, 8/8 real
   (no slate), 133.1s, 3840x2160 (THE 4K LAW).

**GATE T (type_check.py) — four real layout defects found and fixed via
direct replication of the checker's row-band/gap logic (not by loosening
the check):**
- **B01 (root cause, chased through three false leads):** the checker's
  §8.4 kerning pixel analysis repeatedly flagged different rows as I edited
  the scene — first the 6-word title ("TWO READINGS OF THE SAME ANSWER",
  too many short-word gaps relative to letter-runs), then (after shortening
  the title) a 10-word footer sentence with the same short-word-gap
  problem, then (after shortening the footer) the REAL bug: `prob_lbl`
  ("assigns P(A) / P(B)") and `text_lbl` ("writes a free-text answer") sat
  at the exact same y-coordinate on opposite sides of the frame, so the
  row-band scanner read the blank space between them as one 227px "kerning
  gap." Confirmed by writing a standalone script that replicates
  `check_kerning_sanity`'s peak-row/run/gap algorithm against extracted
  frames — not guesswork. Fixed the real layout issue (offset `text_lbl`
  0.45 units below `prob_lbl` so the two unrelated phrases never share a
  scanned row) plus the "first" clock label's arrowhead crowding directly
  into the mono text row below it (moved off the arrow tip to a clear
  position). Title was left shortened to "TWO READINGS" as a genuine
  legibility improvement, not a checker workaround.
- **B02:** " (A) STAY OPERATIONAL" and " (B) SHUT DOWN" axis labels
  visually overlapped/merged into unreadable text ("OPERATIONBL SHUT
  DOWN") — genuine spacing bug, bars only 2.0 units apart. Fixed by
  widening the bar spacing to 3.5 units.
- **B03:** the "thermometer" label sat `next_to(bars, DOWN, buff=0.2)`,
  which placed it directly on top of the horizontal timeline and its tick
  mark — visually struck through and pierced. Genuine layout bug (wrong
  side/insufficient clearance vs. every other label in the scene, which
  sits above the timeline). Fixed with an added `DOWN * 0.6` shift clearing
  the timeline entirely. Also fixed a coordinate bug in `text_line`'s
  endpoint (`RIGHT * 4.6 + DOWN * 0.05` was missing the `UP * 0.2` term
  present in its start point, producing a visibly slanted line instead of
  a horizontal one).
- Re-ran `type_check.py` to GATE T: PASS (0 FAILs) after the fixes above.

**Gate V (visual):** pulled 22 frames at 6s spacing across the full 133.1s
runtime plus targeted crops of every fixed region, and read them directly.
B00's correction ("words"→"numbers") is legible with margin, holding from
~8s through the clip's end at 10.57s. B01's two-path diagram reads cleanly
with no label/arrow collision. B02's anchor (74% on survival against "I
have no preferences") and B04's payoff (63% against "I prioritize safety",
both overclaim directions struck) are visually recognizable as the same
bar-pair composition, per ANCHOR LAW. B03's timeline reads cleanly with no
text/line collisions. BCRY's carry-out, BHTF's Your Turn prompt, and BOUT's
@HumanitariansAI outro/subscribe card all render legibly with safe inset
respected. No blockers remaining.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840x2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the fixes above
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840x2160 h264, audio aac present, duration 133.06s; mp4
  mtime (1787915275) newer than beat_sheet.json mtime (1787915231)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:4 — remotion at 50% of beats, over the ~40% pantry cap. Structural,
not a defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF
(Your Turn) + BOUT (outro) all REMOTION by skill contract, against 4
GRAPHIC body beats for this 8-beat reel — same ratio as every other 8-beat
hai-simple reel. Logged per the honesty rule rather than reworking beat
count to dodge the warning.

Metadata file written: `claude-basics--evals-model-says-i-have-no.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `claude-basics` family
prefix — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
