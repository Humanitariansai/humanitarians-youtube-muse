# Title audit — Lectern run of 2026-09-27

## Executive summary

**What this is.** Every one of the **3,446 postings** sorted by what kind of job its title names, then compared against what that kind of job *should* do in the filter. The point is scale: there are 21 job functions here and 3,082 distinct titles, so instead of reading 3,446 postings you judge **20 family rules** and then read only the disagreements.

**What it found.** 23 postings were **kept from families that should never produce a keep** — the false positives. 1 were **rejected from families that should always produce a keep** — the candidate false negatives. 555 sit in families marked *judge*, where the word genuinely means two different jobs and only a person can split them.

**The most useful thing it found is a bug in itself.** The first version of this audit treated *training* as a teaching word and duly reported 27 rejected "education" jobs — which looked like a serious false-negative problem. They were **Pre-training, Post-Training, Training Runtime, and Researcher, Training**: machine-learning jobs. At an AI company *training* means training a model. The filter had been right about all of them and the audit was wrong. That is why `ML_TRAINING` is the first family rule and why every false-friend family carries a note explaining what the word actually means here.

**How to use it.** Read the two disagreement lists and the *judge* families. For each row: is the filter wrong, or is the family rule wrong? Both are common. Fix whichever it is — `keywords.json` for the filter, `title_families.json` for the rule — and note it in the class log.

---

## The families

`expect` is what the family rule claims should happen. Rows where the tally disagrees with `expect` are the audit.

| Family | expect | kept | rejected | postings | distinct titles | what the word actually means here |
|---|---|---:|---:|---:|---:|---|
| **ML_TRAINING** | reject | 0 | 26 | 26 | 25 | FALSE FRIEND, and the reason this family is first. At an AI company 'training' overwhelmingly means training a MODEL, not teaching a person. 25 of the 27 postings whose titles contain a teaching word  |
| **TEACHING** | keep | 10 **← 1 rejected** | 1 | 11 | 11 | People being taught. This is the target. Pattern widened 2026-09-26: 'Head of Technical Training' was landing in UNCLASSIFIED because the old pattern required a trailing lead/specialist/manager. |
| **EDU_PRODUCT** | judge | 5 | 18 | 23 | 18 | ADDED 2026-09-26. Engineering, product, and PM roles ON an education product — OpenAI's 'Full-Stack Engineer, ChatGPT Education & Learning' and 'Tech Lead Manager, Education', Anthropic's 'Full Stack  |
| **ADVOCACY** | keep | 11 | 0 | 11 | 11 | Teaching a public rather than a classroom. Also the target. |
| **MATERIALS** | keep | 2 | 0 | 2 | 2 | ADDED 2026-09-26. Jobs whose product is the MATERIALS — docs, guides, tutorials, courseware, reference builds. Anthropic's 'Technical Documentation and Content Engineer, Claude Docs' is the model. Not |
| **SALES_ENABLEMENT** | keep | 13 | 0 | 13 | 12 | REVERSED 2026-09-26 by Professor Bear: "developing materials… to train their own people would be a great fit." Sales enablement builds curriculum, runs live training, and produces onboarding content f |
| **TECH_ENABLEMENT** | reject | 7 **← 7 kept** | 0 | 7 | 7 | FALSE FRIEND. Here 'enablement' means making a system capable of something. These are engineering jobs. Still a reject: here 'enablement' describes a system gaining a capability, with no materials and |
| **CUSTOMER_ENABLEMENT** | judge | 8 | 0 | 8 | 8 | GENUINELY AMBIGUOUS. Customer enablement does teach — live training, workshops, adoption plans — but for paying accounts, with renewal risk attached. Whether it counts is a judgment about what the sea |
| **EDU_SALES** | judge | 8 | 0 | 8 | 6 | MOVED to judge 2026-09-26: Professor Bear's target includes developing materials "to sell into universities." A Higher Education Account Executive who only carries a quota is still a reject; one who b |
| **RECRUITING** | reject | 2 **← 2 kept** | 51 | 53 | 49 | FALSE FRIEND, and the one that caught the topic-word rule out. 'University', 'campus', and 'student' are campus-recruiting vocabulary as much as teaching vocabulary. |
| **COMMUNITY** | judge | 10 | 12 | 22 | 22 | AMBIGUOUS. A developer-community manager teaches; a data-centre community-engagement manager does local-government relations; a security-community lead runs vulnerability disclosure. Same word, three  |
| **SALES** | reject | 0 | 602 | 602 | 519 |  |
| **CUSTOMER** | reject | 0 | 259 | 259 | 214 |  |
| **MARKETING** | reject | 3 **← 3 kept** | 194 | 197 | 191 |  |
| **DESIGN** | reject | 0 | 51 | 51 | 45 |  |
| **RESEARCH_DATA** | reject | 2 **← 2 kept** | 293 | 295 | 239 |  |
| **PRODUCT** | reject | 0 | 200 | 200 | 193 |  |
| **ENGINEERING** | reject | 4 **← 4 kept** | 874 | 878 | 790 |  |
| **G_AND_A** | reject | 2 **← 2 kept** | 154 | 156 | 150 |  |
| **OPERATIONS** | reject | 3 **← 3 kept** | 127 | 130 | 124 |  |
| **UNCLASSIFIED** | judge | 7 | 487 | 494 | 446 | No family matched the title. Either a function nobody listed, or a title too vague to classify. |
| TOTAL | | 97 | 3349 | 3,446 | 3,082 | |

## Kept, but the family says reject — 23 false positives

| Family | Company | Title | Location | Why the filter decided that | Verdict | Note |
|---|---|---|---|---|---|---|
| ENGINEERING | Anthropic | [Software Engineer, Education](https://job-boards.greenhouse.io/anthropic/jobs/5389305008) | San Francisco, CA / New York Cit |  |  |  |
| ENGINEERING | Anthropic | [Technical Architect](https://job-boards.greenhouse.io/anthropic/jobs/5421566008) | Remote-Friendly (Travel-Required |  |  |  |
| ENGINEERING | OpenAI | [Developer Experience Engineer, Cyber](https://jobs.ashbyhq.com/openai/708121e8-51ac-4a24-a2ff-bd9889ba5486) | San Francisco |  |  |  |
| ENGINEERING | OpenAI | [Full Stack Software Engineer, Education](https://jobs.ashbyhq.com/openai/9b1b62f5-1400-4672-910a-fda6f975f642) | San Francisco |  |  |  |
| G_AND_A | OpenAI | [Enablement Lead, Government](https://jobs.ashbyhq.com/openai/4cfc6b6b-dd8f-4101-897d-3217e45db1e4) | Washington, DC |  |  |  |
| G_AND_A | Stripe | [Product Compliance and Enablement Manager](https://stripe.com/jobs/search?gh_jid=8003129) | London, Dublin |  |  |  |
| MARKETING | Canva | [Education Marketing Specialist - Indonesia (6-month contract)](https://jobs.smartrecruiters.com/Canva/6000000001299549-education-marketing-specialist-indonesia-6-month-contract-) | Jakarta, Jakarta, Indonesia |  |  |  |
| MARKETING | OpenAI | [Integrated Marketing Manager, Youth Culture](https://jobs.ashbyhq.com/openai/58f32cbe-8c68-415c-bb7f-b6fca4b29ffc) | San Francisco |  |  |  |
| MARKETING | Replit | [Japan Growth Lead](https://jobs.ashbyhq.com/replit/999e1432-3edd-453b-b598-ab4b26e1bc5c) | Remote - Japan |  |  |  |
| OPERATIONS | Canva | [International Growth Strategy Lead (Education)](https://jobs.smartrecruiters.com/Canva/6000000001329699-international-growth-strategy-lead-education-) | Sydney, , Australia |  |  |  |
| OPERATIONS | OpenAI | [AI Deployment Manager (Builder) - Tokyo](https://jobs.ashbyhq.com/openai/bb569a6b-a7e9-4c4d-a78e-d35349b2f9d9) | Tokyo, Japan |  |  |  |
| OPERATIONS | OpenAI | [AI Deployment Manager - Builder](https://jobs.ashbyhq.com/openai/9675cfd2-a983-49d7-80db-d3d58c42eb08) | San Francisco |  |  |  |
| RECRUITING | Netlify | [Your Chance to Join Our Talent Community!](https://job-boards.greenhouse.io/netlify/jobs/4224129002) | Remote |  |  |  |
| RECRUITING | Notion | [Head of Early Career Recruiting](https://jobs.ashbyhq.com/notion/076371b1-e9b0-4ad7-b67b-ae9e4572f65a) | San Francisco, California · New  |  |  |  |
| RESEARCH_DATA | Anthropic | [Safeguards Enforcement Analyst, Conventional Weapons](https://job-boards.greenhouse.io/anthropic/jobs/5410006008) | San Francisco, CA / New York Cit |  |  |  |
| RESEARCH_DATA | OpenAI | [Applied AI Architect, Education](https://jobs.ashbyhq.com/openai/98bffd0e-05cf-4748-93f1-b115c84e37b4) | London, UK |  |  |  |
| TECH_ENABLEMENT | GitLab | [Senior Backend Engineer, Platform Enablement](https://job-boards.greenhouse.io/gitlab/jobs/8750842002) | Remote, United States |  |  |  |
| TECH_ENABLEMENT | Notion | [Workflow + Process Designer (AI Enablement)](https://jobs.ashbyhq.com/notion/c799f1f0-0e7b-4eac-98ce-44223130f2b0) | San Francisco, California |  |  |  |
| TECH_ENABLEMENT | OpenAI | [Applied AI Engineer, Agent Enablement](https://jobs.ashbyhq.com/openai/c1a28411-266b-487b-8ef3-03efb254fc36) | San Francisco |  |  |  |
| TECH_ENABLEMENT | OpenAI | [Full Stack Software Engineer, Agent Enablement](https://jobs.ashbyhq.com/openai/2d7f1028-ce9b-49c7-acc8-782714ca1cf4) | San Francisco |  |  |  |
| TECH_ENABLEMENT | OpenAI | [IT Software Architect, SaaS Enablement and Governance](https://jobs.ashbyhq.com/openai/1e68e5f6-6bda-4d11-89fd-4be731077031) | San Francisco |  |  |  |
| TECH_ENABLEMENT | OpenAI | [Software Engineer, Workload Enablement](https://jobs.ashbyhq.com/openai/9efcef02-0515-4672-bace-81329944b38b) | San Francisco · Seattle |  |  |  |
| TECH_ENABLEMENT | Replit | [Senior Software Engineer, Growth Enablement](https://jobs.ashbyhq.com/replit/f2f56292-890e-498c-844c-07f2bea8ea7a) | Foster City, CA |  |  |  |

## Rejected, but the family says keep — 1 candidate false negatives

| Family | Company | Title | Location | Why the filter decided that | Verdict | Note |
|---|---|---|---|---|---|---|
| TEACHING | Notion | [[Contract] Language Training Specialist - Japanese](https://jobs.ashbyhq.com/notion/f1f9e19d-cbf3-49eb-9824-d04adf2e3d75) | Tokyo, Japan  | only 1 topic words, no role word in title |  |  |

## The *judge* families — 555 postings where the word means two different jobs

| Family | Company | Title | Location | Why the filter decided that | Verdict | Note |
|---|---|---|---|---|---|---|
| COMMUNITY | Anthropic | [Community Engagement Manager, Data Centers (Texas)](https://job-boards.greenhouse.io/anthropic/jobs/5391983008) | Austin, TX / Remote-Friendly, Un |  |  |  |
| COMMUNITY | Anthropic | [Community Engagement Manager, Data Centres (Australia)](https://job-boards.greenhouse.io/anthropic/jobs/5391999008) | Sydney, Australia / Remote-Frien |  |  |  |
| COMMUNITY | Anthropic | [Community Engagement Manager, Data Centres (Canada)](https://job-boards.greenhouse.io/anthropic/jobs/5391974008) | Alberta, CAN / Remote-Friendly,  |  |  |  |
| COMMUNITY | Anthropic | [Head of Community, Enterprise Marketing](https://job-boards.greenhouse.io/anthropic/jobs/5388719008) | San Francisco, CA / New York Cit |  |  |  |
| COMMUNITY | Anthropic | [Head of Partner Account Management & Ecosystem BD](https://job-boards.greenhouse.io/anthropic/jobs/5391195008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| COMMUNITY | Anthropic | [Head of Vulnerability Disclosure & Security Community](https://job-boards.greenhouse.io/anthropic/jobs/5397699008) | San Francisco, CA / New York Cit |  |  |  |
| COMMUNITY | Anthropic | [Staff+ Software Engineer, Platform Ecosystem](https://job-boards.greenhouse.io/anthropic/jobs/5392335008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| COMMUNITY | Canva | [Technical Support Manager - Ecosystem](https://jobs.smartrecruiters.com/Canva/6000000001232059-technical-support-manager-ecosystem) | Makati, , Philippines | only 1 topic words, no role word in title |  |  |
| COMMUNITY | GitLab | [Ecosystem Sales Manager](https://job-boards.greenhouse.io/gitlab/jobs/8684201002) | Remote, United States | no-keyword-match |  |  |
| COMMUNITY | GitLab | [Senior Ecosystem Sales Manager (ESM)- ASEAN](https://job-boards.greenhouse.io/gitlab/jobs/8808524002) | Remote, Singapore | no-keyword-match |  |  |
| COMMUNITY | GitLab | [Senior Ecosystem Sales Manager, Japan](https://job-boards.greenhouse.io/gitlab/jobs/8640173002) | Remote, Japan | no-keyword-match |  |  |
| COMMUNITY | HubSpot | [Senior Director, Ecosystem Product (Builder Platform)](https://www.hubspot.com/careers/jobs/7779509?gh_jid=7779509) | Remote - USA | no-keyword-match |  |  |
| COMMUNITY | OpenAI | [Community Engagement Lead, Ohio](https://jobs.ashbyhq.com/openai/4df2842a-016d-4c69-a011-fab47aa5f981) | US - Remote |  |  |  |
| COMMUNITY | OpenAI | [Federal Account Director, Intelligence Community](https://jobs.ashbyhq.com/openai/fd5522f1-8e39-4d60-8b8a-34fae61104cb) | Washington, DC |  |  |  |
| COMMUNITY | OpenAI | [Software Engineer, Plugin Ecosystem](https://jobs.ashbyhq.com/openai/e42305bf-2266-4dff-82ad-42be7ddac495) | San Francisco | no-keyword-match |  |  |
| COMMUNITY | OpenAI | [Strategic Delivery Lead, Intelligence Community](https://jobs.ashbyhq.com/openai/5f3a6397-47ac-4ef0-9ca9-cd358851a6b9) | Washington, DC |  |  |  |
| COMMUNITY | Stripe | [Full Stack Engineer, Enterprise & Ecosystem](https://stripe.com/jobs/search?gh_jid=8118929) | N/A | no-keyword-match |  |  |
| COMMUNITY | Stripe | [Partner Solutions Engineer, Ecosystem](https://stripe.com/jobs/search?gh_jid=8227563) | US-NYC; US-SF; US-Chicago; US-At | no-keyword-match |  |  |
| COMMUNITY | Stripe | [Product Manager, Ecosystem Risk](https://stripe.com/jobs/search?gh_jid=7984866) | Toronto | no-keyword-match |  |  |
| COMMUNITY | Stripe | [Short-form Video & Social, Community Comms](https://stripe.com/jobs/search?gh_jid=7373865) | SF, NYC |  |  |  |
| COMMUNITY | Supabase | [Event Programs Manager, Developer Community & Ecosystem](https://jobs.ashbyhq.com/supabase/715ba1ea-bd0b-4960-9d5a-defca99f2e24) | Remote, San Francisco, CA |  |  |  |
| COMMUNITY | Supabase | [Partnerships Manager, Ecosystem](https://jobs.ashbyhq.com/supabase/f0f277ac-b96c-478a-81ca-7bd80612533f) | Remote, AMER | only 1 topic words, no role word in title |  |  |
| CUSTOMER_ENABLEMENT | Anthropic | [Scaled Enablement Programs Lead](https://job-boards.greenhouse.io/anthropic/jobs/5391146008) | San Francisco, CA / New York Cit |  |  |  |
| CUSTOMER_ENABLEMENT | Figma | [Customer Enablement Manager (Berlin, Germany)](https://boards.greenhouse.io/figma/jobs/6133181004?gh_jid=6133181004) | Berlin, Germany |  |  |  |
| CUSTOMER_ENABLEMENT | Figma | [Customer Enablement Manager (London, United Kingdom)](https://boards.greenhouse.io/figma/jobs/6130557004?gh_jid=6130557004) | London, England |  |  |  |
| CUSTOMER_ENABLEMENT | Figma | [Customer Enablement Manager (Paris, France)](https://boards.greenhouse.io/figma/jobs/5976498004?gh_jid=5976498004) | Paris, France |  |  |  |
| CUSTOMER_ENABLEMENT | Figma | [Customer Enablement Manager (São Paulo, Brazil)](https://boards.greenhouse.io/figma/jobs/6104028004?gh_jid=6104028004) | São Paulo, Brazil |  |  |  |
| CUSTOMER_ENABLEMENT | Figma | [Manager, Customer Enablement (Tokyo, Japan)](https://boards.greenhouse.io/figma/jobs/6144873004?gh_jid=6144873004) | Tokyo, Japan |  |  |  |
| CUSTOMER_ENABLEMENT | Notion | [Manager, Enablement Programs](https://jobs.ashbyhq.com/notion/98bb09a8-2fdf-4c12-84dd-8568553159d8) | San Francisco, California |  |  |  |
| CUSTOMER_ENABLEMENT | Stripe | [Compliance Manager, User Enablement](https://stripe.com/jobs/search?gh_jid=7530580) | Dublin OR London |  |  |  |
| EDU_PRODUCT | Anthropic | [Full Stack Engineer, Education Labs](https://job-boards.greenhouse.io/anthropic/jobs/5097186008) | San Francisco, CA / New York Cit |  |  |  |
| EDU_PRODUCT | Anthropic | [Machine Learning Infrastructure Engineer, Safeguards Research](https://job-boards.greenhouse.io/anthropic/jobs/5364804008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| EDU_PRODUCT | Canva | [K-12 Education Account Manager Vietnam (12-Month Contract)](https://jobs.smartrecruiters.com/Canva/6000000001319223-k-12-education-account-manager-vietnam-12-month-contract-) | Ho Chi Minh City, Ho Chi Minh, V |  |  |  |
| EDU_PRODUCT | Canva | [Product Support Specialist, Education Team  (Full time, 1-year contrac](https://jobs.smartrecruiters.com/Canva/6000000001287750-product-support-specialist-education-team-full-time-1-year-contract-) | Bengaluru, , India |  |  |  |
| EDU_PRODUCT | Canva | [Project Manager, Education Team (Full time, 1-year contract)](https://jobs.smartrecruiters.com/Canva/6000000001287015-project-manager-education-team-full-time-1-year-contract-) | Delhi, , India |  |  |  |
| EDU_PRODUCT | Canva | [Senior Machine Learning Engineer - Private Search Quality (AU remote)](https://jobs.smartrecruiters.com/Canva/6000000001359898-senior-machine-learning-engineer-private-search-quality-au-remote-) | Sydney, NSW, Australia | only 1 topic words, no role word in title |  |  |
| EDU_PRODUCT | Canva | [Senior Machine Learning Engineer - Private Search Quality (AU remote)](https://jobs.smartrecruiters.com/Canva/6000000001359733-senior-machine-learning-engineer-private-search-quality-au-remote-) | Melbourne, , Australia | only 1 topic words, no role word in title |  |  |
| EDU_PRODUCT | Canva | [Senior Machine Learning Engineer - Research Optimisation](https://jobs.smartrecruiters.com/Canva/6000000001162285-senior-machine-learning-engineer-research-optimisation) | Sydney, , Australia | only 1 topic words, no role word in title |  |  |
| EDU_PRODUCT | OpenAI | [Full-Stack Engineer, ChatGPT Education  & Learning](https://jobs.ashbyhq.com/openai/ef828b89-41ed-4cde-96a9-94ffe5770d4c) | San Francisco |  |  |  |
| EDU_PRODUCT | OpenAI | [Machine Learning Engineer, API Multicloud](https://jobs.ashbyhq.com/openai/5acf4854-1d42-40ca-bff8-4f6f04cdce68) | San Francisco | no-keyword-match |  |  |
| EDU_PRODUCT | OpenAI | [Machine Learning Engineer, Core Experimentation](https://jobs.ashbyhq.com/openai/9d4d2727-27f3-4a63-857c-a96466130645) | Seattle | no-keyword-match |  |  |
| EDU_PRODUCT | OpenAI | [Machine Learning Engineer, Distributed Data Systems - Robotics](https://jobs.ashbyhq.com/openai/4a13c764-18c3-4076-ac87-29e05491be07) | San Francisco | no-keyword-match |  |  |
| EDU_PRODUCT | OpenAI | [Machine Learning Engineer, Integrity](https://jobs.ashbyhq.com/openai/ecf1abec-898c-4acb-a984-42858836a1ff) | San Francisco | no-keyword-match |  |  |
| EDU_PRODUCT | OpenAI | [Machine Learning Engineer, Monetization AI/ML](https://jobs.ashbyhq.com/openai/80f9f564-d789-47bc-91c3-3babf5a1a33d) | San Francisco | no-keyword-match |  |  |
| EDU_PRODUCT | OpenAI | [Machine Learning Engineer, Multimodal Perception and Authentication](https://jobs.ashbyhq.com/openai/1b268692-70d8-46c2-a347-2f7705b5c174) | San Francisco | no-keyword-match |  |  |
| EDU_PRODUCT | Stripe | [Machine Learning Engineer](https://stripe.com/jobs/search?gh_jid=8014859) | Toronto | no-keyword-match |  |  |
| EDU_PRODUCT | Stripe | [Machine Learning Engineer, Link](https://stripe.com/jobs/search?gh_jid=8197886) | New York City  | no-keyword-match |  |  |
| EDU_PRODUCT | Stripe | [Staff Machine Learning Engineer, Financial Connections](https://stripe.com/jobs/search?gh_jid=8148653) | New York | no-keyword-match |  |  |
| EDU_PRODUCT | Stripe | [Staff Software Engineer, Machine Learning Platform](https://stripe.com/jobs/search?gh_jid=7939868) | San Francisco, Seattle | no-keyword-match |  |  |
| EDU_PRODUCT | Stripe | [Staff Software Engineer, Machine Learning Platform](https://stripe.com/jobs/search?gh_jid=7712852) | Toronto | no-keyword-match |  |  |
| EDU_PRODUCT | Twilio | [Machine Learning Engineer](https://job-boards.greenhouse.io/twilio/jobs/7996774) | Remote - Ireland | no-keyword-match |  |  |
| EDU_PRODUCT | Twilio | [Machine Learning Engineer](https://job-boards.greenhouse.io/twilio/jobs/7702644) | Remote - US | no-keyword-match |  |  |
| EDU_PRODUCT | Twilio | [Machine Learning Engineer](https://job-boards.greenhouse.io/twilio/jobs/8007455) | Remote - Spain | no-keyword-match |  |  |
| EDU_SALES | Anthropic | [Research & Education Sales Lead, Beneficial Deployments](https://job-boards.greenhouse.io/anthropic/jobs/5415930008) | San Francisco, CA / New York Cit |  |  |  |
| EDU_SALES | Canva | [Account Executive, Higher Education](https://jobs.smartrecruiters.com/Canva/6000000001424458-account-executive-higher-education) | Austin, , United States |  |  |  |
| EDU_SALES | Canva | [Account Executive, Higher Education (LATAM)](https://jobs.smartrecruiters.com/Canva/6000000001424453-account-executive-higher-education-latam-) | Austin, , United States |  |  |  |
| EDU_SALES | Canva | [Business Development Representative (Higher Education - Public Sector)](https://jobs.smartrecruiters.com/Canva/6000000001375179-business-development-representative-higher-education-public-sector-) | Austin, TX, United States |  |  |  |
| EDU_SALES | Canva | [Higher Education Account Executive](https://jobs.smartrecruiters.com/Canva/6000000001371584-higher-education-account-executive) | Sydney, NSW, Australia |  |  |  |
| EDU_SALES | Stripe | [University Recruiter](https://stripe.com/jobs/search?gh_jid=8226211) | San Francisco, New York, Seattle |  |  |  |
| EDU_SALES | Stripe | [University Recruiter](https://stripe.com/jobs/search?gh_jid=8128011) | Dublin, London |  |  |  |
| EDU_SALES | Stripe | [University Recruiter](https://stripe.com/jobs/search?gh_jid=8159355) | N/A |  |  |  |
| UNCLASSIFIED | Anthropic | [AV Production Specialist](https://job-boards.greenhouse.io/anthropic/jobs/5379593008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Anthropic Fellows Program, ML Systems & Reinforcement Learning](https://job-boards.greenhouse.io/anthropic/jobs/5183051008) | London, UK; Ontario, CAN; Remote | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Compute Country Lead, Canada](https://job-boards.greenhouse.io/anthropic/jobs/5385546008) | Remote-Friendly (Travel Required | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Compute Country Lead, Japan](https://job-boards.greenhouse.io/anthropic/jobs/5385559008) | Tokyo, Japan | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Compute Country Lead, Korea](https://job-boards.greenhouse.io/anthropic/jobs/5385557008) | Seoul, South Korea | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Contracts Manager, EMEA](https://job-boards.greenhouse.io/anthropic/jobs/5264820008) | London, UK | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Corporate Development Integration Lead](https://job-boards.greenhouse.io/anthropic/jobs/5358146008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Corporate Development Lead, Life Sciences](https://job-boards.greenhouse.io/anthropic/jobs/5358110008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Customer Trust Specialist](https://job-boards.greenhouse.io/anthropic/jobs/5418991008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Director, Global Order-to-Cash Transformation](https://job-boards.greenhouse.io/anthropic/jobs/5205735008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Director, Investor Relations](https://job-boards.greenhouse.io/anthropic/jobs/5345466008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Energy Scheduling & Portfolio Lead](https://job-boards.greenhouse.io/anthropic/jobs/5399223008) | Remote-Friendly, United States | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Engineering Manager, Business Technology](https://job-boards.greenhouse.io/anthropic/jobs/5418402008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Engineering Manager, Connectivity - London](https://job-boards.greenhouse.io/anthropic/jobs/5309805008) | London, UK | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Engineering Manager, Cybersecurity Products](https://job-boards.greenhouse.io/anthropic/jobs/5236531008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Engineering Manager, Enterprise](https://job-boards.greenhouse.io/anthropic/jobs/5255912008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Engineering Manager, GPU (ML Accelerator)](https://job-boards.greenhouse.io/anthropic/jobs/4741104008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Engineering Manager, Growth](https://job-boards.greenhouse.io/anthropic/jobs/5361472008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Engineering Manager, Research Productivity](https://job-boards.greenhouse.io/anthropic/jobs/5223093008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Engineering Manager, Safeguards](https://job-boards.greenhouse.io/anthropic/jobs/5410610008) | London, UK | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Engineering Manager, Safeguards Review Tooling](https://job-boards.greenhouse.io/anthropic/jobs/5013366008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Engineering Manager, Scheduler and Fleet Efficiency](https://job-boards.greenhouse.io/anthropic/jobs/5411267008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Engineering Manager, Search](https://job-boards.greenhouse.io/anthropic/jobs/5371065008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Executive Escalations Manager](https://job-boards.greenhouse.io/anthropic/jobs/5418743008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [External Affairs, Brussels](https://job-boards.greenhouse.io/anthropic/jobs/5430422008) | Brussels, Belgium | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [External Affairs, South Korea](https://job-boards.greenhouse.io/anthropic/jobs/5417967008) | Seoul, South Korea | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Hardware Lab Manager](https://job-boards.greenhouse.io/anthropic/jobs/5378092008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Head of Business Controls](https://job-boards.greenhouse.io/anthropic/jobs/5357943008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Head of Business Technology Engineering](https://job-boards.greenhouse.io/anthropic/jobs/5431374008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Head of Global Renewals](https://job-boards.greenhouse.io/anthropic/jobs/5237923008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Head of Partnerships, Japan](https://job-boards.greenhouse.io/anthropic/jobs/5391207008) | Tokyo, Japan | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Head of Strategic Startups](https://job-boards.greenhouse.io/anthropic/jobs/5419210008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Incident Manager - Detection & Response](https://job-boards.greenhouse.io/anthropic/jobs/5397749008) | San Francisco, CA / Seattle, WA  | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Incident Response Manager - Privacy](https://job-boards.greenhouse.io/anthropic/jobs/5432528008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Incident Response Manager - Product & Engineering](https://job-boards.greenhouse.io/anthropic/jobs/5205495008) | Dublin, IE; London, UK; New York | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Life Sciences Operator, Lead](https://job-boards.greenhouse.io/anthropic/jobs/5357746008) | New York City, NY | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Manager, Corporate Network Engineering](https://job-boards.greenhouse.io/anthropic/jobs/5391782008) | San Francisco, CA | only 2 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Manager, Web Engineering](https://job-boards.greenhouse.io/anthropic/jobs/5287926008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Partner Success Lead](https://job-boards.greenhouse.io/anthropic/jobs/5391215008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Partner Success Lead](https://job-boards.greenhouse.io/anthropic/jobs/5427025008) | London, UK | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Partnership Manager, AI for Science](https://job-boards.greenhouse.io/anthropic/jobs/5407938008) | San Francisco, CA / New York Cit |  |  |  |
| UNCLASSIFIED | Anthropic | [Partnerships Manager, US Public Health](https://job-boards.greenhouse.io/anthropic/jobs/5418748008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Product Management, Research](https://job-boards.greenhouse.io/anthropic/jobs/5123082008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Product Support Specialist](https://job-boards.greenhouse.io/anthropic/jobs/5138042008) | Tokyo, Japan | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Product Support Specialist](https://job-boards.greenhouse.io/anthropic/jobs/4979585008) | New York City, NY; San Francisco | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Program Specialist, M&A](https://job-boards.greenhouse.io/anthropic/jobs/5382617008) | San Francisco, CA | only 2 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Reseller Enablement Lead](https://job-boards.greenhouse.io/anthropic/jobs/5391269008) | London, UK |  |  |  |
| UNCLASSIFIED | Anthropic | [Safeguards Enforcement Lead, Cyber Harms](https://job-boards.greenhouse.io/anthropic/jobs/5403775008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Safeguards Enforcement Lead, User Well-Being](https://job-boards.greenhouse.io/anthropic/jobs/5410004008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Senior Manager, IT SOX](https://job-boards.greenhouse.io/anthropic/jobs/5430222008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Startup Partnerships - France & Southern Europe](https://job-boards.greenhouse.io/anthropic/jobs/5131095008) | Paris, France | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Strategic Deals Lead, Cloud Compute](https://job-boards.greenhouse.io/anthropic/jobs/5358104008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Strategic Deals Lead, Compute Partnerships](https://job-boards.greenhouse.io/anthropic/jobs/5358106008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Strategic Partner Development, Product Partnerships - Cybersecurity](https://job-boards.greenhouse.io/anthropic/jobs/5226540008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Strategic Pursuits Lead, RevOps](https://job-boards.greenhouse.io/anthropic/jobs/5390935008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Technical Cyber Threat Investigator](https://job-boards.greenhouse.io/anthropic/jobs/5066995008) | Remote-Friendly (Travel-Required | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Threat Intel Manager, CBRN-E & Advanced Weapons](https://job-boards.greenhouse.io/anthropic/jobs/5305631008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Threat Intel Manager, Model Exploitation & Fraud](https://job-boards.greenhouse.io/anthropic/jobs/5305476008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Transaction Manager](https://job-boards.greenhouse.io/anthropic/jobs/5398827008) | Remote-Friendly, United States | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Transaction Manager, Canada](https://job-boards.greenhouse.io/anthropic/jobs/5418421008) | Remote-Friendly (Travel Required | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Transaction Principal, EU](https://job-boards.greenhouse.io/anthropic/jobs/5398829008) | London, UK | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [Treasury Director, Investments & Liquidity](https://job-boards.greenhouse.io/anthropic/jobs/5358114008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [VC Partnerships Lead](https://job-boards.greenhouse.io/anthropic/jobs/5235692008) | San Francisco, CA / New York Cit | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Anthropic | [[DH] Engineering Manager, AI Observability](https://job-boards.greenhouse.io/anthropic/jobs/5429202008) | San Francisco, CA | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [AI Partnerships Lead](https://jobs.smartrecruiters.com/Canva/6000000001388356-ai-partnerships-lead) | San Francisco, , United States | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [AI Quality Evaluator - Czech (12-month Contract)](https://jobs.smartrecruiters.com/Canva/6000000001409416-ai-quality-evaluator-czech-12-month-contract-) | Prague, Prague, Czechia | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [AI Quality Evaluator - Dutch (12-Month Contract)](https://jobs.smartrecruiters.com/Canva/6000000001363421-ai-quality-evaluator-dutch-12-month-contract-) | Amsterdam, NH, Netherlands | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [AI Quality Evaluator - Hindi (12-month contract)](https://jobs.smartrecruiters.com/Canva/6000000001261958-ai-quality-evaluator-hindi-12-month-contract-) | Bengaluru, KA, India | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [AI Quality Evaluator - Italian (12-month Contract)](https://jobs.smartrecruiters.com/Canva/6000000001411681-ai-quality-evaluator-italian-12-month-contract-) | Milan, Lombardy, Italy | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [AI Quality Evaluator - Spanish (12-month Contract)](https://jobs.smartrecruiters.com/Canva/6000000001409440-ai-quality-evaluator-spanish-12-month-contract-) | Madrid, MD, Spain | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [AI Video Lead - 12 Month FTC](https://jobs.smartrecruiters.com/Canva/6000000001340200-ai-video-lead-12-month-ftc) | Melbourne, VIC, Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [AI Video Lead - 12 Month FTC](https://jobs.smartrecruiters.com/Canva/6000000001340195-ai-video-lead-12-month-ftc) | Sydney, , Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Corporate FP&A Manager](https://jobs.smartrecruiters.com/Canva/6000000001252589-corporate-fp-a-manager) | San Francisco, , United States | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Dutch Language Manager (12 month contract)](https://jobs.smartrecruiters.com/Canva/6000000001262707-dutch-language-manager-12-month-contract-) | Amsterdam, NH, Netherlands | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Engineering Director - Core IT](https://jobs.smartrecruiters.com/Canva/6000000001357773-engineering-director-core-it) | Melbourne, VIC, Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Engineering Director - Core IT](https://jobs.smartrecruiters.com/Canva/6000000001357768-engineering-director-core-it) | Sydney, , Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Enterprise Support Specialist - EMEA (German speaking)](https://jobs.smartrecruiters.com/Canva/6000000001418520-enterprise-support-specialist-emea-german-speaking-) | London, , United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Growth Partnerships Manager, Startups (12 Month Fixed Term Contract)](https://jobs.smartrecruiters.com/Canva/6000000001377496-growth-partnerships-manager-startups-12-month-fixed-term-contract-) | San Francisco, , United States | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Head of LATAM](https://jobs.smartrecruiters.com/Canva/6000000001223065-head-of-latam) | São Paulo, SP, Brazil | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Head of LATAM](https://jobs.smartrecruiters.com/Canva/6000000001223060-head-of-latam) | Mexico City, CDMX, Mexico | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Head of Product Design - Growth](https://jobs.smartrecruiters.com/Canva/6000000001226913-head-of-product-design-growth) | Sydney, , Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Internal Coach (12-month Fixed Term Contract)](https://jobs.smartrecruiters.com/Canva/6000000001353323-internal-coach-12-month-fixed-term-contract-) | Makati, , Philippines | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Korean Language Manager (12-month contract)](https://jobs.smartrecruiters.com/Canva/6000000001320922-korean-language-manager-12-month-contract-) | Seoul, Seoul, Korea, republic of | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Mexico Language Manager](https://jobs.smartrecruiters.com/Canva/6000000001216243-mexico-language-manager) | Mexico City, CDMX, Mexico | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Mexico Product Localization Lead](https://jobs.smartrecruiters.com/Canva/6000000001258718-mexico-product-localization-lead) | Mexico, , Mexico | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Print Lead EMEA](https://jobs.smartrecruiters.com/Canva/6000000001375126-print-lead-emea) | London, , United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Product Localisation Lead - India](https://jobs.smartrecruiters.com/Canva/6000000001158387-product-localisation-lead-india) | Bengaluru, , India | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Production Engineering Manager](https://jobs.smartrecruiters.com/Canva/6000000001378726-production-engineering-manager) | Brisbane, QLD, Australia | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Production Engineering Manager](https://jobs.smartrecruiters.com/Canva/6000000001378702-production-engineering-manager) | Adelaide, SA, Australia | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Production Engineering Manager](https://jobs.smartrecruiters.com/Canva/6000000001378678-production-engineering-manager) | Melbourne, VIC, Australia | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Production Engineering Manager](https://jobs.smartrecruiters.com/Canva/6000000001378563-production-engineering-manager) | Sydney, NSW, Australia | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Senior Graphics and Illustration Specialist - 12 Month FTC](https://jobs.smartrecruiters.com/Canva/6000000001431626-senior-graphics-and-illustration-specialist-12-month-ftc) | Melbourne, VIC, Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Senior Graphics and Illustration Specialist - 12 Month FTC](https://jobs.smartrecruiters.com/Canva/6000000001431597-senior-graphics-and-illustration-specialist-12-month-ftc) | Sydney, , Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Senior Paid Search Manager](https://jobs.smartrecruiters.com/Canva/6000000001416860-senior-paid-search-manager) | Sydney, , Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Senior Performance Creative](https://jobs.smartrecruiters.com/Canva/6000000001362985-senior-performance-creative) | San Francisco, CA, United States | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Senior Performance Creative](https://jobs.smartrecruiters.com/Canva/6000000001362824-senior-performance-creative) | Sydney, , Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Canva | [Senior Production Engineering Manager](https://jobs.smartrecruiters.com/Canva/6000000001378655-senior-production-engineering-manager) | Adelaide, SA, Australia | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Senior Production Engineering Manager](https://jobs.smartrecruiters.com/Canva/6000000001378632-senior-production-engineering-manager) | Sydney, NSW, Australia | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Senior Production Engineering Manager](https://jobs.smartrecruiters.com/Canva/6000000001378609-senior-production-engineering-manager) | Melbourne, VIC, Australia | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Senior Production Engineering Manager](https://jobs.smartrecruiters.com/Canva/6000000001378586-senior-production-engineering-manager) | Brisbane, , Australia | no-keyword-match |  |  |
| UNCLASSIFIED | Canva | [Template Art Director (12-month contract) - Japan](https://jobs.smartrecruiters.com/Canva/6000000001417410-template-art-director-12-month-contract-japan-) | Tokyo, Tokyo, Japan | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Director, Business Systems](https://boards.greenhouse.io/figma/jobs/6019394004?gh_jid=6019394004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Director, Product Design - AI & Context](https://boards.greenhouse.io/figma/jobs/6201114004?gh_jid=6201114004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Director, Research - AI Evals](https://boards.greenhouse.io/figma/jobs/6112112004?gh_jid=6112112004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Director, Solutions Consulting](https://boards.greenhouse.io/figma/jobs/5820284004?gh_jid=5820284004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Enterprise Support Specialist, Korean Speaking (London, United Kingdom](https://boards.greenhouse.io/figma/jobs/6105678004?gh_jid=6105678004) | London, England | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, Distribution Partnerships](https://boards.greenhouse.io/figma/jobs/6118332004?gh_jid=6118332004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, HRIS](https://boards.greenhouse.io/figma/jobs/6132269004?gh_jid=6132269004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, Order Management](https://boards.greenhouse.io/figma/jobs/6206760004?gh_jid=6206760004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, Product Management - Roundtripping](https://boards.greenhouse.io/figma/jobs/6104919004?gh_jid=6104919004) | New York, NY • United States | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, Product Management - Roundtripping (London, United Kingdom)](https://boards.greenhouse.io/figma/jobs/6149007004?gh_jid=6149007004) | London, England | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, Software Engineering - AI Observability](https://boards.greenhouse.io/figma/jobs/5807963004?gh_jid=5807963004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, Software Engineering - Billing](https://boards.greenhouse.io/figma/jobs/5722244004?gh_jid=5722244004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, Software Engineering - DevEx AI Tools](https://boards.greenhouse.io/figma/jobs/6008752004?gh_jid=6008752004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, Software Engineering - Interaction Design](https://boards.greenhouse.io/figma/jobs/5778796004?gh_jid=5778796004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, Solutions Consulting (London, United Kingdom)](https://boards.greenhouse.io/figma/jobs/6111591004?gh_jid=6111591004) | London, England | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, Solutions Consulting (Tokyo, Japan)](https://boards.greenhouse.io/figma/jobs/6134908004?gh_jid=6134908004) | Tokyo, Japan | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Manager, Talent Products](https://boards.greenhouse.io/figma/jobs/6193623004?gh_jid=6193623004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Product Design Intern (2027)](https://boards.greenhouse.io/figma/jobs/6180005004?gh_jid=6180005004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Technical Quality Specialist](https://boards.greenhouse.io/figma/jobs/6111625004?gh_jid=6111625004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Figma | [Video Strategist](https://boards.greenhouse.io/figma/jobs/6204556004?gh_jid=6204556004) | San Francisco, CA • New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [AI Transformation Owner, CRO](https://job-boards.greenhouse.io/gitlab/jobs/8638232002) | Remote, United States | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [AI Transformation Owner, Product & Design](https://job-boards.greenhouse.io/gitlab/jobs/8716179002) | Remote, Canada; Remote, United K | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Associate Renewals Manager](https://job-boards.greenhouse.io/gitlab/jobs/8785825002) | Remote Ireland; Remote, Israel | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Candidate Experience Specialist, Contractor](https://job-boards.greenhouse.io/gitlab/jobs/8801523002) | Remote, United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Candidate Experience Specialist, Contractor](https://job-boards.greenhouse.io/gitlab/jobs/8782471002) | Remote, United States | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Chief of Staff, CRO](https://job-boards.greenhouse.io/gitlab/jobs/8700245002) | Remote, United States | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Director of Product Management, Agentic Software Delivery](https://job-boards.greenhouse.io/gitlab/jobs/8806017002) | Remote, United States | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Director, Strategic Partnerships](https://job-boards.greenhouse.io/gitlab/jobs/8615811002) | Remote, US | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Director, Support (Bengaluru)](https://job-boards.greenhouse.io/gitlab/jobs/8629019002) | Bangalore, India | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Engagement Manager - French Speaking](https://job-boards.greenhouse.io/gitlab/jobs/8809512002) | Remote, United Kingdom | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Engineering Manager](https://job-boards.greenhouse.io/gitlab/jobs/8799044002) | Bangalore, India | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Engineering Manager - Nonlinear Productivity (Friction Elimination & S](https://job-boards.greenhouse.io/gitlab/jobs/8632388002) | Bangalore, India | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Engineering Manager, Agent Foundations: Agent Execution](https://job-boards.greenhouse.io/gitlab/jobs/8759592002) | Remote, United States | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Engineering Manager, Build](https://job-boards.greenhouse.io/gitlab/jobs/8586667002) | Remote, United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Engineering Manager, Data Foundations](https://job-boards.greenhouse.io/gitlab/jobs/8592950002) | Remote, US | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Engineering Manager, Dedicated Integrations](https://job-boards.greenhouse.io/gitlab/jobs/8636648002) | Remote, United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Engineering Manager, Dedicated Integrations Team](https://job-boards.greenhouse.io/gitlab/jobs/8725225002) | Bangalore, India | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Engineering Manager, Switchboard](https://job-boards.greenhouse.io/gitlab/jobs/8586632002) | Remote, United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Engineering Manager, Tenant Scale:Git](https://job-boards.greenhouse.io/gitlab/jobs/8617538002) | Remote, Canada; Remote, United K | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Engineering Manager, Trusted Agentic Development](https://job-boards.greenhouse.io/gitlab/jobs/8782040002) | Remote, Poland | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Field CTO, Public Sector](https://job-boards.greenhouse.io/gitlab/jobs/8792585002) | Remote, United States | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Lead Pricing Strategist](https://job-boards.greenhouse.io/gitlab/jobs/8756163002) | Remote, Canada; Remote, United S | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Manager, Solutions Architects - San Francisco](https://job-boards.greenhouse.io/gitlab/jobs/8396674002) | Remote, US | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Manager, Solutions Architecture - East](https://job-boards.greenhouse.io/gitlab/jobs/8641849002) | Remote, United States | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Public Sector Enablement Lead](https://job-boards.greenhouse.io/gitlab/jobs/8814596002) | Remote, United States |  |  |  |
| UNCLASSIFIED | GitLab | [Senior Engagement Manager - Germany](https://job-boards.greenhouse.io/gitlab/jobs/8725981002) | Remote, Germany | no-keyword-match |  |  |
| UNCLASSIFIED | GitLab | [Senior Executive Business Partner, CFO](https://job-boards.greenhouse.io/gitlab/jobs/8790705002) | Remote; Remote, United States | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | GitLab | [Senior Manager, Public Sector Renewals](https://job-boards.greenhouse.io/gitlab/jobs/8820804002) | Remote, United States | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | HubSpot | [Contract Manager, 1:Few - US Accounts](https://www.hubspot.com/careers/jobs/7668971?gh_jid=7668971) | Remote - Colombia | no-keyword-match |  |  |
| UNCLASSIFIED | HubSpot | [Deal Lead, Corporate Development](https://www.hubspot.com/careers/jobs/7453082?gh_jid=7453082) | Remote - USA | no-keyword-match |  |  |
| UNCLASSIFIED | HubSpot | [German Customer Support Specialist](https://www.hubspot.com/careers/jobs/5097150?gh_jid=5097150) | Remote - Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | HubSpot | [German Customer Support Specialist](https://www.hubspot.com/careers/jobs/5094673?gh_jid=5094673) | Dublin, Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | HubSpot | [Inbound Success Coach](https://www.hubspot.com/careers/jobs/8098031?gh_jid=8098031) | Sydney, Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | HubSpot | [LATAM Inbound Success Coach 2026 - Spanish (P)](https://www.hubspot.com/careers/jobs/8112791?gh_jid=8112791) | Bogotá, Colombia | no-keyword-match |  |  |
| UNCLASSIFIED | HubSpot | [Lead Marketer, AI Usage Automation](https://www.hubspot.com/careers/jobs/8214455?gh_jid=8214455) | Remote - United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | HubSpot | [Lead Marketer, AI Usage Automation](https://www.hubspot.com/careers/jobs/8201644?gh_jid=8201644) | Remote - Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | HubSpot | [Lead Marketer, AI Usage Automation](https://www.hubspot.com/careers/jobs/8164700?gh_jid=8164700) | Remote - USA | no-keyword-match |  |  |
| UNCLASSIFIED | HubSpot | [Renewal Specialist](https://www.hubspot.com/careers/jobs/8081933?gh_jid=8081933) | Sydney, Australia | no-keyword-match |  |  |
| UNCLASSIFIED | HubSpot | [Senior Engineering Manager](https://www.hubspot.com/careers/jobs/7906651?gh_jid=7906651) | Remote - USA | no-keyword-match |  |  |
| UNCLASSIFIED | HubSpot | [Senior Growth Partner Development Manager (PDM)](https://www.hubspot.com/careers/jobs/8118884?gh_jid=8118884) | Tokyo, Japan | no-keyword-match |  |  |
| UNCLASSIFIED | HubSpot | [Small Business Growth Specialist - DACH](https://www.hubspot.com/careers/jobs/5986980?gh_jid=5986980) | Berlin, Germany | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | HubSpot | [Strategic Partner Development Manager](https://www.hubspot.com/careers/jobs/8060201?gh_jid=8060201) | Cambridge, MA, USA | no-keyword-match |  |  |
| UNCLASSIFIED | Jasper AI | [Senior GRC Lead](https://jobs.ashbyhq.com/Jasper%20AI/d86a7821-b768-4f11-b540-3ee0fbc94c96) | United States | no-keyword-match |  |  |
| UNCLASSIFIED | Miro | [Accounts Payable Manager](https://miro.com/careers/vacancy/8640328002?gh_jid=8640328002) | Amsterdam, NL; Austin, US; Londo | no-keyword-match |  |  |
| UNCLASSIFIED | Miro | [Expression of Interest: Enterprise & Strategic AE - UK/I](https://miro.com/careers/vacancy/8611580002?gh_jid=8611580002) | London, UK | no-keyword-match |  |  |
| UNCLASSIFIED | Miro | [Head of CS, DACH](https://miro.com/careers/vacancy/8759046002?gh_jid=8759046002) | Munich, DE | no-keyword-match |  |  |
| UNCLASSIFIED | Miro | [Manager, Customer Support AMER](https://miro.com/careers/vacancy/8700629002?gh_jid=8700629002) | Austin, US | no-keyword-match |  |  |
| UNCLASSIFIED | Miro | [Principal, Field Excellence](https://miro.com/careers/vacancy/8736729002?gh_jid=8736729002) | Amsterdam, NL; London, UK | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Demand & Campaigns Lead, EMEA](https://jobs.ashbyhq.com/notion/edb12109-aa32-461a-b764-1850a2314e0d) | Dublin, Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Engineering Manager, Mobile AI](https://jobs.ashbyhq.com/notion/3979a6f5-2abb-447b-bd3a-0565b06bae24) | New York, New York | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Field Marketer](https://jobs.ashbyhq.com/notion/42279d85-cf60-4c3c-bf82-92b9e215f3c7) | San Francisco, California · New  | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [General Manager, DACH](https://jobs.ashbyhq.com/notion/951a7b72-4cb3-4726-be5e-5359269d4929) | Munich, Germany | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [General Manager, France](https://jobs.ashbyhq.com/notion/42702b6a-b4a6-47ac-add0-07b435a8be38) | Paris, France | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Head of Demand Engine](https://jobs.ashbyhq.com/notion/adb34b7e-89f3-4365-9f8f-4c98d50cc0fd) | San Francisco, California · New  | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Manager, Enterprise Outcome Architects](https://jobs.ashbyhq.com/notion/fed962b2-338d-4ee0-a076-904742c245a0) | San Francisco, California · New  | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Manager, Solutions Consultants, DACH](https://jobs.ashbyhq.com/notion/6140e48c-949d-48a8-a3f0-c826199040fe) | Munich, Germany | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Manager, Solutions Consultants, France](https://jobs.ashbyhq.com/notion/77af0faa-8f69-4dc5-baa6-6e253823bccb) | Paris, France | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Manager, Solutions Consultants, UKI](https://jobs.ashbyhq.com/notion/2f7589e1-b08d-49b1-83aa-2ea2454550db) | London, United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Product Support Manager](https://jobs.ashbyhq.com/notion/3339493a-ee21-49f3-ab09-e1f8ba8f1b92) | Hyderabad, India | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Senior Treasury Manager](https://jobs.ashbyhq.com/notion/6f5d0bc7-dd9e-48fd-9a1d-733ad391e151) | San Francisco, California · New  | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Startup Market Lead, AMER](https://jobs.ashbyhq.com/notion/3129e7bd-f717-47d3-9fdd-c4df026bbf20) | San Francisco, California · New  | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Notion | [Startup Program & Experience Lead](https://jobs.ashbyhq.com/notion/c35370d3-ac9c-4ad7-947b-77ad6e9e176c) | San Francisco, California · New  | no-keyword-match |  |  |
| UNCLASSIFIED | Notion | [Talent Management](https://jobs.ashbyhq.com/notion/9a4b059a-f42b-438e-8098-9acda96825bf) | San Francisco, California | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [AWS Specialist Seller, Strategic Pursuits](https://jobs.ashbyhq.com/openai/c44a22a3-6d6f-41f3-bd54-3379034f3e59) | San Francisco · Seattle | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [AWS Specialist Sellers, Strategic Pursuits](https://jobs.ashbyhq.com/openai/51f1d6a0-2e53-4554-8abe-a100da87978b) | London, UK · Munich, Germany | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Abuse Investigator - Scams & Fraud](https://jobs.ashbyhq.com/openai/7512a020-2f3c-4f19-921d-b76edaeba5d3) | US - Remote · New York City · Wa | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Associate - EMEA](https://jobs.ashbyhq.com/openai/d29b455a-9fee-4610-8e08-ce6a9ea8a37e) | Dublin, Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Associate - EMEA (German Speaking)](https://jobs.ashbyhq.com/openai/6c88bfaa-7f1b-4175-82f1-6d484a516ca8) | Dublin, Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Associate - SF](https://jobs.ashbyhq.com/openai/55f36629-8351-41d9-b2f5-3d63c5e26bf7) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Associate - Singapore (ANZ Market)](https://jobs.ashbyhq.com/openai/d9696b77-5b11-49c5-8d0b-b1826bb6115c) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Associate - Singapore (Korean-speaking)](https://jobs.ashbyhq.com/openai/974fff14-f2d7-4a99-8740-eb8dc5300d82) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Associate, Japan](https://jobs.ashbyhq.com/openai/2f3f416d-cc2a-4836-bcff-daee80c94e95) | Tokyo, Japan | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Associate- EMEA (French Speaking)](https://jobs.ashbyhq.com/openai/1eb6ef0f-0e51-46d3-b888-c1a4c22c190a) | Dublin, Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Digital Native](https://jobs.ashbyhq.com/openai/52263a22-1621-4dbb-9a11-ae4490f2acc8) | Seoul, South Korea | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Digital Native Enterprise](https://jobs.ashbyhq.com/openai/fbb68247-eb54-4ad1-94b4-26e0dc24fd23) | San Francisco · New York City ·  | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Digital Native Large Enterprise](https://jobs.ashbyhq.com/openai/673ca4f5-b5dc-448f-be3c-4f888a6d13ed) | San Francisco · Seattle · US - R | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Digital Native New Business](https://jobs.ashbyhq.com/openai/07fb9365-8e80-48fe-86df-08d60dd46f43) | San Francisco · New York City ·  | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Digital Natives](https://jobs.ashbyhq.com/openai/d085d2ec-0256-4ecf-b493-81ea34942e51) | Delhi, India · Mumbai, India | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Digital Natives](https://jobs.ashbyhq.com/openai/b65d4fb6-1624-4518-bf94-e57ddaa35193) | Tokyo, Japan | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Digital Natives](https://jobs.ashbyhq.com/openai/6245809c-5646-4226-9f20-7bc88a4135aa) | Sydney, Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Digital Natives - France](https://jobs.ashbyhq.com/openai/f5c3b504-3982-4d67-99ba-315b9e14f196) | Paris, France | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Digital Natives - Nordics](https://jobs.ashbyhq.com/openai/4e51e1ac-3fe0-46b5-b036-6143826ecfa5) | Stockholm, Sweden | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Digital Natives Growth](https://jobs.ashbyhq.com/openai/f4467078-033c-4638-ac7e-69a532276d85) | San Francisco | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Digital Natives / MENA](https://jobs.ashbyhq.com/openai/2d91e925-7d2d-4a7d-b824-70678ce9453e) | Abu Dhabi, UAE | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, FSI - Japan](https://jobs.ashbyhq.com/openai/570df8ac-dacb-4686-b59c-ef48eed0580c) | Tokyo, Japan | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Healthcare](https://jobs.ashbyhq.com/openai/93d9be71-6502-4e48-94c2-1c17724e2bc7) | San Francisco · New York City ·  | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Higher Education](https://jobs.ashbyhq.com/openai/dceee17e-1e37-448b-acd3-2f97e41a6af7) | San Francisco · New York City ·  |  |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Insurance](https://jobs.ashbyhq.com/openai/24ade569-b2eb-4879-b6d3-82407ac0efe7) | New York City | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Large Enterprise](https://jobs.ashbyhq.com/openai/25920df6-571d-4e05-aa12-384453f406f8) | Seoul, South Korea | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Large Enterprise](https://jobs.ashbyhq.com/openai/ea738090-a7e0-41bd-b619-afeff9fd18e0) | Munich, Germany · Berlin, German | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Large Enterprise](https://jobs.ashbyhq.com/openai/88a57561-561b-4a14-bc43-78bc7f144164) | London, UK | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Large Enterprise](https://jobs.ashbyhq.com/openai/eb4e4757-94b6-4c7d-a3ba-35fad40c0859) | Delhi, India · India - Remote | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Large Enterprise](https://jobs.ashbyhq.com/openai/8c95db0d-982e-43cf-95e4-e30cb09e6c9c) | San Francisco · New York City ·  | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Large Enterprise (FSI)](https://jobs.ashbyhq.com/openai/10208545-58dd-4cdb-91e1-69b1c2cabe3c) | Singapore | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Large Enterprise - Tokyo](https://jobs.ashbyhq.com/openai/18f58952-c242-4562-8732-073a0ae8029e) | Tokyo, Japan | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Life Sciences](https://jobs.ashbyhq.com/openai/0b32c370-a2bb-4784-a326-67dfbb130ef5) | San Francisco · New York City | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Mid-Market](https://jobs.ashbyhq.com/openai/8a3fdf98-ad82-4082-ace0-9edb89bc8f6d) | Singapore | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Mid-Market](https://jobs.ashbyhq.com/openai/71f97dd6-63bc-4f86-8c34-dcb71577069a) | Sydney, Australia | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Mid-Market](https://jobs.ashbyhq.com/openai/fa312d19-bb9e-4569-b5ed-aed8aa45cd3b) | India - Remote · Mumbai, India · | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Public Sector - Tokyo](https://jobs.ashbyhq.com/openai/e6050096-9dcc-4054-8f3c-02af8b5bcbeb) | Tokyo, Japan | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Startups](https://jobs.ashbyhq.com/openai/0b428c6d-7c06-4feb-82b6-5bbe5cda2a18) | São Paulo | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Startups](https://jobs.ashbyhq.com/openai/9c5161d9-6b13-4a88-b8b9-f17857965897) | Stockholm, Sweden | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Startups (Mandarin-Speaking)](https://jobs.ashbyhq.com/openai/ac0922d9-4731-40a1-b8a3-17b912e1a13b) | Singapore | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Startups Expansion](https://jobs.ashbyhq.com/openai/72c497c3-0350-42d6-b538-abd9e9af9041) | San Francisco | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Account Director, Startups / Tokyo](https://jobs.ashbyhq.com/openai/32905f5c-9405-4073-bc65-c57fcf55a83d) | Tokyo, Japan | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Agency Partner, Ads Solutions](https://jobs.ashbyhq.com/openai/12f6b6ef-be98-4159-9aef-7baac78489bc) | New York City | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Agent Standards Specialist, Global Affairs](https://jobs.ashbyhq.com/openai/80f0deef-7c66-4545-91eb-f43a1481f997) | Washington, DC · New York City | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Applied Risk Standards Specialist](https://jobs.ashbyhq.com/openai/74b9aa04-0b9d-459a-9e2d-0e43fae67a79) | San Francisco · Washington, DC | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [B2B Comms Lead, EMEA](https://jobs.ashbyhq.com/openai/e0deb489-89f3-4de4-9bd8-67107b88653b) | Dublin, Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Business Lead, Special Situations](https://jobs.ashbyhq.com/openai/d8915225-1d6b-4de5-96e3-e8e8511f1288) | San Francisco · New York City | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Business Systems Lead, Procure-to-Pay](https://jobs.ashbyhq.com/openai/c0e1f65b-4731-48b3-ac60-93a269266494) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Client Partner, Ads Solutions](https://jobs.ashbyhq.com/openai/bf9d9e1c-7967-41a4-a7ae-0bf9b6a768c2) | San Francisco · New York City | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Client Partner, Ads Solutions (Spanish Speaking)](https://jobs.ashbyhq.com/openai/bb1c9e6f-892e-434b-9f02-fcf6a238bc1c) | Dublin, Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Client Partner, Ads Solutions - Travel](https://jobs.ashbyhq.com/openai/6742bd76-dcc7-4bbd-bdb3-00c315bc0254) | San Francisco · New York City | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Corporate Development, Deal Lead](https://jobs.ashbyhq.com/openai/4030aec5-ffd4-49a7-bc19-65e63c45e167) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Customer Learning Program Lead](https://jobs.ashbyhq.com/openai/644bf871-a584-49e2-8545-240313d9c8b9) | San Francisco | only 2 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Deal Lead, Special Situations](https://jobs.ashbyhq.com/openai/f16eaf44-208f-4374-b576-f033ed6e5eed) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Deal Lead, Special Situations (Semiconductors)](https://jobs.ashbyhq.com/openai/875b6559-55f0-4cea-ad62-0063d0cb0b73) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Dedicated Support Engineering Lead](https://jobs.ashbyhq.com/openai/deacd43e-9c1b-467c-96e2-11f4f6bdb139) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Demo Studio Lead](https://jobs.ashbyhq.com/openai/a452882b-bb56-4a99-83e6-b8b5d21db3ee) | San Francisco · New York City | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Development Lead](https://jobs.ashbyhq.com/openai/987c4eb8-819e-4258-a91c-f34ecfbcd5f1) | US - Remote | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Development Planner, Industrial Compute](https://jobs.ashbyhq.com/openai/5a647e2b-5d6c-4c71-aeea-b16e3fda4b3f) | US - Remote | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Economic Development Lead](https://jobs.ashbyhq.com/openai/ba803f51-53d8-44b8-8bb7-b79f21d6a4c8) | US - Remote | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Electrical Commissioning Lead](https://jobs.ashbyhq.com/openai/4d0b1eb5-ea5d-460b-8fe6-23c45b0703f5) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Enablement Lead - Knowledge Work](https://jobs.ashbyhq.com/openai/78a49da9-b768-427e-ad01-3e61d80cfea8) | Dublin, Ireland |  |  |  |
| UNCLASSIFIED | OpenAI | [Energy Regulatory Lead](https://jobs.ashbyhq.com/openai/c5dd153c-8506-4d12-8e50-d09d525759fe) | US - Remote | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Engineering Manager, Artifacts](https://jobs.ashbyhq.com/openai/d9b730a4-ee24-4d18-bb46-d8111591c6d2) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Engineering Manager, Cooperative Systems](https://jobs.ashbyhq.com/openai/817c523c-59b2-4206-ae52-7dd6d36090b4) | Seattle | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Engineering Manager, Cooperative Systems](https://jobs.ashbyhq.com/openai/241154df-ab1a-4dfa-8b18-66e087d1e636) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Engineering Manager, Core Experimentation](https://jobs.ashbyhq.com/openai/eda0d516-94bd-4257-9679-aded0d709fba) | Seattle | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Engineering Manager, Core Services](https://jobs.ashbyhq.com/openai/ebc65e7d-d86a-4066-aa82-3a7758d97bb6) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Engineering Manager, Library](https://jobs.ashbyhq.com/openai/b2fb6fa4-07a9-4d8d-adf5-bff18a5e6033) | Seattle | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Engineering Manager, Model Flywheel](https://jobs.ashbyhq.com/openai/37ee9010-079f-4932-9fc9-45cd9372b6dd) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Engineering Manager, Multimodal (API)](https://jobs.ashbyhq.com/openai/1d7f4747-54a3-4141-a39a-c6e7700e969b) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Engineering Manager, Online Data Systems](https://jobs.ashbyhq.com/openai/cb050c48-2e42-4dc0-8860-e6b3e5e6baff) | San Francisco · Mountain View | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Engineering Manager, Rosalind Workbench](https://jobs.ashbyhq.com/openai/4ca2e49f-83bb-4276-be17-d85a9a0c58e9) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Executive Business Partner, India](https://jobs.ashbyhq.com/openai/7a84a4ec-897e-4bd2-a44e-dd148f5d138d) | Mumbai, India | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Executive Programs Lead, Americas](https://jobs.ashbyhq.com/openai/c6b7bcc8-5454-4e6e-844f-c6a55607309a) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Field CTO](https://jobs.ashbyhq.com/openai/23239cae-2a91-4985-94d1-a2acbb3ffa25) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Full-Stack SWE, Data Acquisition (Foundations)](https://jobs.ashbyhq.com/openai/a886ff48-b8a1-4e28-b468-296713a5ad78) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Global Account Director, International Organisations, ME & LATAM](https://jobs.ashbyhq.com/openai/9745f423-9048-48c0-8c57-639611b04abc) | London, UK | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Global Mobility Manager, Strategic Initiatives](https://jobs.ashbyhq.com/openai/002c6146-f1bf-4653-8929-8112b577837b) | San Francisco · New York City ·  | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Global Transportation Programs, Senior Manager](https://jobs.ashbyhq.com/openai/7d87459c-6085-4479-8e77-9255e6dd8329) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Growth - Lifecycle Lead](https://jobs.ashbyhq.com/openai/ef84553e-e02b-4904-a348-710ea8e37346) | San Francisco · New York City | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Growth - Lifecycle Lead (B2B)](https://jobs.ashbyhq.com/openai/effa8b95-3b2d-4f57-8fcd-b3c9b3c142ba) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [HRBP, Consumer Devices](https://jobs.ashbyhq.com/openai/000cf0f2-090d-40c6-b9f8-1699db9a4c68) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Hardware Exploratory](https://jobs.ashbyhq.com/openai/565c001b-c164-477a-88a9-ce81e5e5480d) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Hardware Strategic Sourcing & Manufacturing Partnerships Manager](https://jobs.ashbyhq.com/openai/79432fa9-49c0-4ba0-b2a1-9d589ddc1861) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Hardware Strategic Sourcing Manager, Optics](https://jobs.ashbyhq.com/openai/23014bc8-37d4-4fd9-9a77-d95fdd33437f) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Hardware Systems Planning Lead (1P)](https://jobs.ashbyhq.com/openai/d97380fa-d935-43ec-ad4f-6a7f810b21f2) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Head of Employee Tech & Experience (ETX)](https://jobs.ashbyhq.com/openai/4aa1dcbf-166a-4538-ae4e-08cf39c7ff23) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Head of Marketplace](https://jobs.ashbyhq.com/openai/1aa89889-9323-44eb-a3fb-042c68c45252) | San Francisco · New York City | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Head of Partnerships, Digital Natives](https://jobs.ashbyhq.com/openai/c717b98e-5394-4ad1-ae3f-e036717ad9b5) | San Francisco · New York City | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Head of Sourcing Enablement & Delivery](https://jobs.ashbyhq.com/openai/0681fa01-76c2-47da-9ebd-b4677521e049) | San Francisco |  |  |  |
| UNCLASSIFIED | OpenAI | [Head of Treasury Markets](https://jobs.ashbyhq.com/openai/341561ae-9892-4ba1-9ffb-faafff4f0fb2) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [ISV Partnerships Lead](https://jobs.ashbyhq.com/openai/cd3f8166-9f07-4d1b-944d-a4a6593a196a) | San Francisco · New York City | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [IT Support Dublin, EMEA Regional Lead](https://jobs.ashbyhq.com/openai/8c460221-77ba-4120-b74e-3b1ad7c82818) | Dublin, Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [IT Support Specialist](https://jobs.ashbyhq.com/openai/49ae54dc-3d33-4107-8112-63fac1ee86ca) | Seattle | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Industrial Compute](https://jobs.ashbyhq.com/openai/6d7ece77-bf25-4f5e-9a84-c5ce26e18c37) | US - Remote | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Land Development & Due Diligence Lead](https://jobs.ashbyhq.com/openai/1f247dd3-5c54-49a7-83f5-ca6cf6ed7717) | US - Remote | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Lead, Ads Prospecting & Customer Intelligence](https://jobs.ashbyhq.com/openai/fa5114ae-c6ff-4bbd-9e21-5dcfafd032f7) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Manager, Global Equity Administration](https://jobs.ashbyhq.com/openai/498e0afe-376b-470f-b8c8-9a56a46effa8) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Manager, Senior Support Engineering](https://jobs.ashbyhq.com/openai/36c8356d-b7eb-4aef-b0f5-3a3f3f8dfc5a) | Dublin, Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Market Research Lead](https://jobs.ashbyhq.com/openai/f4cacc93-288b-425f-8bc2-5310d3f12d53) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Mechanical Commissioning Lead](https://jobs.ashbyhq.com/openai/0f58ac8e-6dd2-400d-9c34-29c62b7804b5) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Order Management & Billing Lead — Cloud Marketplaces & Partnerships](https://jobs.ashbyhq.com/openai/1e28e1f0-2580-46d9-b5ba-55c77d706f81) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Partner Director - AWS Alliance Partnership, Japan](https://jobs.ashbyhq.com/openai/9ea666f7-9b16-481f-a16d-f533d45ca795) | Tokyo, Japan | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Partner Director, ANZ](https://jobs.ashbyhq.com/openai/9f586619-7190-4b91-9002-d3826eaed72f) | Sydney, Australia | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Partner Director, HCL, Wipro & Cognizant](https://jobs.ashbyhq.com/openai/a51b521c-d3bf-4653-99c6-c9152827cfb8) | San Francisco · Seattle | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Partner Director, Korea](https://jobs.ashbyhq.com/openai/ea647f38-5af4-4767-8268-608059af4095) | Seoul, South Korea | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Partner Director, McKinsey Alliance](https://jobs.ashbyhq.com/openai/28c96920-a412-47c0-88f8-342790d779ff) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Partner Director, PwC](https://jobs.ashbyhq.com/openai/90cf64cc-4276-433f-bdf0-7cf69309bbd2) | San Francisco · New York City ·  | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Partner Director, Tokyo](https://jobs.ashbyhq.com/openai/cbcc7df1-3e5a-475c-a5ff-6582757d097a) | Tokyo, Japan | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Partnerships, Life Sciences](https://jobs.ashbyhq.com/openai/7aee5d38-6543-4fd7-b110-8cdb609c5c9e) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Performance Modeling Lead](https://jobs.ashbyhq.com/openai/f2293c9f-d036-4198-a268-3dad738c8d19) | San Francisco · Seattle | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Power Trading Lead](https://jobs.ashbyhq.com/openai/6e20368e-d51e-4562-8b94-0166317d52c7) | US - Remote | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Pricing Strategist](https://jobs.ashbyhq.com/openai/3ab0541b-160b-49c0-8609-574db6358332) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Product Engineering Business Lead](https://jobs.ashbyhq.com/openai/8dcf85ee-563d-40de-bc78-cf829404d212) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [RE / RS - Foundations, Search](https://jobs.ashbyhq.com/openai/020b2aae-8be0-408c-ab49-20eefa8541af) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [RE/RS, Data Understanding (MM)](https://jobs.ashbyhq.com/openai/d5331989-2a73-446c-be86-ca5379f27563) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [RE/RS, Data Understanding - Foundations](https://jobs.ashbyhq.com/openai/f9731ef2-9b8a-49ec-95ca-ecef35fa996a) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [RE/RS, Data Understanding - Foundations](https://jobs.ashbyhq.com/openai/5d1a6c05-e18b-43a2-8808-6498929ac253) | Zurich, Switzerland | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Red Team Specialist - Cyber](https://jobs.ashbyhq.com/openai/badafdf8-116b-4849-b848-2f20a3ff2732) | San Francisco · Seattle · Washin | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Regional Client Partner, Ads Solutions](https://jobs.ashbyhq.com/openai/b1d19dac-065d-42d3-9f2c-97cc3fe73cdf) | Paris, France | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Regional Client Partner, Ads Solutions (Mumbai)](https://jobs.ashbyhq.com/openai/a1b4bfdf-673a-4ac4-a459-70118caabc09) | Mumbai, India | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Regional Manager, Ads Solutions (APAC)](https://jobs.ashbyhq.com/openai/6d8b5a16-633c-42ea-8253-f1ca57b632a6) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Scaled Programs Lead, SMB Ads](https://jobs.ashbyhq.com/openai/e36955a7-403d-41e4-b54e-37edc7039173) | San Francisco · New York City | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [Senior Employee Relations Partner](https://jobs.ashbyhq.com/openai/212ea50e-b315-4aef-ba03-5552e66b3129) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Senior Lifecycle Strategist](https://jobs.ashbyhq.com/openai/19e39227-f105-48fa-85d2-59814d4537ed) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Senior Manager, EHS - Robotics](https://jobs.ashbyhq.com/openai/099374c6-3cbb-4964-9a1d-31e6e5b5dcd2) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Senior Manager, Extended Workforce Program](https://jobs.ashbyhq.com/openai/194a69ed-d7a2-4af8-9bec-67a4b7b58451) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Senior Manager, Global Equity Administration](https://jobs.ashbyhq.com/openai/3480c407-cb27-45c9-ad4e-d132ea62b389) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Senior Manager, Order to Cash — AI Products & Cloud Partnerships](https://jobs.ashbyhq.com/openai/103d7043-28ec-4639-9c8d-0910083a1755) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Senior Support Specialist, Ads](https://jobs.ashbyhq.com/openai/f21b387c-617b-4473-9e84-2fbfa89c27a9) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Senior Support Specialist, Ads](https://jobs.ashbyhq.com/openai/215ea33c-47db-4604-910c-3de52ebeb0a6) | Ontario - Remote | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Site Selection Lead](https://jobs.ashbyhq.com/openai/98f65aa5-0f19-4942-9296-63382883dc55) | San Francisco · Seattle | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [South America Lead, Global Affairs (Sao Paulo)](https://jobs.ashbyhq.com/openai/dc5a7877-5bc3-4366-90d4-8370cc11d44e) | São Paulo | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Strategic Experiences Lead, Executive Programs](https://jobs.ashbyhq.com/openai/fa431b48-8f59-4429-85d7-31b84ed2c116) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Strategic Partnerships Manager, France](https://jobs.ashbyhq.com/openai/bd4cdb4e-ecd7-45d6-8cab-0e9fa155104e) | Paris, France | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Strategic Partnerships Manager, Germany](https://jobs.ashbyhq.com/openai/0cf4a8f4-a57a-494b-aad8-4df8ac096939) | Munich, Germany | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Strategic Pursuits Lead](https://jobs.ashbyhq.com/openai/1dc6d2b7-e89f-4d76-8b26-c085b6f4d827) | San Francisco · Seattle | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Strategic Technology Negotiations Lead](https://jobs.ashbyhq.com/openai/5c579ec6-be3a-409b-8ae4-9e3f46af8288) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Subject Matter Expert, Investment Banking](https://jobs.ashbyhq.com/openai/4705a853-46e6-4f91-884c-61e54de91b0e) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Support Delivery Lead](https://jobs.ashbyhq.com/openai/2e645639-3362-42f7-b0b9-e99380c48d29) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Support Delivery Lead](https://jobs.ashbyhq.com/openai/76583c87-78ea-4886-906d-81b0a9c05bfe) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Support Delivery Lead - Toronto](https://jobs.ashbyhq.com/openai/6b8eed3a-d549-4df8-9ac7-134d4d52c600) | Ontario - Remote | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Support Delivery Lead, Ads](https://jobs.ashbyhq.com/openai/0875c19f-3f37-403e-81e9-7bf2429f1e4e) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Support Delivery Lead, EMEA - Dublin](https://jobs.ashbyhq.com/openai/eeaf655b-9460-4e4e-b611-f0caf784c0b1) | Dublin, Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Support Vendor Manager](https://jobs.ashbyhq.com/openai/d4084bb6-f9fa-46df-87ef-da6caed88455) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Systems Integration Manager / Consumer Devices](https://jobs.ashbyhq.com/openai/831960f4-a877-4c41-8fda-17fd321c0230) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Tech Lead Manager, Education](https://jobs.ashbyhq.com/openai/6922ab5c-5b90-4da2-ab10-cbc46d4f4860) | San Francisco |  |  |  |
| UNCLASSIFIED | OpenAI | [Technical Commodity Manager - Robotics](https://jobs.ashbyhq.com/openai/467da204-cd62-4e2d-ad7a-f3138f4f283b) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [Technical Threat Investigator, Threat Intel Engineering](https://jobs.ashbyhq.com/openai/f01b7084-a68d-4e30-ace9-6b5e6d90c517) | San Francisco · New York City ·  | no-keyword-match |  |  |
| UNCLASSIFIED | OpenAI | [US External Affairs Associate, Global Affairs](https://jobs.ashbyhq.com/openai/544af761-e37a-450c-884b-b96506c1b883) | Washington, DC | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | OpenAI | [VC Partnerships Manager](https://jobs.ashbyhq.com/openai/83ac3381-99c0-46a0-897c-abcd8699b466) | San Francisco | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Replit | [Cohort 0](https://jobs.ashbyhq.com/replit/2c147ccb-2557-40f8-aab9-64422cef220c) | Foster City, CA | no-keyword-match |  |  |
| UNCLASSIFIED | Replit | [Director of Product Design](https://jobs.ashbyhq.com/replit/b386f0ef-41e1-48e4-abe3-d35ce627de95) | Foster City, CA | no-keyword-match |  |  |
| UNCLASSIFIED | Replit | [Engineering Manager, Site Reliability Engineering](https://jobs.ashbyhq.com/replit/226d0562-2420-4991-ac18-23c827ed119c) | Foster City, CA | no-keyword-match |  |  |
| UNCLASSIFIED | Replit | [Partnerships Lead, GSIs](https://jobs.ashbyhq.com/replit/e673256c-7701-4b97-b7f4-800b68f03f84) | Foster City, CA | no-keyword-match |  |  |
| UNCLASSIFIED | Replit | [Product Partnerships Manager, Consumer/SMB](https://jobs.ashbyhq.com/replit/56d7dc53-f4ba-4147-9aaa-0fd4af7cbb4f) | Foster City, CA | no-keyword-match |  |  |
| UNCLASSIFIED | Replit | [Senior AI Builder](https://jobs.ashbyhq.com/replit/b333118f-965a-4d94-9557-88aa76779e9a) | Foster City, CA | no-keyword-match |  |  |
| UNCLASSIFIED | Replit | [Senior/Media Manager](https://jobs.ashbyhq.com/replit/4a995918-8f3c-4090-a076-01a04b88dabb) | Foster City, CA | no-keyword-match |  |  |
| UNCLASSIFIED | Replit | [Support Systems Lead (Foster City)](https://jobs.ashbyhq.com/replit/10789e06-f7d1-4619-93aa-1879f84e948e) | Foster City, CA | no-keyword-match |  |  |
| UNCLASSIFIED | Replit | [Support Systems Lead (NYC)](https://jobs.ashbyhq.com/replit/c1a83620-c70f-471b-bd52-9dd19f1a7c09) | NYC (SoHo) | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [ARG Engineering Manager](https://stripe.com/jobs/search?gh_jid=8113337) | US - Remote | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Abuse Investigator](https://stripe.com/jobs/search?gh_jid=8172508) | Dublin | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Abuse Investigator](https://stripe.com/jobs/search?gh_jid=8172487) | Dublin | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Abuse Investigator](https://stripe.com/jobs/search?gh_jid=8172510) | Seattle, San Francisco, New York | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Accounts Receivable Manager](https://stripe.com/jobs/search?gh_jid=7118945) | Bengaluru | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Administrative Business Partner](https://stripe.com/jobs/search?gh_jid=8081673) | SF | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Administrative Business Partner](https://stripe.com/jobs/search?gh_jid=8209652) | Chicago | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Administrative Coordinator](https://stripe.com/jobs/search?gh_jid=8223719) | Mexico City | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Business Value Consultant](https://stripe.com/jobs/search?gh_jid=8097051) | Chicago, New York, San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Capital Markets Investments](https://stripe.com/jobs/search?gh_jid=8164481) | New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Capital Markets, FX Specialist](https://stripe.com/jobs/search?gh_jid=8206733) | New York | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Comms, Public Goods](https://stripe.com/jobs/search?gh_jid=8114272) | San Francisco  | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Communities Partner Development Manager, SaaS Platforms](https://stripe.com/jobs/search?gh_jid=8138000) | US-Remote | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Communities Partner Development Manager, SaaS Platforms](https://stripe.com/jobs/search?gh_jid=8103952) | US-Remote | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Corporate Development M&A Integration Manager](https://stripe.com/jobs/search?gh_jid=8065818) | SF, NYC | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Creative Director, Copy & Campaigns](https://stripe.com/jobs/search?gh_jid=8001341) | US | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Customer Funds Reconciliation Manager, Luxembourg](https://stripe.com/jobs/search?gh_jid=7587353) | Luxembourg | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Data Excellence Manager](https://stripe.com/jobs/search?gh_jid=8106026) | US Remote, Chicago, SF, Seattle, | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Deal Pricing](https://stripe.com/jobs/search?gh_jid=7998031) | Mexico City | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Deal Pricing Strategist](https://stripe.com/jobs/search?gh_jid=8080240) | San Francisco, California | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Deal Pricing Strategist, APAC](https://stripe.com/jobs/search?gh_jid=7960875) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Deal Strategist](https://stripe.com/jobs/search?gh_jid=8224612) | London, Dublin | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Deal Strategist](https://stripe.com/jobs/search?gh_jid=7958150) | US-Remote | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [EMEA Demand Generation, Platforms](https://stripe.com/jobs/search?gh_jid=8209626) | London | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager - Core Performance](https://stripe.com/jobs/search?gh_jid=7835108) | Sydney, Australia | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager - LPM Foundations](https://stripe.com/jobs/search?gh_jid=8230300) | Dublin | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager, APAC & EMEA Cards](https://stripe.com/jobs/search?gh_jid=7841757) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager, Abuse Control Engineering](https://stripe.com/jobs/search?gh_jid=8172489) | Seattle, SF, NYC, Remote in the  | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager, Agentic Commerce](https://stripe.com/jobs/search?gh_jid=8172499) | N/A | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager, Billing Collections](https://stripe.com/jobs/search?gh_jid=8198193) | N/A | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager, Billing Configuration](https://stripe.com/jobs/search?gh_jid=8165515) | N/A | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager, Billing Products](https://stripe.com/jobs/search?gh_jid=8180536) | US-Remote, Chicago | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager, Checkout Optimization](https://stripe.com/jobs/search?gh_jid=8161567) | N/A | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager, Data Transformation](https://stripe.com/jobs/search?gh_jid=7688358) | US-SEA, US-SF, US-NYC, US-Remote | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager, Payments](https://stripe.com/jobs/search?gh_jid=8104767) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager, Requirements Management (Risk)](https://stripe.com/jobs/search?gh_jid=8124299) | Toronto | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Engineering Manager, Terminal](https://stripe.com/jobs/search?gh_jid=7769005) | Toronto, Canada | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Enterprise Support Specialist](https://stripe.com/jobs/search?gh_jid=8141829) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Enterprise Support Specialist](https://stripe.com/jobs/search?gh_jid=8191248) | Dublin | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Executive Advisory Programs Manager](https://stripe.com/jobs/search?gh_jid=8190030) | South San Francisco HQ, New York | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [F&S COE Manager](https://stripe.com/jobs/search?gh_jid=8131132) | Bengaluru | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Fraud Strategist](https://stripe.com/jobs/search?gh_jid=8112448) | LOCATION | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [Global Partnerships Lead — Greater China, Hong Kong & Singapore](https://stripe.com/jobs/search?gh_jid=8146053) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Head of New Business, Startups EMEA](https://stripe.com/jobs/search?gh_jid=8176733) | Dublin | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Head of Platforms Solutions Architecture](https://stripe.com/jobs/search?gh_jid=7915144) | San Francisco, CA | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Head of Private Equity and Advisory Partnerships](https://stripe.com/jobs/search?gh_jid=8165855) | US-San Francisco | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [Head of Strategic Risk Programs, New Markets](https://stripe.com/jobs/search?gh_jid=8076108) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Integrated Campaigns Manager - Stablecoins, Crypto, and Bridge](https://stripe.com/jobs/search?gh_jid=8067276) | US, Remote | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Investigator](https://stripe.com/jobs/search?gh_jid=8172491) | US Remote  | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Investment Lead, Intercept](https://stripe.com/jobs/search?gh_jid=8083464) | New York City, San Francisco, US | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Manager, Competitive Programs](https://stripe.com/jobs/search?gh_jid=8175671) | NYC, Seattle, SF, Remote | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Manager, Global Sanctions](https://stripe.com/jobs/search?gh_jid=8014898) | United States | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Manager, Global Sanctions](https://stripe.com/jobs/search?gh_jid=7896802) | Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Manager, Payments Performance (SEA and Greater China)](https://stripe.com/jobs/search?gh_jid=8175826) | Singapore | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Manager, Solution Architecture Platforms](https://stripe.com/jobs/search?gh_jid=8104302) | South San Francisco, CA , New Yo | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Manager, Solutions Architecture - Enterprise (West)](https://stripe.com/jobs/search?gh_jid=8175633) | San Francisco, CA  | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Manager, Solutions Architecture - Platforms (Chicago)](https://stripe.com/jobs/search?gh_jid=8175667) | Chicago, IL | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Manager, Solutions Architecture- Enterprise Hunter](https://stripe.com/jobs/search?gh_jid=8163542) | New York, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Money Management Demand Generation Manager, Americas](https://stripe.com/jobs/search?gh_jid=8187278) | South San Francisco HQ, Seattle | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [PMM Lead, Executive Content & Experiences](https://stripe.com/jobs/search?gh_jid=8178459) | San Francisco, New York, Seattle | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager](https://stripe.com/jobs/search?gh_jid=8104427) | London | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager](https://stripe.com/jobs/search?gh_jid=8096790) | Mexico | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager (Banks)](https://stripe.com/jobs/search?gh_jid=7289456) | London - United Kingdom | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager, AI Partnerships](https://stripe.com/jobs/search?gh_jid=8165269) | San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager, AMER Bank Partnerships](https://stripe.com/jobs/search?gh_jid=8187566) | US-San Francisco; US-New York Ci | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager, Alliances and Channels](https://stripe.com/jobs/search?gh_jid=8165267) | US-Remote | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager, Global Money Management](https://stripe.com/jobs/search?gh_jid=8143073) | US-NYC; US-San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager, Global Payment Methods](https://stripe.com/jobs/search?gh_jid=8160890) | London | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager, Global Strategic Alliances](https://stripe.com/jobs/search?gh_jid=7461966) | US-SF | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager, Link - Payments Partnerships](https://stripe.com/jobs/search?gh_jid=8090126) | US-NYC; US-San Francisco; US-Sea | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager, Strategic Partnerships](https://stripe.com/jobs/search?gh_jid=8094869) | US-NYC; US-San Francisco; US-Sea | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager, Strategic Partnerships](https://stripe.com/jobs/search?gh_jid=7973002) | US-San Francisco; US-New York Ci | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager, Strategic Payment Partnerships](https://stripe.com/jobs/search?gh_jid=8155164) | US-San Francisco; US-New York Ci | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager- Global Strategic Alliances](https://stripe.com/jobs/search?gh_jid=7677136) | London | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Partner Development Manager- Platforms](https://stripe.com/jobs/search?gh_jid=8139202) | Dublin | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Partner Solutions Architecture Manager](https://stripe.com/jobs/search?gh_jid=8175651) | NY, SF, Chicago, Remote | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [Payments Fraud Investigator](https://stripe.com/jobs/search?gh_jid=7554002) | Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Payments Performance Strategist, LATAM](https://stripe.com/jobs/search?gh_jid=8155386) | CDMX | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Portfolio Pricing Strategist](https://stripe.com/jobs/search?gh_jid=7858811) | US-Remote | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Pricing Strategist](https://stripe.com/jobs/search?gh_jid=8187578) | South San Francisco, New York Ci | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Product Support Specialist](https://stripe.com/jobs/search?gh_jid=8148497) | Chicago | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Proposal Lead](https://stripe.com/jobs/search?gh_jid=8210228) | Chicago; Atlanta | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Risk Partnerships Manager, Banks & Treasury](https://stripe.com/jobs/search?gh_jid=8178563) | London, Dublin, UK-Remote | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Risk Partnerships Manager, Stablecoin](https://stripe.com/jobs/search?gh_jid=8078333) | US-San Francisco; US-NYC; US-Sea | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Seller Systems Team Lead (Night Shift)](https://stripe.com/jobs/search?gh_jid=8175820) | Bengaluru | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Startup Partnerships - Y Combinator](https://stripe.com/jobs/search?gh_jid=8181026) | San Francisco | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [Strategic Payment Advisors Lead - APAC](https://stripe.com/jobs/search?gh_jid=8165853) | Sydney Or Melbourne | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [Strategic Sourcing Manager, Tech & Product](https://stripe.com/jobs/search?gh_jid=8072213) | SF, NYC, SEA | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [Technical Solutions Engineering Manager](https://stripe.com/jobs/search?gh_jid=8079858) | San Francisco or Seattle | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [UK Public Sector Lead](https://stripe.com/jobs/search?gh_jid=8096121) | London | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Stripe | [User Escalation Specialist](https://stripe.com/jobs/search?gh_jid=8180318) | Chicago | no-keyword-match |  |  |
| UNCLASSIFIED | Stripe | [User Risk Strategist](https://stripe.com/jobs/search?gh_jid=8230758) | New York, NY  | no-keyword-match |  |  |
| UNCLASSIFIED | Supabase | [AWS Enterprise Segment Lead](https://jobs.ashbyhq.com/supabase/f3a7c4bf-3e79-4556-a4e9-04d6987a0e8f) | Remote, AMER | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Supabase | [Engineering Manager](https://jobs.ashbyhq.com/supabase/99a80436-89ec-412b-b782-1dd462bd16dc) | Remote, Global | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Supabase | [Engineering Manager, Billing](https://jobs.ashbyhq.com/supabase/b4a2f5e5-5c51-4c1a-abde-a89de27451c7) | Remote, Global | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Supabase | [Member of Technical Staff/ Partners](https://jobs.ashbyhq.com/supabase/cb04ae3a-3a47-4e21-928f-c2456b7b214e) | Remote, Global · Remote, San Fra | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Supabase | [Partnerships Lead (APAC)](https://jobs.ashbyhq.com/supabase/180257c0-ad46-4fae-b34f-36d8ddc2fe2e) | Remote, Singapore | only 1 topic words, no role word in title |  |  |
| UNCLASSIFIED | Twilio | [Compensation Manager](https://job-boards.greenhouse.io/twilio/jobs/7983662) | Remote - US | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Director, Global Campaigns](https://job-boards.greenhouse.io/twilio/jobs/8138860) | Remote - United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Director, LATAM Carrier Relations](https://job-boards.greenhouse.io/twilio/jobs/8175075) | Remote - Brazil; Remote - Colomb | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Executive Business Partner](https://job-boards.greenhouse.io/twilio/jobs/8226528) | Remote - US | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Fraud Specialist 1](https://job-boards.greenhouse.io/twilio/jobs/8132266) | Remote - Estonia | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Incident Commander](https://job-boards.greenhouse.io/twilio/jobs/8089122) | Remote - US | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Manager, Personalized Support](https://job-boards.greenhouse.io/twilio/jobs/8223581) | Remote - India | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Principal PR Manager](https://job-boards.greenhouse.io/twilio/jobs/8197775) | Remote - US | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Principal Presales Product Specialist](https://job-boards.greenhouse.io/twilio/jobs/8180238) | Remote - US | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Senior Engineering Manager](https://job-boards.greenhouse.io/twilio/jobs/8204351) | Remote - US | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Senior Engineering Manager (L5)](https://job-boards.greenhouse.io/twilio/jobs/8001804) | Remote - India | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Senior Engineering Manager Twilio’s Conversational Agents](https://job-boards.greenhouse.io/twilio/jobs/7926887) | Remote - US | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Senior Engineering Manager V&V Media](https://job-boards.greenhouse.io/twilio/jobs/8067147) | Remote - United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Senior Engineering Manager V&V Media](https://job-boards.greenhouse.io/twilio/jobs/8067500) | Remote - Alberta, Canada (DNU) | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Senior Engineering Manager V&V Media](https://job-boards.greenhouse.io/twilio/jobs/8067501) | Remote - Ontario, Canada (DNU) | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Senior Engineering Manager V&V Media](https://job-boards.greenhouse.io/twilio/jobs/8067678) | Remote - US | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Senior Engineering Manager, Voice and Video](https://job-boards.greenhouse.io/twilio/jobs/8073683) | Remote - Ireland | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Senior Manager, Escalation Management](https://job-boards.greenhouse.io/twilio/jobs/8172311) | Remote - US | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Senior Manager, New Business DACH & Benelux](https://job-boards.greenhouse.io/twilio/jobs/8201677) | Remote - United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Senior Telecom Billing Specialist](https://job-boards.greenhouse.io/twilio/jobs/8119052) | Remote - United Kingdom | no-keyword-match |  |  |
| UNCLASSIFIED | Twilio | [Staff, Escalations Manager](https://job-boards.greenhouse.io/twilio/jobs/8207721) | Remote - Spain | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Director, Solutions Architects](https://job-boards.greenhouse.io/vercel/jobs/6111005004) | Hybrid - London, Berlin | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Engineering Manager - Next.js](https://job-boards.greenhouse.io/vercel/jobs/6140055004) | Hybrid - San Francisco, New York | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Engineering Manager, CDN](https://job-boards.greenhouse.io/vercel/jobs/5701765004) | Hybrid - San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Engineering Manager, Dashboard](https://job-boards.greenhouse.io/vercel/jobs/6115908004) | Hybrid - San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [FP&A Manager, Product](https://job-boards.greenhouse.io/vercel/jobs/6183272004) | Hybrid - San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Partner Lead, EMEA](https://job-boards.greenhouse.io/vercel/jobs/5844601004) | Hybrid - London, Berlin | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [SOX Manager](https://job-boards.greenhouse.io/vercel/jobs/6163585004) | Hybrid - India | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Senior HRBP - G&A](https://job-boards.greenhouse.io/vercel/jobs/6090854004) | Hybrid - San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Senior Integrated Campaigns Manager](https://job-boards.greenhouse.io/vercel/jobs/6119765004) | Hybrid - San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Senior Integrated Campaigns Manager](https://job-boards.greenhouse.io/vercel/jobs/6122619004) | Hybrid - San Francisco, New York | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Senior Partner Programs Manager](https://job-boards.greenhouse.io/vercel/jobs/6188894004) | Hybrid - San Francisco, New York | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Software Engineering Intern - Summer '27](https://job-boards.greenhouse.io/vercel/jobs/6181759004) | Hybrid - San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Software Engineering Intern - Winter '27](https://job-boards.greenhouse.io/vercel/jobs/6181755004) | Hybrid - San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Startups Program Lead](https://job-boards.greenhouse.io/vercel/jobs/5971203004) | Hybrid - San Francisco, New York | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Strategic Cloud Partnerships Lead](https://job-boards.greenhouse.io/vercel/jobs/5825469004) | Hybrid - San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Strategic Product Partnerships Lead](https://job-boards.greenhouse.io/vercel/jobs/6188898004) | Hybrid - San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Vercel | [Strategic Sourcing Manager](https://job-boards.greenhouse.io/vercel/jobs/6163582004) | Hybrid - San Francisco | no-keyword-match |  |  |
| UNCLASSIFIED | Webflow | [IT Support Specialist](https://job-boards.greenhouse.io/webflow/jobs/8201996) | Argentina Remote | no-keyword-match |  |  |
| UNCLASSIFIED | Writer | [Director, solutions architecture](https://jobs.ashbyhq.com/writer/1258273b-7cb1-490e-8a2b-14c27ea725fd) | San Francisco, CA | no-keyword-match |  |  |
| UNCLASSIFIED | Writer | [Enterprise AI adoption lead (East)](https://jobs.ashbyhq.com/writer/9658b0b9-40ca-4621-bdf4-26cc9b849eb6) | New York City, NY | only 2 topic words, no role word in title |  |  |
| UNCLASSIFIED | Writer | [Enterprise AI adoption lead (UK)](https://jobs.ashbyhq.com/writer/2738f03f-510a-4f7a-8839-97ca317ca139) | London, UK | only 2 topic words, no role word in title |  |  |
| UNCLASSIFIED | Writer | [Enterprise AI transformation lead (Central)](https://jobs.ashbyhq.com/writer/3ffd6de4-d2fb-44b3-bc4a-4daf0eaa44c8) | Chicago, IL · Austin, TX | no-keyword-match |  |  |
| UNCLASSIFIED | Writer | [Enterprise AI transformation lead (East)](https://jobs.ashbyhq.com/writer/cda64c6b-19cc-4388-baf5-31cce0a440c2) | New York City, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Writer | [Enterprise AI transformation lead (UK)](https://jobs.ashbyhq.com/writer/da607c2c-0d6d-4bc7-b86e-a05859370ea2) | London, UK | no-keyword-match |  |  |
| UNCLASSIFIED | Writer | [Enterprise AI transformation lead (West)](https://jobs.ashbyhq.com/writer/ac169f24-14f9-4654-af81-6e9a7fdd6df3) | San Francisco, CA · Seattle, WA | no-keyword-match |  |  |
| UNCLASSIFIED | Writer | [Strategic AI adoption lead (East)](https://jobs.ashbyhq.com/writer/e95f8bc9-514b-4e8c-9da9-1adea925866b) | New York City, NY | only 2 topic words, no role word in title |  |  |
| UNCLASSIFIED | Writer | [Strategic AI adoption lead (UK)](https://jobs.ashbyhq.com/writer/e55b2a4c-cae6-46ec-b7f3-fc2555b407fe) | London, UK | only 2 topic words, no role word in title |  |  |
| UNCLASSIFIED | Writer | [Strategic AI transformation lead (Central)](https://jobs.ashbyhq.com/writer/dd678cc9-c4a2-45ba-b499-ed84ee0d1f4d) | Chicago, IL · Austin, TX | no-keyword-match |  |  |
| UNCLASSIFIED | Writer | [Strategic AI transformation lead (East)](https://jobs.ashbyhq.com/writer/95d975eb-06f8-4d29-bd75-2fdffa265d78) | New York City, NY | no-keyword-match |  |  |
| UNCLASSIFIED | Writer | [Strategic AI transformation lead (UK)](https://jobs.ashbyhq.com/writer/3b600a0b-3b65-4973-8346-9763360a0dea) | London, UK | no-keyword-match |  |  |
| UNCLASSIFIED | Writer | [Strategic AI transformation lead (West)](https://jobs.ashbyhq.com/writer/a3183d30-ca30-4fb4-bb81-f624cd699b3a) | San Francisco, CA · Seattle, WA | no-keyword-match |  |  |

---

## Why this beats sampling postings

A random sample of 3,446 postings is mostly accountants and backend engineers: true negatives, correctly rejected, and reading them teaches nothing. Sorting by function puts every decision the filter could plausibly have got wrong into two short lists, and it makes the *systematic* errors visible — one word behaving badly across a whole family, rather than a scatter of individual mistakes. Both errors found so far were systematic: `enablement` meaning sales support, and `training` meaning model training.

It does not replace reading a random sample. It finds errors in the families someone thought to name; a teaching job whose title uses none of these words lands in UNCLASSIFIED or in a wrong family, and only a random read will catch that. Do both, and expect this one to be cheaper.

