"""scenes.py — Claude, Your Quizmaster (Film 2, how-to-use-ai lane).

8 Manim scenes, M01-M08 (M08 carries BVDT + BHTF + BOUT). House
conventions: 16:9, safe-area coords (+-6.3 x, +-3.4 y), each scene
carries distinct non-text shapes that evolve across play() calls, every
on-screen text is read aloud in its beat.
"""
from manim import *

config.pixel_width = 1920
config.pixel_height = 1080

INK = "#111111"
PAPER = "#F7F3EA"
ACCENT = "#B8472F"
BLUE = "#2F6BB8"
GREEN = "#2E8B57"
GREY = "#8A8578"
CARD = "#FFFFFF"


def check_mark(pos, scale=1.0, color=GREEN):
    g = VGroup(
        Line(ORIGIN, RIGHT * 0.5 + DOWN * 0.3, color=color, stroke_width=10),
        Line(RIGHT * 0.5 + DOWN * 0.3, RIGHT * 1.3 + UP * 0.4,
             color=color, stroke_width=10),
    ).scale(scale).move_to(pos)
    return g


def bullet(pos, color=ACCENT):
    return Circle(radius=0.09, fill_color=color, fill_opacity=1,
                  stroke_width=0).move_to(pos)


def tag_plate(text, pos, color=INK, bg=CARD):
    plate = RoundedRectangle(corner_radius=0.15, width=len(text) * 0.22 + 0.8,
                             height=0.7, fill_color=bg, fill_opacity=1,
                             stroke_color=color)
    t = Text(text, font_size=20, color=color)
    g = VGroup(plate, t).move_to(pos)
    return g


def head(pos, scale=1.0):
    return Circle(radius=0.55, stroke_color=INK, stroke_width=4,
                  fill_opacity=0).scale(scale).move_to(pos)


class M01_Bidea(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.25, width=9.0, height=4.2,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).shift(UP * 0.3)
        naive = Text("Claude, explain this chapter to me", font_size=24,
                     color=GREY).move_to([0, 1.3, 0])
        arrow = Arrow([-3.2, 0.3, 0], [-3.2, -0.5, 0], color=ACCENT, buff=0.1)
        fixed = Text("Claude, quiz me on this chapter", font_size=26,
                     color=INK).move_to([0, -1.3, 0])
        self.play(GrowFromCenter(card), run_time=0.7)
        self.play(FadeIn(naive, shift=DOWN * 0.2))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(fixed, shift=UP * 0.2))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["retrieval practice", "testing effect",
                 "spaced repetition", "predict-first"]
        defs = ["pull an answer out of memory",
                "quizzing builds memory",
                "review as you start to forget",
                "guess before you look"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.4,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = Text(w, font_size=22, color=ACCENT).move_to([x, 0.55, 0])
            s = Text(d, font_size=14, color=INK).move_to([x, -0.35, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01WhyQuiz(Scene):
    def construct(self):
        # left panel: reread — words go in, trace fades
        p1 = RoundedRectangle(corner_radius=0.2, width=4.9, height=4.0,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK).shift(LEFT * 3.3 + UP * 0.3)
        lab1 = Text("reread", font_size=24, color=GREY).move_to([-3.3, 2.8, 0])
        page = Rectangle(width=1.6, height=1.1, fill_color="#EDE8DA",
                         fill_opacity=1, stroke_width=0).move_to([-3.3, 1.5, 0])
        h1 = head([-3.3, -0.5, 0], scale=0.9)
        arr_in = Arrow([-3.3, 0.8, 0], [-3.3, 0.0, 0], color=GREY, buff=0.05)
        trace_thin = Line([-4.6, -1.6, 0], [-2.0, -1.6, 0], color=GREY,
                          stroke_width=4)
        # right panel: quiz — answers come out, trace thickens
        p2 = RoundedRectangle(corner_radius=0.2, width=4.9, height=4.0,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK).shift(RIGHT * 3.3 + UP * 0.3)
        lab2 = Text("quiz", font_size=24, color=INK).move_to([3.3, 2.8, 0])
        h2 = head([3.3, 0.9, 0], scale=0.9)
        arr_out = Arrow([3.3, 0.3, 0], [3.3, -0.5, 0], color=ACCENT, buff=0.05)
        ans = RoundedRectangle(corner_radius=0.12, width=2.2, height=0.9,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).move_to([3.3, -1.2, 0])
        trace_thick = Line([2.0, -2.1, 0], [4.6, -2.1, 0], color=ACCENT,
                           stroke_width=10)
        # hero number
        n61 = Text("61%", font_size=44, color=GREEN).move_to([-1.2, -2.9, 0])
        nvs = Text("vs", font_size=28, color=GREY).move_to([0, -2.9, 0])
        n40 = Text("40%", font_size=44, color=GREY).move_to([1.2, -2.9, 0])
        week = Text("a week later", font_size=20, color=GREY).move_to(
            [0, -3.35, 0])
        tag = tag_plate("memory researchers", [4.4, -3.1, 0], color=BLUE)
        self.play(FadeIn(p1), FadeIn(lab1))
        self.play(FadeIn(page), FadeIn(h1))
        self.play(GrowArrow(arr_in), FadeIn(trace_thin, run_time=0.5))
        self.play(FadeIn(p2), FadeIn(lab2))
        self.play(FadeIn(h2), GrowArrow(arr_out), FadeIn(ans))
        self.play(FadeIn(trace_thick, run_time=0.5))
        self.play(FadeIn(n61), FadeIn(nvs), FadeIn(n40))
        self.play(FadeIn(week), FadeIn(tag, shift=UP * 0.2))
        self.wait(1.2)


class M04_B02Predict(Scene):
    def construct(self):
        cover = VGroup(
            RoundedRectangle(corner_radius=0.25, width=6.0, height=3.6,
                             fill_color=INK, fill_opacity=1, stroke_width=0),
            Text("?", font_size=72, color=PAPER),
            Text("retrieval practice \u2014 commit first", font_size=22,
                 color=PAPER),
        )
        cover[1].move_to([0, 0.6, 0])
        cover[2].move_to([0, -0.9, 0])
        reveal = VGroup(
            RoundedRectangle(corner_radius=0.25, width=6.0, height=3.6,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK),
            Text("pull an answer out of memory", font_size=26, color=INK),
            Text("instead of re-reading it", font_size=26, color=INK),
        )
        reveal[1].move_to([0, 0.4, 0])
        reveal[2].move_to([0, -0.5, 0])
        note = tag_plate("wrong guesses count", [0, -2.6, 0], color=ACCENT)
        self.play(GrowFromCenter(cover[0]), FadeIn(cover[1]), FadeIn(cover[2]))
        self.wait(0.8)
        self.play(FadeOut(cover), FadeIn(reveal), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.3))
        self.wait(1.2)


class M05_B03Space(Scene):
    def construct(self):
        pts = [(-5.0, 1.8), (-2.6, 0.4), (-2.6, 1.4), (-0.2, 0.0),
               (-0.2, 1.0), (2.2, -0.4), (2.2, 0.6), (4.6, -0.8)]
        segs = VGroup(*[
            Line([x1, y1, 0], [x2, y2, 0], color=INK, stroke_width=6)
            for (x1, y1), (x2, y2) in zip(pts[:-1], pts[1:])
        ])
        axis = Line([-5.6, -1.9, 0], [5.6, -1.9, 0], color=GREY,
                    stroke_width=3)
        dots = VGroup(*[
            Dot(radius=0.16, color=ACCENT).move_to([x, y, 0])
            for x, y in [(-5.0, 1.8), (-2.6, 1.4), (-0.2, 1.0), (2.2, 0.6)]
        ])
        labs = VGroup(*[
            Text(t, font_size=20, color=INK).move_to([x, -2.5, 0])
            for t, x in [("today", -5.0), ("tomorrow", -2.6),
                         ("next week", -0.2), ("next month", 2.2)]
        ])
        tag = tag_plate("catches it as it fades", [3.9, 2.6, 0], color=BLUE)
        self.play(Create(axis))
        self.play(Create(segs), run_time=1.2)
        self.play(*[FadeIn(d, scale=1.6) for d in dots], run_time=0.7)
        self.play(*[FadeIn(l, shift=UP * 0.2) for l in labs], run_time=0.7)
        self.play(FadeIn(tag, shift=DOWN * 0.2))
        self.wait(1.2)


class M06_B04ExplainBack(Scene):
    def construct(self):
        phead = Circle(radius=0.5, fill_color=ACCENT, fill_opacity=1,
                       stroke_width=0).shift(LEFT * 5.0 + UP * 0.6)
        pbody = Rectangle(width=1.0, height=1.2, fill_color=ACCENT,
                          fill_opacity=1, stroke_width=0).shift(
                              LEFT * 5.0 + DOWN * 0.5)
        lines = VGroup(*[
            RoundedRectangle(corner_radius=0.1, width=3.4, height=0.5,
                             fill_color="#EDE8DA", fill_opacity=1,
                             stroke_width=0).move_to([-2.6, 1.2 - i * 0.9, 0])
            for i in range(3)
        ])
        card = RoundedRectangle(corner_radius=0.2, width=3.4, height=3.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).shift(RIGHT * 3.8)
        clab = Text("Claude", font_size=26, color=INK).move_to([3.8, 1.2, 0])
        chk = check_mark([-0.6, 1.2, 0], scale=0.8)
        qm = Text("?", font_size=36, color=ACCENT).move_to([-0.6, 0.3, 0])
        gap = Line([-4.3, -0.05, 0], [-0.9, -0.05, 0], color=ACCENT,
                   stroke_width=6)
        tag = tag_plate("study this", [1.6, -0.9, 0], color=ACCENT)
        self.play(FadeIn(phead), FadeIn(pbody))
        self.play(FadeIn(card), FadeIn(clab))
        for ln in lines:
            self.play(FadeIn(ln, shift=RIGHT * 0.3), run_time=0.5)
        self.play(Create(chk))
        self.play(FadeIn(qm, scale=1.4))
        self.play(Create(gap), FadeIn(tag, shift=UP * 0.2))
        self.wait(1.2)


class M07_B05YourWork(Scene):
    def construct(self):
        labels = ["new rule", "new platform", "new product"]
        cards = VGroup()
        for i, lab in enumerate(labels):
            x = -4.2 + i * 4.2
            box = RoundedRectangle(corner_radius=0.2, width=3.6, height=2.2,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0.6, 0])
            t = Text(lab, font_size=22, color=INK).move_to([x, 0.6, 0])
            cards.add(VGroup(box, t))
        quizzes = VGroup()
        for i in range(3):
            x = -4.2 + i * 4.2
            q = RoundedRectangle(corner_radius=0.12, width=1.2, height=1.2,
                                 fill_color=ACCENT, fill_opacity=1,
                                 stroke_width=0).move_to([x, 2.5, 0])
            qt = Text("?", font_size=36, color=CARD).move_to([x, 2.5, 0])
            quizzes.add(VGroup(q, qt))
        viewer = Dot(radius=0.18, color=INK).move_to([-5.6, -2.6, 0])
        tag = tag_plate("your judgment", [-3.4, -2.6, 0], color=BLUE)
        arr = Arrow([-4.6, -2.3, 0], [-1.6, -1.2, 0], color=BLUE, buff=0.1)
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.6)
        for q in quizzes:
            self.play(FadeIn(q, shift=DOWN * 0.4), run_time=0.5)
        self.play(FadeIn(viewer), FadeIn(tag, shift=RIGHT * 0.2))
        self.play(GrowArrow(arr))
        self.wait(1.2)


class M08_BvdtHtfOut(Scene):
    def construct(self):
        closing = []
        plate = RoundedRectangle(corner_radius=0.25, width=12.4, height=4.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).shift(UP * 0.6)
        closing.append(plate)
        lines = [
            "Act 1: quiz, predict, space, explain back.",
            "You retrieve; Claude only asks the questions.",
            "Act 2: the same moves at your work.",
            "The struggle is the learning.",
        ]
        self.play(FadeIn(plate))
        for i, ln in enumerate(lines):
            y = 2.0 - i * 1.0
            b = bullet([-5.9, y + 0.6, 0])
            t = Text(ln, font_size=20, color=INK)
            t.move_to([-5.4 + t.width / 2, y + 0.6, 0])
            closing += [b, t]
            self.play(FadeIn(b, scale=1.5), FadeIn(t, shift=RIGHT * 0.3),
                      run_time=0.7)
        self.play(*[FadeOut(m) for m in closing], run_time=0.5)

        composer = []
        card = RoundedRectangle(corner_radius=0.25, width=11.6, height=5.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).shift(UP * 0.2)
        composer.append(card)
        title = Text("Your turn \u2014 paste this into Claude",
                     font_size=24, color=ACCENT).move_to([0, 2.5, 0])
        composer.append(title)
        prompt = [
            "Quiz me on YOUR TOPIC.",
            "Ask one question at a time;",
            "wait for my answer.",
            "Tell me what is right, what is",
            "incomplete, and what I missed.",
            "After five questions, give me a",
            "spaced schedule: tomorrow,",
            "next week, next month.",
        ]
        self.play(FadeIn(card), FadeIn(title, shift=DOWN * 0.2))
        for i, ln in enumerate(prompt):
            t = Text(ln, font_size=18, color=INK)
            t.move_to([-5.2 + t.width / 2, 1.75 - i * 0.5, 0])
            composer.append(t)
            self.play(FadeIn(t, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(0.8)
        self.play(*[FadeOut(m) for m in composer], run_time=0.5)

        wm = RoundedRectangle(corner_radius=0.2, width=5.2, height=1.2,
                              fill_color=INK, fill_opacity=1,
                              stroke_width=0).shift(DOWN * 0.4)
        wlab = Text("@NikBearBrown", font_size=28, color=PAPER).move_to(
            wm.get_center())
        self.play(GrowFromCenter(wm), FadeIn(wlab))
        self.wait(1.2)
