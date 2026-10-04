"""scenes.py — Free vs paid: when to pay. (Humanitarians AI YouTube film)

14 Manim scenes, M01-M14, one per beat. Skill: ai-explainer.
House conventions: 16:9, safe-area coords (x within +-6.3, y within +-3.4),
Claude palette (cream stage, warm ink, terracotta accent), one idea per
beat, every on-screen word read aloud in its beat's narration, the
@NikBearBrown watermark bug on every scene.

Each scene adds at least one new non-text shape per play() so the static
QC gate sees evolving shape states; explicit FadeIn/Create/Write before
any .animate() motion.
"""
import numpy as np
from manim import *

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


def spark_dot(pos):
    return Dot(radius=0.09, color=TERRA, fill_opacity=1).move_to(pos)


def card(pos, w, h, fill=CARD, edge=INK, sw=4, radius=0.14):
    return RoundedRectangle(corner_radius=radius, width=w, height=h,
                            fill_color=fill, fill_opacity=1,
                            stroke_color=edge, stroke_width=sw).move_to(pos)


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


def P(x, y):
    return np.array([x, y, 0.0])


class M01_Bidea(Scene):
    """BIDEA — the hesitant writer corrects the membership framing."""

    def construct(self):
        card1 = card(P(0, 0.6), 8.6, 2.2)
        pen = RoundedRectangle(corner_radius=0.06, width=0.14, height=0.7,
                               fill_color=TERRA, fill_opacity=1,
                               stroke_width=0).move_to(P(-3.6, 0.6))
        self.play(FadeIn(card1), FadeIn(pen))
        line1 = T("Paid AI is for AI people.", size=40).move_to(P(0, 0.6))
        self.play(Write(line1), pen.animate.move_to(P(3.6, 0.6)))
        strike = Line(P(1.1, 0.62), P(3.8, 0.62), color=TERRA, stroke_width=10)
        self.play(Create(strike))
        card2 = card(P(0, 0.4), 9.6, 2.8)
        l2a = T("Paid AI is for people who", size=40).move_to(P(0, 1.05))
        l2b = T("keep hitting the wall.", size=40, color=TERRA,
                bold=True).move_to(P(0, 0.05))
        self.play(FadeIn(card2), FadeOut(card1), FadeOut(line1),
                  FadeOut(strike), FadeOut(pen))
        self.play(Write(l2a), Write(l2b))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M02_Bdefs(Scene):
    """BDEFS — four term cards land one by one."""

    def construct(self):
        defs = [
            ("free tier", ["the no-cost plan —", "real, but capped"]),
            ("usage limit", ["how much you can ask", "before it slows down",
                             "or stops you"]),
            ("model", ["the AI engine", "under the hood —",
                       "bigger ones", "think sharper"]),
            ("context", ["how much of your", "conversation the AI",
                         "can hold in its", "head at once"]),
        ]
        xs = [-4.7, -1.57, 1.57, 4.7]
        for i, (term, lines) in enumerate(defs):
            grp = VGroup(card(P(xs[i], 0.3), 2.9, 3.6))
            grp.add(T(term, size=30, bold=True).move_to(P(xs[i], 1.35)))
            for j, ln in enumerate(lines):
                grp.add(T(ln, size=24).move_to(P(xs[i], 0.55 - j * 0.5)))
            if i == 3:
                edge = RoundedRectangle(
                    corner_radius=0.14, width=2.9, height=3.6,
                    fill_opacity=0, stroke_color=TERRA,
                    stroke_width=6).move_to(P(xs[i], 0.3))
                grp.add(edge)
            self.play(FadeIn(grp))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M03_FreeTier(Scene):
    """B00 — the free tier: a real chat window with a meter that empties."""

    def construct(self):
        chat = card(P(-0.8, 0.9), 7.2, 3.6)
        msg1 = RoundedRectangle(corner_radius=0.1, width=5.6, height=0.28,
                                fill_color=GHOST, fill_opacity=1,
                                stroke_width=0).move_to(P(-0.8, 1.7))
        msg2 = RoundedRectangle(corner_radius=0.1, width=4.4, height=0.28,
                                fill_color=GHOST, fill_opacity=1,
                                stroke_width=0).move_to(P(-1.4, 1.2))
        self.play(FadeIn(chat), FadeIn(msg1), FadeIn(msg2))
        meter = RoundedRectangle(corner_radius=0.14, width=7.2, height=0.55,
                                 fill_opacity=0, stroke_color=INK,
                                 stroke_width=4).move_to(P(-0.8, -1.55))
        fill = RoundedRectangle(corner_radius=0.1, width=6.7, height=0.3,
                                fill_color=TERRA, fill_opacity=1,
                                stroke_width=0).move_to(P(-0.8, -1.55))
        msg3 = RoundedRectangle(corner_radius=0.1, width=5.0, height=0.28,
                                fill_color=GHOST, fill_opacity=1,
                                stroke_width=0).move_to(P(-1.1, 0.7))
        msg4 = RoundedRectangle(corner_radius=0.1, width=3.6, height=0.28,
                                fill_color=GHOST, fill_opacity=1,
                                stroke_width=0).move_to(P(-1.8, 0.2))
        self.play(FadeIn(meter), FadeIn(fill), FadeIn(msg3), FadeIn(msg4))
        note = card(P(-0.8, -2.75), 6.8, 0.95)
        note_t = T("limit reached — come back tomorrow", size=28).move_to(
            P(-0.8, -2.75))
        self.play(fill.animate.scale(0.06),
                  FadeIn(note), FadeIn(note_t))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M04_Wall(Scene):
    """B01 — every answer costs money; the sample tray fills, then stops."""

    def construct(self):
        tag = card(P(0, 2.7), 6.4, 0.95)
        tag_t = T("every answer costs money", size=30).move_to(P(0, 2.7))
        tray = Rectangle(width=8.0, height=1.7, fill_opacity=0,
                         stroke_color=INK, stroke_width=5).move_to(P(0, -0.7))
        self.play(FadeIn(tag), FadeIn(tag_t), FadeIn(tray))
        coins = []
        for i, x in enumerate([-3.0, 0.0, 3.0]):
            acard = card(P(x, 1.35), 2.2, 0.9)
            coin = Circle(radius=0.3, fill_color=TERRA, fill_opacity=1,
                          stroke_width=0).move_to(P(x, 1.35))
            self.play(FadeIn(acard), FadeIn(coin))
            self.play(coin.animate.move_to(P(x, -0.7)))
            coins.append(coin)
        coin4 = Circle(radius=0.3, fill_color=TERRA, fill_opacity=1,
                       stroke_width=0).move_to(P(0, 1.35))
        bar = Line(P(-4.0, 0.15), P(4.0, 0.15), color=TERRA, stroke_width=10)
        self.play(FadeIn(coin4))
        self.play(coin4.animate.move_to(P(0, 0.6)), Create(bar))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M05_FourThings(Scene):
    """B02 — the four things money buys, unlocking in a two-by-two grid."""

    def construct(self):
        items = ["a sharper model", "higher limits",
                 "longer memory", "early features"]
        pos = [P(-2.5, 1.35), P(2.5, 1.35), P(-2.5, -1.35), P(2.5, -1.35)]
        for p, label in zip(pos, items):
            grp = VGroup(card(p, 4.4, 2.2))
            grp.add(T(label, size=32, bold=True).move_to(p))
            grp.add(Dot(radius=0.12, color=TERRA,
                        fill_opacity=1).move_to(p + np.array([1.75, 0.75, 0])))
            self.play(FadeIn(grp))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M06_SharpModel(Scene):
    """B03 — hard question splits the panels; easy question does not."""

    def construct(self):
        eco = RoundedRectangle(corner_radius=0.16, width=4.6, height=3.4,
                               fill_opacity=0, stroke_color=DIM,
                               stroke_width=5).move_to(P(-2.7, 0.2))
        flag = RoundedRectangle(corner_radius=0.16, width=4.6, height=3.4,
                                fill_opacity=0, stroke_color=TERRA,
                                stroke_width=6).move_to(P(2.7, 0.2))
        eco_t = T("economy", size=30, color=DIM).move_to(P(-2.7, 1.35))
        flag_t = T("flagship", size=30, bold=True).move_to(P(2.7, 1.35))
        q1 = card(P(0, 2.75), 5.4, 1.0)
        q1_t = T("a hard question", size=32).move_to(P(0, 2.75))
        self.play(FadeIn(eco), FadeIn(flag), FadeIn(eco_t), FadeIn(flag_t),
                  FadeIn(q1), FadeIn(q1_t))
        self.play(FadeIn(x_mark(P(-2.7, -0.3), scale=1.2)),
                  FadeIn(check_mark(P(2.7, -0.3), scale=1.2)))
        q2 = card(P(0, 2.75), 5.4, 1.0)
        q2_t = T("an easy question", size=32).move_to(P(0, 2.75))
        self.play(FadeOut(q1), FadeOut(q1_t), FadeIn(q2), FadeIn(q2_t))
        self.play(FadeIn(check_mark(P(-2.7, -0.3), scale=1.2, color=INK)),
                  FadeIn(check_mark(P(2.7, -0.3), scale=1.2)))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M07_LimitMath(Scene):
    """B04 — the time the wall steals dwarfs the monthly fee."""

    def construct(self):
        axis = Line(P(-5.6, -2.2), P(5.6, -2.2), color=INK, stroke_width=5)
        left_box = RoundedRectangle(corner_radius=0.1, width=2.6, height=4.4,
                                    fill_opacity=0, stroke_color=INK,
                                    stroke_width=4).move_to(P(-2.6, 0.0))
        right_box = RoundedRectangle(corner_radius=0.1, width=2.6, height=1.1,
                                     fill_opacity=0, stroke_color=INK,
                                     stroke_width=4).move_to(P(2.6, -1.65))
        left_l = T("time the wall steals", size=28).move_to(P(-2.6, -2.75))
        right_l = T("the monthly fee", size=28).move_to(P(2.6, -2.75))
        self.play(FadeIn(axis), FadeIn(left_box), FadeIn(right_box),
                  FadeIn(left_l), FadeIn(right_l))
        left_fill = RoundedRectangle(corner_radius=0.06, width=2.2,
                                     height=4.0, fill_color=TERRA,
                                     fill_opacity=1,
                                     stroke_width=0).move_to(P(-2.6, 0.0))
        self.play(FadeIn(left_fill))
        right_fill = RoundedRectangle(corner_radius=0.06, width=2.2,
                                      height=0.7, fill_color=INK,
                                      fill_opacity=1,
                                      stroke_width=0).move_to(P(2.6, -1.65))
        self.play(FadeIn(right_fill))
        tag = card(P(0, 2.6), 5.6, 1.0)
        tag_t = T("paying is a refund", size=32, color=TERRA,
                  bold=True).move_to(P(0, 2.6))
        self.play(FadeIn(tag), FadeIn(tag_t))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M08_FreeEnough(Scene):
    """B05 — three checked rows: when free is the right answer."""

    def construct(self):
        rows = ["casual questions", "trying things out", "light use"]
        ys = [1.6, 0.3, -1.0]
        for label, y in zip(rows, ys):
            grp = VGroup(check_mark(P(-3.4, y), scale=1.0))
            grp.add(T(label, size=36).move_to(P(-1.5, y), aligned_edge=LEFT))
            self.play(FadeIn(grp))
        tag = card(P(0, -2.45), 3.4, 1.0, edge=TERRA, sw=5)
        tag_t = T("stay free", size=32, color=TERRA, bold=True).move_to(
            P(0, -2.45))
        self.play(FadeIn(tag), FadeIn(tag_t),
                  FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M09_Payoff(Scene):
    """B06 — four checked rows: when paying pays off."""

    def construct(self):
        rows = ["daily professional use", "long documents",
                "coding help", "you keep hitting the limit"]
        ys = [2.0, 0.9, -0.2, -1.3]
        for i, (label, y) in enumerate(zip(rows, ys)):
            col = TERRA if i == 3 else INK
            grp = VGroup(check_mark(P(-3.9, y), scale=1.0, color=col))
            grp.add(T(label, size=34).move_to(P(-2.0, y), aligned_edge=LEFT))
            self.play(FadeIn(grp))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M10_TwoQuestions(Scene):
    """B07 — the two-question flowchart: the whole film as a decision."""

    def construct(self):
        d1 = Polygon(P(0, 2.3), P(2.0, 1.3), P(0, 0.3), P(-2.0, 1.3),
                     fill_opacity=0, stroke_color=INK, stroke_width=5)
        d1_t = T("hit the wall weekly?", size=28).move_to(P(0, 1.3))
        self.play(FadeIn(d1), FadeIn(d1_t))
        no1 = Arrow(P(-2.0, 1.3), P(-3.1, 1.3), color=INK, stroke_width=6,
                    buff=0.1)
        no1_t = T("no", size=24).move_to(P(-2.55, 1.75))
        sf1 = card(P(-4.5, 1.3), 2.6, 0.9)
        sf1_t = T("stay free", size=26).move_to(P(-4.5, 1.3))
        yes1 = Arrow(P(0, 0.3), P(0, -0.45), color=TERRA, stroke_width=6,
                     buff=0.1)
        yes1_t = T("yes", size=24, color=TERRA).move_to(P(0.45, -0.1))
        self.play(FadeIn(no1), FadeIn(no1_t), FadeIn(sf1), FadeIn(sf1_t),
                  FadeIn(yes1), FadeIn(yes1_t))
        d2 = Polygon(P(0, -0.45), P(2.0, -1.45), P(0, -2.45), P(-2.0, -1.45),
                     fill_opacity=0, stroke_color=INK, stroke_width=5)
        d2a = T("hour of your time", size=26).move_to(P(0, -1.25))
        d2b = T("> the fee?", size=26).move_to(P(0, -1.7))
        no2 = Arrow(P(-2.0, -1.45), P(-3.1, -1.45), color=INK, stroke_width=6,
                    buff=0.1)
        no2_t = T("no", size=24).move_to(P(-2.55, -1.0))
        sf2 = card(P(-4.5, -1.45), 2.6, 0.9)
        sf2_t = T("stay free", size=26).move_to(P(-4.5, -1.45))
        yes2 = Arrow(P(2.0, -1.45), P(3.1, -1.45), color=TERRA, stroke_width=6,
                     buff=0.1)
        yes2_t = T("yes", size=24, color=TERRA).move_to(P(2.55, -1.0))
        pay = card(P(4.5, -1.45), 2.4, 1.0, edge=TERRA, sw=6)
        pay_t = T("pay", size=30, color=TERRA, bold=True).move_to(
            P(4.5, -1.45))
        self.play(FadeIn(d2), FadeIn(d2a), FadeIn(d2b),
                  FadeIn(no2), FadeIn(no2_t), FadeIn(sf2), FadeIn(sf2_t),
                  FadeIn(yes2), FadeIn(yes2_t), FadeIn(pay), FadeIn(pay_t))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M11_Trap(Scene):
    """B08 — three idle months, one forgotten coin; the one-month rule."""

    def construct(self):
        c1 = card(P(-3.6, 0.6), 3.2, 2.4)
        coin = Circle(radius=0.5, fill_color=TERRA, fill_opacity=1,
                      stroke_width=0).move_to(P(-3.6, 0.6))
        self.play(FadeIn(c1), FadeIn(coin))
        c2 = card(P(0, 0.6), 3.2, 2.4)
        c3 = card(P(3.6, 0.6), 3.2, 2.4)
        self.play(FadeIn(c2), FadeIn(c3))
        self.play(FadeIn(x_mark(P(-3.6, 0.6), scale=1.1, color=DIM)),
                  FadeIn(x_mark(P(0, 0.6), scale=1.1, color=DIM)),
                  FadeIn(x_mark(P(3.6, 0.6), scale=1.1, color=DIM)),
                  coin.animate.scale(0.55))
        tag = card(P(0, -2.2), 7.0, 1.0)
        tag_t = T("one-month experiment first", size=32, color=TERRA,
                  bold=True).move_to(P(0, -2.2))
        self.play(FadeIn(tag), FadeIn(tag_t))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M12_Verdict(Scene):
    """BVDT — five recap bullets, the framework on one screen."""

    def construct(self):
        bullets = [
            ["Free is the real thing — with a meter."],
            ["Paid buys four things:",
             "sharper model, higher limits,",
             "longer memory, early features."],
            ["Sharper model matters on hard questions."],
            ["The test: weekly wall + time worth more",
             "than the fee — pay. Else stay free."],
            ["One-month experiment before annual."],
        ]
        ys = [2.35, 1.3, 0.25, -0.9, -2.05]
        for lines, y in zip(bullets, ys):
            grp = VGroup(Dot(radius=0.11, color=TERRA,
                             fill_opacity=1).move_to(P(-5.6, y + 0.12)))
            for j, ln in enumerate(lines):
                grp.add(T(ln, size=30).move_to(
                    P(-5.05, y - j * 0.52), aligned_edge=LEFT))
            self.play(FadeIn(grp))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M13_YourTurn(Scene):
    """BHTF — the viewer prompt card plus the two-question chips."""

    def construct(self):
        title = T("Your turn.", size=54, bold=True).move_to(P(0, 2.55))
        pcard = card(P(0, 0.35), 10.6, 3.0)
        self.play(Write(title), FadeIn(pcard))
        lines = ["Here is what I used you for this week:",
                 "(list your tasks)",
                 "at what point would paying make sense",
                 "for someone like me?"]
        for j, ln in enumerate(lines):
            self.play(Write(T(ln, size=28).move_to(P(0, 1.25 - j * 0.55))))
        chip1 = card(P(-2.1, -2.35), 3.6, 0.85)
        chip1_t = T("weekly wall?", size=26).move_to(P(-2.1, -2.35))
        self.play(FadeIn(chip1), FadeIn(chip1_t))
        chip2 = card(P(2.1, -2.35), 3.6, 0.85)
        chip2_t = T("time vs fee", size=26).move_to(P(2.1, -2.35))
        self.play(FadeIn(chip2), FadeIn(chip2_t),
                  FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))


class M14_Outro(Scene):
    """BOUT — locked outro: title, terracotta rule, handle."""

    def construct(self):
        t1 = T("Free vs paid:", size=64, bold=True).move_to(P(0, 1.0))
        t2 = T("when to pay", size=64, bold=True).move_to(P(0, 0.05))
        self.play(Write(t1), Write(t2),
                  FadeIn(spark_dot(P(0, 2.3))))
        rule = Line(P(-3.2, -0.85), P(3.2, -0.85), color=TERRA,
                    stroke_width=8)
        self.play(Create(rule))
        dot = Circle(radius=0.16, fill_color=TERRA, fill_opacity=1,
                     stroke_width=0).move_to(P(1.62, 0.02))
        handle = T("@NikBearBrown", size=30).move_to(P(0, -1.85))
        self.play(FadeIn(dot), FadeIn(handle))
        self.play(FadeIn(bug()), FadeIn(spark_dot(P(5.95, -3.05))))
