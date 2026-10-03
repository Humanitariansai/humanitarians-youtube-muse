# BUILD-LOG — claude-cookbooks--claude-liam-cookbook-audit

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-cookbooks/youtube/claude-liam-cookbook-audit/beat_sheet.json`
— a fully-built, Teardown-register `skill-teardown` sheet for the
`cookbook-audit` Anthropic Skill (`SKILL.md`, `style_guide.md`,
`validate_notebook.py`). Never touched the source reel's folder. Started
from an empty reel dir (only `SUBJECT.json` present).

**Facts kept unchanged (redo contract):** a skill is a folder Claude reads
before it works, not something it's trained on; the specific file set
(`SKILL.md` 12k, `style_guide.md` 5k, `validate_notebook.py` 17k); the
Steps mechanism (read SKILL.md, execute in order, return result); the
skill's job (audit an Anthropic Cookbook notebook against a rubric, used
whenever a notebook review or audit is requested); `validate_notebook.py`
as the falsifier that checks the same way regardless of the notebook's
content; the source's own Your Turn worked example verbatim. No AI-video,
pantry, or human-drop beats — B01–B03 are Manim GRAPHIC, B00/BCRY/BHTF/BOUT
are Remotion, per the NO-GENAI/NO-PANTRY LAW (source B00 was already
`ClaudeComposerAsk` REMOTION, not AI-video/pantry, so no substitution was
needed there beyond the mandatory WRITER LAW swap).

**Added, since the source had none:** a dedicated BCRY carry-out beat
(`WantQuote`), invented per CARRY-OUT LAW and folded from the source's B03
"design tell" language, with the Teardown verdict framing ("what it gets
right / what it bites") replaced by a Plain statement of mechanism + limit.

**B00 WRITER LAW:** typed text "How do I get Claude to judge my notebook?",
trigger "judge" → replacement "audit" — the reel's actual misconception
(that auditing a notebook is Claude forming a by-feel impression, corrected
at B01: "the file is the program"). Narration 27 words + `lead_silence_s`
0.8. Render measures 8.43s — just under the 9s guideline figure but frame
inspection confirms the typing completes with the corrected question ("...
to audit my notebook?") fully legible and cursor-terminated at t=8.2s of
8.43s (pulled frames at 4.0s, 7.5s, 8.2s — the correction is mid-flight at
7.5s and complete at 8.2s). Logged as a knowing, verified deviation from
the guideline number, same pattern as the `applying-brand-guidelines`
sibling reel.

**Audio:** `generate_audio_kokoro.py` — 7/7 beats, $0.00, am_onyx. Measured
durations: B00 8.43s, B01 17.11s, B02 15.70s, B03 22.55s, BCRY 10.90s,
BHTF 17.34s, BOUT 3.14s (+1.0s tail_silence_s).

**Render:** `remotion_scenes.py` (foreground, ran to completion across two
invocations — the tool's own timeout cut off mid-run twice, each time
after one beat had rendered; re-invoking picked up where it left off and
skipped already-filled beats) — B00/BCRY/BHTF/BOUT. `render_scenes.py`
(Manim, foreground, single run) — B01/B02/B03, all three ok on first
render, no FAILs.

**Compile:** `compile.py --review` → `-slate.mp4` (96.2s) first, to
confirm the cut before committing to a native 4K pass; then `compile.py`
(no `--review`) → clean master forced to 3840×2160 by THE 4K LAW (no real
slates present, so the clean master compiled directly) →
`claude-cookbooks--claude-liam-cookbook-audit.mp4`, 96.18s,
mean_volume -24.0 dB, max -2.9 dB.

**GATE T** (`type_check.py`): PASS, 0 FAILs, first pass — no iteration
needed.

**Gate V:** read the QC contact sheet (all 7 beats) plus direct frame
pulls at BHTF (t=80s) and BOUT (t=93.5s) confirming the `@HumanitariansAI`
folder label and subscribe/handle skin render correctly (not the
`ClaudeComposerAsk` Root.tsx `@NikBearBrown` default); a frame pull mid-B03
(t=50s) confirmed the anchor-returns pipeline animates as designed after
the QC contact-sheet thumbnail for that beat looked like a flat black
frame (it was mid-transition, not a render defect). No blockers.

**Audio presence:** `ffmpeg -af volumedetect` on the final master:
mean_volume **-24.0 dB**, max -2.9 dB — comfortably above the -40 dB
floor. `ffprobe` confirms an audio stream; master mtime (06:03) newer
than beat_sheet.json (05:58).

**Playlist:** `SUBJECT.json`'s `family` is `claude-cookbooks`, which has no
literal prefix entry in `skills/make/hai-simple/loop/playlists.json`'s
map. Per the fallback rule ("match family, or the hai-simple prefix"), the
`skill` field (`"hai-simple"`) IS a direct key in the map → **"Claude
Basics"** (matches the `applying-brand-guidelines` sibling's resolution;
the earlier `analyzing-financial-statements` sibling used the incorrect
`_default` fallback instead — not repeated here).

Metadata file written: `claude-cookbooks--claude-liam-cookbook-audit.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**, direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K + deliver.py) in this same invocation.

## 2026-08-29 — Phase 4 delivery

The clean master compiled above is already native 3840×2160 (THE 4K LAW in
`compile.py` forces any clean, non-`--review` master to 4K), so the
Fellows-facing 4K file is the same render, copied to the `-4k` filename
`deliver.py` expects:

```
cp claude-cookbooks--claude-liam-cookbook-audit.mp4 \
   claude-cookbooks--claude-liam-cookbook-audit-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged to `DELIVERY/claude-cookbooks--claude-liam-cookbook-audit/` (4K
master + description) and committed the text artifacts (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to
`claude-bear/claude-cookbooks--claude-liam-cookbook-audit/` in the
humanitarians-youtube clone.

**Status: DELIVERED.**
