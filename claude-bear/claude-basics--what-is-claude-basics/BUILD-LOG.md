# BUILD-LOG — claude-basics--what-is-claude-basics

## 2026-08-28 — hai-simple redo, review cut

**Mode:** redo of `anthropics/youtube/claude-basics/what-is-claude-basics`
(Teardown, @NikBearBrown, audience "playlist trailer" for the Claude Basics
series — never built: all 7 core beats status SLATE, no media ever rendered).

**What was kept from the source (facts unchanged):** default Claude sessions
start blank each time (no cross-session memory); a project with real documents
loaded + conversation history changes output specificity; context is the
variable, starved context produces generic output; the concrete action — put
the 3 documents you keep re-explaining into one project. Source's actual posed
question ("What actually changes your results with Claude in the first week?")
kept as the question this redo answers; the source's meta-title ("What Is the
Claude Basics Playlist.") kept as `metadata.title` only. See SOURCES.md for the
full fact-carry-forward and why no ONE-FLAG was needed (no new inference was
introduced re-registering to Plain).

**What changed:** register Teardown → Plain (judgment removed, facts kept);
B00 replaced with `BrutalistHesitantWriter` ("smart" → "fed" — the newcomer
blames the model's intelligence, correction points at what it's fed) per
WRITER LAW; source's compressed 4-beat body (B01/B02/B04/B05) redistributed
across S01–S07 to satisfy hai-simple's mandatory WRONG-GUESS / ANCHOR (three
documents, S04→S05) / BOTH-DIRECTIONS (S06/S07) structure, which the source's
sheet bundled together without separating; outro replaced source's
`ClaudeTitleOutro` (LOCKED to handle `@NikBearBrown` per OUTRO-LOCK.md — would
have silently shown the wrong channel) with `OutroSeries` + `OutroCTA` carrying
the Humanitarians AI skin.

**Built end to end this invocation:** audio (12 beats, Kokoro am_onyx), 7 Manim
GRAPHIC scenes (S01–S07, reel-local `scenes.py`), 5 Remotion beats (B00, BCRY,
BHTF, BOUT, BCTA via `remotion_scenes.py`). B00 TIMING LAW: narration measured
at 8.34s (≥8s floor); pulled a frame at t≈3.5s (correction "smart"→"fed" mid-
strike, terracotta) and t≈7s (final corrected question fully typed, "Is Claude
just not fed enough for my work?") — correction confirmed visible.

**Gate V caught 2 real defects, fixed at the root, re-rendered, recompiled:**
1. S02/S03 — "SMARTER MODEL" label text overflowed both sides of its fixed-
   width `Rectangle` box (font wider than the hardcoded 5.4-unit box). Fixed by
   replacing the fixed box with a `SurroundingRectangle` sized to the text
   itself in both scenes; re-rendered S02/S03, verified the label now sits
   fully inside its border.
2. BHTF — `ClaudeComposerAsk`'s Root.tsx registration hardcodes
   `folderLabel: '@NikBearBrown'` as the composition's defaultProps; since the
   beat's props JSON never set `folderLabel`, the rendered frame showed
   `@NikBearBrown` on a Humanitarians AI reel. Fixed by adding
   `"folderLabel": "@HumanitariansAI"` to BHTF's remotion props; re-rendered,
   verified the corrected handle on screen.

GATE T: PASS (0 FAILs, all §8.10 checks SKIP — no recitation content).
Gate V: PASS after fixes — 18-frame pull (6s spacing) + targeted crops of both
fixed regions + explicit end-of-reel frame for BCTA, zero remaining blockers.
mean_volume: -24.0 dB (floor: -40 dB) — PASS.
Motion histogram: graphic 7/12 (58%), remotion 5/12 — non-blocking warning
(over MOTION.md's ~40% pantry cap); logged as structural, same disposition as
sibling claude-basics reels (a mechanism-explainer body is naturally
GRAPHIC-heavy; not one of hai-simple's hard gates).

**Known, logged, non-blocking cosmetic gap:** `OutroSeries`/`OutroCTA` render
on hardcoded VOX tokens (flat white ground, near-black ink, `#C8102E` crimson —
`tokens/vox.ts`), not the humanitarians cream/ink/teal/crimson (`#F3EBDD` /
`#2F2A26` / `#1F4E5F` / `#E4572E`) used in S01–S07. Neither component exposes
a color prop (checked source: `z.object({eyebrow, line})` / `z.object({line,
handle})`, no `ink`/`bg`/`accent`). Used anyway per hai-simple SKILL.md's
explicit instruction to close with these two named components; not routed
around with an unauthorized new component (GATE L: a genuine template miss is
a design card, not a license to build ad hoc mid-loop). Recorded in
`metadata.skin_warning`.

**Result:** `claude-basics--what-is-claude-basics.mp4`, 110.8s, 3840×2160,
12/12 beats real (no slates), newer than `beat_sheet.json`. Review cut DONE.

---

## 2026-08-28 — Phase 4 delivery

See HAILOOP-LOG.md for outcome (4K render + `deliver.py --push`).
