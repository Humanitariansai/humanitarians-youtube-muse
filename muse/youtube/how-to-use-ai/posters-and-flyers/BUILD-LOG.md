# BUILD-LOG.md — Posters and Flyers

Film #38, Wave 6 "Making things". Built 2026-10-05. Assignment: image
generation for real-world printables (garage sale, bake sale, side
business), companion to `pictures-from-words`, never quote pricing tiers.

## Skill decision

Kept the assigned **show-tell** skill — no switch. The teaching problem is
one workflow in four steps, each a visible thing/part/flow on the same two
cast objects (the poster, the picture frame), which is show-tell's home
ground. The card test was run per beat: no beat's idea is an interface, a
set of numbers, or a single word, so **zero ShowTellCards** — all 9 body
beats are drawings, per the skill's "menu, not a quota" rule. The "why a
card" column in SHOTLIST.md records the reason.

## Voice-code fix (standing bug)

Per-beat `voice` is the Kokoro code `am_onyx` on all 13 beats — never the
persona name. The "Muse"-as-voice bug that broke two Wave 5 films is
asserted against in `make_sheet.py` (`assert b["voice"] == "am_onyx"`).

## Narration care

- Greeting is "Hallo" (known-clean on Kokoro per the skill notes).
- No acronyms, version numbers, or spelled-out letters in narration; "A4 /
  letter" avoided in favour of "the tall shape paper is".
- Every on-screen word is read aloud in its beat (show-tell law).

## QC (recorded in CHECKS-REPORT.md)

- `python3 -m py_compile` clean on `make_sheet.py` and `scenes.py`.
- `static_scene_check.py` for all 9 scene classes, run from `/tmp/gatea/`
  holding only `scenes.py`: **0 warnings, 0 errors** on the first run.
- Two hand-review fixes made before the check: (1) short leader lines
  (B01, B04 zone 3, B06) removed or repositioned — a short leader reads as
  sub-floor text under GATE T; (2) fact chips in B02 auto-sized to text
  length and right-aligned so none overflow the ±6.2 safe area.

## Bookends

REMOTION patterns per the house convention: `BrutalistHesitantWriter`
(trigger "design" -> "draw the art for", no trailing punctuation),
`ClaudeDefinitions` (4 terms, all ≤ 17 chars), `ClaudeComposerAsk`
(greeting "Your turn.", two checks), `ClaudeTitleOutro` (kind
"outro_voice", 1.0 s tail). BVDT is a drawn recap beat, not a card.

## Push

All 12 files pushed to
`muse/youtube/how-to-use-ai/posters-and-flyers/` on
Humanitariansai/humanitarians-youtube-muse via `gh-put-file.py`, each
verified live with a Contents API read. Local `__pycache__` removed; no
MP3/MP4/WAV or secrets committed. README/QUEUE/FRICTIONAL.md untouched per
the standing rule.
