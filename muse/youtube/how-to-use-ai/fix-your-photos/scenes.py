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
fix-your-photos — scenes.py (show-tell).

The iso_kit.py block (top of file) is pasted verbatim from
brutalist.art/skills/make/show-tell/templates/iso_kit.py — Gate A copies only
scenes.py, so the kit must live here, not be imported.

Cast for the whole film (continuity with the companion film ai-that-sees):
the kraft photo card with the ink hills motif, the dark ink person figures
("us" in front, the photobomber behind), the dashed terracotta eraser ring,
the kraft fill patch where the AI invented the background, the dim overlay,
the terracotta sun, the ink crop frame, the magnifier, the grey printer, and
the terracotta check / ink X pair. Every scene: all motion lands in the first
~40% of the beat (fully opaque, nothing half-done at the midpoint GATE T
samples), then `until()` holds on a settled labelled frame and `finish()`
pads to the audio.
"""


# ═════════════════════════════ local helpers ═════════════════════════════
def label(text, x, y, size=40):
    return T(text, size=size, color=INK).move_to([x, y, 0])


def leader(x0, x1, y, color=DIM):
    """A short dim leader line; callers keep ≥0.3 gap to the label."""
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=3)


def photo_card(x, y, w, h, motif="hills"):
    """A kraft photo card — the film's hero object, shared with the companion film. Motifs drawn in ink."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color=BOX_TOP, fill_opacity=1, color=INK, stroke_width=5).move_to([x, y, 0])
    g = VGroup(card)
    sun = Dot([x + w * 0.28, y + h * 0.26, 0], radius=0.13, color=TERRA)
    hill1 = Polygon([x - w * 0.42, y - h * 0.30, 0], [x - w * 0.05, y + h * 0.05, 0],
                    [x + w * 0.28, y - h * 0.30, 0],
                    fill_color=INK, fill_opacity=1, stroke_width=0)
    hill2 = Polygon([x - w * 0.05, y - h * 0.30, 0], [x + w * 0.22, y - h * 0.02, 0],
                    [x + w * 0.42, y - h * 0.30, 0],
                    fill_color=INK, fill_opacity=0.35, stroke_width=0)
    g.add(sun, hill1, hill2)
    return g


def person(x, y, s=1.0):
    """A dark ink person silhouette (head + shoulders). y is the ground line."""
    head = Circle(radius=0.22 * s, color=INK, stroke_width=0,
                  fill_color=INK, fill_opacity=1).move_to([x, y + 0.60 * s, 0])
    body = RoundedRectangle(width=0.52 * s, height=0.72 * s, corner_radius=0.16 * s,
                            color=INK, stroke_width=0,
                            fill_color=INK, fill_opacity=1).move_to([x, y + 0.16 * s, 0])
    return VGroup(head, body)


def eraser_ring(x, y, r=0.7):
    """The dashed terracotta eraser selection ring. Callers Create() it fully opaque, early in the beat."""
    return DashedVMobject(Circle(radius=r, color=TERRA, stroke_width=5).move_to([x, y, 0]),
                          num_dashes=20)


def fill_patch(x, y, w, h):
    """The kraft patch where the AI painted in the background. Grows in after the eraser."""
    return RoundedRectangle(width=w, height=h, corner_radius=0.15,
                            fill_color=GHOST, fill_opacity=1, color=INK, stroke_width=3).move_to([x, y, 0])


def dim_overlay(x, y, w, h):
    """The dim filter over a dark photo: fully translucent, no stroke."""
    return RoundedRectangle(width=w - 0.08, height=h - 0.08, corner_radius=0.14,
                            fill_color=DIM, fill_opacity=0.45, stroke_width=0).move_to([x, y, 0])


def crop_frame(cx, cy, w, h):
    """An ink crop frame, no fill."""
    return RoundedRectangle(width=w, height=h, corner_radius=0.1,
                            color=INK, stroke_width=6, fill_opacity=0).move_to([cx, cy, 0])


def magnifier(x, y, r=1.0):
    """The zoom-in lens: ink ring + ink handle. A new shape."""
    ring = Circle(radius=r, color=INK, stroke_width=6, fill_opacity=0).move_to([x, y, 0])
    handle = Line([x + r * 0.72, y - r * 0.72, 0], [x + r * 1.45, y - r * 1.45, 0], color=INK, stroke_width=6)
    return VGroup(ring, handle)


def doc_card(x, y, w=2.4, h=2.8):
    """An official document: white card, ghost lines, one ink seal dot. What you do NOT edit."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color="#FFFFFF", fill_opacity=1, color=INK, stroke_width=5).move_to([x, y, 0])
    lines = VGroup(*[Line([x - w * 0.32, y + h * 0.30 - i * 0.42, 0],
                          [x + w * 0.32 - (i % 2) * 0.5, y + h * 0.30 - i * 0.42, 0],
                          color=GHOST, stroke_width=5) for i in range(4)])
    seal = Dot([x + w * 0.24, y - h * 0.30, 0], radius=0.14, color=TERRA)
    return VGroup(body, lines, seal)


def printer(x, y):
    """A grey office printer: body, dark slot. Returns (body, slot) — the page is drawn by the scene."""
    body = RoundedRectangle(width=4.6, height=1.5, corner_radius=0.25,
                            fill_color=BAR1, fill_opacity=1, color=INK, stroke_width=5).move_to([x, y, 0])
    slot = RoundedRectangle(width=3.6, height=0.28, corner_radius=0.1,
                            fill_color=DARK_R, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
    return VGroup(body, slot)


def print_page(x, y, w=2.8, h=2.2):
    """The printed photo: white page with the fixed hills motif."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.1,
                            fill_color="#FFFFFF", fill_opacity=1, color=INK, stroke_width=4).move_to([x, y, 0])
    sun = Dot([x + w * 0.24, y + h * 0.24, 0], radius=0.10, color=TERRA)
    hill = Polygon([x - w * 0.36, y - h * 0.30, 0], [x - w * 0.04, y + h * 0.02, 0],
                   [x + w * 0.28, y - h * 0.30, 0],
                   fill_color=INK, fill_opacity=1, stroke_width=0)
    return VGroup(body, sun, hill)


def xmark(x, y, s=0.35, color=INK, w=8):
    return VGroup(Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w),
                  Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w))


# ═════════════════════════════ B00 — the photo with the photobomber ═════════════════════════════
class B00_PhotoHero(Scene):
    def construct(self):
        ph = photo_card(0, 0.2, 4.6, 3.4, "hills")
        us1 = person(-1.15, -0.75, 0.8)
        us2 = person(0.05, -0.75, 0.85)
        bomber = person(1.55, -0.70, 0.55)
        self.play(FadeIn(ph), FadeIn(us1), FadeIn(us2), FadeIn(bomber), run_time=0.7)
        lab = label("photobomber", 3.95, -1.6)
        lead = leader(2.55, 3.1, -1.6)
        self.play(FadeIn(lead), FadeIn(lab), run_time=0.5)
        until(self, "Today you fix it")
        finish(self)


# ═════════════════════════════ B01 — see vs change (the companion nod) ═════════════════════════════
class B01_Companion(Scene):
    def construct(self):
        see = photo_card(-3.0, 0.2, 2.6, 2.2, "hills")
        see_lab = label("see", -3.0, -1.35)
        chg = photo_card(3.0, 0.2, 2.6, 2.2, "hills")
        chg_lab = label("change", 3.0, -1.35)
        self.play(FadeIn(see), FadeIn(see_lab), FadeIn(chg), FadeIn(chg_lab), run_time=0.7)
        ring = eraser_ring(3.3, 0.5, 0.65)
        self.play(Create(ring), run_time=0.5)
        ck = check(3.0, 1.7, s=0.26, color=TERRA, w=8)
        self.play(GrowFromCenter(ck), run_time=0.5)
        until(self, "changing the photo")
        finish(self)


# ═════════════════════════════ B02 — remove the photobomber ═════════════════════════════
class B02_Remove(Scene):
    def construct(self):
        ph = photo_card(-0.2, 0.2, 4.2, 3.2, "hills")
        bomber = person(1.15, -0.75, 0.55)
        self.play(FadeIn(ph), FadeIn(bomber), run_time=0.6)
        ring = eraser_ring(1.15, -0.45, 0.72)
        self.play(Create(ring), run_time=0.5)
        patch = fill_patch(1.15, -0.55, 1.5, 1.5)
        lab = label("gone", 3.7, -1.55)
        lead = leader(2.35, 2.9, -1.55)
        self.play(FadeOut(bomber), GrowFromCenter(patch), FadeIn(lead), FadeIn(lab), run_time=0.7)
        until(self, "paints in")
        finish(self)


# ═════════════════════════════ B03 — the invented fill ═════════════════════════════
class B03_Invent(Scene):
    def construct(self):
        ph = photo_card(-0.2, 0.2, 4.2, 3.2, "hills")
        patch = fill_patch(1.15, -0.55, 1.5, 1.5)
        self.play(FadeIn(ph), FadeIn(patch), run_time=0.7)
        outline = DashedVMobject(Circle(radius=1.0, color=TERRA, stroke_width=5).move_to([1.15, -0.55, 0]),
                                 num_dashes=24)
        self.play(Create(outline), run_time=0.5)
        lab = label("invented", 3.85, -1.35)
        lead = leader(2.25, 2.95, -1.35)
        self.play(FadeIn(lead), FadeIn(lab), run_time=0.4)
        until(self, "can't see")
        finish(self)


# ═════════════════════════════ B04 — fix the lighting ═════════════════════════════
class B04_Light(Scene):
    def construct(self):
        dk = photo_card(-3.0, 0.2, 2.8, 2.6, "hills")
        dk_lab = label("dark", -3.0, -1.6)
        dim = dim_overlay(-3.0, 0.2, 2.8, 2.6)
        br = photo_card(2.9, 0.2, 2.8, 2.6, "hills")
        br_lab = label("bright", 2.9, -1.6)
        self.play(FadeIn(dk), FadeIn(dk_lab), FadeIn(dim), FadeIn(br), FadeIn(br_lab), run_time=0.7)
        arrow = Arrow([-1.35, 0.2, 0], [1.25, 0.2, 0], color=INK, stroke_width=7, buff=0.05)
        self.play(GrowFromCenter(arrow), run_time=0.5)
        sun = Dot([3.65, 0.95, 0], radius=0.17, color=TERRA)
        ck = check(2.9, 1.75, s=0.26, color=TERRA, w=8)
        self.play(GrowFromCenter(sun), GrowFromCenter(ck), run_time=0.5)
        until(self, "slider math")
        finish(self)


# ═════════════════════════════ B05 — straighten and crop ═════════════════════════════
class B05_Straighten(Scene):
    def construct(self):
        ph = photo_card(0, 0.1, 4.6, 3.0, "hills")
        tilt = Line([-2.0, -0.35, 0], [2.0, 0.35, 0], color=INK, stroke_width=6)
        self.play(FadeIn(ph), FadeIn(tilt), run_time=0.7)
        frame = crop_frame(0, 0.1, 4.6, 3.0)
        self.play(Create(frame), run_time=0.5)
        level = Line([-2.0, 0.1, 0], [2.0, 0.1, 0], color=INK, stroke_width=6)
        lab = label("level", -3.85, -1.9)
        lead = leader(-2.6, -3.2, -1.9)
        self.play(FadeOut(tilt), FadeIn(level), FadeIn(lead), FadeIn(lab), run_time=0.6)
        until(self, "level horizon")
        finish(self)


# ═════════════════════════════ B06 — edit a copy ═════════════════════════════
class B06_Copy(Scene):
    def construct(self):
        orig = photo_card(-2.9, 0.2, 2.6, 2.6, "hills")
        orig_lab = label("original", -2.9, -1.6)
        cp = photo_card(2.9, 0.2, 2.6, 2.6, "hills")
        cp_lab = label("copy", 2.9, -1.6)
        self.play(FadeIn(orig), FadeIn(orig_lab), FadeIn(cp), FadeIn(cp_lab), run_time=0.7)
        ring = eraser_ring(3.2, 0.5, 0.6)
        self.play(Create(ring), run_time=0.5)
        ck = check(2.9, 1.8, s=0.26, color=TERRA, w=8)
        self.play(GrowFromCenter(ck), run_time=0.5)
        until(self, "can't be undone")
        finish(self)


# ═════════════════════════════ B07 — check the fix ═════════════════════════════
class B07_Check(Scene):
    def construct(self):
        ph = photo_card(-0.6, 0.1, 4.0, 3.0, "hills")
        patch = fill_patch(1.0, -0.5, 1.4, 1.4)
        self.play(FadeIn(ph), FadeIn(patch), run_time=0.7)
        mag = magnifier(1.0, -0.5, r=1.0)
        self.play(GrowFromCenter(mag), run_time=0.6)
        lab = label("look", 3.9, 1.0)
        lead = leader(2.75, 3.3, 1.0)
        self.play(FadeIn(lead), FadeIn(lab), run_time=0.4)
        until(self, "circle more tightly")
        finish(self)


# ═════════════════════════════ B08 — an edited photo is a made thing ═════════════════════════════
class B08_MadeThing(Scene):
    def construct(self):
        alb = photo_card(-2.9, 0.2, 2.6, 2.6, "hills")
        alb_lab = label("album", -2.9, -1.55)
        doc = doc_card(2.9, 0.2, 2.4, 2.8)
        doc_lab = label("ID", 2.9, -1.7)
        self.play(FadeIn(alb), FadeIn(alb_lab), FadeIn(doc), FadeIn(doc_lab), run_time=0.7)
        ck = check(-2.9, 1.8, s=0.26, color=TERRA, w=8)
        self.play(GrowFromCenter(ck), run_time=0.5)
        xm = xmark(2.9, 0.2, s=0.45, color=INK, w=9)
        self.play(GrowFromCenter(xm), run_time=0.5)
        until(self, "anything official")
        finish(self)


# ═════════════════════════════ B09 — then print ═════════════════════════════
class B09_Print(Scene):
    def construct(self):
        pr = printer(0, -0.5)
        self.play(FadeIn(pr), run_time=0.7)
        page = print_page(0, -1.75)
        self.play(GrowFromCenter(page), run_time=0.8)
        lab = label("print", 3.5, -1.9)
        lead = leader(2.25, 2.85, -1.9)
        self.play(FadeIn(lead), FadeIn(lab), run_time=0.4)
        until(self, "that one file")
        finish(self)
