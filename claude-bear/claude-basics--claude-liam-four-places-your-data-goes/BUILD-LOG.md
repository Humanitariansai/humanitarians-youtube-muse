# BUILD-LOG — claude-basics--claude-liam-four-places-your-data-goes

## 2026-08-28 — review cut, DONE (continuing a prior interrupted pass)

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/claude-basics/claude-liam-four-places-your-data-goes/beat_sheet.json`
(a fully-built Teardown-register, `ai-explainer` reel, `@NikBearBrown`).
Question, facts, and beat count (26) carried over unchanged: one detail typed
into an AI lands in four stacked places — the conversation, product memory,
provider systems, training — ranked by reversibility, not secrecy. B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW): "I told an AI where I live. Can I
delete it?" hesitates on "delete" and corrects to "undo." Register
re-registered Teardown->Plain: two design-judgment clauses cut (B14's "that's
not sinister, it's operational"; B21's "beats any blanket policy" comparison)
— facts unchanged, only the verdict-flavored language removed. Close/outro
re-skinned from `ClaudeTitleOutro`/@NikBearBrown to `OutroCTA`/@HumanitariansAI
with Liam's sign-off; BVDT's artifact heading changed from "The verdict" to
"In short" (same recap lines). Body beats B01-B22/BVDT reuse the source's
`ClaudeDescent`/`ClaudeMemoryReread`/`ClaudeVerdictArtifact` REMOTION
components unchanged in visual grammar — they were already valid REMOTION
(never AI-video, pantry, or human-drop), so NO-GENAI/NO-PANTRY LAW required
no substitution beyond B00; only `folderLabel` updated to `@HumanitariansAI`
throughout. Full redo audit and register audit in SCRIPT.md.

**State on picking this reel back up:** SCRIPT.md, beat_sheet.json, CARRY-OUT.md,
QUESTION.md, and all 26 beats' audio (mp3/) and video (media/ + manim/B17) were
already present from a prior invocation, including a documented B00 fix (the
original `triggerWords: "delete it"` was a two-word phrase that could never
match — `BrutalistHesitantWriter` matches single whitespace-split tokens —
silently never firing the correction; already corrected to single-word
`"delete"` -> `"undo"` and confirmed on a frame pull). A master mp4 already
existed but its file mtime (03:07) predated several of the media renders in
`media/` (B08 through B21 render up to 03:43) — per the COMPLETION LAW that
master was stale, not a finished cut, regardless of its apparent completeness.

Action taken this invocation:

1. Verified all 26 beats present and matching beat_sheet.json (B00-B22 +
   B17 manim, BVDT, BHTF, BOUT — no missing slots).
2. Recompiled: `python3 runtime/scripts/compile.py <REEL_DIR>` (foreground,
   waited on exit code via TaskOutput after the shell auto-backgrounded it
   past the 120s default timeout — never treated the background move as a
   turn-ending event). `compile.py`'s 4K LAW forced the clean master
   (no slates) straight to 2160p.
3. Confirmed the new master is newer than beat_sheet.json: mp4 mtime
   1787903380 > beat_sheet.json mtime 1787903270.
4. Gate V: pulled 33 frames at 8s spacing across the full 260.36s runtime and
   read a representative spread (cold-open correction, three-facts card,
   the four-level descent establish/level/pullback shots, the Training level,
   the pullback "price the worst case," the Your Turn composer, the outro).
   All legible, humanitarians palette (cream ground, terracotta asterisk
   accent, serif ink) on the cold open/pullback/outro beats, Claude-fidelity
   palette on the body `ClaudeDescent`/`ClaudeComposerAsk` beats (expected —
   see SCRIPT.md's "Known mixed-skin note": those components have no
   ink/accent/bg prop override and were not one of the three things this
   skill changes). No text overlap, no off-canvas text, safe inset respected
   throughout. No blockers found.

**Gates:**
- content-check: PASS (26 beats, no violations)
- frame-check: PASS (3840x2160, 26 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py, prior pass): PASS, 0 FAILs across all beats
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840x2160, audio present, duration 260.36s; mp4 mtime newer
  than beat_sheet.json mtime (confirmed above)

**Non-blocking warning (compile.py):** motion histogram remotion:25
manim:1 — remotion at 96% of beats, over the ~40% pantry cap in MOTION.md.
Structural, not a defect introduced this invocation: this redo preserves the
source reel's beat-for-beat structure and component choices exactly (per
hai-simple's redo-mode contract — same question, same beat count, same body
mechanism), and the source was already almost entirely `ClaudeDescent`/
`ClaudeComposerAsk`/`ClaudeMemoryReread` REMOTION shots with a single Manim
beat (B17). Reworking the body's rendering language would mean rewriting the
source's visual grammar, which redo-mode does not authorize. Logged per the
honesty rule rather than silently reworking beat count/lane mix to dodge the
warning.

Metadata file written: `claude-basics--claude-liam-four-places-your-data-goes.md`
(channel @HumanitariansAI, Playlist: **Claude Basics** — resolved from
`skills/make/hai-simple/loop/playlists.json` via the `claude-basics` family
prefix — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-28 — Phase 4 delivery

Master is already 3840x2160 (compile.py's 4K LAW forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-basics--claude-liam-four-places-your-data-goes.mp4 \
   claude-basics--claude-liam-four-places-your-data-goes-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged to `DELIVERY/claude-basics--claude-liam-four-places-your-data-goes/`
(4K master + description) and committed + pushed the text artifacts
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
BUILD-LOG.md, CARRY-OUT.md, QUESTION.md — no media) to
`claude-bear/claude-basics--claude-liam-four-places-your-data-goes/` in the
humanitarians-youtube clone: commit `91e71098`, pushed clean (`git status
--short` empty, `main...origin/main` in sync after).

**Status: DELIVERED.**
