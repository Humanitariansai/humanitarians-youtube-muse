# BUILD-LOG — claude-code--claude-liam-agent-development

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-code/youtube/claude-liam-agent-development/beat_sheet.json`
— a fully-built Teardown reel (7 beats, the Claude Code plugin-dev
`agent-development` skill, `claude-liam` / @NikBearBrown). `source_dir` in
SUBJECT.json pointed at a `/Users/bear/...` path that doesn't exist on this
machine; found the equivalent content at
`anthropics/claude-code/youtube/claude-liam-agent-development/` locally and
read it plus PEDAGOGY.md/SOURCES.md in full before writing anything. Never
touched the source reel's folder.

**Facts kept unchanged:** an agent is one markdown file — YAML frontmatter
(name, description, model, color, optional tools) plus a markdown body that
becomes the system prompt; the description field is the trigger and needs
"Use this agent when" plus two to four examples (Context/user/assistant/why),
or the agent won't fire reliably; model defaults to "inherit"; color has six
semantic options; tools follow least privilege (omit = full access); the
system prompt is five sections (Responsibilities/Process/Standards/Output/
Edge Cases) written in second person; validation rules are concrete (name
3-50 chars, etc.); there is no agent-vs-command decision tree, no
model-selection heuristic, and no multi-agent handoff guidance in the source
skill.

**Beat-count note (redo):** source is 7 beats (B00 cold open, B01 anatomy,
B02 description field + creation paths, B05 Teardown gets-right/bites, BVDT
verdict, BHTF handoff, BOUT outro — B03/B04 unused in the source). Kept the
same count (7) with a 1:1 remap: B00 → BrutalistHesitantWriter; B01/B02 kept
as the two mechanism beats with judgment language dropped; B05's Teardown
"gets right / where it bites" framing recast as B03, a neutral
BOTH-DIRECTIONS beat (precise in the file format, open in the judgment
calls) — same underlying facts, no design verdict, which is the correct
Plain-register home for that content; BVDT (verdict) became BCRY
(carry-out); BHTF/BOUT kept as Your Turn and outro, outro re-skinned to
Humanitarians AI. No beat in the source was AI-VIDEO, pantry, or a
human-drop slot (B00 was already Remotion `ClaudeComposerAsk`), so
NO-GENAI/NO-PANTRY LAW required no beat substitution.

WRONG-GUESS LAW note: with only 7 beats locked by the redo contract, there
was no beat to spare for a dedicated wrong-guess beat separate from B00. The
hesitation IS the wrong guess (WRITER LAW); the correction is picked back up
explicitly at the carry-out (BCRY) instead of in its own body beat — a
deliberate compression under the beat-count constraint, logged in
SCRIPT.md's six-move audit.

**B00 WRITER LAW:** misconception — a plugin builder reaches for "command"
when they actually need an agent (a command only runs when typed; an agent
keeps going on its own through several steps). Typed text: "I need a Claude
Code command for this. / How do I add it?" trigger "command" → replacement
"agent". First render (text: "...command that runs / this task for me. /
How do I add it?", charMs 46/hesitateBetween 12/hesitateWithin 2/mistakeRate
5) ran out of its 10.2s window before the final line typed — verified by
pulling frames at t=7s, t=9.7s, and t=10.05s: the correction landed but "How
do I add it?" never appeared. Fixed at the root: shortened the text (dropped
"that runs / this task for") and sped up the performance (charMs 46→42,
hesitateBetween 12→8, mistakeRate 5→3, jitter 26→22). Re-rendered just B00
(`--only B00 --force`) and reverified: at t=6s "How do" is already typing,
correction ("command"→"agent") visible from ~t=7s, full question "How do I
add it?" complete with the caret by t=9.9s of 10.2s.

**Body beats:** all 3 (B01-B03) built as Manim GRAPHIC scenes, reusing
verbatim the generic "chip row" renderer from the sibling hai-simple reel
`books--claude-liam-building-plugins/scenes.py` (title + up to 5 labeled
chips, optional arrows, optional accent/strike, caption) driven by a
per-beat content dict — not hand-tuned custom scenes. Anchor: B02 plants the
Python security-review agent example ("USE THIS AGENT WHEN" → "2-4 EXAMPLES"
→ "TRIGGERS RELIABLY", accented), paid off at BHTF where the viewer builds
exactly that agent and checks it against the same four criteria the beat
implies. B03 uses `strike` (dimmed MUTE text, not a literal strikethrough
line, per the sibling reel's documented GATE T fix) to mark "MODEL CHOICE"
and "AGENT VS COMMAND" as open/left-to-you against the three precise-format
chips. Close: BCRY `WantQuote` (carry-out), BHTF `ClaudeComposerAsk` (the
source's verbatim Your-Turn prompt, explicit `folderLabel: "@HumanitariansAI"`
per the known ClaudeComposerAsk-defaults-to-@NikBearBrown bug), BOUT
`OutroCTA` (@HumanitariansAI).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (7 beats), `scenes.py` (chip-row Manim generator ported from
the sibling reel + 3-beat content table), `render_scenes.py`. Ran
`generate_audio_kokoro.py` (7/7 beats, am_onyx, $0.00) — measured durations
became the clock. Rendered 3 Manim beats (foreground) and 4 Remotion beats
via `remotion_scenes.py` (both invocations exceeded the tool's 120s
foreground timeout and were auto-moved to background by the harness; blocked
on `TaskOutput` until each returned exit code 0 before proceeding — no
render step was left running unsupervised).

**GATE T (type_check.py) first pass: 1 FAIL.** B03 kerning §8.4: max
inter-glyph gap 337px > threshold 56px. Diagnosed by pulling frames at t=3s
and t=5s and reading them directly: all five chip labels ("NAME RULES",
"EXAMPLE FORMAT", "PROMPT SECTIONS", "MODEL CHOICE", "AGENT VS COMMAND") and
the caption ("spelled out on the left; your call on the right") render
correctly kerned and fully legible — this is the same documented
false-positive class as `books--claude-liam-building-plugins`'s BDNB08Scene
and several other sibling reels already in `KERNING_EXEMPT_PATTERNS`: the
peak-ink row spans multiple separate chip labels at the same y-band, so the
box-to-box gaps between chips (not actual Pango kerning failures) get
misread as one oversized inter-glyph gap. Font is named (Montserrat chips /
EB Garamond caption) in every `Text()` call; structural Pango check already
passed. Added `BPB03Scene` to `type_check.py`'s `KERNING_EXEMPT_PATTERNS`
with the verification recorded inline, matching the established precedent —
never a blanket loosening, only this independently-reverified scene.

**GATE T (type_check.py) final pass: PASS, 0 FAILs.**

Compiled with `compile.py .`: 7/7 beats real (no slate), master born
natively 4K (3840×2160, `compile.py`'s 4K LAW), 116.66s runtime, tail
silence +1.0s on BOUT applied. `content-check`/`frame-check`/`lane-check`
all PASS. `GATE AUDIO: PASS mean_volume -24.0 dB` (compile.py's own gate).

**Gate V:** pulled 15 frames at 8s spacing across the full 116.66s runtime
and read every one directly. B00's correction and full final question land
inside the beat with margin (verified separately above). The B02 anchor
(USE THIS AGENT WHEN → 2-4 EXAMPLES → TRIGGERS RELIABLY, accented) and B03
(precise/open split, two chips dimmed) both read cleanly. BCRY carry-out
card, BHTF (`ClaudeComposerAsk` correctly shows `@HumanitariansAI`, not the
Root.tsx default `@NikBearBrown`), and BOUT (`OutroCTA`, correct title +
handle) all centered, legible, safe-inset, no text overlap. No remaining
blockers.

**Audio (independently reverified beyond compile.py's own gate):** ffprobe
confirms an AAC mono stream at 48kHz present; master mtime
(1787977988) newer than beat_sheet.json (1787977866); `ffmpeg -af
volumedetect`: mean_volume **-24.0 dB**, max -2.9 dB — comfortably above the
-40 dB floor. Resolution confirmed 3840×2160 via ffprobe.

Metadata file written: `claude-code--claude-liam-agent-development.md`
(channel @HumanitariansAI, **Playlist: Claude Code** — SUBJECT.json's
`family` is `"claude-code"`, a direct match in
`skills/make/hai-simple/loop/playlists.json`'s map). Per the DELIVERY
CONTRACT format, the description also carries the direct code link.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-29 — Phase 4 delivery

Master is already 3840×2160 natively (compile.py's 4K LAW), so the
Fellows-facing 4K file is the same render, copied to the `-4k` filename
`deliver.py` expects.
