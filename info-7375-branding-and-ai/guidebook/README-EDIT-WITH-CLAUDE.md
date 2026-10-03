# Brand Guidebook Template — edit with Claude, export with InDesign

You do NOT need to know InDesign. Claude does the editing; InDesign is just the
export button.

## What's in this folder

| File | What it is |
|---|---|
| `brand-guidebook-canonical.indt` | The template master (InDesign format) |
| `brand-guidebook-000-nbb.idml` | The same document in IDML — **this is the file Claude edits** |
| `*.svg`, `*.ai` | Logo artwork (replace with your own marks) |

IDML is a zip of plain XML, so Claude can open it, change any text, color, or
vector shape, and hand you back a valid file. The binary `.indd`/`.indt`
formats Claude can't edit — always work from the `.idml`.

## The workflow (3 steps)

1. **Ask Claude.** Start a Claude session (Cowork or Claude Code) with access to
   this folder and paste the prompt below, filling in your details.
2. **Open the result in InDesign.** Double-click the new `.idml` Claude saved.
   If a *Missing Fonts* dialog appears: click **Activate** (Minion Pro comes
   from Adobe Fonts automatically); install Open Sans and Philosopher free from
   Google Fonts if they're flagged. One-time setup.
3. **Export.** File → Export → **Adobe PDF (Print)** for a shareable guidebook,
   or PNG/JPEG for single pages. Done. (File → Save As → `.indt` if you want
   your own reusable template.)

Deleting pages you don't need is allowed and expected — the template includes
every page a brand might design for; yours probably won't need all of them.

## Paste this into Claude

```
In this folder is brand-guidebook-000-nbb.idml, an InDesign IDML brand
guidebook template. Make me a customized copy named brand-guidebook-MINE.idml
with these changes:

- Replace the name "Nik Bear Brown" everywhere with: [YOUR NAME]
- Replace the website "bearbrown.co" / "BEARBROWN.CO" with: [YOUR SITE]
- Replace the email "bear@bearbrown.co" with: [YOUR EMAIL]
- Replace the title "Founder, Bear Brown" with: [YOUR TITLE]
- Replace the contact-page address with: [YOUR ADDRESS or "leave placeholder"]
- Change the accent color palette from Bear Brown brown (#8B3A0F) to: [YOUR HEX]

Rules for editing the IDML safely:
- It is a zip archive: unzip it, edit the XML, re-zip with the "mimetype" file
  as the FIRST entry, stored uncompressed (zip -X out.idml mimetype -0, then
  add the rest).
- All visible text lives in <Content>...</Content> elements inside
  Stories/*.xml. Replace text there; XML-escape any & < > characters.
- Keep each replacement roughly the same length as the original text (within
  ~25%) so frames don't overflow.
- Colors are defined in Resources/Graphic.xml as ColorValue attributes. To
  re-theme, map the accent family in tint-preserving fashion rather than
  replacing only the exact accent value.
- Validate every changed XML file parses before re-zipping, and verify the zip
  with unzip -t.
- Do not rename files inside the archive or edit designmap.xml unless removing
  pages.

When done, list every replacement you made and anything you could not find.
```

## If something looks wrong in InDesign

- **Red ⊞ symbol on a text frame** — text too long for its box (overset). Click
  the frame with the Type tool and shorten the text, or ask Claude to redo the
  edit shorter.
- **Pink highlight on text** — a font is missing; see step 2.
- **A logo loop fills solid** — select it, then Object → Paths → Make Compound
  Path.
