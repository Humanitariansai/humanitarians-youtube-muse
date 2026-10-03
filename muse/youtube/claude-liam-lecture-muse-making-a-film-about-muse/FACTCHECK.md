# FACTCHECK.md — "Muse making a film about Muse" (Gate F)

Source of truth: `~/docs/muse.md` (primary), `~/docs/client-surfaces.md`,
`~/docs/data-handling.md`. Every number and named claim below was checked
against these docs. Nothing here is sourced from training data.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B01 | Everyone gets their own agent, running on its own dedicated computer | ✓ documented | muse.md: "Every user gets their own agent running on its own dedicated computer" | — |
| 2 | B02 | Every conversation is between one user and their own agent; no group or shared chats | ✓ documented | muse.md: "strictly personal … no group or shared chats" | — |
| 3 | B03 | Powered by Muse Spark, from Meta's Muse model family | ✓ documented | muse.md | Say "Muse Spark" only — never a version number |
| 4 | B04 | Launched September 8, 2026; available in the US and Canada | ✓ documented | muse.md | — |
| 5 | B05 | Chat on every surface | ✓ documented | client-surfaces.md: Chat tab on iOS, Android, web, Mac | — |
| 6 | B06 | It remembers: conversations, preferences, files carry between chats | ✓ documented | data-handling.md: "previous conversations, saved memories …" | Do not claim it remembers "everything" or "forever" |
| 7 | B07 | Skills/connectors: mail, calendar, shopping, media, paired devices | ✓ documented | muse.md skill catalog; client-surfaces.md | Name only skills in the catalog; no invented integrations |
| 8 | B08 | Artifacts: documents, pages, apps it builds for you | ✓ documented | muse.md | — |
| 9 | B09 | Files and the Library tab keep your stuff | ✓ documented | muse.md; files-and-library.md | — |
| 10 | B10 | Scheduled checks, Feed, Ideas, Goals — it works while you're away | ✓ documented | client-surfaces.md tabs; scheduling docs | — |
| 11 | B11 | Web app at muse.ai | ✓ documented | muse.md | — |
| 12 | B12 | iPhone and Android apps (App Store, Google Play) | ✓ documented | muse.md | — |
| 13 | B13 | Mac app pairs your Mac as a device | ✓ documented | client-surfaces.md: "pairs the user's Mac as a device" | — |
| 14 | B14 | WhatsApp as a messaging channel | ✓ documented | muse.md | — |
| 15 | B15 | Free access with a usage limit | ✓ documented | muse.md | — |
| 16 | B16 | Optional paid monthly subscription for more usage | ✓ documented | muse.md | — |
| 17 | B17 | Subscriptions via muse.ai, App Store, Google Play; renew monthly unless canceled | ✓ documented | muse.md | — |

## Deliberately cut / never claimed

- **Prices, tier names, plan details** — not in the docs I can vouch for; the
  film states only "free with a usage limit; paid monthly subscription for
  more." (Per muse.md, the subscription_status skill is the source of truth
  for plans and prices — not this film.)
- **Model version numbers** — "Muse Spark" only.
- **"End-to-end encrypted"** — false per data-handling.md ("Conversations are
  not end-to-end encrypted"); never claimed.
- **Mac app file-access details** — Bear's trust story is context for how
  this film got made, not film content. Not claimed.
- **Any capability not in the skill catalog or docs** — if it isn't
  documented, it isn't in the film.

## PROMPTS.md

No paid generation prompts. All visuals are Manim (free) or library Remotion
components (free). No Higgsfield or other paid beats.
