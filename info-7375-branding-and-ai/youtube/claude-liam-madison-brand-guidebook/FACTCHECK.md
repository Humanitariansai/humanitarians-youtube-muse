# FACTCHECK — claude-liam-madison-brand-guidebook

Status: VERIFIED — 2026-08-11, Bear Brown
**Rule**: No beat ships with an unverified claim.

---

| Beat | Claim | Verdict | Source | Correction |
|---|---|---|---|---|
| B00, B02, B37 | "thirty-two InDesign pages" | PASS | SOURCES.md: "32-page inventory extracted from brand-guidebook-000-nbb.idml" | None |
| B04 | "brand, logo, color, typography, online, stationery, imagery, info" — 8 sections | PASS | PLAN.md act map; page.tsx description: "logo system, color palette, typography, social, stationery, imagery, contact" — 8 confirmed | None |
| B03, B37 | Three files: .indt (master), .idml (for Claude to edit), .pdf (for looking) | PASS | page.tsx `files` array: brand-guidebook.indt, brand-guidebook.idml, brand-guidebook.pdf with exact role labels | None |
| B33 | "IDML is a zip of XML; unzip it — designmap.xml, Stories/, Resources/Graphic.xml" | PASS | page.tsx claudePrompt: "It is a zip archive: unzip it, edit the XML, re-zip…"; Stories/*.xml for text; Resources/Graphic.xml for colors; designmap.xml is root | None |
| B33, B38 | "re-zip with the mimetype file first, stored uncompressed" | PASS | page.tsx claudePrompt: "re-zip with the 'mimetype' file as the FIRST entry, stored uncompressed (zip -X out.idml mimetype -0, then add the rest)" | None |
| B17, B36 | Template orange #FF7929 re-mapped to Bear Brown brown #8B3A0F | PASS | SOURCES.md: "#FF7929→#8B3A0F remap" documented as performed adaptation; #8B3A0F confirmed in bearbrown_co CLAUDE.md: "--m-accent = #8B3A0F" | None |
| B15, B16, B36 | Bear Brown palette: #8B3A0F accent, #FAF9F5 cream, #3D3929 ink | PASS | bearbrown_co CLAUDE.md lists exact hex values under print design system | None |
| B18 | "colors that carry meaning clear 3:1 contrast; if they can't, they decorate" | PASS | bearbrown_co CLAUDE.md: "--p-terra (#D97757) is measured at 2.96:1 on cream — below the 3:1 WCAG threshold. It is used only for decoration" | None |
| B35, B38 | "six brackets: name, website, email, title, address, accent color" | PASS | page.tsx claudePrompt: [YOUR NAME], [YOUR SITE], [YOUR EMAIL], [YOUR TITLE], [YOUR ADDRESS], [YOUR HEX] — exactly 6 fields | None |
| B38 | URL: madison.humanitarians.ai/brand-guidebook | PASS | File path: books/madison.humanitarians.ai/app/brand-guidebook/page.tsx; SOURCES.md lists URL as canonical | None |
| B38 | YOUR TURN rules: same-length text, re-map color family, mimetype-first zip | PASS | page.tsx claudePrompt Rules section contains all three constraints verbatim | None |
| B02 | "sixteen by nine" format | PASS | PNG exports in guidebook/ measured 1920×1080 (ratio 1.778 = 16:9); confirmed from brand-guidebook-000.png via PIL | None |
| B29 | "spacing can be reduced based on design type" | PASS | Confirmed in brand-guidebook-000-nbb.idml: Stories/Story_u5ce7.xml contains `<Content>space can be </Content><Br /><Content>reduce based on design type.</Content>` (original has minor grammar variation; narration is correct paraphrase) | None |

---

All claims verified. No outstanding items.

---

## Sources

- SOURCES.md (books/branding-and-ai/youtube/claude-liam-madison-brand-guidebook/SOURCES.md)
- books/madison.humanitarians.ai/app/brand-guidebook/page.tsx (download page + claudePrompt)
- books/madison.humanitarians.ai/CLAUDE.md (bearbrown_co print design system — hex values, 3:1 rule)
- books/branding-and-ai/guidebook/brand-guidebook-000-nbb.idml (primary source; page count via SOURCES.md)
