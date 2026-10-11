"""scenes.py — Edit video with words. (Humanitarians AI YouTube film)

10 Manim scenes, B00-B09, one per GRAPHIC body beat. Skill: show-tell.
Bookend beats (BIDEA/BDEFS/BHTF/BOUT) are REMOTION and have no Manim class.

House conventions: 16:9, safe-area coords (x within +-6.2, y within +-3.3),
Claude palette (cream stage, warm ink, terracotta accent), one drawing per
beat with minimal labels, every on-screen word read aloud in its beat.
The phone, the chat window with composer strip, and the film-strip clips
are the recurring cast objects. Every scene carries the @NikBearBrown
watermark bug (lower-right).

Class names are literal `class BNN_Name(Scene):` so the render stage finds
them. until()/finish() read beat_sheet.json in this folder (the narration
clock). Each scene adds at least one new non-text shape per play() so the
static QC gate sees evolving shape states; explicit FadeIn/Create/
GrowFromCenter before any motion, no .animate() anywhere.
"""
from manim import *
import numpy as np
import json as _json
import os as _os

config.pixel_width = 1920
config.pixel_height = 1080
config.background_color = "#F2F0E9"

# ---- Claude palette ----
STAGE = "#F2F0E9"
INK = "#3D3929"
TERRA = "#D97757"
DIM = "#8B8F96"
GHOST = "#D9D4C7"
CARD = "#FAF9F5"
KRAFT = "#DCC9AA"
KRAFT_DK = "#C7AE86"
BAR1 = "#B9B3A6"
BAR2 = "#9d9789"
BAR3 = "#7E786B"
SERIF = "EB Garamond"

# manim exposes BOLD/NORMAL; the QC stub does not. Same string values either way.
BOLD = "BOLD"
NORMAL = "NORMAL"


def T(s, size=34, color=INK, bold=False):
    return Text(s, font=SERIF, font_size=size, color=color,
                weight=BOLD if bold else NORMAL)


def bug():
    """Channel watermark bug, lower-right, inside the safe area."""
    return Text("@NikBearBrown", font=SERIF, font_size=16, color=INK,
                fill_opacity=0.45).move_to([5.35, -3.05, 0.0])


def tag(text, x, y, size=32, color=TERRA):
    """A small terracotta tag line under the drawing."""
    return T(text, size=size, color=color, bold=True).move_to([x, y, 0.0])


def _tw(s, fs):
    """Rough text-width estimate so plates always contain their text."""
    return len(s) * fs * 0.0125


def bubble(lines, cx, cy, fs=26, fill=KRAFT, stroke=INK):
    """A chat bubble with explicit line breaks: plate + centered text lines."""
    if isinstance(lines, str):
        lines = [lines]
    w = max(_tw(l, fs) for l in lines) + 0.9
    ts = VGroup(*[T(l, size=fs, color=INK).move_to([cx, cy + (len(lines) - 1) * 0.21 - i * 0.42, 0.0])
                  for i, l in enumerate(lines)])
    h = len(lines) * 0.42 + 0.42
    plate = RoundedRectangle(corner_radius=0.16, width=w, height=h,
                             fill_color=fill, fill_opacity=1,
                             stroke_color=stroke, stroke_width=2).move_to([cx, cy, 0.0])
    return VGroup(plate, ts)


def chat_window(cx=0.0, cy=0.1, w=7.0, h=4.6, title="chat"):
    """The recurring cast object: card, header rule, composer strip."""
    body = RoundedRectangle(corner_radius=0.22, width=w, height=h,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy, 0.0])
    top = cy + h / 2
    bot = cy - h / 2
    rule = Line([cx - w / 2 + 0.25, top - 0.6, 0.0],
                [cx + w / 2 - 0.25, top - 0.6, 0.0],
                color=GHOST, stroke_width=3)
    head = T(title, size=24, color=DIM).move_to([cx - w / 2 + 1.05, top - 0.3, 0.0])
    composer = RoundedRectangle(corner_radius=0.14, width=w - 1.0, height=0.6,
                                fill_color=STAGE, fill_opacity=1,
                                stroke_color=DIM, stroke_width=2).move_to([cx, bot + 0.45, 0.0])
    return VGroup(body, rule, head, composer)


def check_mark(x, y, scale=1.0, color=TERRA):
    g = VGroup(
        Line([0, 0, 0], [0.5, -0.3, 0], color=color, stroke_width=12),
        Line([0.5, -0.3, 0], [1.3, 0.4, 0], color=color, stroke_width=12),
    ).scale(scale).move_to([x, y, 0.0])
    return g


def phone(cx, cy, w=2.7, h=5.3, label=""):
    """A simple phone: outer body, screen, speaker pill, optional label."""
    body = RoundedRectangle(corner_radius=0.3, width=w, height=h,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy, 0.0])
    speaker = RoundedRectangle(corner_radius=0.08, width=0.9, height=0.14,
                               fill_color=INK, fill_opacity=1,
                               stroke_color=INK, stroke_width=1).move_to([cx, cy + h / 2 - 0.32, 0.0])
    screen = RoundedRectangle(corner_radius=0.18, width=w - 0.5, height=h - 1.1,
                              fill_color=STAGE, fill_opacity=1,
                              stroke_color=DIM, stroke_width=2).move_to([cx, cy - 0.18, 0.0])
    parts = [body, speaker, screen]
    if label:
        parts.append(T(label, size=26, color=DIM).move_to([cx, cy + h / 2 - 0.62, 0.0]))
    return VGroup(*parts)


def film_clip(x, y, w=1.15, h=0.72, color=BAR1, label=None):
    """One film-strip clip: rounded rect, optional tiny label beneath."""
    r = RoundedRectangle(corner_radius=0.1, width=w, height=h,
                         fill_color=color, fill_opacity=1,
                         stroke_color=INK, stroke_width=2).move_to([x, y, 0.0])
    if label:
        return VGroup(r, T(label, size=24, color=INK).move_to([x, y - h / 2 - 0.28, 0.0]))
    return r


def music_note(x, y, scale=1.0):
    """A simple quaver: filled ellipse head + stem + flag."""
    head = Ellipse(width=0.42 * scale, height=0.32 * scale,
                   fill_color=TERRA, fill_opacity=1,
                   stroke_color=TERRA, stroke_width=1).move_to([x, y, 0.0])
    stem = Line([x + 0.2 * scale, y + 0.05 * scale, 0.0],
                [x + 0.2 * scale, y + 1.0 * scale, 0.0],
                color=TERRA, stroke_width=8 * scale)
    flag = Line([x + 0.2 * scale, y + 1.0 * scale, 0.0],
                [x + 0.75 * scale, y + 0.82 * scale, 0.0],
                color=TERRA, stroke_width=8 * scale)
    return VGroup(head, stem, flag)


def cursor_tri(x, y, scale=1.0):
    """A small hand-cursor triangle pointer."""
    return Triangle(fill_color=INK, fill_opacity=1,
                    stroke_color=INK, stroke_width=1
                    ).scale(0.28 * scale).rotate(-30 * DEGREES).move_to([x, y, 0.0])


# ---- narration clock: until()/finish() pace against beat_sheet.json ----
try:
    _HERE = _os.path.dirname(_os.path.abspath(__file__))
    with open(_os.path.join(_HERE, "beat_sheet.json")) as _f:
        _SHEET = _json.load(_f)
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s")
                                   or b.get("estimated_duration_s") or 0)
               for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}


def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0


def until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its char share of the narration x the audio)."""
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)


# ============================ BODY SCENES ============================

class B00_HeroChat(Scene):
    def construct(self):
        self.add(bug())
        win = chat_window(cx=0.0, cy=0.75, w=7.2, h=3.4, title="editor chat")
        until(self, "Picture a chat window")
        self.play(Create(win), run_time=1.2)
        ub = bubble(["match the cuts", "to the beat"], 0.0, 0.55, fs=26, fill=KRAFT)
        until(self, "You type")
        self.play(FadeIn(ub), run_time=1.0)
        cols = [BAR1, BAR2, BAR3, BAR1, BAR2]
        clips = VGroup(*[film_clip(-2.9 + 1.45 * i, -1.75, color=cols[i])
                         for i in range(5)])
        self.play(FadeIn(clips), run_time=0.9)
        until(self, "rearrange themselves")
        cols2 = [BAR3, BAR1, BAR2, BAR2, BAR1]
        clips2 = VGroup(*[film_clip(-2.9 + 1.45 * i, -1.75, color=cols2[i])
                          for i in range(5)])
        spark = Dot([-2.9, -1.15, 0.0], radius=0.12, color=TERRA)
        self.play(FadeOut(clips), FadeIn(clips2), FadeIn(spark), run_time=1.2)
        tg = tag("plain language", 0.0, -2.8)
        until(self, "plain language")
        self.play(FadeIn(tg), run_time=0.8)
        finish(self)


class B01_TenHours(Scene):
    def construct(self):
        self.add(bug())
        tl = VGroup(*[film_clip(-5.2 + 0.95 * i, 0.9, w=0.8, h=0.6,
                                color=[BAR1, BAR2, BAR3][i % 3])
                      for i in range(12)])
        until(self, "editing eats time")
        self.play(Create(tl), run_time=1.3)
        c1 = RoundedRectangle(corner_radius=0.16, width=2.6, height=1.0,
                              fill_color=KRAFT, fill_opacity=1,
                              stroke_color=INK, stroke_width=3).move_to([-3.4, -1.2, 0.0])
        t1 = T("1 hour shoot", size=32, bold=True).move_to([-3.4, -1.2, 0.0])
        until(self, "a one-hour shoot")
        self.play(FadeIn(c1), FadeIn(t1), run_time=0.9)
        face = Circle(radius=0.85, color=INK, stroke_width=5).move_to([0.4, -1.2, 0.0])
        hand = Line([0.4, -1.2, 0.0], [0.4, -0.55, 0.0], color=TERRA, stroke_width=8)
        self.play(Create(face), Create(hand), run_time=0.8)
        hand2 = Line([0.4, -1.2, 0.0], [-0.25, -1.2, 0.0], color=TERRA, stroke_width=8)
        until(self, "ten hours or more in the edit")
        self.play(FadeOut(hand), FadeIn(hand2), run_time=1.0)
        c2 = RoundedRectangle(corner_radius=0.16, width=3.1, height=1.0,
                              fill_color="#FFFFFF", fill_opacity=1,
                              stroke_color=INK, stroke_width=3).move_to([3.6, -1.2, 0.0])
        t2 = T("10+ hours edit", size=32, bold=True).move_to([3.6, -1.2, 0.0])
        self.play(FadeIn(c2), FadeIn(t2), run_time=0.9)
        ring = Circle(radius=0.75, color=TERRA, stroke_width=6).move_to([3.6, -1.2, 0.0])
        until(self, "trimming, cutting")
        self.play(Create(ring), run_time=0.8)
        finish(self)


class B02_Announced(Scene):
    def construct(self):
        self.add(bug())
        card = RoundedRectangle(corner_radius=0.18, width=4.6, height=1.5,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=4).move_to([-3.2, 1.5, 0.0])
        ct = T("Made on YouTube", size=34, bold=True).move_to([-3.2, 1.72, 0.0])
        cs = T("Sept 2026", size=30, color=DIM).move_to([-3.2, 1.18, 0.0])
        until(self, "Made on YouTube")
        self.play(Create(card), FadeIn(ct), FadeIn(cs), run_time=1.2)
        ph = phone(2.6, -0.1, w=2.9, h=5.0, label="")
        win = chat_window(cx=2.6, cy=-0.35, w=2.3, h=2.6, title="chat")
        until(self, "conversational editing assistant")
        self.play(FadeIn(ph), Create(win), run_time=1.3)
        l1 = T("Shorts", size=32, bold=True).move_to([-3.6, -1.5, 0.0])
        l2 = T("YouTube Create", size=32, bold=True).move_to([-1.2, -1.5, 0.0])
        until(self, "coming to Shorts")
        self.play(FadeIn(l1), run_time=0.7)
        until(self, "YouTube Create app")
        self.play(FadeIn(l2), run_time=0.7)
        chip = bubble(["try: tighten", "this up"], 2.6, -2.6, fs=24, fill="#FFFFFF", stroke=DIM)
        until(self, "suggested prompt")
        self.play(FadeIn(chip), run_time=0.9)
        finish(self)


class B03_Demo(Scene):
    def construct(self):
        self.add(bug())
        takes = VGroup()
        for i, outfit in enumerate(["outfit A", "outfit B", "outfit C"]):
            x = -3.6 + 3.6 * i
            card = RoundedRectangle(corner_radius=0.16, width=2.9, height=1.9,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3).move_to([x, 1.3, 0.0])
            lab = T(outfit, size=30, bold=True).move_to([x, 1.55, 0.0])
            sub = T("3 takes", size=26, color=DIM).move_to([x, 1.0, 0.0])
            takes.add(VGroup(card, lab, sub))
        until(self, "hands over dance footage")
        self.play(FadeIn(takes), run_time=1.2)
        until(self, "different outfits")
        nm = T("Happy Kelli", size=28, color=DIM).move_to([0.0, 2.55, 0.0])
        self.play(FadeIn(nm), run_time=0.7)
        qb = bubble(["best take of", "each outfit"], 0.0, -0.35, fs=26, fill=KRAFT)
        until(self, "best take of each outfit")
        self.play(FadeIn(qb), run_time=1.0)
        winners = VGroup(*[film_clip(-3.6 + 3.6 * i, -1.7, color=BAR2)
                           for i in range(3)])
        checks = VGroup(*[check_mark(-3.6 + 3.6 * i, -1.7, scale=0.55)
                          for i in range(3)])
        until(self, "add music, add transitions")
        self.play(FadeIn(winners), GrowFromCenter(checks), run_time=1.2)
        note = music_note(4.6, -2.0, scale=1.0)
        arr = VGroup(*[Arrow([-0.2 + 0.9 * i, -2.35, 0.0], [0.5 + 0.9 * i, -2.35, 0.0],
                             color=TERRA, stroke_width=6, buff=0.05)
                       for i in range(2)])
        until(self, "assembles the cut")
        self.play(FadeIn(note), Create(arr), run_time=1.1)
        finish(self)


class B04_Fiddly(Scene):
    def construct(self):
        self.add(bug())
        qb = bubble(["add a title card"], 0.0, 2.35, fs=26, fill=KRAFT)
        until(self, "fiddly work")
        self.play(FadeIn(qb), run_time=0.9)
        clip = film_clip(-3.4, 0.7, w=2.6, h=1.5, color=BAR1)
        self.play(FadeIn(clip), run_time=0.8)
        ov = RoundedRectangle(corner_radius=0.1, width=2.0, height=0.55,
                              fill_color=TERRA, fill_opacity=1,
                              stroke_color=TERRA, stroke_width=1).move_to([-3.4, 0.7, 0.0])
        ovt = T("new episode", size=26, color=CARD, bold=True).move_to([-3.4, 0.7, 0.0])
        until(self, "Text overlays, on command")
        self.play(FadeIn(ov), FadeIn(ovt), run_time=0.9)
        bars = VGroup(*[Rectangle(width=0.16, height=0.3 + 0.12 * ((i * 7) % 9),
                                  fill_color=BAR2, fill_opacity=1,
                                  stroke_width=0).move_to([0.6 + 0.24 * i, 0.7, 0.0])
                        for i in range(16)])
        self.play(FadeIn(bars), run_time=0.9)
        until(self, "Pauses in speech, removed")
        bars2 = VGroup(*[Rectangle(width=0.16, height=0.3 + 0.12 * ((i * 7) % 9),
                                   fill_color=BAR2, fill_opacity=1,
                                   stroke_width=0).move_to([0.6 + 0.24 * (i if i < 6 else i - 2), 0.7, 0.0])
                         for i in range(16) if i not in (6, 7)])
        gap_mark = check_mark(3.1, 1.55, scale=0.5)
        self.play(FadeOut(bars), FadeIn(bars2), FadeIn(gap_mark), run_time=1.1)
        chips = VGroup(*[bubble([s], -3.7 + 3.7 * i, -1.7, fs=22, fill="#FFFFFF", stroke=DIM)
                         for i, s in enumerate(["tighten", "add music", "caption it"])])
        until(self, "proposes the next move")
        self.play(FadeIn(chips), run_time=1.0)
        finish(self)


class B05_YourHands(Scene):
    def construct(self):
        self.add(bug())
        win = chat_window(cx=0.0, cy=0.4, w=7.2, h=3.2, title="editor chat")
        until(self, "jump back into the regular timeline")
        self.play(Create(win), run_time=1.1)
        tl = VGroup(*[film_clip(-4.35 + 1.45 * i, -1.6, color=[BAR1, BAR2, BAR3][i % 3])
                      for i in range(7)])
        self.play(FadeOut(win), FadeIn(tl), run_time=1.1)
        cur = cursor_tri(-1.45, -1.15, scale=1.2)
        edge = Line([-1.45, -2.0, 0.0], [-1.45, -1.2, 0.0], color=TERRA, stroke_width=6)
        until(self, "adjust everything by hand")
        self.play(FadeIn(cur), Create(edge), run_time=0.9)
        tl2 = VGroup(*[film_clip([-4.35, -2.9, -1.225, 0.5, 1.95, 3.4, 4.85][i], -1.6,
                                w=(1.9 if i == 2 else 1.15),
                                color=[BAR1, BAR2, BAR3][i % 3])
                      for i in range(7)])
        cur2 = cursor_tri(-0.275, -1.15, scale=1.2)
        edge2 = Line([-0.275, -2.0, 0.0], [-0.275, -1.2, 0.0], color=TERRA, stroke_width=6)
        until(self, "The AI drafts; you direct")
        self.play(FadeOut(tl), FadeOut(cur), FadeOut(edge),
                  FadeIn(tl2), FadeIn(cur2), FadeIn(edge2), run_time=1.2)
        tg = tag("edits with you, not for you", 0.0, -2.85)
        until(self, "edits with you, not for you")
        self.play(FadeIn(tg), run_time=0.8)
        finish(self)


class B06_Early2027(Scene):
    def construct(self):
        self.add(bug())
        cal = RoundedRectangle(corner_radius=0.2, width=3.4, height=3.0,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=4).move_to([-3.6, 0.2, 0.0])
        chead = T("today", size=30, color=DIM).move_to([-3.6, 1.25, 0.0])
        dots = VGroup(*[Dot([-4.5 + 0.6 * (i % 3), 0.55 - 0.55 * (i // 3), 0.0],
                            radius=0.11, color=BAR2)
                        for i in range(9)])
        until(self, "reported window")
        self.play(Create(cal), FadeIn(chead), FadeIn(dots), run_time=1.2)
        hero = RoundedRectangle(corner_radius=0.2, width=4.6, height=1.7,
                                fill_color=KRAFT, fill_opacity=1,
                                stroke_color=INK, stroke_width=4).move_to([1.8, 0.5, 0.0])
        ht = T("early 2027", size=54, bold=True).move_to([1.8, 0.5, 0.0])
        until(self, "early twenty twenty-seven")
        self.play(GrowFromCenter(hero), FadeIn(ht), run_time=1.1)
        l1 = T("Shorts", size=32, bold=True).move_to([0.6, -1.5, 0.0])
        l2 = T("Create app", size=32, bold=True).move_to([3.0, -1.5, 0.0])
        until(self, "Shorts and the Create app")
        self.play(FadeIn(l1), FadeIn(l2), run_time=0.9)
        cap = T("reported window", size=26, color=DIM).move_to([1.8, -2.35, 0.0])
        until(self, "a preview today")
        self.play(FadeIn(cap), run_time=0.8)
        finish(self)


class B07_MetaShips(Scene):
    def construct(self):
        self.add(bug())
        ph = phone(-3.9, 0.0, w=2.9, h=5.2, label="Edits")
        until(self, "inside the Edits app")
        self.play(FadeIn(ph), run_time=1.0)
        names = ["views", "watch time", "likes"]
        bars = VGroup()
        for i, nm in enumerate(names):
            x = 0.2 + 1.9 * i
            bar = Rectangle(width=0.9, height=0.6 + 0.7 * i,
                            fill_color=[BAR1, BAR2, BAR3][i], fill_opacity=1,
                            stroke_color=INK, stroke_width=2
                            ).move_to([x, -1.4 + (0.6 + 0.7 * i) / 2, 0.0])
            lab = T(nm, size=28).move_to([x, -1.75, 0.0])
            bars.add(VGroup(bar, lab))
        until(self, "reads your Reels numbers")
        self.play(FadeIn(bars), run_time=1.2)
        until(self, "views, watch time, likes")
        dots = VGroup(*[Dot([0.2 + 1.9 * i, 0.6 + 0.7 * i, 0.0], radius=0.13, color=TERRA)
                        for i in range(3)])
        self.play(FadeIn(dots), run_time=0.8)
        qb = bubble(["what to", "make next?"], 3.6, 1.9, fs=26, fill=KRAFT)
        feed = VGroup(*[Arrow([0.2 + 1.9 * i, 0.9 + 0.7 * i, 0.0], [3.0, 1.7, 0.0],
                              color=DIM, stroke_width=4, buff=0.15)
                        for i in range(3)])
        until(self, "what to make next")
        self.play(Create(feed), FadeIn(qb), run_time=1.2)
        finish(self)


class B08_TheLine(Scene):
    def construct(self):
        self.add(bug())
        chips = VGroup(*[bubble([s], -4.2 + 2.8 * i, 1.5, fs=26, fill="#FFFFFF", stroke=DIM)
                         for i, s in enumerate(["hooks", "captions", "scripts", "audio"])])
        until(self, "Hooks, captions, scripts")
        self.play(FadeIn(chips), run_time=1.1)
        until(self, "trending audio")
        note = music_note(5.1, 1.5, scale=0.8)
        self.play(FadeIn(note), run_time=0.7)
        div = Line([-5.5, 0.1, 0.0], [5.5, 0.1, 0.0], color=INK, stroke_width=4)
        until(self, "draws a clear line")
        self.play(Create(div), run_time=0.9)
        tg = tag("the creative calls stay yours", 0.0, -1.3)
        until(self, "does the digging")
        self.play(FadeIn(tg), run_time=0.9)
        ck = check_mark(0.0, -2.2, scale=0.8)
        until(self, "creative calls stay yours")
        self.play(GrowFromCenter(ck), run_time=0.8)
        finish(self)


class B09_Today(Scene):
    def construct(self):
        self.add(bug())
        ph = phone(-3.9, 0.0, w=2.9, h=5.2, label="YouTube Create")
        until(self, "do not have to wait")
        self.play(FadeIn(ph), run_time=1.0)
        loose = VGroup(*[film_clip(0.4 + 1.5 * (i % 3), 1.3 - 1.1 * (i // 3),
                                   color=[BAR1, BAR2, BAR3][i % 3])
                         for i in range(6)])
        until(self, "AI first draft")
        self.play(FadeIn(loose), run_time=1.0)
        neat = VGroup(*[film_clip(-1.225 + 1.25 * i, -0.9, color=[BAR1, BAR2, BAR3][i % 3])
                        for i in range(6)])
        spark = Dot([-1.225, -0.3, 0.0], radius=0.12, color=TERRA)
        until(self, "arranges them into a starting cut")
        self.play(FadeOut(loose), FadeIn(neat), FadeIn(spark), run_time=1.3)
        note = T("no chat yet", size=28, color=DIM).move_to([1.9, -2.0, 0.0])
        until(self, "no chat window yet")
        self.play(FadeIn(note), run_time=0.8)
        chip = bubble(["chat: 2027"], 1.9, -2.75, fs=24, fill=KRAFT, stroke=TERRA)
        until(self, "arrives in twenty twenty-seven")
        self.play(FadeIn(chip), run_time=0.9)
        finish(self)
