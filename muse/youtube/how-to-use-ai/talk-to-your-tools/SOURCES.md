# SOURCES.md — Talk to your tools

## Source material (the film's argument)

Built from scratch 2026-10-04 — **no mirror source**. The thesis (a connector
is a plug between Claude and one of your apps; grant it like a key, start
read-only, keep the send button yours; three first automations — morning
brief, inbox triage, meeting prep — and three warnings — supervised sending,
least privilege, strangers' invites) was written for this film by the parent
orchestrator's brief and is craft advice, not sourced claims. Companion to
the existing film `meetings-into-notes` (the B05 meeting-prep beat).

## Fact-check sources (read 2026-10-04)

- Claude connectors for Google Workspace (Gmail, Calendar, Drive): what they
  are, per-chat toggles, citation-backed responses:
  https://agentandcopilot.com/ai-and-copilot/anthropic-connectors-integrate-google-productivity-apps-natively-into-claude/
- Connect flow (+ → Connectors → Manage connectors; sign in and authorize;
  Gmail/Calendar/Drive; official connectors for Todoist, Notion, Asana, Linear):
  https://mavgpt.ai/resources/five-things-to-build-with-claude-one-weekend-2026
- Step-by-step Google connect walkthrough (claude.ai → Settings →
  Connectors → Connect → sign in → Allow on each permissions screen):
  https://github.com/integralorg/claudecodesystem-cloud/blob/HEAD/.claude/commands/connect.md
- Connectors settings page and per-service connect model:
  https://github.com/pkozanian/chiefofstaff/blob/HEAD/src/brain/integrations/connectors.md
- Connectors directory UI (Settings → Connectors → Browse Connectors;
  permission screens for viewing/editing/managing):
  https://www.makeuseof.com/connect-claude-to-work-apps/
- Caution on the send function (risk of sending the wrong message /
  accidentally hitting send instead of saving a draft):
  https://github.com/pacascos/nate-ai-strategy/blob/HEAD/transcripts/N16_anthropic_didnt_build_browser_smarter.md
- Least-privilege guidance for AI app integrations (audit access, revoke
  unneeded capabilities, every integration expands the attack surface):
  reported via webpronews.com, Feb 2026 (URL not returned by search; claim
  text from the search snippet).
- Calendar-invite prompt injection against Claude (LayerX research:
  malicious Google Calendar event → Claude carries out embedded
  instructions):
  https://www.theregister.com/software/2026/02/11/claude-add-on-turns-google-calendar-into-malware-courier/4626517
- Zero-click calendar-event attack chain on Claude Desktop extensions:
  http://thehackernews.com/2026/02/threatsday-bulletin-ai-prompt-rce.html
- "Invitation Is All You Need" study (Aug 2025): calendar-invite titles
  hijacking a production AI assistant (14 indirect prompt-injection attacks
  demonstrated):
  https://forkast.news/your-calendar-might-be-the-most-dangerous-thing-in-your-smart-home/

## Toolkit

- `~/workspace/brutalist.art/` — show-tell skill (`skills/make/show-tell/SKILL.md`),
  iso kit (`skills/make/show-tell/templates/iso_kit.py`, pasted verbatim into
  scenes.py via the sibling build), static QC (`runtime/qc/static_scene_check.py`).

## Rights / provenance

All visuals are original Manim drawings in the Claude palette; no stock,
no screenshots, no third-party assets. No real people's names, no real
company internals. No rights clearance needed.
