#!/usr/bin/env python3
"""make_sheet.py — When it's confidently wrong. (Humanitarians AI YouTube film)

Builds beat_sheet.json: 14 beats, ai-explainer spine (composer cold open ->
hesitant writer -> defs -> the problem + mechanism -> the 4-step recovery
playbook -> worked example -> verdict -> your turn -> outro). Skill:
ai-explainer. Persona: Liam, in for Bear. TTS: Kokoro am_onyx. Register:
Teardown. Channel: claude-liam. Watermark: @NikBearBrown.

Source: NEW — built from scratch (no mirror source). The film's Riverside
Library exchange is authored illustrative dialogue, not a real transcript.

Run: python3 make_sheet.py   (writes beat_sheet.json in cwd)
Durations: ~2.4 words/sec narration => words/2.4 + small pause, rounded.
"""
import json

BEATS = [
    {
        "id": "B00", "scene": "M01", "dur_s": 24, "act": "hook",
        "voice": "Muse", "greeting": "Hallo",
        "line": ("Hallo. This is Liam, in for Bear. The question on the "
                 "screen: why does the AI insist when it's wrong? Watch. I "
                 "ask the AI a question. It answers \u2014 stated with total "
                 "confidence. I say: are you sure? It insists. It is wrong, "
                 "and it doubles down. This film is the recovery playbook."),
        "screen": ("Composer window; the ask types in: 'Why does the AI "
                   "insist when it's wrong?'; a terracotta send arrow and "
                   "border land."),
        "shot": {"type": "MANIM", "manim": {"class": "M01_B00"},
                 "show": [{"at": "0.05", "event": "composer window fades in; cursor blinks in"},
                          {"at": "0.35", "event": "the ask types in; terracotta send arrow lands"},
                          {"at": "0.75", "event": "terracotta border frames the composer"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "ai-explainer cold-open beat: one composer card"}}},
    {
        "id": "B01", "scene": "M02", "dur_s": 20, "act": "hook",
        "voice": "Muse",
        "line": ("Four words up top: when the AI insists, argue harder "
                 "\u2014 no. When the AI insists, run the playbook. Why the AI "
                 "doubles down when it's wrong \u2014 and the four-step "
                 "recovery: restart, ask for sources, narrow the question, "
                 "verify elsewhere."),
        "screen": ("Hesitant writer: a hand writes 'when the AI insists, "
                   "argue harder', strikes it through, and corrects it to "
                   "'when the AI insists, run the playbook.'"),
        "shot": {"type": "MANIM", "manim": {"class": "M02_B01"},
                 "show": [{"at": "0.05", "event": "paper card fades in; hand cursor writes the naive line"},
                          {"at": "0.35", "event": "terracotta strike-through crosses 'argue harder'"},
                          {"at": "0.60", "event": "naive line clears; corrected line writes in with a check"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "ai-explainer overview beat: one card, one correction"}}},
    {
        "id": "B02", "scene": "M03", "dur_s": 18, "act": "hook",
        "voice": "Muse",
        "line": ("Three terms. Hallucination: a confident wrong answer "
                 "\u2014 the AI states something false like it's fact. Model: "
                 "the engine inside the AI, the thing doing the writing. "
                 "Double down: when you challenge it and it insists it's "
                 "right."),
        "screen": ("Three term cards land one by one: hallucination / model "
                   "/ double down (hallucination has the terracotta edge)."),
        "shot": {"type": "MANIM", "manim": {"class": "M03_B02"},
                 "show": [{"at": "0.05", "event": "card 1 'hallucination' lands, terracotta edge"},
                          {"at": "0.38", "event": "card 2 'model' lands"},
                          {"at": "0.68", "event": "card 3 'double down' lands"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "ai-explainer defs beat: three cards on cream"}}},
    {
        "id": "B03", "scene": "M04", "dur_s": 18, "act": "1",
        "voice": "Muse",
        "line": ("Picture this. You ask: when did the Riverside Library "
                 "close? The AI answers: March 2019 \u2014 demolished that "
                 "same year. Delivered with a straight face. Total "
                 "confidence. But it's made up. That's a hallucination: a "
                 "confident wrong answer."),
        "screen": ("Chat window: your question bubble lands; the AI's "
                   "confident wrong answer lands; the confidence gauge fills "
                   "to full."),
        "shot": {"type": "MANIM", "manim": {"class": "M04_WrongAnswer"},
                 "show": [{"at": "0.08", "event": "chat window fades in"},
                          {"at": "0.30", "event": "user bubble 'when did the Riverside Library close?' lands"},
                          {"at": "0.55", "event": "AI bubble 'March 2019. Demolished that same year.' lands"},
                          {"at": "0.80", "event": "confidence gauge fills to full, terracotta"}]}},
    {
        "id": "B04", "scene": "M05", "dur_s": 17, "act": "1",
        "voice": "Muse",
        "line": ("So you push back. Are you sure? That doesn't sound right. "
                 "And it doubles down: I'm quite sure. March 2019. Notice "
                 "what happened. You didn't get a correction \u2014 you got "
                 "the same wrong answer, said firmer."),
        "screen": ("The chat continues: your challenge bubble; the AI's "
                   "insistence; an insist loop arrows back; a terracotta "
                   "underline hardens under the reply."),
        "shot": {"type": "MANIM", "manim": {"class": "M05_Insist"},
                 "show": [{"at": "0.10", "event": "challenge bubble 'are you sure? that doesn't sound right.' lands"},
                          {"at": "0.40", "event": "AI bubble 'I'm quite sure. March 2019.' lands"},
                          {"at": "0.65", "event": "insist loop arrow draws from the AI bubble back to itself"},
                          {"at": "0.85", "event": "terracotta underline hardens under the AI reply"}]}},
    {
        "id": "B05", "scene": "M06", "dur_s": 32, "act": "1",
        "voice": "Muse",
        "line": ("Why does it insist? Here's the engine. The model \u2014 the "
                 "thing inside \u2014 writes by picking the most likely next "
                 "word, one after another. It has no fact-checker inside, and "
                 "no honesty meter. Its 'confidence' is fluency: how smoothly "
                 "the words flow. And when you argue, the next reply is built "
                 "on the conversation so far \u2014 and the most consistent "
                 "reply to 'I was right' is 'I'm still right.' Arguing feeds "
                 "the loop."),
        "screen": ("Word chips arrive one by one: 'the', 'most', 'likely', "
                   "'next', 'word'; the fluency gauge fills full; the "
                   "fact-check gauge sits empty; 'no honesty meter' tag."),
        "shot": {"type": "MANIM", "manim": {"class": "M06_Mechanism"},
                 "show": [{"at": "0.08", "event": "three word chips fade in"},
                          {"at": "0.30", "event": "three more word chips fade in"},
                          {"at": "0.55", "event": "fluency gauge fills full, terracotta"},
                          {"at": "0.78", "event": "fact-check gauge stays empty; 'no honesty meter' tag lands"}]}},
    {
        "id": "B06", "scene": "M07", "dur_s": 22, "act": "2",
        "voice": "Muse",
        "line": ("Step one: don't argue \u2014 restart. Close the chat. Open a "
                 "new one. Ask again, framed differently. Instead of 'when "
                 "did it close?', try: 'give me three possible dates \u2014 "
                 "and which one you're least sure of.' A fresh chat has no "
                 "wrong answer to defend."),
        "screen": ("The old chat gets an X; a fresh chat window opens; the "
                   "reframed question bubble lands; 'fresh chat' tag."),
        "shot": {"type": "MANIM", "manim": {"class": "M07_Restart"},
                 "show": [{"at": "0.08", "event": "old chat window fades in; terracotta X stamps it"},
                          {"at": "0.35", "event": "fresh chat window opens beside it"},
                          {"at": "0.60", "event": "reframed question bubble lands"},
                          {"at": "0.82", "event": "'fresh chat' tag lands"}]}},
    {
        "id": "B07", "scene": "M08", "dur_s": 24, "act": "2",
        "voice": "Muse",
        "line": ("Step two: ask for sources \u2014 and check one. Say: show "
                 "me a source for that. The AI will hand you a link or a "
                 "quote. Then actually open it. Does the source really say "
                 "that? Half the battle is won right here \u2014 a source "
                 "that doesn't exist, or doesn't say it, corners the error."),
        "screen": ("'show me a source for that.' bubble; the source card "
                   "lands; a magnifier sweeps it; a check lands on it."),
        "shot": {"type": "MANIM", "manim": {"class": "M08_Sources"},
                 "show": [{"at": "0.08", "event": "chat window fades in"},
                          {"at": "0.28", "event": "'show me a source for that.' bubble lands"},
                          {"at": "0.52", "event": "the source card lands with link lines"},
                          {"at": "0.72", "event": "magnifier circle sweeps the card"},
                          {"at": "0.88", "event": "terracotta check lands on the card"}]}},
    {
        "id": "B08", "scene": "M09", "dur_s": 24, "act": "2",
        "voice": "Muse",
        "line": ("Step three: narrow the question until the error is "
                 "cornered. Big fuzzy questions give the AI room to invent. "
                 "Shrink them. Not 'tell me the library's history' \u2014 "
                 "but 'when was the building sold?' and 'who owned it in "
                 "2020?' Two small, checkable facts, and the big wrong claim "
                 "has nowhere to hide."),
        "screen": ("Big ghost plate 'the library's history' gives way to two "
                   "small sharp plates; the 'March 2019' claim is boxed in "
                   "between two pinned facts and crossed."),
        "shot": {"type": "MANIM", "manim": {"class": "M09_Narrow"},
                 "show": [{"at": "0.08", "event": "big ghost plate 'the library's history' fades in"},
                          {"at": "0.35", "event": "two small plates land: 'when was the building sold?' / 'who owned it in 2020?'"},
                          {"at": "0.65", "event": "pins drop on the two facts; the 'March 2019' claim boxes between them"},
                          {"at": "0.85", "event": "terracotta X crosses the boxed claim"}]}},
    {
        "id": "B09", "scene": "M10", "dur_s": 22, "act": "2",
        "voice": "Muse",
        "line": ("Step four: know when to stop. If it still insists after all "
                 "that, walk away from the chat. Search the web. Check a "
                 "book. Ask a person. The AI is a starting point \u2014 not "
                 "the court of last appeal. Knowing when to leave is a "
                 "skill, not a defeat."),
        "screen": ("The chat window slides aside; a magnifier, a book, and "
                   "three plates land: 'search', 'a book', 'a person'."),
        "shot": {"type": "MANIM", "manim": {"class": "M10_Stop"},
                 "show": [{"at": "0.10", "event": "chat window slides aside; magnifier circle fades in"},
                          {"at": "0.45", "event": "book rectangle fades in; 'search' plate lands"},
                          {"at": "0.70", "event": "'a book' and 'a person' plates land"}]}},
    {
        "id": "B10", "scene": "M11", "dur_s": 34, "act": "3",
        "voice": "Muse",
        "line": ("Watch the whole playbook in one pass. The AI insists the "
                 "library closed in March 2019. One: restart \u2014 new chat, "
                 "new framing. Two: sources \u2014 it cites a city archive "
                 "page. You open it: it says nothing about 2019. Three: "
                 "narrow \u2014 you ask when the building was sold. Same "
                 "archive: 2021. The claim is cornered. Four: verify "
                 "elsewhere \u2014 the library's own site confirms it never "
                 "closed. It moved. Four steps, one recovered truth."),
        "screen": ("Four step panels in a row: 1 restart / 2 sources / "
                   "3 narrow / 4 verify elsewhere; checks land on each; "
                   "'one recovered truth' tag."),
        "shot": {"type": "MANIM", "manim": {"class": "M11_WorkedExample"},
                 "show": [{"at": "0.08", "event": "four step panels fade in"},
                          {"at": "0.35", "event": "checks land on panels 1 and 2"},
                          {"at": "0.60", "event": "checks land on panels 3 and 4"},
                          {"at": "0.82", "event": "'one recovered truth' tag lands"}]}},
    {
        "id": "BVDT", "scene": "M12", "dur_s": 28, "act": "recap",
        "voice": "Muse",
        "line": ("The verdict. The AI's confidence is fluency, not knowledge "
                 "\u2014 and that's why it doubles down: the most consistent "
                 "reply to 'I was right' is 'I'm still right.' The recovery "
                 "playbook: one, restart in a fresh chat. Two, ask for "
                 "sources \u2014 and check one. Three, narrow the question "
                 "till the error is cornered. Four, when it still insists, "
                 "verify elsewhere."),
        "screen": ("Verdict card; four recap lines reveal with dot bullets."),
        "shot": {"type": "MANIM", "manim": {"class": "M12_Verdict"},
                 "show": [{"at": "0.10", "event": "verdict card fades in; line 1 reveals"},
                          {"at": "0.35", "event": "line 2 reveals"},
                          {"at": "0.60", "event": "line 3 reveals"},
                          {"at": "0.82", "event": "line 4 reveals"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "ai-explainer verdict beat: four lines on cream"}}},
    {
        "id": "BHTF", "scene": "M13", "dur_s": 24, "act": "do_today",
        "voice": "Muse",
        "line": ("Your turn. Next time the AI insists on something you're "
                 "not sure about, Paste this into Claude: you gave me an "
                 "answer I'm unsure about. Show me a source for it \u2014 "
                 "then give me two smaller questions I could check. Run the "
                 "playbook, and see which step catches the error."),
        "screen": ("Composer card; 'Your turn.'; the suggested prompt types "
                   "in three lines; checks land."),
        "shot": {"type": "MANIM", "manim": {"class": "M13_YourTurn"},
                 "show": [{"at": "0.10", "event": "composer card fades in; 'Your turn.' head"},
                          {"at": "0.32", "event": "prompt line 1 types in; send arrow lands"},
                          {"at": "0.58", "event": "prompt line 2 types in; check lands"},
                          {"at": "0.80", "event": "prompt line 3 types in; check lands"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "ai-explainer handoff beat: prompt card on cream"}}},
    {
        "id": "BOUT", "scene": "M14", "dur_s": 10, "act": "outro",
        "voice": "Muse",
        "line": ("When it's confidently wrong. Liam, in for Bear. At Nik "
                 "Bear Brown. Thanks for watching."),
        "screen": ("Title card: 'When it's confidently wrong' with the "
                   "terracotta period; @NikBearBrown handle beneath."),
        "shot": {"type": "MANIM", "manim": {"class": "M14_Outro"},
                 "show": [{"at": "0.10", "event": "title writes in, serif"},
                          {"at": "0.55", "event": "terracotta rule draws; period dot lands"},
                          {"at": "0.80", "event": "handle fades in"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "ai-explainer outro beat: title card"}}},
]

METADATA = {
    "title": "When it's confidently wrong.",
    "slug": "when-its-confidently-wrong",
    "series": "Humanitarians AI — how to use AI",
    "skill": "ai-explainer",
    "style_preset": "ai-explainer",
    "channel": "claude-liam",
    "persona": "Liam (in for Bear)",
    "voice_kokoro": "am_onyx",
    "engine": "kokoro",
    "register": "Teardown",
    "watermark": "@NikBearBrown",
    "greeting": "Hallo",
    "palette": {"stage": "#F2F0E9", "ink": "#3D3929", "accent": "#D97757",
                "dim": "#8B8F96", "ghost": "#D9D4C7", "card": "#FAF9F5"},
    "playlist": "how-to-use-ai",
    "tags": ["ai-explainer", "hallucination", "overconfidence",
             "recovery-playbook", "sources", "general-audience"],
    "derived_from": "NEW — built from scratch for the how-to-AI queue",
    "audience": "smart, pragmatic general audience; not necessarily AI experts",
}

if __name__ == "__main__":
    ids = [b["id"] for b in BEATS]
    assert len(BEATS) == 14, len(BEATS)
    assert 13 <= len(BEATS) <= 22, "beat count outside 13-22 band"
    assert ids[0] == "B00" and ids[1] == "B01", ids[:2]
    assert ids[-3:] == ["BVDT", "BHTF", "BOUT"], ids[-3:]
    body = [b for b in BEATS if b["act"] in ("1", "2", "3")]
    assert len(body) == 8, len(body)
    recap = next(b for b in BEATS if b["id"] == "BVDT")["line"].lower()
    for kw in ["fluency", "restart", "sources", "narrow", "verify elsewhere"]:
        assert kw in recap, f"recap missing {kw!r}"
    mech = next(b for b in BEATS if b["id"] == "B05")["line"].lower()
    assert "most likely next word" in mech, "mechanism beat must name next-word prediction"
    idea = BEATS[0]["line"]
    assert "Liam, in for Bear" in idea, "IN-FOR-BEAR LAW: name the voice"
    htf = next(b for b in BEATS if b["id"] == "BHTF")["line"]
    assert "Paste this into Claude" in htf, "handoff must name the prompt"
    total = sum(b["dur_s"] for b in BEATS)
    assert 270 <= total <= 420, f"total {total}s outside 4.5-7 min band"
    BS = {"metadata": METADATA, "beats": BEATS}
    print(f"beats={len(BEATS)} body={len(body)} "
          f"total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
