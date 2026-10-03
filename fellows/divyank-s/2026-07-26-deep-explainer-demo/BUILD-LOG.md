# BUILD-LOG — Claude, Constitutional.

## Decisions

- **Single-chapter source.** Used only `ai1-cli/chapters/01-...md` rather
  than spanning several chapters — it's a real 4-part framework on its own,
  and using material I'd already read in full this session avoided
  introducing new, unverified claims under time pressure.
- **No Manim.** This machine has no `pangocairo`/`pkg-config`, so Manim
  can't install (same constraint hit during the cli-explainer build). The
  beat-mix contract's MANIM share (~25-40% of body beats) is absorbed into
  REMOTION instead. Actual mix: VOX 6/28 body beats (21.4%, inside the
  15-30% clean band), REMOTION carries the rest of the "own"-sourced content
  beats, CARD = the 4 act cards. This is a deviation from the genre's
  three-lane texture, logged here rather than silently substituted.
- **VOX stills sourced by the agent, not left as shopping-list asks.** The
  human's standing instruction this session ("if you require characters,
  refer to Smithsonian") was applied via Wikimedia Commons (Smithsonian's own
  search UI blocks non-browser fetches — see the ai-explainer-demo session
  note) — all 6 images found, license-checked, and placed directly into
  `media/<BID>.png` before Gate D2, so `SHOPPING.md` should show zero open
  asks for this build (see that file).
- **Act cards via `FluencySegmentCard`.** Reused an existing reel-local
  Remotion component (originally built for `claude-liam-fluency-trap`) — it's
  generic (`title`, `index`), already Claude-palette-toned (`#F2F0E9`/
  `#3D3929`), and needed no new code.
- **Quote beats via `ClaudeScienceChipGrid` (cols:1).** No dedicated
  "quote card" component was found registered; a single-item ChipGrid gives
  a clean one-card reveal using an already-validated generic component
  rather than inventing new Remotion code mid-build.

## Gate signatures

- Plan / lane histogram: self-reviewed against the mix contract before
  writing (VOX 21.4%, within band) — see this file's Decisions above.
- Gate F (FACTCHECK.md): every claim checked against the source chapter —
  **claims hold**.
- GATE P: see PEDAGOGY.md — pending human sign-off before audio spend.
- Gate D1 (slate previz) / Gate D2 (SHOPPING.md): run after GATE P and audio
  lock, per the required order — not yet run as of this file's writing.

## MISSING

- Manim fragments (the genre's default ~25-40% lane) — none in this build,
  substituted with REMOTION per above. If Manim is installed later
  (`pip install "manim<0.19"` + system `pangocairo`), a future pass could
  convert some ChipGrid quote-cards into Manim equation/isotype fragments for
  closer genre-texture compliance — not required for this build to be
  complete, just noted as the honest gap.
