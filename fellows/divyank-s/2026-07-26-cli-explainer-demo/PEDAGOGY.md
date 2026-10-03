# PEDAGOGY — Claude, Patched. (cli-explainer, claude-liam, --tool claude)

Fresh build, no scout card (no `cli-ideas.md`/`simulation-ideas.md` in
`ai1-cli`). Source is "a thing you built" per the skill's own trigger: this
session's real debugging session that fixed Remotion's macOS-compatibility
crash in the `brutalist.art` toolkit. Thesis: the crash looked like a beat-sheet
bug but was one dependency-version boundary (4.0.438 vs 4.0.439) — found by
reading the binary's own `LC_BUILD_VERSION`, not by guessing at code.

## Required spine check (SKILL.md's mandatory spine)

- B00 INTRO — `ClaudeComposerAsk` cold open, ask answered (COLD OPEN LAW),
  IN-FOR-BEAR LAW narration ✓
- B01 PROBLEM — stakes stated before any prompt appears, no CLI yet ✓
- Cycle 1: B02 ASK → B03 CODE (`ClaudeCodeBeat`, real `otool` command) →
  B04 OUTPUT (`BinaryBranch`, moving, never a still) ✓
- Cycle 2 (**THE REVISION LAW** — mandatory in 16:9): B05 CHANGE → B06 CODE
  (real sweep script) → B07 OUTPUT (`DivergentFates`, moving) — a genuine
  check-and-change, not a cosmetic repeat ✓
- B08 SUMMARY — the lesson in one beat ✓
- B09 NEXT STEPS — HANDOFF LAW: prompt read aloud verbatim then discussed
  (the "before you assume the newest version is right" line) before the
  pause invitation ✓
- B10 OUTRO — title-restate, `ClaudeTitleOutro` ✓
- SPARK-LINE LAW: B02 greeting "The ask,", B05 greeting "The revision," —
  no empty inner-composer greetings ✓
- ACTUAL-CODE LAW: B03/B06 code is the REAL commands run this session
  (see SOURCES.md), trimmed to the lines that teach — not pseudocode ✓
- Greeting "Ciao, Liam" — Wagwan check: charsum('cli-liam-remotion-macos-fix')
  % 10 == 6, not 0, so no Wagwan ✓

## Narration budget

Body beats checked by actual word count (`len(text.split())`), not eyeballed.
Bookends (B00, B09 handoff) exempt.

| Beat | Words |
|---|---|
| B01 | 66 |
| B03 | 50 |
| B04 | 56 |
| B06 | 30 |
| B07 | 40 |
| B08 | 52 |

All inside or under the 45-70 band; B06/B07 run a little lean (30/40) but
that's the CODE/OUTPUT pair reading a short, dense discovery — not padded
for its own sake.

## Evidence discipline (source: SOURCES.md — this session's own transcript,
not a third-party claim)

All claims trace directly to commands actually run in this conversation:
the crash text, the `otool`/`minos` readings, the version-sweep results
(4.0.438 last-good, 4.0.439 first-bad), and the successful post-pin render.
No external fact-check needed — the "source" is our own verified work.

## Friction protected

- Kept: the exact dyld error text and the exact `otool` output — the
  narrative's credibility rests on these being real, not paraphrased.
- Removed: the earlier, now-irrelevant detour (the broken `public/` symlinks
  bug) — a real second bug hit in the same session, but it's a distinct
  story from the macOS/Remotion-version story this reel tells; kept out to
  respect ILLUSTRATE LAW's one-idea-per-reel discipline. Worth a second
  cli-explainer of its own if wanted.

## Status

**VERDICT: PASS** — signed off by the human (Divyank Singh,
singh.divya@northeastern.edu) in chat, 2026-07-24, on review of this
PEDAGOGY.md and the beat sheet's narration.
