# FACTCHECK.md — Tame your inbox

Checked 2026-10-05. Verdicts: PASS, CORRECTED, EXEMPT (framing / craft advice
/ persona mechanics, no factual load). No invented statistics anywhere in the
film — every claim is behavioral and modest. No pricing, no version numbers,
no UI paths quoted verbatim (the film says "your unread email" and
"read-only" generically, so the advice survives redesigns).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | The naive mental model is letting the AI answer emails on its own; the real move is using it as a first-pass, supervised | EXEMPT | Framing of the film's premise; the correction is the pedagogy | — |
| 2 | B00 | The inbox is a pile: a few emails that matter buried in noise; it grows faster than you read it | EXEMPT | Framing metaphor; no statistics claimed ("hundreds" is the viewer's own inbox, not a study) | — |
| 3 | B00 | This film is the companion to the existing `talk-to-your-tools` film ("that one was about the plug") | EXEMPT | Reference to our own film; connectors are not re-taught per the brief | — |
| 4 | B01 | Hand the pile to Claude and ask "what actually needs me"; it reads the lot and sorts the real from the noise | PASS | Claude's Gmail connectors read email natively; per-chat connector toggles; citation-backed responses (same connector model as the companion film's claim 2, web search 2026-10-04) | Worded generically ("your unread email"), no vendor UI claims |
| 5 | B02 | Point it at a long thread and ask for the short version: what was decided, what's still open, what you owe someone | EXEMPT | Workflow advice; the three-line shape is craft guidance, not a product claim | — |
| 6 | B03 | It writes a draft reply in your voice from the thread; you read, fix, and send yourself — a draft is the AI guessing, a sent email is you acting | EXEMPT | Workflow advice; "in your voice" is what drafting assistance does, no guarantee claimed | — |
| 7 | B04 | Never let it send on its own: a draft is reversible, a sent email mostly isn't — keep the send button yours | PASS | Practitioner guidance: "Keep it at draft-only for anything it sends, and require yourself to press the button" (theaidownside/Instinct case, 2026); "gate customer-facing sends" (n8n community, 2026); "AI written emails are drafts at most — nothing should be sent without a thorough copy edit" (Inc., 2025); the companion film's send caution (web search 2026-10-04) | Voiced as the film's rule, not a product claim; "mostly isn't" avoids overclaiming about undo-send windows |
| 8 | B05 | Never let it delete on its own: the AI can't know which old email you'll need later; deleting is forever — archive instead, empty the trash yourself | EXEMPT | Craft advice; "deleting is forever" is the durable-email-hygiene framing, no technical claim about specific providers' retention | — |
| 9 | BHTF | The read-only first-run prompt; the two self-checks (sent folder empty; skim one original against the summary) | EXEMPT | Instructional prompt, not a factual claim | — |
| 10 | BIDEA | Greeting "Ciao" is voiced cleanly by Kokoro am_onyx | PASS | show-tell skill notes: "Ciao" is in the clean-greetings list (2026-09-27); whisper-check at render | — |

## Notes

- No plan/price/product claims are made, so nothing about Claude's 2026
  lineup can go stale. The film deliberately avoids naming connector
  settings paths (already covered in the companion film) and frames the
  first-pass as jobs you ask for, not background automation.
- "Inbox triage", "summary", "draft" definitions in BDEFS are simplified
  for a general audience; directionally correct, not technical definitions.
- The B04/B05 rules are voiced as the film's rules (plain Teardown), not as
  product limitations — they hold for any AI email tool.
