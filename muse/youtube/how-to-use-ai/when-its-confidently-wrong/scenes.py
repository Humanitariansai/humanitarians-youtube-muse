"""scenes.py — When it's confidently wrong. (Humanitarians AI YouTube film)

14 Manim scenes, M01-M14, one per beat. Skill: ai-explainer.
House conventions: 16:9, safe-area coords (x within +-6.3, y within +-3.4),
ai-explainer Claude palette (cream stage, warm ink, terracotta accent), one
image per beat with minimal labels, every on-screen word read aloud in its
beat. The chat window (cream card, kraft header, user/AI bubbles, composer
strip) is the recurring cast object.

Each scene adds at least one new non-text shape per play() so the static
QC gate sees evolving shape states; explicit FadeIn/Create/GrowFromCenter
before any .animate() motion.
"""
import numpy as np
from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.background_color = "#F2F0E9"

# ---- ai-explainer Claude palette ----
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


def chat_window(x=0.0, y=0.1, s=1.0, w=7.6, h=4.4, title="new chat"):
    """The recurring cast object: a chat window with header and composer."""
    body = RoundedRectangle(corner_radius=0.22 * s, width=w * s, height=h * s,
                            fill_color=CARD, fill_opacity=1, stroke_color=INK,
                            stroke_width=4).move_to(np.array([x, y, 0.0]))
    top = y + h * s / 2
    bot = y - h * s / 2
    divider = Line(np.array([x - w * s / 2 + 0.25, top - 0.62 * s, 0.0]),
                   np.array([x + w * s / 2 - 0.25, top - 0.62 * s, 0.0]),
                   color=GHOST, stroke_width=3)
    head = T(title, size=26, color=DIM).move_to(
        np.array([x - w * s / 2 + 1.15 * s, top - 0.31 * s, 0.0]),
        aligned_edge=LEFT)
    composer = RoundedRectangle(corner_radius=0.14 * s, width=w * s - 0.9 * s,
                                height=0.62 * s, fill_color=STAGE,
                                fill_opacity=1, stroke_color=DIM,
                                stroke_width=2).move_to(
                                    np.array([x, bot + 0.5 * s, 0.0]))
    group = VGroup(body, divider, head, composer)
    return {"group": group, "body": body, "divider": divider,
            "composer": composer, "x": x, "y": y, "s": s,
            "top": top, "bot": bot, "w": w * s, "h": h * s}


def user_bubble(text, x, y, s=1.0, fs=26):
    """Right-aligned user bubble, kraft fill."""
    plate = RoundedRectangle(corner_radius=0.16 * s, width=len(text) * 0.185 * s + 0.7 * s,
                             height=0.72 * s, fill_color=KRAFT, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(
                                 np.array([x, y, 0.0]))
    t = T(text, size=fs, color=INK).move_to(np.array([x, y, 0.0]))
    return VGroup(plate, t)


def ai_bubble(text, x, y, s=1.0, fs=26, w=None):
    """Left-aligned AI bubble, card fill."""
    width = w if w else len(text) * 0.185 * s + 0.7 * s
    plate = RoundedRectangle(corner_radius=0.16 * s, width=width,
                             height=0.72 * s, fill_color="#FFFFFF",
                             fill_opacity=1, stroke_color=INK,
                             stroke_width=2).move_to(np.array([x, y, 0.0]))
    t = T(text, size=fs, color=INK).move_to(np.array([x, y, 0.0]))
    return VGroup(plate, t)


def gauge(label, pos, frac, fill=TERRA):
    """A labelled fill gauge: track + fill bar."""
    track = RoundedRectangle(corner_radius=0.12, width=3.6, height=0.5,
                             fill_color=GHOST, fill_opacity=1,
                             stroke_width=0).move_to(pos)
    bar = Rectangle(width=3.6 * frac, height=0.5, fill_color=fill,
                    fill_opacity=1, stroke_width=0).move_to(
                        np.array([track.get_left()[0] + 3.6 * frac / 2,
                                  pos[1], 0.0]))
    lab = T(label, size=26).move_to(np.array([pos[0], pos[1] + 0.62, 0.0]))
    return VGroup(track, bar, lab), track, bar


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
        Line(np.array([-0.45, -0.45, 0]), np.array([0.45, -0.45, 0]),
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


def word_chip(word, pos):
    plate = RoundedRectangle(corner_radius=0.12, width=len(word) * 0.19 + 0.6,
                             height=0.62, fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    t = T(word, size=26).move_to(pos)
    return VGroup(plate, t)


class M01_B00(Scene):
    def construct(self):
        self.add(bug())
        composer = RoundedRectangle(corner_radius=0.22, width=9.6, height=2.7,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK, stroke_width=4).move_to(
                                        np.array([0.0, 0.3, 0.0]))
        cursor = Dot(radius=0.14, color=TERRA, fill_opacity=1).move_to(
            np.array([-4.2, 0.9, 0.0]))
        self.play(FadeIn(composer), FadeIn(cursor), run_time=0.9)
        q1 = T("Why does the AI insist", size=34).move_to(np.array([-1.4, 0.9, 0.0]))
        q2 = T("when it's wrong?", size=34).move_to(np.array([-1.4, 0.15, 0.0]))
        send = Polygon(np.array([3.6, 0.1, 0.0]), np.array([4.5, 0.55, 0.0]),
                       np.array([3.6, 1.0, 0.0]),
                       fill_color=TERRA, fill_opacity=1, stroke_width=0)
        self.play(Write(q1), Write(q2), FadeIn(send), run_time=1.2)
        border = RoundedRectangle(corner_radius=0.28, width=9.9, height=3.0,
                                  fill_opacity=0, stroke_color=TERRA,
                                  stroke_width=5).move_to(np.array([0.0, 0.3, 0.0]))
        self.play(FadeIn(border), FadeOut(cursor), run_time=0.8)
        self.wait(18.0)


class M02_B01(Scene):
    def construct(self):
        self.add(bug())
        paper = RoundedRectangle(corner_radius=0.25, width=10.4, height=3.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=4)
        cursor = Dot(radius=0.14, color=TERRA, fill_opacity=1).move_to(
            np.array([-4.6, 0.6, 0.0]))
        self.play(FadeIn(paper), FadeIn(cursor), run_time=0.9)
        naive = T("when the AI insists, argue harder", size=40).move_to(
            np.array([0.0, 0.5, 0.0]))
        self.play(Write(naive), run_time=1.0)
        strike = Line(naive.get_left() + np.array([-0.15, 0.0, 0.0]),
                      naive.get_right() + np.array([0.15, 0.0, 0.0]),
                      color=TERRA, stroke_width=9)
        self.play(Create(strike), run_time=0.7)
        self.play(FadeOut(naive), FadeOut(strike), FadeOut(cursor), run_time=0.7)
        fixed = T("when the AI insists, run the playbook", size=40).move_to(
            np.array([0.0, 0.5, 0.0]))
        chk = check_mark(np.array([4.6, -1.0, 0.0]), scale=0.9)
        self.play(Write(fixed), GrowFromCenter(chk), run_time=1.2)
        self.wait(12.0)


class M03_B02(Scene):
    def construct(self):
        self.add(bug())
        terms = ["hallucination", "model", "double down"]
        defs = ["a confident wrong answer", "the engine inside the AI",
                "when it insists it's right"]
        xs = [-3.9, 0.0, 3.9]
        for i, (w, d, x) in enumerate(zip(terms, defs, xs)):
            box = RoundedRectangle(corner_radius=0.2, width=3.5, height=2.6,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK, stroke_width=3).move_to(
                                       np.array([x, 0.3, 0.0]))
            edge = TERRA if i == 0 else INK
            strip = Rectangle(width=3.5, height=0.22, fill_color=edge,
                              fill_opacity=1, stroke_width=0).move_to(
                                  np.array([x, 1.49, 0.0]))
            head = T(w, size=30, bold=True).move_to(np.array([x, 0.7, 0.0]))
            sub = T(d, size=24, color=DIM).move_to(np.array([x, -0.15, 0.0]))
            self.play(FadeIn(VGroup(box, strip, head, sub)), run_time=0.9)
        self.wait(11.0)


class M04_WrongAnswer(Scene):
    def construct(self):
        self.add(bug())
        c = chat_window(-1.4, 0.1, 1.0)
        self.play(FadeIn(c["group"]), run_time=0.9)
        uq = user_bubble("when did the Riverside Library close?", 0.7, 1.55, s=0.92)
        self.play(FadeIn(uq), run_time=0.8)
        ai = ai_bubble("March 2019. Demolished that same year.", -0.7, 0.55,
                       s=0.92, w=5.6)
        self.play(FadeIn(ai), run_time=0.8)
        g, _, _ = gauge("confidence", np.array([4.6, -0.6, 0.0]), 1.0)
        self.play(FadeIn(g), run_time=0.9)
        self.wait(11.0)


class M05_Insist(Scene):
    def construct(self):
        self.add(bug())
        c = chat_window(-1.4, 0.1, 1.0)
        self.play(FadeIn(c["group"]), run_time=0.9)
        uq = user_bubble("are you sure? that doesn't sound right.", 0.35, 1.5,
                         s=0.92, )
        self.play(FadeIn(uq), run_time=0.8)
        ai = ai_bubble("I'm quite sure. March 2019.", -0.9, 0.5, s=0.92, w=4.4)
        self.play(FadeIn(ai), run_time=0.8)
        loop = CurvedArrow(np.array([1.6, 0.15, 0.0]), np.array([1.6, 0.85, 0.0]),
                           angle=-2.4, color=INK, stroke_width=6)
        self.play(Create(loop), run_time=0.8)
        under = Line(ai.get_left() + np.array([0.0, -0.42, 0.0]),
                     ai.get_right() + np.array([0.0, -0.42, 0.0]),
                     color=TERRA, stroke_width=8)
        self.play(Create(under), run_time=0.7)
        self.wait(9.0)


class M06_Mechanism(Scene):
    def construct(self):
        self.add(bug())
        words = ["the", "most", "likely", "next", "word", "next"]
        xs = [-4.6, -2.8, -0.7, 1.6, 3.4, 5.0]
        chips = [word_chip(w, np.array([x, 2.2, 0.0])) for w, x in zip(words, xs)]
        self.play(*[FadeIn(ch) for ch in chips[:3]], run_time=0.9)
        self.play(*[FadeIn(ch) for ch in chips[3:]], run_time=0.9)
        g1, _, _ = gauge("fluency", np.array([-3.2, -0.6, 0.0]), 1.0)
        self.play(FadeIn(g1), run_time=0.9)
        g2, _, _ = gauge("fact-check", np.array([2.8, -0.6, 0.0]), 0.04, fill=GHOST)
        tag = plate_tag("no honesty meter", np.array([2.8, -2.2, 0.0]))
        self.play(FadeIn(g2), FadeIn(tag), run_time=1.0)
        self.wait(22.0)


class M07_Restart(Scene):
    def construct(self):
        self.add(bug())
        old = chat_window(-3.6, 0.2, 0.55, title="chat 1")
        self.play(FadeIn(old["group"]), run_time=0.8)
        stamp = x_mark(np.array([-3.6, 0.2, 0.0]), scale=1.4)
        self.play(GrowFromCenter(stamp), run_time=0.7)
        new = chat_window(2.2, 0.1, 0.78, title="chat 2 — fresh")
        self.play(FadeIn(new["group"]), run_time=0.9)
        q = user_bubble("give me three possible dates,", 2.2, 1.15, s=0.8)
        q2 = user_bubble("and which one you're least sure of.", 2.2, 0.42, s=0.8)
        self.play(FadeIn(q), FadeIn(q2), run_time=0.9)
        tag = plate_tag("fresh chat", np.array([2.2, -2.5, 0.0]))
        self.play(FadeIn(tag), run_time=0.7)
        self.wait(14.0)


class M08_Sources(Scene):
    def construct(self):
        self.add(bug())
        c = chat_window(-2.2, 0.15, 0.9)
        self.play(FadeIn(c["group"]), run_time=0.8)
        ask = user_bubble("show me a source for that.", -0.4, 1.5, s=0.9)
        self.play(FadeIn(ask), run_time=0.7)
        card = RoundedRectangle(corner_radius=0.18, width=3.9, height=2.3,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=3).move_to(
                                    np.array([3.6, 0.2, 0.0]))
        head = T("the source", size=28, bold=True).move_to(np.array([3.6, 0.95, 0.0]))
        link1 = Rectangle(width=3.0, height=0.14, fill_color=TERRA,
                          fill_opacity=1, stroke_width=0).move_to(
                              np.array([3.6, 0.35, 0.0]))
        link2 = Rectangle(width=2.2, height=0.14, fill_color=DIM,
                          fill_opacity=1, stroke_width=0).move_to(
                              np.array([3.2, -0.05, 0.0]), aligned_edge=LEFT)
        link3 = Rectangle(width=2.6, height=0.14, fill_color=DIM,
                          fill_opacity=1, stroke_width=0).move_to(
                              np.array([3.4, -0.45, 0.0]), aligned_edge=LEFT)
        self.play(FadeIn(VGroup(card, head, link1, link2, link3)), run_time=0.9)
        mag = Circle(radius=0.75, color=INK, stroke_width=5).move_to(
            np.array([4.4, 0.6, 0.0]))
        handle = Line(np.array([4.95, 0.05, 0.0]), np.array([5.5, -0.5, 0.0]),
                      color=INK, stroke_width=8)
        self.play(FadeIn(VGroup(mag, handle)), run_time=0.8)
        chk = check_mark(np.array([2.5, -1.15, 0.0]), scale=0.9)
        self.play(GrowFromCenter(chk), run_time=0.7)
        self.wait(15.0)


class M09_Narrow(Scene):
    def construct(self):
        self.add(bug())
        big = RoundedRectangle(corner_radius=0.2, width=6.4, height=1.5,
                               fill_color=GHOST, fill_opacity=1,
                               stroke_color=DIM, stroke_width=3).move_to(
                                   np.array([0.0, 1.6, 0.0]))
        bigt = T("the library's history", size=34, color=DIM).move_to(
            np.array([0.0, 1.6, 0.0]))
        self.play(FadeIn(VGroup(big, bigt)), run_time=0.9)
        s1 = plate_tag("when was the building sold?", np.array([-2.9, 0.0, 0.0]), fs=26)
        s2 = plate_tag("who owned it in 2020?", np.array([2.9, 0.0, 0.0]), fs=26)
        self.play(FadeIn(s1), FadeIn(s2), FadeOut(big), FadeOut(bigt), run_time=1.0)
        pin1 = bullet(np.array([-2.9, 0.85, 0.0]))
        pin2 = bullet(np.array([2.9, 0.85, 0.0]))
        claim = RoundedRectangle(corner_radius=0.14, width=3.4, height=0.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=TERRA, stroke_width=4).move_to(
                                     np.array([0.0, -1.9, 0.0]))
        claimt = T("March 2019?", size=30).move_to(np.array([0.0, -1.9, 0.0]))
        self.play(FadeIn(pin1), FadeIn(pin2), FadeIn(VGroup(claim, claimt)),
                  run_time=1.0)
        cross = x_mark(np.array([0.0, -1.9, 0.0]), scale=1.0)
        self.play(GrowFromCenter(cross), run_time=0.7)
        self.wait(15.0)


class M10_Stop(Scene):
    def construct(self):
        self.add(bug())
        c = chat_window(-1.8, 0.1, 0.85)
        self.play(FadeIn(c["group"]), run_time=0.8)
        mag = Circle(radius=0.8, color=INK, stroke_width=5).move_to(
            np.array([3.9, 1.3, 0.0]))
        handle = Line(np.array([4.5, 0.75, 0.0]), np.array([5.1, 0.15, 0.0]),
                      color=INK, stroke_width=8)
        self.play(c["group"].animate.shift(LEFT * 1.2), FadeIn(VGroup(mag, handle)),
                  run_time=0.9)
        book = RoundedRectangle(corner_radius=0.1, width=1.7, height=2.2,
                                fill_color=KRAFT, fill_opacity=1,
                                stroke_color=INK, stroke_width=4).move_to(
                                    np.array([3.9, -1.3, 0.0]))
        p1 = plate_tag("search", np.array([-0.6, -2.5, 0.0]), fs=26)
        self.play(FadeIn(book), FadeIn(p1), run_time=0.8)
        p2 = plate_tag("a book", np.array([1.9, -2.5, 0.0]), fs=26)
        p3 = plate_tag("a person", np.array([4.2, -2.5, 0.0]), fs=26)
        self.play(FadeIn(p2), FadeIn(p3), run_time=0.8)
        self.wait(14.0)


class M11_WorkedExample(Scene):
    def construct(self):
        self.add(bug())
        steps = ["1 restart", "2 sources", "3 narrow", "4 verify elsewhere"]
        xs = [-4.7, -1.6, 1.6, 4.7]
        panels = []
        for s, x in zip(steps, xs):
            box = RoundedRectangle(corner_radius=0.18, width=2.9, height=2.2,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK, stroke_width=3).move_to(
                                       np.array([x, 0.6, 0.0]))
            head = T(s, size=28, bold=True).move_to(np.array([x, 1.25, 0.0]))
            strip = Rectangle(width=2.9, height=0.2, fill_color=GHOST,
                              fill_opacity=1, stroke_width=0).move_to(
                                  np.array([x, 0.75, 0.0]))
            panels.append(VGroup(box, strip, head))
        self.play(*[FadeIn(p) for p in panels], run_time=1.0)
        checks = [check_mark(np.array([x, -0.35, 0.0]), scale=0.7) for x in xs]
        self.play(GrowFromCenter(checks[0]), GrowFromCenter(checks[1]), run_time=0.8)
        self.play(GrowFromCenter(checks[2]), GrowFromCenter(checks[3]), run_time=0.8)
        tag = plate_tag("one recovered truth", np.array([0.0, -2.3, 0.0]))
        self.play(FadeIn(tag), run_time=0.8)
        self.wait(25.0)


class M12_Verdict(Scene):
    def construct(self):
        self.add(bug())
        card = RoundedRectangle(corner_radius=0.25, width=10.2, height=5.0,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=4)
        lines = ["confidence is fluency, not knowledge",
                 "so it doubles down when challenged",
                 "the playbook: restart, sources, narrow",
                 "and verify elsewhere when it insists"]
        ys = [1.5, 0.45, -0.6, -1.65]
        self.play(FadeIn(card), run_time=0.8)
        for s, y in zip(lines, ys):
            dot = bullet(np.array([-4.5, y, 0.0]))
            txt = T(s, size=30).move_to(np.array([-4.1, y, 0.0]),
                                        aligned_edge=LEFT)
            self.play(FadeIn(dot), FadeIn(txt), run_time=0.9)
        self.wait(18.0)


class M13_YourTurn(Scene):
    def construct(self):
        self.add(bug())
        card = RoundedRectangle(corner_radius=0.3, width=10.4, height=5.2,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=4)
        head = T("Your turn.", size=40, bold=True).move_to(np.array([0.0, 1.9, 0.0]))
        self.play(FadeIn(card), FadeIn(head), run_time=0.9)
        l1 = T("you gave me an answer I'm unsure about.", size=28).move_to(
            np.array([0.0, 0.95, 0.0]))
        send = Polygon(np.array([4.3, 0.6, 0.0]), np.array([4.9, 0.95, 0.0]),
                       np.array([4.3, 1.3, 0.0]),
                       fill_color=TERRA, fill_opacity=1, stroke_width=0)
        self.play(Write(l1), FadeIn(send), run_time=0.9)
        l2 = T("Show me a source for it —", size=28).move_to(np.array([0.0, 0.28, 0.0]))
        c1 = check_mark(np.array([-4.3, -1.6, 0.0]), scale=0.7)
        self.play(Write(l2), GrowFromCenter(c1), run_time=0.9)
        l3 = T("then give me two smaller questions I could check.", size=28).move_to(
            np.array([0.0, -0.4, 0.0]))
        c2 = check_mark(np.array([4.3, -1.6, 0.0]), scale=0.7)
        self.play(Write(l3), GrowFromCenter(c2), run_time=0.9)
        self.wait(15.0)


class M14_Outro(Scene):
    def construct(self):
        self.add(bug())
        title = T("When it's confidently wrong", size=68, bold=True)
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
