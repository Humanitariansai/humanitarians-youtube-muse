# CLAUDE-CODE-RENDER.md — Give it a voice

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`, then:

```
cd muse/youtube/how-to-use-ai/give-it-a-voice/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (11 files). Persona: "Liam, in for Bear";
register: Teardown.

Whisper-check before the review cut:
- BIDEA "Hallo" — known-clean greeting; verify it reads naturally.
- B01 "Suno" — check pronunciation; re-voice from phonemes if it slurs.
- B05 "open bracket, excitedly, close bracket" — the on-screen pill shows
  "[excitedly]"; the narration must NOT read the brackets literally.
- BHTF: the prompt is read verbatim — "Turn my script into a
  voiceover-ready script. Use short sentences. Write numbers and acronyms
  the way they sound. Then read it back to me, exactly as it will be
  spoken."
- BOUT: read the title exactly — "Give it a voice. At Nik Bear Brown."
  — then pad a 1.0 s silent tail.

Write the ffprobe-measured durations back to `actual_duration_s` per beat.

## 2. Static layout audit (deferred to this Mac pass)

`manim_layout_audit.py --curve-strict` could not run in the build VM (no
Manim/pangocairo installed) — run it here before the review cut:

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
python3 runtime/qc/manim_layout_audit.py --curve-strict \
  <film-dir>/scenes.py
```

The render-free static checker already passed 7/7 classes (0 warn, 0 error);
this audit is the real-Manin layout confirmation.

## 3. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel give-it-a-voice \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the deck pages stack and the muted speaker
lands in B00; the script page visibly drops INTO the open Suno box (page
between the back and front walls) and the voice wave + music trail merge
into the track bar in B01; the pirate flag dot pops on "pirate captain"
and the three sliders rise on "fine-tune the voice" in B02; the three
step pills chain and the track bar lands on "generate" in B03; the
wandering-accent arc clears the pill and the pause ticks land wide apart
in B04; the Vids window, script pill, "30 voices" pill, "[excitedly]"
tag, and the "built in" check all stay inside the window in B05; the
terracotta X sits squarely on the "teh" word and the clean page earns
the check in B06.

## 4. Final 4K master

```
./art final --reel give-it-a-voice
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 11 beats, ~3m02s (measured audio sets the clock). 7 Manim scenes, all
  static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
