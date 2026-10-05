# SHOTLIST.md — Tame your inbox

One scene per beat. Every body beat is a drawn Manim illustration (Claude
palette, cream stage); labels are 1–3 words beside objects, never inside them.
**No ShowTellCard beats** — every beat's idea is a thing, a part, or a flow,
so each fails the card test at question 1 ("is the idea an interface, a set of
numbers, or one word?"). The composer beat (BHTF) is the mandated bookend, not
a card choice.

The cast: one open tray (kraft fill, ink outline), the pile of email cards,
two sorted stacks ("needs you" ink, "noise" dim), the three-line brief card,
the ghost-lined draft card, the ink SEND pill, the padlock, the grey bin,
and the archive tray.

| beat | scene class / pattern | the motion (the claim, in motion) | labels on screen | why not a card |
|---|---|---|---|---|
| BIDEA | BrutalistHesitantWriter | writer types the naive auto-reply question, backspaces "get Claude to answer my emails" → "use Claude as my email first-pass, safely" | — | bookend |
| BDEFS | ClaudeDefinitions | three terms land one by one | inbox triage · summary · draft | bookend |
| B00 | B00_ThePile | tray lands; email cards drop in from the top until the pile overflows; three terracotta dots land on the buried cards that matter | the pile | the overflowing pile is a thing + a flow — drawn |
| B01 | B01_Triage | a terracotta scan line sweeps the pile; the pile splits into "needs you" (ink) and "noise" (dim); a check lands on "needs you" | triage · needs you · noise | sorting is a flow — drawn |
| B02 | B02_TheSummary | kraft lines draw from the tall thread stack to a brief card that grows with three ink lines; terracotta dots land | the summary | thread-to-brief is a flow — drawn |
| B03 | B03_TheDraft | one email card; a draft card grows beside it with ghost reply lines; an ink check lands | the draft | drafting is a flow — drawn |
| B04 | B04_NeverAutoSend | the draft card; the ink SEND pill lands; an ink lock lands over the pill | never auto-send | the guarded button is a thing — drawn |
| B05 | B05_NeverAutoDelete | an email card hovers over the bin; an ink X stamps the bin; the card slides into the archive tray; a check stamps the tray | never auto-delete | the rejection + re-route is a flow — drawn |
| BHTF | ClaudeComposerAsk | composer opens; the prompt types in full; two check lines land | — | mandated bookend |
| BOUT | ClaudeTitleOutro | title restates; handle; 1.0 s tail | — | mandated bookend |

## Continuity

The same open tray holds the pile in B00 and B01 — B01 starts with the tray
and pile on stage. The draft card of B03 returns in B04, where the SEND pill
lands beneath it. The bin in B05 is a fresh object for the second rule; the
archive tray is its answer.

## Timing notes (GATE T midpoint)

Major motion is kept out of each clip's 45–55% window via `until()` phrase
timing. Event phrases were chosen so landings fall early (B00's card drops on
"Somewhere in here are a bill" / "newsletters, receipts, promos"; B01's split
on "what actually needs me"; B02's brief card on "a dozen emails back and
forth"; B05's X on "Never let it delete on its own") or late (B00's dots on
"This one is about what you do once it's in"; B01's check on "You read what
matters"; B02's dots on "You walk into the meeting"; B03's check on "only then
hit send yourself"; B04's pill on "the damage is done in one click" and the
lock on "the send button stays yours"; B05's archive slide on "tell it to
archive the noise instead" and its check on "empty the trash yourself"). After
Kokoro audio is measured on the Mac, re-verify with the midpoint guard before
the 4K run.

## Label traps checked by hand

- Labels sit beside objects with ≥ 0.3 leader gaps (the `tag()` helper
  stops the leader 0.35 short); no leader touches its label. B05's
  "never auto-delete" sits below the bin, clear of the card's flight path
  to the archive tray.
- Terracotta appears only on dots, the B01 scan line, the B01 check, and the
  B05 tray check — never under text, never as text (the X stamps are ink).
- All coordinates inside ±6.2 × ±3.3 (B00's cards start at y=2.7, inside the
  safe area, and drop to their pile spots); type ≥ 32.
- Every beat has a label up by its midpoint.
- The bin is a grey (BAR2) tapered body, not a near-black field — GATE T
  §8.6b reads large near-black fields as giant text.
