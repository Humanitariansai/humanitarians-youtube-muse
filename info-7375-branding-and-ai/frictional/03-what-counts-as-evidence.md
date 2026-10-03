# What Counts as Evidence

**What this page is.** The range of things that can back a Frictional entry, and what will not.

**The short version.** `FRICTIONAL.md` is the required log. Everything else on this page is optional supporting evidence that makes the *Traceable process* row easy to award — and in a Claude Code course most of it already exists without extra work.

---

## The one test

Every form of evidence passes or fails the same question:

> **Could this have been produced without doing the work?**

A polished summary of your process: yes. Weak evidence.
The commit where you reverted an approach, with a message saying why: no. Strong evidence.

Specificity, mess, and timestamps are what make a record hard to manufacture. Polish is what makes it easy. This is the one place in the course where the rough version is worth more than the clean one.

---

## Evidence you already have

Most of the Traceable process row can be satisfied by artifacts this course already requires you to produce.

**Commit history.** Your strongest and cheapest evidence. [GitHub posting](../prerequisites/github-submission.md) already asks for messages that name the change and what you learned or tested. A log entry citing `fix: preserve unmatched rows in join audit` is traceable at zero marginal cost. Twelve commits that all say `update` carry no information and cannot support the row.

**Test names and test output.** `test_missing_partner` failing, then passing, is a dated record of a specific problem and its resolution. Cite the test, not "the tests."

**PREDICTIONS.md.** Already required. Your original prediction is the anchor for every Attempts entry — the log entry says what you expected, and PREDICTIONS.md proves you wrote it before the run rather than after.

**VERIFICATION.md.** Hand checks, failure cases, candid limits. The limits you record there are usually the same limits your Learning and uncertainty field should name.

**CONTRIBUTIONS.md.** Already required, and it overlaps the Human and AI contributions row. Keep them consistent — a contributions file that credits Claude for work the log never mentions is a discrepancy a reviewer will ask about.

**Preserved outputs.** The actual stdout, the JSON the run produced, the table that came out wrong the first time. Keep the wrong one.

## Optional supporting evidence

Attach or reference these when they help. None are required and none earn extra points on their own.

**Prompt transcripts.** Your exchange with Claude Code. For heavy AI use this is the strongest support for the contributions row, not the most incriminating. Strip anything private before committing it — [GitHub posting](../prerequisites/github-submission.md) excludes credentials, restricted data, and private conversations.

**Photographed paper.** Pictures of the notebook or whiteboard where you worked out the segment comparison you worked through on paper before writing the decision note. Crossed-out work is welcome; legibility is not graded. Caption each with a date and what you were doing.

**A dead-end file.** A running list of approaches that did not work and why you abandoned them. Some students find this easier than a journal because it has exactly one job, and it maps directly onto the Friction and response row.

**Voice memos.** Two or three minutes at the end of a session, talking through where you are stuck. Submit the audio or the transcript. Often faster than typing and harder to fake, because thinking aloud about an unsolved problem is difficult to simulate.

**Draft diffs.** For written deliverables, the first draft alongside the last. The gap between them is a record of your thinking that requires no extra writing at all.

## Accessibility

The requirement is an honest, specific, traceable log — not a particular medium. If any format here is inaccessible to you, another satisfies the requirement equally, and you do not need to say why you chose it. If none work, contact the instructor in the first week and an equivalent will be arranged. This is a normal request and documentation will not be asked for.

---

## What does not count

**Reconstructed narratives presented as contemporaneous.** Writing the log the night before is allowed if you mark the entries retrospective. Writing it the night before and dating it across two weeks is fabrication. The [AI policy](../prerequisites/ai-policy.md) is explicit: AI may organize your authentic effort notes; it must not invent struggle, timestamps, understanding, or human approvals. Neither may you.

**Effort without friction.** "Spent nine hours on this" describes time, not learning, and time is not a graded quantity here. What resisted you?

**Feelings without content.** "This was stressful" may be entirely true and is not evidence of engagement with the material. Attach it to the specific thing that was stressful and it becomes an entry.

**Manufactured struggle.** Inventing confusions you did not have is more work than documenting the ones you did, and it reads false for the same reason reconstruction does: invented confusions are generic, because they are invented from outside the problem. A log saying "parts one and two were straightforward, part three cost me four hours" is more credible than one where everything was hard.

**Volume.** More entries, more commits, more mistakes, more hours: none of these earn points. [prerequisites/frictional.md](../prerequisites/frictional.md) says this outright.

**A log for work you did not do.** Submitting a process record for someone else's implementation is a more serious matter than submitting the implementation alone, because a fabricated evidentiary record is a different act from an omitted one.
