"""scenes.py — "Show It an Example" (show-tell).
Seven Manim scenes, one per body beat. iso_kit.py pasted at top (Gate A copies only this file)."""

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

"""SCENES (appended after the pasted iso_kit.py block)."""

# ── local helpers ─────────────────────────────────────────────────────
def _shadow(x=0.0, y=-3.05, w=10.0, h=0.4):
    return Ellipse(width=w, height=h, fill_color=GHOST, fill_opacity=0.45,
                   stroke_width=0).move_to([x, y, 0])


def _label(text, x, y, size=36):
    return T(text, size=size).move_to([x, y, 0])


def _box_at(ox, oy, s):
    """The film's prompt box (same object, every beat): returns (iso, back, front)."""
    iso = Iso(ox, oy, s)
    back, front = iso.open_box(-1.4, -1.0, 0, 2.8, 2.0, 1.1)
    return iso, back, front


BOX_ISO = (-2.4, -0.3, 1.0)   # the prompt box never moves
ROW_ISO = (1.9, -1.2, 0.8)    # projection used for the example-card row
ROW_SX = (0.7, 2.25, 3.8)     # screen-x of the three good cards
ROW_SY = -1.9                 # screen-y of the card row (constant: a level row)
BAD_SX = 5.35                 # screen-x of the sloppy fourth card
CARD_W, CARD_D = 0.9, 1.1


def _place(iso, sx, sy, w=CARD_W, d=CARD_D):
    """Iso lower-corner (x0, y0) so the page's centre lands at screen (sx, sy)."""
    ox, oy, s = iso.ox, iso.oy, iso.s
    xpy = (sy - oy) / (0.5 * s)
    xmy = (sx - ox) / (0.8660254 * s)
    cx, cy = (xmy + xpy) / 2.0, (xpy - xmy) / 2.0
    return cx - w / 2.0, cy - d / 2.0


def _row_card(iso, sx, sy=ROW_SY, bad=False):
    """One example card centred at screen (sx, sy)."""
    x0, y0 = _place(iso, sx, sy)
    if not bad:
        return iso.page(x0, y0, 0, w=CARD_W, d=CARD_D)
    slab = iso.box(x0, y0, 0, CARD_W, CARD_D, 0.06, top="#D8C39A",
                   left="#C7AE86", right="#BFA67E", sw=2)
    zt = 0.06
    lines = VGroup(*[Line(iso.p(x0 + 0.15, y0 + CARD_D * f, zt),
                          iso.p(x0 + 0.62, y0 + CARD_D * (f + 0.09), zt),
                          color=GHOST, stroke_width=4) for f in (0.22, 0.45, 0.68)])
    dot = Dot(iso.p(x0 + 0.15, y0 + CARD_D * 0.86, zt), radius=0.07, color=TERRA)
    return VGroup(slab, lines, dot)


def _insiders(iso):
    """The three example pages resting inside the prompt box."""
    return [iso.page(x, -0.5, z, w=CARD_W, d=CARD_D)
            for x, z in ((-0.7, 0.15), (0.0, 0.35), (0.7, 0.55))]


class B00_TheBox(Scene):
    """The prompt box drops in; the two ways to fill it: describe, or show."""

    def construct(self):
        self.add(_shadow())
        iso, back, front = _box_at(*BOX_ISO)
        box = VGroup(back, front)
        self.play(FadeIn(box, shift=DOWN * 1.2), run_time=1.0)
        lbl = _label("your prompt", -2.4, -2.3)
        pill_d = pill(2.6, 0.5, 2.6)
        t_d = _label("describe", 2.6, 0.5, size=34)
        pill_s = pill(2.6, -0.7, 2.6)
        t_s = _label("show", 2.6, -0.7, size=34)
        dot = Dot([1.05, -0.7, 0], radius=0.09, color=TERRA)
        self.play(FadeIn(lbl), FadeIn(pill_d), FadeIn(t_d), FadeIn(pill_s),
                  FadeIn(t_s), FadeIn(dot), run_time=0.7)
        until(self, "This film is about the showing way")
        finish(self)


class B01_RuleStack(Scene):
    """The describe way: a stack of instruction pages piles up beside the box."""

    def construct(self):
        self.add(_shadow())
        iso, back, front = _box_at(*BOX_ISO)
        self.add(VGroup(back, front))
        siso = Iso(2.6, -1.0, 0.8)
        pages = VGroup(*[siso.page(-1.0, -0.8, i * 0.15, w=1.1, d=1.4)
                         for i in range(6)])
        for pg in pages:
            self.play(FadeIn(pg, shift=DOWN * 0.4, rate_func=ease_in), run_time=0.45)
        lbl = _label("rules", 2.6, -2.4)
        self.play(FadeIn(lbl), run_time=0.4)
        until(self, "guess what warm actually sounds like")
        finish(self)


class B02_ExamplesIn(Scene):
    """The show way: the rule stack slides off; three example pages drop into the box."""

    def construct(self):
        self.add(_shadow())
        iso, back, front = _box_at(*BOX_ISO)
        box = VGroup(back, front)
        siso = Iso(2.6, -1.0, 0.8)
        stack = VGroup(*[siso.page(-1.0, -0.8, i * 0.15, w=1.1, d=1.4)
                         for i in range(6)])
        self.add(box, stack)
        self.play(FadeOut(stack, shift=RIGHT * 2.0), run_time=0.8)
        for pg in _insiders(iso):
            self.play(FadeIn(pg, shift=DOWN * 1.0, rate_func=ease_in), run_time=0.6)
        lbl = _label("examples", -2.4, -2.3)
        self.play(FadeIn(lbl), run_time=0.4)
        until(self, "like this")
        finish(self)


class B03_FiveThings(Scene):
    """Three examples fly out of the box into a row; five tags rise off them."""

    def construct(self):
        self.add(_shadow(0.5, -3.0, 11.0))
        iso, back, front = _box_at(*BOX_ISO)
        cards = _insiders(iso)
        self.add(back, VGroup(*cards), front)
        # fly each card from inside the box to its slot in the row
        starts = [(-2.66, -0.25), (-2.05, 0.30), (-1.45, 0.85)]
        shifts = [(sx - px, ROW_SY - py) for (px, py), sx in zip(starts, ROW_SX)]
        self.play(*[c.animate.shift(RIGHT * dx + UP * dy)
                    for c, (dx, dy) in zip(cards, shifts)], run_time=0.9)
        tags = [("length", 0.5), ("tone", 1.55), ("shape", 2.6), ("words", 3.65),
                ("tricky bits", 4.7)]
        for word, x in tags:
            w = 1.9 if word == "tricky bits" else 1.3
            pg = pill(x, 0.7, w)
            tx = _label(word, x, 0.7, size=32)
            lead = Line([x, 0.10, 0], [x, -1.10, 0], color=INK, stroke_width=3)
            self.play(FadeIn(pg), FadeIn(tx), Create(lead), run_time=0.35)
        until(self, "copied the lot")
        finish(self)


class B04_BadCard(Scene):
    """A sloppy fourth example drops in; the output page slides out crooked."""

    def construct(self):
        self.add(_shadow(0.5, -3.05, 11.0))
        iso, back, front = _box_at(*BOX_ISO)
        riso = Iso(*ROW_ISO)
        cards = [_row_card(riso, sx) for sx in ROW_SX]
        self.add(back, VGroup(*_insiders(iso)), front, *cards)
        bad = _row_card(riso, BAD_SX, bad=True)
        self.play(FadeIn(bad, shift=DOWN * 0.8, rate_func=ease_in), run_time=0.7)
        out = iso.page(0.1, -0.2, 1.5, w=CARD_W, d=CARD_D)
        out.rotate(0.14, about_point=out.get_center())
        out.move_to([-2.4, -0.9, 0])
        self.play(FadeIn(out, shift=UP * 0.8), run_time=0.7)
        lbl = _label("your draft", -2.4, -2.5, size=34)
        self.play(FadeIn(lbl), run_time=0.4)
        until(self, "teaches the wrong lesson, fast")
        finish(self)


class B05_ThreeChecks(Scene):
    """Three quick checks: a check pops over each good example."""

    def construct(self):
        self.add(_shadow(0.5, -3.05, 11.0))
        riso = Iso(*ROW_ISO)
        cards = [_row_card(riso, sx) for sx in ROW_SX]
        self.add(*cards)
        for x in ROW_SX:
            self.play(FadeIn(check(x, -0.85, s=0.22, color=TERRA, w=8)),
                      run_time=0.4)
        lbl = _label("three checks", 2.25, 0.35)
        self.play(FadeIn(lbl), run_time=0.4)
        until(self, "paste")
        finish(self)


class B06_ShortVsTall(Scene):
    """The comparison: three small examples against the tall rule stack."""

    def construct(self):
        self.add(_shadow(0.0, -3.2, 10.0, 0.3))
        riso = Iso(*ROW_ISO)
        cards = [_row_card(riso, sx) for sx in ROW_SX]
        self.add(*cards)
        stack = VGroup(*[RoundedRectangle(width=2.2, height=0.32, corner_radius=0.06,
                                          fill_color="#FFFFFF", fill_opacity=1,
                                          stroke_color=INK, stroke_width=2.5)
                          .move_to([-3.3, -1.7 + i * 0.36, 0]) for i in range(6)])
        for pg in stack:
            self.play(FadeIn(pg, shift=DOWN * 0.3, rate_func=ease_in), run_time=0.4)
        self.play(FadeIn(_label("examples", 2.25, -2.85)),
                  FadeIn(_label("rules", -3.3, -2.85)), run_time=0.4)
        until(self, "still gets the full picture")
        finish(self)
