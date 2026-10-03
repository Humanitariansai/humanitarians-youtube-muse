# CARRY-OUT — claude-for-legal--claude-liam-ai-tool-handoff

**The sentence:**

> The handoff isn't done when Claude finishes — it's done when a person signs off on what comes back.

**Test:** if someone repeats only this in a meeting next week, is it still true? Yes —
it names the actual boundary (a human confirmation) without naming any tool's specific
steps, so it survives being repeated out of context.

**The wrong guess it's built to defeat:** that returning a result and finishing the job
are the same event — that once Claude delivers, the task is over. The reel falsifies
this with a concrete case (B01): an instruction that is itself wrong gets executed
perfectly, and the flawless execution ships the mistake, because nothing paused to check
the instruction before the output moved on.

**Why this compresses the distinction that matters, not the topic:** the topic is
"AI tool handoffs"; the distinction is *delivery vs. completion*. Every body beat exists
to make that distinction land — scope, boundary, and record (B02) are the three parts
that make "a person signs off" a checkable event rather than a vague gesture at
"human oversight."
