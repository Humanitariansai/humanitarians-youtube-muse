# BUILD-LOG.md — "Claude, Not Your Answer."

## 2026-10-03 — build session

**Source read.** Fetched `beat_sheet.json`, `README.md`, `PEDAGOGY.md` from
the mirror repo (`nikbearbrown/humanitarians-youtube-muse`,
`claude-for-artificial-intelligence/hai-not-your-answer/`) via the Contents
API. The source is an 11-beat film, "Stop using your own Claude at work":
Samsung leak → training-by-default mechanism → per-app toggle paths →
legal framings → clean-room policy. Ignored `mp3/` (never download audio).

**Skill choice: show-tell.** [judgment] The subject is a behavior plus a
settings walkthrough — a case, a mechanism, a switch, a rule. Every beat
draws as one isometric illustration (chat window, documents, toggle, seals,
shield). cc-explainer was wrong (no terminal session); lecture/deep-explainer
too heavy for a 3-minute how-to. Zero cards: the card test answered "no" on
every beat — the film's own cast shows each idea more clearly.

**Rewrite.** 13 beats: BIDEA (hesitant writer; naive question corrected),
BDEFS (training / retention / clean room), 9 drawn body beats, BHTF
(composer with an audit prompt), BOUT (spoken outro). The old VERDICT recap
and the wall-of-text cold-open prompt were dropped per the show-tell
bookends. Narration written at ~150 wpm; estimated total 186.4 s.

**Fact-check.** All 12 claims checked via web search on 2026-10-03 into
FACTCHECK.md: Samsung timeline PASS (The Register, Android Authority,
Gizmodo, The Investor); Anthropic Sept-2025 training/retention change PASS;
per-app toggle paths PASS against mid-2026 guides; Claude's exact toggle
label flagged version-sensitive (voiced generically); legal framings marked
QUALIFY (analysis, not advice, voiced with "I am not a lawyer").

**Scenes.** `scenes.py` = iso_kit.py pasted verbatim at top (per skill: Gate
A copies only scenes.py) + film helpers (`doc`, `chat_window`, `toggle`,
`x_mark`, `lab`) + 9 scene classes `B00_*`…`B08_*`. Coordinates kept within
±6.2 × ±3.3; type floor 32; labels beside objects; terracotta only for dots,
the shield check, and tape.

**QC.** `python3 -m py_compile` clean on both files. Static QC
(`static_scene_check.py --class <C>`) run for all 9 classes: **9 clean ·
0 warn · 0 error on the first run** — no fixes needed. Details in
CHECKS-REPORT.md.

**Docs.** ACTS, SHOTLIST (with "why a card" column), FACTCHECK, SOURCES,
PROMPTS ("no generation prompts"), CLAUDE-CODE-RENDER, README — 12 files
total in `~/workspace/film-builds/how-to-use-ai/claude-not-your-answer/`.

**Push.** All 12 files pushed to
`Humanitariansai/humanitarians-youtube-muse` under
`muse/youtube/how-to-use-ai/claude-not-your-answer/` via
`gh-put-file.py`; each verified live with a Contents API read (HTTP 200).

**Not done (by design):** no narration audio, no renders, no staging, no
publishing. Pre-render package only. Render steps for Bear's Mac are in
CLAUDE-CODE-RENDER.md.
