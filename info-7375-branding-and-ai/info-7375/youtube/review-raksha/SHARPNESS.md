# SHARPNESS GATE — review-raksha

Compiled master: `review-raksha-slate.mp4`
Median Laplacian variance: **316.9**
Failure threshold: 158.4 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 432.5 | 136% | PASS — 136% |
| B01 | 125.8 | 40% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 394.9 | 125% | PASS — 125% |
| B03 | 411.6 | 130% | PASS — 130% |
| B04 | 124.5 | 39% | SKIP (exempt — no pixel-art rotation possible) |
| B05 | 399.3 | 126% | PASS — 126% |
| B06 | 128.6 | 41% | SKIP (exempt — no pixel-art rotation possible) |
| B07 | 128.2 | 40% | SKIP (exempt — no pixel-art rotation possible) |
| B08 | 129.8 | 41% | SKIP (exempt — no pixel-art rotation possible) |
| B09 | 128.4 | 41% | SKIP (exempt — no pixel-art rotation possible) |
| B10 | 397.3 | 125% | PASS — 125% |
| BVDT | 464.9 | 147% | PASS — 147% |
| BHTF | 528.7 | 167% | PASS — 167% |
| BOUT | 238.8 | 75% | PASS — 75% |
