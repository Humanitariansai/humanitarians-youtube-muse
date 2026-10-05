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


def steelman_card(x, y, w=5.6, h=2.2):
    """Answer card with a terracotta rim: the steelman."""
    g = VGroup()
    g.add(RoundedRectangle(width=w, height=h, corner_radius=0.12,
                           fill_color=CARD, fill_opacity=1,
                           stroke_color=TERRA, stroke_width=7).move_to([x, y, 0]))
    for i in range(2):
        f = 0.32 + i * 0.22
        ly = y + h / 2 - f * h
        g.add(Line([x - w / 2 + 0.4, ly, 0], [x + w / 2 - 0.4, ly, 0],
                   color=GHOST, stroke_width=5))
    g.add(lab("the steelman", x + w / 2 + 1.45, y, size=30, bold=True))
    return g


def xmark(x, y, s=0.35, color=TERRA, w=9):
    return VGroup(
        Line([x - s, y - s * 0.8, 0], [x + s, y + s * 0.8, 0], color=color, stroke_width=w),
        Line([x - s, y + s * 0.8, 0], [x + s, y - s * 0.8, 0], color=color, stroke_width=w))


def flag(x, y, s=0.5):
    """Small terracotta flaw-flag triangle."""
    return Polygon([x - s / 2, y, 0], [x + s / 2, y, 0], [x, y + s, 0],
                   fill_color=TERRA, fill_opacity=1, stroke_width=0)


def nod(x, y):
    """The dim nod: a grey circle with a check — the weak answer to 'do you agree?'."""
    g = VGroup()
    g.add(Circle(radius=0.42, stroke_color=DIM, stroke_width=6,
                 fill_opacity=0).move_to([x, y, 0]))
    g.add(check(x, y, s=0.18, color=DIM, w=7))
    return g


# ═════════════════════════════ B00 — the move ═════════════════════════════
class B00_TheMove(Scene):
    def construct(self):
        qp = pill(0, 2.55, 5.8)
        ql = lab("A big decision?", 0, 2.55, size=38)
        until(self, "big decision")
        self.play(FadeIn(qp), FadeIn(ql), run_time=0.5)

        ca = answer_card(-2.95, 0.55, w=4.5, h=2.6)
        la = lab("first answer", -2.95, -1.15, size=32)
        until(self, "first answer")
        self.play(FadeIn(ca), FadeIn(la), run_time=0.6)

        cb = answer_card(2.95, 0.55, w=4.5, h=2.6)
        lb = lab("second opinion", 2.95, -1.15, size=32)
        a1 = Arrow([-0.55, 0.55, 0], [0.55, 0.55, 0], color=INK,
                   stroke_width=6, buff=0)
        a2 = Arrow([0.55, 0.55, 0], [-0.55, 0.55, 0], color=INK,
                   stroke_width=6, buff=0)
        until(self, "get a second opinion")
        self.play(FadeIn(cb), FadeIn(lb), Create(a1), Create(a2), run_time=0.7)

        r1 = pill(-2.95, -2.35, 4.3)
        r1l = lab("ask a second AI", -2.95, -2.35, size=32)
        until(self, "Ask a second AI")
        self.play(FadeIn(r1), FadeIn(r1l), run_time=0.5)

        r2 = pill(2.95, -2.35, 4.3)
        r2l = lab("argue against itself", 2.95, -2.35, size=32)
        until(self, "argue against itself")
        self.play(FadeIn(r2), FadeIn(r2l), run_time=0.5)
        finish(self)


# ═════════════════════════════ B01 — the two routes ═════════════════════════════
class B01_TwoRoutes(Scene):
    def construct(self):
        left = VGroup()
        left.add(chat_window(-3.2, 0.85, w=3.6, h=2.5, title="AI 2"))
        left.add(lab("a second AI", -3.2, -1.15, size=36, bold=True))
        left.add(lab("fresh — never saw", -3.2, -1.75, size=28, color=DIM))
        left.add(lab("the first answer", -3.2, -2.18, size=28, color=DIM))
        until(self, "Route one")
        self.play(FadeIn(left), run_time=0.7)

        right = VGroup()
        right.add(answer_card(3.2, 1.0, w=3.4, h=1.9, nlines=2))
        m1 = answer_card(2.2, -1.15, w=2.0, h=1.3, nlines=1)
        m2 = answer_card(4.2, -1.15, w=2.0, h=1.3, nlines=1)
        right.add(m1, m2)
        right.add(Line([2.7, 0.05, 0], [2.2, -0.5, 0], color=INK, stroke_width=5))
        right.add(Line([3.7, 0.05, 0], [4.2, -0.5, 0], color=INK, stroke_width=5))
        right.add(lab("the steelman", 3.2, -2.2, size=36, bold=True))
        until(self, "Route two")
        self.play(FadeIn(right), run_time=0.7)

        bp = pill(0, -2.95, 6.6)
        bl = lab("both sides on the table", 0, -2.95, size=34)
        until(self, "both sides on the table")
        self.play(FadeIn(bp), FadeIn(bl), run_time=0.5)
        finish(self)


# ═════════════════════════════ B02 — demo, the first answer ═════════════════════════════
class B02_FirstAnswer(Scene):
    def construct(self):
        dp = pill(0, 2.55, 6.6)
        dl = lab("Night-shift job — take it?", 0, 2.55, size=36)
        until(self, "night-shift job")
        self.play(FadeIn(dp), FadeIn(dl), run_time=0.5)

        card = answer_card(0, 0.25, w=5.8, h=2.8, nlines=2)
        txt = lab("Take it — the pay is real.", 0, 0.25, size=36)
        until(self, "says: take it")
        self.play(FadeIn(card), FadeIn(txt), run_time=0.6)

        until(self, "Confident. Done")
        self.play(GrowFromCenter(check(3.55, -1.65, s=0.35, color=TERRA, w=9)),
                  run_time=0.5)
        finish(self)


# ═════════════════════════════ B03 — demo, the steelman ═════════════════════════════
class B03_TheSteelman(Scene):
    def construct(self):
        card = answer_card(0, 1.25, w=5.4, h=2.0, nlines=0)
        txt = lab("Take it — the pay is real.", 0, 1.25, size=34)
        self.play(FadeIn(card), FadeIn(txt), run_time=0.6)

        prompt = qcard(0, 2.8, 7.8, 0.95, "argue the other side at its strongest", size=32)
        until(self, "write back")
        self.play(FadeIn(prompt), run_time=0.5)

        steel = steelman_card(0, -1.15, w=5.6, h=2.0)
        until(self, "the steelman")
        self.play(GrowFromCenter(steel), run_time=0.7)

        p1 = pill(-3.9, -2.75, 3.5)
        p1l = lab("broken sleep", -3.9, -2.75, size=30)
        until(self, "Broken sleep")
        self.play(FadeIn(p1), FadeIn(p1l), run_time=0.4)

        p2 = pill(0, -2.75, 3.5)
        p2l = lab("health costs", 0, -2.75, size=30)
        until(self, "Health costs")
        self.play(FadeIn(p2), FadeIn(p2l), run_time=0.4)

        p3 = pill(3.9, -2.75, 3.5)
        p3l = lab("the drive home", 3.9, -2.75, size=30)
        until(self, "drive home")
        self.play(FadeIn(p3), FadeIn(p3l), run_time=0.4)
        finish(self)


# ═════════════════════════════ B04 — demo, both sides ═════════════════════════════
class B04_BothSides(Scene):
    def construct(self):
        cl = answer_card(-3.15, 0.75, w=4.7, h=2.7, nlines=2)
        tll = lab("the pay is real", -3.15, 0.75, size=34)
        cr = answer_card(3.15, 0.75, w=4.7, h=2.7, nlines=2)
        trl = lab("the costs are real", 3.15, 0.75, size=34)
        vs = lab("vs", 0, 0.75, size=40, bold=True, color=DIM)
        until(self, "hold both")
        self.play(FadeIn(cl), FadeIn(tll), FadeIn(cr), FadeIn(trl),
                  FadeIn(vs), run_time=0.8)

        yp = pill(0, -2.2, 2.8, h=0.95)
        yl = lab("YOU", 0, -2.18, size=42, bold=True)
        until(self, "You decide")
        self.play(FadeIn(yp), FadeIn(yl), run_time=0.5)
        self.play(GrowFromCenter(check(1.95, -2.2, s=0.3, color=TERRA, w=9)),
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
                                       stroke_color=INK, stroke_width=3).move_to([x, 0.75, 0]))
        # lease: a page
        cards.add(RoundedRectangle(width=1.4, height=1.5, corner_radius=0.08,
                                   fill_color="#FFFFFF", fill_opacity=1,
                                   stroke_color=INK, stroke_width=3).move_to([xs[0], 1.05, 0]))
        cards.add(lab("lease", xs[0], -0.95, size=30))
        # job move: a door with an arrow leaving
        cards.add(RoundedRectangle(width=1.1, height=1.6, corner_radius=0.06,
                                   fill_color="#FFFFFF", fill_opacity=1,
                                   stroke_color=INK, stroke_width=3).move_to([xs[1] - 0.35, 1.0, 0]))
        cards.add(Arrow([xs[1] - 0.3, 1.0, 0], [xs[1] + 1.0, 1.0, 0], color=INK,
                        stroke_width=7, buff=0))
        cards.add(lab("job move", xs[1], -0.95, size=30))
        # big purchase: a box with a tag dot
        cards.add(RoundedRectangle(width=1.5, height=1.1, corner_radius=0.06,
                                   fill_color="#FFFFFF", fill_opacity=1,
                                   stroke_color=INK, stroke_width=3).move_to([xs[2], 1.0, 0]))
        cards.add(Dot([xs[2] + 0.75, 1.55, 0], radius=0.11, color=TERRA))
        cards.add(lab("big purchase", xs[2], -0.95, size=30))
        # medical: a cross
        cards.add(Line([xs[3], 0.45, 0], [xs[3], 1.55, 0], color=INK, stroke_width=9))
        cards.add(Line([xs[3] - 0.55, 1.0, 0], [xs[3] + 0.55, 1.0, 0], color=INK, stroke_width=9))
        cards.add(lab("medical", xs[3], -0.95, size=30))
        until(self, "expensive and hard to undo")
        self.play(FadeIn(cards), run_time=0.8)

        for phrase, x in zip(["A lease", "A job", "big purchase", "medical question"], xs):
            until(self, phrase)
            self.play(GrowFromCenter(check(x + 0.75, 1.55, s=0.28, color=TERRA, w=8)),
                      run_time=0.4)

        dp = pill(0, -2.35, 5.4)
        dl = lab("dinner plans — one answer is plenty", 0, -2.35, size=30)
        until(self, "Dinner plans")
        self.play(FadeIn(dp), FadeIn(dl), run_time=0.5)
        finish(self)


# ═════════════════════════════ B06 — the limit ═════════════════════════════
class B06_TheLimit(Scene):
    def construct(self):
        w1 = chat_window(-3.35, 0.95, w=4.3, h=2.9, title="AI 1")
        w2 = chat_window(3.35, 0.95, w=4.3, h=2.9, title="AI 2")
        until(self, "blind spots")
        self.play(FadeIn(w1), FadeIn(w2), run_time=0.7)

        band = RoundedRectangle(width=3.0, height=0.9, corner_radius=0.3,
                                fill_color="#FFFFFF", fill_opacity=1,
                                stroke_color=INK, stroke_width=3).move_to([0, 0.95, 0])
        bandlab = lab("same training", 0, 0.95, size=28)
        until(self, "same brain")
        self.play(FadeIn(band), FadeIn(bandlab), run_time=0.5)

        xs = [-3.45, -1.15, 1.15, 3.45]
        row = VGroup()
        for x in xs:
            row.add(RoundedRectangle(width=2.0, height=1.15, corner_radius=0.14,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK, stroke_width=3).move_to([x, -2.35, 0]))
        for x in xs[:3]:
            row.add(xmark(x, -2.35, s=0.22, color=DIM, w=7))
        glow = RoundedRectangle(width=2.0, height=1.15, corner_radius=0.14,
                                fill_opacity=0,
                                stroke_color=TERRA, stroke_width=7).move_to([xs[3], -2.35, 0])
        row.add(glow)
        until(self, "shop around")
        self.play(FadeIn(row), run_time=0.7)

        until(self, "cheerleader")
        self.play(FadeOut(glow),
                  GrowFromCenter(xmark(xs[3], -2.35, s=0.35, color=TERRA, w=9)),
                  run_time=0.6)
        finish(self)


# ═════════════════════════════ B07 — the pro move ═════════════════════════════
class B07_ProMove(Scene):
    def construct(self):
        p1 = qcard(0, 2.45, 6.4, 1.0, "Do you agree?", size=36)
        until(self, "do you agree?")
        self.play(FadeIn(p1), run_time=0.5)

        nd = nod(0, 1.25)
        until(self, "a nod")
        self.play(FadeIn(nd), run_time=0.5)

        p2 = qcard(0, -0.05, 6.4, 1.0, "Steelman the opposite case.", size=36)
        until(self, "steelman the opposite case")
        self.play(FadeIn(p2), run_time=0.5)

        flags = VGroup(*[flag(x, -1.45) for x in (-1.2, 0.0, 1.2)])
        until(self, "real job")
        self.play(GrowFromCenter(flags), run_time=0.6)

        p3 = qcard(0, -2.55, 6.0, 0.85, "What would change your answer?", size=30)
        until(self, "what would change your answer")
        self.play(FadeIn(p3), run_time=0.5)

        hidden = VGroup()
        hidden.add(answer_card(4.9, -2.55, w=1.9, h=1.2, nlines=1))
        hidden.add(RoundedRectangle(width=1.9, height=1.2, corner_radius=0.1,
                                    fill_color=DIM, fill_opacity=0.85,
                                    stroke_width=0).move_to([4.9, -2.55, 0]))
        hidden.add(lab("kept hidden", 4.9, -1.8, size=26, color=DIM))
        until(self, "independent")
        self.play(FadeIn(hidden), run_time=0.5)
        finish(self)


# ═════════════════════════════ B08 — the habit ═════════════════════════════
class B08_TheHabit(Scene):
    def construct(self):
        c1 = answer_card(-4.0, 0.45, w=3.4, h=2.4, nlines=2)
        l1 = lab("first answer", -4.0, -1.2, size=30)
        until(self, "first answer")
        self.play(FadeIn(c1), FadeIn(l1), run_time=0.6)

        c2 = answer_card(0.4, 0.45, w=3.4, h=2.4, nlines=2)
        l2 = lab("second opinion", 0.4, -1.2, size=30)
        a1 = Arrow([-2.2, 0.45, 0], [-1.45, 0.45, 0], color=INK,
                   stroke_width=6, buff=0)
        until(self, "second opinion")
        self.play(Create(a1), FadeIn(c2), FadeIn(l2), run_time=0.7)

        you = pill(4.45, 0.45, 2.2, h=0.95)
        yl = lab("YOU", 4.45, 0.43, size=40, bold=True)
        a2 = Arrow([2.25, 0.45, 0], [3.25, 0.45, 0], color=INK,
                   stroke_width=6, buff=0)
        until(self, "decide yourself")
        self.play(Create(a2), FadeIn(you), FadeIn(yl), run_time=0.6)
        finish(self)
