# SHOTLIST.md — How to Use Claude

One scene per beat. Every body beat is a drawn Manim illustration (Claude
palette, cream stage); labels are 1–3 words beside objects, never inside them.
**No ShowTellCard beats** — every beat's idea is a thing, a part, or a flow,
so each fails the card test at question 1 ("is the idea an interface, a set of
numbers, or one word?"). The composer beat (BHTF) is the mandated bookend, not
a card choice.

| beat | scene class / pattern | the motion (the claim, in motion) | labels on screen | why not a card |
|---|---|---|---|---|
| BIDEA | BrutalistHesitantWriter | writer types the naive question, backspaces "one prompt" → "context" | — | bookend |
| BDEFS | ClaudeDefinitions | three terms land one by one | prompt · context · model | bookend |
| B00 | B00_ChatWindow | window drops in; cursor lands in the composer; reply lines draw above | chat window | the chat window is a thing — drawn |
| B01 | B01_ModelBehind | dark model block fades in behind the window; three lights come on | model | the model is a part of the setup — drawn |
| B02 | B02_Stranger | question bubble lands; a thin two-line reply draws; the window fades (tab closed); "a stranger" lands | a stranger | a habit/failure is a flow — drawn |
| B03 | B03_ContextIn | three context cards drop into the window; the reply card grows from thin to full | context · answer | context-in/answer-out is a flow — drawn |
| B04 | B04_Project | project box opens; style/rules/example cards drop in; a message rides through; an informed reply grows | project · style · rules · example | a persistent workspace is a thing — drawn |
| B05 | B05_Artifact | side panel grows beside the chat; a finished page fades in inside it | artifact | a panel + document is a thing — drawn |
| B06 | B06_Analysis | page stack lands; terracotta scan line sweeps down; structure map of three grey bars fades in | analysis | scanning-then-mapping is a flow — drawn |
| B07 | B07_Rewrite | rough-draft card lands; "your voice" example lands; polished page grows with a terracotta check | rough draft · your voice | draft-to-final is a flow — drawn |
| B08 | B08_CheckIt | claim bubble lands; a large terracotta check stamps onto it | check it | a warning illustrated on an example — drawn |
| BHTF | ClaudeComposerAsk | composer opens; the prompt types in full; two check lines land | — | mandated bookend |
| BOUT | ClaudeTitleOutro | title restates; handle; 1.0 s tail | — | mandated bookend |

## Timing notes (GATE T midpoint)

Major motion is kept out of each clip's 45–55% window via `until()` phrase
timing. Event phrases were chosen so landings fall early (B00–B02, B05–B06)
or late (B03 reply, B04 cards, B07 final page, B08 check). After Kokoro audio
is measured on the Mac, re-verify with the midpoint guard before the 4K run.

## Continuity

The same chat window opens B00, B01 (shifts right), B02 (closes), B03
(context lands inside it), and B05 (side panel grows beside it). The project
box of B04 is the film's one isometric object; everything else is flat UI in
the same palette.
