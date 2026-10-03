# SHARPNESS GATE — review-satwika

Compiled master: `review-satwika-slate.mp4`
Median Laplacian variance: **185.9**
Failure threshold: 92.9 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 538.1 | 290% | PASS — 290% |
| B01 | 127.1 | 68% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 416.4 | 224% | PASS — 224% |
| B03 | 414.2 | 223% | PASS — 223% |
| B04 | 125.2 | 67% | SKIP (exempt — no pixel-art rotation possible) |
| B05 | 400.1 | 215% | PASS — 215% |
| B06 | 127.3 | 69% | SKIP (exempt — no pixel-art rotation possible) |
| B07 | 129.0 | 69% | SKIP (exempt — no pixel-art rotation possible) |
| B08 | 130.1 | 70% | SKIP (exempt — no pixel-art rotation possible) |
| B09 | 129.4 | 70% | SKIP (exempt — no pixel-art rotation possible) |
| B10 | 127.8 | 69% | SKIP (exempt — no pixel-art rotation possible) |
| BVDT | 465.6 | 251% | PASS — 251% |
| BHTF | 548.4 | 295% | PASS — 295% |
| BOUT | 241.6 | 130% | PASS — 130% |
