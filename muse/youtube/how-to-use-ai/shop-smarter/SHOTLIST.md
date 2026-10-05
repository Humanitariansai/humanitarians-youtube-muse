# SHOTLIST.md — "Shop smarter"

Every body beat is one isometric/flat Manim drawing in the Claude palette
(cream `#F2F0E9`, ink `#3D3929`, terracotta `#D97757`, kraft cardboard tones).
The film's cast, kept constant throughout: the three kraft option boxes
(the same boxes every beat), ink heads, kraft pages, the comparison table,
a magnifier, a price tag, a cursor.

Card test (per the skill): every beat's idea is a thing, a part, or a flow —
none is an interface, a set of numbers, or one word. **Zero ShowTellCards.**
The B02/B03 table is drawn in ink lines, not a data card; the numbers "1, 2,
3" in B08 are ink step markers beside their plates, not data.

Midpoint discipline (GATE T samples each clip at its midpoint): in every
scene all motion completes in the first ~40% of the beat, fully opaque —
nothing is half-faded or half-drawn at the midpoint. `until()` then holds on
a settled, labelled frame; `finish()` pads to the audio. All `until()` phrases
were verified present verbatim in their beat's narration.

| Beat | Class | Shot | Motion (claim) | Labels (≤3 words) | until() phrase |
|---|---|---|---|---|---|
| B00 | B00_ThreeOptions | Three kraft boxes land in a row; A, B, C beneath | boxes land L→R, one terracotta dot on the middle box → labels land | A, B, C | best for what |
| B01 | B01_Priorities | "you" head hands a priority card to the AI panel | card slides to the panel → terracotta dot lands on it | you, AI | measured against |
| B02 | B02_TheTable | Ink grid draws: verticals, then horizontals; A/B/C headers | grid draws in two plays (two membership changes) → headers + label land | A, B, C; side by side | actually compare |
| B03 | B03_Tradeoffs | The same table; terracotta ellipse rings the trade-off row | table fades in (continuity) → ellipse rings row → ink check lands | trade-off | mind the least |
| B04 | B04_ReviewFunnel | Five review pages funnel to one summary page | pages land → funnel draws → summary grows → check lands | patterns | Patterns, not stars |
| B05 | B05_FinePrint | Contract page of tiny lines; magnifier + terracotta ring on a clause | page lands → magnifier lands → ring grows | the catch | actually act on |
| B06 | B06_MoneyTraps | Three trap cards: warranty, returns, renew | cards land → terracotta X stamps each → tag lands | warranty, returns, renew; paragraph nine | paragraph nine |
| B07 | B07_StalePrices | Stale price tag X'd out; cursor cables to a live card | tag lands → X stamps → cursor + cable draw → live card + check land | stale, live, check live | every time |
| B08 | B08_TheMethod | Three numbered plates: priorities, table, fine print; head crowns them | plates + labels land → checks land → head lands | 1 priorities, 2 table, 3 fine print; you decide | the whole co-pilot |

Continuity: B03 reuses B02's exact grid (same helper, same coordinates);
the option boxes in B00 are the kit's `iso.box` in kraft; B08's plates echo
the three-option cast as the method the film leaves behind. Labels sit beside
objects with leader gaps ≥0.3; no label sits inside an outline or on a
terracotta fill.
