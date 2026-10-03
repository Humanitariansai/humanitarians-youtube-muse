# BUILD LOG — hai-simple/claude-for-legal--claude-liam-brief-section-drafter

Redo of `anthropics/claude-for-legal/youtube/claude-liam-brief-section-drafter`
(Teardown register, 7-beat skill-teardown of Anthropic's `brief-section-drafter` skill)
as `hai-simple` (Plain register, Humanitarians AI skin). Source folder untouched.
Unlike several `claude-for-legal` siblings, this source's narration was fully authored
(no unfilled `>` template placeholders) — every beat had real, specific content to
redo from.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Source's B03 opened with "Here is the Teardown
  moment" and closed with a "what it gets right / what it bites" judgment; BVDT
  carried a "Verdict" artifact label. This build's B03 states the same constraint
  (house style, case theory, every fact cited, every case checked) without framing it
  as a design tell, and BCRY carries the same fact as a plain carry-out sentence with
  no verdict framing.
- **Cold open:** source's `ClaudeComposerAsk` ask → `BrutalistHesitantWriter`. Writer
  types the newcomer's wrong-guess word "WRITE" (implying Claude produces the whole
  finished brief), hesitates, corrects to "draft" → lands "Can Claude draft your legal
  brief?". The correction is picked up directly by B03's stated scope (one section,
  not a whole brief) and by BCRY's carry-out (checking still yours).
- **Beat count:** kept the source's 7-beat shape in substance (B00 → B01 anatomy → B02
  pipeline → B03 mechanism → BVDT/BCRY carry-out → BHTF handoff → BOUT outro), plus one
  beat added: the source's single `BOUT` (`ClaudeTitleOutro`) is split into hai-simple's
  fixed two-part Humanitarians AI outro (`OutroSeries` + `OutroCTA`), 7 → 8 beats total —
  same restructuring precedent as every other hai-simple redo in this family.
- **Facts/argument:** unchanged. The skill's anatomy (one file, SKILL.md, 15k), its
  pipeline (Steps section, linear execution), and its constraint (draft one section, in
  house style, consistent with the case theory, every fact and case cited) are the
  source's own facts, reworded only for register — plus fixing a truncation artifact in
  the source's B03/BHTF text (`"write th`, `"draft the [section]", "write th"` cut off
  mid-word) rather than carrying the bug forward.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is a new, complete first-person Claude prompt
  (the source's own handoff prompt was truncated mid-sentence — `"...every fa"` — and
  is rewritten in full here, same "explain your constraints before you act" clause).

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`), so this redo reuses the same REMOTION components rather than
converting to Manim/GRAPHIC — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. `compile.py`'s motion-histogram WARNING (`remotion` 8/8 = 100%, over the
~40% pantry cap) is expected and accepted for the same reason every prior all-REMOTION
sibling logged it: NO-GENAI/NO-PANTRY LAW forces every beat to GRAPHIC or REMOTION, and
this reel's body legitimately has no illustrative-figure beats to draw as Manim — it is a
file/pipeline/constraint explainer, not a worked-example narrative.

## Gates

- **TYPECHECK / GATE T:** first pass flagged a real content violation — B03's
  `SkillTeardownMechanism.body` at 25 words exceeded the §8.5 12-word pull-quote budget
  ("no-wordy-card" — the screen should show structure, not sentences). Fixed by
  compressing to "One section: house style, case theory, every fact and case cited."
  (11 words); narration keeps the fuller sentence. Second pass: 0 content/pixel FAILs.
  One remaining §8.9 sweep flag — `[BOUT/eyebrow] text ends truncated: 'CLAUDE BASICS ·
  HUMANITARIANS AI'` — is a confirmed false positive (the middle-dot `·` character
  triggers the truncation heuristic); the identical string, unfixed, shipped in the
  already-DELIVERED `books--claude-liam-legal-finance` sibling. Left as-is per that
  precedent rather than reworded away from house style.
- **TIMING LAW (B00):** narration 35 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **11.16s**, clears the ≥8s floor. Late frame pull (t≈9.7s)
  confirms the full corrected question "Can Claude draft / my legal / brief?" on
  screen with the correction landed.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (well above the -40 dB floor), max
  -2.9 dB.
- **Gate V (frame QC):** full contact sheet reviewed, plus full-resolution late-frame
  pulls of B00, B03, BCRY, BHTF, BOUT, BCTA. All legible, correctly kerned, no overlap,
  safe inset respected. `@HumanitariansAI` folderLabel explicit on BHTF (avoiding the
  `ClaudeComposerAsk` default-prop bug documented by the `legal-finance` sibling).
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (8/8
  beats, no violations).

## Output

`claude-for-legal--claude-liam-brief-section-drafter-slate.mp4` — 76.5s, 8/8 beats real
(no slates), audible narration throughout (mean_volume -23.9 dB). This is the review cut
(COMPLETION LAW satisfied: newer than `beat_sheet.json`, audible audio verified via
ffprobe/compile GATE AUDIO).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-for-legal"` matches no
prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key fallback →
"Claude Basics". Considered overriding to "Extending Claude — Skills, Plugins &
Connectors" by content analogy (this reel teaches what a Claude Skill file is), the same
override the `books--claude-liam-legal-finance` sibling made — but checked sibling
precedent within THIS family first: every other delivered `claude-for-legal--*` redo
(`ai-inventory`, `ai-tool-handoff`, `auto-updater`, `bar-prep-questions`,
`board-minutes`) resolved to "Claude Basics" via the same fallback, and `auto-updater`'s
own log records self-correcting away from the "Extending Claude" override specifically
for family consistency. Matched that precedent here rather than re-introducing the
inconsistency.
