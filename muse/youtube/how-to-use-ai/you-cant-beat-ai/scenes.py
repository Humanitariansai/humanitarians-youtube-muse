"""scenes.py — "You can't beat AI." (general-audience redo).

12 Manim scenes, S01–S12, one per beat of beat_sheet.json.
House conventions: 16:9, safe-area coords (x in [-6.3, 6.3], y in [-3.4, 3.4]),
ai-explainer / claude-liam skin (cream page, ink, one terracotta accent),
each scene carries distinct non-text shapes that evolve across play() calls,
every on-screen word is also spoken in its beat's narration.
"""

import math

from manim import *

config.pixel_width = 1920
config.pixel_height = 1080

PAGE = "#F2F0E9"
INK = "#3D3929"
ACCENT = "#D97757"
WARN = "#A44A32"
GREEN = "#2E8B57"
GREY = "#8A8578"
CARD = "#FFFFFF"

config.background_color = PAGE


# ---------------------------------------------------------------- helpers ---
def check_mark(pos, scale=1.0, color=GREEN):
    g = VGroup(
        Line(ORIGIN, RIGHT * 0.5 + DOWN * 0.3, color=color, stroke_width=10),
        Line(RIGHT * 0.5 + DOWN * 0.3, RIGHT * 1.3 + UP * 0.4,
             color=color, stroke_width=10),
    ).scale(scale).move_to(pos)
    return g


def cross_mark(pos, scale=1.0, color=WARN):
    g = VGroup(
        Line(LEFT * 0.5 + DOWN * 0.5, RIGHT * 0.5 + UP * 0.5,
             color=color, stroke_width=10),
        Line(LEFT * 0.5 + UP * 0.5, RIGHT * 0.5 + DOWN * 0.5,
             color=color, stroke_width=10),
    ).scale(scale).move_to(pos)
    return g


def doc_icon(pos, scale=1.0, label=None):
    d = Rectangle(width=1.1, height=1.4, fill_color=CARD, fill_opacity=1,
                  stroke_color=INK, stroke_width=3).scale(scale).move_to(pos)
    l1 = Line(LEFT * 0.32, RIGHT * 0.32, color=GREY, stroke_width=4)
    l2 = Line(LEFT * 0.32, RIGHT * 0.10, color=GREY, stroke_width=4)
    lines = VGroup(l1, l2).scale(scale).move_to(pos)
    g = VGroup(d, lines)
    if label is not None:
        t = Text(label, font_size=16, color=INK)
        t.next_to(d, DOWN, buff=0.15)
        g.add(t)
    return g


def person(pos, scale=1.0, color=INK):
    head = Circle(radius=0.28, fill_color=color, fill_opacity=1,
                  stroke_width=0).scale(scale)
    body = Line(UP * 0.2, DOWN * 0.9, color=color, stroke_width=12)
    return VGroup(head, body).scale(scale).move_to(pos)


def tag_plate(text, pos, color=INK, fs=20):
    plate = RoundedRectangle(corner_radius=0.15, width=len(text) * 0.20 + 0.9,
                             height=0.7, fill_color=CARD, fill_opacity=1,
                             stroke_color=color, stroke_width=3).move_to(pos)
    t = Text(text, font_size=fs, color=color)
    g = VGroup(plate, t)
    g.move_to(pos)
    return g


# ------------------------------------------------------------ S01 cold open --
class S01_ColdOpen(Scene):
    """The losing move: paste problem, instant polished answer, ship it."""

    def construct(self):
        window = RoundedRectangle(corner_radius=0.3, width=10.5, height=6.2,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=INK, stroke_width=4)
        window.move_to([0, 0.2, 0])
        bar = RoundedRectangle(corner_radius=0.2, width=9.3, height=0.9,
                               fill_color=PAGE, fill_opacity=1,
                               stroke_color=GREY, stroke_width=3)
        bar.move_to([0, 2.2, 0])
        q = Text("My problem, please fix it…", font_size=24, color=GREY)
        q.move_to([-2.6, 2.2, 0])
        self.play(FadeIn(window), FadeIn(bar), Write(q))

        send = Triangle(fill_color=ACCENT, fill_opacity=1, stroke_width=0
                        ).scale(0.35).rotate(90 * DEGREES).move_to([4.1, 2.2, 0])
        self.play(FadeIn(send))

        ans_lines = VGroup(*[
            Line(LEFT * 3.9 + UP * (0.9 - i * 0.55),
                 LEFT * 3.9 + RIGHT * (6.8 - i * 0.7) + UP * (0.9 - i * 0.55),
                 color=INK, stroke_width=8)
            for i in range(4)
        ]).move_to([0, 0.4, 0])
        doc = doc_icon([3.4, -1.4, 0], scale=1.4)
        self.play(Write(ans_lines), run_time=1.2)
        self.play(FadeIn(doc))
        self.play(check_mark([-3.6, -1.6, 0], scale=1.2))
        win = Text("feels like winning", font_size=30, color=GREEN)
        win.move_to([0, -2.6, 0])
        self.play(FadeIn(win))
        self.wait(0.5)

        # the verdict arrow bends the whole thing down
        bend = CurvedArrow([-4.6, -2.0, 0], [-4.6, -3.2, 0],
                           angle=-60 * DEGREES, color=ACCENT, stroke_width=8)
        verdict = Text("It isn't.", font_size=40, color=ACCENT)
        verdict.move_to([1.8, -2.7, 0])
        self.play(Create(bend), FadeIn(verdict))
        self.wait(1.0)


# ----------------------------------------------------- S02 overview (writer) --
class S02_WriterOverview(Scene):
    """Hesitant writer: wrong framing struck, right framing typed."""

    def construct(self):
        paper = Rectangle(width=11, height=5.6, fill_color=CARD,
                          fill_opacity=1, stroke_color=INK, stroke_width=4)
        paper.move_to([0, 0.2, 0])
        self.play(FadeIn(paper))

        wrong = Text("You can't beat AI at making things.",
                     font_size=44, color=GREY)
        wrong.move_to([0, 1.2, 0])
        self.play(Write(wrong), run_time=1.5)

        strike = Line([-4.9, 0, 0], [4.9, 0, 0], color=ACCENT, stroke_width=10)
        strike.move_to(wrong.get_center())
        self.play(Create(strike))

        right1 = Text("You can't beat AI.", font_size=52, color=INK)
        right1.move_to([0, -0.3, 0])
        self.play(Write(right1), run_time=1.2)
        right2 = Text("So stop competing. Keep the thinking for yourself.",
                      font_size=34, color=INK)
        right2.move_to([0, -1.6, 0])
        self.play(Write(right2), run_time=1.2)
        underline = Line([-3.6, 0, 0], [3.6, 0, 0], color=ACCENT,
                         stroke_width=6).move_to([-0.1, -2.25, 0])
        self.play(Create(underline))
        self.wait(1.0)


# ----------------------------------------------------------- S03 the pattern --
class S03_ThePattern(Scene):
    """Paste-and-hope: figure -> AI box -> mushy document -> shrug."""

    def construct(self):
        fig = person([-4.6, 0.2, 0], color=INK)
        qm = Text("?", font_size=64, color=ACCENT).move_to([-4.6, 1.9, 0])
        self.play(FadeIn(fig), FadeIn(qm))

        ai_box = RoundedRectangle(corner_radius=0.3, width=2.6, height=2.6,
                                  fill_color=INK, fill_opacity=1,
                                  stroke_width=0).move_to([0, 0.2, 0])
        ai_t = Text("AI", font_size=48, color=CARD).move_to([0, 0.2, 0])
        arrow_in = Arrow([-2.9, 0.2, 0], [-1.4, 0.2, 0], color=INK,
                         stroke_width=8)
        self.play(FadeIn(ai_box), FadeIn(ai_t), Create(arrow_in))

        doc = RoundedRectangle(corner_radius=0.15, width=2.2, height=2.6,
                               fill_color=GREY, fill_opacity=0.7,
                               stroke_width=0).move_to([3.9, 0.2, 0])
        wob1 = Arc(radius=0.5, start_angle=20 * DEGREES, angle=140 * DEGREES,
                   color=GREY, stroke_width=6).move_to([3.3, 1.0, 0])
        wob2 = Arc(radius=0.5, start_angle=200 * DEGREES, angle=140 * DEGREES,
                   color=GREY, stroke_width=6).move_to([4.5, -0.5, 0])
        arrow_out = Arrow([1.4, 0.2, 0], [2.7, 0.2, 0], color=GREY,
                          stroke_width=8)
        self.play(Create(arrow_out), FadeIn(doc), FadeIn(wob1), FadeIn(wob2))

        shrug_l = Line([-5.4, 1.2, 0], [-6.0, 1.9, 0], color=ACCENT,
                       stroke_width=8)
        shrug_r = Line([-3.8, 1.2, 0], [-3.2, 1.9, 0], color=ACCENT,
                       stroke_width=8)
        self.play(Create(shrug_l), Create(shrug_r))
        cap = Text("Hope is not a method.", font_size=36, color=INK)
        cap.move_to([0, -2.9, 0])
        self.play(FadeIn(cap))
        self.wait(1.0)


# ---------------------------------------------------------------- S04 the GPS --
class S04_GpsMetaphor(Scene):
    """GPS gets you there while the terrain knowledge drains away."""

    def construct(self):
        ground = RoundedRectangle(corner_radius=0.3, width=11, height=5.6,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=INK, stroke_width=4)
        ground.move_to([0, 0.2, 0])
        self.play(FadeIn(ground))

        a_dot = Dot([-4.2, -1.4, 0], radius=0.22, color=GREEN)
        b_dot = Dot([4.2, 1.6, 0], radius=0.22, color=ACCENT)
        a_t = Text("A", font_size=28, color=INK).move_to([-4.2, -2.1, 0])
        b_t = Text("B", font_size=28, color=INK).move_to([4.2, 2.2, 0])
        route = DashedLine([-4.2, -1.4, 0], [4.2, 1.6, 0], color=INK,
                           stroke_width=8, dash_length=0.25)
        self.play(FadeIn(a_dot), FadeIn(b_dot), FadeIn(a_t), FadeIn(b_t),
                  Create(route))

        # terrain: little hill triangles the driver used to read
        hills = VGroup(*[
            Triangle(fill_color=INK, fill_opacity=0.25, stroke_width=0
                     ).scale(0.35).move_to([x, y, 0])
            for x, y in [(-2.2, 0.6), (-0.4, -1.2), (1.8, 0.4), (3.0, -0.9)]
        ])
        self.play(FadeIn(hills))

        driver = person([-4.2, 2.3, 0], scale=0.8, color=INK)
        down = Arrow([-4.2, 2.9, 0], [-4.2, 2.2, 0], color=ACCENT,
                     stroke_width=8)
        self.play(FadeIn(driver), Create(down))

        # trip by trip, the terrain drains out of the driver's head
        for i in range(3):
            self.play(hills[i].animate.set_fill(opacity=0.05),
                      run_time=0.6)
        self.play(FadeOut(hills))

        dead = RoundedRectangle(corner_radius=0.2, width=3.4, height=1.1,
                                fill_color=WARN, fill_opacity=1,
                                stroke_width=0).move_to([1.4, 2.3, 0])
        dead_t = Text("no GPS", font_size=30, color=CARD).move_to([1.4, 2.3, 0])
        self.play(FadeIn(dead), FadeIn(dead_t))
        self.play(FadeOut(route))
        squiggle = VGroup(
            Arc(radius=0.5, start_angle=0, angle=200 * DEGREES,
                color=ACCENT, stroke_width=8).move_to([-0.6, 0.4, 0]),
            Arc(radius=0.35, start_angle=180 * DEGREES, angle=200 * DEGREES,
                color=ACCENT, stroke_width=8).move_to([0.5, -0.4, 0]),
        )
        self.play(Create(squiggle))
        cap = Text("The tool didn't fail. Your skill did.", font_size=34,
                   color=INK).move_to([0, -2.9, 0])
        self.play(FadeIn(cap))
        self.wait(1.0)


# -------------------------------------------------------- S05 the distinction --
class S05_TheDistinction(Scene):
    """Two columns: outsource the work (check) vs outsource the understanding (cross)."""

    def construct(self):
        divider = Line([0, 3.0, 0], [0, -3.0, 0], color=ACCENT, stroke_width=10)
        self.play(Create(divider))

        head_l = Text("OUTSOURCE THE WORK", font_size=30, color=INK)
        head_l.move_to([-3.1, 2.5, 0])
        head_r = Text("OUTSOURCE THE\nUNDERSTANDING", font_size=30,
                      color=INK).move_to([3.1, 2.5, 0])
        self.play(FadeIn(head_l), FadeIn(head_r))

        docs = VGroup(*[doc_icon([-4.4 + i * 1.3, 0.6, 0], scale=0.8)
                        for i in range(3)])
        self.play(FadeIn(docs))
        self.play(check_mark([-3.1, -1.4, 0], scale=1.4))

        bubble = Ellipse(width=2.6, height=1.6, fill_color=CARD,
                         fill_opacity=1, stroke_color=INK,
                         stroke_width=3).move_to([3.1, 0.6, 0])
        thought1 = Circle(radius=0.12, fill_color=INK, fill_opacity=1,
                          stroke_width=0).move_to([2.2, -0.7, 0])
        thought2 = Circle(radius=0.18, fill_color=INK, fill_opacity=1,
                          stroke_width=0).move_to([2.6, -0.3, 0])
        t1 = Text("…why?", font_size=28, color=GREY).move_to([3.1, 0.6, 0])
        self.play(FadeIn(bubble), FadeIn(thought1), FadeIn(thought2),
                  FadeIn(t1))
        self.play(cross_mark([3.1, -1.4, 0], scale=1.4))
        self.wait(1.0)


# ------------------------------------------------------------ S06 the scenario --
class S06_TheScenario(Scene):
    """Illustrative example: chief of staff, Friday deadline, three deliverables."""

    def construct(self):
        tag = tag_plate("Illustrative example", [0, 3.1, 0], color=GREY, fs=20)
        self.play(FadeIn(tag))

        desk = Rectangle(width=11, height=0.3, fill_color=INK, fill_opacity=1,
                         stroke_width=0).move_to([0, -2.6, 0])
        self.play(FadeIn(desk))

        cal = RoundedRectangle(corner_radius=0.15, width=2.6, height=3.0,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=3)
        cal.move_to([-4.3, -0.6, 0])
        cal_head = Rectangle(width=2.6, height=0.55, fill_color=ACCENT,
                             fill_opacity=1, stroke_width=0)
        cal_head.move_to([-4.3, 0.62, 0])
        self.play(FadeIn(cal), FadeIn(cal_head))
        fri = Circle(radius=0.42, color=ACCENT, stroke_width=8)
        fri.move_to([-3.6, -1.2, 0])
        fri_t = Text("Fri", font_size=26, color=INK).move_to([-3.6, -1.2, 0])
        self.play(Create(fri), FadeIn(fri_t))

        chief = person([-4.3, 2.0, 0], scale=0.9, color=INK)
        self.play(FadeIn(chief))

        d1 = doc_icon([-1.2, -0.4, 0], scale=1.0, label="90-day ROADMAP")
        d2 = doc_icon([1.2, -0.4, 0], scale=1.0, label="PRICING")
        d3 = doc_icon([3.6, -0.4, 0], scale=1.0, label="EXEC EMAIL")
        self.play(FadeIn(d1))
        self.play(FadeIn(d2))
        self.play(FadeIn(d3))
        clock = Circle(radius=0.35, color=WARN, stroke_width=6)
        clock.move_to([5.3, -1.5, 0])
        hand = Line([5.3, -1.5, 0], [5.5, -1.25, 0], color=WARN,
                    stroke_width=6)
        self.play(Create(clock), Create(hand))
        self.wait(1.0)


# ---------------------------------------------------------------- S07 the method --
class S07_FiveSteps(Scene):
    """The five-step pipeline; step two takes the terracotta accent."""

    STEPS = ["WRITE\nCONSTRAINTS", "DRAFT FIRST\nYOURSELF",
             "PASTE DRAFT\n+ CONSTRAINTS", "ASK FOR\nTHREE VERSIONS",
             "PICK ONE,\nEDIT, OWN IT"]

    def construct(self):
        plates = VGroup()
        for i, label in enumerate(self.STEPS):
            x = -5.0 + i * 2.5
            plate = RoundedRectangle(corner_radius=0.2, width=2.1, height=2.4,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK, stroke_width=3)
            plate.move_to([x, 0.4, 0])
            num = Circle(radius=0.3, fill_color=INK, fill_opacity=1,
                         stroke_width=0).move_to([x, 1.15, 0])
            num_t = Text(str(i + 1), font_size=28, color=CARD)
            num_t.move_to([x, 1.15, 0])
            lab = Text(label, font_size=18, color=INK).move_to([x, 0.1, 0])
            plates.add(VGroup(plate, num, num_t, lab))

        arrows = VGroup(*[
            Arrow([-3.95 + i * 2.5, 0.4, 0], [-3.05 + i * 2.5, 0.4, 0],
                  color=GREY, stroke_width=6)
            for i in range(4)
        ])
        self.play(FadeIn(plates))
        self.play(Create(arrows))

        # step two gets the one terracotta accent
        halo = SurroundingRectangle(plates[1], color=ACCENT, stroke_width=10,
                                    buff=0.12)
        self.play(Create(halo))
        key = Text("the step everyone skips", font_size=28, color=ACCENT)
        key.move_to([-2.5, -2.2, 0])
        self.play(FadeIn(key))

        # each plate lights in narration order
        dots = VGroup(*[
            Dot([-5.0 + i * 2.5, 2.0, 0], radius=0.14, color=ACCENT)
            for i in range(5)
        ])
        for d in dots:
            self.play(FadeIn(d), run_time=0.4)
        self.wait(0.8)


# ---------------------------------------------------------------- S08 the signal --
class S08_TheSignal(Scene):
    """Blank prompt (hope) vs filled prompt (clear intent)."""

    def construct(self):
        head = Text("THE TELL: the draft", font_size=34, color=INK)
        head.move_to([0, 2.9, 0])
        self.play(FadeIn(head))

        blank = RoundedRectangle(corner_radius=0.2, width=4.6, height=3.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=GREY, stroke_width=3)
        blank.move_to([-2.9, 0.3, 0])
        qm = Text("?", font_size=110, color=GREY).move_to([-2.9, 0.5, 0])
        hope_t = Text("hoping the machine\nfigures it out", font_size=24,
                      color=GREY).move_to([-2.9, -1.9, 0])
        self.play(FadeIn(blank), FadeIn(qm), FadeIn(hope_t))

        filled = RoundedRectangle(corner_radius=0.2, width=4.6, height=3.2,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=INK, stroke_width=4)
        filled.move_to([2.9, 0.3, 0])
        lines = VGroup(*[
            Line([-0.9, 0, 0], [0.9 - i * 0.18, 0, 0], color=INK,
                 stroke_width=7).move_to([2.9, 1.2 - i * 0.5, 0])
            for i in range(4)
        ])
        self.play(FadeIn(filled), Write(lines))
        self.play(check_mark([4.4, -0.9, 0], scale=1.0))
        intent_t = Text("clear intent:\nyour words first", font_size=24,
                        color=INK).move_to([2.9, -1.9, 0])
        self.play(FadeIn(intent_t))

        cap = Text("The prompt is the instructions you type.",
                   font_size=30, color=ACCENT).move_to([0, -2.9, 0])
        self.play(FadeIn(cap))
        self.wait(1.0)


# ----------------------------------------------------------------- S09 the trap --
class S09_TheTrap(Scene):
    """Speedometer climbs while the understanding bar drains."""

    def construct(self):
        dial = Arc(radius=2.2, start_angle=20 * DEGREES, angle=140 * DEGREES,
                   color=INK, stroke_width=14).move_to([-3.0, -0.4, 0])
        ticks = VGroup(*[
            Line([0, 0, 0], [0, 0.3, 0], color=INK, stroke_width=5)
            .rotate((20 + i * 35) * DEGREES).move_to([
                -3.0 + 2.2 * math.cos((20 + i * 35) * math.pi / 180),
                -0.4 + 2.2 * math.sin((20 + i * 35) * math.pi / 180), 0])
            for i in range(5)
        ])
        needle = Line([-3.0, -0.4, 0], [-1.4, 0.4, 0], color=ACCENT,
                      stroke_width=12)
        self.play(Create(dial), FadeIn(ticks), Create(needle))
        speed_t = Text("getting fast", font_size=30, color=INK)
        speed_t.move_to([-3.0, -2.6, 0])
        self.play(FadeIn(speed_t))

        bar_bg = Rectangle(width=3.4, height=0.7, stroke_color=INK,
                           stroke_width=3, fill_opacity=0).move_to([3.2, 0.8, 0])
        bar_full = Rectangle(width=3.2, height=0.5, fill_color=GREEN,
                             fill_opacity=1, stroke_width=0).move_to([3.2, 0.8, 0])
        bar_t = Text("understanding", font_size=28, color=INK)
        bar_t.move_to([3.2, 1.6, 0])
        self.play(FadeIn(bar_bg), FadeIn(bar_full), FadeIn(bar_t))

        # the needle climbs; the bar drains to nothing
        needle2 = Line([-3.0, -0.4, 0], [-1.2, -0.1, 0], color=ACCENT,
                       stroke_width=12)
        bar_low = Rectangle(width=0.4, height=0.5, fill_color=WARN,
                            fill_opacity=1, stroke_width=0).move_to([1.9, 0.8, 0])
        self.play(FadeOut(needle), FadeIn(needle2))
        self.play(FadeOut(bar_full), FadeIn(bar_low))

        asker = person([2.4, -1.4, 0], scale=0.9, color=INK)
        bubble = Ellipse(width=2.4, height=1.2, fill_color=CARD, fill_opacity=1,
                         stroke_color=INK, stroke_width=3).move_to([4.6, -0.2, 0])
        bq = Text("…explain why?", font_size=26, color=INK).move_to([4.6, -0.2, 0])
        self.play(FadeIn(asker), FadeIn(bubble), FadeIn(bq))
        empty = Circle(radius=0.45, color=GREY, stroke_width=6)
        empty.move_to([0.4, -1.6, 0])
        self.play(Create(empty))
        cap = Text("Feels like getting fast.", font_size=30, color=ACCENT)
        cap.move_to([-1.6, -2.7, 0])
        self.play(FadeIn(cap))
        self.wait(1.0)


# ----------------------------------------------------------------- S10 verdict --
class S10_Verdict(Scene):
    """The opening chat window returns; the five steps stamp; YOURS seals it."""

    def construct(self):
        window = RoundedRectangle(corner_radius=0.3, width=10.5, height=6.2,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=GREY, stroke_width=3)
        window.move_to([0, 0.2, 0])
        doc = doc_icon([0, 0.6, 0], scale=1.6)
        self.play(FadeIn(window), FadeIn(doc))

        dots = VGroup(*[
            Dot([-3.2 + i * 1.6, 2.2, 0], radius=0.24, color=INK)
            for i in range(5)
        ])
        nums = VGroup(*[
            Text(str(i + 1), font_size=22, color=CARD)
            .move_to([-3.2 + i * 1.6, 2.2, 0])
            for i in range(5)
        ])
        for d, n in zip(dots, nums):
            self.play(FadeIn(d), FadeIn(n), run_time=0.4)

        seal = Star(fill_color=ACCENT, fill_opacity=1, stroke_width=0
                    ).scale(0.9).move_to([3.4, -1.2, 0])
        seal_t = Text("YOURS", font_size=26, color=CARD).move_to([3.4, -1.2, 0])
        self.play(FadeIn(seal), FadeIn(seal_t))
        cap = Text("The machine works for you.", font_size=34, color=INK)
        cap.move_to([0, -2.9, 0])
        self.play(FadeIn(cap))
        self.wait(1.0)


# ----------------------------------------------------------------- S11 handoff --
class S11_Handoff(Scene):
    """Your turn: the suggested prompt, typed in the composer."""

    def construct(self):
        greet = Text("Your turn.", font_size=44, color=INK)
        greet.move_to([0, 3.0, 0])
        self.play(FadeIn(greet))

        composer = RoundedRectangle(corner_radius=0.3, width=11, height=4.6,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK, stroke_width=4)
        composer.move_to([0, 0.0, 0])
        self.play(FadeIn(composer))

        prompt_lines = VGroup(*[
            Text(line, font_size=22, color=INK)
            for line in [
                "Here are my constraints and my rough draft.",
                "Work within my thinking — do not replace it.",
                "Give me three versions, each a different approach,",
                "and tell me which assumption of mine each one challenges.",
            ]
        ])
        for i, pl in enumerate(prompt_lines):
            pl.move_to([-4.9, 1.2 - i * 0.55, 0])
            pl.align_to(composer, LEFT)
            pl.shift(RIGHT * 0.6)
        for pl in prompt_lines:
            self.play(Write(pl), run_time=0.7)

        send = Circle(radius=0.4, fill_color=ACCENT, fill_opacity=1,
                      stroke_width=0).move_to([4.9, -1.6, 0])
        arrow = Arrow([4.7, -1.6, 0], [5.15, -1.6, 0], color=CARD,
                      stroke_width=6)
        self.play(FadeIn(send), Create(arrow))

        spark = Text("watch what it challenges", font_size=28, color=ACCENT)
        spark.move_to([0, -2.9, 0])
        self.play(FadeIn(spark))
        self.wait(1.0)


# ------------------------------------------------------------------ S12 outro --
class S12_Outro(Scene):
    """Title restate, poster-style, with the channel handle."""

    def construct(self):
        spark = Star(fill_color=ACCENT, fill_opacity=1, stroke_width=0
                     ).scale(0.28).move_to([0, 2.7, 0])
        self.play(FadeIn(spark))

        title = Text("You can't beat AI.", font_size=96, color=INK)
        title.move_to([0, 0.8, 0])
        self.play(Write(title), run_time=1.5)

        period = Dot([3.55, -0.15, 0], radius=0.16, color=ACCENT)
        self.play(FadeIn(period))

        under1 = Line([-2.6, 0, 0], [-0.6, 0, 0], color=ACCENT, stroke_width=8)
        under1.move_to([0, -0.35, 0])
        self.play(Create(under1))
        under2 = Line([-2.6, 0, 0], [2.6, 0, 0], color=ACCENT, stroke_width=8)
        under2.move_to([0, -0.35, 0])
        self.play(FadeOut(under1), Create(under2))

        handle = Text("@NikBearBrown", font_size=44, color=GREY)
        handle.move_to([0, -1.3, 0])
        self.play(FadeIn(handle))

        sub = Text("Liam, in for Bear", font_size=30, color=GREY)
        sub.move_to([0, -2.3, 0])
        self.play(FadeIn(sub))
        self.wait(1.5)
