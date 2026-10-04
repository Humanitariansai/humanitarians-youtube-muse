# BUILD-LOG.md — Set it up once

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- ~21:45 — Received the assignment from the parent orchestrator: film #23
  of 24, slug `set-it-up-once`, working title "Set it up once", pitch
  "Custom instructions: teach the AI your preferences a single time", NEW
  source (build from scratch), assigned skill `show-tell`. Pre-render
  package only: 12 files, pushed to
  `muse/youtube/how-to-use-ai/set-it-up-once/` on
  Humanitariansai/humanitarians-youtube-muse.
- ~21:50 — Read `skills/make/show-tell/SKILL.md` end to end (spine, the nine
  laws, the card test, the drawing laws, the gate traps). Read the iso_kit
  template (`templates/iso_kit.py`, 144 lines) verbatim.
- ~21:55 — Studied the two sibling show-tell films already in the queue
  (`ai-is-a-slot-machine`, `how-to-rot-your-brain-with-ai`) via the Contents
  API: the beat-sheet format (metadata + beats with beat_id/narration_text/
  estimated_duration_s/lane/shot), the bookend remotion props
  (BrutalistHesitantWriter, ClaudeDefinitions, ClaudeComposerAsk,
  ClaudeTitleOutro), and the make_sheet.py assertion pattern. The brain-rot
  film follows the pure show-tell contract (no BVDT, bookend_exempt
  cold-open + bvdt); this film copies that contract. [record]
- ~22:00 — **Skill choice: show-tell** (staying with the assignment, not
  switching). The film teaches one practical action (open settings, write a
  few lines, done) — the exact show-tell shape: one drawing per beat, the
  voice explains, show the setting and the payoff demo. The card test was
  run per beat: every body beat's idea is a thing (the note), a part (its
  lines), or a flow (note → chats) — all drawn from the film's own cast, so
  no beat passed the test. Zero cards, all drawings. [judgment]
- ~22:05 — Fact-check research (web search, 2026-10-03): ChatGPT Custom
  Instructions (Settings → Personalization, two fields, applied to new
  chats — OpenAI help docs via third-party guides); Claude Personal
  Preferences (Settings → General) + Projects instructions; Gemini
  "Instructions for Gemini" (Settings & help → Personal Intelligence) +
  Gems. Deliberate rot-proofing: the film never names a product's menu path
  on screen or in narration — only "settings, or your profile" and the
  candidate words (instructions / personalization / memory). No statistics
  quoted anywhere. Full record in FACTCHECK.md. [record]
- ~22:10 — Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md, PROMPTS.md
  (paperwork before the first run, per Gate F).
- ~22:15 — Wrote make_sheet.py. First run passed all assertions: 13 beats
  (BIDEA, BDEFS, B00–B08, BHTF, BOUT), 9 manim + 4 bookend lanes, total
  211 s (~3m31s, inside the 200–320 s band); BIDEA trigger contract, BDEFS
  17-char term contract, BHTF prompt-read-in-full contract, BOUT
  outro_voice + 1.0 s tail all green. [record]
- ~22:20 — Wrote scenes.py: iso_kit pasted verbatim (144 lines) + film
  helpers (chat_window, bubble, note, settings_panel, kw_pill, xmark,
  zigzag, pencil, cable, arrowhead) + 9 scene classes B00–B08. Cast: the
  pinned note recurs in every body beat from B01 on.
- ~22:25 — QC gate run 1: `python3 -m py_compile` clean on both files;
  static_scene_check.py per class in a scratch folder holding ONLY
  scenes.py (exactly what Gate A sees): 8 clean, 1 warning — B01_TheNote
  placed the note's terracotta pin dot at y=3.87, outside the safe area,
  during its drop-in. Fixed by starting the drop at y=2.4 (pin at 3.32,
  inside ±3.4). [record]
- ~22:28 — QC gate run 2: 9/9 classes clean · 0 warnings · 0 errors.
  Re-ran B03 and B07 with beat_sheet.json beside scenes.py to exercise the
  real until()/finish() pacing path: still clean. (Full record in
  CHECKS-REPORT.md.) [record]
- ~22:30 — Pre-gate review notes: every explicit coordinate kept inside
  ±6.2 × ±3.3; all type ≥ 32; labels beside objects; terracotta rationed
  (pins, checks, X marks, edit dot only); cables edged in deep kraft
  #9C8462; no rate_functions; MoveAlongPath + ArcBetweenPoints only;
  every until() phrase verified verbatim in its beat's narration_text;
  class names literally `class BNN_Name(Scene):`.
- ~22:35 — Wrote CLAUDE-CODE-RENDER.md, README.md, BUILD-LOG.md,
  CHECKS-REPORT.md. Noted in the render prompt that
  `manim_layout_audit.py --curve-strict` cannot run in this VM (no
  Manim/pangocairo) and is deferred to Bear's Mac render pass.
- Next: push the 12 files via gh-put-file.py; verify each via Contents API
  reads; report back with the FRICTIONAL.md entry.

**Not done (by design).** Pre-render package only: no audio generated, no
Manim render, no assembly, no publish. Render instructions for Bear's Mac
in CLAUDE-CODE-RENDER.md.
