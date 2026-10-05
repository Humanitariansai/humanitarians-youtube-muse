# CLAUDE-CODE-RENDER.md — Your Language Coach

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`, then:

```
cd muse/youtube/how-to-use-ai/your-language-coach/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (11 files). Persona: "Liam, in for
Bear"; register: Teardown. Greeting note: BIDEA opens "Hallo." (Kokoro
says it cleanly — do not substitute "Hej"). Read the BOUT line exactly:
"Your Language Coach. Liam, in for Bear. At Nik Bear Brown."

Kokoro-safety notes, verified at build time:
- The narration speaks NO French. The one French rule is stated in
  English ("I have twelve years"). Do not "improve" this by voicing
  French — Kokoro voices it with English phonemes.
- The hello pills ("hola", "bonjour", "konnichiwa", "salaam") are all on
  the known-clean list; whisper-check B06 anyway.
- The prompt says "cafe" without the accent — read it as written.

Read the BHTF prompt in full, exactly as written in the beat sheet
("Be my French conversation coach…"), pausing slightly before and after
the quoted prompt.

## 2. Pre-render QC (Mac only — could not run in the build VM)

`manim_layout_audit.py --curve-strict` needs Manim/pangocairo and was
NOT run during the build (the build VM has neither). Before the review
cut, run it per scene class from the reel folder:

```
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B00_Coach --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B01_Patience --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B02_Correction --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B03_Rule --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B04_Roleplay --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B05_Level --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B06_Languages --curve-strict
```

Also run `static_scene_check.py` per class from a scratch folder holding
ONLY `scenes.py` (+ `beat_sheet.json` beside it so `until()` pacing
runs) — that is exactly what `art run`'s Gate A sees. Then render each
scene's last frame at low resolution (`manim -ql -s`) and eyeball the
contact sheet, especially: the "I have twelve years" pill and rule card
in B02/B03 (text must sit inside the card), the awning posts in B04,
and the four hello pills in B06 (all inside ±6.2).

## 3. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel your-language-coach \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the naive ask is corrected to the
practice ask in BIDEA; the two bubbles face off with "you"/"coach"
labels in B00; three try-pills, two squiggles, one check, "no clock"
tag in B01; the caret striking "I am twelve" and the corrected pill
arriving with "instant" tag in B02; the rule card growing with "I have
twelve years" and "the rule" label in B03; the awning dropping and the
"coffee" pill traveling in B04; the "slower" pill shrinking the long
reply to a short one in B05; the four hello pills popping and the kraft
"tutor" card sliding in beside the coach in B06; the full coach prompt
fits the composer card in BHTF.

## 4. Final 4K master

```
./art final --reel your-language-coach
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 11 beats, ~3m44s. 7 Manim scenes (B00–B06) + 4 Remotion bookends.
  All 7 scenes static-QC clean (0 warn, 0 error); midpoint-guard
  simulation clean (0 straddles).
- Companion to `learn-anything-faster` — referenced in B06, never
  re-taught.
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
