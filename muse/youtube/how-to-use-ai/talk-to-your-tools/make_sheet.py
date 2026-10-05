#!/usr/bin/env python3
"""make_sheet.py — Talk to your tools (show-tell, Liam, Teardown).

Built from scratch 2026-10-04 for the humanitarians AI YouTube channel, general
audience (smart, pragmatic, not AI experts). Thesis: a connector is a plug
between Claude and one of your apps — grant it like a key, start read-only,
and keep the send button yours. Three automations worth setting up (morning
brief, inbox triage, meeting prep — the companion to the meetings-into-notes
film), and three warnings (never let it send unsupervised; smallest key, pull
unused plugs; delete strangers' invites).

Skill: show-tell (switched from the assigned cc-explainer; see BUILD-LOG.md —
cc-explainer's TERMINAL-FIRST/REAL-SESSION laws need a Claude Code terminal
session, which this film does not have).

Spine (show-tell): BIDEA hesitant writer -> BDEFS terms -> B00 the gap
(manual copying) -> B01 the plug (sign-in dance) -> B02 permissions (read is
looking, send is acting) -> B03 morning brief -> B04 inbox triage ->
B05 meeting prep -> B06 you send (the send button stays yours) ->
B07 pull the plug (least privilege) -> B08 strangers' invites ->
BHTF your-turn composer -> BOUT spoken outro.

Run: python3 make_sheet.py  (writes beat_sheet.json)
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "talk-to-your-tools"
TITLE = "Talk to your tools"
WPM = 150  # Kokoro estimate used by the sibling builds


def est(narration):
    return round(len(narration.split()) / (WPM / 60), 1)


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": est(narration),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image}}


B = [
    beat("B00",
         "Right now, Claude lives in a chat window, and your real life lives somewhere else "
         "\u2014 your inbox, your calendar. So you copy things over by hand: paste the email, "
         "paste the invite. Connectors end the copying. The chat reaches into your apps, and "
         "talks about what's actually in them.",
         "B00_TheGap",
         "The chat window left; an email card and a calendar page right. Two fragment cards "
         "slide from the apps into the composer (the copying); then a cable draws across the gap. "
         "Label 'the gap' beside the window.",
         [{"at": 0.1, "event": "window + apps land"},
          {"at": 0.35, "event": "fragments slide into the composer"},
          {"at": 0.8, "event": "cable draws across the gap"}]),
    beat("B01",
         "Here's how it works. You open your connectors settings, pick the app, and click "
         "connect. Then the app itself asks you to sign in \u2014 Google, Microsoft, whoever "
         "runs it. You never type your password into Claude. It's the same dance as logging "
         "into a new phone app with your Google account.",
         "B01_ThePlug",
         "The plug on its cable slides into the socket on the email app card; a shield with an "
         "ink check pops on the card (signed in). Label 'the plug' beside the card.",
         [{"at": 0.1, "event": "window + app card + plug land"},
          {"at": 0.35, "event": "plug slides into the socket"},
          {"at": 0.75, "event": "sign-in shield pops"}]),
    beat("B02",
         "Then comes the screen that matters most: permissions. It lists exactly what Claude "
         "may do \u2014 read your email, read your calendar, send email. Reading is looking; "
         "sending is acting. So grant the smallest key that works. Start read-only. You can "
         "always widen it later.",
         "B02_Permissions",
         "A permissions card; three rows land one by one ('read email', 'read calendar', "
         "'send email'); ink checks stamp the two read rows, an ink X stamps the send row. "
         "Label 'permissions' beside the card.",
         [{"at": 0.1, "event": "permissions card lands"},
          {"at": 0.3, "event": "'read email' + 'read calendar' rows + checks"},
          {"at": 0.7, "event": "'send email' row + X"}]),
    beat("B03",
         "Now the payoff. The first automation worth setting up: the morning brief. Every "
         "morning, you ask: what's my day, and what needs a reply? Claude reads your calendar "
         "and your unread email, and hands the day back in three lines \u2014 what's on, what "
         "needs you, what can wait.",
         "B03_MorningBrief",
         "The calendar page and the email card left; kraft lines draw to a brief card that "
         "grows right with three lines; three terracotta dots land. Label 'morning brief'.",
         [{"at": 0.1, "event": "calendar + email land"},
          {"at": 0.4, "event": "brief card grows"},
          {"at": 0.8, "event": "three terracotta dots land"}]),
    beat("B04",
         "The second: inbox triage. Point it at the pile and ask: what actually needs me? It "
         "sorts the real from the noise \u2014 the bill and the boss in one stack, newsletters "
         "and receipts in the other. You read what matters, and skip the rest.",
         "B04_InboxTriage",
         "The inbox card splits into two stacks: 'needs you' (ink lines) and 'noise' (dim "
         "lines); a terracotta check lands on the needs-you stack. Label 'triage'.",
         [{"at": 0.1, "event": "inbox card lands"},
          {"at": 0.35, "event": "inbox splits into two stacks"},
          {"at": 0.8, "event": "check lands on 'needs you'"}]),
    beat("B05",
         "The third is the companion to our meetings film. Before a call, ask: what do I need "
         "to know? It pulls the invite and the last thread with these people, and hands you a "
         "one-paragraph brief. You walk in already knowing the room.",
         "B05_MeetingPrep",
         "The calendar page and the email card left; a prep card grows right with paragraph "
         "lines and a terracotta dot. Label 'meeting prep'.",
         [{"at": 0.1, "event": "calendar + email land"},
          {"at": 0.45, "event": "prep card grows"},
          {"at": 0.8, "event": "terracotta dot lands"}]),
    beat("B06",
         "Now what to watch out for. The big one is sending. A draft is Claude guessing; a sent "
         "email is you acting. So let it write every draft it wants \u2014 but nothing leaves "
         "your outbox until your own eyes have read it. The send button stays yours.",
         "B06_YouSend",
         "A draft card grows; a big ink SEND pill lands beneath it; an ink lock lands over the "
         "pill. Label 'you send' beside the card.",
         [{"at": 0.1, "event": "draft card grows"},
          {"at": 0.45, "event": "SEND pill lands"},
          {"at": 0.75, "event": "lock lands over the pill"}]),
    beat("B07",
         "The second warning: give it the smallest key, and take keys back. If a job only "
         "needs reading, never grant sending. And every few months, open your connectors and "
         "pull the plugs you don't use anymore. An unused connection is an unlocked door.",
         "B07_PullThePlug",
         "The app card with the plug in its socket; the plug slides out along its cable and "
         "lands in a tray; a check stamps the tray. Label 'pull the plug'.",
         [{"at": 0.1, "event": "app card + plugged cable land"},
          {"at": 0.5, "event": "plug slides out into the tray"},
          {"at": 0.85, "event": "check stamps the tray"}]),
    beat("B08",
         "And one more, because nobody tells you this. Once it's connected, Claude reads "
         "everything in the app \u2014 including a calendar invite from a total stranger. And "
         "a stranger can hide instructions in an invite that try to steer the AI. So: a weird "
         "invite from someone you don't know? Don't accept it. Don't ask Claude about it. "
         "Delete it.",
         "B08_StrangerInvite",
         "A calendar invite card ('from: stranger') drops in; an ink X stamps it; the card "
         "slides off stage. Label \"strangers' invites\".",
         [{"at": 0.1, "event": "stranger invite drops in"},
          {"at": 0.6, "event": "ink X stamps the invite"},
          {"at": 0.85, "event": "card slides off stage"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": est(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
    remotion("BIDEA", "the question",
             "Hallo. This is Liam, in for Bear. Your inbox piles up, your calendar fills itself, "
             "and Claude can see none of it. The naive fix is to hand it your password. But the "
             "better question is the one on screen.",
             "BrutalistHesitantWriter",
             {"text": "How do I give Claude my passwords",
              "triggerWords": "give Claude my passwords",
              "replacementWords": "connect Claude to my tools safely",
              "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
              "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
             [{"at": 0.0, "event": "types 'How do I give Claude my passwords'"},
              {"at": 0.6, "event": "backspaces 'give Claude my passwords' -> 'connect Claude to my tools safely'"}],
             lead_silence_s=0.8,
             motion_claim="The writer types the naive password question and corrects it to the film's thesis: connect, don't hand over.",
             qc={"sparse_by_design": True,
                 "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion("BDEFS", "terms",
             "Three terms. A connector: the plug between Claude and one of your apps. Permissions: "
             "what you let it do \u2014 read, write, or send. An automation: a repeat job you hand "
             "it, like a morning email summary.",
             "ClaudeDefinitions",
             {"title": "Terms In This Film",
              "terms": [{"term": "connector", "meaning": "the plug between Claude and one of your apps"},
                        {"term": "permissions", "meaning": "what you let it do \u2014 read, write, or send"},
                        {"term": "automation", "meaning": "a repeat job you hand it, like a morning email summary"}],
              "folderLabel": "@NikBearBrown"},
             [{"at": 0.12, "event": "'connector' lands"}, {"at": 0.5, "event": "'permissions' lands"},
              {"at": 0.78, "event": "'automation' lands"}],
             gate="CARD",
             qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Look at my unread emails from this week and give me a three-line summary. "
             "Read only \u2014 do not send, reply, or change anything.")
YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. Connect one app \u2014 your email \u2014 and keep it read-only. Then paste "
    "this into Claude: " + YT_PROMPT +
    " Then check two things yourself. One: did anything leave your inbox? Open your sent "
    "folder \u2014 it should be empty. Two: open your connectors settings \u2014 does the "
    "email connection show read access only? If it shows send, disconnect it and reconnect "
    "with fewer permissions.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE \u00b7 YOUR TURN", "segment": "Talk to your tools",
     "command": YT_PROMPT, "runningText": "paste this into Claude\u2026",
     "output": ["Check: did anything leave your inbox? Open your sent folder \u2014 it should be empty.",
                "Check: open your connectors settings \u2014 does the email connection show read access only? "
                "If it shows send, disconnect and reconnect with fewer permissions."],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"},
     {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, "
                 "minimal labels, with the voice carrying the explanation. The negative space is the style, "
                 "so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0,
          "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own",
                   "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro",
                                "props": {"title": TITLE + ".", "slug": SLUG,
                                          "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE \u00b7 AT WORK",
    "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card "
                              "(Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like "
                              "tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; "
                              "spoken outro stays."),
    "audience": ("general audience \u2014 smart and pragmatic, not necessarily AI experts; "
                 "may never have connected an app to an AI chat tool"),
    "source_doc": ("built from scratch 2026-10-04; no mirror source. Companion to the "
                   "meetings-into-notes film (meeting prep beat B05). No real people's "
                   "names, no real company internals."),
    "playlist": "Getting started with Claude", "chapter_number": 0,
    "tags": ["connectors", "integrations", "email", "calendar", "Claude", "AI assistant",
             "automation", "permissions", "Nik Bear Brown"]},
    "beats": B}

if __name__ == "__main__":
    beats = sheet["beats"]
    # --- identity & count ---
    assert len(beats) == 13, f"expected 13 beats, got {len(beats)}"
    ids = [b["beat_id"] for b in beats]
    assert ids == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "B05", "B06", "B07",
                   "B08", "BHTF", "BOUT"], ids
    # --- duration band (~3:20-5:00; brief allows 3-6 min) ---
    total = sum(b["estimated_duration_s"] for b in beats)
    assert 200 <= total <= 300, f"total {total}s outside 3:20-5:00 band"
    # --- manim beats carry a scene class named for the beat ---
    for b in beats:
        if b["lane"] == "manim":
            cls = b["shot"]["manim"]["class"]
            assert cls.startswith(b["beat_id"] + "_"), f"{b['beat_id']}: class {cls}"
        assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
    # --- BIDEA hesitant-writer mechanics ---
    idea = next(b for b in beats if b["beat_id"] == "BIDEA")
    p = idea["shot"]["remotion"]["props"]
    assert p["triggerWords"] in p["text"], "trigger not verbatim in text"
    assert not p["triggerWords"][-1] in ".?!,;:", "trigger ends in punctuation"
    assert not p["replacementWords"][-1] in ".?!,;:", "replacement ends in punctuation"
    # --- BDEFS term length (ClaudeDefinitions truncates past ~17 chars) ---
    defs = next(b for b in beats if b["beat_id"] == "BDEFS")
    for t in defs["shot"]["remotion"]["props"]["terms"]:
        assert len(t["term"]) <= 17, f"term too long: {t['term']}"
    # --- BHTF composer contract ---
    htf = next(b for b in beats if b["beat_id"] == "BHTF")
    hp = htf["shot"]["remotion"]["props"]
    assert "YOUR TURN" in hp["topic"], "topic must contain YOUR TURN"
    assert hp["greeting"] == "Your turn."
    assert len(hp["output"]) == 2, "two viewer checks"
    assert hp["command"] in htf["narration_text"], "prompt must be read in full"
    # --- BOUT outro contract ---
    out = next(b for b in beats if b["beat_id"] == "BOUT")
    assert out["kind"] == "outro_voice" and out["tail_silence_s"] == 1.0
    assert out["narration_text"].endswith("At Nik Bear Brown.")
    # --- bookends ---
    assert sheet["metadata"]["bookend_exempt"] == ["cold-open", "bvdt"]
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
    print(f"beats={len(beats)} total={total:.1f}s (~{int(total//60)}m{int(total%60):02d}s)")
