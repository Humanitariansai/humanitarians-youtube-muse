# ACTS.md — "Muse making a film about Muse" (claude-liam-lecture-muse-making-a-film-about-muse)

Lecture skill. Channel: claude-liam (Liam, in for Bear · Kokoro am_onyx · @NikBearBrown).
Title (exact, used verbatim in BOUT): "Muse making a film about Muse".
The title is the premise: this film about Muse was made by Muse. BIDEA may
nod to that once, plainly, then get on with the subject.
Source: the Muse product docs — `~/docs/muse.md` (primary),
`~/docs/client-surfaces.md`, `~/docs/data-handling.md` (supporting).
Full source list in SOURCES.md.

The film answers, in order: what Muse is, what it does, where you reach it,
how it is paid for. Self-contained: assumes the viewer knows nothing about
Muse. Narration never says "this chapter" or "the book".

## Bookends (fixed)

- **BIDEA** — hesitant writer. Liam's greeting spoken over it
  ("Hallo. This is Liam, in for Bear. …"), then what the topic is about in
  two or three plain sentences. Correction pair (trigger appears verbatim
  in the typed text): trigger "just another chatbot" → replacement
  "a personal agent".
- **BDEFS** — "Terms In This Lecture" (ClaudeDefinitions), 4 terms, one plain
  line each, in act order:
  1. `agent` — a program that works for you on its own
  2. `memory` — what it keeps about you between chats
  3. `skill` — one built-in thing it knows how to do
  4. `artifact` — a document, page, or app it builds for you
- **BVDT** — "Let's recap with Claude." after a 0.5 s lead pause; 4 lines
  (one bare sentence per act; never 5).
- **BHTF** — "Your turn." Prompt the viewer can paste: ask Muse to remember
  one preference, then recall it in a new chat. Two checks: it recalls it
  correctly; it offers to forget it on request.
- **BOUT** — ClaudeTitleOutro, @NikBearBrown (OUTRO-LOCK.md).

## ACT I — What Muse Is (the product)

Covers muse.md §§ Muse / Quick Facts.

1. A personal AI agent — everyone gets their own agent, running on its own
   dedicated computer. (muse.md)
2. Strictly personal — every conversation is between one user and their own
   agent; no group or shared chats. (muse.md)
3. Powered by Muse Spark, from Meta's Muse model family. (muse.md)
4. Launched September 8, 2026; available in the US and Canada. (muse.md)

Cast: "your agent" = one small computer mark, reused whenever the agent
itself is the subject.

## ACT II — What It Does (capabilities)

Covers muse.md (tabs, artifacts, files), data-handling.md (what it knows),
client-surfaces.md (tabs).

1. It talks with you — chat is the front door on every surface.
   (client-surfaces.md)
2. It remembers — conversations, preferences, and files carry between chats.
   (data-handling.md; memory)
3. It uses tools — skills and connectors: mail, calendar, shopping, media,
   paired devices. (muse.md skill list; client-surfaces.md)
4. It builds things — artifacts: documents, pages, and apps you keep.
   (muse.md; artifacts.md)
5. It keeps your stuff — files and the Library tab. (files-and-library.md)
6. It works while you are away — scheduled checks, Feed posts, Ideas, Goals.
   (client-surfaces.md tabs; scheduling docs)

## ACT III — Where You Reach It (surfaces)

Covers client-surfaces.md; muse.md (WhatsApp row).

1. The web app at muse.ai. (client-surfaces.md)
2. The iPhone and Android apps. (client-surfaces.md)
3. The Mac app — chat, plus it pairs your Mac as a device. (client-surfaces.md)
4. WhatsApp as a messaging channel. (muse.md; chat-connections docs)

Cast: surface marks — phone, laptop, desktop — one consistent set.

## ACT IV — How It Is Paid For (business model)

Covers muse.md § Subscriptions. Stated exactly as documented; no prices or
tier names are invented.

1. Free access with a usage limit. (muse.md)
2. Optional paid monthly subscription for more usage. (muse.md)
3. Subscriptions via muse.ai and the Apple App Store and Google Play Store;
   they renew monthly unless canceled. (muse.md)

## LEFT OUT (with reasons)

- Invite links / referral codes — real, but an aside; not what "what is Muse" needs.
- Per-platform Settings panes in detail — too granular; Act III covers the headline.
- Health-data sync specifics — niche capability, not core to the story.
- Voice and dictation mechanics — feature detail, not needed for the core.
- Data Controls / Reset mechanics — privacy detail; the film is about what
  Muse is and how it is paid for, not its settings screens.

## Runtime estimate (information only)

~14 body beats × ~10 s ≈ 140 s + bookends ≈ 60 s → roughly 3.5–4 minutes.
Length is an output; no target.
