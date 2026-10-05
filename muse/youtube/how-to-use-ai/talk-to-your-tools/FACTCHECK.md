# FACTCHECK.md — Talk to your tools

Checked 2026-10-04. Verdicts: PASS, CORRECTED, EXEMPT (framing / craft advice
/ persona mechanics, no factual load). No invented statistics anywhere in the
film — every claim is behavioral and modest. No pricing, no version numbers,
no UI paths quoted verbatim (the film says "connectors settings" generically,
so the advice survives redesigns).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | The naive mental model is handing Claude your password; the real flow is connecting the app | EXEMPT | Framing of the film's premise; the correction is the pedagogy | — |
| 2 | B00 | Connectors let the chat reach into your apps (email, calendar) instead of you copying things over | PASS | Anthropic's Google Workspace connectors link Claude to Gmail/Calendar/Drive; Claude auto-detects which connector a question needs; per-chat connector toggles (web search 2026-10-04) | Worded generically ("your inbox, your calendar"), no vendor UI claims |
| 3 | B01 | You connect via connectors settings → pick the app → click connect → the app itself asks you to sign in; you never type your password into Claude | PASS | Walkthroughs: claude.ai → Settings → Connectors → Connect → sign in with Google → Allow on each permissions screen; "you sign in / authorize" (OAuth); easy path takes ~2 minutes (web search 2026-10-04) | "You never type your password into Claude" is the OAuth pattern, stated as the mechanism, not a guarantee about every future flow |
| 4 | B01 | "Same dance as logging into a new phone app with your Google account" | EXEMPT | Analogy for the OAuth sign-in pattern, not a factual claim | — |
| 5 | B02 | The permissions screen lists exactly what Claude may do (read email, read calendar, send email); reading is looking, sending is acting; start read-only | PASS | Connect walkthroughs describe reviewing permissions for "viewing, editing, and managing" calendar events and choosing individual permissions; connect flow shows per-permission Allow screens (web search 2026-10-04) | Exact permission labels not quoted (they are version-sensitive); the read-vs-send distinction is the durable part |
| 6 | B03 | The morning brief: ask every morning what's on and what needs a reply; Claude reads calendar + unread email and returns three lines | EXEMPT | Workflow advice; "automations" are framed as repeat jobs you ask for, not scheduled background tasks (no claim about scheduling features) | — |
| 7 | B04 | Inbox triage: ask what needs you; it sorts the real from the noise | EXEMPT | Workflow advice, behavioral, no guarantees | — |
| 8 | B05 | Meeting prep: pull the invite + the last thread, get a one-paragraph brief; companion to the meetings-into-notes film | EXEMPT | Workflow advice; the companion reference is to our own film | — |
| 9 | B06 | A draft is Claude guessing; a sent email is you acting — keep sending supervised | PASS | Practitioner guidance: "be cautious about the send function… the risk that Claude will send the wrong message to the wrong person, accidentally hit send instead of saving draft" (web search 2026-10-04) | Voiced as the film's rule ("the send button stays yours"), not a product claim |
| 10 | B07 | Give the smallest key that works; pull plugs you don't use; unused access is an unlocked door | PASS | Security-expert guidance for AI assistants with app integrations: "apply the principle of least privilege rigorously… If email sending capabilities are not essential, they should be revoked. Every additional integration expands the attack surface" (web search 2026-10-04) | — |
| 11 | B08 | Once connected, Claude reads everything in the app — including a stranger's invite; a stranger can hide instructions in an invite that try to steer the AI; delete weird invites | PASS | Documented attack vector: LayerX research — a malicious Google Calendar event makes Claude carry out embedded instructions (The Register, Feb 2026); "Invitation Is All You Need" study (Aug 2025) — calendar-invite prompt injection demonstrated against production AI assistants (web search 2026-10-04) | Worded without product names or CVE-style specifics; the defensive advice (don't accept, don't ask about, delete) matches the experts' hygiene guidance |
| 12 | BHTF | The read-only first-run prompt; the two self-checks (sent folder empty; connectors show read-only) | EXEMPT | Instructional prompt, not a factual claim | — |
| 13 | BIDEA | Greeting "Hallo" is voiced cleanly by Kokoro am_onyx | PASS | show-tell skill notes: "Hallo" is in the clean-greetings list (2026-09-27); whisper-check at render | — |

## Notes

- No plan/price/product claims are made, so nothing about Claude's 2026
  lineup can go stale. The film deliberately avoids naming the "Manual/Auto"
  permission modes and scheduled-task features (both version-sensitive) and
  frames automations as jobs you ask for.
- "Connector", "permissions", "automation" definitions in BDEFS are
  simplified for a general audience; directionally correct, not technical
  definitions.
- The B08 warning is intentionally one beat, plain words, no lecture —
  the mechanism (hidden instructions in an invite) is real and documented,
  the advice (delete) is the experts' own.
