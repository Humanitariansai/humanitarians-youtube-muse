"""scenes.py — Pictures from Words (How to AI, film 19).

12 Manim scenes, M01–M12. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), each scene carries distinct non-text shapes that evolve
across play() calls, every on-screen text is read aloud in its beat.
All "generated pictures" are drawn placeholders — no real AI images.
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
WARM = "#C97B3D"


def tag_plate(text, pos, color=INK, bg=CARD, font_size=20):
    plate = RoundedRectangle(corner_radius=0.15,
                             width=len(text) * 0.22 + 0.8,
                             height=0.7, fill_color=bg, fill_opacity=1,
                             stroke_color=color)
    t = Text(text, font_size=font_size, color=color)
    g = VGroup(plate, t).move_to(pos)
    return g


def dog_silhouette(pos, color=GREY, scale=1.0):
    """Deliberately simple drawn dog: body, head, four legs, tail."""
    body = Ellipse(width=2.2, height=1.2, fill_color=color, fill_opacity=1,
                   stroke_width=0)
    head = Circle(radius=0.55, fill_color=color, fill_opacity=1,
                  stroke_width=0).move_to([1.25, 0.55, 0])
    legs = VGroup(*[
        Rectangle(width=0.28, height=0.7, fill_color=color, fill_opacity=1,
                  stroke_width=0).move_to([x, -0.85, 0])
        for x in (-0.7, -0.25, 0.35, 0.8)
    ])
    tail = Line([-1.1, 0.2, 0], [-1.7, 0.8, 0], color=color, stroke_width=12)
    return VGroup(body, head, legs, tail).scale(scale).move_to(pos)


def picture_frame(pos, width=6.4, height=3.8):
    return Rectangle(width=width, height=height, stroke_color=INK,
                     stroke_width=3, fill_opacity=0).move_to(pos)


class M01_Bidea(Scene):
    def construct(self):
        prompt_box = RoundedRectangle(corner_radius=0.2, width=9.6, height=1.3,
                                     stroke_color=INK, stroke_width=3,
                                     fill_color=CARD, fill_opacity=1
                                     ).move_to([0, 2.2, 0])
        prompt_text = Text("describe a picture in words",
                           font_size=30, color=INK).move_to([0, 2.2, 0])
        frame = picture_frame([0, -0.9, 0], width=6.8, height=3.6)
        sun = Circle(radius=0.5, fill_color=ACCENT, fill_opacity=1,
                     stroke_width=0).move_to([-1.8, 0.0, 0])
        mountains = VGroup(
            Polygon([-3.0, -2.2, 0], [-1.4, -0.4, 0], [0.2, -2.2, 0],
                    fill_color=GREY, fill_opacity=0.35, stroke_width=0),
            Polygon([-0.6, -2.2, 0], [1.0, -0.8, 0], [2.6, -2.2, 0],
                    fill_color=GREY, fill_opacity=0.35, stroke_width=0),
        )
        self.play(Create(prompt_box))
        self.play(Write(prompt_text), run_time=1.0)
        self.play(Create(frame))
        self.play(GrowFromCenter(sun), run_time=0.7)
        self.play(Create(mountains), run_time=0.9)
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        words = ["image generator", "prompt", "style", "iterate"]
        defs = ["turns words into pictures", "the sentence you type",
                "photo, watercolor, cartoon", "tweak the words, try again"]
        cards = VGroup()
        for i, (w, d) in enumerate(zip(words, defs)):
            x = -5.4 + i * 3.6
            box = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.4,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK).move_to([x, 0, 0])
            t = Text(w, font_size=24, color=ACCENT).move_to([x, 0.55, 0])
            s = Text(d, font_size=14, color=INK).move_to([x, -0.35, 0])
            cards.add(VGroup(box, t, s))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M03_B01Vague(Scene):
    def construct(self):
        pcard = RoundedRectangle(corner_radius=0.2, width=4.4, height=1.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).move_to([-3.9, 1.7, 0])
        ptext = Text('"a dog"', font_size=34, color=INK).move_to([-3.9, 1.7, 0])
        arrow = Arrow(start=[-1.4, 1.7, 0], end=[0.9, 1.7, 0],
                      color=INK, stroke_width=6, buff=0.1)
        frame = picture_frame([3.2, 0.1, 0], width=4.8, height=3.6)
        dog = dog_silhouette([3.2, 0.1, 0], color=GREY)
        caption = Text("vague words in → vague picture out", font_size=22,
                       color=GREY).move_to([0, -2.9, 0])
        self.play(Create(pcard))
        self.play(FadeIn(ptext))
        self.play(Create(arrow), run_time=0.6)
        self.play(Create(frame))
        self.play(GrowFromCenter(dog), run_time=0.9)
        self.play(FadeIn(caption, shift=UP * 0.2))
        self.wait(1.2)


class M04_B02Specific(Scene):
    def construct(self):
        pcard = RoundedRectangle(corner_radius=0.2, width=6.2, height=2.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).move_to([-2.9, 1.85, 0])
        lines = VGroup(
            Text("a sleepy puppy,", font_size=20, color=INK),
            Text("watercolor painting,", font_size=20, color=INK),
            Text("warm cozy morning light", font_size=20, color=INK),
        ).arrange(DOWN, buff=0.18).move_to([-2.9, 1.85, 0])
        chip1 = tag_plate("SUBJECT · puppy", [-2.9, 0.2, 0], color=ACCENT)
        chip2 = tag_plate("STYLE · watercolor", [-2.9, -0.6, 0], color=ACCENT)
        chip3 = tag_plate("MOOD · warm cozy light", [-2.9, -1.4, 0],
                          color=ACCENT)
        frame = picture_frame([3.3, 0.2, 0], width=5.0, height=4.4)
        sun = Circle(radius=0.6, fill_color=ACCENT, fill_opacity=1,
                     stroke_width=0).move_to([4.6, 1.2, 0])
        wash = VGroup(
            Circle(radius=0.9, fill_color=BLUE, fill_opacity=0.25,
                   stroke_width=0).move_to([2.4, -0.6, 0]),
            Circle(radius=0.7, fill_color=GREEN, fill_opacity=0.25,
                   stroke_width=0).move_to([4.2, -0.9, 0]),
        )
        dog = dog_silhouette([3.0, -0.2, 0], color=WARM, scale=0.9)
        self.play(Create(pcard))
        self.play(FadeIn(lines))
        self.play(FadeIn(chip1, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(chip2, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(chip3, shift=RIGHT * 0.3), run_time=0.6)
        self.play(Create(frame))
        self.play(GrowFromCenter(sun), run_time=0.6)
        self.play(FadeIn(wash), run_time=0.6)
        self.play(GrowFromCenter(dog), run_time=0.8)
        self.wait(1.2)


class M05_B03Iterate(Scene):
    def construct(self):
        frame = picture_frame([0, 0.2, 0], width=5.6, height=3.6)
        dog = dog_silhouette([-1.2, -0.2, 0], color=WARM, scale=0.85)
        sun = Circle(radius=0.5, fill_color=ACCENT, fill_opacity=1,
                     stroke_width=0).move_to([1.6, 1.1, 0])
        lab1 = tag_plate("warmer light", [-3.9, 2.5, 0], color=ACCENT)
        arr1 = Arrow(start=[-2.6, 2.3, 0], end=[1.0, 1.4, 0],
                     color=ACCENT, stroke_width=5, buff=0.15)
        sun_warm = Circle(radius=0.85, fill_color=ACCENT, fill_opacity=1,
                          stroke_width=0).move_to([1.6, 1.1, 0])
        lab2 = tag_plate("wider shot", [3.9, 2.5, 0], color=BLUE)
        frame_wide = picture_frame([0, 0.2, 0], width=6.8, height=3.6)
        caption = Text("keep what works, fix one thing", font_size=22,
                       color=GREY).move_to([0, -2.9, 0])
        self.play(Create(frame))
        self.play(FadeIn(dog), run_time=0.7)
        self.play(FadeIn(sun), run_time=0.6)
        self.play(FadeIn(lab1, shift=DOWN * 0.2), run_time=0.6)
        self.play(Create(arr1), run_time=0.6)
        self.play(Transform(sun, sun_warm), run_time=0.8)
        self.play(FadeIn(lab2, shift=DOWN * 0.2), run_time=0.6)
        self.play(Transform(frame, frame_wide), run_time=0.8)
        self.play(FadeIn(caption, shift=UP * 0.2))
        self.wait(1.2)


class M06_B04Recipe(Scene):
    def construct(self):
        labels = ["SUBJECT", "SETTING", "STYLE", "LIGHTING", "MOOD"]
        values = ["a puppy", "a kitchen", "watercolor", "morning sun", "cozy"]
        rows = VGroup()
        for i, (lab, val) in enumerate(zip(labels, values)):
            y = 1.8 - i * 0.95
            plate = RoundedRectangle(corner_radius=0.12, width=2.7, height=0.8,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=ACCENT).move_to([-4.2, y, 0])
            lt = Text(lab, font_size=20, color=ACCENT).move_to([-4.2, y, 0])
            vt = Text(val, font_size=24, color=INK).move_to([-0.2, y, 0])
            rows.add(VGroup(plate, lt, vt))
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(1.2)


class M07_B05HowItWorks(Scene):
    def construct(self):
        pcard = RoundedRectangle(corner_radius=0.2, width=7.4, height=1.1,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK).move_to([-2.2, 2.5, 0])
        ptext = Text("a dog, watercolor, warm light", font_size=20,
                     color=INK).move_to([-2.2, 2.5, 0])
        arrow = Arrow(start=[-2.2, 1.9, 0], end=[-2.2, 1.2, 0],
                      color=INK, stroke_width=6, buff=0.1)
        panels, contents, labels = VGroup(), VGroup(), VGroup()
        xs = [-4.3, 0.0, 4.3]
        names = ["static", "sharper", "picture"]
        for x, name in zip(xs, names):
            panel = RoundedRectangle(corner_radius=0.15, width=3.4, height=2.6,
                                     stroke_color=INK, stroke_width=3,
                                     fill_opacity=0).move_to([x, -0.9, 0])
            lab = Text(name, font_size=20, color=GREY).move_to([x, -2.55, 0])
            panels.add(panel)
            labels.add(lab)
        dots = VGroup(*[
            Dot(point=[-4.3 + (c - 1.5) * 0.55, -0.9 + (r - 1.5) * 0.55, 0],
                radius=0.09, color=GREY)
            for r in range(4) for c in range(4)
        ])
        rough = VGroup(
            Line([-1.0, -1.3, 0], [-0.2, -0.5, 0], color=INK, stroke_width=4),
            Line([-0.2, -0.5, 0], [0.8, -1.3, 0], color=INK, stroke_width=4),
            Circle(radius=0.4, stroke_color=INK, stroke_width=4,
                   fill_opacity=0).move_to([0.9, -0.2, 0]),
        )
        final = VGroup(
            dog_silhouette([4.0, -1.1, 0], color=WARM, scale=0.55),
            Circle(radius=0.35, fill_color=ACCENT, fill_opacity=1,
                   stroke_width=0).move_to([5.0, 0.0, 0]),
        )
        self.play(Create(pcard))
        self.play(FadeIn(ptext))
        self.play(Create(arrow), run_time=0.5)
        self.play(Create(panels[0]))
        self.play(FadeIn(dots), run_time=0.7)
        self.play(FadeIn(labels[0], shift=UP * 0.2), run_time=0.5)
        self.play(Create(panels[1]))
        self.play(Create(rough), run_time=0.8)
        self.play(FadeIn(labels[1], shift=UP * 0.2), run_time=0.5)
        self.play(Create(panels[2]))
        self.play(FadeIn(final), run_time=0.8)
        self.play(FadeIn(labels[2], shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)


class M08_B06Uses(Scene):
    def construct(self):
        specs = [
            ("slides", [-3.1, 1.3, 0]),
            ("invitation", [3.1, 1.3, 0]),
            ("garden mockup", [-3.1, -1.3, 0]),
            ("an idea", [3.1, -1.3, 0]),
        ]
        cards = VGroup()
        for name, pos in specs:
            card = RoundedRectangle(corner_radius=0.2, width=5.4, height=2.2,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK).move_to(pos)
            if name == "slides":
                icon = Rectangle(width=1.1, height=0.8, stroke_color=BLUE,
                                 stroke_width=4, fill_opacity=0
                                 ).move_to([pos[0] - 1.6, pos[1], 0])
            elif name == "invitation":
                icon = VGroup(
                    RoundedRectangle(corner_radius=0.1, width=1.1, height=0.9,
                                     stroke_color=ACCENT, stroke_width=4,
                                     fill_opacity=0),
                    Circle(radius=0.18, fill_color=ACCENT, fill_opacity=1,
                           stroke_width=0),
                ).move_to([pos[0] - 1.6, pos[1], 0])
            elif name == "garden mockup":
                icon = VGroup(
                    Triangle(fill_color=GREEN, fill_opacity=0.6,
                             stroke_width=0).scale(0.55
                                                 ).move_to([0, 0.25, 0]),
                    Rectangle(width=0.9, height=0.35, fill_color=WARM,
                              fill_opacity=1, stroke_width=0
                              ).move_to([0, -0.45, 0]),
                ).move_to([pos[0] - 1.6, pos[1], 0])
            else:
                icon = VGroup(
                    Circle(radius=0.4, stroke_color=ACCENT, stroke_width=5,
                           fill_opacity=0),
                    Line([0, -0.55, 0], [0, -0.85, 0], color=ACCENT,
                         stroke_width=5),
                ).move_to([pos[0] - 1.6, pos[1], 0])
            lab = Text(name, font_size=22, color=INK
                       ).move_to([pos[0] + 0.7, pos[1], 0])
            cards.add(VGroup(card, icon, lab))
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)


class M09_B07TextLimit(Scene):
    def construct(self):
        sign = RoundedRectangle(corner_radius=0.2, width=8.4, height=2.2,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to([0, 0.7, 0])
        garbled = Text("HAPPPY BIRTHDAAY", font_size=44, color=ACCENT
                       ).move_to([0, 0.7, 0])
        magnifier = Circle(radius=1.15, stroke_color=ACCENT, stroke_width=6,
                           fill_opacity=0).move_to([2.2, 0.7, 0])
        tag = tag_plate("read it before you share it", [0, -1.9, 0],
                        color=ACCENT)
        self.play(Create(sign))
        self.play(FadeIn(garbled), run_time=0.8)
        self.play(Create(magnifier), run_time=0.7)
        self.play(FadeIn(tag, shift=UP * 0.2))
        self.wait(1.2)


class M10_B08HandsLimit(Scene):
    def construct(self):
        frame = picture_frame([-1.4, 0.1, 0], width=5.2, height=4.0)
        palm = RoundedRectangle(corner_radius=0.3, width=1.7, height=1.9,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK).move_to([-1.4, -0.5, 0])
        fingers = VGroup(*[
            Rectangle(width=0.32, height=0.9, fill_color=CARD, fill_opacity=1,
                      stroke_color=INK).move_to([-1.4 + off, 0.85, 0])
            for off in (-0.7, -0.42, -0.14, 0.14, 0.42, 0.7)
        ])
        magnifier = Circle(radius=1.3, stroke_color=ACCENT, stroke_width=6,
                           fill_opacity=0).move_to([-1.4, 0.85, 0])
        tag = tag_plate("zoom in before you share", [3.3, -2.4, 0],
                        color=ACCENT)
        self.play(Create(frame))
        self.play(FadeIn(palm), run_time=0.6)
        self.play(FadeIn(fingers), run_time=0.7)
        self.play(Create(magnifier), run_time=0.7)
        self.play(FadeIn(tag, shift=UP * 0.2))
        self.wait(1.2)


class M11_B09Disclose(Scene):
    def construct(self):
        frame = picture_frame([0, 0.4, 0], width=6.4, height=3.8)
        sun = Circle(radius=0.55, fill_color=ACCENT, fill_opacity=1,
                     stroke_width=0).move_to([-1.9, 1.3, 0])
        mountains = Polygon([-2.6, -1.1, 0], [-0.9, 0.5, 0], [0.8, -1.1, 0],
                             fill_color=GREY, fill_opacity=0.35,
                             stroke_width=0)
        stamp = RoundedRectangle(corner_radius=0.15, width=3.6, height=1.3,
                                 fill_color=ACCENT, fill_opacity=1,
                                 stroke_width=0).move_to([0.6, 0.3, 0])
        stamp_text = Text("AI-MADE", font_size=34, color=CARD
                          ).move_to([0.6, 0.3, 0])
        stamp_g = VGroup(stamp, stamp_text)
        caption = Text("say it's AI-made", font_size=24, color=GREY
                       ).move_to([0, -2.5, 0])
        self.play(Create(frame))
        self.play(GrowFromCenter(sun), run_time=0.6)
        self.play(Create(mountains), run_time=0.7)
        self.play(FadeIn(stamp_g, shift=DOWN * 0.5), run_time=0.7)
        self.play(FadeIn(caption, shift=UP * 0.2))
        self.wait(1.2)


class M12_BvdtHtfOut(Scene):
    def construct(self):
        recap_data = [
            ("Act 1 · the ladder",
             "vague words in → subject, style, mood → iterate", 1.9),
            ("Act 2 · the uses",
             "slides, invitations, mockups, drafts", 0.0),
            ("Act 3 · the limits",
             "check the text, check the hands, say it's AI-made", -1.9),
        ]
        recap_mobs = []
        for title, detail, y in recap_data:
            plate = RoundedRectangle(corner_radius=0.15, width=10.6, height=1.5,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK).move_to([0, y, 0])
            t = Text(title, font_size=24, color=ACCENT).move_to([0, y + 0.32, 0])
            d = Text(detail, font_size=16, color=INK).move_to([0, y - 0.35, 0])
            g = VGroup(plate, t, d)
            recap_mobs.append(g)
            self.play(FadeIn(g, shift=UP * 0.2), run_time=0.6)
        self.wait(0.6)
        self.play(FadeOut(VGroup(*recap_mobs)), run_time=0.6)

        do_card = RoundedRectangle(corner_radius=0.2, width=10.6, height=3.2,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=ACCENT).move_to([0, 0, 0])
        do_lines = VGroup(
            Text("1 · type a vague prompt", font_size=22, color=INK),
            Text("2 · rewrite it with the 5-slot recipe", font_size=22,
                 color=INK),
            Text("3 · compare the two pictures", font_size=22, color=INK),
        ).arrange(DOWN, buff=0.3).move_to([0, 0, 0])
        self.play(Create(do_card))
        self.play(FadeIn(do_lines), run_time=0.8)
        self.wait(0.8)
        self.play(FadeOut(VGroup(do_card, do_lines)), run_time=0.6)

        title = Text("Pictures from Words", font_size=64, color=INK
                     ).move_to([-0.2, 0.6, 0])
        period = Text(".", font_size=64, color=ACCENT)
        period.next_to(title, RIGHT, buff=0.05)
        handle = Text("@NikBearBrown", font_size=28, color=GREY
                      ).move_to([0, -1.3, 0])
        self.play(FadeIn(title), run_time=0.8)
        self.play(FadeIn(period), run_time=0.4)
        self.play(FadeIn(handle, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)
