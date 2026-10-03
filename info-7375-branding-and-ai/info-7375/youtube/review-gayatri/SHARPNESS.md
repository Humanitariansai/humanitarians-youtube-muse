# SHARPNESS GATE — review-gayatri

Compiled master: `review-gayatri-slate.mp4`
Median Laplacian variance: **129.6**
Failure threshold: 64.8 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 499.8 | 386% | PASS — 386% |
| B01 | 126.0 | 97% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 396.7 | 306% | PASS — 306% |
| B03 | 126.6 | 98% | SKIP (exempt — no pixel-art rotation possible) |
| B04 | 127.7 | 99% | SKIP (exempt — no pixel-art rotation possible) |
| B05 | 129.8 | 100% | SKIP (exempt — no pixel-art rotation possible) |
| B06 | 129.0 | 100% | SKIP (exempt — no pixel-art rotation possible) |
| B07 | 128.6 | 99% | SKIP (exempt — no pixel-art rotation possible) |
| B08 | 129.4 | 100% | SKIP (exempt — no pixel-art rotation possible) |
| BVDT | 468.7 | 362% | PASS — 362% |
| BHTF | 610.5 | 471% | PASS — 471% |
| BOUT | 195.6 | 151% | PASS — 151% |
