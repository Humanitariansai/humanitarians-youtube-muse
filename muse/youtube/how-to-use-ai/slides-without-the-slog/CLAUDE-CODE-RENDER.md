# CLAUDE-CODE-RENDER.md — Slides without the slog

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/slides-without-the-slog/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (13 files). Persona: "Liam, in for Bear";
register: Teardown. Greeting is "Hallo" (voices cleanly). Read the BOUT line
exactly: "Slides without the slog. At Nik Bear Brown." then a 1.0 s silent tail.

Pronunciation notes: the script avoids spelled-out acronyms, version numbers,
and numbers spoken right before "Claude" (known Kokoro misreadings per the
show-tell skill). Whisper-check BIDEA's first line ("Hallo") as usual.
"Eighteen slides" and "five-slide" are ordinary spoken words, not version
numbers.

## 2. Layout audit (deferred — could not run in the build VM)

`manim_layout_audit.py --curve-strict` needs Manim/pangocairo, which the
build VM does not have. Run it here before the review cut:

```
python3 runtime/qc/manim_layout_audit.py scenes.py --class <ClassName> --curve-strict
```

for each of the 9 scene classes (B00_Goal … B08_Habit). All explicit
coordinates were hand-checked against the ±6.3 × ±3.4 safe area during the
build — including the B00 row, which is laid on a constant (x0+y0) so the
iso rise doesn't push card C out of frame — and the layout math is
recorded in the scenes.py header comment; the audit is the confirmation.

## 3. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel how-to-ai-slides-without-the-slog \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the notes page drops and the three clean
slide cards land in a row in B00; the big wall-of-text slide lands with
its stacked copies behind it in B01; the audience dots' deep-kraft sight
lines draw to the slide (not the speaker) in B02; the outline card's five
slide rows draw in and the approval check lands in B03; the outline card
slides left as slide one drops in, with the arrow and a check, in B04;
the text lines lift out of the slide and the notes card appears below in
B05; the slide shrinks to the back of the room and passes in B06; the
side-by-side reads cleanly in B07 (wall cards left, neat checked stack
right); the three-row rule card lands in B08. Confirm no motion is
mid-flight at any beat's 45–55% midpoint.

## 4. Final 4K master

```
./art final --reel how-to-ai-slides-without-the-slog
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 13 beats, ~3m33s (213 s estimated). 9 Manim scenes, all static-QC clean
  (0 warn, 0 error); 4 Remotion bookends (BIDEA, BDEFS, BHTF, BOUT).
- Skill: show-tell. No ShowTellCard kinds used — every body beat is a
  drawing (reasons in SHOTLIST.md).
- Companion: `the-long-game` — referenced once by name in B03 ("The
  outline is the contract, same as in The long game"), never re-taught.
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
