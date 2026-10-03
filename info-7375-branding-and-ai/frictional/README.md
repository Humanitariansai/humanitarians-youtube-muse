# Frictional — teaching module

**What this is.** The student-facing explanation of the Frictional component — 10% of every Assignment: why the course grades a process log, how to write one, what counts as evidence, and two scored worked examples. Seven pages, a guided template, Canvas paste blocks, and an importable rubric.

**What it is not.** It is not the rules. [prerequisites/frictional.md](../prerequisites/frictional.md) is canonical and this folder is downstream of it. The prerequisites page is the one-page contract; this folder is the explanation students need in order to satisfy it. **If the two ever disagree, the prerequisites page wins** and this folder is the thing to fix.

**Why it was added.** The Frictional rubric is precise about what earns 2 versus 1 versus 0, and silent about why the component exists and what "specific and sufficient" looks like in practice. Nearly every point students lose here is lost to vagueness rather than dishonesty, and vagueness is fixable with examples. That is what these pages supply.

---

## Contents

| File | For | Covers |
|---|---|---|
| [01-why-frictional.md](01-why-frictional.md) | students | The decoupling, why not a detector, performance vs. learning, why friction specifically |
| [02-what-to-write.md](02-what-to-write.md) | students | The seven template fields mapped 1:1 onto the five rubric rows, with weak/strong pairs |
| [03-what-counts-as-evidence.md](03-what-counts-as-evidence.md) | students | Commits, tests, PREDICTIONS.md, transcripts, paper; accessibility; what does not count |
| [04-worked-examples.md](04-worked-examples.md) | students | A 2/10 log and a 10/10 log for Assignment 1, scored row by row |
| [05-how-its-graded.md](05-how-its-graded.md) | students | The rubric, where points actually go, the line the grader holds, interaction with the other 90 |
| [06-ai-and-honest-disclosure.md](06-ai-and-honest-disclosure.md) | students | How the AI policy meets the log; what good AI use looks like in an entry |
| [07-what-is-frictional.md](07-what-is-frictional.md) | optional | The GLP preprint in full, plus a table of which components this course actually instruments |
| [templates/FRICTIONAL-annotated.md](templates/FRICTIONAL-annotated.md) | students | Guided superset of `templates/FRICTIONAL.md` — same seven fields, with the prompts that earn points |
| [canvas-block.md](canvas-block.md) | instructor | Module description, per-Assignment block, week-one announcement |
| [rubric/frictional-rubric.csv](rubric/frictional-rubric.csv) | instructor | The five criteria as a Canvas rubric import, 5 × 2 on the 10-point scale — rescale if the Assignment is not worth 100 |
| `html/` | instructor | Pages 01–07 as paste-ready Canvas HTML |

---

## What this folder had to be corrected to

This module was first drafted generically, before the repo's existing spec was read. Three things were wrong and are worth recording so they are not reintroduced:

- **It used a 20-point rubric with four criteria.** The course uses **five criteria on a 10-point scale, worth 10% of the Assignment** — Attempts, Friction and response, Human and AI contributions, Learning and uncertainty, Traceable process — scored 2 / 1 / 0 per row.
- **It assumed Canvas file upload.** The log is `FRICTIONAL.md` inside `fall-2026/first-name-last-initial/assignment-XX/`, pushed to GitHub, with the Canvas version matching. See [github-submission.md](../prerequisites/github-submission.md).
- **It wrote its own AI policy.** [prerequisites/ai-policy.md](../prerequisites/ai-policy.md) already exists and is canonical. Page 06 now explains it rather than restating or extending it, and carries the policy video link as AGENTS.md requires of graded briefs.

The generic original remains at `bear-textbooks/books/friction-measuring-the-learning-struggle/canvas-module/` for instructors outside this course. It is not the course's version and should not be linked from course materials.

---

## Setup

1. Create a Canvas module named **Frictional**, ordered before Assignment 1. Paste block A from [canvas-block.md](canvas-block.md) as the description.
2. Create seven pages from `html/`, using Canvas's HTML editor (`</>`), and add them to the module in order. Page 07 can be added as an optional item or omitted from module requirements.
3. Upload [templates/FRICTIONAL-annotated.md](templates/FRICTIONAL-annotated.md) to Files and add it to the module.
4. Append block B to each Assignment description. The Assignment rubric row already exists and links the prerequisites page — do not duplicate the rubric in the description.
5. Optional: import `rubric/frictional-rubric.csv` if Frictional is graded in its own Canvas column rather than inside the 100-point Assignment rubric.
6. Post block C as a week-one announcement. Transparency about what the data is for is a design requirement of the framework, not a courtesy, and it works better said out loud than only posted.

## Grading it

Two to four minutes per log once calibrated, which takes roughly one Assignment's worth. Score a batch in one sitting rather than one at a time — that single change does more to reduce drift than anything else.

Hold the line in [05-how-its-graded.md](05-how-its-graded.md): the rubric scores the record, not an inference about the student's mind. If a log and an artifact look mismatched, the [AI policy](../prerequisites/ai-policy.md) already provides the remedy — ask the student to explain their code, methods, results, and decisions. That is a standing provision, applies to strong and weak submissions alike, and is not an accusation. A silent deduction on a hunch is not appealable and is the one move that would turn this component into surveillance.

The most common real failure is a log that is honest, complete, and entirely vague. That is a 5, it is frustrating for everyone, and the fix is [04-worked-examples.md](04-worked-examples.md) rather than a comment.

## Maintenance

- Page 04 is scored against [assignment-01.md](../assignments/fall-2026/assignment-01.md). If that Assignment changes substantially, the worked examples need rewriting against the new work.
- Page 02's field-to-rubric table must stay in sync with `templates/FRICTIONAL.md` and `prerequisites/frictional.md`.
- The two logs in page 04 are **constructed teaching examples and labeled as such in the page**. AGENTS.md forbids manufacturing predictions, evidence, or reflection; the label is what keeps the illustration on the right side of that rule. Do not remove it, and do not replace them with real student work without permission.
- `html/` is generated from the markdown with pandoc, then given inline table and blockquote styles that survive Canvas. Regenerate after editing any page; do not hand-edit the HTML.

```bash
cd frictional && for f in 0*.md; do pandoc "$f" -f gfm -t html5 --wrap=preserve -o "html/${f%.md}.html"; done && python3 html/_style.py
```
