"""scenes.py — AI is a slot machine. (Humanitarians AI YouTube film)

16 Manim scenes, M01-M16, one per beat. Skill: show-tell.
House conventions: 16:9, safe-area coords (x within +-6.3, y within +-3.4),
show-tell Claude palette (cream stage, warm ink, terracotta accent), one
image per beat with minimal labels, every on-screen word read aloud in its
beat. The slot machine is the recurring cast object: cabinet, reel window,
answer tray, lever.

Each scene adds at least one new non-text shape per play() so the static
QC gate sees evolving shape states; explicit FadeIn/Create before any
.animate() motion.
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


def answer_card(text, pos, w=2.2, h=0.85, fs=28, fill=CARD):
    r = RoundedRectangle(corner_radius=0.12, width=w, height=h,
                         fill_color=fill, fill_opacity=1,
                         stroke_color=INK, stroke_width=3).move_to(pos)
    t = T(text, size=fs).move_to(pos)
    return VGroup(r, t)


def plain_card(pos, w=1.6, h=0.62, fill=CARD):
    return RoundedRectangle(corner_radius=0.1, width=w, height=h,
                            fill_color=fill, fill_opacity=1,
                            stroke_color=INK, stroke_width=3).move_to(pos)


def slot_machine(x=0.0, y=0.0, s=1.0):
    """Front-view slot machine: cabinet, reel window, tray, lever."""
    body = RoundedRectangle(
        corner_radius=0.22 * s, width=3.2 * s, height=4.4 * s,
        fill_color=KRAFT, fill_opacity=1, stroke_color=INK,
        stroke_width=6).move_to(np.array([x, y, 0.0]))
    window = Rectangle(
        width=2.5 * s, height=1.0 * s, fill_color=DARK, fill_opacity=1,
        stroke_color=INK, stroke_width=4).move_to(np.array([x, y + 1.25 * s, 0.0]))
    reels = [RoundedRectangle(
        corner_radius=0.08 * s, width=0.68 * s, height=0.8 * s,
        fill_color=GHOST, fill_opacity=1, stroke_width=0
    ).move_to(np.array([x + (i - 1) * 0.8 * s, y + 1.25 * s, 0.0]))
        for i in range(3)]
    tray = Rectangle(
        width=2.5 * s, height=0.62 * s, fill_color=DARK, fill_opacity=1,
        stroke_color=INK, stroke_width=4).move_to(np.array([x, y - 1.35 * s, 0.0]))
    arm = Line(np.array([x + 1.6 * s, y + 0.4 * s, 0.0]),
               np.array([x + 2.3 * s, y + 1.3 * s, 0.0]),
               color=INK, stroke_width=10)
    knob = Circle(radius=0.26 * s, fill_color=TERRA, fill_opacity=1,
                  stroke_width=0).move_to(np.array([x + 2.3 * s, y + 1.3 * s, 0.0]))
    group = VGroup(body, window, *reels, tray, arm, knob)
    return {"group": group, "body": body, "window": window, "reels": reels,
            "tray": tray, "arm": arm, "knob": knob,
            "lever": VGroup(arm, knob), "x": x, "y": y, "s": s}


def check_mark(pos, scale=1.0, color=TERRA):
    g = VGroup(
        Line(np.array([0, 0, 0]), np.array([0.5, -0.3, 0]),
             color=color, stroke_width=12),
        Line(np.array([0.5, -0.3, 0]), np.array([1.3, 0.4, 0]),
             color=color, stroke_width=12),
    ).scale(scale).move_to(pos)
    return g


def x_mark(pos, scale=1.0, color=TERRA):
    g = VGroup(
        Line(np.array([-0.45, 0.45, 0]), np.array([0.45, -0.45, 0]),
             color=color, stroke_width=12),
        Line(np.array([-0.45, -0.45, 0]), np.array([0.45, 0.45, 0]),
             color=color, stroke_width=12),
    ).scale(scale).move_to(pos)
    return g


def bullet(pos, color=TERRA):
    return Circle(radius=0.1, fill_color=color, fill_opacity=1,
                  stroke_width=0).move_to(pos)


def plate_tag(text, pos, fs=28, color=INK, bg=CARD):
    plate = RoundedRectangle(corner_radius=0.14, width=len(text) * 0.2 + 0.8,
                             height=0.72, fill_color=bg, fill_opacity=1,
                             stroke_color=color, stroke_width=3).move_to(pos)
    t = T(text, size=fs, color=color).move_to(pos)
    return VGroup(plate, t)


class M01_Bidea(Scene):
    def construct(self):
        self.add(bug())
        paper = RoundedRectangle(corner_radius=0.25, width=9.6, height=3.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=4)
        cursor = Dot(radius=0.14, color=TERRA, fill_opacity=1).move_to(
            np.array([-4.2, 0.5, 0.0]))
        self.play(FadeIn(paper), FadeIn(cursor), run_time=0.9)
        t_a = T("AI is a ", size=44).move_to(np.array([-2.2, 0.5, 0.0]))
        t_b = T("truth machine.", size=44).next_to(t_a, RIGHT, buff=0.15)
        self.play(Write(t_a), run_time=0.8)
        self.play(Write(t_b), run_time=0.8)
        strike = Line(t_b.get_left() + np.array([-0.15, 0.0, 0.0]),
                      t_b.get_right() + np.array([0.15, 0.0, 0.0]),
                      color=TERRA, stroke_width=9)
        self.play(Create(strike), run_time=0.7)
        self.play(FadeOut(t_a), FadeOut(t_b), FadeOut(strike), run_time=0.7)
        t_c = T("AI is a slot machine.", size=44).move_to(np.array([0.0, 0.5, 0.0]))
        self.play(Write(t_c), run_time=1.0)
        self.wait(14.0)


class M02_Bdefs(Scene):
    def construct(self):
        self.add(bug())
        terms = ["prompt", "probabilistic", "hallucination", "the AI gambler"]
        defs = ["what you type to the AI", "same input, different answer",
                "a confident wrong answer", "pull many, keep the best"]
        xs = [-4.8, -1.6, 1.6, 4.8]
        for i, (w, d, x) in enumerate(zip(terms, defs, xs)):
            box = RoundedRectangle(corner_radius=0.2, width=2.9, height=2.3,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK, stroke_width=3).move_to(
                                       np.array([x, 0.4, 0.0]))
            edge = TERRA if i == 3 else INK
            strip = Rectangle(width=2.9, height=0.22, fill_color=edge,
                              fill_opacity=1, stroke_width=0).move_to(
                                  np.array([x, 1.43, 0.0]))
            head = T(w, size=30, bold=True).move_to(np.array([x, 0.75, 0.0]))
            sub = T(d, size=24, color=DIM).move_to(np.array([x, -0.05, 0.0]))
            self.play(FadeIn(VGroup(box, strip, head, sub)), run_time=0.8)
        self.wait(12.0)


class M03_Machine(Scene):
    def construct(self):
        self.add(bug())
        m = slot_machine(0.0, -0.3, 1.0)
        shadow = Ellipse(width=4.4, height=0.5, fill_color=GHOST,
                         fill_opacity=1, stroke_width=0).move_to(
                             np.array([0.0, -2.85, 0.0]))
        self.play(FadeIn(shadow), run_time=0.6)
        self.play(Create(m["body"]), run_time=0.9)
        self.play(FadeIn(m["window"]), FadeIn(VGroup(*m["reels"])), run_time=0.7)
        self.play(FadeIn(m["tray"]), run_time=0.6)
        self.play(GrowFromCenter(m["lever"]), run_time=0.7)
        pin = T("prompt in", size=30).move_to(np.array([-2.6, 2.6, 0.0]))
        arr1 = Arrow(np.array([-1.4, 2.55, 0.0]), np.array([-0.4, 2.15, 0.0]),
                     color=INK, stroke_width=6, buff=0.1)
        pout = T("answer out", size=30).move_to(np.array([2.9, -2.6, 0.0]))
        arr2 = Arrow(np.array([1.6, -2.35, 0.0]), np.array([2.2, -2.55, 0.0]),
                     color=INK, stroke_width=6, buff=0.1)
        self.play(FadeIn(pin), GrowArrow(arr1), run_time=0.7)
        self.play(FadeIn(pout), GrowArrow(arr2), run_time=0.7)
        self.wait(6.0)


class M04_Probabilistic(Scene):
    def construct(self):
        self.add(bug())
        m = slot_machine(-1.6, -0.4, 0.92)
        self.play(FadeIn(m["group"]), run_time=0.8)
        prompt = answer_card("write about the sea", np.array([2.9, 2.3, 0.0]),
                             w=3.4, h=0.9, fs=28)
        pin = T("same prompt", size=26, color=DIM).move_to(np.array([2.9, 2.95, 0.0]))
        self.play(FadeIn(prompt), FadeIn(pin), run_time=0.8)
        answers = ["a poem", "a list", "a joke"]
        for i, a in enumerate(answers):
            card = answer_card(a, np.array([-3.8 + i * 2.2, -2.75, 0.0]),
                               w=2.0, h=0.75, fs=26)
            self.play(m["lever"].animate.shift(DOWN * 0.7 * m["s"]), run_time=0.5)
            self.play(FadeIn(card), run_time=0.5)
            self.play(m["lever"].animate.shift(UP * 0.7 * m["s"]), run_time=0.5)
        self.wait(9.0)

class M05_Stages(Scene):
    def construct(self):
        self.add(bug())
        names = ["denial", "anger", "bargaining", "depression", "acceptance"]
        xs = [-5.0, -2.5, 0.0, 2.5, 5.0]
        plates = []
        for x in xs:
            p = RoundedRectangle(corner_radius=0.16, width=2.15, height=1.1,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(
                                     np.array([x, 0.5, 0.0]))
            plates.append(p)
        self.play(*[FadeIn(p) for p in plates], run_time=0.9)
        for i, (w, x) in enumerate(zip(names, xs)):
            lab = T(w, size=28, bold=(i == 4)).move_to(np.array([x, -0.45, 0.0]))
            self.play(FadeIn(lab), run_time=0.5)
        for i, x in enumerate(xs[:3]):
            dot = bullet(np.array([x, 1.35, 0.0]))
            self.play(FadeIn(dot), run_time=0.5)
        self.play(FadeIn(bullet(np.array([xs[3], 1.35, 0.0]))), run_time=0.6)
        glow = bullet(np.array([xs[4], 1.35, 0.0])).scale(1.6)
        self.play(FadeIn(glow), run_time=0.7)
        self.wait(8.0)


class M06_Denial(Scene):
    def construct(self):
        self.add(bug())
        m = slot_machine(-3.2, -0.2, 0.62)
        self.play(FadeIn(m["group"]), run_time=0.8)
        card = answer_card("one bad answer", np.array([-3.2, -2.5, 0.0]),
                           w=2.9, h=0.85, fs=28)
        self.play(FadeIn(card), run_time=0.7)
        stamp = x_mark(np.array([-3.2, -2.5, 0.0]), scale=1.1)
        self.play(GrowFromCenter(stamp), run_time=0.7)
        loop = CurvedArrow(np.array([0.2, -2.9, 0.0]), np.array([0.2, -1.6, 0.0]),
                           angle=-2.6, color=INK, stroke_width=6)
        self.play(Create(loop), run_time=0.8)
        lab = T("it's useless", size=32).move_to(np.array([2.6, -2.25, 0.0]))
        self.play(FadeIn(lab), run_time=0.6)
        self.play(loop.animate.shift(RIGHT * 0.25), run_time=0.5)
        self.play(loop.animate.shift(LEFT * 0.25), run_time=0.5)
        self.wait(7.0)


class M07_Anger(Scene):
    def construct(self):
        self.add(bug())
        m = slot_machine(-2.6, -0.3, 0.8)
        self.play(FadeIn(m["group"]), run_time=0.8)
        phone = RoundedRectangle(corner_radius=0.25, width=1.9, height=3.6,
                                 fill_color=DARK, fill_opacity=1,
                                 stroke_color=INK, stroke_width=4).move_to(
                                     np.array([3.8, -0.2, 0.0]))
        self.play(FadeIn(phone), run_time=0.7)
        for i in range(3):
            shot = Rectangle(width=1.5, height=0.8, fill_color=GHOST,
                             fill_opacity=1, stroke_width=0).move_to(
                                 np.array([3.8, 0.9 - i * 1.0, 0.0]))
            self.play(FadeIn(shot), run_time=0.5)
        for i in range(3):
            bolt = Polygon(
                np.array([3.0 - i * 0.3, 1.2 - i * 0.7, 0.0]),
                np.array([1.6 - i * 0.3, 0.4 - i * 0.7, 0.0]),
                np.array([2.2 - i * 0.3, 0.2 - i * 0.7, 0.0]),
                np.array([0.9 - i * 0.3, -0.6 - i * 0.7, 0.0]),
                fill_color=TERRA, fill_opacity=1, stroke_width=0)
            self.play(FadeIn(bolt), run_time=0.4)
        self.play(m["group"].animate.shift(RIGHT * 0.3), run_time=0.3)
        self.play(m["group"].animate.shift(LEFT * 0.6), run_time=0.3)
        self.play(m["group"].animate.shift(RIGHT * 0.3), run_time=0.3)
        self.wait(6.0)


class M08_Bargaining(Scene):
    def construct(self):
        self.add(bug())
        plinth = RoundedRectangle(corner_radius=0.15, width=3.0, height=0.7,
                                  fill_color=KRAFT_D, fill_opacity=1,
                                  stroke_color=INK, stroke_width=4).move_to(
                                      np.array([0.0, -2.2, 0.0]))
        self.play(FadeIn(plinth), run_time=0.7)
        arm = Line(np.array([0.0, -1.85, 0.0]), np.array([0.0, 0.6, 0.0]),
                   color=INK, stroke_width=12)
        knob = Circle(radius=0.34, fill_color=TERRA, fill_opacity=1,
                      stroke_width=0).move_to(np.array([0.0, 0.95, 0.0]))
        self.play(Create(arm), GrowFromCenter(knob), run_time=0.8)
        mitt = Circle(radius=0.55, fill_color=KRAFT, fill_opacity=1,
                      stroke_color=INK, stroke_width=4).move_to(
                          np.array([0.9, 0.5, 0.0]))
        self.play(FadeIn(mitt), run_time=0.6)
        self.play(mitt.animate.shift(LEFT * 0.5 + UP * 0.3), run_time=0.6)
        dial1 = Circle(radius=0.7, color=INK, stroke_width=5).move_to(
            np.array([-3.4, 0.6, 0.0]))
        tick1 = Line(np.array([-3.4, 0.6, 0.0]), np.array([-3.4, 1.2, 0.0]),
                     color=TERRA, stroke_width=8)
        dial2 = Circle(radius=0.7, color=INK, stroke_width=5).move_to(
            np.array([3.4, 0.6, 0.0]))
        tick2 = Line(np.array([3.4, 0.6, 0.0]), np.array([3.9, 1.0, 0.0]),
                     color=TERRA, stroke_width=8)
        self.play(Create(dial1), Create(tick1), run_time=0.6)
        self.play(Create(dial2), Create(tick2), run_time=0.6)
        lab = T("the perfect prompt", size=34).move_to(np.array([0.0, -3.0, 0.0]))
        self.play(FadeIn(lab), run_time=0.7)
        self.wait(8.0)


class M09_Depression(Scene):
    def construct(self):
        self.add(bug())
        m = slot_machine(-3.0, -0.2, 0.62)
        self.play(FadeIn(m["group"]), run_time=0.8)
        face = Circle(radius=1.35, fill_color=CARD, fill_opacity=1,
                      stroke_color=INK, stroke_width=5).move_to(
                          np.array([2.8, 0.5, 0.0]))
        self.play(Create(face), run_time=0.7)
        hand1 = Line(np.array([2.8, 0.5, 0.0]), np.array([2.8, 1.5, 0.0]),
                     color=INK, stroke_width=8)
        hand2 = Line(np.array([2.8, 0.5, 0.0]), np.array([3.6, 0.5, 0.0]),
                     color=INK, stroke_width=8)
        self.play(FadeIn(VGroup(hand1, hand2)), run_time=0.6)
        self.play(hand1.animate.rotate(4.2, about_point=np.array([2.8, 0.5, 0.0])),
                  hand2.animate.rotate(2.1, about_point=np.array([2.8, 0.5, 0.0])),
                  run_time=1.2)
        lab = T("6 hours", size=32).move_to(np.array([2.8, -1.5, 0.0]))
        ghost_card = RoundedRectangle(corner_radius=0.1, width=1.9, height=0.6,
                                      fill_opacity=0, stroke_color=DIM,
                                      stroke_width=3, stroke_dash_array=[0.12, 0.08]
                                      ).move_to(np.array([-3.0, -2.5, 0.0]))
        self.play(FadeIn(lab), FadeIn(ghost_card), run_time=0.7)
        self.play(FadeOut(ghost_card),
                  m["lever"].animate.shift(DOWN * 0.6 * m["s"]), run_time=0.8)
        self.wait(6.0)


class M10_Gambler(Scene):
    def construct(self):
        self.add(bug())
        m = slot_machine(-2.8, -0.4, 0.85)
        self.play(FadeIn(m["group"]), run_time=0.8)
        pile = []
        for i in range(6):
            c = plain_card(np.array([1.8 + (i % 3) * 1.75, -2.2 - (i // 3) * 0.75, 0.0]),
                           w=1.6, h=0.62)
            pile.append(c)
        self.play(m["lever"].animate.shift(DOWN * 0.6 * m["s"]), run_time=0.4)
        self.play(*[FadeIn(c) for c in pile[:3]], run_time=0.6)
        self.play(m["lever"].animate.shift(UP * 0.6 * m["s"]), run_time=0.4)
        self.play(m["lever"].animate.shift(DOWN * 0.6 * m["s"]), run_time=0.4)
        self.play(*[FadeIn(c) for c in pile[3:]], run_time=0.6)
        self.play(m["lever"].animate.shift(UP * 0.6 * m["s"]), run_time=0.4)
        best = []
        for i in range(5):
            c = plain_card(np.array([-4.4 + i * 1.15, 2.35, 0.0]), w=1.05, h=0.62)
            best.append(c)
        self.play(*[FadeIn(c) for c in best], run_time=0.8)
        checks = [check_mark(np.array([-4.4 + i * 1.15, 2.35, 0.0]), scale=0.45)
                  for i in range(5)]
        self.play(*[GrowFromCenter(ch) for ch in checks], run_time=0.8)
        self.play(*[FadeOut(c) for c in pile], run_time=0.7)
        self.wait(6.0)

class M11_ThreeVersions(Scene):
    def construct(self):
        self.add(bug())
        m = slot_machine(-3.4, -0.5, 0.7)
        self.play(FadeIn(m["group"]), run_time=0.8)
        prompt = answer_card("give me three different angles on this",
                             np.array([2.4, 2.5, 0.0]), w=4.6, h=0.95, fs=26)
        self.play(FadeIn(prompt), run_time=0.8)
        cards = [plain_card(np.array([0.6 + i * 2.05, -0.6, 0.0]), w=1.9, h=0.8)
                 for i in range(3)]
        self.play(*[FadeIn(c) for c in cards], run_time=0.9)
        nums = [T(str(i + 1), size=30, bold=True).move_to(
            np.array([0.6 + i * 2.05, -0.6, 0.0])) for i in range(3)]
        self.play(*[FadeIn(n) for n in nums], run_time=0.6)
        tag = plate_tag("ask for three", np.array([2.4, -2.5, 0.0]))
        self.play(FadeIn(tag), run_time=0.7)
        self.wait(8.0)


class M12_Intern(Scene):
    def construct(self):
        self.add(bug())
        wrong = answer_card("something wrong", np.array([-3.6, 0.8, 0.0]),
                            w=3.2, h=0.95, fs=28)
        self.play(FadeIn(wrong), run_time=0.7)
        stamp = x_mark(np.array([-3.6, 0.8, 0.0]), scale=1.0)
        self.play(GrowFromCenter(stamp), run_time=0.6)
        arc = CurvedArrow(np.array([-1.8, 0.8, 0.0]), np.array([0.6, 0.8, 0.0]),
                          angle=-1.1, color=INK, stroke_width=6)
        self.play(Create(arc), run_time=0.7)
        better = plain_card(np.array([2.6, 0.8, 0.0]), w=3.0, h=0.95)
        self.play(FadeIn(better), run_time=0.7)
        bubble = RoundedRectangle(corner_radius=0.3, width=5.6, height=1.25,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=INK, stroke_width=3).move_to(
                                      np.array([0.0, -1.8, 0.0]))
        btext = T("ask me clarifying questions", size=30).move_to(
            np.array([0.0, -1.8, 0.0]))
        self.play(FadeIn(VGroup(bubble, btext)), run_time=0.8)
        chk = check_mark(np.array([3.6, -1.8, 0.0]), scale=0.8)
        self.play(GrowFromCenter(chk), run_time=0.7)
        self.wait(9.0)


class M13_Batches(Scene):
    def construct(self):
        self.add(bug())
        cards = []
        for i in range(5):
            fill = GHOST if i in (1, 3) else CARD
            c = plain_card(np.array([-4.4 + i * 2.2, 0.3, 0.0]),
                           w=2.0, h=0.85, fill=fill)
            cards.append(c)
        self.play(*[FadeIn(c) for c in cards], run_time=0.9)
        fresh = [plain_card(np.array([-4.4 + i * 2.2, 0.3, 0.0]),
                            w=2.0, h=0.85) for i in (1, 3)]
        self.play(FadeOut(cards[1]), FadeOut(cards[3]), run_time=0.6)
        self.play(*[FadeIn(c) for c in fresh], run_time=0.7)
        checks = [check_mark(np.array([-4.4 + i * 2.2, 0.3, 0.0]), scale=0.55)
                  for i in range(5)]
        self.play(*[GrowFromCenter(ch) for ch in checks], run_time=0.8)
        tag = plate_tag("pull enough times", np.array([0.0, -2.3, 0.0]))
        self.play(FadeIn(tag), run_time=0.7)
        self.wait(8.0)


class M14_Recap(Scene):
    def construct(self):
        self.add(bug())
        lines = ["probabilistic: same prompt, new answer",
                 "denial, anger, bargaining, depression,",
                 "then acceptance",
                 "three versions, manage it, think in batches"]
        for i, s in enumerate(lines):
            y = 1.6 - i * 1.05
            dot = bullet(np.array([-5.6, y, 0.0]))
            txt = T(s, size=30).move_to(np.array([-5.2, y, 0.0]),
                                        aligned_edge=LEFT)
            self.play(FadeIn(dot), FadeIn(txt), run_time=0.9)
        self.wait(10.0)


class M15_YourTurn(Scene):
    def construct(self):
        self.add(bug())
        card = RoundedRectangle(corner_radius=0.3, width=10.4, height=5.2,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=4)
        self.play(FadeIn(card), run_time=0.8)
        head = T("Your turn.", size=40, bold=True).move_to(np.array([0.0, 1.9, 0.0]))
        self.play(FadeIn(head), run_time=0.6)
        lines = ["give me five different versions of this,",
                 "then ask me clarifying questions",
                 "about which one to keep."]
        for i, s in enumerate(lines):
            t = T(s, size=28).move_to(np.array([0.0, 0.9 - i * 0.62, 0.0]))
            self.play(Write(t), run_time=0.7)
        c1 = check_mark(np.array([-3.4, -1.7, 0.0]), scale=0.7)
        l1 = T("keep the best", size=28).move_to(np.array([-2.55, -1.7, 0.0]),
                                                 aligned_edge=LEFT)
        c2 = check_mark(np.array([0.9, -1.7, 0.0]), scale=0.7)
        l2 = T("trash the rest", size=28).move_to(np.array([1.75, -1.7, 0.0]),
                                                  aligned_edge=LEFT)
        self.play(GrowFromCenter(c1), FadeIn(l1), run_time=0.7)
        self.play(GrowFromCenter(c2), FadeIn(l2), run_time=0.7)
        self.wait(10.0)


class M16_Outro(Scene):
    def construct(self):
        title = T("AI is a slot machine", size=72, bold=True)
        self.play(Write(title), run_time=1.2)
        rule = Line(title.get_left() + np.array([0.0, -0.75, 0.0]),
                    title.get_right() + np.array([0.0, -0.75, 0.0]),
                    color=TERRA, stroke_width=7)
        self.play(Create(rule), run_time=0.6)
        dot = Dot(radius=0.14, color=TERRA, fill_opacity=1).move_to(
            title.get_right() + np.array([-0.1, -0.5, 0.0]))
        self.play(FadeIn(dot), run_time=0.5)
        handle = T("@NikBearBrown", size=36).move_to(np.array([0.0, -1.9, 0.0]))
        self.play(FadeIn(handle), run_time=0.8)
        self.wait(4.0)
