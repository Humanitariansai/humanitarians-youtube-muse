"""scenes.py — Stop using your own Claude at work (personal-ai-at-work).

12 Manim scenes, M01-M12. House conventions: 16:9, safe-area coords
(+-6.3 x, +-3.4 y), each scene carries distinct non-text shapes that evolve
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


class M01_Bidea(Scene):
    def construct(self):
        win = Rectangle(width=5.2, height=3.8, stroke_color=INK,
                        stroke_width=3, fill_color=CARD, fill_opacity=1)
        head = Rectangle(width=5.2, height=0.6, fill_color=INK,
                         fill_opacity=1, stroke_width=0).shift(UP * 1.6)
        slip = RoundedRectangle(corner_radius=0.15, width=3.8, height=1.6,
                                fill_color="#EDE8DA", fill_opacity=1,
                                stroke_width=0).shift(DOWN * 2.9)
        slip_bar = Rectangle(width=2.8, height=0.35, fill_color=ACCENT,
                             fill_opacity=1, stroke_width=0).move_to(
                                 slip.get_center())
        slip_g = VGroup(slip, slip_bar)
        arrow = Arrow([-1.6, 0, 0], [1.6, 0, 0], color=ACCENT, buff=0.1)
        model = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).shift(RIGHT * 4.2)
        gear = Circle(radius=0.5, stroke_color=BLUE, stroke_width=8,
                      fill_opacity=0).move_to(model.get_center())
        m_lab = Text("model", font_size=22, color=INK).next_to(
            model, DOWN, buff=0.2)
        tag = tag_plate("kept for years", [4.2, -2.9, 0], color=ACCENT)
        self.play(Create(win), FadeIn(head))
        self.play(FadeIn(slip_g, shift=UP * 0.5))
        self.play(slip_g.animate.shift(UP * 1.9), run_time=0.8)
        self.play(GrowArrow(arrow))
        self.play(FadeIn(model), Create(gear), FadeIn(m_lab))
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        terms = [
            ("personal AI", "a chatbot account that's yours"),
            ("training", "your chats improve the model"),
            ("retention", "how long chats are kept"),
            ("NDA", "the secrecy agreement you signed"),
            ("anonymize", "strip names before you paste"),
            ("enterprise plan", "business account, no training"),
        ]
        xs = [-4.2, 0.0, 4.2]
        ys = [1.25, -1.15]
        cards = []
        for i, (w, d) in enumerate(terms):
            x = xs[i % 3]
            y = ys[i // 3]
            box = RoundedRectangle(corner_radius=0.2, width=3.6, height=2.0,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, y, 0])
            t = Text(w, font_size=22, color=ACCENT).move_to([x, y + 0.45, 0])
            s = Text(d, font_size=13, color=INK).move_to([x, y - 0.4, 0])
            cards.append(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.25), run_time=0.55)
        self.wait(1.2)


class M03_B01Samsung(Scene):
    def construct(self):
        line = Line([-5.5, 0, 0], [5.5, 0, 0], color=INK, stroke_width=6)
        d0 = tag_plate("day 0: permission", [-4.4, 1.3, 0], color=BLUE)
        leaks = [
            (-2.4, "source code", UP),
            (0.4, "yield code", DOWN),
            (3.0, "meeting recording", UP),
        ]
        self.play(Create(line), FadeIn(d0, shift=DOWN * 0.3))
        for x, lab, side in leaks:
            pip = Dot(radius=0.22, color=ACCENT).move_to([x, 0, 0])
            t = Text(lab, font_size=20, color=INK).move_to(
                [x, 0.9 * side[1], 0])
            tick = Line([x, -0.25, 0], [x, 0.25, 0], color=ACCENT,
                        stroke_width=6)
            self.play(FadeIn(pip, scale=1.6), Create(tick),
                      FadeIn(t, shift=side * 0.2 * -1), run_time=0.7)
        cap = tag_plate("3 leaks in 20 days", [0, -2.6, 0], color=ACCENT)
        self.play(FadeIn(cap, shift=UP * 0.3))
        self.wait(1.2)


class M04_B02Ban(Scene):
    def construct(self):
        win = Rectangle(width=4.6, height=3.4, stroke_color=INK,
                        stroke_width=3, fill_color=CARD, fill_opacity=1)
        head = Rectangle(width=4.6, height=0.55, fill_color=INK,
                         fill_opacity=1, stroke_width=0).shift(UP * 1.425)
        lines = VGroup(*[
            Rectangle(width=3.2, height=0.32, fill_color="#EDE8DA",
                      fill_opacity=1, stroke_width=0).move_to(
                          [0, 0.7 - i * 0.65, 0])
            for i in range(3)
        ])
        sign = ban_sign([0, 0, 0], scale=1.15)
        ban_tag = tag_plate("company-wide ban", [-3.9, -2.7, 0],
                            color=ACCENT)
        inv_tag = tag_plate("disciplinary investigations", [3.9, -2.7, 0],
                            color=INK)
        self.play(Create(win), FadeIn(head), FadeIn(lines))
        self.play(GrowFromCenter(sign), run_time=0.8)
        self.play(FadeIn(ban_tag, shift=UP * 0.3),
                  FadeIn(inv_tag, shift=UP * 0.3))
        self.wait(1.2)


class M05_B03Mechanism(Scene):
    def construct(self):
        bubbles = VGroup(*[
            RoundedRectangle(corner_radius=0.25, width=2.6, height=0.9,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK).move_to([-4.2, 1.4 - i * 1.3, 0])
            for i in range(3)
        ])
        arrow = Arrow([-2.5, 0.4, 0], [-0.4, 0.4, 0], color=ACCENT, buff=0.1)
        model = RoundedRectangle(corner_radius=0.2, width=3.4, height=2.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).shift(RIGHT * 2.6 + UP * 0.4)
        gear = Circle(radius=0.55, stroke_color=BLUE, stroke_width=8,
                      fill_opacity=0).move_to(model.get_center())
        m_lab = Text("improves the model", font_size=18, color=INK).next_to(
            model, DOWN, buff=0.2)
        row = RoundedRectangle(corner_radius=0.2, width=9.6, height=1.3,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).shift(DOWN * 2.6)
        r_lab = Text("Settings > Privacy: 'Help improve our AI models'",
                     font_size=18, color=INK).move_to([-1.4, -2.6, 0])
        tog, track, knob = toggle_switch([3.9, -2.6, 0], on=True)
        self.play(*[FadeIn(b, shift=RIGHT * 0.3) for b in bubbles],
                  run_time=0.8)
        self.play(GrowArrow(arrow))
        self.play(FadeIn(model), Create(gear), FadeIn(m_lab))
        self.play(FadeIn(row), FadeIn(r_lab), FadeIn(tog))
        self.play(knob.animate.move_to([3.9 + 0.42, -2.6, 0]),
                  run_time=0.7)
        self.wait(1.2)


class M06_B04Retention(Scene):
    def construct(self):
        on_lab = Text("setting ON", font_size=22, color=ACCENT).move_to(
            [-5.0, 1.4, 0])
        bar_on = Rectangle(width=8.4, height=0.7, fill_color=ACCENT,
                           fill_opacity=1, stroke_width=0)
        bar_on.move_to([-1.2 + 4.2, 1.4, 0])
        on_val = Text("up to 5 years", font_size=20, color=ACCENT).move_to(
            [4.4, 0.7, 0])
        off_lab = Text("setting OFF", font_size=22, color=GREEN).move_to(
            [-5.0, -0.4, 0])
        bar_off = Rectangle(width=1.0, height=0.7, fill_color=GREEN,
                            fill_opacity=1, stroke_width=0)
        bar_off.move_to([-1.2 + 0.5, -0.4, 0])
        off_val = Text("~30 days", font_size=20, color=GREEN).move_to(
            [0.4, -1.1, 0])
        tag = tag_plate("opt-out starts now — can't pull back old data",
                        [0, -2.6, 0], color=INK)
        self.play(FadeIn(on_lab))
        self.play(FadeIn(bar_on), FadeIn(on_val, shift=LEFT * 0.3),
                  run_time=0.8)
        self.play(FadeIn(off_lab))
        self.play(FadeIn(bar_off), FadeIn(off_val, shift=LEFT * 0.3),
                  run_time=0.8)
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M07_B05ClaudeToggle(Scene):
    def construct(self):
        panel = RoundedRectangle(corner_radius=0.25, width=8.6, height=4.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).shift(UP * 0.4)
        head = Text("Settings", font_size=30, color=INK).move_to(
            [-3.4, 2.0, 0])
        prowl = Text("Privacy", font_size=24, color=GREY).move_to(
            [-3.4, 1.0, 0])
        lab = Text("'Help improve our AI models'", font_size=22,
                   color=INK).move_to([-1.6, -0.2, 0])
        tog, track, knob = toggle_switch([3.0, -0.2, 0], on=True)
        check = check_mark([3.0, -1.6, 0], scale=1.0)
        tag = tag_plate("ten seconds", [-3.4, -2.9, 0], color=BLUE)
        self.play(FadeIn(panel), FadeIn(head, shift=RIGHT * 0.2))
        self.play(FadeIn(prowl, shift=RIGHT * 0.2))
        self.play(FadeIn(lab, shift=RIGHT * 0.2), FadeIn(tog))
        self.play(knob.animate.shift(RIGHT * 0.84),
                  track.animate.set_fill(GREEN), run_time=0.8)
        self.play(Create(check))
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M08_B06FourToggles(Scene):
    def construct(self):
        apps = [
            ("Claude", "Settings > Privacy"),
            ("ChatGPT", "Settings > Data Controls"),
            ("Grok", "profile > data controls"),
            ("Gemini", "myactivity.google.com"),
        ]
        xs = [-2.6, 2.6]
        ys = [1.35, -1.35]
        cards = []
        for i, (name, path) in enumerate(apps):
            x = xs[i % 2]
            y = ys[i // 2]
            box = RoundedRectangle(corner_radius=0.2, width=4.7, height=2.2,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, y, 0])
            t = Text(name, font_size=26, color=ACCENT).move_to(
                [x, y + 0.55, 0])
            s = Text(path, font_size=14, color=INK).move_to([x, y - 0.3, 0])
            ck = check_mark([x + 1.7, y - 0.75, 0], scale=0.55)
            cards.append(VGroup(box, t, s, ck))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.25), run_time=0.6)
        cap = tag_plate("four apps, four toggles", [0, -2.9, 0], color=INK)
        self.play(FadeIn(cap, shift=UP * 0.3))
        self.wait(1.2)


class M09_B07Legal(Scene):
    def construct(self):
        cards = [
            ("NDA breach", "the AI company is an outside party"),
            ("data-protection law", "depends on your jurisdiction"),
            ("IT policy breach", "your workplace rules"),
        ]
        xs = [-4.2, 0.0, 4.2]
        for i, (w, d) in enumerate(cards):
            box = RoundedRectangle(corner_radius=0.2, width=3.7, height=2.3,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([xs[i], 0.6, 0])
            t = Text(w, font_size=22, color=ACCENT).move_to(
                [xs[i], 1.25, 0])
            s = Text(d, font_size=13, color=INK).move_to([xs[i], 0.15, 0])
            self.play(FadeIn(VGroup(box, t, s), shift=UP * 0.25),
                      run_time=0.7)
        stamp = RoundedRectangle(corner_radius=0.15, width=5.4, height=0.9,
                                 stroke_color=ACCENT, stroke_width=4,
                                 fill_opacity=0).shift(DOWN * 2.2).rotate(
                                     -0.05)
        slab = Text("a paste is enough", font_size=24, color=ACCENT).move_to(
            stamp.get_center()).rotate(-0.05)
        self.play(GrowFromCenter(stamp), FadeIn(slab, shift=DOWN * 0.2))
        note = Text("not legal advice", font_size=16, color=GREY).move_to(
            [0, -3.0, 0])
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.2)


class M10_B08CleanRoom(Scene):
    def construct(self):
        doc = RoundedRectangle(corner_radius=0.2, width=6.4, height=4.2,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK).shift(UP * 0.5)
        secrets = ["client: Acme Corp", "revenue: $4.2M", "source code v9"]
        holders = ["[CLIENT NAME]", "[REVENUE]", "[CODE]"]
        self.play(FadeIn(doc))
        for i, (sec, hold) in enumerate(zip(secrets, holders)):
            y = 1.8 - i * 1.1
            bar = Rectangle(width=4.4, height=0.55, fill_color=ACCENT,
                            fill_opacity=0.85, stroke_width=0).move_to(
                                [-0.4, y, 0])
            s = Text(sec, font_size=18, color=CARD).move_to(bar.get_center())
            self.play(FadeIn(bar), FadeIn(s), run_time=0.5)
            x1 = Line([-2.4, y + 0.28, 0], [1.6, y - 0.28, 0], color=INK,
                      stroke_width=5)
            x2 = Line([-2.4, y - 0.28, 0], [1.6, y + 0.28, 0], color=INK,
                      stroke_width=5)
            self.play(Create(x1), Create(x2), run_time=0.5)
            ph = Text(hold, font_size=18, color=BLUE).move_to([4.6, y, 0])
            arr = Arrow([2.0, y, 0], [3.4, y, 0], color=BLUE, buff=0.1)
            self.play(GrowArrow(arr), FadeIn(ph, shift=LEFT * 0.2),
                      run_time=0.5)
        tag = tag_plate("the AI still answers; the secrets stay home",
                        [0, -2.8, 0], color=INK)
        self.play(FadeIn(tag, shift=UP * 0.3))
        self.wait(1.2)


class M11_B09Enterprise(Scene):
    def construct(self):
        p = RoundedRectangle(corner_radius=0.2, width=4.8, height=3.0,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=ACCENT, stroke_width=4).move_to(
                                 [-3.0, 0.5, 0])
        pt = Text("Personal plan", font_size=26, color=ACCENT).move_to(
            [-3.0, 1.4, 0])
        ps = Text("trains by default — opt out yourself", font_size=15,
                  color=INK).move_to([-3.0, 0.3, 0])
        e = RoundedRectangle(corner_radius=0.2, width=4.8, height=3.0,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=GREEN, stroke_width=4).move_to(
                                 [3.0, 0.5, 0])
        et = Text("Team / Enterprise", font_size=24, color=GREEN).move_to(
            [3.0, 1.4, 0])
        es = Text("no training on your data, by default", font_size=15,
                  color=INK).move_to([3.0, 0.3, 0])
        arrow = Arrow([-0.3, 0.5, 0], [0.7, 0.5, 0], color=GREEN, buff=0.1)
        tag = tag_plate("make the case", [0, -2.4, 0], color=GREEN)
        self.play(FadeIn(p), FadeIn(pt), FadeIn(ps))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(e), FadeIn(et), FadeIn(es))
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
            "Samsung said yes; three leaks in twenty days.",
            "Your chats can train the model on personal plans.",
            "Opt in: kept up to five years; opting out starts now.",
            "Four apps, four toggles — flip them all.",
            "One paste can break an NDA, a law, and IT policy.",
            "Anonymize before you paste — or go enterprise.",
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
        do = RoundedRectangle(corner_radius=0.2, width=8.4, height=1.6,
                              fill_color="#EDE8DA", fill_opacity=1,
                              stroke_width=0).shift(DOWN * 2.7)
        d1 = Text("1. Settings > Privacy: flip the toggle", font_size=20,
                  color=INK).move_to([-2.4, -2.5, 0])
        d2 = Text("2. Paste the audit prompt into Claude", font_size=20,
                  color=INK).move_to([2.5, -3.0, 0])
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
