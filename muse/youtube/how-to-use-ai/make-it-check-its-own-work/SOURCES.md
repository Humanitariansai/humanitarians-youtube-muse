# SOURCES.md — "Make It Check Its Own Work."

Build source: NEW — built from scratch for the humanitarians AI YouTube
channel "How to AI" series. No mirror source. Skill: show-tell (iso_kit
pasted at the top of scenes.py; no imports — Gate A copies only scenes.py).

## Primary sources for the technique

Self-critique / self-check prompting is documented in vendor and
community prompt-engineering guidance:

1. Anthropic's prompt-engineering documentation — the self-check pattern
   ("Before you finish, verify your answer against [test criteria]"),
   described as catching errors reliably, especially for coding and math;
   also "Ask Claude to self-check." Quoted and summarized in the
   prompt-engineering notes below.
2. Google's prompting strategies — self-critique ("prompt models to review
   outputs against original constraints"). Cited in the prompt-engineering
   notes below.
3. https://github.com/obrelix/what-lurks-within/blob/HEAD/claude-opus-4.6-prompt-engineering-guide.md
   — "Self-Verification and Critique": "Have Claude review and improve its
   own output" (prompt chaining for quality improvement).
4. https://blog.reviewaitool.com/2026/04/04/anthropic-claude-tips-tricks-2026/
   — the reviewer technique: get a draft, then ask the model to act as a
   reviewer, critique it, and revise; warns that vague "make it better" is
   too vague and needs a specific role and goal.
5. https://github.com/ilyaivanchikov/mendbot/blob/HEAD/docs/prompt-engineering-best-practices.md
   — "Self-Check / Sanity Check": ask the model to verify its own
   conclusions before finishing; sources given as Anthropic ("Ask Claude to
   self-check") and Google ("Self-critique").
6. https://github.com/mib-dotnet/llm-prompting-blueprint
   — "Encourage the model to review or critique its own output"; "Re-ask
   with 'improve this' on its own answer."
7. https://github.com/huangeddie/dotfiles/blob/HEAD/dot_agents/packages/exact_coding/exact_skills/prompt-engineering/resources/anthropic.md
   — "Ask Claude to self-check"; notes the nuance that models with
   always-on reasoning verify their own work well without explicit
   instruction.

## The demo

The "which months have 28 days?" riddle is a long-standing logic riddle;
the film uses it as a staged demonstration of the critique move, not as a
research finding. February has 28 days (29 in leap years); all other months
have 30 or 31 — so all twelve months have at least 28 days.

## What is NOT sourced

No accuracy-improvement statistics are claimed anywhere in the film; the
"reduces errors, doesn't eliminate them" framing is the author's judgment
(see FACTCHECK.md). The email redraft in B04 is an illustrative example
written for the film, not a documented case.
