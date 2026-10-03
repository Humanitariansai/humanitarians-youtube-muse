# How Frictional Is Graded

**What this page is.** The rubric from [prerequisites/frictional.md](../prerequisites/frictional.md), what each row rewards, and the one line the grader holds.

**The short version.** Five rows, scored **2 / 1 / 0** each on a 10-point scale — 2 specific and sufficient, 1 vague or incomplete, 0 absent. That scale is a **proportion, not a fixed number of points**: Frictional is always 10% of the Assignment. Frictional assesses the actual process, not whether the result succeeded.

---

## The rubric

| Criterion | Points | Evidence |
|---|---:|---|
| Attempts | 2 | What you actually tried and expected. |
| Friction and response | 2 | Confusion, surprise, a difficult decision, or an assumption you checked, and what you did next. |
| Human and AI contributions | 2 | Your work, Claude's assistance, and what you accepted, changed, or rejected. |
| Learning and uncertainty | 2 | What changed in your understanding, or what remains unresolved. |
| Traceable process | 2 | Dated entries connected to commits, prompts, outputs, drafts, or tests. |
| **Total** | **10** | |

This is reproduced from the prerequisites page, which is canonical. If the two ever disagree, the prerequisites page wins.

## The proportions

Every Assignment splits the same four ways, whatever it is worth. The shares are fixed; the points scale.

| Component | Share | 100-point Assignment | 25-point Assignment |
|---|---:|---:|---:|
| Implementation / explanation | 60% | 60 | 15 |
| **Frictional** | **10%** | **10** | **2.5** |
| GitHub version posting matching Canvas | 10% | 10 | 2.5 |
| Relative Quartile | 20% | 20 | 5 |
| **Total** | **100%** | **100** | **25** |

The rubric below is always scored out of 10 and then scaled. On a 25-point Assignment a row worth 2 is
worth 0.5, and a log scoring 8/10 earns 2.0 of the available 2.5. Nothing about what earns a 2 changes
with the size of the Assignment — only the arithmetic afterwards.

## Where the points actually go

Across a term, almost every point lost in this component is lost to one of four things, and none of them is dishonesty:

**Vagueness.** A category name where an object belongs. "The audience part was tricky" instead of "the counts summed to 39." This is the single largest source of lost points and it is entirely fixable by rereading your own entry once.

**Missing expectations.** The Attempts row asks what you tried *and expected*. Logs routinely record the attempt and drop the prediction, which caps the row at 1.

**Naming the tool without the disposition.** "Used Claude for the brief" is disclosure, which is worth something, but the row asks what you accepted, changed, or rejected. Without that clause it is a 1.

**Claiming nothing is unresolved.** The Learning and uncertainty row wants what changed *or* what remains open, and the strongest logs give both. A log in which everything resolved cleanly reads as incurious, and it is almost never true.

## What does not cost you points

Say these plainly; none of them are penalized:

- **The attempt failed.** An unsuccessful attempt can earn full credit. This is stated in the prerequisites and it is meant literally.
- **The work was straightforward.** Say so and name the checks you ran. That is a complete entry.
- **You used AI heavily.** A log showing extensive, well-bounded Claude use can score 10/10. See [AI and honest disclosure](06-ai-and-honest-disclosure.md).
- **You are still confused.** Naming an unresolved thing is what the fourth row asks for.
- **You worked few hours, or made few commits.** More time, more mistakes, and more commits do not earn extra points.
- **The log is ungrammatical, fragmentary, or blunt.** It is a log.

---

## The line the grader holds

There is an obvious way to misuse a framework like this: read a log, form an impression that a student is faking, and lower the score on the strength of that impression. That is not assessment. It is a hunch with a rubric attached, it is not appealable, and it would turn the component into surveillance.

So:

> **The rubric scores the record, not an inference about your mind.**

All five rows are readable off the page and appealable on the evidence. Every row can be maxed by documenting honestly — including documenting heavy AI use, a failed approach, or an assignment you found easy.

If a log and an artifact look badly mismatched, that produces a **conversation**, not a silent deduction. The [AI policy](../prerequisites/ai-policy.md) already establishes that the instructor or TA may ask you to explain code, methods, results, and decisions. That request is routine, applies to strong and weak submissions alike, and is not an accusation.

## How Frictional interacts with the other three components

The four components measure different things and are scored separately.

**Implementation or explanation (60%)** scores the artifact. A thin log does not reduce it. The reverse is also true: a superb log does not rescue an implementation that is not there.

**GitHub posting (10%)** scores delivery. FRICTIONAL.md being present and in the right folder is part of *that* row's "complete version." Its quality is scored here instead — the two do not double-count.

**Relative Quartile (20%)** compares the resulting work against peers. [That page](../prerequisites/relative-quartile.md) states the division directly: Frictional assesses effort; the quartile compares the work.

The one place the log can move another score is upward. If your implementation has a defect and your log shows that you identified it, understood it, and ran out of time rather than out of understanding, that is documented honest scope — and honest limits are explicitly part of what Verification and Relative Quartile reward. A defect the student demonstrably saw is a different submission from one the student never noticed, and the artifact alone cannot distinguish them.

## Who sees your log

The instructor and the course TAs. Frictional logs are part of your Assignment submission and do not become a separate institutional record or a behavioral profile. They are read to decide where teaching goes next.

You are welcome to ask for your own logs and the grader's notes at any point. Around Assignment 4 is the useful moment: reading four of your own logs in sequence is the cheapest metacognitive exercise available in this course.

## Late, missing, and revised logs

FRICTIONAL.md is part of the submitted version, so the Assignment's own deadline and Canvas's late policy govern it. A missing log is a 0 in this component and also costs the "complete version" row in [GitHub posting](../prerequisites/github-submission.md), because the required artifact list includes it.

If you revise after verification, resubmit the new checked revision under the normal Canvas rules and add a dated entry saying what changed. Do not silently rewrite earlier entries — add to the log rather than editing history.
