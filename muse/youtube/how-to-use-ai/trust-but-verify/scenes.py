"""scenes.py — Trust, but verify (Film 21, "How to AI").

10 Manim scenes, M01–M10, one per visual beat. House conventions: 16:9,
safe-area coords (±6.3 x, ±3.4 y), each scene carries distinct non-text
shapes that evolve across play() calls, every on-screen text is read
aloud in its beat. Every shape is introduced with an explicit
FadeIn/Create/GrowFromCenter/GrowArrow (never via .animate alone).
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


def x_mark(pos, scale=1.0, color=ACCENT):
    g = VGroup(
        Line(LEFT * 0.45 + UP * 0.45, RIGHT * 0.45 + DOWN * 0.45,
             color=color, stroke_width=12),
        Line(LEFT * 0.45 + DOWN * 0.45, RIGHT * 0.45 + UP * 0.45,
             color=color, stroke_width=12),
    ).scale(scale).move_to(pos)
    return g


def tag_plate(text, pos, color=INK, bg=CARD):
    plate = RoundedRectangle(corner_radius=0.15, width=len(text) * 0.22 + 0.8,
                             height=0.7, fill_color=bg, fill_opacity=1,
                             stroke_color=color)
    t = Text(text, font_size=20, color=color)
    g = VGroup(plate, t).move_to(pos)
    return g


class M01_Bidea(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.2, width=12.0, height=3.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to([0, 0.8, 0])
        who = Text("AI: totally confident", font_size=22, color=GREY).move_to(
            [0, 2.0, 0])
        claim = Text("Humans only use 10% of their brains.", font_size=28,
                     color=INK).move_to([0, 0.8, 0])
        x1 = Line([-5.4, 2.3, 0], [5.4, -0.7, 0], color=ACCENT,
                  stroke_width=14)
        x2 = Line([-5.4, -0.7, 0], [5.4, 2.3, 0], color=ACCENT,
                  stroke_width=14)
        false_tag = tag_plate("FALSE", [0, -2.4, 0], color=CARD, bg=ACCENT)
        self.play(FadeIn(card, shift=UP * 0.3))
        self.play(FadeIn(who), FadeIn(claim, shift=UP * 0.2))
        self.play(Create(x1), Create(x2), run_time=0.8)
        self.play(FadeIn(false_tag, shift=UP * 0.3))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        terms = [
            ("hallucination", "AI inventing, not lying"),
            ("confident tone", "a style, not a fact"),
            ("primary source", "where the fact lives"),
            ("independent check", "a second, uncopied source"),
            ("stakes", "what it costs if wrong"),
        ]
        rows = VGroup()
        for i, (term, gloss) in enumerate(terms):
            y = 2.5 - i * 1.0
            plate = RoundedRectangle(corner_radius=0.15, width=11.4,
                                     height=0.85, fill_color=CARD,
                                     fill_opacity=1,
                                     stroke_color=INK).move_to([0, y, 0])
            t = Text(term, font_size=22, color=ACCENT)
            g = Text(gloss, font_size=16, color=INK)
            line = VGroup(t, g).arrange(RIGHT, buff=0.4).move_to([0, y, 0])
            rows.add(VGroup(plate, line))
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.25), run_time=0.6)
        self.wait(1.2)


class M03_B01Step1(Scene):
    def construct(self):
        lab1 = Text("100% - says the AI", font_size=22, color=INK).move_to(
            [-3.6, 1.7, 0])
        bar1 = Rectangle(width=9.6, height=0.7, stroke_color=INK,
                         stroke_width=3, fill_color=ACCENT,
                         fill_opacity=1).move_to([0, 0.9, 0])
        ev1 = Text("evidence: nothing", font_size=20, color=GREY).move_to(
            [0, 0.0, 0])
        xa = Line([-4.4, 1.4, 0], [4.4, 0.4, 0], color=ACCENT,
                  stroke_width=10)
        xb = Line([-4.4, 0.4, 0], [4.4, 1.4, 0], color=ACCENT,
                  stroke_width=10)
        lab2 = Text("60% - and shows why", font_size=22, color=INK).move_to(
            [-3.5, -1.1, 0])
        bar2_bg = Rectangle(width=9.6, height=0.7, stroke_color=INK,
                            stroke_width=3, fill_color=CARD,
                            fill_opacity=1).move_to([0, -1.9, 0])
        bar2 = Rectangle(width=5.76, height=0.7, stroke_color=GREEN,
                         stroke_width=0, fill_color=GREEN,
                         fill_opacity=1).move_to([-1.92, -1.9, 0])
        ev2 = Text("evidence: the study, the data", font_size=20,
                   color=GREEN).move_to([0, -2.8, 0])
        chk = check_mark([5.4, -1.9, 0], scale=0.9)
        self.play(FadeIn(lab1), FadeIn(bar1))
        self.play(FadeIn(ev1, shift=UP * 0.2))
        self.play(Create(xa), Create(xb), run_time=0.7)
        self.play(FadeIn(lab2), FadeIn(bar2_bg), FadeIn(bar2))
        self.play(FadeIn(ev2), FadeIn(chk, shift=UP * 0.2))
        self.wait(1.2)


class M04_B02Demo(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.2, width=10.8, height=2.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to([0, 1.5, 0])
        l1 = Text("Banana before bed -", font_size=26, color=INK).move_to(
            [0, 2.0, 0])
        l2 = Text("fall asleep 40% faster.", font_size=26,
                  color=INK).move_to([0, 1.4, 0])
        foot = Text("[1] Journal of Sleep Medicine, 2023", font_size=18,
                    color=BLUE).move_to([0, 0.75, 0])
        cursor = Arrow([6.0, -0.6, 0], [4.6, 0.3, 0], color=INK, buff=0.1)
        dead = Rectangle(width=5.4, height=2.0, stroke_color=ACCENT,
                         stroke_width=4, fill_color=CARD,
                         fill_opacity=1).move_to([0, -1.6, 0])
        code = Text("404", font_size=44, color=ACCENT).move_to([0, -1.45, 0])
        why = Text("dead page - no study", font_size=17, color=GREY).move_to(
            [0, -2.1, 0])
        strike = Line([-4.6, 1.7, 0], [4.6, 1.7, 0], color=ACCENT,
                      stroke_width=10)
        caught = tag_plate("step 2 caught it", [-3.8, -2.9, 0], color=GREEN)
        self.play(FadeIn(card, shift=UP * 0.3))
        self.play(FadeIn(l1), FadeIn(l2), FadeIn(foot))
        self.play(GrowArrow(cursor), FadeIn(dead), FadeIn(code),
                  FadeIn(why))
        self.play(Create(strike), FadeIn(caught, shift=UP * 0.3))
        self.wait(1.2)


class M05_B03Crosscheck(Scene):
    def construct(self):
        xs = [-4.4, 0.0, 4.4]
        cards = VGroup()
        for x in xs:
            cards.add(
                RoundedRectangle(corner_radius=0.2, width=3.4, height=2.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).move_to([x, 0.6, 0]))
        la = Text("Source A", font_size=24, color=INK).move_to([-4.4, 1.2, 0])
        lb = Text("Source B", font_size=24, color=INK).move_to([0.0, 1.2, 0])
        lc = Text("Source C", font_size=24, color=GREY).move_to([4.4, 1.2, 0])
        copied = Text("copied A", font_size=18, color=GREY).move_to(
            [4.4, 0.55, 0])
        ind = Text("independent", font_size=18, color=GREEN).move_to(
            [-2.2, 2.4, 0])
        echo = Text("echo", font_size=18, color=ACCENT).move_to([2.2, 2.4, 0])
        ca = check_mark([-4.4, -0.2, 0], scale=0.9)
        cb = check_mark([0.0, -0.2, 0], scale=0.9)
        xx = x_mark([4.4, -0.2, 0], scale=0.9)
        legs = tag_plate("claim has legs", [-2.2, -2.6, 0], color=GREEN)
        chamber = tag_plate("echo chamber", [3.4, -2.6, 0], color=ACCENT)
        self.play(GrowFromCenter(cards[0]), FadeIn(la))
        self.play(GrowFromCenter(cards[1]), FadeIn(lb), FadeIn(ind))
        self.play(GrowFromCenter(cards[2]), FadeIn(lc), FadeIn(copied),
                  FadeIn(echo))
        self.play(FadeIn(ca), FadeIn(cb), FadeIn(xx, shift=UP * 0.2))
        self.play(FadeIn(legs, shift=UP * 0.2), FadeIn(chamber, shift=UP * 0.2))
        self.wait(1.2)


class M06_B04Numbers(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.2, width=4.6, height=2.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to([0, 1.6, 0])
        num = Text("40%", font_size=64, color=ACCENT).move_to([0, 1.6, 0])
        q1 = tag_plate("WHEN was it measured?", [-3.4, -0.6, 0])
        q2 = tag_plate("HOW did you get it?", [3.4, -0.6, 0])
        flow = VGroup()
        labels = ["dataset", "formula", "steps"]
        for i, lab in enumerate(labels):
            x = -2.4 + i * 2.4
            sq = Square(side_length=0.8, stroke_color=INK, stroke_width=3,
                        fill_opacity=0).move_to([x, -1.8, 0])
            t = Text(lab, font_size=16, color=GREY).move_to([x, -2.45, 0])
            flow.add(VGroup(sq, t))
        a1 = Arrow([-1.8, -1.8, 0], [-0.6, -1.8, 0], color=GREY, buff=0.1)
        a2 = Arrow([0.6, -1.8, 0], [1.8, -1.8, 0], color=GREY, buff=0.1)
        strike = Line([-2.0, 2.3, 0], [2.0, 0.9, 0], color=ACCENT,
                      stroke_width=10)
        rumor = tag_plate("a rumor with good lighting", [0, -3.0, 0],
                          color=GREY)
        self.play(FadeIn(card, shift=UP * 0.3))
        self.play(FadeIn(num, scale=0.6))
        self.play(FadeIn(q1, shift=UP * 0.2), FadeIn(q2, shift=UP * 0.2))
        self.play(FadeIn(flow), GrowArrow(a1), GrowArrow(a2))
        self.play(Create(strike), FadeIn(rumor, shift=UP * 0.2))
        self.wait(1.2)


class M07_B05Stakes(Scene):
    def construct(self):
        bar = Rectangle(width=11.0, height=0.9, stroke_color=INK,
                        stroke_width=3, fill_color=CARD,
                        fill_opacity=1).move_to([0, 0.6, 0])
        low = Rectangle(width=5.5, height=0.9, stroke_color=GREEN,
                        stroke_width=0, fill_color=GREEN,
                        fill_opacity=1).move_to([-2.75, 0.6, 0])
        low_lab = Text("quiz night - let it ride", font_size=17,
                       color=CARD).move_to([-2.75, 0.6, 0])
        high = Rectangle(width=5.5, height=0.9, stroke_color=ACCENT,
                         stroke_width=0, fill_color=ACCENT,
                         fill_opacity=1).move_to([2.75, 0.6, 0])
        high_lab = Text("health, money - all 4 steps", font_size=17,
                        color=CARD).move_to([2.75, 0.6, 0])
        mark1 = Dot(radius=0.22, color=INK).move_to([-2.75, 1.45, 0])
        mark2 = Dot(radius=0.22, color=INK).move_to([2.75, 1.45, 0])
        plate = tag_plate("match the effort to the stakes", [0, -1.6, 0])
        sixty = Text("60 seconds", font_size=22, color=ACCENT).move_to(
            [2.75, -0.7, 0])
        self.play(FadeIn(bar, shift=UP * 0.2))
        self.play(FadeIn(low), FadeIn(low_lab))
        self.play(FadeIn(high), FadeIn(high_lab))
        self.play(FadeIn(mark1, shift=DOWN * 0.2))
        self.play(FadeOut(mark1), FadeIn(mark2, shift=DOWN * 0.2))
        self.play(FadeIn(plate, shift=UP * 0.2), FadeIn(sixty))
        self.wait(1.2)


class M08_B06Card(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.2, width=11.4, height=4.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to([0, 0, 0])
        title = Text("the 60-second habit", font_size=28,
                     color=ACCENT).move_to([0, 1.55, 0])
        rows = [
            "1 - how sure? what changes your mind?",
            "2 - show the source - and open it",
            "3 - one independent cross-check",
            "4 - numbers show their work",
        ]
        row_mobs = VGroup()
        for i, r in enumerate(rows):
            y = 0.65 - i * 0.8
            b = Circle(radius=0.14, fill_color=ACCENT, fill_opacity=1,
                       stroke_width=0).move_to([-5.0, y, 0])
            t = Text(r, font_size=22, color=INK).move_to([0, y, 0])
            row_mobs.add(VGroup(b, t))
        self.play(GrowFromCenter(card, run_time=0.7))
        self.play(FadeIn(title, shift=DOWN * 0.2))
        for r in row_mobs:
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)


class M09_B07YourTurn(Scene):
    def construct(self):
        comp = RoundedRectangle(corner_radius=0.2, width=11.4, height=3.0,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to([0, 1.0, 0])
        head = Text("Your turn.", font_size=30, color=ACCENT).move_to(
            [0, 2.05, 0])
        lines = [
            "From now on, when one of your claims",
            "could change a real decision, attach",
            "your confidence level, your source,",
            "and what would change your mind.",
            "If you don't know, say so.",
        ]
        prompt = VGroup()
        for i, ln in enumerate(lines):
            prompt.add(Text(ln, font_size=18, color=INK).move_to(
                [0, 1.45 - i * 0.45, 0]))
        chips = VGroup(
            tag_plate("a health tip", [-3.8, -1.9, 0]),
            tag_plate("a price", [0.0, -1.9, 0]),
            tag_plate("a fact for work", [3.8, -1.9, 0]),
        )
        self.play(FadeIn(comp, shift=UP * 0.3))
        self.play(FadeIn(head, shift=DOWN * 0.2))
        self.play(FadeIn(prompt, shift=UP * 0.2), run_time=0.9)
        self.play(FadeIn(chips, shift=UP * 0.3))
        self.wait(1.2)


class M10_B08Outro(Scene):
    def construct(self):
        title = Text("Trust, but verify", font_size=60, color=INK)
        dot = Text(".", font_size=60, color=ACCENT)
        head = VGroup(title, dot).arrange(RIGHT, buff=0.05).move_to(
            [0, 0.8, 0])
        handle = Text("@NikBearBrown", font_size=30, color=GREY).move_to(
            [0, -0.9, 0])
        sign = tag_plate("Liam, in for Bear.", [0, -2.2, 0])
        self.play(FadeIn(head, shift=DOWN * 0.2), run_time=0.9)
        self.play(FadeIn(handle, shift=DOWN * 0.15))
        self.play(FadeIn(sign, shift=UP * 0.2))
        self.wait(1.2)
