# Push. Tag. Live.

**Skill:** cli-explainer (`--tool github`) · **Voice:** am_onyx (Darshil) · **Duration:** ~4 min (16 beats) · **Status:** rendered (final cut + slate produced)
**Destination:** `darshil-s/2026-08-25-medas-frontend-cicd`

## About this video

`medas-aggregation-frontend` is the React/Vite frontend for an AI-assisted
diagnostic tool doctors use to review sepsis and diagnosis output. Developers
were pushing code to it, but nothing built, containerized, or hosted it —
every deploy was a manual build on someone's machine.

The video covers, in order: (1) the complete GCP setup — Artifact Registry,
finding and widening the backend's existing Workload Identity Federation
provider, granting the frontend repo impersonation rights on the shared
service account, and the GitHub Environment secrets/variables that tie it
together; (2) the app's own structure — an auth-gated React UI with
sepsis/diagnosis review components; (3) the pivot — trust chain and app both
ready, but no pipeline existed — and the tag-based CI/CD pipeline (a two-stage
Docker build, GitHub Actions workflow, deploy to Cloud Run) designed to close
that gap.

Every command, file, and config value shown is drawn directly from the real
setup work (`DEPLOY.md`, `Dockerfile`, `.github/workflows/deploy.yaml`, and the
app's own source tree) — no placeholder-typo narrative, no screen recordings;
every visual is a native Remotion reconstruction of the real material.

## File structure

```
2026-08-25-medas-frontend-cicd/
└── beat_sheet.json   — the full beat sheet: narration + Remotion scene config
                         generate_audio_kokoro.py and ./art run read
```

Rendered media (mp3/, media/, clips/, mp4/, qc frames) are produced locally by
the rebuild steps below and are not checked into this repo (gitignored, same
as elsewhere in this repo).

## Rebuilding this video

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
python3 runtime/scripts/generate_audio_kokoro.py ../humanitarians-youtube/fellows/darshil-s/2026-08-25-medas-frontend-cicd
./art run   ../humanitarians-youtube/fellows/darshil-s/2026-08-25-medas-frontend-cicd
./art final ../humanitarians-youtube/fellows/darshil-s/2026-08-25-medas-frontend-cicd
```

Rendered locally at 3840x2160 (4K), free — Kokoro TTS + Remotion, no paid services.
