# PROMPTS.md — Agents: AI that does things.

Prompts Muse was given (by Bear / the parent orchestrator) that shaped
this film, in order.

1. The film-builder standing rules (MEMORY.md): build lecture films as
   pre-render packages for the humanitarians AI YouTube channel
   (https://www.youtube.com/@humanitariansai), always using the Liam
   persona ("Liam, in for Bear"); identity constants (channel claude-liam,
   Kokoro voice am_onyx, Teardown register, watermark @NikBearBrown);
   never render/publish; push everything to GitHub immediately; 12-file
   package; QC gate; FRICTIONAL.md seven-field entries.
2. The audience and skill-menu rules: "Assume a general audience — smart
   and pragmatic but NOT necessarily AI experts. Every term gets explained.
   Show rather than tell." Skill picked per film from the full set
   (lecture, show-tell, cc-explainer, ai-explainer, deep-explainer).
3. This film's assignment (2026-10-04): film with slug
   `agents-that-do-things`, working title "Agents: AI that does things",
   pitch "What 'agentic' AI means for a normal person — where it helps,
   where it goes wrong, how to supervise it", assigned skill ai-explainer
   (switch allowed with reason recorded).
4. The assignment's package convention: 12 files in
   `~/workspace/film-builds/how-to-ai/agents-that-do-things/`; beat sheet
   uses `beat_id`, `narration_text`, `estimated_duration_s`, and a `shot`
   object with `type` GRAPHIC (+ `shot.manim.class`) for Manim beats or
   REMOTION (+ `shot.remotion.pattern`) for bookend beats; `make_sheet.py`
   generates `beat_sheet.json` with assertions on beat counts and total
   duration; `scenes.py` classes named `<BID>_<Name>(Scene)`; the QC gate
   (py_compile clean + static checker 0 warnings/0 errors per scene);
   push all 12 files to
   `Humanitariansai/humanitarians-youtube-muse:muse/youtube/how-to-use-ai/agents-that-do-things/`
   via gh-put-file.py and verify each with a Contents API read; never
   commit MP3/MP4/WAV/__pycache__; never put secrets in film files; do not
   write muse/FRICTIONAL.md, muse/README.md, or muse/QUEUE.md.
5. The audience content rules: explain every technical term (agent, tool
   use, autonomy, loop) in plain language, shown wherever possible; aim
   3–6 minutes; never quote pricing tiers; teach decision frameworks
   instead; do not assert version-specific product features as timeless
   facts.

No generation prompts were used in this build — all visuals are
hand-authored Manim scenes plus four Remotion bookend beats (patterns from
the ai-explainer skill: ClaudeComposerAsk, BrutalistHesitantWriter,
ClaudeTitleOutro), rendered at Bear's Mac render pass.
