# Assignment 4 — Voice and experience

**INFO 7375 · Branding and AI · Fall 2026 · 100 points · Due: Canvas**

[AI Policy for Professor Bear's Courses | Using AI Responsibly in Class](https://youtu.be/8Ut0Cdl6vMw?si=9w3aEpt1ZyAR4Kiz)

**Predict → Build It → Use It → Ship It → Verify**

Bundle [Lesson 6](../../lessons/06-voice-and-story/README.md) and [Lesson 7](../../lessons/07-touchpoints-and-experience/README.md) into one contribution to your running brand project. The lesson Assessments are ungraded.

## Predict

Which voice choice could make the message less accurate or less useful? Predict a failure before generating copy. At which touchpoint will the actual experience contradict the brand promise? Name the expected mismatch. Save the expectation before the relevant output or feedback.

## Build It

Build a Python copy-review linter using explicit voice rules and claim IDs. Flag prohibited phrases, missing evidence references, and length constraints; keep stylistic flags separate from factual findings.

Build a Python journey-state simulator for discovery, consideration, use, support, and exit. Record promises, actions, failure paths, and the owner of each handoff.

## Use It

Ask Claude to draft an introduction, a product description, and an error message from the same voice brief. Revise the copy and explain where consistency requires different expression.

Ask Claude to walk through a fictional customer journey against your prototype. Compare the simulated trace with any actual usability observation you obtain; do not conflate them.

## Ship It

Submit voice guide, three copy samples, linter output, and revision diff; journey map, simulator, failure trace, and repair proposal. Include the implementation, tests, inputs, actual outputs, source credits, and [submission records](../../templates/README.md). Post the final checked version to the designated GitHub location and upload the matching version to Canvas.

## Verify

Test an unsupported claim in perfect brand voice and accurate copy that triggers a false stylistic flag. Human review decides context and meaning.

Test an unsupported transition, a dead end, and an unresolved support handoff. A simulated customer is not a real customer testimonial.

Document actual findings and limitations. Fictional cases, simulations, and proposed campaigns must remain labeled. No ad spend, public release, invented testimonial, or legal clearance is required or implied.

## Division of labor

**AI should** draft and vary copy while checking explicit constraints; simulate paths and propose failure cases.

**Human should** choose the voice, verify promises, and edit for audience and context; inspect the experience, gather real feedback when available, and own service commitments.

## Rubric — 100 points

| Implementation criterion | Points | Full-credit evidence |
|---|---:|---|
| Prediction and acceptance contract | 8 | Specific original expectations, assumptions, and a measurable failure condition. A wrong prediction alone does not lose credit. |
| Python implementation | 22 | Working requested mechanisms with documented inputs, outputs, and meaningful boundaries. |
| Applied use and evidence | 12 | Actual application to the stated task, preserved outputs, and explicit fixture/live distinctions. |
| Verification | 12 | The specified hand checks and failure cases, reproduction of the shipped version, and candid limits. |
| Technical handoff and explanation | 6 | Explainable mechanisms, reproducible commands, credited sources, and a conclusion supported by the evidence. |
| **Implementation subtotal** | **60** | |
| [Frictional](../../prerequisites/frictional.md) | 10 | Honest effort and learning log. |
| [GitHub posting](../../prerequisites/github-submission.md) | 10 | Correctly delivered, identifiable version matching Canvas. |
| [Relative Quartile](../../prerequisites/relative-quartile.md) | 20 | Overall quality relative to peers after all submissions are reviewed. |
| **Total** | **100** | |

For implementation rows, award full points for complete evidence, proportionate partial credit for a documented partial implementation, and zero when the required evidence is absent. Explain deductions. The technical handoff row assesses usability and understanding; GitHub points assess delivery. Frictional assesses the actual process, not whether the result succeeded. A finding that survives the audit can earn full credit when checks are discriminating and scope is honest.

An explainer video or Brutalist production is optional and may support communication quality within Relative Quartile. It has no separate points; excellent written evidence can earn full credit. Claude Code is assumed; direct API calls and paid media tools are unnecessary.

