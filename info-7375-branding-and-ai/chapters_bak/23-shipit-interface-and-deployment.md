# Appendix S4 — Interface Design and Deployment
*The interface is not a finishing layer. It is a contract. Every session, the user checks whether you kept it.*

> **TL;DR:** This appendix treats the interface as a promise the user re-checks every time they open your tool — not a coat of paint added at the end. It defines what "interface" really covers, shows three ways an interface can betray the brand, compares two fast build frameworks, and walks you through building and deploying a working one.
>
> | Section | Preview |
> |---|---|
> | What "Interface" Actually Means | The several different things the word "interface" refers to, and why each carries brand weight. |
> | Three Faces of Misalignment | Three ways an interface can quietly contradict the brand it represents. |
> | Three Case Studies | Real products read for how their interface kept or broke the user's trust. |
> | Streamlit and Gradio — Choosing the Right Framework | A practical comparison of two fast ways to build an AI tool's interface. |
> | Building the Interface | Constructing the working interface for your tool, including its empty and error states. |
> | Deployment | Getting the tool online so other people can actually use it. |
> | What the Interface Is Doing in the Larger Arc | How the interface fits the path from idea to shipped brand. |

---

On February 6, 2023, Google announced Bard at a press event and released a promotional video. In it, Bard answered a question about the James Webb Space Telescope with three confident bullet points. The third claimed that JWST had taken the first images of a planet outside our solar system. The first exoplanet images were taken by the European Southern Observatory's Very Large Telescope in 2004, nearly two decades before JWST launched.

Journalists noticed within hours. Reuters ran the story on February 8. By close of trading that day, Alphabet had lost approximately $100 billion in market capitalization.

The error was not the cause. Research-preview AI systems make errors; this was disclosed. The cause was the interface: a polished, Google-branded promotional video presenting Bard's output as confident, authoritative, Google-quality information. The interface made a promise. The system broke it in a domain where anyone with internet access could check. The market priced the gap.

Your tool will not lose $100 billion if the interface overpromises. But it will lose users, and the mechanism is identical. This appendix is about building an interface that makes only the promises the underlying system can keep.

## What "Interface" Actually Means

The word *interface* is doing at least four different jobs in conversations about AI tools. Each job is real. None of them can substitute for the others. Engineers who think "interface" means "UI" consistently underinvest in the layers that damage brand.

**Layer 1: The visual surface.** Buttons, forms, layouts, colors, typography, spacing. This is the layer most engineering students think of when they hear "interface design." It matters. It is also the layer most easily fixed after the fact — a button color is trivial to change; a structural misalignment between the interface and the system is not.

**Layer 2: The interaction model.** How the user thinks about working with the tool. Is this a chat interface? A search interface? A form with outputs? A dashboard? The interaction model sets the user's mental model of the system's capabilities before they see a single result. A chat interface implies conversational competence. A search interface implies index breadth. A form implies structured, reliable output. Whatever model you choose, the user will hold the system to it.

**Layer 3: The deployment surface.** What the user encounters before the UI loads. The URL itself — a random alphanumeric string on a free tier says something different than a named domain. Account creation or not — a login wall before the tool demonstrates anything has a conversion cost. Latency — a five-second wait on first load is a brand signal that the system is slow or overloaded. The "is this real?" question that every new user asks is answered primarily by Layer 3, before they have seen Layer 1 at all.

**Layer 4: The brand surface.** The small things that compound. Error messages — what does the interface say when something goes wrong? Empty states — what does the user see before they have done anything? Confidence — when the system is uncertain, does the interface say so? Tone — is the copy in the help documentation consistent with the copy in the tool itself? Layer 4 is where the Bard failure lived. The UI was excellent. The interaction model was clear. The deployment was polished. The brand surface — confident bullet points, no source attribution, no hedging, no uncertainty signal — is what broke.

All four layers have to be coherent with each other and with the underlying system.

<!-- → [TABLE: Four interface layers — columns: layer number, layer name, what it includes, most common engineering mistake, failure mode when misaligned with system — shows the full taxonomy before the misalignment discussion applies it] -->

![The four interface layers stacked from visual surface to interaction model to deployment surface to brand surface — each naming what it includes and its common engineering mistake, with the brand surface marked as where the Bard failure lived.](../images/23-shipit-interface-and-deployment-fig-01.png)

## Three Faces of Misalignment

Before building the interface, you need to understand the failure modes precisely enough to design against them. There are three structural forms of interface-brand misalignment. Each has a different cause and a different fix.

**Confidence misalignment** is when the interface presents output as more certain than the system actually is. Bard's bullet points had no source citations, no hedging language, no "this may be incorrect" qualifier. The user saw confident assertions from an authoritative source. The interface conveyed a certainty the system did not have.

This is the most common failure mode for AI interfaces built by engineers. The reason is structural: when you are building the tool, the system's outputs look reasonable to you. You have been running it for weeks. You have seen the cases where it works. You build the interface to show the output clearly and confidently, because that is what looks good in the demo. You ship. The first user who hits a low-confidence case sees a confident-looking wrong answer.

The fix is not to make the system more accurate. The fix is to make the interface honest about the system's accuracy. Confidence scores, "verify with source" footers, "this answer may not be complete" banners on edge cases — any of these costs almost nothing to implement and repairs the misalignment at the UI layer without requiring a system overhaul.

**Capability misalignment** is when the interface implies the tool can do things it cannot reliably do. A chat interface implies general conversational competence. If your tool is a scoped Q&A system that can answer questions about three specific topics, the chat interface is lying to the user about the system's scope. A "summarize this document" button implies the system handles any document. If your tool handles PDFs but not Excel files, the button is lying.

The mechanism: the user encounters the implied capability in their first or second session. They try to use the feature the interface implied. The system fails or produces poor output. The user concludes the tool is broken and does not return. A narrower capability claim is almost always more trustworthy than a broader one, even if the broader claim would be more impressive in a demo. "Summarize PDFs up to 20 pages" is less exciting than "summarize any document" and far more trustworthy when the user uploads a 50-page PDF and gets a degraded result.

**Tone misalignment** is when the interface speaks in a voice the underlying system cannot maintain. A friendly, casual, first-person chatbot interface paired with a system that returns clipped, templated responses. A sober enterprise interface paired with a system that sometimes produces chatty, informal outputs. A "we're here to help" onboarding flow followed by a system that returns technical error messages without explanation.

Tone misalignment is the subtlest of the three because it operates below the level of explicit claims. No one put "this system is warm and conversational" in the interface copy. But the interaction model, the visual surface, the copy in the empty states — all of it signals a tone that the system has to maintain in its outputs. When it does not, the user feels something is off without being able to articulate exactly what.

The fix is tone-matching: read the system's actual outputs, then design the interface copy to match the register of those outputs.

<!-- → [TABLE: Three misalignment types — columns: type, definition, how engineers produce it, what users experience, specific fix — consolidates the taxonomy before the case studies apply it] -->

![The three faces of interface-brand misalignment — confidence, capability, and tone — each panel giving the definition, how engineers cause it, what users experience, and the fix, with confidence misalignment marked as the most common failure.](../images/23-shipit-interface-and-deployment-fig-02.png)

## Three Case Studies

These three cases represent the three misalignment types at scale, and each reveals how fast the brand consequence arrives.

**Google Bard, February 2023 — Confidence Misalignment.** The Bard story opened this appendix, but the design lesson is worth making explicit: the interface's confidence level has to be calibrated to the system's actual reliability. A research preview should look like a research preview, not like a finished Google product. Google's response over the following days acknowledged the demo had not passed internal testing standards. The brand damage was not repaired by the correction. The initial impression, formed in the six seconds of a promotional video, was what spread.

**Snapchat Redesign, February 2018 — Tone Misalignment.** Snapchat launched a major interface redesign that reorganized core navigation: Stories from friends and professional content publishers were moved to separate sections, and the "Discover" feed was promoted to a more prominent position. The intent was to better distinguish personal communication from content consumption.

Users responded immediately and negatively. A petition demanding a revert gathered 1.2 million signatures within the first week. Kylie Jenner, then among Snapchat's most-followed users, tweeted that she had stopped using the app; the stock dropped roughly 7% the following day. Snapchat's daily active user count declined in subsequent quarters, a trend the company attributed in part to the redesign.

The failure was not technical. The redesign worked as designed. It was a brand-surface failure: Snapchat had been the interface for private, ephemeral communication between friends — the design was deliberately casual, personal, slightly chaotic. The redesign introduced a more organized, media-forward structure that signaled "content platform" to users who had chosen Snapchat precisely because it was not a content platform. Interface changes are brand changes. Users hold the interface to the promise the previous version made.

**Microsoft Tay, March 2016 — Capability Misalignment.** Microsoft launched Tay on March 23, 2016, as a chatbot on Twitter designed to learn from and respond to conversations with users. The interface — an open Twitter account that anyone could mention and receive a response from — implied a system capable of beneficial public conversation that would improve with interaction.

Within sixteen hours, coordinated trolls had submitted inputs designed to cause Tay to produce offensive, racist, and conspiratorial outputs. Microsoft pulled the account offline within a day of launch, but not before screenshots had circulated widely. The capability misalignment was structural: the interface implied a system that could safely learn from arbitrary public input. The system could not. The interface made public interaction the learning mechanism; the system had no defenses against adversarial inputs.

Microsoft's post-mortem acknowledged the team had not anticipated this in testing, having tested with a small, non-adversarial group. The design lesson: test the interface against the population that will actually use it, not the population you wish would use it. Public interfaces will encounter adversarial users, boundary cases, and interaction patterns the development team did not anticipate. The capability claims have to hold against that population.

<!-- → [TABLE: Three case studies mapped to three misalignment types — columns: product/event, misalignment type, interface promise, system reality, brand consequence — directed comparison makes the three cases immediately comparable] -->

![Three case studies mapped to the three misalignments — Bard (confidence), Snapchat (tone), Tay (capability) — each row carrying the interface promise, the system reality, and the brand consequence.](../images/23-shipit-interface-and-deployment-fig-03.png)

## Streamlit and Gradio — Choosing the Right Framework

You will not be hand-coding a frontend for this version of your tool. The two correct tools for AI tool prototypes at this stage are Streamlit and Gradio. Choosing between them is itself an interface decision — the framework shapes the interaction model.

**Streamlit** is a Python-first web app framework. You write Python; Streamlit renders a web application. The development model is simple: a Python script runs top to bottom on every user interaction, and Streamlit re-renders the page on each run. Streamlit is strong at multi-step workflows, dashboards, and applications where the user's job is to *do work* — configure inputs, run a process, inspect results, iterate. File upload widgets, multi-select filters, data tables, progress bars, conditional display logic, multi-page applications — all are first-class in Streamlit. A Streamlit application feels like a web app. The interaction model implies: "this is a tool you use to accomplish a task." Deploy via Streamlit Community Cloud: push to GitHub, connect the repo, get a public URL. Free tier is sufficient.

**Gradio** is a Python library for building interactive ML demos, now part of Hugging Face. The development model is component-based: you define input components, output components, and the function that maps inputs to outputs. Gradio renders the interface. Gradio is strong at single-purpose model demos where the user's job is to *try the model* — submit an input, see an output, submit another. A Gradio interface feels like a demo. The interaction model implies: "this is a model you can probe." Deploy via Hugging Face Spaces: push to a Space repository, select Gradio as the SDK, get a public URL. Free tier is sufficient.

The choice is an interaction model decision, not a preference decision. The question is: what is the user's primary job when they use this tool?

If the user's job is to *do work* — upload a file, configure parameters, run a process, see structured results, iterate — choose Streamlit. A competitor news pipeline that the user configures with their RSS feeds. A research summarization tool that takes a topic and a date range and returns a formatted report. These are Streamlit tools.

If the user's job is to *try the model* — type an input, see an output, type another input — choose Gradio. A content-generation tool that takes a brief and returns three headline variants. A brand-voice classifier that takes a piece of copy and returns a voice profile. A sentiment scorer that takes a URL and returns a breakdown. These are Gradio tools.

The mismatch to avoid: an orchestrated multi-agent system deployed behind a Gradio "type a prompt, get a result" interface. The architecture implies structured, reliable, inspectable behavior; the Gradio interaction model implies free-form exploration. If your pipeline architecture is orchestrated, your interface should be Streamlit — structured inputs, visible outputs, inspectable state.

<!-- → [TABLE: Streamlit vs. Gradio selection guide — columns: criterion, Streamlit, Gradio; rows: user's primary job, interaction model implied, architecture fit, deployment platform, which pipeline types fit each — makes the decision a lookup rather than a debate] -->

![The Streamlit-versus-Gradio selection guide: do work (Streamlit) versus try the model (Gradio), compared across user's primary job, interaction model implied, architecture fit, deployment platform, and pipeline fit — with the mismatch to avoid, an orchestrated system behind a free-form Gradio box.](../images/23-shipit-interface-and-deployment-fig-04.png)

## Building the Interface

"Minimum viable interface" is not the same as "minimum effort interface." Minimum effort produces a bare form that works but makes no commitments. Minimum viable produces the smallest interface that accurately represents what the tool does, makes the right commitments, and does not make the wrong ones.

Three components every minimum viable AI tool interface needs.

**An input affordance that matches the system's actual inputs.** If the system takes an RSS URL, the interface should have a URL field, not a free-text prompt box. The shape of the input signals the system's scope. A free-text prompt box implies general natural-language understanding; a URL field implies structured ingestion of a specific kind of resource.

**A visible processing state.** AI pipelines take time. A blank screen while the system runs is a brand failure — users think the tool is broken and close the tab. A spinner, a progress bar, a "processing your request..." message — any of these is sufficient. Streamlit's `st.spinner()` and `st.progress()` components make this trivial.

**An output surface that represents confidence accurately.** If the system returns a result with a confidence score, show the score. If the system returns a result that should be verified, say so in the interface copy. If the system sometimes returns "I don't know" — which any well-designed AI system should — the interface should handle that gracefully, not display an empty string.

What the minimum viable interface should not have: features your system does not reliably support, input types the system cannot handle, capability claims in the copy the system cannot keep.

<!-- → [DIAGRAM: Minimum viable interface — three required components as labeled boxes (Input affordance matches system scope, Visible processing state, Output surface with confidence representation) and three prohibited components (Features system can't reliably support, Input types system can't handle, Capability claims system can't keep) — required on left, prohibited on right, with the alignment audit as the gate between design and deploy] -->

![The minimum viable interface: three required components — input affordance matching system scope, visible processing state, output surface representing confidence — beside three prohibited ones, with the alignment audit as the gate that must be passed between design and deploy.](../images/23-shipit-interface-and-deployment-fig-05.png)

### The Alignment Audit

Before you deploy, run the alignment audit. It is a two-column exercise.

Left column: every implicit promise your interface makes. These are not the things you wrote in the README or said in the pitch. They are the things a user will infer from the visual surface, the interaction model, the deployment surface, and the brand surface. Write them all down. Some will be obvious: "the tool can analyze any RSS feed." Some will be subtle: "the tool produces professional-quality output." Some will be about tone: "this tool is from a team that cares about quality."

Right column: can the underlying system keep this promise, reliably, for the population of users who will use the tool?

For every row where the answer is "no" or "sometimes" or "not for this kind of user," fix the interface before you ship. Remove the claim, add a qualifier, narrow the input, or add an explicit uncertainty signal. Do not fix the system — that comes later, in the Build-Measure-Learn loop. Fix the interface now, so the system and the interface are making the same promises.

Here is what the audit looks like in practice, using a sentiment analysis pipeline.

*Interface promises:* "Analyzes your competitor news." "Scores articles for sentiment." "Delivers daily to your Google Sheet." "Up to 10 RSS feeds." "Results in under 3 minutes."

*System reality checks:*

- "Analyzes your competitor news" — the system analyzes RSS content from feeds the user configures. It does not scrape content behind paywalls. ✗ Narrow the claim: "Analyzes publicly available RSS content from your configured feeds."
- "Scores articles for sentiment" — the system scores using GPT-4o-mini with a three-point scale. Accuracy is high for clear-cut cases, lower for ambiguous cases. ✗ Add a qualifier: "Sentiment scoring is approximate; verify important findings."
- "Delivers daily to your Google Sheet" — accurate if the n8n workflow is running. If the workflow fails, the Sheet does not update. ✗ Add an error state: "If the Sheet has not updated by 8 a.m., check the workflow status at [URL]."
- "Up to 10 RSS feeds" — accurate. ✓ No change needed.
- "Results in under 3 minutes" — accurate under normal load; API latency can push this to 5 minutes occasionally. ✗ Revise to: "Results typically in under 5 minutes."

Five claims. Three needed fixes before the tool was aligned. None of the fixes required changing the system. All of them required the engineer to stop presenting the ideal case and start presenting the realistic case.

<!-- → [TABLE: Alignment audit worked example — columns: claim as written, system reality, pass/fail, specific fix applied — five rows from the sentiment analysis pipeline; illustrates the two-column format in action] -->

![The alignment audit worked on the sentiment pipeline: five interface claims, the system reality for each, pass or fail, and the specific fix applied — three of five needed narrowing, none required changing the system.](../images/23-shipit-interface-and-deployment-fig-06.png)

## Deployment

Deployment is not the interesting part of this appendix, but it is the gate. The deliverable is a URL that someone other than you can visit and use. Getting there requires four concrete steps.

**Step 1: Choose a host.** Streamlit Community Cloud and Hugging Face Spaces are the two free, low-friction options. Both require a GitHub account. Both get you from working code to public URL in under an hour if your dependencies are clean.

**Step 2: Write the requirements file.** Every Python package your tool uses needs to be in a `requirements.txt` (Streamlit) or listed in your Space's configuration (Gradio). Missing dependencies are the most common cause of "it works on my machine" deployment failures. Run `pip freeze > requirements.txt` in a clean virtual environment, not your general development environment.

**Step 3: Handle secrets correctly.** Your tool uses API keys. API keys do not go in the code, and they do not go in the GitHub repository. Streamlit Community Cloud and Hugging Face Spaces both have secrets management — environment variables accessible to the running application but not visible in the repository. Use them. A deployed tool with API keys in the code is a security failure; both platforms will flag it and may terminate the deployment.

**Step 4: Test the deployed URL before you share it.** Run through your own tool as a user who has never seen it. Do the inputs work? Does the processing state show? Does the output render correctly? Does the error state trigger when the system fails? The deployment environment is not your development environment; behavior can differ.

![Deployment in four steps — choose a host, write a clean requirements.txt, handle secrets correctly, and test the deployed URL as a first-time user — each annotated with its most common failure, ending at a public URL someone else can use.](../images/23-shipit-interface-and-deployment-fig-07.png)

### The README as Interface

The README is not documentation. It is the last interface layer — the one the user encounters when they are trying to understand what they just used, or before they decide whether to use it at all.

A portfolio-quality README has six elements. First, what the tool does — one paragraph, no marketing language. What it takes as input, what it produces as output, who it is for. Second, how to use it — step-by-step, with the assumption that the user has never seen the tool before. Third, what its limits are — explicit. What the tool does not do. What kinds of input it handles poorly. What the confidence of the output is. This is the README-level alignment audit. Fourth, the architecture diagram — a figure showing the pipeline: inputs, processing steps, outputs, external services. A hand-drawn diagram photographed and embedded is fine; the content matters more than the rendering. Fifth, the technology stack — what the tool is built with: Streamlit or Gradio, which LLM API, n8n or direct code, storage layer. Sixth, the deployed URL — at the top, before anything else. The user should not have to read four paragraphs to find the link.

<!-- → [TABLE: README quality checklist — six rows, one per element; columns: element name, what it should contain, common failure mode, self-grading question — makes the README a structured artifact, not a freeform document] -->

![The README as the last interface layer: six elements in reading order — deployed URL at the top, then what it does, how to use it, limits, architecture diagram, and tech stack — each with what it should contain and how it fails.](../images/23-shipit-interface-and-deployment-fig-08.png)

## What the Interface Is Doing in the Larger Arc

The interface closes the loop that the PRD opened.

The PRD specified what the tool would do and what it would not. The pipeline implemented the what. The architecture determined how reliably it would run. The interface is where the user encounters the result of all three prior decisions, every session.

The alignment audit is the mechanism that connects all four. A PRD that said "out of scope: social media monitoring" should produce an interface that does not have a social media input field. A pipeline that produces outputs with variable confidence should produce an interface that shows confidence indicators. An architecture that is orchestrated and reliable should produce an interface that is structured and inspectable, not exploratory.

The interface is also where the archetype becomes visible to the user. A Sage archetype builds tools that provide insight — the interface should surface the insight clearly, attribute it honestly, and signal where it is uncertain. A Creator archetype builds tools that produce things — the interface should make the output the hero of the page, offer variants, and make iteration fast. A Caregiver archetype builds tools that help people — the interface should be warm, patient, forgiving of input errors, and generous with guidance.

If the interface contradicts the archetype — if a Sage tool has a splashy, entertainment-forward interface, or if a Caregiver tool has an austere, efficiency-forward interface — the user picks up on the mismatch and the brand surface loses coherence. The interface should be the archetype, not just the tool.

<!-- → [TABLE: Archetype-to-interface alignment guide — columns: archetype, visual surface signals, interaction model fit, deployment surface tone, brand surface copy style; rows for Sage, Creator, Caregiver, Magician, Hero — makes the abstract archetype-interface connection concrete and actionable] -->

> The interface is the only part of your system the user experiences directly. Everything else — the pipeline, the model, the architecture, the data sources — is invisible to the user. The interface is all they have. Make every layer of it a promise the system can keep.

**What would change my mind:** strong evidence that fast time-to-deployment frameworks (Streamlit, Gradio) lead students to ship *worse*-calibrated interfaces than custom-built frontends — specifically, that the framework's constraints force interaction models that systematically misalign with the tool's actual capability. The current argument is that framework constraints produce discipline. If the evidence went the other way — if students using custom frontends shipped more aligned interfaces because the build effort forced more deliberate interaction model decisions — I would revise the framework recommendation.

**Still puzzling:** why engineers consistently overpromise in first interfaces — buttons implying broader capability than the system can deliver, "AI-powered" copy overstating what the AI is doing, missing uncertainty surfaces. The behavior is universal enough that I suspect it is structural: engineers think about interfaces as presentation layers to be made impressive, not as contracts to be kept. I have not yet found a teaching intervention that successfully installs the contract framing before the first interface is built rather than after the first interface fails.

---

## LLM Exercises

### Exercise 1 — When to Use AI
*Run these tasks with an LLM and evaluate what it can and cannot do:*

Ask the model to draft the empty, loading, and error states for a tool you describe. Give it the tool's archetype and one sentence about what it does. Evaluate the output: does the copy hold the archetype under failure, or does it default to generic helpfulness that could have come from any tool?

**The tell:** you can test whether the drafted copy would feel consistent with the rest of the interface, including in states the model did not generate. If the error state sounds like a different product, the model matched "error state copy" patterns rather than your specific archetype.

### Exercise 2 — When NOT to Use AI
*Identify the judgment the AI cannot make:*

Run the alignment audit on your own tool: enumerate five implicit promises your interface makes, then ask the model to check each against the system's actual capability. Evaluate: what did the model need to know about the system that it did not have — and how would that missing knowledge change the audit result?

**The tell:** you've crossed the line when "it deploys" substitutes for "it keeps the promise." The model can run a syntactic audit against a description you supply. Whether the interface actually keeps the promise requires using the deployed tool as a real user, which the model cannot do.

*Series connection:* Interface-as-contract — the promise the user re-checks every session.

### Exercise 3 — Recipe Exercise
**Build:** a deployed brand tool with drafted interface states.

```
Using my tool description and archetype below, draft the interface copy for
four states: empty (user has not yet submitted anything), loading (system is
processing), success (system returned a result), and error (system failed).

Each state should:
- Hold my archetype's voice (not generic helpfulness)
- Make only promises the system description says it can keep
- Give the user enough information to know what to do next

Then identify one implicit promise my interface is making that the system
description does not confirm. Flag it for my alignment audit.

Tool description + archetype:
[PASTE]
```

**Adapt:** personal brand track — the "interface" is every surface a recruiter or hiring manager encounters. Audit your LinkedIn headline, resume summary, and email signature against the same four-layer framework.

### Exercise 4 — CLI Exercise
**Build:** a deployed tool and `your-brand/interface-contract.md`

```
Scaffold a Streamlit [or Gradio] interface for my tool that includes:
- Input affordance matching the system's actual inputs (no free-text prompt
  box if the system takes structured inputs)
- Visible processing state (spinner or progress bar)
- Output surface with one confidence qualifier
- Empty state copy in my brand voice
- Error state copy in my brand voice

Then write your-brand/interface-contract.md stating: the promise, the three
failure states and their copy, and how each was tested. Do not deploy to a
live host without my approval. Stop after the files + a working local run.
```

**Inspect:** empty, loading, and error states all exist and were actually triggered; voice matches archetype. **If it goes wrong:** the model builds happy-path only — force a failing input and confirm the copy holds.

### Exercise 5 — AI Validation Exercise
**Validate** the deployed interface. Rate each criterion Pass / Fail / Cannot-determine with evidence:

- **Correctness:** does the input affordance match the system's actual inputs — no free-text prompt where the system expects a URL, no "any document" claim where the system handles PDFs only?
- **Completeness:** all four states present (empty, loading, success, error) and tested with actual inputs?
- **Scope:** confidence misalignment, capability misalignment, and tone misalignment each checked in the alignment audit?
- **Brand-specific:** does the interface copy hold the archetype under failure, not just on the happy path?
- **Failure-mode check:** any capability claim in the interface that the system cannot reliably keep? Any state that defaults to generic copy rather than archetype-consistent copy?

**AI Use Disclosure:** two sentences — what the model produced and how you used it; one judgment it could not make (whether the deployed interface actually keeps its promises for real users) that required you to use the tool yourself.

---

## Key Terms

interface layers (visual surface / interaction model / deployment surface / brand surface) · confidence misalignment · capability misalignment · tone misalignment · alignment audit · minimum viable interface · Streamlit · Gradio · empty state · error state · README as interface

## Bridge

The deployed URL from this appendix is the first public artifact the brand has to account for. The alignment audit you ran before shipping is the first application of a discipline that generalizes: every brand surface should make only the promises the underlying reality can keep.
