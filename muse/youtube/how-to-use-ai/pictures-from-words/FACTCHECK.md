# FACTCHECK.md — Pictures from Words

Every checkable claim in the script was verified before writing (checked
2026-10-03). No statistics are invented. Unverifiable or version-specific
claims were cut; hedges are kept where sources hedge.

## Verified (record)

1. The effective prompt formula across guides is subject + style (+
   setting + lighting + mood + composition): community "S-S-C-D-C" method
   (Subject, Style, Constraints, Details, Composition); DALL-E prompting
   guides list Subject / Style-Medium / Setting-Atmosphere / Lighting-Mood
   / Composition-Perspective; CapCut/OpenAI-oriented guide: clarity +
   style + lighting + composition + color. → web search 2026-10-03
   [record]
2. Text-to-image models do not "type" letters; they generate letter-like
   shapes, so words in generated images are frequently misspelled.
   PetaPixel (2024-03-06), quoting UCL computer scientist Peter Bentley:
   "they do not understand 3D objects nor do they understand text when it
   appears in images … text within an image is just another part of an
   image to them." TechCrunch (2024-03-21), quoting DAIR's Asmelash Teka
   Hadgu: models "perform much better on artifacts like cars and people's
   faces, and less so on smaller things like fingers and handwriting."
   → web search 2026-10-03 [record]
3. Hands/fingers are a historically hard case for image generators; the
   arXiv literature (e.g. 2408.15461) treats realistic hand generation as
   an open problem with dedicated repair methods (HandRefiner,
   HandDiffuser). The film says "getting better every year" — a hedge the
   sources support directionally, not a metric. → web search 2026-10-03
   [record]
4. Diffusion image models start from random noise and remove noise step by
   step: Midjourney "Seeds" docs ("every image begins as random noise like
   TV static"); Ho et al. 2020 (DDPM sampling). Verified independently in
   the companion fellows film
   (`fellows/rohan-v/2026-09-25-how-ai-image-generators-turn-noise-into-a-picture`,
   FACTCHECK.md claims 5–7). The film's one-liner ("starts from visual
   static … and sharpens it, step by step, steered by your sentence") is a
   plain-language compression of this. → companion film + web [record]
5. AI-content disclosure is an established norm: TikTok, YouTube, X, and
   Meta apps carry AI labels/disclosure toggles; C2PA Content Credentials
   is the open provenance standard; EU AI Act Article 50 requires visible
   labels on AI-generated content that could be mistaken for authentic.
   The film says "most platforms now offer an AI label, and some places
   require one" — deliberately hedged to avoid version-specific policy
   claims. → web search 2026-10-03 [record]
6. Iterating prompts across several rounds is standard prompting practice
   (every guide above assumes revision); "three or four rounds is normal"
   is framed as practical experience, not a measured statistic. [record
   as practice, not metric]

## Judgments (judgment)

- The "ladder" (vague → subject/style/mood → iterate) is my teaching
  structure for the film, not a quoted source. [judgment]
- The five-slot recipe (subject, setting, style, lighting, mood) is my
  compression of the guides' longer lists into five memorable slots.
  [judgment]
- "The sweet spot is drafts and placeholders" is an editorial judgment
  about where a general audience gets value without risk. [judgment]
- "Short words survive best" for in-image text is practical advice drawn
  from the failure mode in (2), not a measured claim. [judgment]

## Cut or disclosed

- No product names are recommended and no version-specific features are
  asserted ("open any image generator"); the film must not rot.
- No claim that hands/faces are "fixed" — the film says "check closely",
  which holds whether or not models improve.
- No claim about any platform's exact disclosure rule text; "some places
  require one" is the hedge, and platform policies change.
- No real AI-generated images are shown; every "result" is a drawn Manim
  placeholder, so the film never misrepresents a specific model's output.
- The "companion fellows film" is referenced by repo path only; nothing is
  quoted from it on screen.
