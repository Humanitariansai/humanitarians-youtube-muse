# PEDAGOGY — Claude, Gated. (ai-explainer, claude-liam)

Scout-sourced build: `vids/video-ideas.md` Candidate 01, from
`ai1-cli/chapters/01-inventory-research-blueprint-signoff.md`. Thesis: AI1
CLI blocks a new book from drafting until it clears four gates — inventory,
research, blueprint, sign-off — and the last gate is one the agent is
constitutionally barred from signing itself.

## Act structure

- B00 cold open (`ClaudeComposerAsk`) with RESULT lines, IN-FOR-BEAR LAW
  narration ("this is Liam, in for Bear") ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 (cold open), B02 (ask
  micro-beat, ASK→RESULT pair with B03), B05 (verdict), B06 (handoff), B07
  (outro). B01 (`LayerStack`), B03 (`DivergentFates`), B04 (`ChipGrid`) are
  concept illustrations — no two consecutive beats share a scheme ✓
- ASK→RESULT LAW: B02 (ask, command pre-typed, no type-on per SPARK-LINE
  LAW) → B03 (result, the real chapter-17 divergence) reads as one receipt ✓
- SHOW-DON'T-TELL LAW: every beat's `shot.show` block authored before
  narration was finalized; PPT-test checked — each visual event lands on the
  spoken claim it illustrates ✓
- NARRATION BUDGET: body beats checked by word count — B01 62 words, B03 66
  words, B04 61 words, all inside the 45-70 band. Bookends (B00, B05
  verdict, B06 handoff) are exempt and run longer by design ✓
- HANDOFF LAW: B06 prompt is read aloud verbatim, then discussed (the
  "flags its own weakest guess" clause), before the pause invitation ✓
- Title-restate OUTRO ✓ · Greeting "Namaste, Liam" — Wagwan check:
  charsum('claude-liam-blueprint-before-draft') % 10 == 8, not 0, so no
  Wagwan ✓

## Evidence discipline (source: SOURCES.md, verified 2026-07-24 against the
primary chapter directly — this reel's source IS the book, not a
third-party claim needing external fact-check)

| Claim | Source line | Verdict |
|---|---|---|
| "the agent prepares; the human signs" | ch01 line 15, verbatim | OK |
| Four gates: inventory → research → blueprint → sign-off (GATE 0) | ch01 lines 13-17 | OK |
| Chapter 17 misclassified as "a longer... version of the profile," corrected to qualitative-research chapter | ch01 line 119, near-verbatim | OK |
| "the inventory is a claim, and you just checked it" | ch01 lines 23 & 119, verbatim | OK |
| "I don't understand that prompt at all" | ch01 line 131, verbatim | OK |
| Four replacement questions | ch01 lines 135-137, compressed for on-screen chips | OK — meaning unchanged |
| "one wrong row out of twenty-four" | ch01 line 119 | OK |

## Friction protected

- Kept: the exact "agent prepares; the human signs" line as the reel's
  spine quote — it IS the book's own stated rule, not our paraphrase.
- Removed: the chapter's much longer worked example (the full triangulated
  research run across three AI systems, the 14-chapter TOC, the module
  structure) — extraneous to the single insight this scout card asks for;
  stays in the source chapter for anyone who wants the full worked example.

## Status

**VERDICT: PASS** — signed off by the human (Divyank Singh, singh.divya@northeastern.edu) in chat, 2026-07-24, on review of this PEDAGOGY.md's narration and act structure. Covers B00–B07 (the original 8-beat cut, already audio-generated and rendered).

## Addendum — BINV (added after the original PASS, not yet covered by it)

New beat inserted between B01 and B02: a VOX-still archival beat ("the
inventory, felt") requested by the human to add a real historical/archival
image and a beat of visual variety against the otherwise all-abstract
illustration set (LayerStack / DivergentFates / ChipGrid).

- **Placement rationale:** B01 introduces all four gates abstractly;
  BINV zooms into gate 1 (inventory) concretely and tactilely, right before
  B02/B03's concrete example (the chapter-17 catch) of that same gate
  working — so the sequence goes overview → felt/embodied → proved-by-example.
- **Narration (61 words):** grounds the same "inventory is a claim, and you
  just checked it" discipline already used in B01/B03 in a new frame (the
  archivist's job of reading the object, not the label) — not a repeated
  claim, a repeated discipline shown from a new angle. No new factual claims
  beyond what's already verified in SOURCES.md / the table above.
- **Media:** real archival photograph (Smithsonian Open Access preferred,
  per the human's direction), human-sourced into `pantry/` as `BINV.png` —
  not AI-generated, not a screenshot. `shot.prompt` in beat_sheet.json
  describes what to look for; `build.needs` carries the search link.
- **ILLUSTRATE LAW:** stays clean — BINV is a VOX/pantry beat, not a Claude
  UI beat, so the UI-only-at-bookends rule is unaffected.

**VERDICT: PASS** — signed off by the human (Divyank Singh,
singh.divya@northeastern.edu) in chat, 2026-07-24, on review of the BINV
narration above.
