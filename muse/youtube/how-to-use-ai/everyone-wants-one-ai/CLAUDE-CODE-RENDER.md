# CLAUDE-CODE-RENDER.md — "ChatGPT or Claude?" (general-audience redo)

Render this film on the Mac with Claude Code + the brutalist.art toolkit.
Pre-render package only — nothing here publishes or uploads anything.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/everyone-wants-one-ai/
```

Files: `beat_sheet.json`, `scenes.py`, `make_sheet.py`, `ACTS.md`,
`SHOTLIST.md`, `FACTCHECK.md`, `SOURCES.md`, `CHECKS-REPORT.md`,
`BUILD-LOG.md`, `PROMPTS.md`, `README.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/B00.mp3`, `audio/B01.mp3`, … `audio/BOUT.mp3`
(12 files). Persona: "Liam, in for Bear"; register: Teardown.
The B00 line starts "Hola. This is Liam, in for Bear." — read it exactly.
The BHTF line contains a quoted prompt — read the quote verbatim, then the
discussion after it.

## 2. Review cut

Render the Manim scenes (`scenes.py`, classes M01–M10) and assemble a review
cut against the measured MP3 durations. Conform each scene to its beat's
audio; M10 covers three beats (BVDT 30 s, BHTF 25 s, BOUT 12 s) in three
phases — split or hold per the audio.

## 3. Visual QC

Sample frames (≥2 fps) plus each beat at ~15/50/85% of its span; actually
look at the PNGs. Check: title-safe margins, no edge bleed or clipping,
legibility at full frame, the @NikBearBrown bug on every beat (lower-right,
low opacity), canvas fill (no timid undersized graphics), and that every
on-screen word is read aloud in its beat. Fix root causes in `scenes.py`
and re-render until zero blockers.

## 4. Captions and final

Generate captions from the narration lines, mux, and produce the final MP4
locally. Do NOT publish or upload — the master stays local for Bear's
review.

## 5. Notes for the render

- House palette is in `scenes.py` (INK/PAPER/ACCENT/BLUE/GREEN/GREY/CARD).
- M02's strike-through must land on the spoken word "smartest".
- M08's two columns must hold ≥ 2 s.
- The outro (M10 phase 3) restates the exact title "ChatGPT or Claude?"
  with the @NikBearBrown handle; Liam re-reads the title then says
  "Liam, in for Bear. Thanks for watching." No jingle, no music on the card.
