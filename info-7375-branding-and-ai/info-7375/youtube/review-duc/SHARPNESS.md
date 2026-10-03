# SHARPNESS GATE — review-duc

Compiled master: `review-duc-slate.mp4`
Median Laplacian variance: **390.4**
Failure threshold: 195.2 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 498.0 | 128% | PASS — 128% |
| B01 | 127.1 | 33% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 390.3 | 100% | PASS — 100% |
| B03 | 392.2 | 100% | PASS — 100% |
| B04 | 392.2 | 100% | PASS — 100% |
| B05 | 127.3 | 33% | SKIP (exempt — no pixel-art rotation possible) |
| B06 | 390.6 | 100% | PASS — 100% |
| B07 | 128.3 | 33% | SKIP (exempt — no pixel-art rotation possible) |
| B08 | 130.6 | 33% | SKIP (exempt — no pixel-art rotation possible) |
| B09 | 129.2 | 33% | SKIP (exempt — no pixel-art rotation possible) |
| B10 | 401.0 | 103% | PASS — 103% |
| BVDT | 464.3 | 119% | PASS — 119% |
| BHTF | 568.9 | 146% | PASS — 146% |
| BOUT | 225.3 | 58% | PASS — 58% |
