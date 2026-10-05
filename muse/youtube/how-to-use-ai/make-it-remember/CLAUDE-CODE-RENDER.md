# CLAUDE-CODE-RENDER.md — Make it remember (and forget)

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`,
then:

```
cd muse/youtube/how-to-use-ai/make-it-remember/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field with
Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (13 files). Persona: "Liam, in for Bear";
register: Teardown; greeting language German ("Hallo" — known-clean).
Bookend beats BIDEA/BDEFS/BHTF/BOUT render in Remotion (see §2); the 9 body
beats (B00–B08) are Manim scenes in `scenes.py`.

Pronunciation notes: whisper-check "café" (B00/B01/B03/B04/B05/B08),
"incognito" (BDEFS/B06), and "ID numbers" (B02 — Kokoro may read "ID" as
"id"; reword to "identity numbers" if it does). Read the BOUT line exactly:
"Make it remember (and forget). At Nik Bear Brown." — then pad BOUT with a
1.0 s silent tail and write measured durations back to `actual_duration_s`.

## 2. Review cut

Body scenes (Manim):

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel how-to-use-ai-make-it-remember \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Bookends (Remotion, via `runtime/scripts/remotion_scenes.py`): BIDEA uses
pattern `BrutalistHesitantWriter` (trigger "remember me" → "remember what
matters, forget what doesn't"); BDEFS uses `ClaudeDefinitions` (terms:
memory / topics / incognito); BHTF uses `ClaudeComposerAsk` (greeting "Your
turn.", the full prompt in `command`); BOUT uses `ClaudeTitleOutro` with
`kind: "outro_voice"`.

Watch the review slate. Check: the "café in Lisbon" card lands inside the
notebook tray in B00; the three keep-worthy cards stack without covering the
"memory" label in B01; the three terracotta X's sit centered on the banned
cards in B02; the cursor lands on the "Topics" pill in B03; the rewritten
"new office" card lands back where "old office" was in B04; the shelf line
sits under the notebook in B05; the rising incognito card meets the X before
the notebook in B06; the window and bubble fully leave in B07; the two "on"
pills land clear of the cabinet and notebook in B08.

Layout audit: `manim_layout_audit.py --curve-strict` could NOT be run in the
build VM (no Manim/pangocairo installed) — run it on the Mac for every scene
class before the 4K render. The static gate passed 9/9 clean, 0 warn, 0 error
(see CHECKS-REPORT.md).

## 3. Final 4K master

```
./art final --reel how-to-use-ai-make-it-remember
```

## 4. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 13 beats, ~3m36s (216 s estimated). 9 Manim scenes, all static-QC clean
  (0 warn, 0 error); 4 Remotion bookends. No ShowTellCard used (zero cards —
  the card test failed for every body beat; see SHOTLIST.md).
- Skill note: the assignment named cc-explainer; the film was built as
  show-tell because cc-explainer's TERMINAL-FIRST / REAL-SESSION laws cannot
  be satisfied (no terminal session exists for this topic, no `claude` CLI
  in the build VM, no credential authorized to run one). Recorded in
  BUILD-LOG.md with the same precedent as the free-vs-paid build.
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
