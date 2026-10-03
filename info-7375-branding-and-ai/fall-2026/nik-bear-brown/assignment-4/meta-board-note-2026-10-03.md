# Meta's job board — 2026-10-03

**What this is.** The answer to "why not Meta — maybe Meta wants to do this?"

**What I tried.** `metacareers.com/jobsearch/` loads, but it is a JS shell:
no server-rendered job data in the HTML, and search runs on Meta's internal
authenticated GraphQL (`/graphql/` with rotating doc IDs). There is no public
JSON feed. Three shapes checked (direct `/jobs?q=`, the `/jobsearch/` page
source, embedded JSON) — nothing machine-readable without a session.

**Finding.** Meta is an **unreadable board**, same category as Google in the
2026-09-26 log. Per the course's own precedent, I stopped rather than guess
more endpoints or reverse-engineer private GraphQL.

**Manual check (re-checkable by hand).** A web search for Meta education /
advocate / "Muse for Education" roles surfaced no dedicated Muse-for-education
advocate posting as of 2026-10-03. Meta does run education-adjacent programs
(e.g., the Meta Career Programs virtual learning series for students), but
that is recruiting marketing, not a staffed education-advocate function.

**What this means.** On the demand measure, Meta belongs in the
"unreadable" section with Google, Adobe, Salesforce, and GitHub — absence
from the table is a measurement gap, not evidence of no demand. The honest
options are the same ones the log left open: check metacareers.com by hand
periodically, or build a browser-driven reader.

**Your input:** whether the browser-driven reader is worth building.
