# BUILD-LOG.md — "The first answer is a draft"

Film 8 of 24 · slug `the-first-answer-is-a-draft` · built 2026-10-03 by Muse (subagent film-package builder).

## Skill choice
Kept the assigned skill: **show-tell**. The film is a concrete visual demonstration — one evolving object (the draft page) transforming beat by beat — which is exactly the skill's home ground: one simple isometric drawing per beat, minimal labels, narration carries the idea. No other skill in the set fits better; nothing about the film is a lecture, a product tour, or a character piece. [judgment]

## Card test result
Zero ShowTellCards. Every body beat passed the card test toward a drawing: the ideas are a thing (the page) and physical actions on it (a stamp, trims, tags), not interfaces, numbers, or single words. B06's before/after is the film's own two pages, which a drawing shows as clearly as any card. Recorded per-beat in SHOTLIST.md. [judgment]

## Build order
1. Read the show-tell SKILL.md, the iso_kit template, the example make_sheet, the static checker source, and the approved-props catalog (decided the film's own draft page was a better cast than any catalog prop — no quota). [record]
2. Read `muse/FRICTIONAL.md` from the write repo via the Contents API (surrogate credential flow) to match the seven-field entry format. [record]
3. Authored ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md, PROMPTS.md. [record]
4. Wrote make_sheet.py with built-in assertions (13 beats; 9 manim classes matching beat ids; total duration 140–360 s; BIDEA trigger verbatim and punctuation-free; BDEFS terms ≤ 17 chars; BHTF reads prompt in full; BOUT 1.0 s tail; bookend_exempt set). First run: 13 beats, 9 manim scenes, est 150 s. [record]
5. Wrote scenes.py: iso_kit pasted verbatim at top (not imported — Gate A copies only scenes.py), then film helpers (`standing_card`, `card_line`, `draft_tag`, `pushback_pill`, `label_right`) and nine scene classes. Removed a dead helper (`page_group`) before QC. [record]
6. QC gate: `py_compile` clean on both files; static_scene_check.py on all 9 classes → 9 clean · 0 warn · 0 error, first run. [record]
7. Wrote BUILD-LOG.md, CHECKS-REPORT.md, CLAUDE-CODE-RENDER.md, README.md. [record]
8. Pushed all 12 files to `muse/youtube/how-to-use-ai/the-first-answer-is-a-draft/` on Humanitariansai/humanitarians-youtube-muse via gh-put-file.py; verified every file with a Contents API read afterwards. [record]

## Failures and fixes
- None in the QC gate. One pre-QC self-catch: the B01 rubber stamp's start position (y=3.6) would have tripped the checker's safe-area warning; lowered to y=2.9 (top edge 3.35 < 3.4) before the first checker run. [record]
- manim_layout_audit.py --curve-strict cannot run in this VM (no Manim/pangocairo installed); deferred to Bear's Mac render pass per the task. [record]

## Design notes
- The film's cast is a single draft page that evolves B02→B05 (vague ghost lines → trimmed → sharp ink lines with dinner names → 15-minute tags), so the viewer watches iteration happen. Continuity: each scene rebuilds the same page geometry at the same iso coordinates. [judgment]
- Greeting stays "Hallo" (Kokoro-clean per the skill's list). Narration spells out numbers ("fifteen minutes"); no acronyms, no version numbers, no decimals — no whisper-check risks. [judgment]
- FACTCHECK.md has no empirical claims — this film is advice, and the log keeps claims modest and behavioral. [judgment]
- Narration total ≈ 150 s estimated (2.5 min) — at the low end of the 3–6 min target, but the skill's law 9 ("as long as it needs, no longer") governs: every beat is a step the viewer actually needs, no padding added to hit a length. [judgment]
