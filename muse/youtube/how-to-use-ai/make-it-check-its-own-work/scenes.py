"""scenes.py — "Make It Check Its Own Work." (show-tell).

9 Manim scenes, B00-B08, one drawing per beat. House palette (cream stage,
warm ink, terracotta accents); iso_kit pasted at top (Gate A copies only
scenes.py). Each scene adds new non-text shapes via Create/FadeIn/
GrowFromCenter (never via .animate() alone); labels sit beside objects;
coords within +-6.2 x +-3.3 y.
"""

"""
iso_kit.py — the show-tell drawing kit. PASTE this block at the top of a reel's scenes.py;
do not import it (Gate A copies only scenes.py into its sandbox).

Drawn isometric objects in the Claude palette: cardboard boxes (closed, open, taped), dark
MCP blocks with ports, flat skill pages, server stacks with lights, checks, a cursor, pills.
Pacing helpers read the reel's beat_sheet.json so scenes wait for their spoken phrase.

Every rule in ../SKILL.md "DRAWING LAWS" is already obeyed by these primitives; keep it that
way when you add one (label beside, never inside; terracotta never under text; dim greys
with gaps for chart blocks; type floor 32).
"""
from manim import *
import numpy as np
import json as _json, os as _os

# ═════════════════════════════ ISO KIT (show-tell) ═════════════════════════════
STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; CARD = "#FAF9F5"
BOX_TOP, BOX_L, BOX_R = "#F3E9D8", "#DCC9AA", "#C7AE86"          # kraft cardboard: top, left face, right face (deep enough for Gate V contrast)
BOX_IN1, BOX_IN2, BOX_FLOOR = "#CDB894", "#BFA67E", "#B39A72"     # inside walls + floor
DARK_TOP, DARK_L, DARK_R = "#3A3530", "#26221F", "#1E1B18"        # MCP / server blocks
PAGE_TOP, PAGE_L, PAGE_R = "#FFFFFF", "#ECE7DF", "#E2DCD2"         # skill pages
BAR1, BAR2, BAR3 = "#8B8F96", "#B4AFA6", "#D9D4C7"                # chart segments, dim to ghost
SERIF = "EB Garamond"
C30 = 0.8660254
config.background_color = STAGE


def T(s, size=36, color=INK, bold=False):
    return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")


class Iso:
    """Isometric projection: x runs right-up, y runs left-up, z runs up. (ox, oy) is where (0,0,0) lands."""
    def __init__(self, ox=0.0, oy=0.0, s=1.0):
        self.ox, self.oy, self.s = ox, oy, s

    def p(self, x, y, z=0.0):
        return np.array([self.ox + (x - y) * C30 * self.s, self.oy + (x + y) * 0.5 * self.s + z * self.s, 0.0])

    def v(self, dx, dy, dz=0.0):
        return self.p(dx, dy, dz) - self.p(0, 0, 0)

    def quad(self, pts, fill, stroke=INK, sw=4):
        return Polygon(*[self.p(*q) for q in pts], fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)

    def box(self, x0, y0, z0, w, d, h, top=BOX_TOP, left=BOX_L, right=BOX_R, sw=4):
        """Closed box: the two front faces (x = x0 and y = y0) plus the top."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        return VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], left, sw=sw),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], right, sw=sw),
            self.quad([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top, sw=sw))

    def open_box(self, x0, y0, z0, w, d, h):
        """(back, front): floor + inner back walls, then the front walls. Put contents between them."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        back = VGroup(
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], BOX_FLOOR),
            self.quad([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], BOX_IN1),
            self.quad([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], BOX_IN2))
        front = VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], BOX_L),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], BOX_R))
        back.set_z_index(0); front.set_z_index(2)
        return back, front

    def tape(self, x0, y0, z1, w, d, drop=0.35, t=0.22):
        """Terracotta tape across the top (along x) and down the left front face."""
        ym = y0 + d / 2
        return VGroup(
            self.quad([(x0, ym - t, z1), (x0 + w, ym - t, z1), (x0 + w, ym + t, z1), (x0, ym + t, z1)], TERRA, sw=0),
            self.quad([(x0, ym - t, z1), (x0, ym + t, z1), (x0, ym + t, z1 - drop), (x0, ym - t, z1 - drop)], TERRA, sw=0))

    def mcp(self, x0, y0, z0, w=1.3, d=1.3, h=0.7):
        """Dark MCP block with two light ports on its right front face."""
        body = self.box(x0, y0, z0, w, d, h, DARK_TOP, DARK_L, DARK_R)
        ports = VGroup(*[self.box(x0 + w * f, y0 - 0.18, z0 + h * 0.3, w * 0.16, 0.18, h * 0.3, GHOST, BOX_IN1, BOX_IN2, sw=1)
                         for f in (0.22, 0.58)])
        return VGroup(body, ports)

    def page(self, x0, y0, z0, w=1.1, d=1.4):
        """A skill page lying flat: white slab, three ghost text lines, one terracotta dot."""
        slab = self.box(x0, y0, z0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        zt = z0 + 0.06
        lines = VGroup(*[Line(self.p(x0 + 0.2, y0 + d * f, zt), self.p(x0 + w - 0.2, y0 + d * f, zt), color=GHOST, stroke_width=4)
                         for f in (0.3, 0.5, 0.7)])
        dot = Dot(self.p(x0 + 0.2, y0 + d * 0.86, zt), radius=0.06, color=TERRA)
        return VGroup(slab, lines, dot)

    def server(self, x0, y0, z0, w=1.4, d=1.4, slab=0.42, n=3):
        """A stack of dark server slabs; returns (stack, lights) — lights start ghost, turn terracotta."""
        stack = VGroup(*[self.box(x0, y0, z0 + i * (slab + 0.04), w, d, slab, DARK_TOP, DARK_L, DARK_R) for i in range(n)])
        lights = VGroup(*[Dot(self.p(x0 + 0.25, y0, z0 + i * (slab + 0.04) + slab / 2), radius=0.06, color=GHOST) for i in range(n)])
        return stack, lights


def ease_in(t):
    """Quadratic ease-in (things dropping into a box). Local: Gate A's stub has no ease_in_quad."""
    return t * t


def check(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.75, 0], color=color, stroke_width=w),
                  Line([x - s * 0.3, y - s * 0.75, 0], [x + s * 1.1, y + s * 0.85, 0], color=color, stroke_width=w))


def cursor(x, y, s=0.45):
    return Polygon([x, y, 0], [x, y - s, 0], [x + s * 0.28, y - s * 0.72, 0], [x + s * 0.62, y - s * 0.66, 0],
                   fill_color=INK, fill_opacity=1, stroke_color=CARD, stroke_width=2)


def pill(x, y, w, h=0.62, fill="#FFFFFF"):
    return RoundedRectangle(width=w, height=h, corner_radius=h / 2, fill_color=fill, fill_opacity=1, stroke_width=0).move_to([x, y, 0])


# ═════════════════════════════ pacing (narration is the clock) ═════════════════════════════
try:
    _SHEET = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}


def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0


def until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its character share of the narration × the measured audio)."""
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)


# ═════════════════════════════ film helpers ═════════════════════════════

def lab(s, x, y, size=34, color=INK, bold=False):
    return T(s, size=size, color=color, bold=bold).move_to([x, y, 0])


def chat_window(x, y, w=7.2, h=4.6, title="Claude"):
    """Pale UI panel with a dark title bar (carries the contrast)."""
    g = VGroup()
    g.add(RoundedRectangle(width=w, height=h, corner_radius=0.18,
                           fill_color=CARD, fill_opacity=1,
                           stroke_color=INK, stroke_width=4).move_to([x, y, 0]))
    g.add(RoundedRectangle(width=w, height=0.72, corner_radius=0.18,
                           fill_color=DARK_TOP, fill_opacity=1,
                           stroke_width=0).move_to([x, y + h / 2 - 0.36, 0]))
    g.add(T(title, size=30, color="#FFFFFF")
          .move_to([x - w / 2 + 1.0, y + h / 2 - 0.36, 0]))
    return g


def answer_card(x, y, w=4.6, h=2.6, nlines=3):
    """White answer card: ghost text lines + terracotta dot."""
    g = VGroup()
    g.add(RoundedRectangle(width=w, height=h, corner_radius=0.12,
                           fill_color=CARD, fill_opacity=1,
                           stroke_color=INK, stroke_width=3).move_to([x, y, 0]))
    for i in range(nlines):
        f = 0.30 + i * 0.20
        ly = y + h / 2 - f * h
        g.add(Line([x - w / 2 + 0.35, ly, 0], [x + w / 2 - 0.35, ly, 0],
                   color=GHOST, stroke_width=5))
    g.add(Dot([x - w / 2 + 0.35, y + h / 2 - 0.22, 0],
              radius=0.08, color=TERRA))
    return g


def qcard(x, y, w, h, text, size=34):
    """Question card: rounded rect, centered text, terracotta dot."""
    g = VGroup()
    g.add(RoundedRectangle(width=w, height=h, corner_radius=0.2,
                           fill_color=CARD, fill_opacity=1,
                           stroke_color=INK, stroke_width=3).move_to([x, y, 0]))
    g.add(T(text, size=size).move_to([x, y, 0]))
    g.add(Dot([x - w / 2 + 0.4, y + h / 2 - 0.28, 0],
              radius=0.08, color=TERRA))
    return g


def magnifier(x, y, r=0.75):
    """The critic's lens: terracotta rim + handle."""
    g = VGroup()
    g.add(Circle(radius=r, stroke_color=TERRA, stroke_width=8,
                 fill_opacity=0).move_to([x, y, 0]))
    hx, hy = x + r * 0.7, y - r * 0.7
    g.add(Line([hx, hy, 0], [hx + 0.7, hy - 0.7, 0],
               color=TERRA, stroke_width=8))
    return g


def month_pills():
    """Twelve month pills, 2 rows of 6. Returns (pills, letters, xs, ys)."""
    letters = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]
    pills, xs, ys = VGroup(), [], []
    for i, L in enumerate(letters):
        px = -2.55 + (i % 6) * 1.02
        py = 1.55 if i < 6 else 0.70
        xs.append(px); ys.append(py)
        pg = VGroup()
        pg.add(RoundedRectangle(width=0.92, height=0.62, corner_radius=0.31,
                                fill_color="#FFFFFF", fill_opacity=1,
                                stroke_color=INK, stroke_width=2.5).move_to([px, py, 0]))
        pg.add(lab(L, px, py - 0.02, size=30))
        pills.add(pg)
    return pills, letters, xs, ys


def flag(x, y, s=0.5):
    """Small terracotta flaw-flag triangle."""
    return Polygon([x - s / 2, y, 0], [x + s / 2, y, 0], [x, y + s, 0],
                   fill_color=TERRA, fill_opacity=1, stroke_width=0)


# ═════════════════════════════ B00 — the move ═════════════════════════════
class B00_TheSecondLook(Scene):
    def construct(self):
        win = chat_window(0, 0.2)
        self.play(FadeIn(win), run_time=0.6)

        card = answer_card(0, 0.1, w=4.8, h=2.7)
        until(self, "gives you its answer")
        self.play(FadeIn(card), run_time=0.6)

        lens = magnifier(4.6, 2.4, r=0.8)
        until(self, "send it back")
        self.play(FadeIn(lens), run_time=0.4)
        self.play(lens.animate.move_to([1.7, 0.9, 0]), run_time=0.7)

        until(self, "looking twice")
        self.play(GrowFromCenter(check(2.75, -1.55, s=0.35, color=TERRA, w=9)),
                  run_time=0.5)
        finish(self)


# ═════════════════════════════ B01 — the three questions ═════════════════════════════
class B01_ThreeQuestions(Scene):
    def construct(self):
        c1 = qcard(0, 1.95, 8.2, 1.35, "What's wrong with this answer?")
        c2 = qcard(0, 0.20, 8.2, 1.35, "What did you assume?")
        c3 = qcard(0, -1.55, 8.2, 1.35, "What's the strongest objection to it?")
        until(self, "One:")
        self.play(FadeIn(c1), run_time=0.5)
        until(self, "Two:")
        self.play(FadeIn(c2), run_time=0.5)
        until(self, "Three:")
        self.play(FadeIn(c3), run_time=0.5)
        finish(self)


# ═════════════════════════════ B02 — demo, the trap ═════════════════════════════
class B02_TheTrap(Scene):
    def construct(self):
        pills, _, xs, ys = month_pills()
        title = lab("Which months have 28 days?", 0, 2.75, size=44)
        until(self, "which months")
        self.play(FadeIn(pills), FadeIn(title), run_time=0.7)

        feb = T("February", size=48).move_to([0, -1.65, 0])
        card = answer_card(0, -1.75, w=4.6, h=1.6, nlines=0)
        until(self, "February")
        self.play(FadeIn(card), FadeIn(feb), run_time=0.6)

        glow = Circle(radius=0.56, stroke_color=TERRA, stroke_width=9,
                      fill_opacity=0).move_to([xs[1], ys[1], 0])
        self.play(Create(glow), run_time=0.5)

        until(self, "It is also wrong")
        x1 = Line([-0.9, -1.35, 0], [0.9, -2.15, 0], color=TERRA, stroke_width=10)
        x2 = Line([-0.9, -2.15, 0], [0.9, -1.35, 0], color=TERRA, stroke_width=10)
        self.play(FadeOut(glow), Create(x1), Create(x2), run_time=0.6)
        finish(self)


# ═════════════════════════════ B03 — demo, the catch ═════════════════════════════
class B03_TheCatch(Scene):
    def construct(self):
        pills, _, xs, ys = month_pills()
        card = answer_card(0, -1.85, w=5.0, h=1.7, nlines=0)
        feb = T("February", size=44).move_to([0, -1.75, 0])
        glow = Circle(radius=0.56, stroke_color=TERRA, stroke_width=9,
                      fill_opacity=0).move_to([xs[1], ys[1], 0])
        self.play(FadeIn(pills), FadeIn(card), FadeIn(feb), FadeIn(glow),
                  run_time=0.7)

        prompt = qcard(0, 2.85, 7.4, 0.9, "What's wrong with your answer?", size=32)
        until(self, "write back")
        self.play(FadeIn(prompt), run_time=0.5)

        lens = magnifier(-4.6, 1.1, r=0.7)
        until(self, "catches it")
        self.play(FadeIn(lens), run_time=0.4)
        self.play(lens.animate.move_to([4.6, 1.1, 0]), run_time=0.8)
        self.play(FadeOut(lens), FadeOut(glow), run_time=0.4)

        until(self, "every other month")
        dots = VGroup(*[Dot([x, y, 0], radius=0.10, color=TERRA)
                        for x, y in zip(xs, ys)])
        self.play(FadeIn(dots), run_time=0.8)

        until(self, "all of them")
        self.remove(feb)
        fixed = T("All twelve.", size=44).move_to([0, -1.75, 0])
        self.play(FadeIn(fixed), run_time=0.5)
        self.play(GrowFromCenter(check(2.9, -2.35, s=0.32, color=TERRA, w=9)),
                  run_time=0.5)
        finish(self)


# ═════════════════════════════ B04 — the email ═════════════════════════════
class B04_TheEmail(Scene):
    def construct(self):
        draft = VGroup()
        draft.add(RoundedRectangle(width=7.8, height=2.6, corner_radius=0.14,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK, stroke_width=3).move_to([0, 1.0, 0]))
        draft.add(lab("To: your boss", -3.15, 1.95, size=30, color=DIM))
        draft.add(lab("Per my last email,", 0, 1.25, size=32))
        draft.add(lab("as I already explained, the deadline moved.", 0, 0.55, size=32))
        draft.add(Dot([-3.55, 2.0, 0], radius=0.08, color=TERRA))
        until(self, "email to your boss")
        self.play(FadeIn(draft), run_time=0.7)

        until(self, "quietly rude")
        self.play(Create(Line([-2.9, 0.28, 0], [2.9, 0.28, 0],
                              color=TERRA, stroke_width=7)), run_time=0.5)

        until(self, "rewrites it")
        redraft = VGroup()
        redraft.add(RoundedRectangle(width=7.8, height=1.7, corner_radius=0.14,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK, stroke_width=3).move_to([0, -1.95, 0]))
        redraft.add(lab("Quick update: the deadline moved.", -0.4, -1.95, size=32))
        self.play(FadeIn(redraft), run_time=0.6)
        self.play(GrowFromCenter(check(3.35, -1.95, s=0.3, color=TERRA, w=9)),
                  run_time=0.5)
        finish(self)


# ═════════════════════════════ B05 — where it pays ═════════════════════════════
class B05_WhereItPays(Scene):
    def construct(self):
        xs = [-4.8, -1.6, 1.6, 4.8]
        cards = VGroup()
        for x in xs:
            cards.add(RoundedRectangle(width=2.6, height=2.8, corner_radius=0.16,
                                       fill_color=CARD, fill_opacity=1,
                                       stroke_color=INK, stroke_width=3).move_to([x, 0.5, 0]))
        # numbers
        cards.add(lab("123", xs[0], 0.85, size=64, bold=True))
        cards.add(lab("numbers", xs[0], -0.45, size=32))
        # dates: mini calendar
        cal = VGroup()
        cal.add(RoundedRectangle(width=1.5, height=1.5, corner_radius=0.1,
                                 fill_color="#FFFFFF", fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to([xs[1], 0.9, 0]))
        cal.add(RoundedRectangle(width=1.5, height=0.4, corner_radius=0.1,
                                 fill_color=INK, fill_opacity=1,
                                 stroke_width=0).move_to([xs[1], 1.45, 0]))
        cards.add(cal)
        cards.add(lab("dates", xs[1], -0.45, size=32))
        # code
        cards.add(lab("{ }", xs[2], 0.85, size=64, bold=True))
        cards.add(lab("code", xs[2], -0.45, size=32))
        # plans: route arrow
        route = VGroup()
        route.add(Arrow([-0.6, 0.9, 0], [0.6, 0.9, 0], color=INK,
                        stroke_width=7, buff=0).shift([xs[3], 0, 0]))
        route.add(Dot([xs[3] - 0.6, 0.9, 0], radius=0.09, color=TERRA))
        cards.add(route)
        cards.add(lab("plans", xs[3], -0.45, size=32))
        self.play(FadeIn(cards), run_time=0.8)

        for phrase, x in zip(["Numbers,", "dates,", "code,", "plans"], xs):
            until(self, phrase)
            self.play(GrowFromCenter(check(x + 0.75, 1.35, s=0.28, color=TERRA, w=8)),
                      run_time=0.4)
        finish(self)


# ═════════════════════════════ B06 — the limit ═════════════════════════════
class B06_TheLimit(Scene):
    def construct(self):
        card = answer_card(-1.8, 0.2, w=4.8, h=3.2, nlines=4)
        crack = Line([-3.4, 0.36, 0], [-0.4, 0.36, 0], color=GHOST, stroke_width=4)
        self.play(FadeIn(card), FadeIn(crack), run_time=0.7)

        lens = magnifier(-1.8, 0.2, r=0.95)
        until(self, "same brain")
        self.play(FadeIn(lens), run_time=0.4)
        until(self, "blind spots")
        self.play(lens.animate.move_to([0.4, 0.2, 0]), run_time=0.9)

        until(self, "breaks what was fine")
        patch = RoundedRectangle(width=2.2, height=0.44, corner_radius=0.2,
                                 fill_color=TERRA, fill_opacity=1,
                                 stroke_width=0).move_to([-1.8, -0.12, 0])
        self.play(FadeIn(patch), run_time=0.5)

        until(self, "You stay the judge")
        youpill = pill(4.3, 0.2, 2.0, h=0.85)
        youlab = lab("YOU", 4.3, 0.18, size=40, bold=True)
        self.play(FadeIn(youpill), FadeIn(youlab), run_time=0.5)
        finish(self)


# ═════════════════════════════ B07 — the pro move ═════════════════════════════
class B07_ProMove(Scene):
    def construct(self):
        p1 = qcard(0, 1.5, 6.6, 1.05, "Is this right?", size=36)
        until(self, "is this right?")
        self.play(FadeIn(p1), run_time=0.5)

        until(self, "one answer")
        yesm = lab("YES", 0, 0.05, size=84, bold=True)
        self.play(FadeIn(yesm), run_time=0.5)

        p2 = qcard(0, -1.45, 6.6, 1.05, "What's wrong with this?", size=36)
        until(self, "what is wrong instead")
        self.play(FadeIn(p2), run_time=0.5)

        until(self, "hunting flaws")
        flags = VGroup(*[flag(x, -2.75) for x in (-1.2, 0.0, 1.2)])
        self.play(GrowFromCenter(flags), run_time=0.6)
        finish(self)


# ═════════════════════════════ B08 — the habit ═════════════════════════════
class B08_TheHabit(Scene):
    def construct(self):
        card = answer_card(-3.6, 0.4, w=3.6, h=2.4, nlines=3)
        until(self, "get the answer")
        self.play(FadeIn(card), run_time=0.6)

        lens = magnifier(3.6, 0.4, r=0.85)
        until(self, "send it back")
        self.play(FadeIn(lens), run_time=0.5)

        until(self, "then decide")
        top = CurvedArrow([-1.7, 1.35, 0], [1.7, 1.35, 0],
                          angle=-55 * DEGREES, color=INK, stroke_width=6)
        bot = CurvedArrow([1.7, -0.55, 0], [-1.7, -0.55, 0],
                          angle=-55 * DEGREES, color=INK, stroke_width=6)
        self.play(Create(top), Create(bot), run_time=0.8)

        until(self, "whole habit")
        minis = VGroup(
            qcard(-3.8, -2.5, 3.4, 0.8, "What's wrong?", size=32),
            qcard(0.0, -2.5, 3.4, 0.8, "Assumed what?", size=32),
            qcard(3.8, -2.5, 3.4, 0.8, "Objection?", size=32))
        self.play(FadeIn(minis), run_time=0.7)
        finish(self)
