"""scenes.py — What never to paste into AI (what-never-to-paste-into-ai).

12 Manim scenes, M01-M12. House conventions: 16:9, safe-area coords
(+-6.3 x, +-3.4 y), each scene carries distinct non-text shapes that evolve
across play() calls, every on-screen text is read aloud in its beat.
All example data is obviously fake (test card number, EXAMPLE/fake strings).
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


def ban_sign(pos, scale=1.0, color=ACCENT):
    ring = Circle(radius=1.1, stroke_color=color, stroke_width=14,
                  fill_opacity=0)
    bar = Line(LEFT * 0.78 + UP * 0.78, RIGHT * 0.78 + DOWN * 0.78,
               color=color, stroke_width=14)
    g = VGroup(ring, bar).scale(scale).move_to(pos)
    return g


def toggle_switch(pos, on=True, scale=1.0):
    track = RoundedRectangle(corner_radius=0.3, width=1.6, height=0.7,
                             fill_color="#EDE8DA" if on else GREEN,
                             fill_opacity=1, stroke_width=0)
    knob = Circle(radius=0.3, fill_color=GREY if on else CARD, fill_opacity=1,
                  stroke_width=0)
    knob.move_to([-0.42 if on else 0.42, 0, 0])
    g = VGroup(track, knob).scale(scale).move_to(pos)
    return g, track, knob


def cross_out(pos, width, height=0.55, color=INK):
    x1 = Line([-width / 2, height / 2, 0], [width / 2, -height / 2, 0],
              color=color, stroke_width=5).move_to(pos)
    x2 = Line([-width / 2, -height / 2, 0], [width / 2, height / 2, 0],
              color=color, stroke_width=5).move_to(pos)
    return VGroup(x1, x2)


def person_icon(pos, scale=1.0, color=INK):
    head = Circle(radius=0.28, fill_color=color, fill_opacity=1,
                  stroke_width=0)
    body = RoundedRectangle(corner_radius=0.2, width=0.7, height=0.9,
                            fill_color=color, fill_opacity=1,
                            stroke_width=0)
    body.next_to(head, DOWN, buff=0.08)
    g = VGroup(head, body).scale(scale).move_to(pos)
    return g


class M01_Bidea(Scene):
    def construct(self):
        bubble = RoundedRectangle(corner_radius=0.3, width=3.4, height=2.0,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=INK).shift(LEFT * 4.4 + UP * 0.4)
        blab = Text("chat", font_size=24, color=INK).move_to(
            bubble.get_center())
        arrow = Arrow([-2.3, 0.4, 0], [0.6, 0.4, 0], color=ACCENT, buff=0.1)
        card = Rectangle(width=4.6, height=3.2, stroke_color=INK,
                         stroke_width=3, fill_color=CARD,
                         fill_opacity=1).shift(RIGHT * 3.4 + UP * 0.4)
        stamp = Rectangle(width=1.0, height=1.2, stroke_color=BLUE,
                          stroke_width=4, fill_opacity=0).move_to(
                              [4.9, 1.2, 0])
        addr = VGroup(*[
            Rectangle(width=2.6, height=0.22, fill_color="#EDE8DA",
                      fill_opacity=1, stroke_width=0).move_to(
                          [3.0, 0.3 - i * 0.45, 0])
            for i in range(3)
        ])
        clab = Text("postcard", font_size=22, color=INK).move_to(
            [3.4, -1.9, 0])
        tag = tag_plate("like a postcard", [0, -2.9, 0], color=ACCENT)
        self.play(FadeIn(bubble), FadeIn(blab))
        self.play(GrowArrow(arrow), run_time=0.7)
        self.play(FadeIn(card), Create(stamp), FadeIn(addr), FadeIn(clab),
                  run_time=0.9)
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        terms = [
            ("postcard test", "would you write it on a postcard?"),
            ("training", "chats improve the AI model"),
            ("retention", "how long chats are kept"),
            ("redaction", "blacking bits out"),
            ("anonymize", "real names -> fakes"),
            ("credential", "anything that logs you in"),
        ]
        xs = [-4.2, 0.0, 4.2]
        ys = [1.25, -1.15]
        for i, (w, d) in enumerate(terms):
            x = xs[i % 3]
            y = ys[i // 3]
            box = RoundedRectangle(corner_radius=0.2, width=3.6, height=2.0,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, y, 0])
            t = Text(w, font_size=22, color=ACCENT).move_to([x, y + 0.45, 0])
            s = Text(d, font_size=13, color=INK).move_to([x, y - 0.4, 0])
            self.play(FadeIn(VGroup(box, t, s), shift=UP * 0.25),
                      run_time=0.55)
        self.wait(1.2)


class M03_B01Why(Scene):
    def construct(self):
        phone = RoundedRectangle(corner_radius=0.3, width=2.2, height=3.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).shift(LEFT * 4.6)
        plab = Text("you paste", font_size=20, color=INK).move_to(
            [-4.6, -2.6, 0])
        arrow = Arrow([-3.2, 0, 0], [-1.2, 0, 0], color=ACCENT, buff=0.1)
        server = RoundedRectangle(corner_radius=0.2, width=3.2, height=3.6,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=INK).move_to([0.6, 0, 0])
        slab = Text("company servers", font_size=20, color=INK).move_to(
            [0.6, -2.6, 0])
        self.play(FadeIn(phone), FadeIn(plab))
        self.play(GrowArrow(arrow), FadeIn(server), FadeIn(slab),
                  run_time=0.9)
        plates = [
            ("stored", 1.9, BLUE),
            ("reviewed by staff", 0.5, ACCENT),
            ("may train the model", -0.9, INK),
        ]
        for lab, y, col in plates:
            p = tag_plate(lab, [4.6, y, 0], color=col)
            self.play(FadeIn(p, shift=LEFT * 0.3), run_time=0.6)
        tag = tag_plate("not will — can", [-1.4, -2.9, 0], color=ACCENT)
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M04_B02Settings(Scene):
    def construct(self):
        p = RoundedRectangle(corner_radius=0.2, width=5.2, height=3.2,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=ACCENT, stroke_width=4).move_to(
                                 [-3.2, 0.6, 0])
        pt = Text("Personal plan", font_size=26, color=ACCENT).move_to(
            [-3.2, 1.5, 0])
        ps = Text("find the training toggle", font_size=16,
                  color=INK).move_to([-3.2, 0.4, 0])
        tog, track, knob = toggle_switch([-3.2, -0.6, 0], on=True)
        e = RoundedRectangle(corner_radius=0.2, width=5.2, height=3.2,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=GREEN, stroke_width=4).move_to(
                                 [3.2, 0.6, 0])
        et = Text("Business plan", font_size=26, color=GREEN).move_to(
            [3.2, 1.5, 0])
        es = Text("no training by default", font_size=16,
                  color=INK).move_to([3.2, 0.4, 0])
        eck = check_mark([3.2, -0.6, 0], scale=0.8)
        tag = tag_plate("defaults change — check yours", [0, -2.6, 0],
                        color=INK)
        self.play(FadeIn(p), FadeIn(pt), FadeIn(ps), FadeIn(tog))
        self.play(knob.animate.shift(RIGHT * 0.84),
                  track.animate.set_fill(GREEN), run_time=0.8)
        self.play(FadeIn(e), FadeIn(et), FadeIn(es), Create(eck))
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M05_B03Passwords(Scene):
    def construct(self):
        doc = RoundedRectangle(corner_radius=0.2, width=7.6, height=4.2,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).shift(UP * 0.6)
        rows = [
            "password: pa55word-EXAMPLE",
            "api key: sk-fake-0000",
        ]
        self.play(FadeIn(doc))
        for i, row in enumerate(rows):
            y = 1.7 - i * 1.2
            bar = Rectangle(width=5.6, height=0.7, fill_color=ACCENT,
                            fill_opacity=0.85, stroke_width=0).move_to(
                                [-0.8, y, 0])
            s = Text(row, font_size=18, color=CARD).move_to(bar.get_center())
            self.play(FadeIn(bar), FadeIn(s), run_time=0.5)
            x = cross_out([-0.8, y, 0], 5.8, color=INK)
            self.play(Create(x), run_time=0.5)
        sign = ban_sign([4.6, 0.6, 0], scale=0.9)
        self.play(GrowFromCenter(sign), run_time=0.8)
        tag = tag_plate("whoever sees it owns the account", [0, -2.9, 0],
                        color=ACCENT)
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M06_B04Money(Scene):
    def construct(self):
        doc = RoundedRectangle(corner_radius=0.2, width=7.6, height=4.2,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).shift(UP * 0.6)
        rows = [
            "card: 4111 1111 1111 1111",
            "routing: 000000000",
        ]
        self.play(FadeIn(doc))
        for i, row in enumerate(rows):
            y = 1.7 - i * 1.2
            bar = Rectangle(width=5.2, height=0.7, fill_color=ACCENT,
                            fill_opacity=0.85, stroke_width=0).move_to(
                                [-0.8, y, 0])
            s = Text(row, font_size=18, color=CARD).move_to(bar.get_center())
            self.play(FadeIn(bar), FadeIn(s), run_time=0.5)
            x = cross_out([-0.8, y, 0], 5.4, color=INK)
            self.play(Create(x), run_time=0.5)
        key = tag_plate("keys, not facts", [4.4, -1.4, 0], color=BLUE)
        self.play(FadeIn(key, shift=UP * 0.3))
        tag = tag_plate("'two grand in checking' is fine", [0, -2.9, 0],
                        color=INK)
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M07_B05OtherPeople(Scene):
    def construct(self):
        items = [
            ("kid's name + school", -4.2),
            ("medical details", 0.0),
            ("a friend's message", 4.2),
        ]
        for lab, x in items:
            ic = person_icon([x, 0.8, 0], scale=1.0, color=BLUE)
            t = Text(lab, font_size=17, color=INK).move_to([x, -0.9, 0])
            self.play(FadeIn(ic, shift=UP * 0.2), FadeIn(t, shift=UP * 0.2),
                      run_time=0.6)
        sign = ban_sign([0, 0.3, 0], scale=1.5, color=ACCENT)
        self.play(GrowFromCenter(sign), run_time=0.8)
        tag = tag_plate("you can't consent for them", [0, -2.7, 0],
                        color=ACCENT)
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M08_B06Work(Scene):
    def construct(self):
        slips = ["client data", "unreleased numbers", "internal code"]
        for i, lab in enumerate(slips):
            y = 2.4 - i * 1.1
            s = tag_plate(lab, [-4.6, y, 0], color=GREY)
            self.play(FadeIn(s, shift=RIGHT * 0.3), run_time=0.5)
        box = Rectangle(width=4.6, height=3.4, stroke_color=INK,
                        stroke_width=3, fill_color=CARD,
                        fill_opacity=1).shift(RIGHT * 3.0 + UP * 0.3)
        lock = RoundedRectangle(corner_radius=0.1, width=1.2, height=1.0,
                                fill_color=ACCENT, fill_opacity=1,
                                stroke_width=0).move_to([3.0, 0.0, 0])
        shackle = Arc(radius=0.45, start_angle=0, angle=PI, color=INK,
                      stroke_width=6).move_to([3.0, 0.55, 0])
        wlab = Text("locked", font_size=20, color=INK).move_to(
            [3.0, -2.0, 0])
        self.play(FadeIn(box), FadeIn(lock), Create(shackle), FadeIn(wlab))
        arrow = Arrow([-1.4, 0.3, 0], [0.5, 0.3, 0], color=ACCENT, buff=0.1)
        x = cross_out([-0.45, 0.3, 0], 1.6, height=1.4, color=ACCENT)
        self.play(GrowArrow(arrow))
        self.play(Create(x), run_time=0.6)
        tag = tag_plate("not yours to paste", [0, -2.9, 0], color=INK)
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M09_B07Redact(Scene):
    def construct(self):
        doc = RoundedRectangle(corner_radius=0.2, width=7.6, height=4.2,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).shift(UP * 0.6)
        rows = [
            "acct: 0000-0000",
            "password: EXAMPLE",
            "name: Redacted",
        ]
        self.play(FadeIn(doc))
        bars = []
        for i, row in enumerate(rows):
            y = 1.8 - i * 1.1
            bar = Rectangle(width=4.6, height=0.6, fill_color="#EDE8DA",
                            fill_opacity=1, stroke_width=0).move_to(
                                [-0.6, y, 0])
            s = Text(row, font_size=17, color=INK).move_to(bar.get_center())
            self.play(FadeIn(bar), FadeIn(s), run_time=0.5)
            blk = Rectangle(width=4.6, height=0.6, fill_color=INK,
                            fill_opacity=1, stroke_width=0).move_to(
                                [-0.6, y, 0])
            bars.append(blk)
            self.play(FadeIn(blk, shift=RIGHT * 0.2), run_time=0.5)
        check = check_mark([5.2, 0.6, 0], scale=1.0)
        self.play(Create(check))
        tag = tag_plate("the AI answers anyway", [0, -2.9, 0], color=GREEN)
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M10_B08Anonymize(Scene):
    def construct(self):
        reals = ["Acme Corp", "$4.2M", "contract v9"]
        holds = ["[CLIENT X]", "[R]", "[DOC]"]
        for i, (real, hold) in enumerate(zip(reals, holds)):
            y = 1.8 - i * 1.1
            r = Text(real, font_size=19, color=ACCENT).move_to([-4.4, y, 0])
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.5)
            x = cross_out([-4.4, y, 0], 2.6, color=INK)
            self.play(Create(x), run_time=0.4)
            arr = Arrow([-2.4, y, 0], [-0.8, y, 0], color=BLUE, buff=0.1)
            ph = Text(hold, font_size=19, color=BLUE).move_to([1.6, y, 0])
            self.play(GrowArrow(arr), FadeIn(ph, shift=LEFT * 0.2),
                      run_time=0.5)
        tag = tag_plate("summarize the document, don't upload it",
                        [0, -2.6, 0], color=INK)
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M11_B09Pause(Scene):
    def construct(self):
        card = Rectangle(width=5.6, height=3.6, stroke_color=INK,
                         stroke_width=3, fill_color=CARD,
                         fill_opacity=1).shift(UP * 0.4)
        stamp = Rectangle(width=1.0, height=1.2, stroke_color=BLUE,
                          stroke_width=4, fill_opacity=0).move_to(
                              [1.9, 1.2, 0])
        q = Text("?", font_size=120, color=ACCENT).move_to([-0.6, 0.4, 0])
        pause1 = Rectangle(width=0.3, height=1.2, fill_color=GREEN,
                           fill_opacity=1, stroke_width=0).move_to(
                               [-4.6, -2.2, 0])
        pause2 = Rectangle(width=0.3, height=1.2, fill_color=GREEN,
                           fill_opacity=1, stroke_width=0).move_to(
                               [-3.9, -2.2, 0])
        tag = tag_plate("the 3-second pause", [2.4, -2.9, 0], color=INK)
        self.play(FadeIn(card), Create(stamp))
        self.play(FadeIn(q, scale=1.4), run_time=0.8)
        self.play(FadeIn(pause1), FadeIn(pause2))
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M12_RecapHtfOut(Scene):
    def construct(self):
        recap_mobs = []
        plate = RoundedRectangle(corner_radius=0.25, width=12.4, height=5.0,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).shift(UP * 0.7)
        recap_mobs.append(plate)
        lines = [
            "A chat is a postcard, not a diary.",
            "Pasted text can be stored, reviewed, trained on.",
            "Never: passwords, credentials, money numbers.",
            "Never other people's private details.",
            "Never work secrets you don't own.",
            "Redact, anonymize, or describe. Ask first.",
        ]
        self.play(FadeIn(plate))
        for i, ln in enumerate(lines):
            y = 2.5 - i * 0.75
            b = bullet([-5.9, y + 0.7, 0])
            t = Text(ln, font_size=18, color=INK)
            t.move_to([-5.4 + t.width / 2, y + 0.7, 0])
            recap_mobs += [b, t]
            self.play(FadeIn(b, scale=1.5), FadeIn(t, shift=RIGHT * 0.3),
                      run_time=0.6)
        do = RoundedRectangle(corner_radius=0.2, width=9.4, height=1.6,
                              fill_color="#EDE8DA", fill_opacity=1,
                              stroke_width=0).shift(DOWN * 2.7)
        d1 = Text("1. Paste the privacy-coach prompt", font_size=20,
                  color=INK).move_to([-2.8, -2.5, 0])
        d2 = Text("2. Check: is training still on?", font_size=20,
                  color=INK).move_to([2.6, -3.0, 0])
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
