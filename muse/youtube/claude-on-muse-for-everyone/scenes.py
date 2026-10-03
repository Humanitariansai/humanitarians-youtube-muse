"""scenes.py — "Claude making a film about Muse" (general-audience redo).

19 Manim scenes, M01–M19. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), each scene carries distinct non-text shapes that evolve
across play() calls, every on-screen text is read aloud in its beat.
Deep-explainer shape: a read, a critique, a resolution — all drawn.
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


def tag_plate(text, pos, color=INK, bg=CARD, fs=20):
    plate = RoundedRectangle(corner_radius=0.15, width=len(text) * 0.24 + 0.9,
                             height=0.75, fill_color=bg, fill_opacity=1,
                             stroke_color=color)
    t = Text(text, font_size=fs, color=color)
    return VGroup(plate, t).move_to(pos)


class M01_Bidea(Scene):
    def construct(self):
        desk = Rectangle(width=9, height=0.25, fill_color=INK,
                         fill_opacity=1, stroke_width=0).shift(DOWN * 2.2)
        wr = Circle(radius=0.55, fill_color=ACCENT, fill_opacity=1,
                    stroke_width=0).shift(LEFT * 3 + DOWN * 1.2)
        paper = Rectangle(width=5.2, height=3.4, fill_color=CARD, fill_opacity=1,
                          stroke_color=INK).shift(RIGHT * 1.5 + UP * 0.5)
        t1 = Text("what Meta tells you", font_size=26, color=GREY).move_to(
            paper.get_center() + UP * 0.5)
        strike = Line([-1.4, 0, 0], [1.4, 0, 0], color=ACCENT,
                      stroke_width=6).move_to(t1.get_center())
        t2 = Text("what Bear and Claude think", font_size=26,
                  color=INK).move_to(paper.get_center() + DOWN * 0.5)
        tag = tag_plate("Claude = the AI assistant Bear worked with",
                        [0, 2.9, 0], color=BLUE, fs=18)
        self.play(FadeIn(desk), FadeIn(wr), FadeIn(paper))
        self.play(Write(t1), run_time=0.8)
        self.play(Create(strike), run_time=0.5)
        self.play(Write(t2), run_time=0.8)
        self.play(FadeIn(tag, shift=DOWN * 0.2))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["agent", "connector", "allow-list", "prompt injection"]
        defs = ["a program that works\nfor you on its own",
                "a plug-in linking the agent\nto a service, like email",
                "only listed things\nare permitted",
                "hidden instructions\nthat steer the agent"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.6,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = Text(w, font_size=26, color=ACCENT).move_to([x, 0.7, 0])
            s = Text(d, font_size=15, color=INK).move_to([x, -0.4, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01Acts(Scene):
    def construct(self):
        goal = tag_plate("goal", [-4.6, 0, 0], color=BLUE)
        plans = VGroup(*[
            RoundedRectangle(corner_radius=0.15, width=1.6, height=1.0,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK).move_to([-1.8 + i * 0.2,
                                                        0.9 - i * 0.9, 0])
            for i in range(2)
        ])
        steps = VGroup(*[
            Circle(radius=0.32, fill_color=GREEN, fill_opacity=1,
                   stroke_width=0).move_to([1.2 + i * 1.1, 0, 0])
            for i in range(3)
        ])
        gate = RoundedRectangle(corner_radius=0.2, width=2.2, height=1.4,
                                fill_color="#EDE8DA", fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=3).move_to(
                                    [4.6, 0, 0])
        glab = Text("you approve", font_size=20, color=ACCENT).move_to(
            gate.get_center())
        a1 = Arrow([-3.4, 0, 0], [-2.6, 0, 0], color=GREY, buff=0.1)
        a2 = Arrow([-0.6, 0, 0], [0.4, 0, 0], color=GREY, buff=0.1)
        a3 = Arrow([2.9, 0, 0], [3.5, 0, 0], color=ACCENT, buff=0.1)
        self.play(FadeIn(goal, shift=RIGHT * 0.3))
        self.play(*[FadeIn(p, shift=RIGHT * 0.3) for p in plans],
                  GrowArrow(a1), run_time=0.8)
        self.play(*[FadeIn(s, scale=1.4) for s in steps], GrowArrow(a2),
                  run_time=0.8)
        self.play(FadeIn(gate), FadeIn(glab), GrowArrow(a3), run_time=0.8)
        self.wait(1.2)


class M04_B02Launch(Scene):
    def construct(self):
        cal = RoundedRectangle(corner_radius=0.2, width=3.0, height=2.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).shift(LEFT * 3.6 + UP * 0.4)
        cal_lab = Text("Sept 8, 2026", font_size=24, color=INK).move_to(
            cal.get_center())
        counter = Text("2.5M", font_size=64, color=ACCENT).shift(
            RIGHT * 1.2 + UP * 0.8)
        clab = Text("downloads, ~2 weeks", font_size=22, color=INK).next_to(
            counter, DOWN, buff=0.2)
        doc_tag = tag_plate("document reports", [1.2, -1.2, 0], color=GREY,
                            fs=18)
        stamp = RoundedRectangle(corner_radius=0.15, width=5.6, height=1.0,
                                 stroke_color=BLUE, stroke_width=4,
                                 fill_opacity=0).shift(DOWN * 2.5).rotate(-0.05)
        slab = Text("endurance, not intelligence", font_size=22,
                    color=BLUE).move_to(stamp.get_center()).rotate(-0.05)
        self.play(FadeIn(cal), FadeIn(cal_lab, shift=UP * 0.2))
        self.play(FadeIn(counter, scale=1.6), FadeIn(clab))
        self.play(FadeIn(doc_tag, shift=UP * 0.2))
        self.play(GrowFromCenter(stamp), FadeIn(slab, shift=DOWN * 0.15))
        self.wait(1.2)


class M05_B03CloudComputer(Scene):
    def construct(self):
        user = Circle(radius=0.55, fill_color=BLUE, fill_opacity=1,
                      stroke_width=0).shift(LEFT * 4.8)
        cloud = VGroup(*[
            Circle(radius=1.1, fill_color="#EDE8DA", fill_opacity=1,
                   stroke_width=0).move_to([x, y, 0])
            for x, y in [(0.4, 0.6), (1.5, 0.9), (2.5, 0.5), (1.4, 0.1)]
        ]).shift(RIGHT * 0.6)
        icons = VGroup(
            Rectangle(width=0.9, height=0.65, fill_color=BLUE, fill_opacity=1,
                      stroke_width=0),
            Circle(radius=0.35, fill_color=ACCENT, fill_opacity=1,
                   stroke_width=0),
            Rectangle(width=0.7, height=0.5, fill_color=GREEN, fill_opacity=1,
                      stroke_width=0),
        ).arrange(RIGHT, buff=0.5).move_to([2.0, 0.5, 0])
        link = Arrow([-4.0, 0.4, 0], [-0.6, 0.4, 0], color=ACCENT, buff=0.15)
        cap = Text("your computer in Meta's cloud", font_size=24,
                   color=INK).shift(DOWN * 2.4)
        self.play(FadeIn(user, shift=RIGHT * 0.4))
        self.play(*[FadeIn(c, scale=1.3) for c in cloud], run_time=0.8)
        self.play(*[FadeIn(ic, scale=1.5) for ic in icons], run_time=0.8)
        self.play(GrowArrow(link), FadeIn(cap, shift=UP * 0.2))
        self.wait(1.2)


class M06_B04Errands(Scene):
    def construct(self):
        icons = VGroup()
        spots = [-5.0, -3.0, -1.0, 1.0, 3.0, 5.0]
        shapes = [
            Triangle(fill_color=BLUE, fill_opacity=1,
                     stroke_width=0).scale(0.5),
            Circle(radius=0.4, fill_color=ACCENT, fill_opacity=1,
                   stroke_width=0),
            Rectangle(width=0.9, height=0.6, fill_color=GREEN, fill_opacity=1,
                      stroke_width=0),
            RoundedRectangle(corner_radius=0.15, width=0.9, height=0.9,
                             fill_color=BLUE, fill_opacity=1, stroke_width=0),
            Rectangle(width=0.7, height=0.9, fill_color=GREY, fill_opacity=1,
                      stroke_width=0),
            Star(fill_color=ACCENT, fill_opacity=1, stroke_width=0).scale(0.4),
        ]
        for x, sh in zip(spots, shapes):
            sh.move_to([x, 0.4, 0])
            icons.add(sh)
        cap = Text("errands, not essays", font_size=26, color=INK).shift(
            DOWN * 2.0)
        for ic in icons:
            self.play(FadeIn(ic, shift=UP * 0.4), run_time=0.45)
        self.play(FadeIn(cap, shift=UP * 0.2))
        self.wait(1.2)


class M07_B05Connectors(Scene):
    def construct(self):
        board = RoundedRectangle(corner_radius=0.25, width=10.4, height=3.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).shift(UP * 0.4)
        plugs = VGroup()
        for i in range(5):
            p = RoundedRectangle(corner_radius=0.15, width=1.5, height=1.5,
                                 fill_color=GREY, fill_opacity=1,
                                 stroke_width=0)
            p.move_to([-4.0 + i * 2.0, 0.4, 0])
            plugs.add(p)
        amz = RoundedRectangle(corner_radius=0.15, width=1.5, height=1.5,
                               fill_color="#EDE8DA", fill_opacity=1,
                               stroke_color=GREY, stroke_width=2).move_to(
                                   [4.0, -1.6, 0])
        x = Cross(scale_factor=0.35, color=ACCENT).move_to(amz.get_center())
        blab = tag_plate("blocked", [4.0, -2.9, 0], color=ACCENT, fs=18)
        cap = Text("commerce first", font_size=24, color=INK).shift(
            DOWN * 2.0 + LEFT * 3.4)
        self.play(FadeIn(board))
        for p in plugs:
            p.set_fill(BLUE)
            self.play(FadeIn(p, scale=1.4), run_time=0.4)
        self.play(FadeIn(amz), Create(x), FadeIn(blab, shift=UP * 0.2))
        self.play(FadeIn(cap, shift=UP * 0.2))
        self.wait(1.2)


class M08_B06Pricing(Scene):
    def construct(self):
        cards = VGroup()
        tiers = [("Free", "$0", GREEN), ("Power", "$20", BLUE),
                 ("Maximum", "$100", ACCENT)]
        for i, (name, price, col) in enumerate(tiers):
            x = -3.8 + i * 3.8
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.8,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0.4, 0])
            t = Text(name, font_size=26, color=INK).move_to([x, 1.1, 0])
            pr = Text(price, font_size=34, color=col).move_to([x, 0.1, 0])
            per = Text("/mo" if i else "", font_size=18, color=GREY).move_to(
                [x, -0.7, 0])
            cards.add(VGroup(box, t, pr, per))
        card_tag = tag_plate("card required even for free", [0, -1.8, 0],
                             color=ACCENT, fs=20)
        doc_tag = tag_plate("document reports", [0, -2.8, 0], color=GREY,
                            fs=18)
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(card_tag, shift=UP * 0.2))
        self.play(FadeIn(doc_tag, shift=UP * 0.2))
        self.wait(1.2)


class M09_B07Money(Scene):
    def construct(self):
        merch = RoundedRectangle(corner_radius=0.2, width=2.6, height=1.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).shift(LEFT * 4.4)
        mlab = Text("merchant", font_size=22, color=INK).move_to(
            merch.get_center())
        cut = Circle(radius=0.45, fill_color=GREEN, fill_opacity=1,
                     stroke_width=0).shift(LEFT * 1.2)
        metalab = Text("Meta's cut", font_size=22, color=INK).shift(
            LEFT * 1.2 + DOWN * 1.1)
        meta = RoundedRectangle(corner_radius=0.2, width=2.2, height=1.6,
                                fill_color=INK, fill_opacity=1,
                                stroke_width=0).shift(RIGHT * 1.6)
        metal = Text("Meta", font_size=24, color=PAPER).move_to(
            meta.get_center())
        a1 = Arrow([-3.1, 0, 0], [-1.7, 0, 0], color=GREY, buff=0.1)
        a2 = Arrow([-0.7, 0, 0], [0.5, 0, 0], color=GREY, buff=0.1)
        throne = tag_plate("intent layer", [3.4, -1.8, 0], color=ACCENT,
                           fs=22)
        gauge = Rectangle(width=4.4, height=0.4, fill_color="#EDE8DA",
                          fill_opacity=1, stroke_width=0).shift(
                              RIGHT * 1.6 + DOWN * 2.8)
        fill = Rectangle(width=1.0, height=0.4, fill_color=ACCENT,
                         fill_opacity=1, stroke_width=0)
        fill.move_to([-0.6 + 0.5 - 0.0, -2.8, 0])
        glab = Text("11 of 47 payments automatable", font_size=20,
                    color=GREY).next_to(gauge, DOWN, buff=0.2)
        self.play(FadeIn(VGroup(merch, mlab)))
        self.play(FadeIn(cut), FadeIn(metalab, shift=UP * 0.2),
                  GrowArrow(a1))
        self.play(FadeIn(VGroup(meta, metal)), GrowArrow(a2))
        self.play(FadeIn(throne, shift=UP * 0.3))
        self.play(FadeIn(gauge), FadeIn(fill), FadeIn(glab, shift=UP * 0.2))
        self.wait(1.2)


class M10_B08Disk(Scene):
    def construct(self):
        disk = Circle(radius=2.2, fill_color="#EDE8DA", fill_opacity=1,
                      stroke_width=0).shift(LEFT * 2.6)
        folders = VGroup(*[
            RoundedRectangle(corner_radius=0.1, width=1.1, height=0.8,
                             fill_color=GREY, fill_opacity=1,
                             stroke_width=0).move_to(
                                 [-2.6 + (i % 3) * 1.3 - 1.3,
                                  0.9 - (i // 3) * 1.3, 0])
            for i in range(9)
        ])
        one = SurroundingRectangle(folders[4], color=GREEN, buff=0.12,
                                   stroke_width=4)
        cap = Text("whole disk, not one folder", font_size=28, color=ACCENT)
        cap.shift(RIGHT * 3.2)
        self.play(FadeIn(disk), *[FadeIn(f) for f in folders], run_time=1.0)
        self.play(*[f.animate.set_fill(ACCENT) for f in folders],
                  run_time=0.8)
        self.play(Create(one), run_time=0.5)
        self.play(FadeIn(cap, shift=LEFT * 0.3))
        self.wait(1.2)


class M11_B09Bouncers(Scene):
    def construct(self):
        door1 = Rectangle(width=2.6, height=3.8, stroke_color=INK, stroke_width=3,
                          fill_opacity=0).shift(LEFT * 3.4)
        list1 = tag_plate("banned list", [-3.4, 2.7, 0], color=ACCENT, fs=18)
        door2 = Rectangle(width=2.6, height=3.8, stroke_color=INK, stroke_width=3,
                          fill_opacity=0).shift(RIGHT * 3.4)
        list2 = tag_plate("guest list", [3.4, 2.7, 0], color=GREEN, fs=18)
        crowd = VGroup(*[
            Circle(radius=0.28,
                   fill_color=ACCENT if i == 3 else BLUE,
                   fill_opacity=1, stroke_width=0).move_to(
                       [-5.6 + i * 0.75, -0.6, 0])
            for i in range(6)
        ])
        guests = VGroup(*[
            Circle(radius=0.28, fill_color=GREEN, fill_opacity=1,
                   stroke_width=0).move_to([2.2 + i * 0.75, -0.6, 0])
            for i in range(2)
        ])
        check = check_mark([4.9, -1.7, 0], scale=0.8)
        cap = Text("deny-list vs allow-list", font_size=26, color=INK).shift(
            DOWN * 2.8)
        self.play(Create(door1), FadeIn(list1), Create(door2), FadeIn(list2))
        self.play(*[FadeIn(c, shift=RIGHT * 1.6) for c in crowd],
                  run_time=1.2)
        self.play(*[FadeIn(g, shift=RIGHT * 0.8) for g in guests],
                  Create(check), run_time=0.8)
        self.play(FadeIn(cap, shift=UP * 0.2))
        self.wait(1.2)


class M12_B10Shield(Scene):
    def construct(self):
        shield = Polygon(
            [-1.6, 1.8, 0], [1.6, 1.8, 0], [1.6, 0.2, 0],
            [0, -1.8, 0], [-1.6, 0.2, 0],
            fill_color="#EDE8DA", fill_opacity=1, stroke_color=INK,
            stroke_width=3,
        ).shift(LEFT * 3.4)
        crack1 = Line([-3.9, 1.2, 0], [-3.0, -0.2, 0], color=ACCENT,
                      stroke_width=5)
        crack2 = Line([-2.8, -0.4, 0], [-3.4, -1.4, 0], color=ACCENT,
                      stroke_width=5)
        lab1 = tag_plate("researchers report: zero-day", [2.2, 1.2, 0],
                         color=ACCENT, fs=18)
        sub1 = Text("needs local access first", font_size=18,
                    color=GREY).move_to([2.2, 0.4, 0])
        lab2 = tag_plate("researchers report: 6.8 GB export", [2.2, -0.8, 0],
                         color=ACCENT, fs=18)
        sub2 = Text("reports, not disasters", font_size=18, color=GREY).move_to(
            [2.2, -1.6, 0])
        self.play(Create(shield))
        self.play(Create(crack1), Create(crack2))
        self.play(FadeIn(lab1, shift=LEFT * 0.3), FadeIn(sub1))
        self.play(FadeIn(lab2, shift=LEFT * 0.3), FadeIn(sub2))
        self.wait(1.2)


class M13_B11Cloud(Scene):
    def construct(self):
        files = VGroup(*[
            Rectangle(width=1.0, height=1.3, fill_color=BLUE, fill_opacity=0.9,
                      stroke_width=0).move_to([-4.2 + i * 1.5, -1.8, 0])
            for i in range(4)
        ])
        cloud = VGroup(*[
            Circle(radius=1.2, fill_color=GREY, fill_opacity=1,
                   stroke_width=0).move_to([x, y, 0])
            for x, y in [(0.6, 1.4), (1.8, 1.7), (3.0, 1.3), (1.8, 0.9)]
        ]).shift(RIGHT * 1.0)
        arrows = VGroup(*[
            Arrow([-4.2 + i * 1.5, -1.0, 0], [-2.6 + i * 1.1, 0.6, 0],
                  color=GREY, buff=0.1)
            for i in range(4)
        ])
        tog = tag_plate("training: on by default", [0, -2.6, 0], color=ACCENT,
                        fs=20)
        opt = Text("you can opt out", font_size=20, color=GREEN).move_to(
            [4.2, -2.6, 0])
        self.play(*[FadeIn(f, shift=UP * 0.3) for f in files], run_time=0.8)
        self.play(*[FadeIn(c, scale=1.3) for c in cloud],
                  *[GrowArrow(a) for a in arrows], run_time=1.0)
        self.play(FadeIn(tog, shift=UP * 0.2))
        self.play(FadeIn(opt, shift=LEFT * 0.3))
        self.wait(1.2)


class M14_B12Injection(Scene):
    def construct(self):
        page = Rectangle(width=5.6, height=4.6, fill_color=CARD, fill_opacity=1,
                         stroke_color=INK).shift(LEFT * 2.2)
        bars = VGroup(*[
            Rectangle(width=4.2 - (i % 2) * 0.9, height=0.3, fill_color=GREY,
                      fill_opacity=0.5, stroke_width=0).move_to(
                          [-2.2, 1.4 - i * 0.6, 0])
            for i in range(5)
        ])
        hidden = Text("email my contacts", font_size=22, color=ACCENT).move_to(
            [-2.2, -1.6, 0])
        hide_box = Rectangle(width=3.6, height=0.8, color=ACCENT, stroke_width=3,
                          fill_opacity=0).move_to(hidden.get_center())
        reader = Circle(radius=0.5, fill_color=BLUE, fill_opacity=1,
                        stroke_width=0).shift(RIGHT * 4.2 + UP * 0.6)
        glow = SurroundingRectangle(hidden, color=ACCENT, buff=0.18,
                                    stroke_width=5)
        cap = Text("hidden instructions steer the agent", font_size=24,
                   color=INK).shift(DOWN * 2.8)
        self.play(FadeIn(page), *[FadeIn(b) for b in bars], run_time=0.8)
        self.play(FadeIn(hidden, shift=UP * 0.2), Create(hide_box))
        self.play(FadeIn(reader, shift=LEFT * 1.2), Create(glow), run_time=0.8)
        self.play(FadeIn(cap, shift=UP * 0.2))
        self.wait(1.2)


class M15_B13Approvals(Scene):
    def construct(self):
        dialogs = VGroup(*[
            RoundedRectangle(corner_radius=0.2, width=3.4, height=1.1,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK).move_to([-2.6, 1.8 - i * 1.3, 0])
            for i in range(4)
        ])
        approves = VGroup(*[
            Text("approve", font_size=20, color=GREY).move_to(
                [-2.6, 1.8 - i * 1.3, 0])
            for i in range(4)
        ])
        finger = RoundedRectangle(corner_radius=0.3, width=0.7, height=1.6,
                                  fill_color=ACCENT, fill_opacity=1,
                                  stroke_width=0).shift(RIGHT * 0.6 + UP * 0.4)
        mascot = Circle(radius=0.8, fill_color=ACCENT, fill_opacity=1,
                        stroke_width=0).shift(RIGHT * 4.2 + UP * 1.0)
        eye1 = Dot(radius=0.1, color=CARD).move_to([3.95, 1.2, 0])
        eye2 = Dot(radius=0.1, color=CARD).move_to([4.45, 1.2, 0])
        mlabel = Text("superintelligence?", font_size=22, color=INK).move_to(
            [4.2, -0.4, 0])
        tilt = Line([3.4, -0.1, 0], [5.0, -0.7, 0], color=GREY, stroke_width=4)
        self.play(*[FadeIn(d) for d in dialogs],
                  *[FadeIn(a) for a in approves], run_time=0.9)
        self.play(FadeIn(finger, shift=DOWN * 0.5))
        self.play(finger.animate.shift(DOWN * 0.9 + LEFT * 1.2),
                  run_time=0.8)
        self.play(FadeIn(mascot, scale=1.4), FadeIn(eye1), FadeIn(eye2))
        self.play(FadeIn(mlabel, shift=UP * 0.2), Create(tilt))
        self.wait(1.2)


class M16_B14WebOnly(Scene):
    def construct(self):
        app = RoundedRectangle(corner_radius=0.3, width=1.8, height=1.8,
                               fill_color=ACCENT, fill_opacity=1,
                               stroke_width=0).shift(LEFT * 4.2 + UP * 0.6)
        trash = VGroup(
            Rectangle(width=1.4, height=1.6, fill_color=GREY, fill_opacity=1,
                      stroke_width=0),
            Rectangle(width=1.7, height=0.2, fill_color=GREY, fill_opacity=1,
                      stroke_width=0).shift(UP * 0.9),
        ).shift(LEFT * 1.2 + UP * 0.4)
        gone = check_mark([0.6, 0.6, 0], scale=0.9)
        glab = Text("verified gone", font_size=22, color=GREEN).move_to(
            [0.6, -0.6, 0])
        browser = tag_plate("muse.ai", [3.6, 0.6, 0], color=BLUE, fs=24)
        phone = RoundedRectangle(corner_radius=0.25, width=1.4, height=2.6,
                                 fill_color="#EDE8DA", fill_opacity=1,
                                 stroke_color=GREY).shift(RIGHT * 5.2 - UP * 0.6)
        x = Cross(scale_factor=0.35, color=ACCENT).move_to(phone.get_center())
        self.play(FadeIn(app))
        self.play(FadeIn(trash), app.animate.shift(RIGHT * 3.0 + DOWN * 0.2),
                  run_time=0.8)
        self.play(Create(gone), FadeIn(glab, shift=UP * 0.2))
        self.play(FadeIn(browser, shift=LEFT * 0.4))
        self.play(FadeIn(phone), Create(x))
        self.wait(1.2)


class M17_B15Sandbox(Scene):
    def construct(self):
        bot = Circle(radius=0.6, fill_color=BLUE, fill_opacity=1,
                     stroke_width=0).shift(LEFT * 4.6)
        blab = Text("bot account", font_size=20, color=INK).next_to(
            bot, DOWN, buff=0.2)
        repos = VGroup(*[
            RoundedRectangle(corner_radius=0.15, width=2.0, height=1.2,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK).move_to([-1.6 + i * 2.4, 0.6, 0])
            for i in range(3)
        ])
        rlab = Text("public repos only", font_size=20, color=INK).move_to(
            [0.8, -0.6, 0])
        gate = RoundedRectangle(corner_radius=0.2, width=3.0, height=1.6,
                                fill_color="#EDE8DA", fill_opacity=1,
                                stroke_width=0).shift(RIGHT * 4.4 + UP * 0.2)
        glab = Text("PR + review", font_size=20, color=INK).move_to(
            gate.get_center())
        a1 = Arrow([-3.8, 0, 0], [-2.8, 0.2, 0], color=ACCENT, buff=0.1)
        a2 = Arrow([2.6, 0.4, 0], [2.9, 0.4, 0], color=ACCENT, buff=0.1)
        self.play(FadeIn(bot), FadeIn(blab, shift=UP * 0.2))
        self.play(*[FadeIn(r, shift=UP * 0.2) for r in repos],
                  FadeIn(rlab), GrowArrow(a1), run_time=0.9)
        self.play(FadeIn(gate), FadeIn(glab, shift=DOWN * 0.2),
                  GrowArrow(a2))
        self.wait(1.2)


class M18_B16Rules(Scene):
    def construct(self):
        cards = VGroup()
        rules = [
            ("caps outside the agent", "card limit, not just instructions",
             BLUE),
            ("human decides irreversible", "a person, not the agent", ACCENT),
            ("guard the short list", "email · money · passwords", GREEN),
        ]
        for i, (title, sub, col) in enumerate(rules):
            y = 1.8 - i * 1.9
            box = RoundedRectangle(corner_radius=0.2, width=8.6, height=1.5,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=col, stroke_width=3)
            box.move_to([0, y, 0])
            t = Text(title, font_size=26, color=INK).move_to([-3.9 + len(title)
                                                             * 0.155, y + 0.25,
                                                             0])
            s = Text(sub, font_size=20, color=GREY).move_to(
                [-3.9 + len(sub) * 0.12, y - 0.35, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.4), run_time=0.7)
        self.wait(1.2)


class M19_BvdtHtfOut(Scene):
    def construct(self):
        recap_mobs = []
        plate = RoundedRectangle(corner_radius=0.25, width=12.4, height=6.0,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).shift(UP * 0.3)
        recap_mobs.append(plate)
        lines = [
            "A consumer agent that acts — big launch, built for endurance.",
            "Its own cloud computer; errands through connectors.",
            "Subscriptions now; fees and the intent layer later.",
            "Full disk, deny-list, researcher findings, cloud data,",
            "hidden instructions, tired approvers.",
            "Bear's answer: web only, sandbox only, caps outside.",
        ]
        self.play(FadeIn(plate))
        for i, ln in enumerate(lines):
            y = 2.2 - i * 0.85
            b = bullet([-5.9, y + 0.3, 0])
            t = Text(ln, font_size=19, color=INK)
            t.move_to([-5.4 + t.width / 2, y + 0.3, 0])
            recap_mobs += [b, t]
            self.play(FadeIn(b, scale=1.5), FadeIn(t, shift=RIGHT * 0.3),
                      run_time=0.6)
        do = RoundedRectangle(corner_radius=0.2, width=10.0, height=2.0,
                              fill_color="#EDE8DA", fill_opacity=1,
                              stroke_width=0).shift(DOWN * 2.8)
        d1 = Text("List your AI apps' disk access: allow-list or deny-list?",
                  font_size=22, color=INK).move_to(do.get_center())
        recap_mobs += [do, d1]
        self.play(FadeIn(do), FadeIn(d1, shift=UP * 0.2))
        self.play(*[FadeOut(m) for m in recap_mobs], run_time=0.5)
        wm = RoundedRectangle(corner_radius=0.2, width=7.6, height=1.4,
                              fill_color=INK, fill_opacity=1,
                              stroke_width=0).shift(DOWN * 0.2)
        wlab = Text("Claude making a film about Muse", font_size=26,
                    color=PAPER).move_to(wm.get_center() + UP * 0.25)
        whandle = Text("@NikBearBrown", font_size=20, color=GREY).move_to(
            wm.get_center() + DOWN * 0.35)
        self.play(GrowFromCenter(wm), FadeIn(wlab), FadeIn(whandle))
        self.wait(1.2)
