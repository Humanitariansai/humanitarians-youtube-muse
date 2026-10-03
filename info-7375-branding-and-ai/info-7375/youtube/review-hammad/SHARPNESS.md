# SHARPNESS GATE — review-hammad

Compiled master: `review-hammad-slate.mp4`
Median Laplacian variance: **314.9**
Failure threshold: 157.4 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 553.7 | 176% | PASS — 176% |
| B01 | 125.3 | 40% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 387.4 | 123% | PASS — 123% |
| B03 | 399.5 | 127% | PASS — 127% |
| B04 | 127.1 | 40% | SKIP (exempt — no pixel-art rotation possible) |
| B05 | 414.5 | 132% | PASS — 132% |
| B06 | 394.0 | 125% | PASS — 125% |
| B07 | 130.5 | 41% | SKIP (exempt — no pixel-art rotation possible) |
| B08 | 129.4 | 41% | SKIP (exempt — no pixel-art rotation possible) |
| B09 | 129.5 | 41% | SKIP (exempt — no pixel-art rotation possible) |
| B10 | 129.0 | 41% | SKIP (exempt — no pixel-art rotation possible) |
| BVDT | 465.1 | 148% | PASS — 148% |
| BHTF | 618.2 | 196% | PASS — 196% |
| BOUT | 242.4 | 77% | PASS — 77% |
