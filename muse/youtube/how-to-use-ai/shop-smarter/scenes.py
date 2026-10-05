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
"""
shop-smarter — scenes.py (show-tell).

The iso_kit.py block (top of file) is pasted verbatim from
brutalist.art/skills/make/show-tell/templates/iso_kit.py — Gate A copies only
scenes.py, so the kit must live here, not be imported.

Cast for the whole film: the three kraft option boxes (the same boxes every
beat), ink heads, kraft pages, the comparison table, a magnifier, a price tag.
Every scene: all motion lands in the first ~40% of the beat (fully opaque,
nothing half-done at the midpoint GATE T samples), then `until()` holds on a
settled labelled frame and `finish()` pads to the audio.
"""


# ═════════════════════════════ local helpers ═════════════════════════════
def label(text, x, y, size=40):
    return T(text, size=size, color=INK).move_to([x, y, 0])


def leader(x0, x1, y, color=DIM):
    """A dim leader line; callers keep ≥0.3 gap to the label and ≥0.6 length."""
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=3)


def head(x, y, r=0.5, fill=GHOST):
    """A simple person: ink-outlined head circle + shoulders, ghost fill."""
    c = Circle(radius=r, color=INK, stroke_width=5, fill_color=fill, fill_opacity=1).move_to([x, y, 0])
    sh = Polygon([x - r * 0.95, y - r * 2.0, 0], [x + r * 0.95, y - r * 2.0, 0],
                 [x + r * 0.55, y - r * 0.85, 0], [x - r * 0.55, y - r * 0.85, 0],
                 fill_color=fill, fill_opacity=1, color=INK, stroke_width=5)
    return VGroup(c, sh)


def x_mark(x, y, s=0.3, color=TERRA, w=8):
    """A terracotta X stamp."""
    return VGroup(Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w),
                  Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w))


def mini_page(x, y, w=1.15, h=0.75):
    """A small kraft-white page with one ghost text line (a review)."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.12,
                            fill_color=CARD, fill_opacity=1, color=INK, stroke_width=3).move_to([x, y, 0])
    line = Line([x - w * 0.32, y + 0.08, 0], [x + w * 0.32, y + 0.08, 0], color=GHOST, stroke_width=4)
    return VGroup(card, line)


def ghost_lines(x, y, w, n, gap=0.28, color=GHOST, sw=4):
    """n horizontal ghost text lines centred on (x, y)."""
    return VGroup(*[Line([x - w / 2, y - i * gap, 0], [x + w / 2, y - i * gap, 0],
                         color=color, stroke_width=sw) for i in range(n)])


def table_grid_v():
    """The comparison grid's verticals (drawn in one play)."""
    return VGroup(*[Line([x, -1.6, 0], [x, 1.6, 0], color=INK, stroke_width=3) for x in (-3, -1, 1, 3)])


def table_grid_h():
    """The comparison grid's horizontals (drawn in the next play: a membership change)."""
    return VGroup(*[Line([-3, y, 0], [3, y, 0], color=INK, stroke_width=3) for y in (1.6, 0.8, 0.0, -0.8, -1.6)])


def table_grid():
    """The comparison grid: 3 columns × 4 rows of ink lines (headers land separately)."""
    return VGroup(table_grid_v(), table_grid_h())


def column_headers():
    return VGroup(label("A", -2, 2.05), label("B", 0, 2.05), label("C", 2, 2.05))


# ═════════════════════════════ B00 — the three options ═════════════════════════════
class B00_ThreeOptions(Scene):
    def construct(self):
        boxes = VGroup()
        dots = []
        for ox in (-3.3, 0.0, 3.3):
            iso = Iso(ox, -1.0, 0.8)
            boxes.add(iso.box(0, 0, 0, 1.9, 1.9, 1.2))
            dots.append(iso.p(0.95, 0.95, 1.2))
        hero_dot = Dot(dots[1], radius=0.09, color=TERRA)
        labs = VGroup(label("A", -3.3, -2.05), label("B", 0.0, -2.05), label("C", 3.3, -2.05))
        leads = VGroup(*[Line([ox, -1.1, 0], [ox, -1.7, 0], color=DIM, stroke_width=3) for ox in (-3.3, 0.0, 3.3)])
        self.play(FadeIn(boxes[0]), run_time=0.5)
        self.play(FadeIn(boxes[1]), FadeIn(hero_dot), run_time=0.5)
        self.play(FadeIn(boxes[2]), run_time=0.5)
        self.play(FadeIn(leads), FadeIn(labs), run_time=0.5)
        until(self, "best for what")
        finish(self)


# ═════════════════════════════ B01 — your priorities first ═════════════════════════════
class B01_Priorities(Scene):
    def construct(self):
        h = head(-3.8, 0.2)
        you_lab = label("you", -3.8, -1.6)
        panel = RoundedRectangle(width=2.4, height=2.4, corner_radius=0.3,
                                 fill_color=CARD, fill_opacity=1, color=INK, stroke_width=5).move_to([3.6, 0.2, 0])
        spark = VGroup(*[Line([3.6 + 0.5 * np.cos(a), 0.2 + 0.5 * np.sin(a), 0],
                              [3.6 + 0.75 * np.cos(a), 0.2 + 0.75 * np.sin(a), 0],
                              color=INK, stroke_width=5) for a in np.linspace(0, 2 * np.pi, 8, endpoint=False)])
        ai_lab = label("AI", 3.6, -1.6)
        card = RoundedRectangle(width=2.0, height=1.2, corner_radius=0.2,
                                fill_color=CARD, fill_opacity=1, color=INK, stroke_width=4).move_to([-1.2, 0.2, 0])
        card_lines = ghost_lines(-1.2, 0.5, 1.4, 3, gap=0.28)
        card.add(card_lines)
        dot = Dot([-1.2, -0.2, 0], radius=0.09, color=TERRA)
        self.play(FadeIn(h), FadeIn(you_lab), FadeIn(panel), FadeIn(spark), FadeIn(ai_lab), FadeIn(card), run_time=0.6)
        self.play(card.animate.shift(RIGHT * 2.6), run_time=0.6)
        self.play(GrowFromCenter(dot.move_to([1.4, -0.2, 0])), run_time=0.4)
        until(self, "measured against")
        finish(self)


# ═════════════════════════════ B02 — ask for the table ═════════════════════════════
class B02_TheTable(Scene):
    def construct(self):
        # Grid draws in two plays (verticals, then horizontals): two membership
        # changes, so the static checker sees the shape set grow play by play.
        gv = table_grid_v()
        gh = table_grid_h()
        heads = column_headers()
        lab = label("side by side", 0, -2.35)
        self.play(Create(gv), run_time=0.6)
        self.play(Create(gh), run_time=0.6)
        self.play(FadeIn(heads), FadeIn(lab), run_time=0.5)
        until(self, "actually compare")
        finish(self)


# ═════════════════════════════ B03 — the trade-off question ═════════════════════════════
class B03_Tradeoffs(Scene):
    def construct(self):
        grid = table_grid()
        heads = column_headers()
        ring = Ellipse(width=6.4, height=1.0, color=TERRA, stroke_width=6, fill_opacity=0).move_to([0, -0.4, 0])
        ck = check(2.0, -0.4, s=0.22, color=INK, w=8)
        lab = label("trade-off", 0, -2.35)
        self.play(FadeIn(grid), FadeIn(heads), run_time=0.4)
        self.play(GrowFromCenter(ring), run_time=0.5)
        self.play(GrowFromCenter(ck), run_time=0.4)
        self.play(FadeIn(lab), run_time=0.4)
        until(self, "mind the least")
        finish(self)


# ═════════════════════════════ B04 — review funnel ═════════════════════════════
class B04_ReviewFunnel(Scene):
    def construct(self):
        pages = VGroup(*[mini_page(x, 1.7) for x in (-4.4, -2.2, 0, 2.2, 4.4)])
        funnel = VGroup(Line([-4.9, 1.25, 0], [-1.1, -0.35, 0], color=INK, stroke_width=4),
                        Line([4.9, 1.25, 0], [1.1, -0.35, 0], color=INK, stroke_width=4))
        summary = RoundedRectangle(width=2.8, height=1.5, corner_radius=0.2,
                                   fill_color=CARD, fill_opacity=1, color=INK, stroke_width=5).move_to([0, -1.15, 0])
        slines = ghost_lines(0, -0.8, 2.0, 3, gap=0.3)
        sdot = Dot([1.0, -1.5, 0], radius=0.09, color=TERRA)
        ck = check(1.75, -0.35, s=0.22, color=TERRA, w=8)
        lab = label("patterns", 0, -2.5)
        self.play(FadeIn(pages), run_time=0.5)
        self.play(Create(funnel), run_time=0.5)
        self.play(GrowFromCenter(summary), FadeIn(slines), GrowFromCenter(sdot), run_time=0.5)
        self.play(GrowFromCenter(ck), FadeIn(lab), run_time=0.4)
        until(self, "Patterns, not stars")
        finish(self)


# ═════════════════════════════ B05 — the fine print ═════════════════════════════
class B05_FinePrint(Scene):
    def construct(self):
        contract = RoundedRectangle(width=3.0, height=4.4, corner_radius=0.15,
                                    fill_color=CARD, fill_opacity=1, color=INK, stroke_width=4).move_to([-1.5, 0, 0])
        tiny = ghost_lines(-1.5, 1.6, 2.4, 12, gap=0.28, sw=3)
        ring = Ellipse(width=2.2, height=0.5, color=TERRA, stroke_width=6, fill_opacity=0).move_to([-1.5, -0.2, 0])
        glass = Circle(radius=0.7, color=INK, stroke_width=5, fill_opacity=0).move_to([-1.5, -0.2, 0])
        handle = Line([-1.0, -0.7, 0], [-0.3, -1.4, 0], color=INK, stroke_width=8)
        lab = label("the catch", -1.5, -2.7)
        self.play(FadeIn(contract), FadeIn(tiny), run_time=0.5)
        self.play(FadeIn(glass), FadeIn(handle), run_time=0.5)
        self.play(GrowFromCenter(ring), FadeIn(lab), run_time=0.5)
        until(self, "actually act on")
        finish(self)


# ═════════════════════════════ B06 — money traps by name ═════════════════════════════
class B06_MoneyTraps(Scene):
    def construct(self):
        xs = (-3.4, 0.0, 3.4)
        cards = VGroup(*[RoundedRectangle(width=2.6, height=1.4, corner_radius=0.2,
                                          fill_color=CARD, fill_opacity=1, color=INK, stroke_width=4).move_to([x, 0.5, 0])
                         for x in xs])
        clines = VGroup(*[ghost_lines(x, 0.85, 1.8, 2, gap=0.3, sw=3) for x in xs])
        labs = VGroup(label("warranty", -3.4, -0.85), label("returns", 0.0, -0.85), label("renew", 3.4, -0.85))
        marks = VGroup(*[x_mark(x, 0.5) for x in xs])
        tag = label("paragraph nine", 0, -2.2)
        self.play(FadeIn(cards), FadeIn(clines), FadeIn(labs), run_time=0.6)
        self.play(GrowFromCenter(marks[0]), GrowFromCenter(marks[1]), GrowFromCenter(marks[2]), run_time=0.6)
        self.play(FadeIn(tag), run_time=0.4)
        until(self, "paragraph nine")
        finish(self)


# ═════════════════════════════ B07 — the AI doesn't know today's price ═════════════════════════════
class B07_StalePrices(Scene):
    def construct(self):
        tag = RoundedRectangle(width=2.4, height=1.6, corner_radius=0.25,
                               fill_color=CARD, fill_opacity=1, color=INK, stroke_width=4).move_to([-3.2, 0.3, 0])
        tag_line = Line([-4.0, 0.55, 0], [-2.4, 0.55, 0], color=GHOST, stroke_width=6)
        slash = Line([-4.0, 0.55, 0], [-2.4, 0.05, 0], color=INK, stroke_width=5)
        stale_lab = label("stale", -3.2, -1.1)
        xm = x_mark(-3.2, 0.3, s=0.32)
        cur = cursor(-1.9, 0.6)
        cable = Line([-1.8, 0.3, 0], [1.8, 0.3, 0], color="#9C8462", stroke_width=6)
        live = RoundedRectangle(width=2.4, height=1.6, corner_radius=0.25,
                                fill_color=CARD, fill_opacity=1, color=INK, stroke_width=4).move_to([3.2, 0.3, 0])
        live_lab = label("live", 3.2, -1.1)
        ck = check(3.2, 0.3, s=0.24, color=INK, w=8)
        lab = label("check live", 0, -2.3)
        self.play(FadeIn(tag), FadeIn(tag_line), FadeIn(slash), FadeIn(stale_lab), FadeIn(live_lab), run_time=0.5)
        self.play(GrowFromCenter(xm), run_time=0.4)
        self.play(FadeIn(cur), run_time=0.3)
        self.play(Create(cable), FadeIn(live), run_time=0.5)
        self.play(cur.animate.shift(RIGHT * 5.0), run_time=0.4)
        self.play(GrowFromCenter(ck), FadeIn(lab), run_time=0.4)
        until(self, "every time")
        finish(self)


# ═════════════════════════════ B08 — the method card ═════════════════════════════
class B08_TheMethod(Scene):
    def construct(self):
        ys = (1.1, -0.1, -1.3)
        plates = VGroup(*[RoundedRectangle(width=3.6, height=1.0, corner_radius=0.2,
                                           fill_color=CARD, fill_opacity=1, color=INK, stroke_width=4).move_to([-1.2, y, 0])
                          for y in ys])
        labs = VGroup(label("1  priorities", 2.1, 1.1), label("2  table", 2.1, -0.1), label("3  fine print", 2.1, -1.3))
        cks = VGroup(*[check(0.15, y, s=0.2, color=TERRA, w=7) for y in ys])
        h = head(-1.2, 2.35, r=0.4)
        hlab = label("you decide", 1.9, 2.55)
        hlead = leader(-0.75, 1.15, 2.55)
        self.play(FadeIn(plates), FadeIn(labs), run_time=0.6)
        self.play(GrowFromCenter(cks[0]), GrowFromCenter(cks[1]), GrowFromCenter(cks[2]), run_time=0.5)
        self.play(FadeIn(h), FadeIn(hlead), FadeIn(hlab), run_time=0.4)
        until(self, "the whole co-pilot")
        finish(self)
