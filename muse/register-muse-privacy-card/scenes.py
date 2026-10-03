"""scenes.py — Register for Muse with a privacy.com card (Film 1).

13 Manim scenes, M01–M13. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), each scene carries distinct non-text shapes that evolve
across play() calls, every on-screen text is read aloud in its beat.
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


def coin(pos, label="$1", scale=1.0):
    c = Circle(radius=0.45, fill_color=ACCENT, fill_opacity=1,
               stroke_width=0).move_to(pos)
    t = Text(label, font_size=24, color=CARD).move_to(pos)
    return VGroup(c, t).scale(scale)


class M01_Bidea(Scene):
    def construct(self):
        form = Rectangle(width=7.0, height=4.6, stroke_color=INK,
                         stroke_width=3, fill_opacity=0)
        field = Rectangle(width=5.6, height=0.9, stroke_color=ACCENT,
                          stroke_width=5, fill_opacity=0).shift(DOWN * 1.1)
        lab = Text("credit card", font_size=24, color=GREY).next_to(
            field, UP, buff=0.25)
        card = RoundedRectangle(corner_radius=0.2, width=3.6, height=2.2,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).shift(RIGHT * 1.8)
        clim = Text("$10 limit", font_size=26, color=ACCENT).move_to(
            card.get_center())
        card_g = VGroup(card, clim)
        self.play(Create(form))
        self.play(Create(field), FadeIn(lab))
        self.play(FadeIn(card_g, shift=LEFT * 0.6), run_time=0.9)
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["Muse", "Meta account", "authorization hold", "virtual card"]
        defs = ["Meta's personal AI agent", "your Instagram / Facebook login",
                "a $1 card check, not a charge", "a privacy.com number + limit"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.4,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = Text(w, font_size=26, color=ACCENT).move_to([x, 0.55, 0])
            s = Text(d, font_size=15, color=INK).move_to([x, -0.35, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01Platforms(Scene):
    def construct(self):
        win = VGroup(
            Rectangle(width=4.4, height=3.2, stroke_color=INK, stroke_width=3,
                      fill_color=CARD, fill_opacity=1),
            Rectangle(width=4.4, height=0.5, fill_color=INK, fill_opacity=1,
                      stroke_width=0).shift(UP * 1.35),
            Text("muse.ai", font_size=24, color=INK),
        ).shift(LEFT * 4.2)
        phone = VGroup(
            RoundedRectangle(corner_radius=0.25, width=1.9, height=3.6,
                             stroke_color=INK, stroke_width=3,
                             fill_color=CARD, fill_opacity=1),
            Circle(radius=0.28, fill_color=ACCENT, fill_opacity=1,
                   stroke_width=0),
        ).shift(RIGHT * 0.2 + DOWN * 0.2)
        mac = VGroup(
            Rectangle(width=3.4, height=2.3, stroke_color=INK, stroke_width=3,
                      fill_color=CARD, fill_opacity=1).shift(UP * 0.4),
            Rectangle(width=4.2, height=0.18, fill_color=INK, fill_opacity=1,
                      stroke_width=0).shift(DOWN * 0.85),
        ).shift(RIGHT * 4.0)
        tag = tag_plate("US + Canada", [0, -2.6, 0], color=BLUE)
        self.play(GrowFromCenter(win), run_time=0.7)
        self.play(GrowFromCenter(phone), run_time=0.7)
        self.play(GrowFromCenter(mac), run_time=0.7)
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M04_B02Fork(Scene):
    def construct(self):
        dot = Dot(radius=0.16, color=INK).shift(LEFT * 5)
        q = Text("Have a Meta account?", font_size=26, color=INK).shift(
            LEFT * 5 + UP * 1.0)
        yes_arrow = Arrow([-4.4, 0, 0], [-1.2, 1.4, 0], color=GREEN, buff=0.1)
        no_arrow = Arrow([-4.4, 0, 0], [-1.2, -1.4, 0], color=GREY, buff=0.1)
        yes_lab = Text("YES: sign in", font_size=24, color=GREEN).move_to(
            [1.2, 1.6, 0])
        no_lab = Text("NO: card asked", font_size=24, color=GREY).move_to(
            [1.2, -1.6, 0])
        icons = VGroup(
            Square(side_length=0.55, fill_color=BLUE, fill_opacity=1,
                   stroke_width=0),
            Circle(radius=0.3, fill_color=ACCENT, fill_opacity=1,
                   stroke_width=0),
        ).arrange(RIGHT, buff=0.3).move_to([3.6, 1.6, 0])
        check = check_mark([4.9, 1.6, 0], scale=0.9)
        self.play(FadeIn(dot), FadeIn(q, shift=DOWN * 0.2))
        self.play(GrowArrow(yes_arrow), GrowArrow(no_arrow))
        self.play(FadeIn(yes_lab), FadeIn(no_lab), FadeIn(icons))
        self.play(Create(check))
        self.wait(1.2)


class M05_B03Hold(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.2, width=5.2, height=3.2,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).shift(LEFT * 2.2 + UP * 0.5)
        c = coin([ -2.2, 3.0, 0])
        lab = Text("hold, not a charge", font_size=26, color=INK).shift(
            RIGHT * 3.4 + UP * 1.2)
        track = Rectangle(width=5.6, height=0.28, fill_color="#EDE8DA",
                          fill_opacity=1, stroke_width=0).shift(
                              RIGHT * 3.0 + DOWN * 0.4)
        fill = Rectangle(width=0.2, height=0.28, fill_color=GREEN,
                         fill_opacity=1, stroke_width=0)
        fill.move_to([3.0 - 2.8 + 0.1, -0.4, 0])
        week = Text("released ~1 week", font_size=22, color=GREY).next_to(
            track, DOWN, buff=0.25)
        self.play(FadeIn(card))
        self.play(FadeIn(c), run_time=0.5)
        self.play(c.animate.shift(DOWN * 2.0),
                  FadeIn(lab, shift=LEFT * 0.3), run_time=0.8)
        self.play(FadeIn(fill), FadeIn(week))
        self.play(fill.animate.stretch_to_fit_width(5.6).move_to(
            [3.0, -0.4, 0]), run_time=1.0)
        self.wait(1.2)


class M06_B04VirtualCard(Scene):
    def construct(self):
        card = RoundedRectangle(corner_radius=0.25, width=6.4, height=3.8,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).shift(UP * 0.4)
        blocks = VGroup(*[
            Rectangle(width=1.1, height=0.55, fill_color="#EDE8DA",
                      fill_opacity=1, stroke_width=0).move_to(
                          [-2.2 + i * 1.45, 0.9, 0])
            for i in range(4)
        ])
        lock = bullet([-2.2, -0.5, 0], color=BLUE)
        lock_lab = Text("its own spending limit", font_size=22,
                        color=INK).next_to(lock, RIGHT, buff=0.25)
        us_tag = tag_plate("US-only", [-4.2, -2.4, 0], color=ACCENT)
        free_tag = tag_plate("free tier", [4.2, -2.4, 0], color=GREEN)
        self.play(GrowFromCenter(card), run_time=0.8)
        self.play(*[FadeIn(b) for b in blocks], run_time=0.8)
        self.play(FadeIn(lock), FadeIn(lock_lab, shift=RIGHT * 0.2))
        self.play(FadeIn(us_tag, shift=UP * 0.3),
                  FadeIn(free_tag, shift=UP * 0.3))
        self.wait(1.2)


class M07_B05NewCard(Scene):
    def construct(self):
        s1 = RoundedRectangle(corner_radius=0.2, width=4.6, height=3.4,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK).shift(LEFT * 3.6)
        bank = Rectangle(width=1.4, height=0.9, fill_color=BLUE,
                         fill_opacity=1, stroke_width=0).move_to(
                             [-4.6, 0.8, 0])
        idc = check_mark([-2.6, 0.8, 0], scale=0.7)
        s1_lab = Text("1. account: bank + ID check", font_size=20,
                      color=INK).move_to([-3.6, -0.9, 0])
        arrow = Arrow([-1.0, 0, 0], [0.6, 0, 0], color=ACCENT, buff=0.1)
        s2 = RoundedRectangle(corner_radius=0.2, width=4.6, height=3.4,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK).shift(RIGHT * 3.6)
        btn = RoundedRectangle(corner_radius=0.15, width=2.2, height=0.8,
                               fill_color=ACCENT, fill_opacity=1,
                               stroke_width=0).move_to([3.6, 0.8, 0])
        btn_lab = Text("New Card", font_size=20, color=CARD).move_to(
            btn.get_center())
        num = VGroup(*[
            Rectangle(width=0.8, height=0.4, fill_color="#EDE8DA",
                      fill_opacity=1, stroke_width=0).move_to(
                          [2.4 + i * 1.0, -0.5, 0])
            for i in range(4)
        ])
        s2_lab = Text("2. fresh number + CVV", font_size=20, color=INK).move_to(
            [3.6, -1.5, 0])
        self.play(FadeIn(s1), FadeIn(bank), Create(idc), FadeIn(s1_lab))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(s2), FadeIn(VGroup(btn, btn_lab), shift=DOWN * 0.2))
        self.play(*[FadeIn(n) for n in num], FadeIn(s2_lab), run_time=0.8)
        self.wait(1.2)


class M08_B06Limit(Scene):
    def construct(self):
        track = Line([-4.5, 0.8, 0], [4.5, 0.8, 0], color=GREY,
                     stroke_width=8)
        knob = Circle(radius=0.32, fill_color=ACCENT, fill_opacity=1,
                      stroke_width=0).move_to([-4.5, 0.8, 0])
        lab = Text("$10", font_size=30, color=ACCENT).move_to([4.5, 1.7, 0])
        bar = Rectangle(width=6.0, height=0.7, fill_color="#EDE8DA",
                        fill_opacity=1, stroke_width=0).shift(DOWN * 1.2)
        cap = Rectangle(width=6.0, height=0.7, fill_color=GREEN, fill_opacity=1,
                        stroke_width=0).shift(DOWN * 1.2)
        c = coin([-2.0, 1.8, 0], scale=0.8)
        big = RoundedRectangle(corner_radius=0.15, width=2.2, height=1.1,
                               fill_color=ACCENT, fill_opacity=0.85,
                               stroke_width=0).move_to([2.5, 1.8, 0])
        big_lab = Text("$50?", font_size=26, color=CARD).move_to(
            big.get_center())
        denied = Text("declined", font_size=24, color=ACCENT).move_to(
            [2.5, -2.6, 0])
        self.play(Create(track), FadeIn(knob))
        self.play(knob.animate.move_to([4.5, 0.8, 0]), FadeIn(lab),
                  run_time=0.9)
        self.play(FadeIn(bar))
        self.play(FadeIn(c), run_time=0.5)
        self.play(c.animate.shift(DOWN * 1.9), run_time=0.7)
        self.play(FadeIn(VGroup(big, big_lab), shift=DOWN * 0.4))
        self.play(VGroup(big, big_lab).animate.shift(UP * 0.7),
                  FadeIn(denied, shift=UP * 0.2), run_time=0.7)
        self.wait(1.2)


class M09_B07UseIt(Scene):
    def construct(self):
        form = Rectangle(width=5.4, height=4.4, stroke_color=INK, stroke_width=3,
                         fill_opacity=0).shift(LEFT * 2.6)
        fields = VGroup(*[
            Rectangle(width=4.2, height=0.7, stroke_color=GREY, stroke_width=2,
                      fill_opacity=0).move_to([-2.6, 1.2 - i * 1.1, 0])
            for i in range(3)
        ])
        card = RoundedRectangle(corner_radius=0.2, width=3.4, height=2.1,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).shift(RIGHT * 4.4 + UP * 1.0)
        details = VGroup(*[
            Rectangle(width=1.9, height=0.4, fill_color=BLUE, fill_opacity=1,
                      stroke_width=0).move_to([4.4, 1.6 - i * 0.6, 0])
            for i in range(3)
        ])
        check = check_mark([-2.6, -1.6, 0], scale=1.0)
        pause = VGroup(
            Rectangle(width=0.28, height=0.9, fill_color=GREY, fill_opacity=1,
                      stroke_width=0),
            Rectangle(width=0.28, height=0.9, fill_color=GREY, fill_opacity=1,
                      stroke_width=0),
        ).arrange(RIGHT, buff=0.25).move_to([4.4, -1.2, 0])
        pause_lab = Text("pause after", font_size=20, color=GREY).next_to(
            pause, DOWN, buff=0.25)
        self.play(Create(form), *[Create(f) for f in fields])
        self.play(FadeIn(card), *[FadeIn(d) for d in details])
        self.play(*[d.animate.shift(LEFT * 4.4 + DOWN * (0.4 + i * 0.5))
                     for i, d in enumerate(details)], run_time=1.0)
        self.play(Create(check))
        self.play(FadeIn(pause), FadeIn(pause_lab, shift=UP * 0.2))
        self.wait(1.2)


class M10_B08Names(Scene):
    def construct(self):
        f1 = Rectangle(width=5.2, height=1.0, stroke_color=INK, stroke_width=3,
                       fill_opacity=0).shift(UP * 1.2)
        l1 = Text("Your name", font_size=24, color=GREY).move_to(
            f1.get_center() + LEFT * 1.4)
        f2 = Rectangle(width=5.2, height=1.0, stroke_color=INK, stroke_width=3,
                       fill_opacity=0).shift(DOWN * 0.4)
        l2 = Text("Agent name", font_size=24, color=GREY).move_to(
            f2.get_center() + LEFT * 1.3)
        cursor = Rectangle(width=0.08, height=0.5, fill_color=ACCENT,
                           fill_opacity=1, stroke_width=0).move_to(
                               f1.get_center() + RIGHT * 0.4)
        bubble = Ellipse(width=4.6, height=1.6, fill_color=CARD, fill_opacity=1,
                         stroke_color=INK).shift(DOWN * 2.2)
        blab = Text("personal, not shared", font_size=22, color=INK).move_to(
            bubble.get_center())
        self.play(Create(f1), FadeIn(l1, shift=RIGHT * 0.2))
        self.play(FadeIn(cursor))
        self.play(cursor.animate.shift(RIGHT * 1.2), run_time=0.6)
        self.play(Create(f2), FadeIn(l2, shift=RIGHT * 0.2),
                  cursor.animate.move_to(f2.get_center() + RIGHT * 0.4))
        self.play(GrowFromCenter(bubble), FadeIn(blab))
        self.wait(1.2)


class M11_B09Connect(Scene):
    def construct(self):
        c1 = RoundedRectangle(corner_radius=0.2, width=4.8, height=2.6,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK).shift(LEFT * 2.8 + UP * 0.4)
        t1 = Text("Gmail", font_size=28, color=INK).move_to([-3.9, 1.0, 0])
        tr1 = RoundedRectangle(corner_radius=0.2, width=1.3, height=0.6,
                               fill_color="#EDE8DA", fill_opacity=1,
                               stroke_width=0).move_to([-1.9, 1.0, 0])
        k1 = Circle(radius=0.26, fill_color=GREY, fill_opacity=1,
                    stroke_width=0).move_to([-2.25, 1.0, 0])
        c2 = RoundedRectangle(corner_radius=0.2, width=4.8, height=2.6,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=INK).shift(RIGHT * 2.8 + UP * 0.4)
        t2 = Text("Google Calendar", font_size=24, color=INK).move_to(
            [1.7, 1.0, 0])
        tr2 = RoundedRectangle(corner_radius=0.2, width=1.3, height=0.6,
                               fill_color="#EDE8DA", fill_opacity=1,
                               stroke_width=0).move_to([3.7, 1.0, 0])
        k2 = Circle(radius=0.26, fill_color=GREY, fill_opacity=1,
                    stroke_width=0).move_to([3.35, 1.0, 0])
        opt = tag_plate("optional", [0, -2.2, 0], color=BLUE)
        self.play(FadeIn(c1), FadeIn(t1), FadeIn(tr1), FadeIn(k1))
        self.play(FadeIn(c2), FadeIn(t2), FadeIn(tr2), FadeIn(k2))
        self.play(k1.animate.move_to([-1.55, 1.0, 0]).set_fill(GREEN),
                  k2.animate.move_to([4.05, 1.0, 0]).set_fill(GREEN),
                  run_time=0.8)
        self.play(FadeIn(opt, shift=UP * 0.3))
        self.wait(1.2)


class M12_B10YoureIn(Scene):
    def construct(self):
        desk = Rectangle(width=9, height=0.25, fill_color=INK, fill_opacity=1,
                         stroke_width=0).shift(DOWN * 2.2)
        head = Circle(radius=0.5, fill_color=ACCENT, fill_opacity=1,
                      stroke_width=0).shift(LEFT * 3 + DOWN * 1.1)
        body = Rectangle(width=1.0, height=1.2, fill_color=ACCENT,
                         fill_opacity=1, stroke_width=0).shift(
                             LEFT * 3 + DOWN * 0.1)
        screen = Rectangle(width=3.4, height=2.2, fill_color=CARD,
                           fill_opacity=1, stroke_color=INK).shift(
                               RIGHT * 2.2 + UP * 0.3)
        gauge_track = Rectangle(width=4.4, height=0.5, fill_color="#EDE8DA",
                                fill_opacity=1, stroke_width=0).shift(
                                    DOWN * 2.9)
        gauge_fill = Rectangle(width=0.3, height=0.5, fill_color=BLUE,
                               fill_opacity=1, stroke_width=0)
        gauge_fill.move_to([-2.2 + 0.15, -2.9, 0])
        gauge_lab = Text("free tier: usage limit", font_size=20,
                         color=GREY).next_to(gauge_track, DOWN, buff=0.2)
        stamp = RoundedRectangle(corner_radius=0.15, width=6.4, height=1.0,
                                 stroke_color=GREEN, stroke_width=4,
                                 fill_opacity=0).shift(UP * 2.6).rotate(
                                     -0.06)
        stamp_lab = Text("real card never touched the form", font_size=22,
                         color=GREEN).move_to(stamp.get_center()).rotate(-0.06)
        self.play(FadeIn(desk), FadeIn(head), FadeIn(body), FadeIn(screen))
        self.play(FadeIn(gauge_fill), FadeIn(gauge_lab))
        self.play(gauge_fill.animate.stretch_to_fit_width(2.6).move_to(
            [-2.2 + 1.3, -2.9, 0]), run_time=0.9)
        self.play(GrowFromCenter(stamp), FadeIn(stamp_lab, shift=DOWN * 0.2))
        self.wait(1.2)


class M13_BvdtHtfOut(Scene):
    def construct(self):
        recap_mobs = []
        plate = RoundedRectangle(corner_radius=0.25, width=12.4, height=5.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).shift(UP * 0.5)
        recap_mobs.append(plate)
        lines = [
            "The fork: Meta account skips it; else a $1 hold.",
            "The workaround: privacy.com card, $10 limit.",
            "Setup: your name, your agent's name, your apps.",
        ]
        self.play(FadeIn(plate))
        for i, ln in enumerate(lines):
            y = 1.9 - i * 1.1
            b = bullet([-5.9, y + 0.5, 0])
            t = Text(ln, font_size=20, color=INK)
            t.move_to([-5.4 + t.width / 2, y + 0.5, 0])
            recap_mobs += [b, t]
            self.play(FadeIn(b, scale=1.5), FadeIn(t, shift=RIGHT * 0.3),
                      run_time=0.7)
        do = RoundedRectangle(corner_radius=0.2, width=8.4, height=2.2,
                              fill_color="#EDE8DA", fill_opacity=1,
                              stroke_width=0).shift(DOWN * 2.6)
        d1 = Text("1. privacy.com: new card, $10 limit", font_size=22,
                  color=INK).move_to([-2.2, -2.3, 0])
        d2 = Text("2. muse.ai: register", font_size=22, color=INK).move_to(
            [2.6, -2.9, 0])
        recap_mobs += [do, d1, d2]
        self.play(FadeIn(do), FadeIn(d1, shift=UP * 0.2),
                  FadeIn(d2, shift=UP * 0.2))
        self.play(*[FadeOut(m) for m in recap_mobs], run_time=0.5)
        wm = RoundedRectangle(corner_radius=0.2, width=5.2, height=1.2,
                              fill_color=INK, fill_opacity=1,
                              stroke_width=0).shift(DOWN * 0.4)
        wlab = Text("@NikBearBrown", font_size=28, color=PAPER).move_to(
            wm.get_center())
        self.play(GrowFromCenter(wm), FadeIn(wlab))
        self.wait(1.2)
