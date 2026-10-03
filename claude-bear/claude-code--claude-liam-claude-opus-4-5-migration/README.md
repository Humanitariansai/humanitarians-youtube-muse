# Migrating to Opus 4.5

Say your code calls Claude on Sonnet 4.0, Sonnet 4.5, or Opus 4.1, and it's
time to move it to Opus 4.5. The natural guess is that "migrate" also means
Claude quietly smooths over anything that behaves differently on the new
model — it doesn't. The skill touches exactly four things: a model string, a
beta header, one parameter, and a summary. Watch one line of code go from
Sonnet 4.5 with a beta context header to Opus 4.5 with the header gone and
effort set to high — nothing else touched. It searches your whole codebase
first, updates the right string for whichever platform you're on (Anthropic
API, AWS Bedrock, Google Vertex AI, or Azure AI Foundry), and leaves every
Haiku call exactly where it is, on purpose. If your code only ever called
Sonnet or Opus, that's the whole job in one pass. If Opus 4.5 actually
behaves differently once it's running, the skill won't touch your prompt for
that on its own — you report the specific behavior, and only then does it
make a targeted adjustment.

**Topic:** CLAUDE CODE · MODEL MIGRATION
**Playlist:** Claude Code
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-code--claude-liam-claude-opus-4-5-migration

---

## Chapters

0:00 The naive framing: "how do I upgrade my code to Opus 4.5?"
0:12 Time to move models
0:20 The natural guess
0:27 Four things, nothing else
0:37 The anchor: one call, before
0:46 Search, then update every platform
1:00 Two edits that ride along
1:07 One model stays put
1:14 The anchor returns: one call, after
1:26 The clean case
1:33 Opt-in, never by default
1:47 Carry-out
1:55 Your turn
2:24 Outro

---

## YOUR TURN

Search this codebase for Claude model strings and migrate them to Opus 4.5 —
Anthropic API, AWS Bedrock, Google Vertex AI, or Azure AI Foundry, whichever
you use. Remove any one-million-token-context beta header you find, add an
effort parameter, and summarize every change.

Run that on your own codebase, and watch two things: does it leave every
Haiku string untouched, and does it change so much as one word of your
prompts without asking first?

---

## Deliberately not claimed

No claim that Azure AI Foundry has a documented source-string table (the
skill's own platform matrix pairs it with a target string only). No specific
reproduction steps for "tool overtriggering" or the other opt-in behavioral
adjustments — they're named as illustrative examples, not guaranteed
symptoms. No claim that migration carries a rollback path; the video simply
doesn't raise it.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ModelMigration #Opus45 #LLM #HumanitariansAI #ProfessorBear

---
