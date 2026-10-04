# ACTS.md — Tame Your Spreadsheets

Show-tell film (skill: `show-tell`), 11 beats, ~303 s estimated (~5:03).
Persona Liam ("Liam, in for Bear"), Kokoro voice `am_onyx`, Teardown register,
channel `claude-liam`, watermark `@NikBearBrown`. Audience: smart, pragmatic,
not AI experts — every term explained, show rather than tell.

The film has one through-line, the bake shop's monthly sales list (fictional:
Lena's Bake Shop). The same sheet appears in B00, B01, B02, B03 and returns
tamed in B06 — "same objects, whole film" (show-tell law 4).

## Act 1 — The question (bookends, Remotion)

- **BIDEA — BrutalistHesitantWriter.** Greeting: "Hallo. This is Liam, in
  for Bear." The writer types the naive question ("How do I learn Excel, to
  track my sales?") and corrects it to the real one ("tame this spreadsheet").
  `lead_silence_s: 0.8`.
- **BDEFS — ClaudeDefinitions.** "Terms In This Film": formula, cell
  reference, clean data — one line each.

## Act 2 — The three moves (Manim drawings, one image per beat)

- **B00 — the fear.** The hero object: a messy sales grid lands. Messy dates,
  mixed city spellings. Claim: it's just a table; you already know how to
  read one. A patient coach is coming.
- **B01 — plain words in.** The coach arrives: a Claude chat page beside the
  sheet. The hero phrase: "write me the formula that…". Claim: describe what
  you want in plain words; the AI translates. Plain English in, formula out.
- **B02 — the formula lands.** `=SUM(B2:B31)` pasted into the total cell; the
  B2:B31 range bracketed. Claim: read the formula left to right — the
  cell-reference pattern (address of the stretch you want) dissolves half the
  fear.
- **B03 — the warning.** The formula highlights the wrong column; a magnifier
  checks five rows of the right one. Claim: the AI can be confidently wrong
  about cell references — sanity-check every formula on a small sample. The
  checking is your job.
- **B04 — cleanup.** Messy rows in, a scan line sweeps, tidy rows out.
  Claim: paste messy data, ask "clean this up, make everything consistent",
  and an afternoon of find-and-replace happens in seconds.
- **B05 — the insight.** Six day-bars grow; Saturday's towers. Claim: ask
  "what's interesting in this data?" — the AI proposes, you decide (glance
  back at the sheet and confirm).

## Act 3 — Payoff, your turn, outro (bookends)

- **B06 — the tamed sheet.** The same sheet returns: clean rows, the formula,
  a mini chart, a big check. Claim: you never learned Excel — you described,
  you checked, you stayed in charge.
- **BHTF — ClaudeComposerAsk.** "Your turn." One concrete prompt (formula for
  column B + "what's interesting in this data?"), read in full; two
  viewer-run checks: hand-add five rows; read the answer back against the
  sheet.
- **BOUT — ClaudeTitleOutro.** "Tame Your Spreadsheets. At Nik Bear Brown."
  + 1.0 s silent tail. Spoken outro, never exempt.

No ShowTellCard beats used (0 of 7 body beats are cards): every beat is a
thing, a part, or a flow — drawings teach them better. Card test documented
in SHOTLIST.md.
