# CLAUDE-CODE-RENDER.md — The long game

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/the-long-game/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (13 files). Persona: "Liam, in for Bear";
register: Teardown. Greeting is "Hallo" (voices cleanly). Read the BOUT line
exactly: "The long game. At Nik Bear Brown." then a 1.0 s silent tail.

Pronunciation notes: the script avoids spelled-out acronyms, version numbers,
and numbers spoken right before "Claude" (known Kokoro misreadings per the
show-tell skill). Whisper-check BIDEA's first line ("Hallo") as usual.

## 2. Layout audit (deferred — could not run in the build VM)

`manim_layout_audit.py --curve-strict` needs Manim/pangocairo, which the
build VM does not have. Run it here before the review cut:

```
python3 runtime/qc/manim_layout_audit.py scenes.py --class <ClassName> --curve-strict
```

for each of the 9 scene classes (B00_Stack … B08_Habit). All explicit
coordinates were hand-checked against the ±6.3 × ±3.4 safe area during the
build; the audit is the confirmation.

## 3. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel how-to-ai-the-long-game \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the page stack drops with its title line in
B00; the stack bursts into scattered pages in B01 with the repeat and
contradiction dots; the three numbered pages, drift dots, and staple read
cleanly in B02; the outline card's four section rows draw in and the
approval check lands in B03; the arrow chain grows outline → section one →
section two in B04–B05 with a check per section; the scan line sweeps and
the repeated line lifts out in B06; the side-by-side reads cleanly in B07
(jumble left, neat checked stack right); the three-row rule card lands in
B08. Two known soft spots: B02's drift dots land at ~52–55% of the beat
and B07's right-side stack arrives at ~52–58% — confirm the midpoint
frames still read.

## 4. Final 4K master

```
./art final --reel how-to-ai-the-long-game
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 13 beats, ~3m22s (202 s estimated). 9 Manim scenes, all static-QC clean
  (0 warn, 0 error); 4 Remotion bookends (BIDEA, BDEFS, BHTF, BOUT).
- Skill: show-tell. No ShowTellCard kinds used — every body beat is a
  drawing (reasons in SHOTLIST.md).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
