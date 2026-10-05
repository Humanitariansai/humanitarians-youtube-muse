"""scenes.py — The yes-man problem. (Humanitarians AI YouTube film)

9 Manim scenes, B00-B08, one per GRAPHIC body beat. Skill: ai-explainer.
Bookend beats (BIDEA/BDEFS/BHTF/BOUT) are REMOTION and have no Manim class.

House conventions: 16:9, safe-area coords (x within +-6.3, y within +-3.4),
Claude palette (cream stage, warm ink, terracotta accent), one drawing per
beat with minimal labels, every on-screen word read aloud in its beat.
The chat window (cream card, header rule, user/AI bubbles, composer strip)
is the recurring cast object; the "You're absolutely right!" bubble is the
recurring punchline object. Every scene carries the @NikBearBrown watermark
bug (lower-right).

Class names are literal `class BNN_Name(Scene):` so the render stage finds
them. until()/finish() read beat_sheet.json in this folder (the narration
clock). Each scene adds at least one new non-text shape per play() so the
static QC gate sees evolving shape states; explicit FadeIn/Create/
GrowFromCenter/Transform before any motion, no .animate() anywhere.
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


def bubble(lines, cx, cy, fs=24, fill=KRAFT, stroke=INK):
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


def chat_window(cx=0.0, cy=0.1, w=7.0, h=4.6, title="new chat"):
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


def thumb_up(x, y, scale=1.0):
    """Terracotta thumbs-up medallion: circle + check."""
    ring = Circle(radius=0.34 * scale, color=TERRA, stroke_width=8).move_to([x, y, 0.0])
    ck = check_mark(x - 0.13 * scale, y + 0.12 * scale, scale=0.28 * scale)
    return VGroup(ring, ck)


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

class B00_YesMan(Scene):
    def construct(self):
        self.add(bug())
        win = chat_window(cx=0.0, cy=0.15, w=7.0, h=4.6)
        until(self, "Picture this")
        self.play(Create(win), run_time=1.2)
        ub = bubble(["loyalty programs are", "a waste of money"], 0.35, 1.05, fs=24, fill=KRAFT)
        until(self, "You type")
        self.play(FadeIn(ub), run_time=1.0)
        ab = bubble(["You're absolutely right!"], -0.35, -0.35, fs=26, fill="#FFFFFF")
        until(self, "The AI replies")
        self.play(FadeIn(ab), run_time=1.0)
        ck = check_mark(-3.6, -0.35, scale=0.9)
        self.play(GrowFromCenter(ck), run_time=0.8)
        tg = tag("no questions, no friction", 0.0, -2.85)
        until(self, "no questions, no friction")
        self.play(FadeIn(tg), run_time=0.8)
        finish(self)


class B01_Mirror(Scene):
    def construct(self):
        self.add(bug())
        wl = chat_window(cx=-3.0, cy=0.15, w=5.4, h=4.6, title="chat one")
        until(self, "Now the same AI")
        self.play(Create(wl), run_time=1.1)
        ubl = bubble(["best investment"], -3.0, 1.1, fs=22, fill=KRAFT)
        self.play(FadeIn(ubl), run_time=0.9)
        abl = bubble(["You're absolutely", "right!"], -3.0, -0.35, fs=22, fill="#FFFFFF")
        until(self, "The AI replies")
        self.play(FadeIn(abl), run_time=0.9)
        wr = chat_window(cx=3.0, cy=0.15, w=5.4, h=4.6, title="chat two")
        ubr = bubble(["a waste of money"], 3.0, 1.1, fs=22, fill=KRAFT)
        until(self, "Same enthusiasm")
        self.play(Create(wr), run_time=1.1)
        self.play(FadeIn(ubr), run_time=0.9)
        abr = bubble(["You're absolutely", "right!"], 3.0, -0.35, fs=22, fill="#FFFFFF")
        self.play(FadeIn(abr), run_time=0.9)
        mirror = DashedLine([0.0, 1.9, 0.0], [0.0, -1.9, 0.0], color=TERRA, stroke_width=5)
        self.play(Create(mirror), run_time=0.8)
        tg = tag("opposite opinion \u2014 same reply", 0.0, -2.85)
        until(self, "It has a mirror")
        self.play(FadeIn(tg), run_time=0.8)
        finish(self)


class B02_FiveModels(Scene):
    def construct(self):
        self.add(bug())
        view = bubble(["your view"], 0.0, 2.55, fs=26, fill=KRAFT)
        until(self, "Researchers tested")
        self.play(FadeIn(view), run_time=0.9)
        cards = VGroup(*[
            RoundedRectangle(corner_radius=0.16, width=1.9, height=1.15,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3).move_to([-4.4 + 2.2 * i, 0.1, 0.0])
            for i in range(5)])
        dots = VGroup(*[Dot([-4.4 + 2.2 * i, 0.1, 0.0], radius=0.13, color=TERRA)
                        for i in range(5)])
        self.play(FadeIn(cards), FadeIn(dots), run_time=1.1)
        until(self, "the same habit")
        arrows = VGroup(*[
            CurvedArrow([-4.4 + 2.2 * i, 0.75, 0.0], [(-4.4 + 2.2 * i) * 0.25, 2.0, 0.0],
                        angle=55 * DEGREES, color=TERRA, stroke_width=5)
            for i in range(5)])
        self.play(Create(arrows), run_time=1.4)
        tg = tag("five assistants \u2014 same habit", 0.0, -2.55)
        until(self, "sycophancy")
        self.play(FadeIn(tg), run_time=0.8)
        finish(self)


class B03_ThumbsUpSchool(Scene):
    def construct(self):
        self.add(bug())
        agree = bubble(["agrees with you"], -3.5, 1.55, fs=24, fill="#FFFFFF", stroke=TERRA)
        honest = bubble(["honest but", "uncomfortable"], -3.5, -0.15, fs=24, fill=CARD, stroke=DIM)
        until(self, "Look at the training")
        self.play(Create(agree), Create(honest), run_time=1.3)
        until(self, "thumbs up, thumbs down")
        ups = VGroup(*[thumb_up(-4.6 + 1.1 * i, 2.45, scale=0.9) for i in range(3)])
        self.play(FadeIn(ups[0]), FadeIn(ups[1]), FadeIn(ups[2]), run_time=1.2)
        dial_cx, dial_cy, dial_r = 3.1, 0.55, 1.55
        track = Arc(radius=dial_r, start_angle=0, angle=PI, color=GHOST,
                    stroke_width=16).move_to([dial_cx, dial_cy, 0.0])
        red = Arc(radius=dial_r, start_angle=PI * 0.68, angle=PI * 0.32, color=TERRA,
                  stroke_width=16).move_to([dial_cx, dial_cy, 0.0])
        needle_lo = Line([dial_cx, dial_cy, 0.0],
                         [dial_cx + dial_r * 0.85 * np.cos(PI * 0.18),
                          dial_cy + dial_r * 0.85 * np.sin(PI * 0.18), 0.0],
                         color=INK, stroke_width=7)
        needle_hi = Line([dial_cx, dial_cy, 0.0],
                         [dial_cx + dial_r * 0.85 * np.cos(PI * 0.82),
                          dial_cy + dial_r * 0.85 * np.sin(PI * 0.82), 0.0],
                         color=TERRA, stroke_width=7)
        dial_lab = T("agreement", size=30, color=DIM).move_to([dial_cx, dial_cy - 0.85, 0.0])
        self.play(Create(track), FadeIn(dial_lab), run_time=1.0)
        until(self, "the agreement dial")
        self.play(FadeIn(needle_lo), run_time=0.5)
        self.play(Create(red), Transform(needle_lo, needle_hi), run_time=1.2)
        rb_arrow = CurvedArrow([2.2, -2.5, 0.0], [4.0, -2.5, 0.0], angle=-70 * DEGREES,
                               color=TERRA, stroke_width=6)
        tg = tag("spring 2025: rolled back", 1.2, -1.9, size=28)
        until(self, "roll the update back")
        self.play(Create(rb_arrow), FadeIn(tg), run_time=1.0)
        finish(self)


class B04_PermissionToDisagree(Scene):
    def construct(self):
        self.add(bug())
        win = chat_window(cx=0.0, cy=0.15, w=7.0, h=4.6)
        until(self, "Step one")
        self.play(Create(win), run_time=1.2)
        ub = bubble(["tell me why", "I'm wrong"], 0.5, 1.05, fs=26, fill=KRAFT)
        until(self, "tell me why")
        self.play(FadeIn(ub), run_time=1.0)
        mask_plate = RoundedRectangle(corner_radius=0.16, width=4.2, height=1.05,
                                      fill_color="#FFFFFF", fill_opacity=1,
                                      stroke_color=INK, stroke_width=2).move_to([-0.5, -0.35, 0.0])
        mask_t = T("you're right!", size=30, color=DIM).move_to([-0.5, -0.35, 0.0])
        mask = VGroup(mask_plate, mask_t)
        self.play(FadeIn(mask), run_time=0.9)
        push_plate = RoundedRectangle(corner_radius=0.16, width=4.2, height=1.05,
                                      fill_color="#FFFFFF", fill_opacity=1,
                                      stroke_color=TERRA, stroke_width=4).move_to([-0.5, -0.35, 0.0])
        push_t = T("here's the flaw:", size=30, color=INK, bold=True).move_to([-0.5, -0.35, 0.0])
        push = VGroup(push_plate, push_t)
        until(self, "the assignment")
        self.play(Transform(mask, push), run_time=1.1)
        tg = tag("disagreement is the assignment", 0.0, -2.85)
        self.play(FadeIn(tg), run_time=0.8)
        finish(self)


class B05_AskBeforeTell(Scene):
    def construct(self):
        self.add(bug())
        facedown = RoundedRectangle(corner_radius=0.18, width=3.6, height=2.0,
                                    fill_color=INK, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3).move_to([-2.6, 0.5, 0.0])
        q = T("?", size=96, color=STAGE, bold=True).move_to([-2.6, 0.62, 0.0])
        until(self, "Step two")
        self.play(Create(facedown), FadeIn(q), run_time=1.1)
        cap = T("your view: not said yet", size=30, color=DIM).move_to([-2.6, -0.95, 0.0])
        self.play(FadeIn(cap), run_time=0.8)
        ab = bubble(["the honest one"], 2.4, 0.7, fs=30, fill="#FFFFFF")
        until(self, "what do you think")
        self.play(FadeIn(ab), run_time=1.0)
        ck = check_mark(4.7, 0.7, scale=0.9)
        self.play(GrowFromCenter(ck), run_time=0.8)
        tg = tag("the honest first answer", 0.0, -2.85)
        until(self, "the honest one")
        self.play(FadeIn(tg), run_time=0.8)
        finish(self)


class B06_Steelman(Scene):
    def construct(self):
        self.add(bug())
        straw = Rectangle(width=1.5, height=1.2, fill_color=GHOST, fill_opacity=1,
                          stroke_width=0).move_to([-2.9, -1.35, 0.0])
        straw_lab = T("straw man", size=34, color=DIM).move_to([-2.9, -2.35, 0.0])
        until(self, "Step three")
        self.play(FadeIn(straw), FadeIn(straw_lab), run_time=1.0)
        steel = Rectangle(width=1.5, height=3.3, fill_color=TERRA, fill_opacity=1,
                          stroke_width=0).move_to([0.1, -0.3, 0.0])
        steel_lab = T("steel man", size=34, color=INK, bold=True).move_to([0.1, -2.35, 0.0])
        until(self, "steelman the other side")
        self.play(GrowFromEdge(steel, DOWN), FadeIn(steel_lab), run_time=1.1)
        carg = CurvedArrow([0.1, 1.5, 0.0], [3.6, 2.1, 0.0], angle=50 * DEGREES,
                           color=TERRA, stroke_width=7)
        carg_lab = T("the other side", size=30, color=DIM).move_to([2.9, 1.15, 0.0])
        until(self, "the strongest counterargument")
        self.play(Create(carg), FadeIn(carg_lab), run_time=1.0)
        tg = tag("the strongest counterargument", 0.0, -2.95)
        self.play(FadeIn(tg), run_time=0.8)
        finish(self)


class B07_JudgeTheIdea(Scene):
    def construct(self):
        self.add(bug())
        fl = RoundedRectangle(corner_radius=0.18, width=3.9, height=2.6,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=DIM, stroke_width=3).move_to([-3.35, 0.35, 0.0])
        fr = RoundedRectangle(corner_radius=0.18, width=3.9, height=2.6,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK, stroke_width=3).move_to([3.35, 0.35, 0.0])
        lab_l = T("you", size=30, color=DIM).move_to([-3.35, 2.05, 0.0])
        lab_r = T("a stranger", size=30, color=INK, bold=True).move_to([3.35, 2.05, 0.0])
        until(self, "Step four")
        self.play(Create(fl), Create(fr), FadeIn(lab_l), FadeIn(lab_r), run_time=1.3)
        idea = bubble(["the idea"], -3.35, 0.35, fs=30, fill=KRAFT)
        until(self, "as if a stranger wrote it")
        self.play(FadeIn(idea), run_time=0.9)
        idea_target = bubble(["the idea"], 3.35, 0.35, fs=30, fill=KRAFT)
        until(self, "Take yourself out of the frame")
        self.play(Transform(idea, idea_target), run_time=1.2)
        ck = check_mark(5.15, 1.35, scale=0.9)
        self.play(GrowFromCenter(ck), run_time=0.8)
        tg = tag("grade the idea", 0.0, -2.85)
        until(self, "grade the idea")
        self.play(FadeIn(tg), run_time=0.8)
        finish(self)


class B08_PlaybookPass(Scene):
    def construct(self):
        self.add(bug())
        chips = VGroup(*[
            bubble([txt], x, y, fs=22, fill=CARD, stroke=DIM)
            for txt, x, y in [("what do you think", -3.3, 2.5),
                              ("strongest case", 2.2, 2.5),
                              ("honest bottom line", 0.0, 1.35)]])
        until(self, "the whole playbook")
        self.play(FadeIn(chips[0]), FadeIn(chips[1]), FadeIn(chips[2]), run_time=1.4)
        ab = bubble(["they often pay", "for themselves"], -1.9, -0.35, fs=28, fill="#FFFFFF")
        until(self, "The AI answers")
        self.play(FadeIn(ab), run_time=1.0)
        flaw = bubble(["the flaw in", "your plan"], 2.6, -0.35, fs=28, fill=CARD, stroke=TERRA)
        self.play(FadeIn(flaw), run_time=0.9)
        pin = Dot([2.6, 0.75, 0.0], radius=0.16, color=TERRA)
        pin_ring = Circle(radius=0.3, color=TERRA, stroke_width=5).move_to([2.6, 0.75, 0.0])
        until(self, "the flaw in your plan")
        self.play(GrowFromCenter(pin), Create(pin_ring), run_time=0.9)
        tg = tag("pushback", 0.0, -2.85, size=38)
        until(self, "That is pushback")
        self.play(FadeIn(tg), run_time=0.8)
        finish(self)
