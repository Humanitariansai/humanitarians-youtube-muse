"""scenes.py — Manim visuals for "AI will fail." (why-ai-will-fail).

One Scene class per beat (14 classes). Claude-brand fidelity palette:
cream stage #F2F0E9, warm ink #3D3929, terracotta accent #D97757.
16:9 frame; all explicit coordinates inside the safe area (|x|<=6.3, |y|<=3.4).
Standard Manim API only (renders with Manim + Kokoro pipeline on Bear's Mac).

QC: python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py \
        scenes.py --class <ClassName>   # 0 warnings, 0 errors required
"""
from manim import *

# ---------------------------------------------------------------- palette --- #
CREAM = "#F2F0E9"
INK = "#3D3929"
TERRA = "#D97757"
GRAY = "#8A8578"
WHITE = "#FFFFFF"
PAPER = "#FBFAF6"

# ---------------------------------------------------------------- helpers --- #
def _bg():
    """Full-frame cream background."""
    return Rectangle(
        width=14.24, height=8.0,
        fill_color=CREAM, fill_opacity=1.0, stroke_width=0,
    ).move_to([0, 0, 0])


def _wm():
    """Channel watermark bug, lower-right, low-key."""
    return Text("@NikBearBrown", font_size=20, color=GRAY, opacity=0.55).move_to([5.25, -3.15, 0])


def _card(w, h, fill=PAPER):
    return RoundedRectangle(
        width=w, height=h, corner_radius=0.22,
        fill_color=fill, fill_opacity=1.0,
        stroke_color=INK, stroke_width=2.5,
    )


def _t(s, size, color=INK, pos=(0, 0, 0)):
    return Text(s, font_size=size, color=color).move_to(list(pos))


# ============================================================ B00 COLD OPEN == #
class SceneColdOpen(Scene):
    """The Olsen quote, typeset, then stamped WRONG."""

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        self.play(FadeIn(bg), FadeIn(_wm()))

        year = _t("1977", 110, INK, (0, 2.0, 0))
        self.play(Write(year))

        card = _card(11.5, 2.8).move_to([0, -0.9, 0])
        q1 = _t("There is no reason for any individual", 34, INK, (0, -0.35, 0))
        q2 = _t("to have a computer in his home.", 34, INK, (0, -0.95, 0))
        attr = _t("-- Ken Olsen, founder of DEC", 26, GRAY, (0, -1.55, 0))
        self.play(FadeIn(card), Write(q1), Write(q2), FadeIn(attr))

        ring = Circle(radius=1.05, stroke_color=TERRA, stroke_width=10,
                      fill_opacity=0).move_to([4.3, -0.9, 0])
        stamp = _t("WRONG", 56, TERRA, (4.3, -0.9, 0))
        self.play(GrowFromCenter(ring), FadeIn(stamp))
        self.wait(0.6)


# ============================================================== B01 OVERVIEW == #
class SceneOverview(Scene):
    """Century timeline lights up; the pattern equation assembles."""

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        self.play(FadeIn(bg), FadeIn(_wm()))

        tl = Line(start=[-5.6, -1.6, 0], end=[5.6, -1.6, 0],
                  stroke_color=INK, stroke_width=4)
        self.play(Create(tl))

        marks = [("1925", -4.6), ("1977", -2.8), ("1982", -1.0),
                 ("1995", 0.8), ("2007", 2.6), ("2008", 4.4)]
        dots = [Dot(point=[x, -1.6, 0], radius=0.12, color=TERRA)
                for _, x in marks]
        labels = [_t(y, 22, INK, (x, -2.15, 0)) for y, x in marks]
        self.play(AnimationGroup(*[GrowFromCenter(d) for d in dots], lag_ratio=0.25),
                  *[FadeIn(l) for l in labels])

        c1 = _card(3.4, 1.3).move_to([-4.2, 1.6, 0])
        t1 = _t("the expert is sure", 26, INK, (-4.2, 1.6, 0))
        plus = _t("+", 44, INK, (-2.0, 1.6, 0))
        c2 = _card(3.6, 1.3).move_to([0.2, 1.6, 0])
        t2 = _t("the future arrives", 26, INK, (0.2, 1.6, 0))
        eq = _t("=", 44, INK, (2.5, 1.6, 0))
        c3 = _card(3.2, 1.3, fill=TERRA).move_to([4.4, 1.6, 0])
        t3 = _t("wrong call", 26, WHITE, (4.4, 1.6, 0))
        self.play(FadeIn(c1), FadeIn(t1), FadeIn(plus),
                  FadeIn(c2), FadeIn(t2), FadeIn(eq),
                  FadeIn(c3), FadeIn(t3))
        self.wait(0.6)


# ============================================================ B02 THE LIST == #
class SceneTheList(Scene):
    """Four evidence cards cascade: year, expert, quote, outcome."""

    def _one_card(self, cx, cy, year, name, quote, outcome):
        card = _card(5.8, 2.2).move_to([cx, cy, 0])
        y = _t(year, 30, TERRA, (cx, cy + 0.65, 0))
        n = _t(name, 22, INK, (cx, cy + 0.25, 0))
        q = _t(quote, 20, GRAY, (cx, cy - 0.15, 0))
        o = _t(outcome, 22, TERRA, (cx, cy - 0.55, 0))
        return VGroup(card, y, n, q, o)

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        title = _t("A century of wrong calls", 46, INK, (0, 2.9, 0))
        self.play(FadeIn(bg), FadeIn(_wm()), Write(title))

        cards = [
            self._one_card(-3.2, 1.1, "1977", "Ken Olsen, DEC founder",
                           "'No home computers.'", "2B PCs. DEC gone."),
            self._one_card(3.2, 1.1, "1995", "Robert Metcalfe, Ethernet",
                           "'Internet will collapse.'", "He drank his column."),
            self._one_card(-3.2, -1.7, "2007", "Steve Ballmer, Microsoft",
                           "iPhone: 'no chance.'", "2B+ sold."),
            self._one_card(3.2, -1.7, "1998", "Paul Krugman, economist",
                           "'Internet = fax machine.'", "5.5B online."),
        ]
        for c in cards:
            self.play(FadeIn(c))
        self.wait(0.6)


# ======================================================= B03 BLOCKBUSTER == #
class SceneBlockbuster(Scene):
    """Keyes quote left; Netflix counter climbs right; Blockbuster shrinks."""

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        self.play(FadeIn(bg), FadeIn(_wm()))

        card = _card(6.4, 4.6).move_to([-3.0, 0, 0])
        head = _t("2008 -- Jim Keyes, Blockbuster CEO", 22, INK, (-3.0, 1.7, 0))
        l1 = _t("'I've been frankly confused", 24, INK, (-3.0, 0.9, 0))
        l2 = _t("by this fascination that", 24, INK, (-3.0, 0.45, 0))
        l3 = _t("everybody has with Netflix.'", 24, INK, (-3.0, 0.0, 0))
        cap = _t("streaming looked like a toy", 22, GRAY, (-3.0, -1.0, 0))
        self.play(FadeIn(card), Write(head), Write(l1), Write(l2), Write(l3),
                  FadeIn(cap))

        counter = _t("300M+", 100, TERRA, (3.2, 1.2, 0))
        clabel = _t("Netflix subscribers", 24, INK, (3.2, 0.3, 0))
        self.play(GrowFromCenter(counter), FadeIn(clabel))

        sq = Rectangle(width=1.1, height=1.1, fill_color=INK, fill_opacity=1.0,
                       stroke_width=0).move_to([3.2, -1.1, 0])
        blabel = _t("the last Blockbuster: Bend, Oregon", 20, GRAY, (3.2, -1.9, 0))
        self.play(FadeIn(sq), FadeIn(blabel))
        self.wait(0.6)

# ================================================== B04 ELLISON + VALENTI == #
class SceneEllisonValenti(Scene):
    """Two quote cards; each gets its outcome banner."""

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        self.play(FadeIn(bg), FadeIn(_wm()))

        # --- Ellison / cloud ---
        card1 = _card(6.2, 3.6).move_to([-3.2, 0.6, 0])
        h1 = _t("2008 -- Larry Ellison, Oracle CEO", 22, INK, (-3.2, 1.9, 0))
        e1 = _t("'It's complete", 22, INK, (-3.2, 1.35, 0))
        e2 = _t("gibberish. It's insane.'", 22, INK, (-3.2, 0.9, 0))
        self.play(FadeIn(card1), Write(h1), Write(e1), Write(e2))

        b1 = RoundedRectangle(width=5.8, height=1.3, corner_radius=0.2,
                              fill_color=TERRA, fill_opacity=1.0,
                              stroke_width=0).move_to([-3.2, -1.95, 0])
        b1t1 = _t("cloud: hundreds of billions/yr", 20, WHITE, (-3.2, -1.8, 0))
        b1t2 = _t("Oracle sells it now", 20, WHITE, (-3.2, -2.15, 0))
        self.play(FadeIn(b1), FadeIn(b1t1), FadeIn(b1t2))

        # --- Valenti / VCR ---
        card2 = _card(6.2, 3.6).move_to([3.2, 0.6, 0])
        h2 = _t("1982 -- Jack Valenti, Hollywood", 22, INK, (3.2, 1.9, 0))
        v1 = _t("'The VCR is to the", 22, INK, (3.2, 1.35, 0))
        v2 = _t("film producer as the", 22, INK, (3.2, 0.95, 0))
        v3 = _t("Boston strangler is to", 22, INK, (3.2, 0.55, 0))
        v4 = _t("the woman home alone.'", 22, INK, (3.2, 0.15, 0))
        self.play(FadeIn(card2), Write(h2), Write(v1), Write(v2), Write(v3), Write(v4))

        b2 = RoundedRectangle(width=5.8, height=1.3, corner_radius=0.2,
                              fill_color=TERRA, fill_opacity=1.0,
                              stroke_width=0).move_to([3.2, -1.95, 0])
        b2t = _t("home video > box office", 20, WHITE, (3.2, -1.95, 0))
        self.play(FadeIn(b2), FadeIn(b2t))
        self.wait(0.6)


# ======================================================== B05 PENICILLIN == #
class ScenePenicillin(Scene):
    """The 1941 journal page dissolves into lives saved."""

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        self.play(FadeIn(bg), FadeIn(_wm()))

        page = Rectangle(width=7.2, height=4.6, fill_color=WHITE, fill_opacity=1.0,
                         stroke_color=INK, stroke_width=2.5).move_to([-2.6, 0, 0])
        head = _t("British Medical Journal", 30, INK, (-2.6, 1.6, 0))
        yr = _t("1941", 24, GRAY, (-2.6, 1.15, 0))
        p1 = _t("'does not appear to have been", 22, INK, (-2.6, 0.5, 0))
        p2 = _t("considered as possibly useful", 22, INK, (-2.6, 0.1, 0))
        p3 = _t("from any other point of view.'", 22, INK, (-2.6, -0.3, 0))
        note = _t("on penicillin", 22, TERRA, (-2.6, -0.9, 0))
        page_group = VGroup(page, head, yr, p1, p2, p3, note)
        self.play(FadeIn(page_group), Write(head), Write(p1), Write(p2), Write(p3))

        dots = [Dot(point=[-4.9 + i * 1.4, -1.6 + j * 0.8, 0],
                    radius=0.11, color=TERRA)
                for i in range(8) for j in range(5)]
        label = _t("penicillin: hundreds of millions of lives saved", 26, INK, (0, 2.6, 0))
        self.play(FadeOut(page_group), *[FadeIn(d) for d in dots], Write(label))
        self.wait(0.6)


# ===================================================== B06 INSIDER TRAP == #
class SceneInsiderTrap(Scene):
    """The old scoreboard cannot see the new game."""

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        title = _t("The insider trap", 40, INK, (0, 2.9, 0))
        self.play(FadeIn(bg), FadeIn(_wm()), Write(title))

        # old game: bars on the incumbent's axis
        xline = Line(start=[-5.8, -1.8, 0], end=[-0.6, -1.8, 0],
                     stroke_color=INK, stroke_width=4)
        bars = [Rectangle(width=0.9, height=h, fill_color=INK, fill_opacity=0.75,
                          stroke_width=0).move_to([x, -1.8 + h / 2, 0])
                for x, h in [(-5.0, 1.0), (-3.8, 1.6), (-2.6, 2.2)]]
        blabel = _t("Blockbuster's scoreboard: stores", 22, INK, (-3.2, -2.5, 0))
        self.play(Create(xline), *[FadeIn(b) for b in bars], FadeIn(blabel))

        # new game: its own curve on its own axis
        pts = [(0.2, -1.6), (1.4, -1.5), (2.6, -1.1), (3.8, -0.3), (5.0, 1.0)]
        segs = [Line(start=[*a, 0], end=[*b, 0], stroke_color=TERRA, stroke_width=6)
                for a, b in zip(pts, pts[1:])]
        nlabel = _t("Netflix: a different game", 22, TERRA, (3.0, 1.8, 0))
        self.play(AnimationGroup(*[Create(s) for s in segs], lag_ratio=0.3),
                  FadeIn(nlabel))

        dashed = DashedLine(start=[-1.4, 0.4, 0], end=[1.2, -1.2, 0], color=GRAY)
        q = _t("?", 60, GRAY, (0.1, -0.5, 0))
        cap = _t("the old scoreboard can't see it", 22, GRAY, (0.2, -2.5, 0))
        self.play(Create(dashed), FadeIn(q), FadeIn(cap))
        self.wait(0.6)


# ========================================================= B07 TOY CURVE == #
class SceneToyCurve(Scene):
    """Snapshot vs trajectory: the curve that bends upward."""

    def construct(self):
        import math
        self.camera.background_color = CREAM
        bg = _bg()
        self.play(FadeIn(bg), FadeIn(_wm()))

        xax = Line(start=[-5.8, -2.4, 0], end=[5.8, -2.4, 0],
                   stroke_color=INK, stroke_width=3)
        yax = Line(start=[-5.8, -2.4, 0], end=[-5.8, 2.4, 0],
                   stroke_color=INK, stroke_width=3)
        xl = _t("time", 22, GRAY, (5.3, -2.85, 0))
        yl = _t("quality", 22, GRAY, (-6.0, 2.0, 0))
        self.play(Create(xax), Create(yax), FadeIn(xl), FadeIn(yl))

        def q(x):
            return -2.0 + 4.2 / (1.0 + math.exp(-1.1 * (x - 0.6)))

        xs = [-5.2 + i * 0.8 for i in range(14)]
        segs = [Line(start=[a, q(a), 0], end=[b, q(b), 0],
                     stroke_color=INK, stroke_width=5)
                for a, b in zip(xs, xs[1:])]
        self.play(AnimationGroup(*[Create(s) for s in segs], lag_ratio=0.15))

        pins = [Dot(point=[x, q(x), 0], radius=0.12, color=TERRA)
                for x in (-4.4, -3.6, -2.8)]
        pin_labels = [_t(s, 20, GRAY, (x, q(x) + 0.45, 0))
                      for s, x in [("pixel soup", -4.4), ("buffering", -3.6),
                                   ("'will fail'", -2.8)]]
        self.play(*[FadeIn(p) for p in pins], *[FadeIn(l) for l in pin_labels])

        arrow = Arrow(start=[0.8, -0.4, 0], end=[4.6, 1.9, 0],
                      color=TERRA, stroke_width=8)
        alabel = _t("trajectory", 26, TERRA, (3.4, 2.5, 0))
        self.play(GrowArrow(arrow), FadeIn(alabel))
        self.wait(0.6)

# ===================================================== B08 FAMILIAR FORM == #
class SceneFamiliarForm(Scene):
    """THEN cards wired to their NOW twins."""

    def _pair_card(self, cx, cy, l1, l2, l3=None):
        card = _card(5.6, 1.9).move_to([cx, cy, 0])
        t1 = _t(l1, 22, INK, (cx, cy + 0.45, 0))
        t2 = _t(l2, 22, INK, (cx, cy + 0.0, 0))
        parts = [card, t1, t2]
        if l3:
            t3 = _t(l3, 20, GRAY, (cx, cy - 0.45, 0))
            parts.append(t3)
        return VGroup(*parts)

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        h1 = _t("THEN", 36, INK, (-3.4, 2.7, 0))
        h2 = _t("NOW", 36, INK, (3.4, 2.7, 0))
        self.play(FadeIn(bg), FadeIn(_wm()), Write(h1), Write(h2))

        t1 = self._pair_card(-3.4, 1.3, "streaming: pixel soup", "buffering wheel", "(2007)")
        t2 = self._pair_card(-3.4, -1.2, "computers everywhere,", "not in the statistics", "(Solow, 1987)")
        self.play(FadeIn(t1), FadeIn(t2))

        a1 = Arrow(start=[-0.4, 1.3, 0], end=[0.4, 1.3, 0],
                   color=TERRA, stroke_width=6)
        a2 = Arrow(start=[-0.4, -1.2, 0], end=[0.4, -1.2, 0],
                   color=TERRA, stroke_width=6)
        self.play(GrowArrow(a1), GrowArrow(a2))

        n1 = self._pair_card(3.4, 1.3, "'AI hallucinates'", "invented cases, 6 fingers")
        n2 = self._pair_card(3.4, -1.2, "AI: +0.5% productivity", "in a decade", "(Acemoglu, 2024)")
        self.play(FadeIn(n1), FadeIn(n2))
        self.wait(0.6)


# ======================================================= B09 HONEST PART == #
class SceneHonestPart(Scene):
    """A frozen snapshot vs the moving trajectory."""

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        self.play(FadeIn(bg), FadeIn(_wm()))

        frame = Rectangle(width=5.4, height=3.4, stroke_color=INK,
                          stroke_width=3, fill_opacity=0).move_to([-3.3, 0, 0])
        fdot = Dot(point=[-3.3, -0.6, 0], radius=0.14, color=INK)
        cap1 = _t("snapshot: AI today, flawed", 22, INK, (-3.3, 2.15, 0))
        self.play(FadeIn(frame), FadeIn(fdot), FadeIn(cap1))

        strip_cells = []
        for i, cx in enumerate([1.5, 3.35, 5.2]):
            cell = Rectangle(width=1.7, height=3.4, stroke_color=INK,
                             stroke_width=2.5, fill_opacity=0).move_to([cx, 0, 0])
            y0 = -1.0 + i * 0.7
            mini = Line(start=[cx - 0.6, y0, 0], end=[cx + 0.6, y0 + 0.9, 0],
                        stroke_color=TERRA, stroke_width=5)
            strip_cells.append(VGroup(cell, mini))
        cap2 = _t("trajectory: where it's heading", 22, TERRA, (3.35, 2.15, 0))
        strip = VGroup(*strip_cells)
        self.play(*[FadeIn(c) for c in strip_cells], FadeIn(cap2))

        ring = SurroundingRectangle(strip, color=TERRA, stroke_width=6, buff=0.15)
        verdict = _t("bet on this", 26, TERRA, (3.35, -2.35, 0))
        self.play(Create(ring), FadeIn(verdict))
        self.wait(0.6)


# ================================================== B10 ASYMMETRIC BET == #
class SceneAsymmetricBet(Scene):
    """The 2x2 payoff matrix: three of four futures reward learning."""

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        title = _t("Run the bet both ways", 40, INK, (0, 2.9, 0))
        self.play(FadeIn(bg), FadeIn(_wm()), Write(title))

        cells = [
            ((-3.1, 0.95), "AI matters, you learned", "you are ready"),
            ((3.1, 0.95), "AI matters, you waited", "you're catching up"),
            ((-3.1, -1.45), "AI is hype, you learned", "lost hours, gained skill"),
            ((3.1, -1.45), "AI is hype, you ignored it", "saved a few hours"),
        ]
        groups = []
        for (cx, cy), cond, out in cells:
            rect = _card(6.0, 2.2).move_to([cx, cy, 0])
            c = _t(cond, 20, GRAY, (cx, cy + 0.45, 0))
            o = _t(out, 24, INK, (cx, cy - 0.25, 0))
            groups.append(VGroup(rect, c, o))
        self.play(*[FadeIn(g) for g in groups])

        checks = [_t("\u2713", 40, TERRA, (cx + 2.45, cy + 0.7, 0))
                  for (cx, cy), _, _ in cells[:3]]
        self.play(*[FadeIn(ch) for ch in checks])

        banner = _t("Learning is cheap. Dismissing is expensive.", 28, TERRA, (0, -2.95, 0))
        self.play(FadeIn(banner))
        self.wait(0.6)


# =========================================================== B11 VERDICT == #
class SceneVerdict(Scene):
    """Four takeaways check off in sequence."""

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        title = _t("The verdict", 48, INK, (0, 2.8, 0))
        self.play(FadeIn(bg), FadeIn(_wm()), Write(title))

        lines = [
            "1. A century of confident wrong calls",
            "2. The insider trap: the new judged by the old",
            "3. Judge the trajectory, not the snapshot",
            "4. Learning is cheap; dismissing is expensive",
        ]
        ys = [1.7, 0.7, -0.3, -1.3]
        for line, y in zip(lines, ys):
            dot = Dot(point=[-5.9, y, 0], radius=0.12, color=TERRA)
            t = _t(line, 28, INK, (0.2, y, 0))
            self.play(GrowFromCenter(dot), FadeIn(t))
        self.wait(0.6)


# ========================================================= B12 YOUR TURN == #
class SceneYourTurn(Scene):
    """The handoff prompt types itself onto a card."""

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        card = _card(12.2, 5.2, fill=WHITE).move_to([0, -0.2, 0])
        head = _t("Your turn -- try it yourself", 34, INK, (0, 2.0, 0))
        self.play(FadeIn(bg), FadeIn(_wm()), FadeIn(card), Write(head))

        prompt = [
            "Find the five most common reasons people say AI will fail.",
            "For each: the strongest argument,",
            "the past technology it most resembles,",
            "and what would prove it right or wrong.",
            "Be a fair referee.",
        ]
        cursor = Rectangle(width=0.09, height=0.42, fill_color=TERRA,
                           fill_opacity=1.0, stroke_width=0)
        for i, s in enumerate(prompt):
            y = 1.2 - i * 0.5
            line = _t(s, 24, INK, (0, y, 0))
            self.play(Write(line), FadeIn(cursor.move_to([-5.75, y, 0])))

        footer = _t("paste this into Claude...", 24, GRAY, (0, -2.9, 0))
        self.play(FadeOut(cursor), FadeIn(footer))
        self.wait(0.6)


# ============================================================= B13 OUTRO == #
class SceneOutro(Scene):
    """Title restate, poster-style, with the @NikBearBrown handle."""

    def construct(self):
        self.camera.background_color = CREAM
        bg = _bg()
        self.play(FadeIn(bg), FadeIn(_wm()))

        t1 = Text("AI will fail", font_size=96, color=INK)
        t2 = Text(".", font_size=96, color=TERRA).next_to(t1, RIGHT, buff=0.05)
        title = VGroup(t1, t2).move_to([0, 0.6, 0])
        self.play(Write(t1), FadeIn(t2))

        rule = Line(start=[-3, -0.9, 0], end=[3, -0.9, 0],
                    stroke_color=TERRA, stroke_width=4)
        handle = _t("@NikBearBrown", 40, INK, (0, -1.7, 0))
        self.play(Create(rule), FadeIn(handle))
        self.wait(0.8)
