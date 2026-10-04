# CLAUDE-CODE-RENDER.md — Set it up once

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/set-it-up-once/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field with
Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (13 files). Persona: "Liam, in for Bear";
register: Teardown; greeting language German ("Hallo" — known-clean).
Bookend beats BIDEA/BDEFS/BHTF/BOUT render in Remotion (see §2); the 9 body
beats (B00–B08) are Manim scenes in `scenes.py`.

Pronunciation notes: spell "p-values" as heard (check with a whisper
transcript); the acronym "AI" is voiced fine. Read the BOUT line exactly:
"Set it up once. At Nik Bear Brown." — then pad BOUT with a 1.0 s silent
tail and write measured durations back to `actual_duration_s`.

## 2. Review cut

Body scenes (Manim):

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel how-to-use-ai-set-it-up-once \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Bookends (Remotion, via `runtime/scripts/remotion_scenes.py`): BIDEA uses
pattern `BrutalistHesitantWriter` (trigger "forget everything between
chats" → "start every chat already knowing me"); BDEFS uses
`ClaudeDefinitions` (terms: instructions / memory / preferences);
BHTF uses `ClaudeComposerAsk` (greeting "Your turn.", the full prompt in
`command`); BOUT uses `ClaudeTitleOutro` with `kind: "outro_voice"`.

Watch the review slate. Check: the note's drop-in lands inside the settings
panel in B01; the four good lines fit the note in B03 (line 3,
"plain English, no jargon", is the widest); the scribbles visibly spill off
the note's bottom edge in B04; the pinned note sits on the right window's
top edge in B05; the edited line "comfortable with basics" lands where
"beginner at statistics" was in B07.

Layout audit: `manim_layout_audit.py --curve-strict` could NOT be run in the
build VM (no Manim/pangocairo installed) — run it on the Mac for every scene
class before the 4K render. The static gate passed 9/9 clean, 0 warn, 0 error
(see CHECKS-REPORT.md).

## 3. Final 4K master

```
./art final --reel how-to-use-ai-set-it-up-once
```

## 4. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 13 beats, ~3m31s (211 s estimated). 9 Manim scenes, all static-QC clean
  (0 warn, 0 error); 4 Remotion bookends. No ShowTellCard used (zero cards —
  the card test failed for every body beat; see SHOTLIST.md).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
