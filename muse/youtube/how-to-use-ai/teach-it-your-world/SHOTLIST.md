# SHOTLIST.md — "Teach it your world"

13 beats, ~336 s estimated (Kokoro `am_onyx`). 7 Manim scenes (B02–B08),
6 Remotion bookends (B00, B01, BDEFS, BVDT, BHTF, BOUT). 16:9, Claude palette
(cream `#F2F0E9`, ink `#3D3929`, terracotta `#D97757`), EB Garamond.

## Bookends (Remotion)

| Beat | Pattern | What the viewer watches |
|---|---|---|
| B00 | `ClaudeComposerAsk` | Greeting "Konnichiwa, Liam". The command "What should I pack for my trek next month?" types in; the running indicator spins; the generic packing list types in line by line and holds — correct for everyone, right for no one. |
| B01 | `BrutalistHesitantWriter` | The writer types "AI is smart because it knows everything." / "Hand it your documents, and it answers from your world." — then strikes "because it knows everything" and types "when you give it your material". `lead_silence_s: 0.8`; narration ≥ 9 s so the typing and the correction land. |
| BDEFS | `ClaudeDefinitions` | "Terms In This Film": knowledge base → upload → grounding → RAG, one row at a time, one plain line each. |
| BVDT | `ClaudeVerdictArtifact` | Verdict card, heading "Teach it your world", brand "@NikBearBrown". Four lines stagger in two pages: the mechanism, the practice, the pin-and-quote, the falsifiable test ("ask about something only your docs know"). |
| BHTF | `ClaudeComposerAsk` | Greeting "Your turn." The rota prompt types in full and holds while Liam reads it aloud and discusses it; two check lines land at the end. |
| BOUT | `ClaudeTitleOutro` | Title restate in serif with terracotta period; "@NikBearBrown" beneath; slug-seeded mascot; no subline. 1.0 s silent tail. |

## Body (Manim, one drawing per beat)

| Beat | Scene class | Shot |
|---|---|---|
| B02 | `B02_TheGap` | Big dim ghost circle, label "the internet"; small kraft box with terracotta tape, label "your docs". Question card "on call Friday?" slides in; an arrow fires into the big circle; three wobbly squiggle lines grow inside as the answer; an ink "?" lands beside them. |
| B03 | `B03_TheFix` | Open kraft box centre-stage, label "give it the source". Three pages drop in one by one. An answer card lands with wobbly lines; the lines straighten into solid ink; a terracotta check lands beneath. |
| B04 | `B04_TheLibrarian` | A shelf of five dim standing pages; question card "rota?"; answer card. Two matching pages light with terracotta edge rings, lift off the shelf, fly to the answer card; three solid answer lines draw in. Label "librarian". |
| B05 | `B05_MeaningMap` | A dim dot scatter. Three ink dots cluster close, labelled "invoice" / "receipt" / "bill"; a terracotta ring draws around the cluster. One far dot labelled "elephant". Label beneath: "near = similar meaning". |
| B06 | `B06_WhatToUpload` | Three open kraft boxes in a row, labels "your notes" / "work docs" / "only-you-know". A page drops into each box in turn. |
| B07 | `B07_ThreeHabits` | Three numbered cards: "give it / the source", "pin it: / only from this", "make it / quote", each with one terracotta dot. A terracotta check lands on each card in turn. |
| B08 | `B08_WhereItBites` | Three mini-panels: a half-empty open box ("blind spots"); a cobwebbed page beside a fresh page ("stale in, stale out"); a page with an ink X and two solid "quoted" lines beneath ("wrong doc = confident quote"). |

## Motion rules (all beats)

- Every play() introduces its shapes with FadeIn/Create/GrowFromCenter first;
  nothing appears only via .animate().
- All motion completes in the first ~40% of the beat; `until()` holds on the
  settled, labelled frame; `finish()` pads to the measured audio.
- One terracotta accent per beat (checks, rings, tape, glow). Terracotta
  never sits under text.
- Every on-screen word is spoken in its beat's narration (verified in
  CHECKS-REPORT.md).
- `@NikBearBrown` bug, lower-right, inside the safe area, on every Manim
  scene (`self.add(bug())`).
