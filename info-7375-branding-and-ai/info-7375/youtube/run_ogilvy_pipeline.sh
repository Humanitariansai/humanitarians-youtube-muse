#!/bin/bash
# Pipeline: audio + compile for all remaining Ogilvy reels
# Run from books/ dir: bash branding-and-ai/info-7375/youtube/run_ogilvy_pipeline.sh

set -e
BOOKS_DIR="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$BOOKS_DIR"
LOG="branding-and-ai/info-7375/youtube/pipeline.log"

log() { echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }

# Gayatri: just re-compile (audio already done, BOUT missing)
log "=== GAYATRI re-compile ==="
ART_FACTS=0 ART_STRICT=0 ./brutalist-art/art run branding-and-ai/info-7375/youtube/ogilvy-gayatri 2>&1 | tee -a "$LOG"
log "=== GAYATRI done ==="

for SLUG in kanishk vaibhav hammad denis xinchen satwika tanaka; do
  REEL="branding-and-ai/info-7375/youtube/ogilvy-$SLUG"
  log "=== $SLUG: audio ==="
  python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py "$REEL" --no-gate 2>&1 | tee -a "$LOG"
  log "=== $SLUG: compile ==="
  ART_FACTS=0 ART_STRICT=0 ./brutalist-art/art run "$REEL" 2>&1 | tee -a "$LOG"
  log "=== $SLUG done ==="
done

log "=== ALL DONE ==="
