# CLAUDE-CODE-RENDER.md — Muse Does the Assignment

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`, then:

```
cd muse/youtube/claude-liam-lecture-muse-does-the-assignment/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B01.mp3` … `audio/B14.mp3`, `audio/BVDT.mp3`, `audio/BHTF.mp3`,
`audio/BOUT.mp3` (19 files). Persona: "Liam, in for Bear"; register:
Teardown. Greeting note: BIDEA opens "Hallo." (Kokoro says it cleanly — do
not substitute "Hej"). Course note: BIDEA names "INFO 6205" (reads as "info
sixty-two oh five" — checked, keep). Read the BOUT line exactly:
"Muse Does the Assignment. Liam, in for Bear. At Nik Bear Brown."

Kokoro-safety notes, verified at build time:
- "BFS" is spoken as letters (bee-eff-ess) — whisper-check BDEFS and B04.
- "NP-hard" is on the known-clean list — whisper-check B11 anyway.
- B08's terminal lines are verbatim test output ("25 passed, 0 failed" /
  "ALL TESTS PASSED") — read exactly, including the numerals.
- The BHTF prompt must be read in full, exactly as written in the beat
  sheet, pausing slightly before and after the quoted prompt.

## 2. Pre-render QC (Mac only — could not run in the build VM)

`manim_layout_audit.py --curve-strict` needs Manim/pangocairo and was
NOT run during the build (the build VM has neither). Before the review
cut, run it per scene class from the reel folder:

```
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B01_Grid --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B02_Rules --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B03_Example --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B04_Legs --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B05_Order --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B06_Twelve --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B07_States --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B08_Crosscheck --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B09_Greedy --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B10_Trap --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B11_Wall --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B12_Rule --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B13_SixVsTwelve --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B14_Fixes --curve-strict
```

Note: the static render-free gate passed 14/14 clean in the build VM; the
fixes made for it (overlay highlights instead of in-place fills, drawn check
marks, explicit boxes, hand-built 2^K curve) are render-identical or better
in real Manim.

## 3. Render

```
./brutalist.art/art run muse/youtube/claude-liam-lecture-muse-does-the-assignment --height 2160
```

Manim scenes render for real; the 5 Remotion bookends (BIDEA, BDEFS, BVDT,
BHTF, BOUT) render on the Mac (they were labeled slates in the VM cut).

## 4. Final

```
./brutalist.art/art final muse/youtube/claude-liam-lecture-muse-does-the-assignment --height 2160 --out <reel>/exports/landscape
```

Check the master: 3840×2160, runtime equals the sum of the audio, 1.0 s
silent tail after the outro. `python3 brutalist.art/runtime/scripts/bookend_check.py <reel>`.

Never publish without Bear's explicit instruction.
