# BUILD-LOG — claude-for-legal--claude-liam-clearance

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-clearance/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):** the
source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated 2026-07-25) but
its narration text carries literal, never-filled template placeholders (`>`) at every
point where the actual skill-specific fact should be: `"The skill is clearance. >."`,
`"Claude's job: >."`, `SkillTeardownMechanism.body` left as `">"`,
`ClaudeVerdictArtifact.artifactLines` includes a bare `">"`, `"I want to >."`. Its
`source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ip-legal/skills/clearance/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor an
`ip-legal` folder exists anywhere. Same defect class as the `ai-inventory` /
`ai-tool-handoff` / `aia-generation` / `amendment-history` siblings already delivered
in this family.

**The call:** reconstructed a generic, defensible account of what an IP clearance
skill does — screen a proposed name/mark against a checklist of sources and criteria a
SKILL.md defines, return a structured clearance report — per the fresh-script Phase 1
rule ("when in doubt, describe behavior generically"). No fact in the resulting script
is Claude-specific, database-specific, or a legal-outcome claim; the central fact (a
screening checklist is not a legal sign-off) holds regardless of the exact source text.

**What changed vs. source (per redo contract):**

- **Register:** Teardown → Plain. Source's B03 opened "Here is the Teardown moment"
  and BVDT carried a "Verdict" artifact label with "what it gets right / what it
  bites" framing. This build's B03 states the same class of constraint (screening
  checklist, flag matches) without a design-tell frame, and BCRY carries the fact as
  a plain carry-out sentence.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`. Writer types
  the newcomer's wrong-guess word "APPROVE" (implying Claude issues a final legal
  clearance decision), hesitates, corrects to "screen" → lands "Can Claude screen my
  trademark for use?". Picked up directly by B03's stated scope and BCRY's carry-out.
- **Beat count:** kept the source's 7-beat shape in substance (B00 → B01 anatomy → B02
  pipeline → B03 mechanism → BVDT/BCRY carry-out → BHTF handoff → BOUT outro), plus the
  fixed hai-simple outro split (`ClaudeTitleOutro` → `OutroSeries` + `OutroCTA`), 7 → 8
  beats — same restructuring precedent as every sibling in this family.
- **Facts/argument:** reconstructed per the source-gap finding above (no real facts to
  carry over). B01's file size (26k) and B02's phase labels were already filled in the
  source's own REMOTION props (not placeholders) and are kept verbatim.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is a new, complete first-person Claude prompt
  (the source's own handoff was an unfilled `"I want to >."` template) using the same
  "explain your input requirements before you act" clause the family's other redos use.

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`), so this redo reuses the same REMOTION components rather than
converting to Manim/GRAPHIC — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. `compile.py`'s motion-histogram WARNING (`remotion` 8/8 = 100%, over
the ~40% pantry cap) is expected and accepted for the same reason every prior
all-REMOTION sibling logged it (e.g. `claude-for-legal--claude-liam-brief-section-drafter`):
NO-GENAI/NO-PANTRY LAW forces every beat to GRAPHIC or REMOTION, and this reel's body
legitimately has no illustrative-figure beats to draw as Manim — it is a
file/pipeline/constraint explainer, not a worked-example narrative.

## Gates

- **TYPECHECK / GATE T:** one flag, confirmed false positive: `[BOUT/eyebrow] text
  ends truncated: 'CLAUDE BASICS · HUMANITARIANS AI'` — the middle-dot `·` character
  triggers the §8.9 truncation heuristic. Identical string, unfixed, already shipped in
  the DELIVERED `brief-section-drafter` and `legal-finance` siblings; left as-is per
  that precedent rather than reworded away from house style. 0 pixel-beat FAILs, 0
  shape FAILs.
- **TIMING LAW (B00):** narration 33 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **10.7s**, clears the ≥8s floor. Late frame pull (t=9.5s)
  confirms the full corrected question "Can Claude screen / my trademark / for use?"
  on screen with the correction landed.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (ffmpeg volumedetect, verified
  independently of `compile.py`'s own report), max -2.9 dB — well above the -40 dB
  floor.
- **Gate V (frame QC):** pulled 14 frames every 5s across the full 70.5s runtime, plus
  a targeted pull at t=69.5s for BCTA. All 8 beats legible, correctly kerned, no text
  overlap, safe inset respected. `OutroSeries`/`OutroCTA` render on flat white rather
  than the humanitarians cream ground — same shared-component behavior already logged
  unremarked in sibling reels (e.g. `ai-inventory`, `books--claude-liam-legal-finance`).
  `@HumanitariansAI` folderLabel explicit on BHTF.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (8/8
  beats, no violations, canvas 3840×2160).
- **COMPLETION LAW:** master mp4 mtime (1788026175) newer than beat_sheet.json mtime
  (1788026093); beat_sheet.json was never touched after the compile that produced the
  final master.

## Output

`claude-for-legal--claude-liam-clearance.mp4` — 70.5s, 8/8 beats real (no slate),
native 3840×2160 (Remotion beats render at 4K already), audible narration throughout
(mean_volume -23.9 dB, ffmpeg-verified). This is the review cut (COMPLETION LAW
satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-for-legal"` matches no
prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key fallback →
"Claude Basics" — same resolution every other delivered `claude-for-legal--*` redo in
this family has used (`ai-inventory`, `ai-tool-handoff`, `auto-updater`,
`bar-prep-questions`, `board-minutes`, `brief-section-drafter`).

Metadata file written: `claude-for-legal--claude-liam-clearance.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per the
DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.

## 2026-08-29 — Phase 4 delivery

- **4K master:** `compile.py` without `--review` enforces its 4K LAW automatically —
  wrote `claude-for-legal--claude-liam-clearance.mp4` natively at 3840x2160
  (Remotion beats were already rendered at native 4K), 70.5s, 8/8 beats real,
  mean_volume -23.9 dB. Copied to `-4k.mp4` so `deliver.py`'s `newest_master()` picks
  it as the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/claude-for-legal--claude-liam-clearance/` (4K master + description, syncs
  to Drive `Claude_Bear/` on this machine's Drive-for-desktop mount); repo
  `humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-clearance/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md +
  CARRY-OUT.md + QUESTION.md — no media). Commit `7fcb712a`, pushed clean (verified
  `git log` + `git status` against `origin/main`).

**Status: DELIVERED.**
