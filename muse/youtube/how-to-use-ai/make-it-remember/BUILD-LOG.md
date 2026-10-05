# BUILD-LOG.md — Make it remember (and forget)

## 2026-10-04 — build

**Assignment:** film #24 of the "How to AI" series, slug `make-it-remember`,
working title "Make it remember (and forget)", pitch "Memory features: what
to store, what never to store, and how to delete it." Assigned skill:
`cc-explainer`. Audience: smart general, not AI experts; 3–6 min; no pricing
tiers; privacy claims verified. [record]

**Skill decision (recorded here per the assignment's switch allowance).**
Read `cc-explainer/SKILL.md` first. Its TERMINAL-FIRST law requires the body
to be a reconstructed `CCSession` terminal session, and REAL-SESSION LAW
requires the transcript to come from a session that actually ran
(`SESSION.md`). This film has no terminal session to reconstruct: there is
no `claude` CLI installed in this VM, the task authorizes no credential to
run one against, and the CC kit components (`CCSession`, `CCDefinitions`,
etc.) are not ported to this brutalist.art tree. Inventing a session would
be a DOUBLE-CHECK LAW violation. The same switch was made by the
free-vs-paid-when-to-pay build (cc-explainer → ai-explainer, recorded in
muse/FRICTIONAL.md). Here the topic is the direct sibling of
set-it-up-once (custom instructions → memory), which shipped as show-tell.
**Switched skill: cc-explainer → show-tell.** [judgment]

**Research (2026-10-04).** Two web searches; grounded facts in FACTCHECK.md
§Verified: Claude memory topics in Settings → Memory → Topics (Engadget
how-to, TechRepublic controls explainer, AndroidAuthority, BigGo, SparkOne);
on by default for Free/Pro/Max; saved as you chat; sensitive topics off by
default; never-stored categories; Pause vs Reset; incognito; chat search
separate from memory; corrections apply going forward. Deliberately cut the
Cowork shared-memory announcement from the film (context, not the habit).
[record]

**Authoring.** Wrote make_sheet.py (13 beats, 216 s ≈ 3m36s, show-tell
spine): BIDEA (hesitant writer, trigger "remember me" → "remember what
matters, forget what doesn't"), BDEFS (memory / topics / incognito),
B00–B08 Manim body beats around the notebook cast, BHTF (ClaudeComposerAsk,
prompt read in full), BOUT (title restate, 1.0 s tail). All make_sheet
assertions passed on the first run; beat_sheet.json written. [record]

**scenes.py.** Pasted the show-tell iso_kit (no import — Gate A copies only
scenes.py), then film helpers (notebook tray, note cards, chat windows,
settings panel, archive cabinet, pencil, X marks, kraft cables) and nine
scene classes B00–B08. Two authoring fixes before QC: (1) a syntax error in
B04's MoveAlongPath play (stray paren closed self.play early) — fixed by
hoisting the path to a variable; (2) a `.set(height=0.5)` hack on the
incognito pill — replaced with a properly constructed small pill. [record]

**QC.** py_compile clean on both files. static_scene_check.py run per class
from the film folder with beat_sheet.json beside scenes.py (real
until()/finish() timing): 9 clean · 0 warn · 0 error on the first run —
no checker failures to fix. manim_layout_audit.py --curve-strict could not
run in this VM (no Manim/pangocairo); deferred to Bear's Mac render pass,
noted in CLAUDE-CODE-RENDER.md and CHECKS-REPORT.md. [record]

**Push.** All 12 files pushed via gh-put-file.py to
`muse/youtube/how-to-use-ai/make-it-remember/`; every push verified with a
Contents API read (HTTP 200). No MP3/MP4/WAV/__pycache__/.DS_Store committed
or written. muse/FRICTIONAL.md, muse/README.md, muse/QUEUE.md untouched
(coordinator owns them). [record]
