# BUILD-LOG — claude-for-legal--claude-liam-cease-desist

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-cease-desist/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `cease-desist` legal
Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a Skill is
a folder Claude reads before it acts, holding one instruction file
(SKILL.md) written in plain language with no hidden logic; the pipeline is
linear — read the file, execute each step in order, return the result, no
branching unless a step says so; one specific rule governs the
cease-desist Skill in particular — the internal draft, the pre-send brief,
and the triage memo are all marked attorney work product, but the outgoing
letter is not, because it's written for the other side rather than kept as
an internal file; and the limit — Claude executes reliably, but only does
what the SKILL.md says. B00 replaced the source's `ClaudeComposerAsk`
puppet-handoff cold open with `BrutalistHesitantWriter` (WRITER LAW:
"deciding" → "following steps" — the newcomer's wrong guess that Claude
uses its own legal judgment, corrected toward the actual mechanism: a fixed
file, followed step by step). Register re-registered Teardown→Plain: the
source's "design tell"/"deliberate trade-off" framing (B03) was
re-expressed as a plain mechanism description with no judgment on whether
the design choice was good; BVDT's two verdict facts (reliable execution,
file-only limit) were merged into the single BCRY carry-out sentence rather
than kept as a separate bulleted artifact card, per CARRY-OUT LAW. Close
re-skinned to @HumanitariansAI (see OutroSeries deviation below).

**Beat count discipline:** source is the shortest of the `claude-liam-*`
Teardown family — 7 beats (B00 + B01/B02/B03 anatomy-pipeline-design-tell +
BVDT verdict + BHTF your-turn + BOUT outro), a single-example skill
walkthrough with no wrong-guess, anchor, or both-directions beats of its own
to redistribute (unlike richer deep-explainer sources on other
`claude-for-legal`/`books--` siblings). This redo kept the same 7-beat
shape rather than inventing extra structure beats: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02, B03→NB03 stayed one beat each; BVDT folded into BCRY; BHTF kept,
with the source's bracketed placeholder ("I want to >") replaced by a
concrete, paste-ready scenario so the prompt is actually runnable today;
BOUT kept. Full audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`, one title + up to 4 labeled
chips + optional arrows/accent/strike + caption) copied verbatim from the
`books--claude-liam-support` sibling. B00 hesitant-writer correction
("deciding" → "following steps") verified on screen by direct frame pull:
mid-typing at t≈4s shows "ac" with the "c" in terracotta mid-correction; by
t≈9s the settled text reads "When Claude writes a cease and desist, is it
following steps?" — full clip 9.83s (≥8s TIMING LAW window met).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`; NB01–NB03
rendered via `render_scenes.py`. First `type_check.py` pass was **FAIL, 2
defects** — both fixed at the root, not by loosening the checker:

- **min-size §8.1, NB03** — the third chip's original label ("OUTGOING
  LETTER: not marked", 27 chars) forced a much smaller auto-fit scale than
  its two siblings ("DRAFT: marked" / "BRIEF: marked"), rendering
  genuinely cramped at 9px. Verified by direct frame crop: visibly smaller
  and harder to read than the other two chips, a real defect, not a false
  positive. Fixed by shortening all three chip labels to parallel length
  ("INTERNAL DRAFT" / "TRIAGE MEMO" / "OUTGOING LETTER", 14–15 chars each)
  so none needs the aggressive scale-down; re-rendered, re-measured
  22px ≥ 20px floor, and re-confirmed by frame pull that all three chips
  now read at consistent size. `beat_sheet.json`'s
  `graphic.production_viz.chips` for NB03 was synced to the fixed wording
  before the recompile, per COMPLETION LAW.
- **min-size §8.1, BOUT (`OutroCTA`)** — reproducibly measured a 38px
  text-run (<41px floor) on this reel's exact render, verified by direct
  pixel/connected-component analysis against `type_check.py`'s own
  `check_min_size`/`text_run_bboxes` functions: the checker takes the *min*
  height across every individual glyph blob on the frame (it does not
  group letters into words), and a lowercase x-height letter inside the
  fixed-font-size `@HumanitariansAI` handle text measured 35–38px on this
  render — while the same component with the same handle string measured
  a single 155px merged blob on the `books--claude-liam-support` sibling's
  BOUT (confirmed by running `check_min_size` directly against both mp4s
  side by side). A forced re-render of `OutroCTA` with identical props
  reproduced the identical 38px result deterministically, ruling out
  transient encoding noise — this is real per-render glyph-blob
  segmentation variance in a shared, prop-less component (no font-size
  prop exists on `OutroCTA` to fix at the content level), and no
  `MIN_SIZE_EXEMPT_PATTERNS` mechanism exists in `type_check.py` to extend
  (unlike the kerning/bbox-overlap checks, which do have one) — adding one
  would be inventing a new exemption category for a shared validator, not
  applying an established one. Rather than loosen the validator, switched
  BOUT to hai-simple's other sanctioned HAI outro pattern, `OutroSeries`
  (per hai-simple SKILL.md: "renders via Remotion OutroSeries / OutroCTA"),
  which carries no small fixed-size handle text at all (eyebrow + serif
  line only, both large). Confirmed clean by direct frame read (legible,
  no truncation) and by GATE T: PASS.

`type_check.py` went 2→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-for-legal--claude-liam-cease-desist.mp4`, 7/7 beats filled
real (no slate), 76.4s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 2 defects + fixes above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 76.42s; mp4
  mtime (1788020241) newer than beat_sheet.json mtime (1788020160)
- Gate V (visual): pulled frames every 8s across the full runtime plus
  targeted checks of B00 (mid-correction at t≈4s, settled+correct at
  t≈9s), NB01–NB03 (all three chips legible post-fix), BCRY (carry-out
  sentence reads clean), BHTF (correct topic/title/@HumanitariansAI handle,
  paste-ready prompt text legible), and BOUT (OutroSeries: correct eyebrow
  "CEASE-DESIST · @HumanitariansAI", correct title restate, crimson
  underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 9.83s (≥8s requirement met); the
  "deciding" → "following steps" correction lands on screen by t≈9s.

Metadata file written: `claude-for-legal--claude-liam-cease-desist.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
playlists.json, SUBJECT.json's family (`claude-for-legal`) matches no map
prefix; falling through to the `hai-simple` skill-key match (→ "Claude
Basics") per the literal instruction, consistent with the same reasoning
already logged on the `claude-for-legal--claude-liam-case-brief` sibling
(same family, same fallback, same playlist — no per-family override
convention has been established for `claude-for-legal` beyond this
skill-key default). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
