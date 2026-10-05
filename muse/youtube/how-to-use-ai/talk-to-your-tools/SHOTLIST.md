# SHOTLIST.md — Talk to your tools

One scene per beat. Every body beat is a drawn Manim illustration (Claude
palette, cream stage); labels are 1–3 words beside objects, never inside them.
**No ShowTellCard beats** — every beat's idea is a thing, a part, or a flow,
so each fails the card test at question 1 ("is the idea an interface, a set of
numbers, or one word?"). The composer beat (BHTF) is the mandated bookend, not
a card choice.

The cast: one chat window (cream card, dark title strip, composer pill), one
plug on a deep-kraft cable, one email app card, one calendar page, and — for
the warnings — the ink SEND pill, the tray, and the stranger's invite card.

| beat | scene class / pattern | the motion (the claim, in motion) | labels on screen | why not a card |
|---|---|---|---|---|
| BIDEA | BrutalistHesitantWriter | writer types the naive password question, backspaces "give Claude my passwords" → "connect Claude to my tools safely" | — | bookend |
| BDEFS | ClaudeDefinitions | three terms land one by one | connector · permissions · automation | bookend |
| B00 | B00_TheGap | window + email card + calendar page land; two fragments slide into the composer (the copying); a kraft cable draws across the gap | the gap | the gap/copying is a flow — drawn |
| B01 | B01_ThePlug | the plug slides into the socket on the email card; a sign-in shield with an ink check pops | the plug | the sign-in dance is a flow — drawn |
| B02 | B02_Permissions | the two read rows land with terracotta checks; the send row lands with an ink X | permissions | a permission list is a thing — drawn |
| B03 | B03_MorningBrief | kraft lines draw from calendar + email to a brief card that grows with three lines; terracotta dots land | morning brief | sources-to-brief is a flow — drawn |
| B04 | B04_InboxTriage | the inbox card splits into two stacks: "needs you" (ink) and "noise" (dim); a check lands on what matters | triage · needs you · noise | sorting is a flow — drawn |
| B05 | B05_MeetingPrep | kraft lines draw from invite + thread; the prep card grows with a paragraph; a terracotta dot lands | meeting prep | sources-to-brief is a flow — drawn |
| B06 | B06_YouSend | the draft card grows; the ink SEND pill lands; an ink lock lands over the pill | you send | the guarded button is a thing — drawn |
| B07 | B07_PullThePlug | the plug slides out of the socket along its cable and lands in the tray; a check stamps the tray | pull the plug | unplugging is a flow — drawn |
| B08 | B08_StrangerInvite | the stranger's invite drops in; an ink X stamps it; the card slides off stage | strangers' invites | the rejection is a flow — drawn |
| BHTF | ClaudeComposerAsk | composer opens; the prompt types in full; two check lines land | — | mandated bookend |
| BOUT | ClaudeTitleOutro | title restates; handle; 1.0 s tail | — | mandated bookend |

## Continuity

The same chat window opens B00 and its cable crosses the gap; the same plug
pushes into the email card's socket in B01 and is pulled out of it in B07.
The email card and calendar page recur as the sources in B03 and B05. The
kraft cable is deep kraft (`#9C8462`) throughout — never ink-edged, so it
never fuses with the dark socket under GATE T.

## Timing notes (GATE T midpoint)

Major motion is kept out of each clip's 45–55% window via `until()` phrase
timing. Event phrases were chosen so landings fall early (B01 plug, B02
read rows, B05 kraft lines) or late (B00 fragments + cable, B03 brief card,
B04 split, B06 SEND pill, B07 plug pull, B08 X stamp). B04's split uses
`lead=0.5` on "what actually needs me" to finish before the window. After
Kokoro audio is measured on the Mac, re-verify with the midpoint guard
before the 4K run.

## Label traps checked by hand

- Labels sit beside objects with ≥ 0.3 leader gaps (the `tag()` helper
  stops the leader 0.35 short); no leader touches its label.
- Terracotta appears only on dots, checks, and the B00 cable spark — never
  under text, never as text (the X stamps and the "?" are ink).
- All coordinates inside ±6.2 × ±3.3; type ≥ 32.
- Every beat has a label up by its midpoint (B04's "triage" tags the
  needs-you stack before the split; B08's "strangers' invites" lands with
  the invite).
