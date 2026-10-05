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
ai-that-sees — scenes.py (show-tell).

The iso_kit.py block (top of file) is pasted verbatim from
brutalist.art/skills/make/show-tell/templates/iso_kit.py — Gate A copies only
scenes.py, so the kit must live here, not be imported.

Cast for the whole film: the kraft photo card (ink motifs: hills, leaf,
receipt), the AI eye (ink almond, ink iris, one terracotta pupil spark), the
plus attach button, the terracotta scan line, the chat window, and the white
answer page. Every scene: all motion lands in the first ~40% of the beat
(fully opaque, nothing half-done at the midpoint GATE T samples), then
`until()` holds on a settled labelled frame and `finish()` pads to the audio.
"""


# ═════════════════════════════ local helpers ═════════════════════════════
def label(text, x, y, size=40):
    return T(text, size=size, color=INK).move_to([x, y, 0])


def leader(x0, x1, y, color=DIM):
    """A short dim leader line; callers keep ≥0.3 gap to the label."""
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=3)


def eye(x, y, s=1.0):
    """The AI's eye: ink almond, ink iris, one terracotta pupil spark. The film's vision motif."""
    almond = Ellipse(width=1.9 * s, height=1.05 * s, color=INK, stroke_width=5,
                     fill_color=CARD, fill_opacity=1).move_to([x, y, 0])
    iris = Circle(radius=0.30 * s, color=INK, stroke_width=0,
                  fill_color=INK, fill_opacity=1).move_to([x, y, 0])
    spark = Dot([x, y, 0], radius=0.11 * s, color=TERRA)
    return VGroup(almond, iris, spark)


def photo_card(x, y, w, h, motif="hills"):
    """A kraft photo card — the film's hero object. Motifs are drawn in ink."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color=BOX_TOP, fill_opacity=1, color=INK, stroke_width=5).move_to([x, y, 0])
    g = VGroup(card)
    if motif == "hills":
        sun = Dot([x + w * 0.28, y + h * 0.24, 0], radius=0.13, color=TERRA)
        hill1 = Polygon([x - w * 0.38, y - h * 0.30, 0], [x - w * 0.05, y + h * 0.05, 0],
                        [x + w * 0.28, y - h * 0.30, 0],
                        fill_color=INK, fill_opacity=1, stroke_width=0)
        hill2 = Polygon([x - w * 0.05, y - h * 0.30, 0], [x + w * 0.22, y - h * 0.02, 0],
                        [x + w * 0.42, y - h * 0.30, 0],
                        fill_color=INK, fill_opacity=0.35, stroke_width=0)
        g.add(sun, hill1, hill2)
    elif motif == "leaf":
        stem = Line([x, y - h * 0.32, 0], [x, y + h * 0.10, 0], color=INK, stroke_width=6)
        leaf = Polygon([x, y + h * 0.34, 0], [x + w * 0.26, y + h * 0.12, 0],
                       [x, y - h * 0.06, 0], [x - w * 0.26, y + h * 0.12, 0],
                       fill_color=CARD, fill_opacity=1, color=INK, stroke_width=5)
        spots = VGroup(*[Dot([x + dx, y + dy, 0], radius=0.055, color=INK)
                         for dx, dy in ((0.06, 0.18), (-0.08, 0.08), (0.02, -0.01))])
        g.add(stem, leaf, spots)
    elif motif == "receipt":
        lines = VGroup(*[Line([x - w * 0.32, y + h * 0.30 - i * h * 0.13, 0],
                              [x + w * 0.30 - (i % 2) * w * 0.12, y + h * 0.30 - i * h * 0.13, 0],
                              color=GHOST, stroke_width=5) for i in range(5)])
        total = Line([x - w * 0.32, y - h * 0.32, 0], [x + w * 0.18, y - h * 0.32, 0],
                     color=INK, stroke_width=6)
        g.add(lines, total)
    return g


def plus_button(x, y, r=0.42):
    """The attach button: cream circle, ink ring, ink plus. Generic — paperclip or plus."""
    fill = Circle(radius=r, fill_color=CARD, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
    ring = Circle(radius=r, color=INK, stroke_width=5).move_to([x, y, 0])
    plus = VGroup(Line([x - r * 0.5, y, 0], [x + r * 0.5, y, 0], color=INK, stroke_width=7),
                  Line([x, y - r * 0.5, 0], [x, y + r * 0.5, 0], color=INK, stroke_width=7))
    return VGroup(fill, ring, plus)


def scan_line(x0, x1, y):
    """The terracotta scan line. Callers sweep it fully opaque and let it rest
    before the midpoint GATE T samples."""
    return Line([x0, y, 0], [x1, y, 0], color=TERRA, stroke_width=7)


def chat_window(x, y, w=5.6, h=3.0):
    """A message composer: cream card, ink outline, grey (BAR1) title band."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.25,
                            fill_color=CARD, fill_opacity=1, color=INK, stroke_width=5).move_to([x, y, 0])
    band = RoundedRectangle(width=w - 0.06, height=0.55, corner_radius=0.18,
                            fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([x, y + h / 2 - 0.32, 0])
    return VGroup(body, band)


def answer_page(x, y, w=2.4, h=2.6, rows=3):
    """The AI's written answer: white card, ghost lines, one terracotta dot."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color="#FFFFFF", fill_opacity=1, color=INK, stroke_width=5).move_to([x, y, 0])
    ls = VGroup(*[Line([x - w * 0.34, y + h * 0.30 - i * 0.45, 0],
                       [x + w * 0.34 - (i % 2) * 0.4, y + h * 0.30 - i * 0.45, 0],
                       color=GHOST, stroke_width=5) for i in range(rows)])
    dot = Dot([x - w * 0.34, y - h * 0.30, 0], radius=0.09, color=TERRA)
    return VGroup(body, ls, dot)


def error_dialog(x, y, w=4.2, h=2.6):
    """An unreadable error dialog: dim body, grey band, ink X, garbled ink lines."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.25,
                            fill_color=DIM, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
    band = RoundedRectangle(width=w - 0.06, height=0.5, corner_radius=0.18,
                            fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([x, y + h / 2 - 0.30, 0])
    xg = VGroup(Line([x + w / 2 - 0.60, y + h / 2 - 0.60, 0], [x + w / 2 - 0.28, y + h / 2 - 0.28, 0],
                     color=CARD, stroke_width=6),
                Line([x + w / 2 - 0.60, y + h / 2 - 0.28, 0], [x + w / 2 - 0.28, y + h / 2 - 0.60, 0],
                     color=CARD, stroke_width=6))
    lines = VGroup(*[Line([x - w * 0.36, y + 0.45 - i * 0.42, 0],
                          [x + w * 0.30 - (i % 2) * w * 0.14, y + 0.45 - i * 0.42, 0],
                          color=INK, stroke_width=5) for i in range(3)])
    warn = Dot([x - w * 0.36, y - 0.75, 0], radius=0.12, color=TERRA)
    return VGroup(body, band, xg, lines, warn)


def form_card(x, y, w=3.6, h=3.0, rows=4):
    """A paper form: white card, ink boxes, ghost lines. Returns (group, row_ys)."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color="#FFFFFF", fill_opacity=1, color=INK, stroke_width=5).move_to([x, y, 0])
    rs, rys = [], []
    for i in range(rows):
        ry = y + h * 0.32 - i * (h * 0.64 / (rows - 1))
        rys.append(ry)
        box = Rectangle(width=0.4, height=0.32, color=INK, stroke_width=4,
                        fill_opacity=0).move_to([x - w * 0.32, ry, 0])
        ln = Line([x - w * 0.10, ry, 0], [x + w * 0.32, ry, 0], color=GHOST, stroke_width=5)
        rs.append(VGroup(box, ln))
    return VGroup(body, *rs), rys


def id_card(x, y, w=2.6, h=3.4):
    """An ID document: card, ghost face, ghost lines. What you do NOT attach."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color=CARD, fill_opacity=1, color=INK, stroke_width=5).move_to([x, y, 0])
    face = Circle(radius=0.42, color=INK, stroke_width=5,
                  fill_color=GHOST, fill_opacity=1).move_to([x, y + 0.75, 0])
    lines = VGroup(*[Line([x - w * 0.32, y - 0.35 - i * 0.4, 0],
                          [x + w * 0.32 - (i % 2) * 0.5, y - 0.35 - i * 0.4, 0],
                          color=GHOST, stroke_width=5) for i in range(3)])
    return VGroup(body, face, lines)


def scribble(x, y, w, phase=0.0):
    """One wavy handwriting-ish line (clearly not text: a smooth sine)."""
    xs = np.linspace(-w / 2, w / 2, 24)
    pts = [np.array([x + t, y + 0.14 * np.sin(2.2 * t / w * 6.28 + phase), 0.0]) for t in xs]
    vm = VMobject()
    vm.set_points_as_corners(pts)
    vm.set_stroke(color=INK, width=5)
    return vm


def crop_frame(cx, cy, w, h):
    """An ink crop frame, no fill."""
    return RoundedRectangle(width=w, height=h, corner_radius=0.1,
                            color=INK, stroke_width=6, fill_opacity=0).move_to([cx, cy, 0])


def busy_card(x, y, w=4.6, h=3.0):
    """A busy kraft photo: assorted dim shapes plus one ink tile (the thing that
    matters). Returns (group, (tile_x, tile_y))."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color=BOX_TOP, fill_opacity=1, color=INK, stroke_width=5).move_to([x, y, 0])
    rng = np.random.default_rng(7)
    bits = []
    for _ in range(9):
        bx = x + rng.uniform(-w / 2 + 0.4, w / 2 - 0.4)
        by = y + rng.uniform(-h / 2 + 0.4, h / 2 - 0.4)
        if rng.random() < 0.5:
            bits.append(Circle(radius=0.14, color=DIM, stroke_width=4,
                               fill_opacity=0).move_to([bx, by, 0]))
        else:
            bits.append(Rectangle(width=0.34, height=0.26, color=GHOST, stroke_width=0,
                                  fill_color=GHOST, fill_opacity=1).move_to([bx, by, 0]))
    tx, ty = x + w * 0.28, y - h * 0.22
    target = Rectangle(width=0.5, height=0.5, color=INK, stroke_width=5,
                       fill_color=INK, fill_opacity=0.25).move_to([tx, ty, 0])
    return VGroup(card, VGroup(*bits), target), (tx, ty)


def swatch(x, y, fill):
    return RoundedRectangle(width=1.9, height=2.3, corner_radius=0.18,
                            fill_color=fill, fill_opacity=1, color=INK, stroke_width=5).move_to([x, y, 0])


def xmark(x, y, s=0.35, color=INK, w=8):
    return VGroup(Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w),
                  Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w))


# ═════════════════════════════ B00 — the move itself ═════════════════════════════
class B00_PhotoHero(Scene):
    def construct(self):
        win = chat_window(-0.4, 0.1)
        pb = plus_button(-1.9, -0.55)
        self.play(FadeIn(win), FadeIn(pb), run_time=0.7)
        ph = photo_card(-1.9, 0.45, 2.0, 1.7, "hills")
        self.play(GrowFromCenter(ph), run_time=0.6)
        lab = label("photo", 3.95, 0.55)
        lead = leader(2.6, 3.2, 0.55)
        self.play(FadeIn(lead), FadeIn(lab), run_time=0.5)
        until(self, "Same paperclip")
        finish(self)


# ═════════════════════════════ B01 — how vision works ═════════════════════════════
class B01_HowVision(Scene):
    def construct(self):
        ph = photo_card(-3.0, 0.2, 2.6, 2.2, "hills")
        lab = label("scan", -3.0, -1.6)
        e = eye(2.8, 0.4)
        self.play(FadeIn(ph), FadeIn(lab), FadeIn(e), run_time=0.7)
        sl = scan_line(-4.1, -1.9, 1.0)
        self.play(FadeIn(sl), run_time=0.3)
        self.play(sl.animate.shift(DOWN * 1.8), run_time=0.7)
        ap = answer_page(2.8, -1.5, 2.3, 1.9)
        self.play(GrowFromCenter(ap), run_time=0.6)
        until(self, "top to bottom")
        finish(self)


# ═════════════════════════════ B02 — the error message ═════════════════════════════
class B02_ErrorShot(Scene):
    def construct(self):
        dlg = error_dialog(-1.6, 0.3)
        lab = label("error", -1.6, -1.75)
        self.play(FadeIn(dlg), FadeIn(lab), run_time=0.7)
        e = eye(3.2, 1.2)
        self.play(FadeIn(e), run_time=0.5)
        sl = scan_line(-3.5, 0.3, 1.2)
        self.play(FadeIn(sl), run_time=0.3)
        self.play(sl.animate.shift(DOWN * 1.7), run_time=0.7)
        ap = answer_page(3.2, -1.35, 2.3, 1.9)
        self.play(GrowFromCenter(ap), run_time=0.6)
        until(self, "plain language")
        finish(self)


# ═════════════════════════════ B03 — receipts ═════════════════════════════
class B03_Receipt(Scene):
    def construct(self):
        rc = photo_card(-2.9, 0.0, 2.0, 3.0, "receipt")
        lab = label("receipt", -2.9, -2.0)
        self.play(FadeIn(rc), FadeIn(lab), run_time=0.7)
        sl = scan_line(-3.8, -2.0, 1.3)
        self.play(FadeIn(sl), run_time=0.3)
        self.play(sl.animate.shift(DOWN * 2.4), run_time=0.7)
        ap = answer_page(2.4, 0.0, 2.6, 2.6)
        self.play(GrowFromCenter(ap), run_time=0.6)
        until(self, "hands you the numbers")
        finish(self)


# ═════════════════════════════ B04 — the sick plant ═════════════════════════════
class B04_Plant(Scene):
    def construct(self):
        pc = photo_card(-2.9, 0.2, 2.6, 2.6, "leaf")
        lab = label("plant", -2.9, -1.75)
        e = eye(2.9, 0.9)
        self.play(FadeIn(pc), FadeIn(lab), FadeIn(e), run_time=0.7)
        sl = scan_line(-4.0, -1.8, 1.3)
        self.play(FadeIn(sl), run_time=0.3)
        self.play(sl.animate.shift(DOWN * 2.0), run_time=0.7)
        ap = answer_page(2.9, -1.45, 2.3, 1.9)
        self.play(GrowFromCenter(ap), run_time=0.6)
        until(self, "what it needs")
        finish(self)


# ═════════════════════════════ B05 — forms ═════════════════════════════
class B05_Form(Scene):
    def construct(self):
        fc, rys = form_card(-2.6, 0.1)
        lab = label("form", -2.6, -1.85)
        self.play(FadeIn(fc), FadeIn(lab), run_time=0.7)
        band = RoundedRectangle(width=3.1, height=0.55, corner_radius=0.12,
                                fill_color=GHOST, fill_opacity=0.9, color=DIM, stroke_width=3)
        band.move_to([-2.6, rys[0], 0])
        self.play(FadeIn(band), run_time=0.4)
        self.play(band.animate.shift(DOWN * (rys[0] - rys[1])), run_time=0.4)
        self.play(band.animate.shift(DOWN * (rys[1] - rys[2])), run_time=0.4)
        ap = answer_page(2.9, 0.1, 2.3, 2.2)
        self.play(GrowFromCenter(ap), run_time=0.6)
        until(self, "row by row")
        finish(self)


# ═════════════════════════════ B06 — which one ═════════════════════════════
class B06_WhichOne(Scene):
    def construct(self):
        s1 = swatch(-2.2, -0.1, BOX_L)
        s2 = swatch(0.4, -0.1, BAR1)
        lab = label("which one", -0.9, -1.9)
        e = eye(-0.9, 1.9, s=0.85)
        self.play(FadeIn(s1), FadeIn(s2), FadeIn(lab), FadeIn(e), run_time=0.7)
        ck = check(0.4, 1.35, s=0.28, color=TERRA, w=8)
        self.play(GrowFromCenter(ck), run_time=0.5)
        until(self, "says why")
        finish(self)


# ═════════════════════════════ B07 — handwriting ═════════════════════════════
class B07_Handwriting(Scene):
    def construct(self):
        wb = RoundedRectangle(width=3.8, height=2.8, corner_radius=0.18,
                              fill_color="#FFFFFF", fill_opacity=1, color=INK, stroke_width=5).move_to([-2.8, 0.1, 0])
        lab = label("notes", -2.8, -1.8)
        self.play(FadeIn(wb), FadeIn(lab), run_time=0.7)
        s1 = scribble(-2.8, 0.75, 2.8, 0.0)
        s2 = scribble(-2.8, 0.15, 2.4, 2.1)
        s3 = scribble(-2.8, -0.45, 2.6, 4.2)
        self.play(Create(s1), Create(s2), Create(s3), run_time=0.8)
        arrow = Arrow([-0.6, 0.1, 0], [0.9, 0.1, 0], color=INK, stroke_width=7, buff=0.05)
        pg = answer_page(2.9, 0.1, 2.6, 2.6)
        self.play(GrowFromCenter(arrow), GrowFromCenter(pg), run_time=0.6)
        until(self, "clean text")
        finish(self)


# ═════════════════════════════ B08 — one clear photo ═════════════════════════════
class B08_ClearPhoto(Scene):
    def construct(self):
        bl = RoundedRectangle(width=2.4, height=2.9, corner_radius=0.18,
                              fill_color=DIM, fill_opacity=1, stroke_width=0).move_to([-2.6, 0.1, 0])
        blobs = VGroup(*[Dot([-2.6 + dx, 0.1 + dy, 0], radius=0.3, color=GHOST, fill_opacity=0.55)
                         for dx, dy in ((-0.45, 0.55), (0.4, -0.25), (0.05, -0.65))])
        bl_lab = label("blurry", -2.6, -1.85)
        cr = photo_card(2.6, 0.1, 2.4, 2.9, "hills")
        cr_lab = label("clear", 2.6, -1.85)
        self.play(FadeIn(bl), FadeIn(blobs), FadeIn(bl_lab), FadeIn(cr), FadeIn(cr_lab), run_time=0.7)
        ck = check(2.6, 1.75, s=0.28, color=TERRA, w=8)
        self.play(GrowFromCenter(ck), run_time=0.5)
        until(self, "the camera caught")
        finish(self)


# ═════════════════════════════ B09 — point at it ═════════════════════════════
class B09_PointIt(Scene):
    def construct(self):
        card, (tx, ty) = busy_card(-1.2, 0.1)
        self.play(FadeIn(card), run_time=0.7)
        frame = crop_frame(-1.2, 0.1, 4.6, 3.0)
        self.play(Create(frame), run_time=0.5)
        self.play(frame.animate.scale(0.30).move_to([tx, ty, 0]), run_time=0.6)
        lead = Line([tx + 0.40, ty - 0.15, 0], [2.3, -1.4, 0], color=DIM, stroke_width=3)
        lab = label("this one", 3.45, -1.4)
        self.play(FadeIn(lead), FadeIn(lab), run_time=0.5)
        until(self, "yours would go to")
        finish(self)


# ═════════════════════════════ B10 — say what you want ═════════════════════════════
class B10_SayWhat(Scene):
    def construct(self):
        ph = photo_card(-2.9, 0.1, 2.8, 2.4, "hills")
        self.play(FadeIn(ph), run_time=0.7)
        qbody = RoundedRectangle(width=2.6, height=2.2, corner_radius=0.18,
                                 fill_color="#FFFFFF", fill_opacity=1, color=INK, stroke_width=5).move_to([2.9, 0.35, 0])
        qlines = VGroup(*[Line([2.9 - 0.95, 0.35 + 0.55 - i * 0.5, 0],
                               [2.9 + 0.95 - (i % 2) * 0.5, 0.35 + 0.55 - i * 0.5, 0],
                               color=INK, stroke_width=5) for i in range(3)])
        self.play(FadeIn(qbody), run_time=0.5)
        self.play(Create(qlines[0]), Create(qlines[1]), Create(qlines[2]), run_time=0.7)
        arrow = Arrow([1.4, 0.1, 0], [-1.3, 0.1, 0], color=INK, stroke_width=7, buff=0.05)
        self.play(GrowFromCenter(arrow), run_time=0.5)
        lab = label("the question", 2.9, -1.9)
        self.play(FadeIn(lab), run_time=0.4)
        until(self, "your words are the question")
        finish(self)


# ═════════════════════════════ B11 — what not to share ═════════════════════════════
class B11_KeepItPrivate(Scene):
    def construct(self):
        rc = photo_card(-2.9, 0.2, 2.0, 2.6, "receipt")
        rc_lab = label("receipt", -2.9, -1.55)
        idc = id_card(2.4, 0.2)
        id_lab = label("ID", 2.4, -1.95)
        self.play(FadeIn(rc), FadeIn(rc_lab), FadeIn(idc), FadeIn(id_lab), run_time=0.7)
        ck = check(-2.9, 1.75, s=0.28, color=TERRA, w=8)
        self.play(GrowFromCenter(ck), run_time=0.5)
        xm = xmark(2.4, 0.2, s=0.45, color=INK, w=9)
        self.play(GrowFromCenter(xm), run_time=0.5)
        until(self, "do not attach it")
        finish(self)
