"""scenes.py — Posters and Flyers (Humanitarians AI YouTube film)

9 Manim scenes, B00-B07 + BVDT, one per GRAPHIC body beat. Skill: show-tell.
Film #38, Wave 6 "Making things"; companion to film 19 "Pictures from words".

House conventions: 16:9, safe-area coords (x within +-6.2, y within +-3.3),
show-tell Claude palette (cream stage, warm ink, terracotta accent), one
image per beat with minimal labels, every on-screen word read aloud in its
beat. The cast: the POSTER (portrait kraft sheet) and the PICTURE FRAME
(landscape card) — the same two objects in every beat.

Each scene adds at least one new non-text shape per play() so the static
QC gate sees evolving shape states: explicit FadeIn/Create before any
.animate() motion, and every midpoint already holds landed, settled objects.
"""
import numpy as np
from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.background_color = "#F2F0E9"

# ---- show-tell Claude palette ----
STAGE = "#F2F0E9"
INK = "#3D3929"
TERRA = "#D97757"
DIM = "#8B8F96"
GHOST = "#D9D4C7"
CARD = "#FAF9F5"
KRAFT = "#DCC9AA"
KRAFT_D = "#C7AE86"
DARK = "#26221F"
SERIF = "EB Garamond"

# manim exposes BOLD/NORMAL; the QC stub does not. Same string values either way.
BOLD = "BOLD"
NORMAL = "NORMAL"


def T(s, size=32, color=INK, bold=False):
    return Text(s, font=SERIF, font_size=size, color=color,
                weight=BOLD if bold else NORMAL)


def bug():
    """Channel watermark bug, lower-right, inside the safe area."""
    return Text("@NikBearBrown", font_size=16, color=INK,
                fill_opacity=0.45).move_to(np.array([5.35, -3.05, 0.0]))


def shadow(pos, w=4.2):
    return Ellipse(width=w, height=0.32, fill_color=GHOST,
                   fill_opacity=0.8, stroke_width=0).move_to(pos)


def poster(x=0.0, y=0.0, w=3.2, h=4.5):
    """Portrait kraft poster sheet, the film's hero object."""
    return RoundedRectangle(corner_radius=0.14, width=w, height=h,
                            fill_color=KRAFT, fill_opacity=1,
                            stroke_color=INK, stroke_width=6).move_to(
        np.array([x, y, 0.0]))


def frame_pic(x=0.0, y=0.0, w=4.0, h=2.8):
    """Landscape picture card, the film's second cast object."""
    return RoundedRectangle(corner_radius=0.14, width=w, height=h,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=6).move_to(
        np.array([x, y, 0.0]))


def chip(text, pos, w=None, fs=32):
    if w is None:
        w = len(text) * 0.21 + 0.9
    r = RoundedRectangle(corner_radius=0.12, width=w, height=0.78,
                         fill_color=CARD, fill_opacity=1,
                         stroke_color=INK, stroke_width=3).move_to(pos)
    t = T(text, size=fs).move_to(pos)
    return VGroup(r, t)


def num_chip(n, pos, fs=32):
    """Ink numeral badge for zone/step numbers (GATE T: numerals are ink)."""
    c = Circle(radius=0.3, fill_color=CARD, fill_opacity=1,
               stroke_color=INK, stroke_width=3).move_to(pos)
    t = T(str(n), size=fs, bold=True).move_to(pos)
    return VGroup(c, t)


def check(pos, scale=1.0):
    g = VGroup(
        Line(np.array([0, 0, 0]), np.array([0.5, -0.3, 0]),
             color=TERRA, stroke_width=12),
        Line(np.array([0.5, -0.3, 0]), np.array([1.3, 0.4, 0]),
             color=TERRA, stroke_width=12),
    ).scale(scale).move_to(pos)
    return g


def x_mark(pos, scale=1.0):
    g = VGroup(
        Line(np.array([-0.45, 0.45, 0]), np.array([0.45, -0.45, 0]),
             color=TERRA, stroke_width=12),
        Line(np.array([-0.45, -0.45, 0]), np.array([0.45, 0.45, 0]),
             color=TERRA, stroke_width=12),
    ).scale(scale).move_to(pos)
    return g


def label(text, pos, fs=34):
    """Small ink label; sits beside objects with a leader line."""
    return T(text, size=fs).move_to(pos)


def leader(p1, p2):
    """Short ink leader from label to object (kept clear of the label)."""
    return Line(np.array(p1), np.array(p2), color=INK, stroke_width=3)


def hill(y0, x0, w):
    """Simple hill triangle for the art doodle."""
    return Polygon(np.array([x0 - w / 2, y0, 0]),
                   np.array([x0 + w / 2, y0, 0]),
                   np.array([x0, y0 + 0.9, 0]),
                   fill_color=KRAFT_D, fill_opacity=1,
                   stroke_color=INK, stroke_width=3)


def sun_dot(pos, r=0.28):
    return Circle(radius=r, fill_color=TERRA, fill_opacity=1,
                  stroke_width=0).move_to(pos)


class B00_Hero(Scene):
    """The poster arrives: headline band, detail lines, art doodle."""

    def construct(self):
        sh = shadow(np.array([0.0, -2.62, 0.0]), w=4.4)
        p = poster(x=-0.9, y=0.1)
        self.play(Create(sh), Create(p), run_time=2.0)

        band = Rectangle(width=2.7, height=0.72, fill_color=CARD,
                         fill_opacity=1, stroke_color=INK,
                         stroke_width=4).move_to(np.array([-0.9, 1.55, 0.0]))
        line1 = Line(np.array([-2.0, 0.85, 0.0]), np.array([0.2, 0.85, 0.0]),
                     color=INK, stroke_width=5)
        line2 = Line(np.array([-2.0, 0.45, 0.0]), np.array([-0.4, 0.45, 0.0]),
                     color=INK, stroke_width=5)
        self.play(Create(band), Create(line1), Create(line2), run_time=2.5)

        s = sun_dot(np.array([-1.6, -1.1, 0.0]))
        h = hill(-1.95, -0.5, 2.0)
        self.play(FadeIn(s), Create(h), run_time=2.5)

        lab = label("poster", np.array([2.45, 1.5, 0.0]))
        ld = leader(np.array([2.05, 1.5, 0.0]), np.array([0.85, 1.0, 0.0]))
        self.play(FadeIn(lab), Create(ld), FadeIn(bug()), run_time=1.5)
        self.wait(4.6)


class B01_Companion(Scene):
    """The five-slot recipe feeds the picture frame; the doodle warms up."""

    def construct(self):
        f = frame_pic(x=-2.4, y=0.2)
        self.play(FadeIn(f), run_time=1.5)

        words = ["subject", "setting", "style", "lighting", "mood"]
        chips = VGroup(*[
            chip(w, np.array([2.9, 1.9 - i * 0.95, 0.0]), w=2.3)
            for i, w in enumerate(words)])
        pieces = []
        y0, x0 = 0.9, -2.4
        for i, name in enumerate(words):
            self.play(FadeIn(chips[i]), run_time=1.0)
            if name == "subject":
                pieces.append(sun_dot(np.array([x0 - 1.0, y0 - 0.4, 0.0])))
                self.play(FadeIn(pieces[-1]), run_time=0.8)
            elif name == "setting":
                pieces.append(hill(y0 - 1.1, x0, 2.6))
                self.play(Create(pieces[-1]), run_time=0.8)
            elif name == "style":
                pieces.append(Rectangle(width=3.5, height=0.9,
                                        fill_color=KRAFT_D, fill_opacity=0.55,
                                        stroke_width=0).move_to(
                    np.array([x0, y0 - 0.75, 0.0])))
                self.play(FadeIn(pieces[-1]), run_time=0.8)
            elif name == "lighting":
                pieces.append(sun_dot(np.array([x0 + 1.1, y0 + 0.5, 0.0]),
                                      r=0.2))
                self.play(FadeIn(pieces[-1]), run_time=0.8)
            else:
                pieces.append(Circle(radius=0.16, fill_color=TERRA,
                                     fill_opacity=1, stroke_width=0).move_to(
                    np.array([x0 - 0.2, y0 + 0.55, 0.0])))
                self.play(FadeIn(pieces[-1]), run_time=0.8)

        arr = Arrow(np.array([1.45, 0.2, 0.0]), np.array([-0.1, 0.2, 0.0]),
                    color=INK, stroke_width=8, buff=0.1)
        self.play(Create(arr), run_time=1.2)
        lab = label("the recipe", np.array([2.9, 2.95, 0.0]))
        self.play(FadeIn(lab), FadeIn(bug()), run_time=1.0)
        self.wait(3.0)


class B02_Facts(Scene):
    """Three fact chips fly onto the poster and become its words."""

    def construct(self):
        sh = shadow(np.array([-1.4, -2.62, 0.0]), w=4.4)
        p = poster(x=-1.4, y=0.1)
        self.play(Create(sh), Create(p), run_time=1.8)

        facts = ["garage sale", "Saturday, 9 a.m.", "12 Maple Street"]
        for i, ftext in enumerate(facts):
            cw = len(ftext) * 0.21 + 0.9
            c = chip(ftext, np.array([6.0 - cw / 2, 1.7 - i * 1.5, 0.0]),
                     w=cw)
            self.play(FadeIn(c), run_time=1.0)
            tgt = np.array([-1.4, 1.55 - i * 0.85, 0.0])
            line = Line(tgt + np.array([-1.15, 0.0, 0.0]),
                        tgt + np.array([1.15, 0.0, 0.0]),
                        color=INK, stroke_width=5)
            self.play(FadeOut(c), Create(line), run_time=1.2)

        lab = label("three facts", np.array([3.3, -2.3, 0.0]))
        ld = leader(np.array([2.95, -2.2, 0.0]), np.array([0.35, -1.3, 0.0]))
        self.play(FadeIn(lab), Create(ld), FadeIn(bug()), run_time=1.0)
        self.wait(2.5)


class B03_ExactWords(Scene):
    """Misspelled headline is stamped out; the exact words replace it."""

    def construct(self):
        sh = shadow(np.array([-1.2, -2.62, 0.0]), w=4.4)
        p = poster(x=-1.2, y=0.1)
        self.play(Create(sh), Create(p), run_time=1.5)

        wrong = T("GARAG SALE", size=48, bold=True).move_to(
            np.array([-1.2, 1.5, 0.0]))
        self.play(FadeIn(wrong), run_time=1.0)
        self.play(Rotate(wrong, angle=0.06), run_time=0.6)
        self.play(Rotate(wrong, angle=-0.12), run_time=0.6)
        self.play(Rotate(wrong, angle=0.06), run_time=0.6)

        quote = chip('"GARAGE SALE"', np.array([3.3, 2.3, 0.0]), w=3.4, fs=30)
        self.play(FadeIn(quote), run_time=1.2)
        xm = x_mark(np.array([-1.2, 1.5, 0.0]), scale=1.6)
        self.play(FadeIn(xm), FadeOut(wrong), run_time=1.2)
        right = T("GARAGE SALE", size=48, bold=True).move_to(
            np.array([-1.2, 1.5, 0.0]))
        self.play(FadeOut(xm), FadeIn(right), run_time=1.2)

        lab = label("exact words", np.array([3.1, 0.9, 0.0]))
        ld = leader(np.array([2.7, 0.85, 0.0]), np.array([0.55, 1.35, 0.0]))
        self.play(FadeIn(lab), Create(ld), FadeIn(bug()), run_time=1.0)
        self.wait(2.4)


class B04_Layout(Scene):
    """Three zones: headline, details, empty room for facts."""

    def construct(self):
        p = poster(x=-1.2, y=0.1)
        self.play(Create(p), run_time=1.5)

        z1 = Rectangle(width=2.7, height=0.9, fill_color=CARD,
                       fill_opacity=1, stroke_color=INK,
                       stroke_width=4).move_to(np.array([-1.2, 1.5, 0.0]))
        n1 = num_chip(1, np.array([-3.05, 1.5, 0.0]))
        l1 = label("headline", np.array([-4.35, 1.5, 0.0]), fs=32)
        self.play(Create(z1), FadeIn(n1), FadeIn(l1), run_time=2.0)

        z2 = Rectangle(width=2.7, height=0.9, fill_color=CARD,
                       fill_opacity=1, stroke_color=INK,
                       stroke_width=4).move_to(np.array([-1.2, 0.35, 0.0]))
        n2 = num_chip(2, np.array([-3.05, 0.35, 0.0]))
        l2 = label("details", np.array([-4.3, 0.35, 0.0]), fs=32)
        self.play(Create(z2), FadeIn(n2), FadeIn(l2), run_time=2.0)

        z3 = Rectangle(width=2.7, height=1.5, fill_color=GHOST,
                       fill_opacity=0.9, stroke_color=DIM,
                       stroke_width=3).move_to(np.array([-1.2, -1.15, 0.0]))
        n3 = num_chip(3, np.array([-3.05, -1.15, 0.0]))
        l3 = label("room for facts", np.array([2.0, -1.15, 0.0]), fs=32)
        self.play(Create(z3), FadeIn(n3), FadeIn(l3),
                  FadeIn(bug()), run_time=2.2)
        self.wait(2.8)


class B05_Split(Scene):
    """AI draws the picture; you write the words."""

    def construct(self):
        f = frame_pic(x=-3.0, y=0.2, w=3.6, h=2.5)
        s = sun_dot(np.array([-3.7, 0.5, 0.0]))
        h = hill(-0.45, -3.0, 2.2)
        self.play(FadeIn(f), FadeIn(s), Create(h), run_time=2.0)
        la = label("AI draws", np.array([-3.0, 2.1, 0.0]))
        self.play(FadeIn(la), run_time=1.0)

        p = poster(x=2.6, y=0.1, w=2.7, h=4.0)
        hw = T("GARAGE SALE", size=36, bold=True).move_to(
            np.array([2.6, 1.3, 0.0]))
        d1 = Line(np.array([1.65, 0.7, 0.0]), np.array([3.55, 0.7, 0.0]),
                  color=INK, stroke_width=5)
        d2 = Line(np.array([1.65, 0.3, 0.0]), np.array([3.0, 0.3, 0.0]),
                  color=INK, stroke_width=5)
        self.play(Create(p), FadeIn(hw), Create(d1), Create(d2), run_time=2.5)
        lb = label("you write", np.array([2.6, 2.6, 0.0]))
        self.play(FadeIn(lb), run_time=1.0)

        arr = Arrow(np.array([-1.0, 0.2, 0.0]), np.array([1.05, 0.2, 0.0]),
                    color=INK, stroke_width=8, buff=0.15)
        self.play(Create(arr), run_time=1.2)
        top = label("split the job", np.array([0.0, 2.9, 0.0]))
        self.play(FadeIn(top), FadeIn(bug()), run_time=1.0)
        self.wait(3.0)


class B06_PrintCheck(Scene):
    """The print checklist: tall shape, dark on light, 3-second test."""

    def construct(self):
        p = poster(x=-1.6, y=0.1, w=3.0, h=4.4)
        hw = T("GARAGE SALE", size=40, bold=True).move_to(
            np.array([-1.6, 1.5, 0.0]))
        d1 = Line(np.array([-2.8, 0.9, 0.0]), np.array([-0.4, 0.9, 0.0]),
                  color=INK, stroke_width=5)
        d2 = Line(np.array([-2.8, 0.5, 0.0]), np.array([-1.0, 0.5, 0.0]),
                  color=INK, stroke_width=5)
        self.play(Create(p), FadeIn(hw), Create(d1), Create(d2), run_time=2.5)

        checks = [("tall shape", 1.9), ("dark on light", 0.7),
                  ("3-second test", -0.5)]
        for text, y in checks:
            c = check(np.array([1.7, y, 0.0]), scale=0.9)
            lab = label(text, np.array([3.75, y, 0.0]), fs=32)
            self.play(FadeIn(c), FadeIn(lab), run_time=1.8)

        hw2 = T("GARAGE SALE", size=46, bold=True).move_to(
            np.array([-1.6, 1.5, 0.0]))
        self.play(FadeIn(hw2), FadeOut(hw), FadeIn(bug()), run_time=1.2)
        self.wait(2.9)


class B07_Label(Scene):
    """The AI-made tag stamps onto the poster."""

    def construct(self):
        p = poster(x=-1.2, y=0.1)
        s = sun_dot(np.array([-1.9, -0.9, 0.0]))
        h = hill(-1.75, -1.0, 2.0)
        self.play(Create(p), FadeIn(s), Create(h), run_time=2.0)

        ring = Circle(radius=0.85, color=TERRA, stroke_width=6,
                      stroke_opacity=1).move_to(np.array([-0.1, 1.35, 0.0]))
        self.play(GrowFromCenter(ring), run_time=1.2)

        tag_r = RoundedRectangle(corner_radius=0.1, width=1.9, height=0.7,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=TERRA, stroke_width=4).move_to(
            np.array([-0.1, 1.35, 0.0])).rotate(0.12)
        tag_t = T("AI-made", size=34, bold=True).move_to(
            np.array([-0.1, 1.35, 0.0])).rotate(0.12)
        tag = VGroup(tag_r, tag_t)
        self.play(FadeIn(tag), FadeOut(ring), run_time=1.2)

        lab = label("say it", np.array([3.2, 1.6, 0.0]))
        ld = leader(np.array([2.9, 1.6, 0.0]), np.array([1.0, 1.45, 0.0]))
        self.play(FadeIn(lab), Create(ld), FadeIn(bug()), run_time=1.0)
        self.wait(2.6)


class BVDT_Recap(Scene):
    """Four numbered chips recap the film's spine."""

    def construct(self):
        p = poster(x=-3.4, y=0.1, w=2.6, h=3.9)
        self.play(Create(p), run_time=1.5)

        steps = [("say the job", 2.05), ("exact words", 1.0),
                 ("AI draws, you write", -0.05), ("label AI-made", -1.1)]
        for i, (text, y) in enumerate(steps):
            n = num_chip(i + 1, np.array([-0.5, y, 0.0]))
            c = chip(text, np.array([2.3, y, 0.0]),
                     w=3.0 if i == 2 else 2.5, fs=30)
            if i == 3:
                c[0].set_stroke(color=TERRA, width=4)
            last = (i == 3)
            if last:
                self.play(FadeIn(n), FadeIn(c), FadeIn(bug()), run_time=1.8)
            else:
                self.play(FadeIn(n), FadeIn(c), run_time=1.8)

        self.wait(3.0)
