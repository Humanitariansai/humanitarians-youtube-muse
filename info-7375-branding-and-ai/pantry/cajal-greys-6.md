# Cajal Palette — 6-class Greys (sequential)

ColorBrewer 2.0 `Greys`, n=6. Single-hue sequential ramp for ordered/quantitative
data encoding in cajal figures (choropleths, heatmaps, intensity ramps, gradients).
Print-safe, photocopy-safe, and colorblind-safe (single-hue ramps are unaffected by
color vision deficiency). Use hex values directly in SVG attributes.

## Ramp (light → dark)

| Step | Token | Hex | Use |
|------|-------|-----|-----|
| 1 | `--grey-1` | `#f7f7f7` | Lowest value / lightest fill |
| 2 | `--grey-2` | `#d9d9d9` | |
| 3 | `--grey-3` | `#bdbdbd` | |
| 4 | `--grey-4` | `#969696` | |
| 5 | `--grey-5` | `#636363` | |
| 6 | `--grey-6` | `#252525` | Highest value / darkest fill |

## Usage notes

- Use for a single ordered variable only — light = low, dark = high. Do not assign
  the steps to unordered categories (use the categorical palette for that).
- Separate filled regions with the standard hairline stroke `stroke="#D4D4D4"`
  (or `#FFFFFF` on dark maps) so adjacent steps stay legible.
- For the darkest two steps (`#636363`, `#252525`), set overlaid text to `#FFFFFF`;
  for the lighter four, keep text `#2a1a0e`.
- Provide a discrete legend swatch strip — readers read steps, not a continuous bar.
- `#C8102E` (red) and `#C8860E` (ochre) from the base cajal palette may still mark a
  single highlighted region/outline on top of the grey ramp.

## SVG snippet

```svg
<!-- legend swatches -->
<rect x="0"   y="0" width="24" height="16" fill="#f7f7f7" stroke="#D4D4D4"/>
<rect x="24"  y="0" width="24" height="16" fill="#d9d9d9" stroke="#D4D4D4"/>
<rect x="48"  y="0" width="24" height="16" fill="#bdbdbd" stroke="#D4D4D4"/>
<rect x="72"  y="0" width="24" height="16" fill="#969696" stroke="#D4D4D4"/>
<rect x="96"  y="0" width="24" height="16" fill="#636363" stroke="#D4D4D4"/>
<rect x="120" y="0" width="24" height="16" fill="#252525" stroke="#D4D4D4"/>
```

Source: ColorBrewer 2.0 (Cynthia Brewer, Penn State) — Greys, 6-class, HEX.
