# FACTCHECK.md — Make it remember (and forget)

Every claim in the script was checked before writing (2026-10-04). No
statistics are quoted anywhere in the film, so there are no numbers to
verify. No pricing, no version numbers, no model names.

## Verified (record)

1. Claude saves memory as individual topics while you chat; the full list
   sits under Topics in Settings → Memory, where each can be read, edited,
   or deleted. → Engadget "How to edit Claude's memory"
   (engadget.com/2246397), TechRepublic "Claude Memory Now Follows You Into
   Cowork" (2026-08/09), corroborated by BigGo and SparkOne, 2026-10-04
   [record]
2. Memory is enabled by default for Free, Pro and Max users on web,
   desktop, and mobile. → Engadget, TechRepublic, AndroidAuthority
   (claude-cowork-shares-memory-with-chat-3702922), 2026-10-04 [record]
3. Claude adds topics to memory *as you chat*, instead of summarizing
   conversations after they end (Anthropic announcement 2026-08-25). →
   SparkOne, BigGo, AndroidAuthority, 2026-10-04 [record]
4. "Include sensitive topics in memory" is off by default; health, race,
   ethnicity, religious beliefs, politics, gender identity are not stored
   unless the user opts in. → TechRepublic, BigGo, AndroidAuthority,
   2026-10-04 [record]
5. Even with sensitive topics on, some things are never stored:
   government-issued ID numbers, Social Security numbers, criminal history,
   immigration status, anything violating the acceptable use policy. →
   BigGo and AndroidAuthority quoting Anthropic, 2026-10-04 [record]
6. Pause keeps existing memories stored but stops Claude using them and
   creating new ones; Reset permanently deletes all stored memories
   (including project memories) and cannot be undone. → TechRepublic,
   2026-10-04 [record]
7. "Search and reference chats" (retrieving info from old conversations)
   is separate from memory and has its own setting. → TechRepublic,
   2026-10-04 [record]
8. Incognito chats do not use existing memory and do not add new memories.
   → TechRepublic, 2026-10-04 [record]
9. Edit path: Settings → Memory → Topics → Edit/Delete icons (web);
   mobile: profile → Settings → App → Capabilities → Memory files. The
   film's "Settings, then Memory, then Topics" matches the verified web
   path. → Engadget, 2026-10-04 [record]
10. Correcting a stored detail (e.g. a company name) applies to future
    conversations. → iclarified and kucoin coverage of the Anthropic
    announcement, 2026-10-04 [record]
11. Each Claude Project has its own memory space; what is created inside a
    project stays there. → dev.to
    "The Memory in ChatGPT and Claude, and Where It Stops" (2026-09),
    2026-10-04 [record]

## Judgments (judgment)

- "Deleting the chat doesn't delete the note" is an inference from the
  verified structure: topics live in a separate store (Settings → Memory →
  Topics), not inside chats, so deleting a chat cannot remove the topic.
  The ChatGPT parallel is explicit (dev.to: "deleting a conversation does
  not delete what ChatGPT learned about you from it"). [judgment]
- The note-card examples ("café in Lisbon", "bullet points", "Ana: short
  updates", "deadline: Friday") are my illustrations of keep-worthy notes,
  not quoted from any product's docs. [judgment]
- "Passwords, card numbers, door codes" as secrets that never belong in a
  chat that becomes memory is advice grounded in the never-stored
  categories plus ordinary security prudence — no product documents this
  specific list. [judgment]
- "The test: would a future chat thank you for this?" is my decision
  framework for what to store — advice, not a product fact. [judgment]
- The notebook drawings are schematic illustrations of the documented
  behaviors (pause shelves, reset empties, incognito turns the note away),
  not screenshots or claims about exact UI. [judgment]
- The film does not claim edits are retroactive or that memory applies to
  other companies' products; the settings path is Claude-specific and
  stated as such. [judgment]

## Cut or disclosed

- Incognito nuance: TechRepublic notes incognito chats are still retained
  30 days by default — memory is a separate matter from chat retention.
  The film says "leaves no trace in memory", which is the verified claim;
  the retention caveat is recorded here, not in the film. [record]
- The Cowork shared-memory announcement (2026-08-25) is context for the
  feature's scope but was cut from the film to keep it about the one
  habit: check the notebook. [judgment]
- "ID numbers" in the narration needs a Kokoro whisper-check (see
  CLAUDE-CODE-RENDER.md). [my input]
