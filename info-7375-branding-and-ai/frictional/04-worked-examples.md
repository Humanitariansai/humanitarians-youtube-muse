# Worked Examples: A Thin Log and a Strong One

**What this page is.** Two Frictional logs for the same Assignment, scored row by row on the [official rubric](../prerequisites/frictional.md). One earns 2/10. One earns 10/10. Read this page before your first submission — it is the fastest way to see what *specific and sufficient* means.

**Both students shipped working code and a readable brief.** On the 60% implementation share they would score within a few points of each other. The Frictional gap is 8 of 10 — most of a letter grade once it is scaled.

> **These are constructed teaching examples, not real student work.** They were written to illustrate the rubric. No student wrote either one.

---

## The Assignment both students did

[Assignment 1 — Brand promise and audience](../assignments/fall-2026/assignment-01.md): a Python brand-brief validator covering audience, problem, promise, evidence, alternatives, exclusions and owner, plus an audience-evidence ledger linking segment, job, observation, source, date and confidence — with observed findings kept separate from hypotheses.

---

## Log A — 2/10

> **FRICTIONAL.md**
>
> **10/12** — Started the assignment. Picked my brand and wrote the brief, then built the validator. It was a bit confusing at first but I figured it out.
>
> **10/14** — Did the audience ledger. Used Claude to help with the two alternative briefs. The segments were tricky but I narrowed it down. Wrote the decision note and pushed. Overall I learned a lot about positioning.

### Scoring

| Row | Score | Why |
|---|---:|---|
| Attempts | 1 | Names activities but no expectation anywhere. Nothing was predicted, so nothing can have been violated. |
| Friction and response | 0 | "A bit confusing," "tricky." Categories of experience, not experiences. No object, no check, no response. |
| Human and AI contributions | 1 | Claude is disclosed, which is honest and worth something. "Help with the two alternative briefs" does not say what was accepted, changed, or rejected — and the brief asks for exactly that separation. |
| Learning and uncertainty | 0 | "Learned a lot" is content-free and nothing is named as unresolved. |
| Traceable process | 0 | Two dates, no commits, no test names, no ledger rows cited. Nothing a reviewer can open. |
| **Total** | **2** | |

**The point of Log A:** this student may have done every bit of the work. That is the problem. They submitted an artifact indistinguishable from a generated one and a log indistinguishable from a generated one. The 2 is not an accusation — it is the honest statement that the evidence does not support more. Every sentence could have been written by someone who never picked a brand.

---

## Log B — 10/10

> **FRICTIONAL.md**
>
> **10/12** — *What I tried and expected:* Wrote the brief for the running brand first, then the validator. Expected `alternatives` to be the field I'd struggle with.
> *What happened / what I checked:* It wasn't. `evidence` was. I wrote a promise in nine words and then could not put anything in the evidence field that was not a hypothesis. Everything I had was a reason the promise *ought* to be believable, not a reason to think anyone believes it.
> *What I did next:* Left the field empty rather than filling it, and made the validator refuse to mark a brief complete with an empty `evidence` — so the gap is visible in the artifact instead of papered over in prose. Currently the brief fails its own validator, deliberately, and the decision note says so.
> *Contributions:* Mine. Claude not used yet.
> *Understand / do not understand:* Understand that a promise and the evidence for a promise are different objects and I had been writing the first while feeling the second. Do not know what counts as evidence at this stage — I have no customers yet, and I am not sure "a competitor does this and survives" is evidence about *my* promise.
> *Evidence:* `test_rejects_brief_with_empty_evidence`; commit `feat: refuse to complete a brief with no evidence for its promise`. Next: the ledger.
>
> **10/14** — *Tried and expected:* Built the audience-evidence ledger and back-filled six rows. Predicted this would be the quick part.
> *What happened:* Four of the six rows have a `source` that supports the topic but not the observation. I had written "freelancers lose time to invoicing" and cited an article about freelancer admin burden generally. The article never mentions invoicing. I had been treating "a source exists about this area" as "a source supports this claim."
> *What I did next:* Moved all four to a `hypothesis` table with the source removed, and left two in `observed`. The segment comparison now rests on two rows instead of six, which is a much weaker and much more honest position. Rewrote the decision note around what I actually have.
> *Understand / do not understand:* Understand that the `source` column was letting me launder a hunch by attaching a citation to its neighbourhood. Do not know how to get real observations for this segment inside the term without running interviews I am not authorized to run.
> *Evidence:* `test_observed_row_requires_source_supporting_the_observation`; `evidence/ledger-before-1014.json` preserved; commit `fix: move four unsupported rows from observed to hypothesis`.
>
> **10/15** — *Tried and expected:* Asked Claude Code for two competing briefs after my own prediction was recorded. Predicted they would differ on audience.
> *What happened:* They differed on adjectives and nothing else. Read side by side they are the same brand twice. I spent twenty minutes unable to say why.
> *What I did next:* Asked Claude what makes two positioning statements collapse into one. It gave three causes; the one that matched is that neither brief says who the offering is **not** for. **Accepted** the diagnosis. **Rejected** its proposed fix — sharpen the adjectives in each — because that is a wording change and the problem is structural. Added `exclusions` as a required field in the validator instead, and the two briefs now genuinely diverge because they exclude different people.
> *Contributions:* Claude — drafts generated, diagnosis accepted, proposed fix rejected, schema change written by me. Transcript in `evidence/claude-briefs-1015.md`.
> *Understand / do not understand:* Understand that a positioning statement with no exclusion is not a position, and that this is why generated briefs read as interchangeable. Still unresolved: whether an exclusion I am unwilling to publish counts as a real one.
> *Evidence:* commit `feat: require exclusions before a brief validates`.
>
> **10/16 (retrospective, written 10-17)** — *Tried and expected:* Final pass; expected only README edits.
> *What happened:* The `confidence` column in the ledger is still free text nobody validates — the same weakness I fixed in `source`, one column over. Out of scope to fix now.
> *What I did next:* Left it and named it in VERIFICATION.md as a known limit rather than pretending it isn't there.
> *Understand / do not understand:* Understand that unvalidated fields are where hypotheses re-enter a ledger that is supposed to keep them out. Do not know whether confidence can be constrained without becoming theatre.
> *Evidence:* VERIFICATION.md limits section; commit `docs: record unvalidated confidence column as known limit`.

### Scoring

| Row | Score | Why |
|---|---:|---|
| Attempts | 2 | Every entry states what was tried and what was expected. The 10/14 prediction — "this would be the quick part" — is specific enough to be *wrong*, which is what makes it worth 2. |
| Friction and response | 2 | Four frictions, each anchored to an object — the empty evidence field, four of six ledger rows, two briefs that read identically, the free-text confidence column — each with what was done next, including one thing left undone and declared. |
| Human and AI contributions | 2 | Claude's contribution is bounded precisely: drafts generated, diagnosis accepted, fix rejected, schema change written by the student, transcript preserved. Entries with no AI use say so. |
| Learning and uncertainty | 2 | Something changed in every entry and every entry names something still open. "A much weaker and much more honest position" is a student grading their own evidence rather than their own effort. |
| Traceable process | 2 | Every entry cites a test, a commit subject, or a preserved artifact. The retrospective entry is marked. |
| **Total** | **10** | |

---

## What actually separates them

Log B is not longer because the student worked harder or wrote better. It took roughly twelve minutes across four sessions. It is longer because it is **anchored**: every claim points at a specific object in the actual work.

Three moves do nearly all of the work, and you can copy all three:

1. **Write the expectation before the run.** You cannot record a violated prediction if you never recorded a prediction. This is the same discipline PREDICTIONS.md already asks of you.
2. **Name the object, not the category.** Not "the segments were tricky" — `four of six rows`, `the article never mentions invoicing`, `test_observed_row_requires_source_supporting_the_observation`.
3. **Say what you did with the help.** Accepted, changed, or rejected. Log B's highest-value entry is the one where Claude's diagnosis was right and its fix was worth refusing.

Before you submit, take any sentence in your log and ask whether a classmate who never opened your repository could have written it. If they could, you have written about the Assignment. Write about what happened instead.
