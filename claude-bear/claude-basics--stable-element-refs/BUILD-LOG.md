# BUILD-LOG — claude-basics--stable-element-refs

## 2026-08-28 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/stable-element-refs/beat_sheet.json` (an
unbuilt Teardown-register scaffold — 0/8 beats filled, no SCRIPT.md).
Question, facts, and beat count (8) carried over unchanged: pixel-coordinate
browser automation ties a click to one viewport (a "Confirm Order" button at
(960, 540) on a 1920×1080 window moves to (720, 405) after a resize to
1440×900, so the old coordinate misses); the fix is a JS-injected stable
`data-ref` attribute (`ref="confirm_order_1"`) stamped on every clickable
element before Claude ever reads the page, so Claude targets by ref name
instead of pixel — the ref survives the resize because it's attached to the
element, not the screen position; exclusion — dynamic elements added to the
page after the ref pass ran need their own re-injection pass, not covered by
the same mechanism. B00 replaced a `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "stable" → "fragile"); the source's
exact ref-assignment prompt moved verbatim (condensed) to BHTF as the Your
Turn prompt. Register re-registered Teardown→Plain (no design judgment added
or removed — the source narration carried none). Close/outro re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Source's B05
verdict/recap beat dropped as a restatement (its content already carried by
B02–B04); source's B04 exclusions beat folded into B04's both-directions
clause. Source's B03 "morph" centerpiece (viewport shrinking while ref stays
glued to the button) is what B04 dramatizes as the anchor payoff. No source
beat was `ai-video-prompt`, pantry, or a human-drop slot (all were already
Remotion-shaped, just unbuilt), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 8 beats, free, `am_onyx`. Durations: B00
   11.86s, B01 12.93s, B02 17.98s, B03 13.29s, B04 18.60s, BCRY 9.41s,
   BHTF 14.95s, BOUT 4.84s.
2. Wrote `scenes.py` (4 Manim scenes, B01–B04) sized to the measured
   durations, and `render_scenes.py`; rendered all four in the foreground.
   B02/B04 scene classes are named `SERB02Scene`/`SERB04Scene` (not the
   boilerplate `B02Scene`/`B04Scene`) specifically to avoid colliding with
   other reels' same-named scenes in `type_check.py`'s global exemption
   sets (see `SPCB04Scene` precedent in that file).
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` (foreground,
   tracked as a background task and waited on its exit code — exit 0,
   never treated as done until the notification confirmed it). B00
   verified: `media/B00.mp4` = 11.87s (≥8s TIMING LAW), and frames pulled
   at 4.0–4.5s show "stable" in terracotta mid-deletion, being replaced by
   "fra[gile]" — the correction lands well inside the beat.
4. `compile.py` → `claude-basics--stable-element-refs.mp4`, 8/8 real (no
   slate), 104.9s, 3840×2160 (THE 4K LAW).

**GATE T (type_check.py) — two real defects found and fixed, plus two
confirmed false-positive patterns exempted (not suppressed blind):**
- Real defect #1: in B02, the "Confirm Order" button label text was
  positioned exactly on top of the click-coordinate dot (`btn2_lbl.move_to
  (btn2.get_center())` and `dot2.move_to(btn2.get_center())` — literally the
  same point), making the label illegible ("Confin[dot]Order"). Fixed by
  moving the caption below the frame instead of inside the button, and
  dropping the redundant "old: (960, 540)" text label (a crossed dot alone
  conveys it; narration + footer already state it in words).
- Real defect #2: in B04, the `ref="confirm_order_1"` label under the right
  viewport frame directly overlapped the caveat's "added after load — no ref
  yet" caption (confirmed by frame pull: the text visibly fused, e.g.
  "...order_1"no ref yet"). Fixed by moving the caveat cluster up into
  frame2's row (clear of ref2's row below the frame) instead of fighting for
  horizontal space in the same band.
- Confirmed false positive (bbox-overlap §8.6b): the "1440 × 900" viewport
  card (a RoundedRectangle) contains a nested RoundedRectangle button with a
  centered dot — same box+interior-shape nesting pattern as
  `B03_HookMechanism`/`B02_FiveProperties` already in
  `BBOX_OVERLAP_EXEMPT_PATTERNS`. The card's closed-stroke bbox
  (~381×212px) naturally encloses the button's bbox (~138×56px), reported
  as "two labels overlapping" though neither is text. Verified by direct
  frame pull (mid-clip and last frame, both B02 and B04): the button sits
  cleanly inside the card with visible margin. Renamed the scenes to
  `SERB02Scene`/`SERB04Scene` first (see above) and added them to
  `BBOX_OVERLAP_EXEMPT_PATTERNS` with justification.
- Confirmed false positive (kerning §8.4, B04 only): the MONO
  `ref="confirm_order_1"` label mixes quote marks and underscores, which
  sit near the baseline and register as a separate low-ink band from the
  cap-height letters, so the row-based gap analyser misreads the
  quote-to-letter transition as one oversized inter-glyph gap. Font is
  named (Menlo); frame pulled and read directly shows one continuous,
  legible monospace run. Added `SERB04Scene` to `KERNING_EXEMPT_PATTERNS`
  with justification.
- Re-ran `type_check.py` to GATE T: PASS (0 FAILs) after the fixes and
  exemptions above.

**Gate V (visual):** pulled 17 frames at 6s spacing across the full 104.9s
runtime, plus targeted frames at the B00 correction and the B02/B04 fix
points, and read them directly. B00's "stable"→"fragile" correction is
legible mid-beat. B02's anchor (Confirm Order button, (960,540) on
1920×1080; crossed dot showing the same raw pixel missing on the resized
viewport) and B04's payoff (identical frame pair, ref label glued to the
button through the resize, caveat cleanly separated) are visually
recognizable as the same object, per ANCHOR LAW. BCRY/BHTF/BOUT text is
centered, legible, no overlap, safe inset respected. No blockers remaining.

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the fixes and exemptions above
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio aac present, duration 104.875s; mp4
  mtime (1787925290) newer than beat_sheet.json mtime (1787924992)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:4 — remotion at 50% of beats, over the ~40% pantry cap in MOTION.md.
Structural, not a defect: hai-simple's mandated shape is B00 (writer) + BCRY
+ BHTF (Your Turn) + BOUT (outro) all REMOTION by skill contract, against 4
GRAPHIC body beats for this 8-beat reel — the ratio is fixed by beat count.
Logged per the honesty rule rather than reworking beat count to dodge the
warning.

Metadata file written: `claude-basics--stable-element-refs.md` (channel
@HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `claude-basics` family
prefix — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate.

## Phase 4 — delivery

Master was already born at 3840×2160 (compile.py's 4K LAW), so it was
copied to `claude-basics--stable-element-refs-4k.mp4` rather than a separate
4K re-render. `deliver.py --push` staged `DELIVERY/claude-basics--stable-element-refs/`
(4K master + description) and committed the text artifacts (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md) to `humanitarians-youtube/claude-bear/` — commit
`9db5db04`, pushed.

**Status: DELIVERED.**
