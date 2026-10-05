# BUILD-LOG — Code without coding

## 2026-10-04 — package built (film-build worker subagent)

**Skill choice:** kept `show-tell` (assigned). The film is a textbook
show-tell: one simple isometric drawing per beat, minimal labels, Liam's
narration carrying every idea. No beat passed the card test (every beat is a
thing/part/flow best drawn with the film's own cast — a page landing, cards
springing up, a tower toppling, a cursor clicking), so zero ShowTellCards.
[judgment]

**Source:** NEW film, not a refactor — no mirror-repo source exists for this
pitch. Written from scratch: the promise (words in, page out), the pipeline
(words → code → page), two safety rules (checkable by looking; personal
only), the three mistakes (too big; secrets; no testing), the repair loop
(describe it back), and the why-now number. [record]

**Beat design (13 beats, ~248 s est.):** BIDEA hesitant writer (naive
"build everything" request corrected into "does one small thing" — the
correction is mistake one's lesson), BDEFS (code / AI coding tool / bug),
B00 hero (the finished page arrives), B01 the pipeline, B02 checkable builds,
B03 personal-only builds, B04 mistake one (tower topples → one small thing),
B05 mistake two (password card blocked), B06 mistake three (click every
button), B07 the repair loop, B08 why now (25%, attributed, hero number +
curve), BHTF composer exercise (build one small page), BOUT spoken outro.
[judgment]

**Fact work:** the one number (25% of YC W25 on 95% AI-written codebases)
verified via web search 2026-10-04 — TechCrunch Mar 2025 reporting Jared
Friedman/Garry Tan in YC's "Vibe Coding is the Future" video. Attributed
aloud AND captioned ("per Y Combinator") per the thin-numbers law. Noted the
reporting caveat (those founders are technical) and kept the film's claim
inside it. "thousands of lines" is rhetorical, not a stat. No pricing tiers,
no version-specific features (BHTF modelLabel is the neutral "Claude").
[record]

**Pacing decision:** narrations for B01/B02/B03/B04 were rewritten so every
`until()` key phrase sits inside the first ~35% of its beat — nothing is
mid-motion at the clip midpoint under GATE T sampling. Two beats land their
payoff after the midpoint (B04's clean page ~68%, B07's fix ~63%); both start
motion well clear of the 50% ± margin window. The house `words/2.5` estimate
runs ~1.6× long vs real Kokoro, so phrase-keyed motion scales with the
measured audio. [judgment]

**Template fix:** the pasted `iso_kit.py` had a latent bug in `open_box` — a
duplicated point (`(x1, y1, z1)` twice) made a degenerate quad. Fixed while
pasting; `open_box` isn't used by this film's scenes, but the file is the
house kit and the fix is truthful. [record]

**QC:** `py_compile` clean; `static_scene_check.py` 9/9 scenes clean,
0 warnings, 0 errors after one fix round (B03/B05 `name_tag` start positions
were at y=3.6, outside the ±3.3 safe area — re-staged inside the frame; the
drops now start at y=2.94/2.9). `manim_layout_audit.py --curve-strict`
cannot run in this VM (no Manim/pangocairo); deferred to Bear's Mac render
pass, recorded in CHECKS-REPORT.md and CLAUDE-CODE-RENDER.md. [record]

**Push:** all 12 files pushed to `Humanitariansai/humanitarians-youtube-muse`
`muse/youtube/how-to-use-ai/code-without-coding/` via `gh-put-file.py`,
each verified with a Contents API read afterwards. Did not touch
`muse/FRICTIONAL.md`, `muse/README.md`, or `muse/QUEUE.md`. [record]

**Open for Bear:** render narration (Kokoro `am_onyx`) + Manim on his Mac per
CLAUDE-CODE-RENDER.md; run the layout audit there; never publish without his
explicit instruction.
