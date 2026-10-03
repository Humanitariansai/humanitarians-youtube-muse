# BUILD-LOG — claude-code--claude-liam-claude-opus-4-5-migration

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-code/youtube/claude-liam-claude-opus-4-5-migration/beat_sheet.json`
(Teardown reel documenting the `claude-opus-4-5-migration` Claude Code plugin
skill, already fully built, 7 beats, no SCRIPT.md — source
`beats[*].narration_text` served as the locked script). Built entirely fresh
this invocation — only SUBJECT.json existed on pickup (the
`/Users/bear/...` source path in SUBJECT.json does not exist on this
machine; the same reel exists locally at
`anthropics/claude-code/youtube/claude-liam-claude-opus-4-5-migration/`, used
as the actual source).

Question, facts, and full body argument carried over unchanged: the four
target platforms and exact model strings (Anthropic API
`claude-opus-4-5-20251101`, AWS Bedrock
`anthropic.claude-opus-4-5-20251101-v1:0`, Google Vertex AI
`claude-opus-4-5@20251101`, Azure AI Foundry `claude-opus-4-5-20251101`), the
three source models (Sonnet 4.0, Sonnet 4.5, Opus 4.1), the explicit Haiku
exclusion, the six-step workflow (search → update strings → remove the
`context-1m-2025-08-07` beta header → add `effort: high` → summarize → offer
to help with prompt adjustments), and the opt-in-only discipline for the
five behavioral-adjustment triggers (tool overtriggering, over-engineering,
code exploration, frontend design, thinking sensitivity — represented by
their governing rule at NB10 rather than listed individually, to keep Plain
mechanism rather than Teardown inventory).

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "upgrade" → "migrate" — the
newcomer's wrong guess that migrating a model also means Claude tunes
prompts/behavior for the new model, corrected toward the actual narrow
mechanism). Register re-registered Teardown → Plain: the source's B05/BVDT
"gets right" / "bites" verdict recap (Azure source-table gap, vague
triggers, no rollback guidance, effort.md external dependency) was dropped
entirely — no design judgment carried over — and replaced by this register's
own required shape: a wrong-guess beat (NB02) broken by a case (NB03), one
anchor planted and paid off (NB04 → NB08, the same model-call line before
and after migration), and a both-directions pair (NB09 clean case / NB10
opt-in-only case) built from the source's own scope rules rather than a
verdict. Close re-skinned to `WantQuote` / `ClaudeComposerAsk` / `OutroCTA`
with @HumanitariansAI and Liam's sign-off. Source's dense 2-beat mechanism
(B01 platform matrix + six-step workflow, B02 five behavioral triggers) was
split into 10 single-idea Plain beats (NB01–NB10) per hai-simple's
one-idea-per-beat rule. Full audit in SCRIPT.md's "Beat-count note (redo)"
section. Net: 14 beats (B00 + 10 body + BCRY/BHTF/BOUT), full body argument
preserved, no fact dropped, judgment removed.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's only beat needing replacement was B00 (`ClaudeComposerAsk`,
REMOTION already, swapped for `BrutalistHesitantWriter` per WRITER LAW). All
10 GRAPHIC beats built on one shared "chip row" Manim template
(`scenes.py`/`render_scenes.py`) plus a second "code card" template built
for this reel's anchor (`render_code_card`) — the anchor is a single
model-call line shown before migration (NB04) and after (NB08), same card
frame both times, so the payoff reads as literally the same line returning.

Audio generated fresh (`generate_audio_kokoro.py`, all 14 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground; the initial invocation exceeded the tool's 120s timeout and
was auto-backgrounded — waited on the process directly via `pgrep` rather
than ending the turn, per this skill's one-shot/foreground-render rule, and
confirmed exit 0 with all 4 beats OK before continuing); all 10 GRAPHIC
beats rendered via `render_scenes.py`. First `type_check.py` pass was FAIL
(1 defect):

- **min-size §8.1, NB02** — the 2-chip row's chip-width formula capped
  chip width at the same 3.2-unit ceiling used for 3–4 chip rows, forcing
  the long label "SMOOTHED-OVER BEHAVIOR" to scale down past the legibility
  floor (16px < 20px floor). Root-caused to `scenes.py`'s
  `render_chip_row`: a 2-chip row has far more spare width than a 3–4 chip
  row but was using the same cap. Fixed by widening the cap to 5.4 units
  for rows of 1–2 chips (`cap = 3.2 if n >= 3 else 5.4`); re-rendered NB02
  and NB06 (the only two 2-chip beats) and recompiled.

`type_check.py` went 1→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-code--claude-liam-claude-opus-4-5-migration.mp4`, 14/14
beats filled real (no slate), 144.4s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (14 beats, no violations)
- frame-check: PASS (3840×2160, 14 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see defect + fix above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 144.44s; mp4
  mtime (01:05) newer than beat_sheet.json mtime (00:55)
- Gate V (visual): pulled frames every 10s across the full 144s runtime plus
  a targeted end-frame pull for BOUT. No blockers: every chip row legible,
  both anchor code cards (NB04/NB08) render the same frame with the correct
  before/after code, correct @HumanitariansAI handle throughout, correct
  title/subline in BHTF and BOUT, HAI outro skin present. B00's correction
  ("upgrade" → "migrate") confirmed already on screen by t=10s of the
  12.1s beat, comfortably within the visible-correction window.
- B00 TIMING LAW: `actual_duration_s` 12.1s (≥8s requirement comfortably
  met, no `lead_silence_s` padding needed beyond the authored 0.8s).

**Non-blocking warning (compile.py):** motion histogram graphic:10
remotion:4 — graphic at 71%, over the ~40% pantry cap in MOTION.md.
Structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as REMOTION
against a 10-beat GRAPHIC body carried over from the source's mechanism
argument — the ratio follows beat count, not a choice made in this build.
Same disposition as every sibling in HAILOOP-LOG.md. Logged per the honesty
rule rather than reworking beat count to dodge the warning.

**Cosmetic note carried from sibling precedent:** `OutroCTA` renders on its
own hardcoded white ground, not the humanitarians cream — no color props
exist on the component. Same known seam already logged on multiple
`books--claude-liam-*` and other hai-simple siblings; not fixed here for the
same reason (no prop to fix it with).

Metadata file written:
`claude-code--claude-liam-claude-opus-4-5-migration.md` (channel
@HumanitariansAI, **Playlist: Claude Code** — `family: "claude-code"` maps
directly to "Claude Code" in playlists.json, no fallback reasoning needed).
Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
