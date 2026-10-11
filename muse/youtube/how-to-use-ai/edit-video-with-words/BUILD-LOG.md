# BUILD-LOG.md — Edit video with words

Built 2026-10-07 by Muse, show-tell skill, for the How to AI queue
(Wave 7, #45). Proactivity build: the film was the next item in the
verified Wave 7 queue and the standing directive is to keep building
film after film.

- Re-verified the fact set at build time (2026-10-07): YouTube
  conversational editing announced at Made on YouTube 2026-09-23;
  reported window early 2027 for Shorts + YouTube Create (TechCrunch +
  4 corroborating outlets; YouTube's own posts give no date → the film
  says "the reported window" and captions it on screen). Meta Edits
  Assistant announced 2026-09-30, rolling out US on the Edits app; reads
  views/retention/likes/etc., suggests hooks/captions/scripts/audio;
  "does the digging, creative calls are yours" (Westervelt).
- Wrote `make_sheet.py` (14 beats: 4 bookends + 10 Manim body beats),
  `scenes.py` (10 scene classes + phone/chat/clip/note/cursor helpers).
- Narration: Kokoro `am_onyx`, all 14 beats, measured total 177.2 s
  (~2m57s). BOUT padded with the 1.0 s silent tail (4.11 s) and written
  back to the sheet. No telemetry/approval issues (offline path).
- Static QC (`static_scene_check.py`, per-class, scratch folder):
  first pass 9/10 clean; B09 had one safe-area warning (clip row ran to
  x=6.9) → re-centered, second pass 10/10 clean, 0 warnings, 0 errors.
- `manim_layout_audit.py --curve-strict` NOT run (no pangocairo in this
  VM) — Bear's Mac runs it per CLAUDE-CODE-RENDER.md before the review
  cut.
- Render (VM, 1080p): 10 scenes → `manim/B00.mp4` … `manim/B09.mp4`.
  Two visual fixes after frame review: B04 suggestion chips overlapped
  (re-spaced to x=-3.7/0/3.7, fs=22); B05 stretched clip overlapped its
  neighbor (re-laid the second timeline row, cursor re-seated on the
  dragged edge). Both re-QC'd clean and re-rendered.
- Slate cut: `compile.py --review --height 1080` → 1920×1080 review MP4
  (177.4 s); the 4 Remotion bookends are labeled slates (Remotion can't
  render in the build VM); Bear's Mac renders the real ones.
- Estimated runtime ~2m57s (narration clock). Lane histogram: 10 Manim,
  4 bookend slates. No paid steps; no approval gates tripped (all free).
- Publish note: re-verify the early-2027 window before the final
  publish render (B06/B09 carry the hedge on screen and in VO).
