# SHOTLIST.md — Make It Interview You First

One scene per beat. Every body beat is a drawn Manim illustration (Claude
palette, cream stage); labels are 1–3 words beside objects or as captions
below (the approved card-row pattern), never inside an outline.
**No ShowTellCard beats** — every beat's idea is a thing, a part, or a flow,
so each fails the card test at question 1 ("is the idea an interface, a set of
numbers, or one word?"). The composer beat (BHTF) is the mandated bookend, not
a card choice.

The film's cast, kept whole: the composer card, question bubbles (white circle
+ terracotta dot), question cards, the iso brief box, answer pages, answer
chips, and the check.

| beat | scene class / pattern | the motion (the claim, in motion) | labels on screen | why not a card |
|---|---|---|---|---|
| BIDEA | BrutalistHesitantWriter | writer types the naive prompt question, backspaces "write the perfect prompt" → "make Claude interview me first" | — | bookend |
| BDEFS | ClaudeDefinitions | three terms land one by one | prompt · interview · brief | bookend |
| B00 | B00_AskOnce | composer lands; "plan my trip" types; a thin page grows above; "generic answer" lands | generic answer | the one-line ask / thin answer is a thing — drawn |
| B01 | B01_AskFirst | "Ask me 5 questions first." types into the composer; five question bubbles drop in; "the interview" lands | the interview | the move is a flow — drawn |
| B02 | B02_FiveQuestions | five question cards land in a row on each spoken word; a terracotta scan line sweeps under them | budget · dates · who · pace · must-see | the questions are the film's cast — drawn |
| B03 | B03_BriefBuilt | the brief box opens; five answer chips drop in one by one | your brief (chips: tight · November · 2 + 1 · slow · fish market) | answers-into-a-box is a flow — drawn |
| B04 | B04_TailoredPlan | brief box + thin dimmed generic page; arrow to a full tailored page that grows line by line; terracotta check stamps it | tailored plan | contrast of two pages is a comparison — drawn |
| B05 | B05_SecondDemo | envelope card; three question bubbles land; a finished letter page fades in with an ink check | difficult email | the email demo is a thing + flow — drawn |
| B06 | B06_SharpQuestions | a dimmed lazy card ("favourite colour?") gets a grey strike; a highlighted sharp card ("changes the answer?") lands with dot + check | ask what changes the answer | judging two questions is a comparison — drawn |
| B07 | B07_TheRule | two task cards: "your trip"/"your email" get bubbles + check; "Tokyo time?" gets a straight arrow + "skip" | needs you · skip | the rule is a flow — drawn |
| BHTF | ClaudeComposerAsk | composer opens; the prompt types in full; two check lines land | — | mandated bookend |
| BOUT | ClaudeTitleOutro | title restates; handle; 1.0 s tail | — | mandated bookend |

## Timing notes (GATE T midpoint)

Major motion is kept out of each clip's 45–55% window via `until()` phrase
timing. Event phrases were chosen so landings fall early (B00–B02 cards,
B03 chips start, B04 page) or late (B03 last chips, B04 check, B05–B07
labels). B02's cards land at roughly 15–30% of the narration; B03's later
chips may drift toward the midpoint depending on measured Kokoro pacing —
re-verify with the midpoint guard on Bear's Mac after audio is measured
(see CLAUDE-CODE-RENDER.md). No terracotta object is mid-motion at any
sampled point by design.

## Continuity

The same composer card opens B00 and B01. The brief box of B03 returns in
B04 (smaller, with chips inside, feeding the tailored page via an ink arrow).
The thin generic page of B00 returns dimmed in B04 for the contrast shot.
Question bubbles are the same prop in B01, B05, and B07.
