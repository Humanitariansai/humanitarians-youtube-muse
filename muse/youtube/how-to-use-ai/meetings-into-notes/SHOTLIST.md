# SHOTLIST.md — Meetings into Notes

One scene per beat. Every body beat is a drawn Manim illustration (Claude
palette, cream stage); labels are 1–3 words beside objects, never inside them.
**No ShowTellCard beats** — every beat's idea is a thing, a part, or a flow,
so each fails the card test at question 1 ("is the idea an interface, a set of
numbers, or one word?"). The composer beat (BHTF) is the mandated bookend, not
a card choice.

The cast: one messy transcript page (white card, ghost text lines, terracotta
dot), one chat window (cream card, dark title strip, composer pill at the
bottom), and the three output cards (summary / decisions / action items) in
grey outlines so they read inside the ink-outlined window.

| beat | scene class / pattern | the motion (the claim, in motion) | labels on screen | why not a card |
|---|---|---|---|---|
| BIDEA | BrutalistHesitantWriter | writer types the naive question, backspaces "take better meeting notes" → "get Claude to turn the meeting into notes" | — | bookend |
| BDEFS | ClaudeDefinitions | three terms land one by one | transcript · summary · action item | bookend |
| B00 | B00_RamblingMeeting | transcript page drops in with tangled lines; three small bubbles land, each remembering a different date | the meeting | the rambling meeting is a thing — drawn |
| B01 | B01_PasteIt | the transcript page slides into the composer; a reply card grows with a terracotta check | mess in · notes out | paste-in/get-back is a flow — drawn |
| B02 | B02_RoughNotes | three fragment cards ("launch??", "Sam — paymt", "release notes?") drop into the composer as-is; a check lands | rough notes | fragments-feeding-a-window is a flow — drawn |
| B03 | B03_ThreeBullets | the exact prompt types into the composer; a reply grows with three bullet lines and terracotta dots | summarize | prompt-in/three-bullets-out is a flow — drawn |
| B04 | B04_DecisionsOwners | prompt lands in two lines; a reply card grows: two decision rows, each with an owner pill ("Maya", "Sam") | owners | decisions-with-owners is a flow — drawn |
| B05 | B05_Unresolved | two loose-end cards drop in; ink "?" marks land on them | unresolved | loose ends surfacing is a flow — drawn |
| B06 | B06_Example | the transcript page lands; three output cards spring out of the window beside it: summary / decisions / action items | example | the fictional example is a flow — drawn |
| B07 | B07_KeepAsking | a follow-up question lands in the composer; an email card grows beside the window | keep asking | asking-on is a flow — drawn |
| B08 | B08_CheckRules | the transcript page drops; an ink lock lands over it | check your rules | a warning illustrated on an object — drawn |
| BHTF | ClaudeComposerAsk | composer opens; the prompt types in full; two check lines land | — | mandated bookend |
| BOUT | ClaudeTitleOutro | title restates; handle; 1.0 s tail | — | mandated bookend |

## Continuity

The same transcript page opens B00, feeds the composer in B01, is named in
the fragments of B02, comes out of the window as three cards in B06, and sits
under the lock in B08. The same chat window carries the composer through
B01–B07. The three output cards of B06 wear the same grey outlines and bullet
style as the B03/B04/B05 replies.

## Timing notes (GATE T midpoint)

Major motion is kept out of each clip's 45–55% window via `until()` phrase
timing. Event phrases were chosen so landings fall early (B00 page, B01 page,
B02 fragments, B03 reply, B05 marks) or late (B04 decision rows, B06 cards,
B07 email card, B08 lock). After Kokoro audio is measured on the Mac,
re-verify with the midpoint guard before the 4K run.

## Label traps checked by hand

- Labels sit beside objects with ≥ 0.3 leader gaps; no leader touches its label.
- Terracotta appears only on dots, checks, and the B03 bullet dots — never
  under text, never as text (the "?" marks in B05 are ink).
- All coordinates inside ±6.2 × ±3.3; type ≥ 32.
- Every beat has a label up by its midpoint (B02's "rough notes" lands with
  the fragments; B06's "example" tags the window before the cards spring out).
