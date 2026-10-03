"""scenes.py — "ChatGPT or Claude?" (general-audience redo).

10 Manim scenes, M01–M10. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), each scene carries distinct non-text shapes that evolve
across play() calls, every on-screen text is read aloud in its beat.
Drawn, not carded: each beat's visual is the idea itself, in motion.
All mobjects are added explicitly (never introduced by .animate() alone).
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


def red_x(pos, scale=1.0, color=ACCENT):
    g = VGroup(
        Line(LEFT * 0.7 + UP * 0.7, RIGHT * 0.7 + DOWN * 0.7,
             color=color, stroke_width=10),
        Line(LEFT * 0.7 + DOWN * 0.7, RIGHT * 0.7 + UP * 0.7,
             color=color, stroke_width=10),
    ).scale(scale).move_to(pos)
    return g


def doc_card(pos, w=3.4, h=2.2):
    g = VGroup(
        RoundedRectangle(corner_radius=0.15, width=w, height=h,
                         fill_color=CARD, fill_opacity=1,
                         stroke_color=INK, stroke_width=3)
    )
    for i in range(3):
        ln = Line(LEFT * (w / 2 - 0.5), RIGHT * (w / 2 - 0.5),
                  color=GREY, stroke_width=5)
        ln.move_to([pos[0], pos[1] + h / 2 - 0.6 - i * 0.55, 0])
        g.add(ln)
    g.move_to(pos)
    return g


def bullet(pos, color=ACCENT):
    return Circle(radius=0.09, fill_color=color, fill_opacity=1,
                  stroke_width=0).move_to(pos)


class M01_ColdOpen(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        win = RoundedRectangle(corner_radius=0.3, width=10, height=5.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=4)
        win.move_to(UP * 0.4)
        greet = Text("Hola, Liam", font_size=40, color=INK)
        greet.move_to(win.get_top() + DOWN * 0.7 + LEFT * 3.2)
        q = Text("ChatGPT or Claude \u2014 which should I use?",
                 font_size=30, color=INK)
        q.move_to(greet.get_center() + DOWN * 0.9 + RIGHT * 0.6)
        spark = Dot(radius=0.12, color=ACCENT, fill_opacity=1)
        spark.move_to(q.get_center() + LEFT * 4.3)
        a1 = Text("Use the one your company pays for.", font_size=26,
                  color=GREY)
        a2 = Text("Test both on your real work.", font_size=26, color=GREY)
        a3 = Text("The chart is not the test.", font_size=26, color=GREY)
        a1.move_to(q.get_center() + DOWN * 1.1)
        a2.move_to(a1.get_center() + DOWN * 0.6)
        a3.move_to(a2.get_center() + DOWN * 0.6)
        self.add(win)
        self.play(Write(greet), run_time=0.8)
        self.play(Write(q), run_time=1.0)
        self.play(FadeIn(spark), run_time=0.4)
        self.play(FadeIn(a1), run_time=0.5)
        self.play(FadeIn(a2), run_time=0.5)
        self.play(FadeIn(a3), run_time=0.5)
        self.wait(0.5)


class M02_BlufWriter(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        desk = Rectangle(width=11, height=0.25, fill_color=INK,
                         fill_opacity=1, stroke_width=0).shift(DOWN * 2.6)
        writer = Circle(radius=0.5, fill_color=ACCENT, fill_opacity=1,
                        stroke_width=0).shift(LEFT * 3.4 + DOWN * 1.6)
        paper = Rectangle(width=6.4, height=3.6, fill_color=CARD,
                          fill_opacity=1, stroke_color=INK,
                          stroke_width=3).shift(RIGHT * 1.2 + UP * 0.6)
        l1 = Text("The question isn't", font_size=30, color=INK)
        l1.move_to(paper.get_center() + UP * 0.9)
        l2a = Text("which is smartest.", font_size=30, color=INK)
        l2a.move_to(paper.get_center() + UP * 0.2)
        strike = Line(l2a.get_left() + LEFT * 0.1, l2a.get_right() + RIGHT * 0.1,
                      color=ACCENT, stroke_width=7)
        l2b = Text("which is best on a chart.", font_size=30, color=INK)
        l2b.move_to(paper.get_center() + DOWN * 0.7)
        self.add(desk, writer, paper)
        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2a), run_time=0.8)
        self.play(Create(strike), run_time=0.5)
        self.play(FadeIn(l2b), run_time=0.8)
        self.wait(0.5)


class M03_Definitions(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        terms = [
            ("model", "the AI engine under the hood"),
            ("prompt", "what you type in the chat box"),
            ("context", "what it already knows about you"),
            ("benchmark", "a test score on a chart"),
        ]
        cards = VGroup()
        for i, (term, meaning) in enumerate(terms):
            card = RoundedRectangle(corner_radius=0.2, width=9.5, height=1.25,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3)
            card.move_to([0, 2.1 - i * 1.55, 0])
            t = Text(term, font_size=32, color=ACCENT)
            t.move_to(card.get_left() + RIGHT * 1.1)
            m = Text(meaning, font_size=26, color=INK)
            m.move_to(card.get_left() + RIGHT * 4.4)
            cards.add(VGroup(card, t, m))
        for c in cards:
            self.play(FadeIn(c), run_time=0.5)
        self.wait(0.5)


class M04_TheRule(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        d1 = RoundedRectangle(corner_radius=0.25, width=4.4, height=3.0,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK, stroke_width=4)
        d1.move_to(LEFT * 2.9 + UP * 1.0)
        d2 = RoundedRectangle(corner_radius=0.25, width=4.4, height=3.0,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=ACCENT, stroke_width=6)
        d2.move_to(RIGHT * 2.9 + UP * 1.0)
        l1 = Text("the one you have", font_size=28, color=INK)
        l1.move_to(d1.get_center())
        l2 = Text("both", font_size=34, color=ACCENT)
        l2.move_to(d2.get_center())
        bars = VGroup()
        for i, h in enumerate([0.5, 0.9, 0.65]):
            b = Rectangle(width=0.45, height=h, fill_color=BLUE,
                          fill_opacity=0.8, stroke_width=0)
            b.move_to([LEFT * 1.2 + RIGHT * i * 0.7, -2.2 + h / 2, 0])
            bars.add(b)
        x = red_x([-0.5, -1.7, 0], scale=0.9)
        doc = doc_card([3.2, -1.7, 0], w=3.0, h=1.9)
        chk = check_mark([4.6, -1.0, 0], scale=0.8)
        self.play(FadeIn(d1), FadeIn(l1), run_time=0.6)
        self.play(FadeIn(d2), FadeIn(l2), run_time=0.6)
        self.play(FadeIn(bars), run_time=0.5)
        self.play(Create(x), run_time=0.4)
        self.play(FadeIn(doc), run_time=0.5)
        self.play(Create(chk), run_time=0.4)
        self.wait(0.5)


class M05_ChartsLie(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        bars = VGroup()
        for i, h in enumerate([1.0, 1.7, 1.35]):
            b = Rectangle(width=0.7, height=h, fill_color=GREY,
                          fill_opacity=0.7, stroke_width=0)
            b.move_to([LEFT * 4.2 + RIGHT * i * 1.1, -0.6 + h / 2, 0])
            bars.add(b)
        star = Star(n=5, outer_radius=0.45, inner_radius=0.22,
                    fill_color=ACCENT, fill_opacity=1, stroke_width=0)
        star.move_to([-3.1, 1.6, 0])
        x = red_x([-3.1, 0.2, 0], scale=1.6)
        body = Square(side_length=1.6, fill_color=CARD, fill_opacity=1,
                      stroke_color=INK, stroke_width=4)
        body.move_to([2.6, -1.2, 0])
        roof = Triangle(fill_color=INK, fill_opacity=1, stroke_width=0)
        roof.scale(1.25).move_to([2.6, 0.15, 0])
        car = RoundedRectangle(corner_radius=0.25, width=1.7, height=0.7,
                               fill_color=BLUE, fill_opacity=1, stroke_width=0)
        car.move_to([2.6, -2.5, 0])
        w1 = Circle(radius=0.18, fill_color=INK, fill_opacity=1,
                    stroke_width=0).move_to([2.1, -2.95, 0])
        w2 = Circle(radius=0.18, fill_color=INK, fill_opacity=1,
                    stroke_width=0).move_to([3.1, -2.95, 0])
        cap = Text("which car fits your driveway?", font_size=28, color=INK)
        cap.move_to([2.6, 2.6, 0])
        self.play(FadeIn(bars), FadeIn(star), run_time=0.7)
        self.play(Create(x), run_time=0.5)
        self.play(FadeIn(body), FadeIn(roof), run_time=0.5)
        self.play(FadeIn(car), FadeIn(w1), FadeIn(w2), run_time=0.5)
        self.play(Write(cap), run_time=0.8)
        self.wait(0.5)


class M06_ContextFolder(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        chat = RoundedRectangle(corner_radius=0.25, width=4.6, height=4.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=3)
        chat.move_to(LEFT * 3.4 + UP * 0.2)
        chat_label = Text("every chat", font_size=24, color=GREY)
        chat_label.move_to(chat.get_top() + DOWN * 0.4)
        retypes = VGroup()
        for i in range(3):
            t = Text("my background is\u2026", font_size=22, color=GREY)
            t.move_to(chat.get_center() + UP * (0.8 - i * 0.9))
            retypes.add(t)
        folder_back = Rectangle(width=3.6, height=2.6, fill_color="#E3DCCB",
                                fill_opacity=1, stroke_width=0)
        folder_back.move_to(RIGHT * 3.4 + DOWN * 1.0)
        folder_tab = Rectangle(width=1.4, height=0.4, fill_color="#E3DCCB",
                               fill_opacity=1, stroke_width=0)
        folder_tab.move_to(folder_back.get_top() + UP * 0.15 + LEFT * 0.9)
        folder_label = Text("write once", font_size=24, color=INK)
        folder_label.move_to([3.4, 2.6, 0])
        files = VGroup()
        names = ["who I am", "my company", "how I write"]
        for i, nm in enumerate(names):
            f = Rectangle(width=2.9, height=0.55, fill_color=CARD,
                          fill_opacity=1, stroke_color=INK, stroke_width=2)
            f.move_to([3.4, -0.2 - i * 0.8, 0])
            fl = Text(nm, font_size=20, color=INK)
            fl.move_to(f.get_center())
            files.add(VGroup(f, fl))
        session = RoundedRectangle(corner_radius=0.25, width=3.6, height=1.6,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=BLUE, stroke_width=4)
        session.move_to([3.4, 1.2, 0])
        arrow = Arrow(folder_back.get_top() + UP * 0.3, session.get_bottom(),
                      color=BLUE, stroke_width=6)
        self.add(chat, chat_label)
        for t in retypes:
            self.play(FadeIn(t), run_time=0.4)
        self.play(FadeIn(folder_back), FadeIn(folder_tab),
                  FadeIn(folder_label), run_time=0.5)
        for f in files:
            self.play(FadeIn(f), run_time=0.4)
        self.play(FadeIn(session), Create(arrow), run_time=0.6)
        self.play(FadeOut(files), run_time=0.5)
        got = Text("already knows", font_size=24, color=BLUE)
        got.move_to(session.get_center())
        self.play(Write(got), run_time=0.6)
        self.wait(0.5)


class M07_ChatgptLane(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        img = Rectangle(width=3.2, height=2.6, fill_color="#DCE7F5",
                        fill_opacity=1, stroke_color=INK, stroke_width=3)
        img.move_to(LEFT * 4.0 + UP * 0.3)
        sun = Circle(radius=0.35, fill_color=ACCENT, fill_opacity=1,
                     stroke_width=0).move_to(img.get_center() + UP * 0.5 + LEFT * 0.7)
        hill = Triangle(fill_color=GREEN, fill_opacity=0.7, stroke_width=0)
        hill.scale(0.9).move_to(img.get_center() + DOWN * 0.6)
        edit = Arrow(img.get_right() + RIGHT * 0.1, img.get_right() + RIGHT * 1.2,
                     color=ACCENT, stroke_width=8)
        elab = Text("describe the change", font_size=22, color=INK)
        elab.move_to([LEFT * 4.0, -1.9, 0])
        sheet = Rectangle(width=3.2, height=2.6, fill_color=CARD,
                          fill_opacity=1, stroke_color=INK, stroke_width=3)
        sheet.move_to(UP * 0.3)
        grid = VGroup()
        for i in range(1, 3):
            v = Line(sheet.get_top() + DOWN * 0.01, sheet.get_bottom() + UP * 0.01,
                     color=GREY, stroke_width=2)
            v.move_to([LEFT * 0.53 + RIGHT * i * 1.06, 0.3, 0])
            grid.add(v)
        for i in range(1, 3):
            h = Line(sheet.get_left() + RIGHT * 0.01, sheet.get_right() + LEFT * 0.01,
                     color=GREY, stroke_width=2)
            h.move_to([0, 0.3 + UP * (i * 0.85 - 0.85) - DOWN * 0.0, 0])
            grid.add(h)
        slab = Text("your spreadsheet, in the chat", font_size=22, color=INK)
        slab.move_to([0, -1.9, 0])
        lens = Circle(radius=0.85, stroke_color=INK, stroke_width=8,
                      fill_opacity=0)
        lens.move_to(RIGHT * 4.0 + UP * 0.6)
        handle = Line(lens.get_center() + RIGHT * 0.6 + DOWN * 0.6,
                      lens.get_center() + RIGHT * 1.3 + DOWN * 1.3,
                      color=INK, stroke_width=10)
        dlab = Text("search that digs deeper", font_size=22, color=INK)
        dlab.move_to([RIGHT * 4.0, -1.9, 0])
        self.play(FadeIn(img), FadeIn(sun), FadeIn(hill), run_time=0.6)
        self.play(Create(edit), Write(elab), run_time=0.6)
        self.play(FadeIn(sheet), FadeIn(grid), Write(slab), run_time=0.7)
        self.play(Create(lens), Create(handle), Write(dlab), run_time=0.7)
        self.wait(0.5)


class M08_TwoExits(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        c1 = RoundedRectangle(corner_radius=0.25, width=5.2, height=4.4,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK, stroke_width=4)
        c1.move_to(LEFT * 3.1 + UP * 0.2)
        c2 = RoundedRectangle(corner_radius=0.25, width=5.2, height=4.4,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK, stroke_width=4)
        c2.move_to(RIGHT * 3.1 + UP * 0.2)
        h1 = Text("writing", font_size=34, color=INK)
        h1.move_to(c1.get_top() + DOWN * 0.7)
        a1 = Text("-> Claude", font_size=36, color=BLUE)
        a1.move_to(c1.get_center() + UP * 0.2)
        s1 = Text("+ memory folder", font_size=24, color=GREY)
        s1.move_to(c1.get_center() + DOWN * 0.7)
        h2 = Text("images - sheets - research", font_size=26, color=INK)
        h2.move_to(c2.get_top() + DOWN * 0.7)
        a2 = Text("-> ChatGPT", font_size=36, color=ACCENT)
        a2.move_to(c2.get_center() + UP * 0.2)
        s2 = Text("the better pick", font_size=24, color=GREY)
        s2.move_to(c2.get_center() + DOWN * 0.7)
        self.play(FadeIn(c1), Write(h1), run_time=0.6)
        self.play(Write(a1), Write(s1), run_time=0.6)
        self.play(FadeIn(c2), Write(h2), run_time=0.6)
        self.play(Write(a2), Write(s2), run_time=0.6)
        self.wait(1.0)


class M09_TheTest(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        face = Circle(radius=1.4, stroke_color=INK, stroke_width=8,
                      fill_opacity=0).move_to(LEFT * 4.0 + UP * 0.4)
        btn = Rectangle(width=0.5, height=0.35, fill_color=INK,
                        fill_opacity=1, stroke_width=0)
        btn.move_to(face.get_top() + UP * 0.25)
        hand = Line(face.get_center(), face.get_center() + UP * 0.9,
                    color=ACCENT, stroke_width=8)
        t30 = Text("30:00", font_size=34, color=INK)
        t30.move_to(face.get_center() + DOWN * 0.4)
        out1 = doc_card([0.2, 0.4, 0], w=2.6, h=3.0)
        out2 = doc_card([3.4, 0.4, 0], w=2.6, h=3.0)
        vs = Text("same task", font_size=24, color=GREY)
        vs.move_to([1.8, -1.9, 0])
        chk = check_mark([0.2, 0.4, 0], scale=1.2)
        self.play(Create(face), FadeIn(btn), Create(hand), run_time=0.7)
        self.play(Write(t30), run_time=0.5)
        self.play(FadeIn(out1), FadeIn(out2), Write(vs), run_time=0.7)
        self.play(Create(chk), run_time=0.5)
        self.wait(0.5)


class M10_Closing(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        lines = [
            "One AI is a fantasy \u2014 the stack is the answer.",
            "Claude for long-form work, kept sharp by one folder.",
            "ChatGPT for images, spreadsheets, deep search.",
            "Nothing outranks the test: your work, your judgment.",
        ]
        shown = VGroup()
        for i, ln in enumerate(lines):
            b = bullet([-5.2, 1.8 - i * 1.0, 0])
            t = Text(ln, font_size=28, color=INK)
            t.move_to([-4.9, 1.8 - i * 1.0, 0]).shift(RIGHT * 0.2)
            t.next_to(b, RIGHT, buff=0.25)
            g = VGroup(b, t)
            shown.add(g)
            self.play(FadeIn(g), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(shown), run_time=0.5)
        card = RoundedRectangle(corner_radius=0.25, width=10.5, height=3.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=5)
        card.move_to(UP * 0.3)
        p1 = Text("\u201cInterview me about my work week \u2014", font_size=28,
                  color=INK)
        p2 = Text("then tell me which AI should be my default,", font_size=28,
                  color=INK)
        p3 = Text("and name one task to test in both.\u201d", font_size=28,
                  color=INK)
        p1.move_to(card.get_center() + UP * 0.8)
        p2.move_to(card.get_center())
        p3.move_to(card.get_center() + DOWN * 0.8)
        plabel = Text("paste into Claude", font_size=24, color=ACCENT)
        plabel.move_to(card.get_top() + UP * 0.45)
        self.play(FadeIn(card), FadeIn(plabel), run_time=0.5)
        self.play(Write(p1), Write(p2), Write(p3), run_time=1.2)
        self.wait(0.8)
        self.play(FadeOut(card), FadeOut(plabel), FadeOut(p1), FadeOut(p2),
                  FadeOut(p3), run_time=0.5)
        title = Text("ChatGPT or Claude?", font_size=72, color=INK)
        title.move_to(UP * 0.6)
        dot = Text(".", font_size=72, color=ACCENT)
        dot.next_to(title, RIGHT, buff=0.05).shift(DOWN * 0.05)
        handle = Text("@NikBearBrown", font_size=36, color=GREY)
        handle.move_to(title.get_center() + DOWN * 1.3)
        rule = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        rule.move_to(title.get_center() + DOWN * 0.75)
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(dot), Create(rule), Write(handle), run_time=0.8)
        self.wait(1.0)
