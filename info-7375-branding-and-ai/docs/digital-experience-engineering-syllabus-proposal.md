# Digital Experience Engineering\*
## The Creative Engineer: Designing Experiences and Conducting Agentic AI

**Proposed syllabus revision for faculty and curriculum review · September 29, 2026**

The course title for this proposal is **Digital Experience Engineering\***. This is an agentic AI course in experience design and conducting AI, organized around the Creative Engineer. This draft reflects the permission in the supplied email exchange to redesign the content; it does not represent final curriculum approval.

## Course information

| Field | Proposed course information |
|---|---|
| Course number | INFO XXXX for permanent-course proposal; current special-topics identifier INFO 7375 |
| Term | Fall 2026 |
| Credit hours | 4 semester hours |
| CRN | 16549, carried from the supplied syllabus; confirm for the offering |
| Format | Online, as listed in the supplied syllabus |
| Instructors | Professor Nik Bear Brown — ni.brown@neu.edu; Professor Nina Harris — n.harris@northeastern.edu |
| Office hours | Zoom by appointment |
| Teaching assistant | Name, email, and office hours to be announced in Canvas |

## Course description

Digital Experience Engineering is an agentic AI course that teaches experience design and conducting AI. It develops the Creative Engineer: a practitioner who identifies worthwhile problems, designs coherent experiences, conducts AI agents through implementation, and evaluates what people can actually understand and accomplish with the resulting system. Students combine experience design, human–computer interaction, systems thinking, and agentic workflow design to create interactive products, services, and professional experiences.

The studio uses two primary tools: Figma for design and Northeastern-provided Claude for agentic implementation. Figma for Education, Figma Design, and FigJam support user journeys, information architectures, interaction models, design systems, agent responsibilities, and evaluation criteria. Students direct Claude to call Figma's Model Context Protocol (MCP) server, obtain structured design context, and implement bounded tasks. They inspect how design intent survives translation into a working experience, review the resulting changes, and revise designs through observation and testing.

Projects may include students' own original products and AI tools, personal branding and interactive portfolios, educational experiences, public-interest services, creative tools, onboarding systems, and workplace applications. Students deliver a tested functional experience and a portfolio case study documenting the problem, alternatives, design decisions, human and AI contributions, and evidence of improvement. Assessment emphasizes the quality of design, judgment, orchestration, and evaluation, with functional implementation providing the means to test those decisions.

## Intellectual foundation: the Creative Engineer

The course starts with a practical question: as agentic AI reduces the effort required for many implementation tasks, what should an engineer become better at deciding?

The answer organizes the studio: discovering a problem worth addressing, imagining alternatives, choosing an experience appropriate to its users, specifying how the system should behave, conducting its construction, and judging its consequences. Students examine the Creative Engineer chapter's arguments about professional signals as propositions to investigate. A polished artifact alone provides limited evidence of who made the consequential decisions.

The chapter's four verbs remain visible throughout the course:

- **Ideate:** discover needs, reframe the problem, generate alternatives, and choose a direction using evidence.
- **Build:** specify the behavior, delegate suitable work to agents, inspect changes, and verify a functional implementation.
- **Brand:** make purpose, identity, voice, and value legible through the experience. Personal branding is an explicit application, supported by truthful evidence of capability.
- **Ship:** put a usable experience before its intended reviewers or users, observe what happens, and revise. Classroom or controlled delivery can satisfy this requirement; public deployment is a separate choice.

These activities repeat as evidence changes the design. AI may contribute ideas, code, critique, tests, and documentation. Students remain responsible for deciding what deserves to be built, whether the evidence supports it, and which actions to authorize. The course does not assume every implementation task can be automated or that human judgment is infallible.

## Prerequisites

Working proficiency in at least one programming language, with Python recommended; basic familiarity with software, data, or information systems; and willingness to engage in design critique, independent investigation, and iterative work. Prior Figma experience is not required. Students must be able to inspect and explain the technical behavior of their submissions, including code produced with AI assistance.

## Learning outcomes

By the end of the course, students will be able to:

1. Formulate an experience-design problem from stakeholder needs, evidence, constraints, and explicit assumptions; compare plausible alternatives before selecting a solution.
2. Design coherent journeys, information structures, interactions, content, and visual systems for a defined audience, including professional identity and portfolio experiences where appropriate.
3. Build an inspectable Figma design system using components, variants, variables, layout rules, and annotations that communicate intent to both people and agents.
4. Specify human and agent responsibilities, system boundaries, data and service interfaces, permissions, and intervention points in an experience architecture.
5. Direct Claude through Figma MCP to translate structured design context into bounded implementation tasks, inspect changes, and evaluate fidelity to the intended experience.
6. Conduct AI through problem formulation, plausibility auditing, tool orchestration, interpretive judgment, and revision when new evidence changes earlier decisions.
7. Design and evaluate success, uncertainty, error, recovery, and human-handoff states, considering accessibility, privacy, security, and reliability.
8. Plan and carry out usability investigations and technical acceptance checks, distinguish observation from inference, and revise the experience using the results.
9. Deliver and defend a functional experience and portfolio case study showing alternatives, decisions, version history, contributions, evidence, and limitations.

## Tools and course materials

**Primary design environment:** Figma for Education, Figma Design, and FigJam. Students use these throughout the semester for research synthesis, diagrams, journeys, components, prototypes, critique, and design history.

**Primary implementation environment:** Claude through Northeastern's institutional offering. Students use Claude to interpret design briefs, propose implementation plans, produce and revise code, develop tests, and help investigate discrepancies. Claude Code is the intended client for repository-based implementation, subject to confirmation of institutional access. Students conduct the work and remain responsible for design decisions, accepted changes, and verification.

**Connection between the two:** Figma MCP calls originate from the course's NEU Claude environment. Students give Claude a scoped design reference and task; Claude retrieves the authorized Figma context; the student reviews the plan, implementation, and observed behavior. Figma remains the shared design source, and revisions return to that source so that design and implementation remain consistent. MCP is the connection between the primary tools, not a third design application.

Students begin at [Claude at Northeastern](https://claude.northeastern.edu/) and sign in with their university account through SSO. The portal confirms access for active students, faculty, and staff; it does not establish that every account has Claude Code or an enabled Figma connector. Before the integration studio, instructors verify the supported Claude client, institutional connector settings, Figma authorization, and available usage allowances. The baseline course does not require a personal paid Claude subscription or assume access to separately billed API credits.

Git and GitHub support version history, reviewed changes, and reproducible evidence. Runtime technologies follow the project's needs; learning a particular frontend framework is not the organizing objective.

Education verification and placement in an Education team are separate onboarding steps. Students verify their actual account, team, seat, file permissions, and available MCP tools before the first integration exercise. Figma documents Education access and the MCP connection in its [Education guide](https://help.figma.com/hc/en-us/articles/360041061214-Figma-for-Education) and [MCP introduction](https://developers.figma.com/docs/figma-mcp-server/). Availability and usage allowances can change; the course does not promise unlimited calls or universal access to every AI feature.

The central MCP exercise is reading structured design context and evaluating its implementation. Agent writes to a Figma canvas may be used when available and authorized. If access or quotas prevent an individual live run, an instructor demonstration plus an exported design-context packet provides the same critique and evaluation exercise, with the substituted evidence identified. Figma Make, Sites, Weave, and paid services are optional extensions, not prerequisites for completion.

Required readings are instructor-provided selections from **The Creative Engineer**, **Conducting AI**, and relevant experience-design materials. No textbook purchase is required. Two companion film sequences support studio work: [Figma for Educational AI](https://www.youtube.com/playlist?list=PLW3r2g0eZ8lA) for design and design context, and **Claude for Educational AI** for conducting implementation, reviewing changes, and evaluating results. The Claude playlist is planned; its link and selected films will be added when available. Until then, instructors assign selected materials from the local `anthropics` collection through Canvas. Canvas identifies the assigned selections and current setup instructions.

## Studio method

Each cycle follows **Predict → Design → Conduct → Experience → Verify and Revise**.

Conducting AI means framing the work, assigning bounded responsibilities to agents, providing relevant context, inspecting proposals and actions, evaluating evidence, and intervening when the work needs a new direction. Students practice this alongside experience design in every module.

Students predict how a person or agent will interpret the proposed experience, design alternatives in Figma, conduct a bounded implementation, observe the working result, and decide what to change. Short readings and films prepare students for online studios devoted to critique, demonstrations, design reviews, and evaluation. Each review asks what decision the student made, what evidence informed it, what the agent contributed, and what remains unresolved.

Implementation is required at a scale sufficient to test the design. Students may delegate substantial coding to agents. They must still understand the relevant architecture, inspect agent changes, and demonstrate that the resulting behavior meets their acceptance criteria. Neither code volume nor the number of tools used establishes design quality.

## Project choices and personal portfolios

Students pursue one main project through the semester. Acceptable domains include:

- **Original products and AI tools:** design an original digital product or AI-powered tool for a problem and audience the student identifies. Examples include an agentic research assistant, creative copilot, specialized learning tool, or new interactive service. Students define the product concept, user experience, core capabilities, and boundaries; design it in Figma; and conduct Claude through implementation, testing, and revision. For AI-powered products, they also design the AI's role, user controls, uncertainty, and human intervention points.
- **Personal branding and professional portfolios:** an interactive experience through which a defined audience can discover work, inspect evidence, understand an engineer's distinctive contribution, and make an informed next decision.
- **Educational experiences:** learning tools, feedback systems, interactive textbooks, study environments, or tutoring interfaces.
- **Public-interest and service experiences:** resource discovery, volunteer onboarding, community services, or accessible information systems.
- **Workplace and product experiences:** decision support, research workspaces, internal tools, onboarding, or collaboration systems.
- **Creative experiences:** interactive storytelling, cultural interpretation, music discovery, or tools that support creative practice.

Every project must include a meaningful interactive journey and at least one bounded agentic workflow in its design or operation. An agent need not face the end user: students may conduct agents to implement a deterministic experience. In that case, the agent workflow itself must have a design brief, permissions, review points, and evaluation evidence.

A personal-brand project is assessed through its audience fit, information architecture, interaction design, accessibility, credibility, and technical behavior. Students can use a fictional professional or consenting collaborator when personal disclosure is unsuitable. Archetypes may be used as creative prompts; their usefulness must be tested through the resulting design rather than treated as psychological diagnoses.

All students produce a professional portfolio case study of their course project, regardless of project domain. It should make their creative and supervisory contributions visible. Public posting, advertising expenditure, audience growth, and commercial success are not conditions for earning credit.

## Fourteen-week course schedule

| Week | Studio focus | Design and conducting work | Evidence or milestone |
|---|---|---|---|
| 1 | The Creative Engineer: designing and conducting AI | Ideate, Build, Brand, Ship; establish human design responsibility and agent implementation responsibilities; introduce project domains; set up Figma Education and NEU Claude | Initial experience critique, four-verb self-audit, setup record |
| 2 | Problem design and conducting AI inquiry | Stakeholders, user tasks, observation, constraints, and problem reframing; direct Claude to challenge assumptions and propose alternatives; distinguish generated suggestions from stakeholder evidence | **A1: Opportunity and experience brief** |
| 3 | Identity and information architecture with AI | Personal branding and portfolios as experience systems; design audience, voice, evidence, navigation, and journeys; conduct Claude's critique of competing architectures and justify the chosen structure | FigJam journey map and two competing information architectures |
| 4 | Interaction design and conducting AI critique | Design interaction flows, low-fidelity alternatives, hierarchy, typography, and accessibility; direct and challenge AI critique; choose a direction with reasons | **A2: Experience concepts and design rationale** |
| 5 | Design systems as instructions for agents | Figma components, variants, variables, auto layout, naming, annotations, and responsive behavior; specify what Claude should preserve, infer, or ask before changing | Inspectable design system and documented interaction states |
| 6 | Conducting AI through design context | Call Figma MCP through NEU Claude; compare a screenshot with structured context; specify scope, acceptance criteria, permissions, and change review; conduct Claude's implementation | Bounded design-to-implementation experiment and fidelity comparison |
| 7 | Designing agentic systems and conducting workflows | Design relationships among people, agents, software, data, and services; specify state, context, tool responsibilities, approval points, failure paths, and handoffs; conduct a bounded workflow | FigJam architecture, agent task contracts, and a working critical journey |
| 8 | Midterm defense: design and conducting decisions | Demonstrate the journey; defend alternatives and design choices; explain instructions given to Claude, accepted and rejected changes, and gaps between intention and behavior | **A3: Figma system, agentic prototype, and midterm defense** |
| 9 | Designing trust and human intervention in agentic AI | Design “I don't know,” sources, consent, permissions, escalation, correction, and undo; conduct Claude through failure scenarios and review recovery behavior | **A4: Agent orchestration and recovery design** |
| 10 | Conducting AI evaluation and human usability inquiry | Design task-based usability sessions and acceptance criteria; conduct Claude's test generation and accessibility review; compare automated findings with observed human experience | Evaluation plan, observations, and prioritized design changes |
| 11 | Designing operational constraints and conducting revision | Set latency, cost, reliability, privacy, and security requirements; direct Claude to investigate failures and implement justified revisions; review observability, deployment, and rollback choices | **A5: Evaluation and redesign dossier**, including operating assumptions |
| 12 | Conducting delivery and designing professional evidence | Conduct a reviewed, reproducible release; check design fidelity; design a portfolio narrative documenting decisions, version history, and human/AI contributions | Release candidate, case-study draft, and peer handoff |
| 13 | Final design and conducting reviews — Group 1 | Demonstrate the experience and its evidence; defend design judgment and supervision of AI; respond to critique and explain unresolved trade-offs | A6 presentations, Group 1; critique participation |
| 14 | Final design and conducting reviews — Group 2 and synthesis | Demonstrate, defend, and revise; explain how the Creative Engineer framed, designed, conducted, evaluated, and improved the experience | **A6: Final experience and portfolio case study**; Group 2 presentations |

Canvas supplies calendar dates, presentation groups, and delivery details. Weekly studio artifacts feed the six graded submissions; they do not create eleven separate implementation assignments. Both presentation groups have equal requirements and the same final revision deadline.

## Assessment and grading — proposed replacement

The following course-level weights replace the implementation-led categories in the supplied revision for purposes of this proposal. They are not an additional grading layer or a change to an already published course policy.

| Submission | Weight | What earns credit |
|---|---:|---|
| A1 — Opportunity and experience brief | 10% | Problem evidence, audience and context, scope, alternatives, measurable experience goals |
| A2 — Experience concepts and design rationale | 15% | Quality and distinctness of alternatives; information architecture, identity and content decisions; reasons for the chosen direction |
| A3 — Figma system, agentic prototype, and midterm defense | 20% | Coherent design system, interaction quality, explicit design intent, MCP evidence, reviewed agent implementation, and defense of the critical journey |
| A4 — Agent orchestration and recovery design | 15% | Clear responsibilities, bounded actions, permissions, state transitions, uncertainty, recovery, and human intervention |
| A5 — Evaluation and redesign dossier | 15% | Credible observations, appropriate tests, accessibility and operational checks, changes justified by evidence, and stated limits |
| A6 — Final experience and portfolio case study | 25% | Functional delivery, design coherence, evidence of improvement, reproducibility, professional communication, and identifiable individual judgment |
| **Total** | **100%** | |

Detailed rubrics are provided with each brief. Across the submissions, assessors examine problem framing, design quality, conducting decisions, functional evidence, evaluation, and communication. A visually polished submission with weak reasoning or an unusable core journey cannot earn full credit. A large codebase or complex deployment does not compensate for an unclear experience.

The final 25 points comprise: integrated experience quality (8), verified functionality and evaluation evidence (6), demonstrated conducting and technical judgment (5), and portfolio case study plus oral defense (6). This makes a working system consequential while keeping design and judgment central. Group projects must identify each student's decisions and contributions; each student submits an individual contribution account and participates in the defense.

## Final project deliverables

1. **Experience brief:** intended audience, problem, evidence, boundaries, alternatives, and success criteria.
2. **Figma design source:** journeys, information architecture, reusable system, annotated interaction states, and reviewable design history.
3. **Experience architecture:** people, agents, interfaces, services, data, and authority boundaries, including failures and recovery.
4. **Functional experience:** a runnable or deployed implementation of the core journey, with reproducible setup. Simulated integrations are clearly labeled and cannot stand in for every functional behavior.
5. **Conducting record:** representative briefs, agent actions, accepted and rejected proposals, important changes, checks, and human decisions. Submit relevant excerpts rather than an undigested chat archive.
6. **Evaluation dossier:** observed task outcomes, accessibility checks, technical acceptance results, limitations, and a before/after account of revisions.
7. **Portfolio case study and demonstration:** a clear account of what was designed, why it matters, how it changed, and what the student contributed. A private submission is sufficient.

## AI use and design responsibility

Agentic AI is a working partner throughout the studio. Students are encouraged to use it for exploration, implementation, testing, and critique while maintaining responsibility for design decisions and delivered behavior. They must be able to explain the system they submit, inspect changes affecting its important behavior, and distinguish an agent's assertion from observed evidence.

Credit AI contributions and source material. Preserve meaningful intermediate versions and record why consequential proposals were accepted or rejected. AI-generated personas, usability responses, quotations, and test results must be identified as synthetic; they cannot be represented as real interviews or observed user behavior. Design reviews should show at least one consequential decision the student made and the evidence used to make it.

Use synthetic or appropriately cleared project data in Claude and connected design files. Follow the requirements linked from the [NEU Claude portal](https://claude.northeastern.edu/), including the required review before uploading covered confidential information, personal information, or restricted research data. A connector does not grant permission to expose additional files or data. Scope access to the course project and review consequential write, sharing, and deployment actions before execution.

## Communication and success in the studio

Use Canvas discussions for general questions and clarifications. Contact the instructors or attend office hours for project and design critique; direct grading and administrative questions to the TA once assigned. The supplied syllabus's target response time is 48 hours during the academic week.

Start with a narrow, important journey. Bring alternatives to critique, keep design decisions visible, and test the experience before adding scope. Seek help when an unclear problem, interaction, handoff, or assumption prevents progress. Submit evidence that another person can follow from design intent to actual behavior.

## Administrative provisions

The academic-policy text and grade scale below are retained from the supplied proposal. They have not been independently verified as current university policy and require the ordinary institutional syllabus review before student distribution.

| Percentage | Grade | Grade points |
|---|---|---:|
| 95.0–100.0 | A | 4.000 |
| 90.0–94.9 | A− | 3.667 |
| 87.0–89.9 | B+ | 3.333 |
| 84.0–86.9 | B | 3.000 |
| 80.0–83.9 | B− | 2.667 |
| 77.0–79.9 | C+ | 2.333 |
| 74.0–76.9 | C | 2.000 |
| 70.0–73.9 | C− | 1.667 |
| 69.9 and below | F | 0.000 |

**Incomplete Grades.** An incomplete grade may be reported when a student has failed to complete a major component of a required course. The final decision on an incomplete is up to the instructor. Missing work should be completed within the required university timeframe or the final grade will reflect work completed and missing assignments receiving no credit.

**Attendance and Late Work.** Students are expected to participate beginning with the first day of class. Students registered in SEIS courses (INFO, CSYE, and DAMG) are allowed a maximum of 2 absences per course, with 3 or more absences resulting in an F for that course. Students must communicate with faculty before a deadline if work will be late; work submitted late without prior communication will not be graded.

**Religious Observance.** Students unable to participate because of religious beliefs will be provided an opportunity to make up missed academic requirements consistent with university policy. Requests should be made to the instructor in advance and in accordance with the University Policy on Instructional Accommodations for Student Religious Observance.

**Course Evaluations and SEIS Student Feedback.** Students are encouraged to complete midterm and end-of-term course evaluation surveys. Students may also provide anonymous feedback to SEIS regarding the course, instructors, or instructional support.

**Academic Integrity.** Students are responsible for following Northeastern University academic integrity requirements, including standards related to cheating, fabrication, plagiarism, unauthorized collaboration, participation in academically dishonest activities, and facilitating academic dishonesty.

**Student Accommodations / Disability Access Services (DAS).** Northeastern University and Disability Access Services (DAS) provide accommodations for eligible students. Students seeking accommodations should follow the DAS process and coordinate approved accommodations with the appropriate university offices and course instructors.

**Office of Global Services.** International students are responsible for maintaining applicable immigration and enrollment requirements. Students should consult the Office of Global Services for current guidance regarding instructional methods and status requirements.

**University Resources.** Students have access to Northeastern University Library services, Canvas technical support, ITS support, University Health and Counseling Services, and other university resources.

**Outreach, Engagement, and Belonging.** Northeastern University is committed to fostering a respectful and welcoming learning environment in which varied backgrounds, experiences, and perspectives contribute to teaching, research, and learning.

**Title IX.** Northeastern University prohibits sex- and gender-based discrimination and maintains university processes and resources for reporting and addressing prohibited conduct.

---

## Faculty review appendix: rationale and teaching resources

### What this revision changes

The supplied proposal establishes a sound engineering domain but organizes most weeks around implementation stages: integration, workflow construction, deployment, performance, and monitoring. This revision places the design of the experience and the conduct of agentic work at the center of those activities. Engineering rigor appears in explicit behavioral specifications, bounded interfaces, acceptance criteria, observed operation, and the student's ability to defend decisions.

Personal branding remains an explicit project option, studied as a designed interaction between a professional and an audience that needs to assess their work. Portfolios become evidence-bearing interfaces and a required account of creative and technical judgment. These applications coexist with educational, service, product, and creative experiences. The course's engineering contribution is made assessable through the quality of the designed system and its actual behavior.

Figma is used across the entire design cycle: framing and architecture in FigJam; interactions, systems, and prototypes in Figma Design; structured context through MCP; and review of discrepancies between the design and implementation. Students learn to direct agents using an inspectable specification and to evaluate the result as an experience.

### Playlist alignment

The linked playlist was inspected for its 26 listed titles on September 29, 2026. The mapping below is a proposed teaching use based on those titles and available local film descriptions, not a claim that every video was watched or every demonstration independently reproduced.

| Studio use | Selected playlist films |
|---|---|
| Creative Engineer and professional evidence | [Job-Hunting in Public, Without Needing a Job](https://www.youtube.com/watch?v=U6UdCOMBuUI); [Hand In the History, Not Just the Design](https://www.youtube.com/watch?v=saJieSuje84) |
| Design environment and onboarding | [Figma for Educational AI: A Design Tool for Engineers](https://www.youtube.com/watch?v=iikHWZjfqQE); [Verify, Then Upgrade](https://www.youtube.com/watch?v=VbICGMmMOak) |
| MCP and structured design context | [The Figma MCP Server: Hand Your Agent the Design](https://www.youtube.com/watch?v=L8XX50b-8y4); [Screenshot vs the Frame](https://www.youtube.com/watch?v=vaaGNW3jepY) |
| Design systems and design intent | [Auto Layout Is for the Agent?](https://www.youtube.com/watch?v=PTbTHSFbo2U); [Variables Become Your CSS](https://www.youtube.com/watch?v=yq553zEjdBo); [Tell the Agent What a Component Is For](https://www.youtube.com/watch?v=HMRFC9AtWEM) |
| Authority and human review | [The Agent Draws, You Merge](https://www.youtube.com/watch?v=DPBrdel-5Bw); [An Agent's Permission Slip](https://www.youtube.com/watch?v=pq4ZeONLJlc) |
| Uncertainty and evaluation | [Designing “I Don't Know”](https://www.youtube.com/watch?v=pv1ZpweUKcw); [Figma Eval Board to Tests](https://www.youtube.com/watch?v=tYH92Pqw-MM) |
| Continuing design and resource constraints | [The Diagram That Changes Every Week](https://www.youtube.com/watch?v=j_yLifLc38k); [What a Day of Figma Costs an Agent](https://www.youtube.com/watch?v=SKEollgJwTc) |

Films labeled “pending,” “the test we haven't run,” or “pending the class” are proposals or partial investigations. Use them to design and execute a classroom test, not as evidence that the test succeeded. Runtime capabilities and access should be checked against current documentation before assigning a dependent exercise.

### Planned Claude for Educational AI companion playlist

The `anthropics` collection provides source material for the planned playlist. The following is an editorial selection plan based on the inspected collection structure, course index, and available production notes. Local assets and production reports do not establish that a film is published, current, or ready for assignment. Review the selected films and reproduce access-dependent demonstrations before adding them to Canvas.

| Course alignment | Proposed Claude preparation | Local source candidates under `books/anthropics/` |
|---|---|---|
| Weeks 1–2: Creative Engineer and learning | Institutional onboarding, Claude as a learning and implementation partner, student responsibility | `youtube/claude-for-education/`; `youtube/claude-code-for-students/` |
| Weeks 3–5: Intent and context | Turn a design decision into a bounded brief; select relevant context and state acceptance criteria | `courses/real_world_prompting/`; `youtube/show-tell-context-is-a-budget/` |
| Week 6: Figma-to-Claude integration | Explain MCP tools and permissions; demonstrate the actual NEU Claude-to-Figma connection | `youtube/claude-mcp-connectors/`; pair with the Figma MCP films; record or verify the institutional setup separately |
| Weeks 6–8: Conducting implementation | Plan, implement, inspect changes, test, and revise a critical user journey | `youtube/claude-code/nbb-engineering-partner-loop/`; `youtube/show-tell-seven-steps-before-a-feature-ships/` |
| Weeks 7–9: Authority and recovery | Bound tool actions, define intervention points, and explain human approval | `youtube/show-tell-five-ways-to-wire-an-agent/`; `youtube/show-tell-where-the-hooks-fire/` |
| Weeks 10–11: Evidence and evaluation | Challenge generated claims, inspect test evidence, and compare behavior with design intent | `courses/prompt_evaluations/`; `youtube/show-tell-four-reviewers-and-a-sieve/` |
| Weeks 12–14: Delivery and portfolio evidence | Explain the student's decisions, implementation revisions, review history, and remaining limitations | `youtube/show-tell-from-session-to-dashboard/`; pair with the Figma history and professional-evidence films |

Select only the parts that support the studio's design and conducting outcomes. API-oriented source exercises may be adapted to the supported institutional Claude workflow; direct API programming is an optional extension. Each assigned film should lead to a small design decision, reviewed implementation action, or evaluation artifact for the student's project.

### Relationship to the companion courses

| Course | Distinct contribution to this studio |
|---|---|
| Prompt Engineering for Generative AI | Mechanisms behind prompts, tools, context, and agent loops |
| Conducting AI | Supervisory judgment, problem formulation, orchestration, and re-engagement |
| Computational Skepticism for AI | Tests and evidence that challenge a design or system claim |
| Irreducibly Human | Reasoned allocation of responsibility between people and AI |
| Digital Experience Engineering | Integration of these practices into a coherent experience for an audience, expressed through design and tested through use |

### Decisions before approval

Confirm the permanent course number and title, CRN and modality, proposed six-submission grading model, calendar dates, and the institution's required administrative wording. The existing repository describes a different 15-lesson and ten-day assignment structure; this 14-week proposal follows the supplied revision and must be adopted explicitly before replacing that structure. Faculty should also confirm tool access and the equivalent exercise for students affected by account limitations.

The Creative Engineer chapter supplies the framing, but its broad labor-market assertions and historical statistics should receive an editorial fact-check before being used as empirical course claims. This syllabus does not depend on a universal claim that AI has eliminated implementation work or that ideation cannot involve AI.
