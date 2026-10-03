# FEEDBACK.md

Reviewer notes for **"Your Weekly Video, Handled."** — left empty by the builder
on purpose. Feedback belongs to the reviewer, and an unsigned draft in this file
would read as if someone had already given it.

## How to use this file

Add a dated block per review pass. Keep the verdict line explicit — the point of
the file is that a later reader can tell what was actually decided.

```markdown
## YYYY-MM-DD — <reviewer name>

**Verdict:** approved | changes requested | rejected

**What works**
-

**What to change**
- <beat id> — <what is wrong> → <what it should be instead>

**Blocking?** yes | no
```

## Acting on feedback

Every note below maps to a beat id, and every beat is regenerable. A change to
narration is not a re-edit — it is a rewrite of that beat's line, a re-measure of
its audio, and a recompile:

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel> --only B05
ART_CONCURRENCY=4 python3 runtime/scripts/remotion_scenes.py <reel> --only B05 --force
python3 runtime/scripts/compile.py <reel> --height 2160
```

Timing is never adjusted by hand. If a beat runs long, the line gets shorter and
the audio is measured again — the narration is the clock, in both directions.

---

*No review has been recorded yet.*
