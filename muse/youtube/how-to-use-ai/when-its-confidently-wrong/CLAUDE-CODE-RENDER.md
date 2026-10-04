# CLAUDE-CODE-RENDER.md — When it's confidently wrong.

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/when-its-confidently-wrong/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`,
`FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `line` field with Kokoro
voice `am_onyx`. Save as `audio/B00.mp3`, `audio/B01.mp3`, …,
`audio/BOUT.mp3` (14 files). Persona: "Liam, in for Bear"; register:
Teardown. Greeting "Hallo" opens B00 — whisper-check it (known-clean
Kokoro greetings include Hallo). Read the BOUT line exactly: "When it's
confidently wrong. Liam, in for Bear. At Nik Bear Brown. Thanks for
watching."

## 2. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel when-its-confidently-wrong \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the ask types into the composer in M01;
the strike-through crosses "argue harder" in M02; the confidence gauge
fills to full in M04; the insist loop draws in M05; the fluency gauge
fills while the fact-check gauge sits empty in M06; the old chat gets
its X in M07; the magnifier sweeps the source card in M08; the "March
2019?" claim is boxed and crossed in M09; the four panels each take a
check in M11; the terracotta rule draws under the title in M14.

## 3. Type and layout audit

Run on the Mac (cannot run in this VM — no Manim/pangocairo here):

```
python3 runtime/qc/manim_layout_audit.py --curve-strict
```

This checks per-rendered-frame type size, overflow, contrast, kerning,
and layout curves. Fix any FAIL before the final master.

## 4. Final 4K master

```
./art final --reel when-its-confidently-wrong
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 14 beats, ~5m17s. 14 scenes, all static-QC clean (0 warn, 0 error).
- Skill: ai-explainer (switched from the suggested deep-explainer; see
  BUILD-LOG.md) — zero cards, all drawings; the chat window is the
  recurring cast object.
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
