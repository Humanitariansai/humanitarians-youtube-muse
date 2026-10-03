"""scenes.py — "Muse making a film about Muse" (general-audience redo).

17 Manim scenes, M01–M17. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), each scene carries distinct non-text shapes that evolve
across play() calls, every on-screen text is read aloud in its beat.
Drawn, not carded: each beat's visual is the idea itself, in motion.
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


def bubble_row(n, start_x, y, w=2.6):
    g = VGroup()
    for i in range(n):
        b = RoundedRectangle(corner_radius=0.3, width=w, height=0.7,
                             fill_color=CARD if i % 2 == 0 else "#EDE8DA",
                             fill_opacity=1, stroke_width=0)
        b.move_to([start_x + (i % 2) * 1.2, y - (i // 2) * 1.1, 0])
        g.add(b)
    return g


class M01_Bidea(Scene):
    def construct(self):
        desk = Rectangle(width=9, height=0.25, fill_color=INK,
                         fill_opacity=1, stroke_width=0).shift(DOWN * 2.2)
        wr = Circle(radius=0.55, fill_color=ACCENT, fill_opacity=1,
                    stroke_width=0).shift(LEFT * 3 + DOWN * 1.2)
        paper = Rectangle(width=4.6, height=3.4, fill_color=CARD, fill_opacity=1,
                          stroke_color=INK).shift(RIGHT * 1.5 + UP * 0.5)
        t1 = Text("just another chatbot", font_size=26, color=GREY).move_to(
            paper.get_center() + UP * 0.5)
        strike = Line([-1.2, 0, 0], [1.2, 0, 0], color=ACCENT,
                      stroke_width=6).move_to(t1.get_center())
        t2 = Text("a personal agent", font_size=30, color=INK).move_to(
            paper.get_center() + DOWN * 0.6)
        tag = Text("made by Muse", font_size=22, color=BLUE).to_edge(
            UP, buff=0.7)
        self.play(FadeIn(desk), FadeIn(wr), FadeIn(paper))
        self.play(Write(t1), run_time=0.8)
        self.play(Create(strike), run_time=0.5)
        self.play(Write(t2), run_time=0.7)
        self.play(FadeIn(tag, shift=DOWN * 0.2))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["agent", "memory", "skill", "artifact"]
        defs = ["a program that works\nfor you on its own",
                "what it keeps about\nyou between chats",
                "one built-in thing\nit knows how to do",
                "a document, page, or app\nit builds for you"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.6,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = Text(w, font_size=28, color=ACCENT).move_to([x, 0.7, 0])
            s = Text(d, font_size=15, color=INK).move_to([x, -0.4, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01Pairing(Scene):
    def construct(self):
        user = Circle(radius=0.6, fill_color=BLUE, fill_opacity=1,
                      stroke_width=0).shift(LEFT * 4.5)
        ulab = Text("you", font_size=24, color=INK).next_to(user, DOWN,
                                                           buff=0.25)
        agent = RoundedRectangle(corner_radius=0.3, width=1.4, height=1.4,
                                 fill_color=ACCENT, fill_opacity=1,
                                 stroke_width=0).shift(ORIGIN)
        alab = Text("your agent", font_size=24, color=INK).next_to(
            agent, DOWN, buff=0.25)
        comp = Rectangle(width=2.2, height=1.5, fill_color=INK, fill_opacity=1,
                         stroke_width=0).shift(RIGHT * 4.5)
        clab = Text("its computer", font_size=24, color=INK).next_to(
            comp, DOWN, buff=0.25)
        link1 = Line([-3.9, 0, 0], [-0.7, 0, 0], color=ACCENT, stroke_width=6)
        link2 = Line([0.7, 0, 0], [3.4, 0, 0], color=ACCENT, stroke_width=6)
        self.play(FadeIn(user), FadeIn(ulab, shift=UP * 0.2))
        self.play(FadeIn(agent), FadeIn(alab, shift=UP * 0.2))
        self.play(FadeIn(comp), FadeIn(clab, shift=UP * 0.2))
        self.play(Create(link1), Create(link2), run_time=0.9)
        self.wait(1.2)


class M04_B02Personal(Scene):
    def construct(self):
        win = RoundedRectangle(corner_radius=0.25, width=5.2, height=3.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).shift(LEFT * 2.4)
        u = Circle(radius=0.4, fill_color=BLUE, fill_opacity=1,
                   stroke_width=0).move_to([-3.6, 0.6, 0])
        win2 = RoundedRectangle(corner_radius=0.25, width=5.2, height=3.6,
                                fill_color="#EDE8DA", fill_opacity=1,
                                stroke_color=GREY).shift(RIGHT * 2.4)
        x = Cross(scale_factor=0.6, color=ACCENT).move_to(win2.get_center())
        cap = Text("yours, like your phone", font_size=26, color=INK).to_edge(
            UP, buff=0.7)
        self.play(FadeIn(win), FadeIn(u, shift=RIGHT * 0.3))
        self.play(FadeIn(win2, shift=LEFT * 0.5), run_time=0.7)
        self.play(Create(x))
        self.play(Write(cap), run_time=0.7)
        self.wait(1.2)


class M05_B03B04Engine(Scene):
    def construct(self):
        comp = Rectangle(width=3.0, height=2.0, fill_color=INK, fill_opacity=1,
                         stroke_width=0).shift(LEFT * 3.5 + UP * 0.6)
        eng = Text("Muse Spark", font_size=28, color=ACCENT).move_to(
            comp.get_center() + UP * 1.6)
        glow = SurroundingRectangle(comp, color=ACCENT, buff=0.25,
                                    stroke_width=4)
        cal = RoundedRectangle(corner_radius=0.2, width=2.6, height=2.2,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).shift(RIGHT * 0.5 + UP * 0.6)
        cal_lab = Text("Sept 8, 2026", font_size=22, color=INK).move_to(
            cal.get_center())
        pin1 = Dot(radius=0.18, color=BLUE).move_to([3.4, 1.8, 0])
        pin2 = Dot(radius=0.18, color=BLUE).move_to([4.6, 0.9, 0])
        reg = Text("US + Canada", font_size=22, color=BLUE).move_to(
            [4.0, -0.6, 0])
        self.play(FadeIn(comp))
        self.play(FadeIn(eng, shift=DOWN * 0.2), Create(glow))
        self.play(FadeIn(cal), FadeIn(cal_lab, shift=UP * 0.2))
        self.play(FadeIn(pin1, shift=DOWN * 0.4), FadeIn(pin2, shift=DOWN * 0.4),
                  FadeIn(reg, shift=UP * 0.2))
        self.wait(1.2)


class M06_B05Chat(Scene):
    def construct(self):
        bubbles = bubble_row(4, -2.2, 1.2, w=3.2)
        self.play(FadeIn(bubbles[0], shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(bubbles[1], shift=LEFT * 0.3), run_time=0.5)
        self.play(FadeIn(bubbles[2], shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(bubbles[3], shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.2)


class M07_B06Memory(Scene):
    def construct(self):
        book = Rectangle(width=4.4, height=5.2, fill_color=CARD, fill_opacity=1,
                         stroke_color=INK).shift(LEFT * 2.0)
        spine = Line([-2.0, 2.6, 0], [-2.0, -2.6, 0], color=GREY,
                     stroke_width=4)
        slips = VGroup(*[
            Rectangle(width=2.6, height=0.5, fill_color=BLUE, fill_opacity=0.85,
                      stroke_width=0).move_to([-2.0, 1.2 - i * 0.9, 0])
            for i in range(3)
        ])
        flip = CurvedArrow([-4.2, -2.0, 0], [0.2, -2.0, 0], color=ACCENT)
        keep = Text("still there next week", font_size=22, color=GREEN).shift(
            RIGHT * 3.6 + DOWN * 1.0)
        check = check_mark([5.3, -0.2, 0], scale=0.8)
        self.play(FadeIn(book), Create(spine))
        self.play(*[FadeIn(s, shift=DOWN * 0.3) for s in slips], run_time=0.9)
        self.play(Create(flip), run_time=0.7)
        self.play(FadeIn(keep, shift=LEFT * 0.3), Create(check))
        self.wait(1.2)


class M08_B07Tools(Scene):
    def construct(self):
        agent = Circle(radius=0.7, fill_color=ACCENT, fill_opacity=1,
                       stroke_width=0).shift(ORIGIN)
        plugs = VGroup()
        spots = [[-4.6, 1.6], [-1.6, 2.4], [1.6, 2.4], [4.6, 1.6]]
        shapes = [
            Rectangle(width=0.9, height=0.7, fill_color=GREY, fill_opacity=1,
                      stroke_width=0),
            RoundedRectangle(corner_radius=0.15, width=0.9, height=0.9,
                             fill_color=GREY, fill_opacity=1, stroke_width=0),
            Circle(radius=0.45, fill_color=GREY, fill_opacity=1,
                   stroke_width=0),
            Rectangle(width=0.6, height=1.0, fill_color=GREY, fill_opacity=1,
                      stroke_width=0),
        ]
        for (x, y), sh in zip(spots, shapes):
            sh.move_to([x, y, 0])
            plugs.add(sh)
        links = VGroup(*[
            Line([x * 0.55, y * 0.45, 0], [x * 0.85, y * 0.8, 0],
                 color=GREY, stroke_width=3)
            for (x, y) in spots
        ])
        self.play(FadeIn(agent, scale=1.3))
        for p, ln in zip(plugs, links):
            self.play(FadeIn(p, scale=1.4), Create(ln), run_time=0.5)
        self.wait(1.2)


class M09_B08Artifact(Scene):
    def construct(self):
        page = Rectangle(width=4.6, height=5.4, fill_color=CARD, fill_opacity=1,
                         stroke_color=INK).shift(LEFT * 2.4)
        lines = VGroup(*[
            Rectangle(width=3.4 - (i % 3) * 0.7, height=0.22,
                      fill_color=GREY, fill_opacity=0.7,
                      stroke_width=0).move_to([-2.4, 1.8 - i * 0.55, 0])
            for i in range(7)
        ])
        tray = RoundedRectangle(corner_radius=0.2, width=3.6, height=1.2,
                                fill_color="#EDE8DA", fill_opacity=1,
                                stroke_width=0).shift(RIGHT * 4.0 + DOWN * 1.6)
        tlab = Text("kept: artifact", font_size=22, color=INK).move_to(
            tray.get_center() + DOWN * 1.0)
        self.play(FadeIn(page))
        self.play(*[FadeIn(ln, shift=RIGHT * 0.2) for ln in lines[:4]],
                  run_time=0.8)
        self.play(*[FadeIn(ln, shift=RIGHT * 0.2) for ln in lines[4:]],
                  run_time=0.7)
        self.play(FadeIn(tray), page.animate.shift(RIGHT * 3.2 + DOWN * 0.6),
                  run_time=0.9)
        self.play(FadeIn(tlab, shift=UP * 0.2))
        self.wait(1.2)


class M10_B09Library(Scene):
    def construct(self):
        shelves = VGroup(*[
            Rectangle(width=9.0, height=0.16, fill_color=INK, fill_opacity=1,
                      stroke_width=0).move_to([0, 1.6 - i * 1.8, 0])
            for i in range(3)
        ])
        files = VGroup()
        for i in range(3):
            for j in range(4):
                f = Rectangle(width=0.8, height=1.1,
                              fill_color=[BLUE, ACCENT, GREEN, GREY][j],
                              fill_opacity=0.9, stroke_width=0)
                f.move_to([-3.6 + j * 1.7, 2.35 - i * 1.8, 0])
                files.add(f)
        lab = Text("Library", font_size=30, color=INK).to_edge(UP, buff=0.7)
        self.play(*[Create(s) for s in shelves], run_time=0.7)
        self.play(*[FadeIn(f, shift=DOWN * 0.3) for f in files[:6]],
                  run_time=0.8)
        self.play(*[FadeIn(f, shift=DOWN * 0.3) for f in files[6:]],
                  run_time=0.8)
        self.play(Write(lab), run_time=0.6)
        self.wait(1.2)


class M11_B10Away(Scene):
    def construct(self):
        face = Circle(radius=1.6, stroke_color=INK, stroke_width=5,
                      fill_opacity=0).shift(LEFT * 3.0)
        hand1 = Line([-3.0, 0.4, 0], [-3.0, 1.4, 0], color=INK, stroke_width=6)
        hand2 = Line([-3.0, 0.4, 0], [-2.2, 0.9, 0], color=INK, stroke_width=6)
        moon = Circle(radius=0.55, fill_color=GREY, fill_opacity=1,
                      stroke_width=0).shift(RIGHT * 4.6 + UP * 2.2)
        user = Circle(radius=0.5, fill_color=BLUE, fill_opacity=0.35,
                      stroke_width=0).shift(RIGHT * 1.2 + DOWN * 1.4)
        tasks = VGroup()
        for i in range(3):
            box = RoundedRectangle(corner_radius=0.15, width=2.4, height=0.7,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK)
            box.move_to([1.2, 1.4 - i * 1.1, 0])
            tasks.add(box)
        checks = VGroup(*[check_mark([2.9, 1.4 - i * 1.1, 0], scale=0.6)
                          for i in range(3)])
        self.play(Create(face), Create(hand1), Create(hand2))
        self.play(FadeIn(moon, shift=LEFT * 0.4),
                  FadeIn(user, shift=UP * 0.3))
        for t, c in zip(tasks, checks):
            self.play(FadeIn(t, shift=LEFT * 0.3), Create(c), run_time=0.6)
        self.wait(1.2)


class M12_B11Web(Scene):
    def construct(self):
        win = Rectangle(width=7.6, height=4.6, fill_color=CARD, fill_opacity=1,
                        stroke_color=INK)
        bar = Rectangle(width=7.6, height=0.7, fill_color=INK, fill_opacity=1,
                        stroke_width=0).shift(UP * 1.95)
        addr = RoundedRectangle(corner_radius=0.3, width=4.4, height=0.55,
                                fill_color=PAPER, fill_opacity=1,
                                stroke_width=0).move_to([-1.0, 1.95, 0])
        url = Text("muse.ai", font_size=26, color=INK).move_to(
            addr.get_center())
        body = Text("your agent is here", font_size=24, color=GREY).move_to(
            [0, -0.4, 0])
        self.play(Create(win), FadeIn(bar))
        self.play(FadeIn(addr))
        self.play(Write(url), run_time=0.7)
        self.play(FadeIn(body, shift=UP * 0.2))
        self.wait(1.2)


class M13_B12Phone(Scene):
    def construct(self):
        phone = RoundedRectangle(corner_radius=0.35, width=2.6, height=5.2,
                                 fill_color=INK, fill_opacity=1,
                                 stroke_width=0).shift(LEFT * 2.6)
        screen = RoundedRectangle(corner_radius=0.2, width=2.2, height=4.6,
                                  fill_color=PAPER, fill_opacity=1,
                                  stroke_width=0).shift(LEFT * 2.6)
        bubbles = VGroup(*[
            RoundedRectangle(corner_radius=0.2, width=1.6, height=0.5,
                             fill_color=CARD if i % 2 == 0 else "#EDE8DA",
                             fill_opacity=1, stroke_width=0).move_to(
                                 [-2.6 + (0.2 if i % 2 == 0 else -0.2),
                                  1.4 - i * 0.8, 0])
            for i in range(4)
        ])
        cap = Text("same agent, same memory", font_size=24, color=INK).shift(
            RIGHT * 3.4)
        self.play(GrowFromCenter(phone))
        self.play(FadeIn(screen))
        self.play(*[FadeIn(b, shift=UP * 0.2) for b in bubbles], run_time=0.9)
        self.play(FadeIn(cap, shift=LEFT * 0.3))
        self.wait(1.2)


class M14_B13B14MacWhats(Scene):
    def construct(self):
        lap = VGroup(
            Rectangle(width=3.6, height=2.4, stroke_color=INK, stroke_width=3,
                      fill_color=CARD, fill_opacity=1).shift(
                          LEFT * 3.2 + UP * 0.5),
            Rectangle(width=4.4, height=0.2, fill_color=INK, fill_opacity=1,
                      stroke_width=0).shift(LEFT * 3.2 + DOWN * 0.8),
        )
        wa = RoundedRectangle(corner_radius=0.35, width=3.4, height=1.4,
                              fill_color=GREEN, fill_opacity=0.9,
                              stroke_width=0).shift(RIGHT * 3.2 + UP * 0.5)
        wlab = Text("WhatsApp", font_size=24, color=CARD).move_to(
            wa.get_center() + UP * 0.25)
        ticks = check_mark([4.3, 0.35, 0], scale=0.6, color=CARD)
        cap = Text("meet it where you are", font_size=24, color=INK).shift(
            DOWN * 2.4)
        self.play(FadeIn(lap, shift=RIGHT * 0.4))
        self.play(GrowFromCenter(wa), FadeIn(wlab, shift=DOWN * 0.2))
        self.play(Create(ticks))
        self.play(FadeIn(cap, shift=UP * 0.2))
        self.wait(1.2)


class M15_B15B16Paid(Scene):
    def construct(self):
        track = RoundedRectangle(corner_radius=0.25, width=8.0, height=0.9,
                                 fill_color="#EDE8DA", fill_opacity=1,
                                 stroke_width=0)
        free_fill = RoundedRectangle(corner_radius=0.25, width=3.2, height=0.9,
                                     fill_color=BLUE, fill_opacity=1,
                                     stroke_width=0).shift(LEFT * 2.4)
        free_lab = Text("free: use it plenty", font_size=22, color=INK).next_to(
            track, DOWN, buff=0.4).shift(LEFT * 2.4)
        paid_fill = RoundedRectangle(corner_radius=0.25, width=4.0, height=0.9,
                                     fill_color=ACCENT, fill_opacity=1,
                                     stroke_width=0).shift(RIGHT * 2.0)
        paid_lab = Text("paid monthly: more", font_size=22, color=INK).next_to(
            track, DOWN, buff=0.4).shift(RIGHT * 2.0)
        note = Text("same agent, same features", font_size=22,
                    color=GREY).shift(DOWN * 2.2)
        self.play(FadeIn(track))
        self.play(GrowFromEdge(free_fill, LEFT), FadeIn(free_lab),
                  run_time=0.8)
        self.play(GrowFromEdge(paid_fill, LEFT), FadeIn(paid_lab),
                  run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M16_B17Signup(Scene):
    def construct(self):
        s1 = tag_plate("muse.ai", [-4.4, 0.8, 0])
        s2 = tag_plate("App Store", [0, 0.8, 0])
        s3 = tag_plate("Google Play", [4.4, 0.8, 0])
        a1 = Arrow([-2.9, 0.8, 0], [-1.6, 0.8, 0], color=ACCENT, buff=0.1)
        a2 = Arrow([1.6, 0.8, 0], [2.9, 0.8, 0], color=ACCENT, buff=0.1)
        cyc = Arc(radius=1.1, start_angle=0.4, angle=5.4, color=BLUE,
                  stroke_width=6).shift(DOWN * 1.6)
        arrow_head = Triangle(fill_color=BLUE, fill_opacity=1,
                              stroke_width=0).scale(0.18)
        arrow_head.move_to([-1.05, -0.75, 0]).rotate(-0.5)
        clab = Text("monthly · cancel anytime", font_size=22,
                    color=INK).shift(DOWN * 2.9)
        self.play(FadeIn(s1))
        self.play(GrowArrow(a1), FadeIn(s2))
        self.play(GrowArrow(a2), FadeIn(s3))
        self.play(Create(cyc), FadeIn(arrow_head))
        self.play(FadeIn(clab, shift=UP * 0.2))
        self.wait(1.2)


def tag_plate(text, pos, color=INK, bg=CARD):
    plate = RoundedRectangle(corner_radius=0.15, width=len(text) * 0.24 + 0.9,
                             height=0.75, fill_color=bg, fill_opacity=1,
                             stroke_color=color)
    t = Text(text, font_size=22, color=color)
    return VGroup(plate, t).move_to(pos)


class M17_BvdtHtfOut(Scene):
    def construct(self):
        recap_mobs = []
        plate = RoundedRectangle(corner_radius=0.25, width=12.4, height=5.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).shift(UP * 0.4)
        recap_mobs.append(plate)
        lines = [
            "Your own agent on its own computer — strictly yours.",
            "Talks, remembers, uses tools, builds, keeps, works away.",
            "Reach it: web, phone, Mac, WhatsApp.",
            "Free with a limit, or paid monthly for more.",
        ]
        self.play(FadeIn(plate))
        for i, ln in enumerate(lines):
            y = 1.8 - i * 1.0
            b = bullet([-5.9, y + 0.4, 0])
            t = Text(ln, font_size=20, color=INK)
            t.move_to([-5.4 + t.width / 2, y + 0.4, 0])
            recap_mobs += [b, t]
            self.play(FadeIn(b, scale=1.5), FadeIn(t, shift=RIGHT * 0.3),
                      run_time=0.7)
        do = RoundedRectangle(corner_radius=0.2, width=9.6, height=2.2,
                              fill_color="#EDE8DA", fill_opacity=1,
                              stroke_width=0).shift(DOWN * 2.7)
        d1 = Text("Ask Muse to remember one preference.", font_size=22,
                  color=INK).move_to([-1.6, -2.4, 0])
        d2 = Text("New chat: ask what it remembers.", font_size=22,
                  color=INK).move_to([1.4, -3.0, 0])
        recap_mobs += [do, d1, d2]
        self.play(FadeIn(do), FadeIn(d1, shift=UP * 0.2),
                  FadeIn(d2, shift=UP * 0.2))
        self.play(*[FadeOut(m) for m in recap_mobs], run_time=0.5)
        wm = RoundedRectangle(corner_radius=0.2, width=7.2, height=1.4,
                              fill_color=INK, fill_opacity=1,
                              stroke_width=0).shift(DOWN * 0.2)
        wlab = Text("Muse making a film about Muse", font_size=26,
                    color=PAPER).move_to(wm.get_center() + UP * 0.25)
        whandle = Text("@NikBearBrown", font_size=20, color=GREY).move_to(
            wm.get_center() + DOWN * 0.35)
        self.play(GrowFromCenter(wm), FadeIn(wlab), FadeIn(whandle))
        self.wait(1.2)
