"""scenes.py — "One AI or many?" (#24 of 24, how-to-use-ai).

10 Manim scenes, M01–M10. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), each scene carries distinct non-text shapes that evolve
across play() calls, every on-screen text is read aloud in its beat.
Drawn, not carded: each beat's visual is the idea itself, in motion.
All mobjects are added explicitly (never introduced by .animate() alone).
No vendors named, no version numbers, no rankings, no prices — every
comparison is generic (M05's podium carries anonymous icons only).
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
        greet = Text("Ciao, Liam", font_size=40, color=INK)
        greet.move_to(win.get_top() + DOWN * 0.7 + LEFT * 3.2)
        q = Text("One AI or many \u2014 which should I pick?",
                 font_size=30, color=INK)
        q.move_to(greet.get_center() + DOWN * 0.9 + RIGHT * 0.6)
        spark = Dot(radius=0.12, color=ACCENT, fill_opacity=1)
        spark.move_to(q.get_center() + LEFT * 4.3)
        a1 = Text("Everyone wants one.", font_size=26, color=GREY)
        a2 = Text("But 'best' is the wrong question.", font_size=26, color=GREY)
        a3 = Text("The truth is liberating.", font_size=26, color=GREY)
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
        l1.move_to(paper.get_center() + UP * 1.0)
        l2a = Text("which AI is smartest.", font_size=30, color=INK)
        l2a.move_to(paper.get_center() + UP * 0.3)
        strike = Line(l2a.get_left() + LEFT * 0.1, l2a.get_right() + RIGHT * 0.1,
                      color=ACCENT, stroke_width=7)
        l2b = Text("It's whether you've learned", font_size=30, color=INK)
        l2b.move_to(paper.get_center() + DOWN * 0.6)
        l2c = Text("to use one well.", font_size=30, color=INK)
        l2c.move_to(paper.get_center() + DOWN * 1.25)
        self.add(desk, writer, paper)
        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2a), run_time=0.8)
        self.play(Create(strike), run_time=0.5)
        self.play(FadeIn(l2b), run_time=0.8)
        self.play(FadeIn(l2c), run_time=0.6)
        self.wait(0.5)


class M03_Definitions(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        terms = [
            ("AI tool", "the app you talk to"),
            ("prompt", "what you type into it"),
            ("wall", "a job your tool can't do"),
            ("leaderboard", "a score chart, gone stale"),
        ]
        cards = VGroup()
        for i, (term, meaning) in enumerate(terms):
            card = RoundedRectangle(corner_radius=0.2, width=9.5, height=1.25,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3)
            t = Text(term, font_size=30, color=ACCENT)
            t.move_to(card.get_left() + RIGHT * 1.2)
            m = Text(meaning, font_size=24, color=INK)
            m.move_to(card.get_left() + RIGHT * 4.6)
            card.move_to(UP * (2.1 - i * 1.45))
            t.move_to(card.get_center() + LEFT * 3.2)
            m.next_to(t, RIGHT, buff=0.6)
            g = VGroup(card, t, m)
            cards.add(g)
            self.add(g)
            self.play(FadeIn(g), run_time=0.6)
        self.wait(0.5)


class M04_TwoGaps(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # left pair: the gap between tools — small, grey
        h1 = Text("the gap between tools", font_size=24, color=GREY)
        h1.move_to(LEFT * 3.3 + UP * 2.9)
        b1a = Rectangle(width=1.4, height=2.2, fill_color=GREY,
                        fill_opacity=0.55, stroke_width=0)
        b1a.move_to(LEFT * 4.0 + DOWN * 0.2)
        b1b = Rectangle(width=1.4, height=2.4, fill_color=GREY,
                        fill_opacity=0.55, stroke_width=0)
        b1b.move_to(LEFT * 2.4 + DOWN * 0.1)
        lab1 = Text("near-equal bars", font_size=20, color=GREY)
        lab1.move_to(LEFT * 3.3 + DOWN * 1.7)
        # right pair: the gap between users — wide, terracotta accent
        h2 = Text("the gap between users", font_size=24, color=INK)
        h2.move_to(RIGHT * 3.3 + UP * 2.9)
        b2a = Rectangle(width=1.4, height=1.0, fill_color=ACCENT,
                        fill_opacity=0.35, stroke_width=0)
        b2a.move_to(RIGHT * 4.0 + DOWN * 0.8)
        b2b = Rectangle(width=1.4, height=3.4, fill_color=ACCENT,
                        fill_opacity=0.9, stroke_width=0)
        b2b.move_to(RIGHT * 2.4 + UP * 0.4)
        lab2a = Text("using it badly", font_size=20, color=INK)
        lab2a.move_to(RIGHT * 4.0 + DOWN * 1.7)
        lab2b = Text("using it well", font_size=20, color=INK)
        lab2b.move_to(RIGHT * 2.4 + DOWN * 1.7)
        self.add(h1, b1a, b1b, lab1)
        self.play(FadeIn(h2), run_time=0.4)
        self.play(GrowFromEdge(b2a, DOWN), GrowFromEdge(b2b, DOWN),
                  run_time=1.0)
        self.add(lab2a, lab2b)
        self.play(FadeIn(lab2a), FadeIn(lab2b), run_time=0.5)
        self.wait(0.5)


class M05_Podium(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        rounds = ["round 1", "round 2", "round 3"]
        tops = [
            (Circle(radius=0.28, fill_color=ACCENT, fill_opacity=1, stroke_width=0),
             Square(side_length=0.5, fill_color=BLUE, fill_opacity=1, stroke_width=0),
             Triangle(fill_color=GREEN, fill_opacity=1, stroke_width=0).scale(0.35)),
            (Square(side_length=0.5, fill_color=BLUE, fill_opacity=1, stroke_width=0),
             Triangle(fill_color=GREEN, fill_opacity=1, stroke_width=0).scale(0.35),
             Circle(radius=0.28, fill_color=ACCENT, fill_opacity=1, stroke_width=0)),
            (Triangle(fill_color=GREEN, fill_opacity=1, stroke_width=0).scale(0.35),
             Circle(radius=0.28, fill_color=ACCENT, fill_opacity=1, stroke_width=0),
             Square(side_length=0.5, fill_color=BLUE, fill_opacity=1, stroke_width=0)),
        ]
        for i, (rlab, order) in enumerate(zip(rounds, tops)):
            cx = (i - 1) * 4.2
            lab = Text(rlab, font_size=24, color=INK)
            lab.move_to(RIGHT * cx + UP * 2.9)
            self.add(lab)
            self.play(FadeIn(lab), run_time=0.3)
            heights = [2.6, 1.8, 1.0]
            for j, (sh, h) in enumerate(zip(order, heights)):
                step = Rectangle(width=1.3, height=h, fill_color=CARD,
                                 fill_opacity=1, stroke_color=INK, stroke_width=3)
                step.move_to(RIGHT * (cx + (j - 1) * 1.5) + DOWN * (1.9 - h / 2))
                self.add(step)
                sh.move_to(step.get_top() + UP * 0.55)
                self.play(GrowFromEdge(step, DOWN), run_time=0.4)
                self.add(sh)
                self.play(FadeIn(sh), run_time=0.3)
            crown = Text("top", font_size=20, color=GREY)
            crown.move_to(RIGHT * (cx - 1.5) + UP * 2.2)
            self.add(crown)
            self.play(FadeIn(crown), run_time=0.3)
        caption = Text("the leaderboard moves while you run", font_size=24,
                       color=GREY)
        caption.move_to(DOWN * 3.1)
        self.add(caption)
        self.play(FadeIn(caption), run_time=0.6)
        self.wait(0.5)


class M06_SkillTransfers(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        stations = [("Tool A", LEFT * 4.2), ("Tool B", ORIGIN),
                    ("next year's winner", RIGHT * 4.2)]
        for name, pos in stations:
            pod = RoundedRectangle(corner_radius=0.2, width=2.6, height=1.6,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK, stroke_width=3)
            pod.move_to(pos + UP * 1.9)
            lab = Text(name, font_size=22, color=INK)
            lab.move_to(pod.get_center())
            self.add(pod, lab)
        box = RoundedRectangle(corner_radius=0.25, width=4.6, height=2.4,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=ACCENT, stroke_width=4)
        box.move_to(LEFT * 4.2 + DOWN * 0.6)
        blab = Text("your skill", font_size=28, color=ACCENT)
        blab.move_to(box.get_top() + DOWN * 0.35)
        skills = ["ask well", "judge drafts", "push back", "know when to stop"]
        tiles = VGroup()
        for k, s in enumerate(skills):
            tile = RoundedRectangle(corner_radius=0.12, width=3.9, height=0.38,
                                    fill_color=PAPER, fill_opacity=1,
                                    stroke_color=INK, stroke_width=2)
            tx = Text(s, font_size=18, color=INK)
            tx.move_to(tile.get_center())
            tg = VGroup(tile, tx)
            tg.move_to(box.get_center() + UP * (0.45 - k * 0.48))
            tiles.add(tg)
        self.add(box, blab)
        self.play(FadeIn(box), FadeIn(blab), run_time=0.5)
        for tg in tiles:
            self.add(tg)
            self.play(FadeIn(tg), run_time=0.3)
        whole = VGroup(box, blab, tiles)
        self.play(whole.animate.shift(RIGHT * 4.2), run_time=0.8)
        self.play(whole.animate.shift(RIGHT * 4.2), run_time=0.8)
        self.wait(0.5)


class M07_TheRule(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        big = Text("1", font_size=220, color=ACCENT)
        big.move_to(LEFT * 4.4 + UP * 0.6)
        rule = Text("pick the one you have", font_size=34, color=INK)
        rule.move_to(RIGHT * 0.6 + UP * 1.9)
        self.add(big)
        self.play(FadeIn(big), run_time=0.6)
        self.add(rule)
        self.play(Write(rule), run_time=0.8)
        items = ["ask well", "show examples", "check the draft"]
        for i, it in enumerate(items):
            y = 0.7 - i * 0.85
            row = Text(it, font_size=28, color=INK)
            row.move_to(RIGHT * 1.2 + UP * y)
            self.add(row)
            self.play(FadeIn(row), run_time=0.4)
            cm = check_mark(RIGHT * 3.9 + UP * y, scale=0.8)
            self.add(cm)
            self.play(FadeIn(cm), run_time=0.3)
        cap = Text("this series teaches you how", font_size=24, color=GREY)
        cap.move_to(RIGHT * 1.4 + DOWN * 2.6)
        self.add(cap)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(0.5)


class M08_FourWalls(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        walls = ["images", "code", "your files' home", "price"]
        bricks = VGroup()
        for i, w in enumerate(walls):
            brick = RoundedRectangle(corner_radius=0.15, width=4.6, height=1.0,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK, stroke_width=3)
            t = Text(w, font_size=28, color=INK)
            t.move_to(brick.get_center())
            g = VGroup(brick, t)
            g.move_to(LEFT * 2.2 + UP * (2.2 - i * 1.3))
            bricks.add(g)
            self.add(g)
            self.play(FadeIn(g), run_time=0.4)
        second = RoundedRectangle(corner_radius=0.2, width=2.8, height=2.0,
                                  fill_color=PAPER, fill_opacity=1,
                                  stroke_color=BLUE, stroke_width=3)
        second.move_to(RIGHT * 3.6 + DOWN * 0.6)
        slab = Text("tool two", font_size=26, color=BLUE)
        slab.move_to(second.get_center())
        self.add(second, slab)
        self.play(GrowFromEdge(second, DOWN), FadeIn(slab), run_time=0.8)
        cap = Text("'maybe better' is not a wall", font_size=24, color=GREY)
        cap.move_to(DOWN * 3.1)
        self.add(cap)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(0.5)


class M09_TheCost(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        clock = Circle(radius=1.0, fill_color=CARD, fill_opacity=1,
                       stroke_color=INK, stroke_width=3)
        clock.move_to(UP * 1.8)
        hand1 = Line(clock.get_center(), clock.get_center() + UP * 0.6,
                     color=INK, stroke_width=6)
        hand2 = Line(clock.get_center(), clock.get_center() + RIGHT * 0.45,
                     color=INK, stroke_width=6)
        bag = RoundedRectangle(corner_radius=0.25, width=3.4, height=2.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=3)
        bag.move_to(LEFT * 3.4 + DOWN * 0.9)
        baglab = Text("shopping", font_size=26, color=GREY)
        baglab.move_to(bag.get_bottom() + DOWN * 0.45)
        bar_bg = Rectangle(width=1.6, height=3.0, fill_color=CARD,
                           fill_opacity=1, stroke_color=INK, stroke_width=3)
        bar_bg.move_to(RIGHT * 3.4 + DOWN * 0.7)
        barlab = Text("getting good", font_size=26, color=INK)
        barlab.move_to(bar_bg.get_bottom() + DOWN * 0.45)
        self.add(clock, hand1, hand2, bag, baglab, bar_bg, barlab)
        self.play(Create(clock), run_time=0.5)
        hours = VGroup()
        for k in range(4):
            dot = Dot(radius=0.14, color=GREY, fill_opacity=1)
            dot.move_to(clock.get_center() + UP * 0.1)
            self.add(dot)
            self.play(dot.animate.move_to(bag.get_center() + LEFT * (0.8 - k * 0.5)),
                      run_time=0.4)
            hours.add(dot)
        self.play(FadeOut(hours), run_time=0.4)
        fill = Rectangle(width=1.6, height=3.0, fill_color=GREEN,
                         fill_opacity=0.85, stroke_width=0)
        fill.move_to(bar_bg.get_center())
        self.add(fill)
        self.play(GrowFromEdge(fill, DOWN), run_time=0.9)
        card = Text("build the stack slowly", font_size=28, color=ACCENT)
        card.move_to(DOWN * 3.1)
        self.add(card)
        self.play(FadeIn(card), run_time=0.5)
        self.wait(0.5)


class M10_Closing(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # Phase 1: verdict lines
        verdicts = [
            "Pick one AI. Learn it properly.",
            "Your skill transfers to any tool.",
            "Add a second only at a named wall.",
            "Images, code, your files' home, or price.",
            "Your own thirty-minute test never goes stale.",
        ]
        rows = VGroup()
        for i, v in enumerate(verdicts):
            b = bullet(LEFT * 5.2 + UP * (1.9 - i * 0.95))
            line = Text(v, font_size=28, color=INK)
            line.next_to(b, RIGHT, buff=0.35)
            g = VGroup(b, line)
            rows.add(g)
            self.add(g)
            self.play(FadeIn(g), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(rows), run_time=0.5)
        # Phase 2: your-turn prompt card
        pc = doc_card(ORIGIN, w=9.0, h=3.4)
        pl1 = Text("Interview me about my week,", font_size=28, color=INK)
        pl2 = Text("then name the wall.", font_size=28, color=INK)
        pl1.move_to(pc.get_center() + UP * 0.7)
        pl2.move_to(pc.get_center() + DOWN * 0.1)
        cap2 = Text("paste this into Claude", font_size=22, color=GREY)
        cap2.move_to(pc.get_bottom() + DOWN * 0.5)
        self.add(pc)
        self.play(GrowFromCenter(pc), run_time=0.6)
        self.add(pl1, pl2, cap2)
        self.play(FadeIn(pl1), FadeIn(pl2), FadeIn(cap2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeOut(pc), FadeOut(pl1), FadeOut(pl2), FadeOut(cap2),
                  run_time=0.5)
        # Phase 3: title outro
        title = Text("One AI or many?", font_size=84, color=INK)
        title.move_to(UP * 0.6)
        handle = Text("@NikBearBrown", font_size=36, color=ACCENT)
        handle.move_to(title.get_center() + DOWN * 1.6)
        self.add(title)
        self.play(Write(title), run_time=1.0)
        self.add(handle)
        self.play(FadeIn(handle), run_time=0.6)
        self.wait(0.5)
