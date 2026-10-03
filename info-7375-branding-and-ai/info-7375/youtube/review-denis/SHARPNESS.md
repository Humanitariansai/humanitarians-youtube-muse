# SHARPNESS GATE — review-denis

Compiled master: `review-denis-slate.mp4`
Median Laplacian variance: **159.7**
Failure threshold: 79.9 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 457.4 | 286% | PASS — 286% |
| B01 | 125.9 | 79% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 398.7 | 250% | PASS — 250% |
| B03 | 126.8 | 79% | SKIP (exempt — no pixel-art rotation possible) |
| B04 | 399.2 | 250% | PASS — 250% |
| B05 | 406.1 | 254% | PASS — 254% |
| B06 | 391.0 | 245% | PASS — 245% |
| B07 | 128.2 | 80% | SKIP (exempt — no pixel-art rotation possible) |
| B08 | 129.4 | 81% | SKIP (exempt — no pixel-art rotation possible) |
| B09 | 128.8 | 81% | SKIP (exempt — no pixel-art rotation possible) |
| B10 | 127.6 | 80% | SKIP (exempt — no pixel-art rotation possible) |
| B11 | 126.6 | 79% | SKIP (exempt — no pixel-art rotation possible) |
| B12 | 128.4 | 80% | SKIP (exempt — no pixel-art rotation possible) |
| BVDT | 873.0 | 547% | PASS — 547% |
| BHTF | 530.4 | 332% | PASS — 332% |
| BOUT | 190.1 | 119% | PASS — 119% |
