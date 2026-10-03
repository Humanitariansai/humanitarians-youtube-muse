# SHARPNESS GATE — review-vaibhav

Compiled master: `review-vaibhav-slate.mp4`
Median Laplacian variance: **198.5**
Failure threshold: 99.2 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 559.9 | 282% | PASS — 282% |
| B01 | 127.3 | 64% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 414.9 | 209% | PASS — 209% |
| B03 | 128.0 | 64% | SKIP (exempt — no pixel-art rotation possible) |
| B04 | 406.5 | 205% | PASS — 205% |
| B05 | 398.4 | 201% | PASS — 201% |
| B06 | 126.5 | 64% | SKIP (exempt — no pixel-art rotation possible) |
| B07 | 129.0 | 65% | SKIP (exempt — no pixel-art rotation possible) |
| B08 | 129.4 | 65% | SKIP (exempt — no pixel-art rotation possible) |
| B09 | 130.3 | 66% | SKIP (exempt — no pixel-art rotation possible) |
| BVDT | 469.2 | 236% | PASS — 236% |
| BHTF | 565.5 | 285% | PASS — 285% |
| BOUT | 198.5 | 100% | PASS — 100% |
