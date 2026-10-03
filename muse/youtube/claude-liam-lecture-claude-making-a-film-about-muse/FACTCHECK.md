# FACTCHECK.md — "Claude making a film about Muse" (Gate F)

Source of truth: the document Bear pasted on 2026-10-03 ("Meta Muse: What
It Does, Security Concerns, and Business Model"). The film presents the
document's content AS Bear and Claude's opinion — Liam narrates their
analysis; he does not assert it as his own verified fact.

## Attribution map (how each claim class is voiced)

| Class | Examples | Voicing |
|---|---|---|
| Doc's own framing/analysis | "personal superintelligence" as framing; endurance-not-intelligence; intent layer; skepticism | "Bear and Claude's read", "their analysis" |
| Attributed to Meta | launch date, tagline "AI That Hustles for You", "first step" quote, no ads inside Muse | "Meta says" |
| Third-party reports | Malwarebytes zero-day; Pivot to AI critique; "one analysis" (11/47); "widely expected" (Marketplace) | "researchers report", "one analysis estimates", "widely expected" — never as established fact |
| Nik's experience/take | capability vs GPT-6 Astra / Claude Fable / Opus; phone discomfort | "in Nik's experience" |
| Cross-checked with Muse docs | Sept 8 2026 launch; US/Canada; Muse Spark; surfaces | solid — matches `~/docs/muse.md` |
| Numbers from the doc only | 2.5M downloads; pricing tiers; $1.25/$4.25 API; 6.8 GB export | "the document reports" — not independently verified |

## Beat-by-beat claims

| # | Beat | Claim | Verdict | Fix |
|---|---|---|---|---|
| 1 | B01 | Agent that acts: goal → plan → steps, approval before consequential actions | doc's framing of the product | voice as their read |
| 2 | B02 | Launched Sept 8 2026 (Meta); Muse Spark (cross-checked); < GPT-6 Astra etc. (Nik's take); 2.5M downloads (doc reports) | mixed attribution | keep each attribution separate |
| 3 | B03 | Persistent Linux VM per user; same architecture as Cowork/Codex | doc's technical description | voice as their read |
| 4 | B04 | Errand list; Ticketmaster launch partner; "endurance, not intelligence" | doc's analysis | voice as their read |
| 5 | B05 | Interfaces + connector lists; Amazon blocked (CNBC per doc); custom connectors unreviewed | third-party + doc | attribute the block; rest as their read |
| 6 | B06 | Small business (Sept 29, TechCrunch per doc); nothing publishes without approval (Meta per doc); Spark API as sanctioned dev route | mixed | attribute |
| 7 | B07 | Pricing tiers + weekly allowances; card required even for free | doc reports | "the document reports" |
| 8 | B08 | API pricing with/without data sharing | doc reports | "the document reports" |
| 9 | B09 | Transaction fees, merchant-paid; free tier as a bet (Zuckerberg per doc) | attributed | attribute the Zuckerberg line |
| 10 | B10 | Subs/API/ads-angle/training-data as secondary revenue | doc's analysis | voice as their read; "Meta says no ads inside Muse" attributed |
| 11 | B11 | Intent layer strategy; 11-of-47 skepticism ("one analysis"); who it's for | analysis | attribute the 11/47; the rest as their read |
| 12 | B12 | Full Disk Access covers the whole disk; behavioral promise vs technical boundary | doc's critique | voice as their critique |
| 13 | B13 | Deny-list violates fail-safe defaults (Saltzer & Schroeder 1975); folder pickers were possible; Messages/Notes/Mail need FDA | doc's critique | voice as their critique |
| 14 | B14 | Malwarebytes zero-day (needs local execution); 6.8 GB runtime export; prompt-extraction reports | third-party reports | attribute each; keep the "needs local execution" qualifier |
| 15 | B15 | Training on by default; policy-not-crypto; cloud processing; token exposure | doc's critique | voice as their critique |
| 16 | B16 | Prompt injection adversarial risk; approval fatigue | doc's analysis | voice as their analysis |
| 17 | B17 | Mascot as trust shortcut (BU professor cited); superintelligence branding overpromises | doc's critique | attribute the professor |
| 18 | B18 | Ad-business conflicts; self-graded attribution; Meta-only advice; lock-in; roadmap risk; phone permissions | doc's analysis | voice as their analysis |
| 19 | B19 | Bear removed the Mac app; verified via pgrep/LaunchAgents/mdfind; web-only | Bear's reported actions | voice as what he did |
| 20 | B20 | The VM/PR/CI/burner pipeline setup | Bear's reported setup | voice as what he did |
| 21 | B21 | General rules (assume breach, caps outside the agent, etc.) | Bear's stated rules | voice as his rules |
| 22 | B22 | Six open questions | doc's list | voice as open questions |

## Deliberately cut / never claimed

- **Prices as established fact** — my product docs don't list them; the film
  attributes all pricing to the document.
- **"Muse is a security disaster" as narrator fact** — it's the document's
  critique (and Pivot to AI's headline); the film voices it as their view.
- **Any claim about what Meta will do** (ads coming, free tier tightening) —
  voiced as the document's expectation, never as fact.
- **OmniRoute executor details** — named once as "stays disabled"; the
  mechanism is not the film's business.

## PROMPTS.md

No paid generation prompts. All visuals are Manim (free) or library Remotion
components (free). No Higgsfield or other paid beats.
