# PROMPTS — claude-liam-madison-brand-guidebook

All media for this reel is either:
- **Tier 1 own material** — InDesign page exports (no gen-AI, no rights sidecars)
- **Pipeline-generated** — Manim or Remotion (no prompts needed)

No gen-AI image or video generation is required for this reel.

---

## Open pantry slots — InDesign export action

All 11 stills come from a single InDesign export:

```
File → Export → PNG
Pages: 1, 3, 4, 7, 11, 16, 18, 20, 25, 29, 31
Resolution: 2× (or High Quality / 300 DPI equivalent)
Source file: books/branding-and-ai/guidebook/brand-guidebook-000-nbb.idml
             (open as new document → File > Save → Export Pages)
```

Drop exported PNGs into `pantry/` renamed as follows:

| InDesign page | Rename to |
|---|---|
| Page 1 (cover) | `pantry/B02-still.png` |
| Page 3 (welcome) | `pantry/B08-still.png` |
| Page 4 (contents) | `pantry/B04-still.png` |
| Page 7 (logo elements key) | `pantry/B09-still.png` |
| Page 11 (color palette) | `pantry/B15-still.png` |
| Page 16 (type specimen) | `pantry/B19-still.png` |
| Page 18 (triple typeface) | `pantry/B21-still.png` |
| Page 20 (online post) | `pantry/B23-still.png` |
| Page 25 (stationery) | `pantry/B25-still.png` |
| Page 29 (imagery) | `pantry/B31-still.png` |
| Page 31 (contact) | `pantry/B32-still.png` |

B10 reads `pantry/B09-still.png` (same page as B09 — vox run R1).
B26 reads `pantry/B25-still.png` (same page as B25 — vox run R2).

After dropping files: re-run `./brutalist-art/art run branding-and-ai/youtube/claude-liam-madison-brand-guidebook`
