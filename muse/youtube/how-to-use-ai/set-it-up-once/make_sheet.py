#!/usr/bin/env python3
"""make_sheet.py — Set it up once (Humanitarians AI YouTube film, #23 of 24).

Builds beat_sheet.json: 13 beats, show-tell spine (hesitant writer -> terms
-> the annoyance -> the note -> where it lives -> good lines -> bad lines ->
payoff demo -> never-lines -> keep it fresh -> follows you -> your turn ->
outro). Skill: show-tell. Persona: Liam, in for Bear. TTS: Kokoro am_onyx.
Register: Teardown. Channel: claude-liam. Watermark: @NikBearBrown.

Source: NEW — built from scratch (no mirror source). Facts verified
2026-10-03: ChatGPT Custom Instructions, Claude Personal Preferences,
Gemini Instructions for Gemini (see FACTCHECK.md). All UI described
generically so the film doesn't rot.

Run: python3 make_sheet.py   (writes beat_sheet.json in cwd)
Durations: ~150 wpm narration => words/2.5 + small pause, rounded.
"""
import json

SLUG = "set-it-up-once"
TITLE = "Set it up once"


def manim(beat_id, cls, show_events, sparse_reason=None):
    shot = {"type": "MANIM", "manim": {"class": cls},
            "show": [{"at": at, "event": ev} for at, ev in show_events]}
    if sparse_reason:
        shot["qc"] = {"sparse_by_design": True, "sparse_reason": sparse_reason}
    return shot


B = [
    {
        "beat_id": "BIDEA", "act": "the question", "lane": "bookend",
        "proof_gate": "SHOW",
        "narration_text": ("Hallo. This is Liam, in for Bear. You asked: why does "
                           "the AI forget everything between chats? Wrong question. "
                           "A new chat is supposed to start fresh. The real question "
                           "is: how do I make every chat start already knowing me?"),
        "estimated_duration_s": 17, "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "REMOTION", "source": "own",
            "show": [
                {"at": 0.0, "event": "types 'Why does the AI forget everything between chats?'"},
                {"at": 0.6, "event": "backspaces 'forget everything between chats' -> 'start every chat already knowing me' on the spoken correction"}],
            "remotion": {
                "pattern": "BrutalistHesitantWriter",
                "props": {
                    "text": "Why does the AI\nforget everything\nbetween chats?",
                    "triggerWords": "forget everything between chats",
                    "replacementWords": "start every chat already knowing me",
                    "fontSize": 70, "charMs": 22, "hesitateBetween": 6,
                    "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
                    "seed": "set-it-up-once", "banner": ""}}},
        "lead_silence_s": 0.8,
        "motion_claim": ("The writer types the naive forget-between-chats question "
                         "and corrects it to the real one: start every chat already knowing me."),
        "qc": {"sparse_by_design": True,
               "sparse_reason": "Hesitant-writer bookend: the correction is the motion."},
    },
    {
        "beat_id": "BDEFS", "act": "terms", "lane": "bookend",
        "proof_gate": "CARD",
        "narration_text": ("Three terms you'll hear. Instructions: saved lines the app "
                           "reads before every chat. Memory: things the AI itself saves "
                           "from your chats. And preferences: your standing answers — "
                           "tone, format, how much you already know."),
        "estimated_duration_s": 15, "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "REMOTION", "source": "own",
            "show": [
                {"at": 0.12, "event": "'instructions' lands"},
                {"at": 0.5, "event": "'memory' lands"},
                {"at": 0.78, "event": "'preferences' lands"}],
            "remotion": {
                "pattern": "ClaudeDefinitions",
                "props": {
                    "title": "Terms In This Film",
                    "terms": [
                        {"term": "instructions",
                         "meaning": "saved lines the app reads before every chat"},
                        {"term": "memory",
                         "meaning": "things the AI itself saves from your chats"},
                        {"term": "preferences",
                         "meaning": "your standing answers: tone, format, skill level"}],
                    "folderLabel": "@NikBearBrown"}}},
        "qc": {"sparse_by_design": True,
               "sparse_reason": "TERMS card: three prerequisites, one line each."},
    },
    {
        "beat_id": "B00", "act": "the problem", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("Meet the annoyance. You open the AI and ask: explain "
                           "p-values. Back comes a wall of technical jargon. You're a "
                           "beginner at statistics, but the AI doesn't know that. This "
                           "chat started five seconds ago — so you explain yourself. Again."),
        "estimated_duration_s": 18, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B00", "B00_Repeat", [
            (0.05, "chat window fades in with a 'one chat' label"),
            (0.30, "user bubble 'explain p-values' lands"),
            (0.50, "the jargon answer lands line by line"),
            (0.80, "a loop arrow draws and the 'again?' label lands")],
            "show-tell body beat: one window, one exchange, one loop"),
        "motion_claim": "The jargon answer lands on a stranger chat, then the loop arrow closes the repeat.",
    },
    {
        "beat_id": "B01", "act": "the setting", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("Now the fix. Most AI apps have a settings page where you can "
                           "write a few lines about yourself — your standing instructions. "
                           "The app pins that note to every new chat. It's like a cover "
                           "page the AI reads before it ever sees your question."),
        "estimated_duration_s": 19, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B01", "B01_TheNote", [
            (0.05, "settings panel fades in with a 'settings' label"),
            (0.30, "the note drops into the panel and the terracotta pin lands"),
            (0.60, "two chat windows fade in on the right"),
            (0.80, "kraft cables draw from the note to each window; 'every chat' lands")],
            "show-tell body beat: the pinned note joins the cast"),
        "motion_claim": "The note drops into settings, gets pinned, and cables it to every chat.",
    },
    {
        "beat_id": "B02", "act": "the setting", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("Where is it? Open your AI app's settings, or your profile "
                           "page. Look for words like instructions, personalization, or "
                           "memory. Every app names it differently and moves it around — "
                           "so search for the word, not the button."),
        "estimated_duration_s": 16, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B02", "B02_WhereItLives", [
            (0.05, "settings panel close-up fades in"),
            (0.30, "three keyword pills land: instructions / personalization / memory"),
            (0.60, "the cursor hovers onto the 'instructions' pill"),
            (0.80, "a terracotta check lands; 'look for these words' label lands")],
            "show-tell body beat: one panel, three words, one choice"),
        "motion_claim": "The cursor picks 'instructions' out of the three candidate words.",
    },
    {
        "beat_id": "B03", "act": "the note", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("What do you write? Good instructions are short and concrete. "
                           "Three to five lines, each one a standing answer. Keep answers "
                           "short. I'm a beginner at statistics. Plain English, no jargon. "
                           "Give me steps I can try today."),
        "estimated_duration_s": 17, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B03", "B03_GoodLines", [
            (0.05, "the pinned note fades in with 'the note' label"),
            (0.25, "'keep answers short' writes in with its bullet"),
            (0.45, "'beginner at statistics' writes in with its bullet"),
            (0.65, "'plain English, no jargon' writes in with its bullet"),
            (0.85, "'steps I can try today' writes in with its bullet")],
            "show-tell body beat: the note fills with four short lines"),
        "motion_claim": "Four concrete lines write themselves onto the note, one per spoken line.",
    },
    {
        "beat_id": "B04", "act": "the note", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("Bad instructions are a life story — the AI can't use your "
                           "biography. Or they contradict themselves: be brief, and "
                           "explain everything. Two orders that fight. The AI can't obey "
                           "both — so give it one rule per line."),
        "estimated_duration_s": 17, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B04", "B04_BadNote", [
            (0.05, "the note fades in again, labelled 'the note'"),
            (0.30, "dim scribble lines fill the page and spill off its edge"),
            (0.60, "the 'be brief!' and 'explain everything!' pills land below"),
            (0.80, "a terracotta X lands between the two pills")],
            "show-tell body beat: overflow plus one contradiction"),
        "motion_claim": "The life story spills off the page; the two orders collide on the X.",
    },
    {
        "beat_id": "B05", "act": "payoff", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("The payoff. Same question, two chats. Without the note: a wall "
                           "of jargon. With the note: short, plain, no jargon — written "
                           "for a beginner. You wrote four lines once. Every chat after "
                           "that starts informed."),
        "estimated_duration_s": 16, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B05", "B05_Payoff", [
            (0.05, "the 'same question' bar types in on top"),
            (0.25, "both chat windows fade in below, labelled"),
            (0.50, "the jargon answer lands in the left window"),
            (0.70, "the pinned note lands on the right window; the plain answer lands"),
            (0.88, "a terracotta check lands on the right window")],
            "show-tell body beat: two panels, one difference"),
        "motion_claim": "The same question gets two answers; the note is the only difference.",
    },
    {
        "beat_id": "B06", "act": "keep it", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("One more kind of line: what you never want. No emojis. No 'as "
                           "an AI language model.' Don't open with an apology. The AI's "
                           "habits are yours to set — write down the ones you don't like, "
                           "and they're gone."),
        "estimated_duration_s": 17, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B06", "B06_NeverWant", [
            (0.05, "the pinned note fades in with 'the note' label"),
            (0.30, "'no emojis' lands and is crossed with a terracotta X"),
            (0.55, "'no as an AI' lands and is crossed with a terracotta X"),
            (0.80, "'no sorry-first opens' lands and is crossed with a terracotta X")],
            "show-tell body beat: three bans, three crosses"),
        "motion_claim": "Three unwanted habits are written down and crossed out.",
    },
    {
        "beat_id": "B07", "act": "keep it", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("One last thing: it's not set-and-forget. Your needs change, "
                           "so the note can change. Pull it out, rewrite a line, pin it "
                           "back. Review it every few months — or the day the answers "
                           "start feeling off."),
        "estimated_duration_s": 16, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B07", "B07_KeepFresh", [
            (0.05, "the pinned note fades in with three lines"),
            (0.30, "the note lifts out; the pencil appears"),
            (0.55, "'beginner at statistics' is replaced by 'comfortable with basics'"),
            (0.80, "the 'every few months' pill lands; the note pins back down")],
            "show-tell body beat: the note is edited, not replaced"),
        "motion_claim": "One line is rewritten and the note pins back into place.",
    },
    {
        "beat_id": "B08", "act": "keep it", "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": ("And the note follows you. Same instructions on your phone and "
                           "your computer — wherever you open the app. One setting, "
                           "written once, shaping every chat you ever start."),
        "estimated_duration_s": 13, "voice": "am_onyx", "engine": "kokoro",
        "shot": manim("B08", "B08_FollowsYou", [
            (0.05, "the pinned note fades in at center"),
            (0.35, "the phone and the web window fade in left and right"),
            (0.65, "kraft cables draw from the note to both devices")],
            "show-tell body beat: one note, two devices"),
        "motion_claim": "The same note feeds the phone and the computer.",
    },
    {
        "beat_id": "BHTF", "act": "your turn", "lane": "bookend",
        "proof_gate": "SHOW",
        "narration_text": ("Your turn. Open your AI app's settings and find the "
                           "instructions page. Then paste this in: I like answers that "
                           "are short and practical. I'm a beginner at statistics, so "
                           "explain terms in plain English. No jargon, no filler. Run it "
                           "on your next question — and notice: the AI is meeting the "
                           "informed version of you."),
        "estimated_duration_s": 25, "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "REMOTION", "source": "own",
            "show": [
                {"at": 0.0, "event": "Composer opens — 'Your turn.'"},
                {"at": 0.1, "event": "the prompt types in full"},
                {"at": 0.8, "event": "two check lines land"}],
            "remotion": {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "greeting": "Your turn.",
                    "topic": "AI · YOUR TURN",
                    "segment": "Set It Up Once",
                    "command": ("I like answers that are short and practical. I'm a "
                                "beginner at statistics, so explain terms in plain "
                                "English. No jargon, no filler."),
                    "runningText": "paste this into your AI…",
                    "output": [
                        "Check: your next answer is shorter than the last one.",
                        "Check: no term went unexplained."],
                    "folderLabel": "@NikBearBrown"}}},
    },
    {
        "beat_id": "BOUT", "act": "outro", "lane": "bookend",
        "proof_gate": "SHOW",
        "narration_text": "Set it up once. At Nik Bear Brown.",
        "estimated_duration_s": 5, "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "REMOTION", "source": "own",
            "show": [{"at": 0.0, "event": "title restates; handle"}],
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {
                    "title": "Set it up once",
                    "slug": "set-it-up-once",
                    "handle": "@NikBearBrown",
                    "subline": "Teach it once. Every chat starts informed."}}},
        "kind": "outro_voice",
        "tail_silence_s": 1.0,
    },
]

METADATA = {
    "slug": SLUG, "title": TITLE, "topic": "AI · CUSTOM INSTRUCTIONS",
    "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "watermark": "@NikBearBrown",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell style (Bear, 2026-09-26): opens on the "
                              "hesitant writer + terms card, no verdict card; "
                              "Your Turn is the composer; spoken outro stays."),
    "audience": ("smart general audience — pragmatic, not necessarily AI "
                 "experts; every term explained"),
    "source_doc": "NEW — built from scratch 2026-10-03 (no mirror source); "
                  "facts verified 2026-10-03, see FACTCHECK.md",
    "playlist": "How to use AI", "chapter_number": 23,
    "tags": ["custom instructions", "personalization", "ChatGPT", "Claude",
             "Gemini", "how to use AI", "Nik Bear Brown"],
}

if __name__ == "__main__":
    ids = [b["beat_id"] for b in B]
    assert ids == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "B05",
                   "B06", "B07", "B08", "BHTF", "BOUT"], ids
    assert len(B) == 13, len(B)
    assert sum(1 for b in B if b["lane"] == "manim") == 9, "expected 9 manim body beats"
    assert sum(1 for b in B if b["lane"] == "bookend") == 4, "expected 4 bookends"
    total = sum(b["estimated_duration_s"] for b in B)
    assert 200 <= total <= 320, f"total duration {total}s outside 200-320s band"
    for b in B:
        assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
        assert b["voice"] == "am_onyx" and b["engine"] == "kokoro", \
            f"{b['beat_id']}: voice/engine"
        assert b["shot"]["show"], f"{b['beat_id']}: no show block"
        if b["lane"] == "manim":
            cls = b["shot"]["manim"]["class"]
            assert cls.startswith(b["beat_id"] + "_"), \
                f"{b['beat_id']}: class {cls} must start with beat id"
    # IN-FOR-BEAR law
    assert "Liam, in for Bear" in B[0]["narration_text"], "name the voice"
    # BIDEA trigger contract: trigger appears verbatim in text; neither ends in punctuation
    _tp = B[0]["shot"]["remotion"]["props"]
    assert _tp["triggerWords"] in _tp["text"].replace("\n", " "), \
        "triggerWords not verbatim in text"
    assert _tp["triggerWords"][-1] not in ".?!" and \
        _tp["replacementWords"][-1] not in ".?!", \
        "trigger/replacement must not end in punctuation"
    # BDEFS term-length contract (ClaudeDefinitions truncates past ~17 chars)
    for t in B[1]["shot"]["remotion"]["props"]["terms"]:
        assert len(t["term"]) <= 17, f"BDEFS term too long: {t['term']!r}"
    # BHTF prompt contract: the command is read in full in the narration
    _htf = next(b for b in B if b["beat_id"] == "BHTF")
    assert _htf["shot"]["remotion"]["props"]["command"] in \
        _htf["narration_text"], "BHTF prompt not read in full"
    # BOUT outro contract
    _out = next(b for b in B if b["beat_id"] == "BOUT")
    assert _out["kind"] == "outro_voice" and _out["tail_silence_s"] == 1.0, \
        "BOUT must be outro_voice with 1.0s tail"
    sheet = {"metadata": METADATA, "beats": B}
    with open("beat_sheet.json", "w") as f:
        json.dump(sheet, f, indent=2, ensure_ascii=False)
    print(f"beats={len(B)} manim=9 bookends=4 total={total}s "
          f"(~{total//60}m{total%60:02d}s)")
