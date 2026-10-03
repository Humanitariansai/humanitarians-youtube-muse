# Claude, Listener Creator.

A Skill's "listener" isn't a live watcher hovering over your inbox — it's a
file Claude writes describing one condition, that fires later when an email
matches it. The `listener-creator` skill is two files: a `SKILL.md`
instruction set (plain text, about nine kilobytes) and a `templates` folder
— no live process, no hidden logic. `SKILL.md` has a Steps section Claude
works through top to bottom: read the request, write the condition, return
the definition. Ask for a listener that flags any email from your boss
marked urgent and forwards it right away, and the skill writes exactly that
condition into a file — from then on, the same forward fires every time an
email matches boss and urgent, because the condition in the file doesn't
change. The same fact cuts the other way: an equally urgent email from a
client never fires it, because "client" was never written into the
condition. A listener matches the words in the file, not how urgent an
email actually feels.

**Topic:** SKILLS · LISTENER-CREATOR
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-agent-sdk-demos--claude-liam-listener-creator

---

## Chapters

0:00 A Skill must be some live watcher scanning my inbox. Is that it?
0:12 A folder, not a watcher
0:30 Steps, top to bottom — the anchor
0:49 Reliable — then out of scope
1:19 Carry-out
1:33 Your turn
1:49 Outro

---

## YOUR TURN

"I want a listener that flags any email mentioning a contract renewal and
forwards it to my legal team. Read the listener-creator skill and walk me
through what you'll do before you do it — show me exactly which condition
you're writing into the file."

Why it's worth running: asking Claude to name the condition before it
writes the listener surfaces the constraint logic directly — you see the
Steps section working exactly as this reel describes, on your own request.

---

## Deliberately not claimed

Not a verdict on whether this design is good or limiting — that's Teardown
territory; this reel states the mechanism and the boundary, and stops. Not
a claim that every Skill shares this exact file layout — `listener-creator`'s
`SKILL.md` + `templates` folder is this reel's worked example. Not a claim
that a listener's condition can never be written more broadly — only that
its current definition matches only what's currently in the file.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
