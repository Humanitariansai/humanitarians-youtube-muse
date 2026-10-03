# SHARPNESS GATE — review-tanaka

Compiled master: `review-tanaka-slate.mp4`
Median Laplacian variance: **233.1**
Failure threshold: 116.5 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 510.3 | 219% | PASS — 219% |
| B01 | 126.6 | 54% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 413.6 | 177% | PASS — 177% |
| B03 | 126.8 | 54% | SKIP (exempt — no pixel-art rotation possible) |
| B04 | 403.9 | 173% | PASS — 173% |
| B05 | 387.1 | 166% | PASS — 166% |
| B06 | 127.6 | 55% | SKIP (exempt — no pixel-art rotation possible) |
| B07 | 126.2 | 54% | SKIP (exempt — no pixel-art rotation possible) |
| B08 | 130.7 | 56% | SKIP (exempt — no pixel-art rotation possible) |
| B09 | 129.2 | 55% | SKIP (exempt — no pixel-art rotation possible) |
| BVDT | 464.9 | 199% | PASS — 199% |
| BHTF | 566.0 | 243% | PASS — 243% |
| BOUT | 233.1 | 100% | PASS — 100% |
