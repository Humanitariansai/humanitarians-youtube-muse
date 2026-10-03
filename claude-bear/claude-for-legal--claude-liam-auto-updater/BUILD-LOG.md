# BUILD-LOG — claude-for-legal--claude-liam-auto-updater

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-auto-updater/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata
`register: "Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`.../claude-for-legal/legal-builder-hub/skills/auto-updater/SKILL.md` — a
path that only exists on the original build machine and is unreachable
from here). Built entirely fresh this invocation — only SUBJECT.json
existed on pickup. 7 beats — B00 cold open, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF handoff, BOUT outro.

**Source defect found on read, logged per the honesty rule:** three of the
source's seven beats carry a literal unfilled `>` character sitting exactly
where `auto-updater`'s own specific content should have been substituted
in — B00 ("The skill is auto-updater. **>**."), B03 ("Claude's job:
**>**."), BVDT ("The SKILL.md is the spec — **>**."), BHTF ("I want to
**>**."). Confirmed against `anthropics/BUILD-SKILL-EXPLAINERS-LOG.md`'s
2026-07-25 batch-build entry for `auto-updater`, which shipped straight to
"DONE ✓" with the placeholder never filled — a batch template-substitution
bug in the original pipeline, not a stylistic choice. The source therefore
never actually states what `auto-updater` specifically automates or what
its concrete steps are, and the real `SKILL.md` is unreachable from this
machine to recover them.

**What this redo keeps and what it does not invent:** every fact the
source's *readable* text establishes is kept unchanged and generalized —
a Skill is a folder Claude reads before acting; its `SKILL.md` is plain
sentences, not hidden logic ("the file is the program"); the pipeline lives
in a Steps section read top to bottom, linear, no branching unless a step
says so; run it twice on the same input and you get the same steps and the
same result; the guarantee holds only for what the file describes. Per
hai-simple's "when in doubt, describe behavior generically" rule, this
reel builds entirely on those generic-but-true facts about how a Claude
Skill works, using `auto-updater` only as the *name* of the example skill
— it never states what `auto-updater` specifically automates, since the
source never actually said so. Full reasoning in QUESTION.md.

B00 WRITER LAW: naive guess "model" (logic baked into the model itself,
some hidden capability) → corrected to "file" (baked into `SKILL.md`) — the
newcomer's default read of an "auto"-anything skill, falsified by B02's
concrete case (delete step 3, step 3 doesn't happen, nothing hidden fills
the gap). Anchor B01 → B03: a `SKILL.md` card with five numbered steps,
planted, then returned to and run twice with identical results before a
case outside the file shows nothing to match.

**TIMING LAW defect found and fixed at the root, not papered over:** the
first B00 render (`mistakeRate:6, hesitateWithin:3, hesitateBetween:22,
charMs:55`) reached the trigger word "model" fully typed by ~t=10.2s of the
11.29s beat, then froze there for the rest of the clip — the seeded
performance's post-correction sequence (1000-1500ms decision pause + 5
backspaces + 4-char retype + tail punctuation + final pause, ≈2.5s) did not
fit in the ~1.1s remaining before the composition's audio-driven duration
ran out. Verified directly: frames pulled at t=9.5/10.2/10.6/10.9/11.1s all
showed "model" static in terracotta, never resolving to "file" — this is
exactly the pilot-era bug the skill's TIMING LAW section warns about, just
manifesting at the *end* of the correction instead of never reaching it.
Fixed by speeding up the typing performance itself (`mistakeRate 6→3,
hesitateWithin 3→2, hesitateBetween 22→10, charMs 55→38, jitter 26→22`,
same seed) so the full performance — including the correction — completes
with margin; re-rendered, re-verified by frame pull at t=9.0s: the
corrected final text "into the file?" is already resting in ink color a
full 2.3s before the beat ends. `media/B00.mp4` = 11.3s (clears the ≥8s
TIMING LAW window).

**Gate V defect found and fixed at the root:** first full frame-pull pass
(1/8 fps across the 95.3s runtime, all 12 frames read directly) caught a
real card-clip defect in B02 — the "only if the / step says so" annotation
was set inside a fixed small square (`RegularPolygon(n=4).scale(0.55)`)
sized for a short label, not two lines of prose; text visibly overflowed
past the box's left/right/top edges. Fixed at the root in `scenes.py`:
replaced the fixed square with `SurroundingRectangle` sized from the text
object itself plus padding, so the box always fits its content. Re-rendered
B02 only, recompiled, reconfirmed clean by direct frame crop at the same
timestamp — text now sits fully inside the box with margin on all sides.

All 3 GRAPHIC beats (B01/B02/B03) built on one shared custom Manim
`scenes.py`/`render_scenes.py` (humanitarians palette #F3EBDD/#2F2A26/
#E4572E/#1F4E5F), one scene class per beat, same pattern as the
`claude-code--claude-liam-plugin-structure` sibling. No source beat was
ai-video-prompt, pantry, or a human-drop slot — the source's original build
was already entirely REMOTION (`ClaudeComposerAsk`/`SkillTeardownAnatomy`/
`SkillTeardownPipeline`/`SkillTeardownMechanism`/`ClaudeVerdictArtifact`/
`ClaudeTitleOutro`) — NO-GENAI/NO-PANTRY LAW required no substitution
beyond the WRITER LAW swap at B00.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (B00
re-rendered once with `--only B00 --force` after the TIMING LAW fix); all 3
GRAPHIC beats rendered via `render_scenes.py` (B02 re-rendered once after
the card-clip fix). Compiled twice (once per fix) via:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-for-legal--claude-liam-auto-updater.mp4`, 7/7 beats filled
real (no slate), 95.3s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (re-run clean after both fixes)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 95.33s; mp4
  mtime (1788008459) newer than beat_sheet.json mtime (1788008110)
- Gate V (visual): pulled 12 frames at 8s spacing across the full 95.3s
  runtime plus targeted frame pulls of B00 (correction verified resting by
  t≈9.0s, 2.3s margin before beat end) and B02 (card-clip fix verified by
  direct crop). No remaining blockers: legible everywhere, safe inset
  respected, no text overlap, correct @HumanitariansAI handle and title on
  BHTF/BOUT.

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape (B00 writer + BCRY + BHTF + BOUT all REMOTION)
against 3 GRAPHIC body beats for this 7-beat reel — same disposition as
every other short hai-simple reel in this family (e.g.
`claude-code--claude-liam-plugin-structure`). Manim clips were time-
stretched by compile.py to fill their measured audio durations (B01 8.8s→
17.6s at 2.01x, B02 10.7s→16.2s at 1.51x, B03 10.6s→19.6s at 1.85x);
spot-checked in the Gate V frame pull, no visible artifacting (static-
camera compositions, no fast motion to stretch).

**Cosmetic note carried from sibling precedent:** `OutroCTA` renders on its
own hardcoded white ground, not the humanitarians cream — no color prop
exists on the component. Same known seam already logged on multiple
`claude-liam-*`/hai-simple siblings; not fixed here for the same reason (no
prop to fix it with).

Metadata file written: `claude-for-legal--claude-liam-auto-updater.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
playlists.json, `claude-for-legal` has no literal map entry, but `hai-simple`
(this reel's `skill` field) IS a literal map key → "Claude Basics" — this
resolves before any content-matching or `_default` fallback per the match
order (family, then the `hai-simple` prefix, then `_default`). First draft
of this log had reasoned toward "Extending Claude — Skills, Plugins &
Connectors" by content analogy to the unrelated `books--claude-liam-support`
override; caught before delivery by checking sibling precedent within THIS
family directly — every other delivered `claude-for-legal--*` redo facing
the identical unfilled-template defect (`ai-inventory`, `ai-tool-handoff`)
already used "Claude Basics" via the skill-key fallback, none overrode it.
Corrected to match for consistency across the family. `beat_sheet.json`'s
own `metadata.playlist` field was already stamped ("Extending Claude —
Skills, Plugins & Connectors") by the time this was caught, after the
final compile — left as-is per COMPLETION LAW (never touch beat_sheet.json
after compiling; playlist is pure metadata, not rendered into any frame,
so this is a harmless cosmetic mismatch, same disposition already logged
on the `creating-financial-models` sibling for the identical situation).
The `.md` file above and this log carry the corrected value. Direct code
link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-29 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-for-legal--claude-liam-auto-updater-4k.mp4` rather than
re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-for-legal--claude-liam-auto-updater/` (4K master +
description) for the Drive sync. Committed to
`claude-bear/claude-for-legal--claude-liam-auto-updater/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4/scenes.py media-adjacent scripts
beyond what deliver.py stages) in the humanitarians-youtube clone, pushed.

**Status: DELIVERED.**
