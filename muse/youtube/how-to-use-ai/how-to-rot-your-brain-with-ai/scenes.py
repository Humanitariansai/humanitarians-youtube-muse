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
scenes.py — show-tell Manim scenes for "How to outsource everything to AI & get dumb".

The iso_kit block above is pasted verbatim from
brutalist.art/skills/make/show-tell/templates/iso_kit.py (never imported: Gate A
copies only this file). Below it, the film's own cast and ten body-beat scenes.

Cast (same objects, whole film): the worker (kraft body, head, glowing brain),
the dark AI box with its terracotta spark, iso pages, a pencil, and small
segment gauges. Labels sit beside objects, never inside outlines; text floor 32;
every explicit coordinate inside ±6.2 x ±3.3. Each scene adds at least one new
non-text shape after its first frame (Gate A).
"""

# ═════════════════════ film cast: how-to-rot-your-brain-with-ai ═════════════════════
def lab(text, x, y, size=36):
    return T(text, size=size).move_to([x, y, 0])


def floor_shadow(cx, w=6.0):
    return Ellipse(width=w, height=0.45, fill_color=GHOST, fill_opacity=0.9,
                   stroke_width=0).move_to([cx, -2.78, 0])


def spark4(x, y, r=0.22):
    pts = []
    for k in range(8):
        rr = r if k % 2 == 0 else r * 0.34
        a = k * np.pi / 4 + np.pi / 8
        pts.append([x + rr * np.cos(a), y + rr * np.sin(a), 0])
    return Polygon(*pts, fill_color=TERRA, fill_opacity=1, stroke_width=0)


def ai_box(cx, cy, s=1.0):
    """Dark AI block with a terracotta spark above it."""
    g = Iso(cx, cy, s)
    body = g.box(-0.85, -0.85, 0, 1.7, 1.7, 1.15, DARK_TOP, DARK_L, DARK_R)
    sp = g.p(0, 0, 1.15)
    return VGroup(body, spark4(sp[0], sp[1] + 0.42 * s, 0.24 * s))


def brain_glyph(x, y, r=0.4, lit=True):
    c = Circle(radius=r, fill_color="#F7CBB6" if lit else GHOST, fill_opacity=1,
               stroke_color=INK, stroke_width=3).move_to([x, y, 0])
    sq = VGroup(
        ArcBetweenPoints([x - r * 0.55, y + r * 0.1, 0], [x - r * 0.05, y + r * 0.35, 0],
                         angle=1.3, color=INK, stroke_width=3),
        ArcBetweenPoints([x + r * 0.05, y - r * 0.35, 0], [x + r * 0.55, y - r * 0.1, 0],
                         angle=1.3, color=INK, stroke_width=3))
    dot = Dot([x, y, 0], radius=r * 0.2, color=TERRA if lit else DIM)
    return VGroup(c, sq, dot)


def worker(cx, cy, s=1.0):
    body = RoundedRectangle(width=1.25 * s, height=1.8 * s, corner_radius=0.35 * s,
                            fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK,
                            stroke_width=4).move_to([cx, cy - 0.35, 0])
    head = Circle(radius=0.72 * s, fill_color=CARD, fill_opacity=1, stroke_color=INK,
                  stroke_width=4).move_to([cx, cy + 1.3, 0])
    return VGroup(body, head, brain_glyph(cx, cy + 1.3, 0.4 * s, lit=True))


def pencil(x, y, s=1.0, ang=-0.55):
    shaft = Rectangle(width=1.05 * s, height=0.2 * s, fill_color=BOX_TOP, fill_opacity=1,
                      stroke_color=INK, stroke_width=2.5).move_to([x, y, 0])
    tip = Triangle(fill_color=INK, fill_opacity=1, stroke_width=0).scale(0.13 * s).move_to(
        [x + 0.62 * s, y, 0])
    grp = VGroup(shaft, tip)
    grp.rotate(ang, about_point=[x, y, 0])
    return grp


def envelope(cx, cy, s=1.0):
    body = RoundedRectangle(width=1.9 * s, height=1.25 * s, corner_radius=0.12 * s,
                            fill_color=CARD, fill_opacity=1, stroke_color=INK,
                            stroke_width=3.5).move_to([cx, cy, 0])
    flap = VGroup(
        Line([cx - 0.95 * s, cy + 0.62 * s, 0], [cx, cy + 0.05 * s, 0], color=DIM, stroke_width=3),
        Line([cx, cy + 0.05 * s, 0], [cx + 0.95 * s, cy + 0.62 * s, 0], color=DIM, stroke_width=3))
    return VGroup(body, flap)


def sheet_grid(cx, cy, w=1.8, h=1.25, cols=3, rows=3):
    outer = Rectangle(width=w, height=h, fill_color=CARD, fill_opacity=1, stroke_color=INK,
                      stroke_width=3.5).move_to([cx, cy, 0])
    gl = []
    for i in range(1, cols):
        xx = cx - w / 2 + i * w / cols
        gl.append(Line([xx, cy - h / 2, 0], [xx, cy + h / 2, 0], color=DIM, stroke_width=2))
    for j in range(1, rows):
        yy = cy - h / 2 + j * h / rows
        gl.append(Line([cx - w / 2, yy, 0], [cx + w / 2, yy, 0], color=DIM, stroke_width=2))
    return VGroup(outer, VGroup(*gl))


def vsegments(x, y0, n, filled, w=0.6, h=0.34, gap=0.12, down=False):
    """Vertical meter: returns (filled_list, empty_list), BAR1 vs ghost."""
    fl, em = [], []
    for i in range(n):
        yy = y0 - i * (h + gap) if down else y0 + i * (h + gap)
        seg = Rectangle(width=w, height=h, fill_color=BAR1 if i < filled else GHOST,
                        fill_opacity=1, stroke_width=0).move_to([x, yy, 0])
        (fl if i < filled else em).append(seg)
    return fl, em


def gear(x, y, r=0.42):
    c = Circle(radius=r, fill_color=BOX_L, fill_opacity=1, stroke_color=INK,
               stroke_width=3).move_to([x, y, 0])
    teeth = []
    for a in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        tx, ty = x + (r + 0.06) * np.cos(a), y + (r + 0.06) * np.sin(a)
        teeth.append(Rectangle(width=0.16, height=0.2, fill_color=BOX_L, fill_opacity=1,
                               stroke_color=INK, stroke_width=2).move_to([tx, ty, 0]).rotate(
                                   a, about_point=[tx, ty, 0]))
    hub = Dot([x, y, 0], radius=r * 0.28, color=INK)
    return VGroup(c, VGroup(*teeth), hub)


def zigzag(x, y, w=1.1, amp=0.13, n=4):
    pts = [[x - w / 2 + i * w / n, y + (amp if i % 2 == 0 else -amp), 0] for i in range(n + 1)]
    return VGroup(*[Line(pts[i], pts[i + 1], color=INK, stroke_width=4) for i in range(n)])


# ═════════════════════════════ scenes (one per visual beat) ═════════════════════════════
class B00_Hero(Scene):
    """The hero cast: you (worker, glowing brain) and your AI (dark box, spark)."""

    def construct(self):
        sh1, sh2 = floor_shadow(-2.9), floor_shadow(2.9)
        w = worker(-2.9, -0.5)
        lab_you = lab("you", -2.9, -2.2)
        ab = ai_box(2.9, -0.85)
        lab_ai = lab("your AI", 2.9, -2.2)
        self.play(FadeIn(sh1), FadeIn(w), FadeIn(lab_you), run_time=1.2)
        until(self, "And meet your AI")
        self.play(FadeIn(sh2), FadeIn(ab), run_time=1.2)
        self.play(FadeIn(lab_ai), run_time=0.8)
        until(self, "which work should you never hand over")
        finish(self)


class B01_PasteHope(Scene):
    """Paste-and-hope: the phone draws its route while terrain knowledge drains."""

    def construct(self):
        w = worker(-4.7, -0.9, 0.85)
        phone = RoundedRectangle(width=2.3, height=3.5, corner_radius=0.25, fill_color=CARD,
                                 fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([0.2, 0.1, 0])
        lab_app = lab("the app", 0.2, -2.15, 34)
        rp = [[-0.55, 1.25, 0], [0.75, 0.75, 0], [-0.15, 0.0, 0], [0.95, -0.75, 0]]
        route = VGroup(*[Line(rp[i], rp[i + 1], color=INK, stroke_width=5) for i in range(3)])
        ahead = Triangle(fill_color=INK, fill_opacity=1, stroke_width=0).scale(0.15).move_to(
            [0.95, -0.75, 0]).rotate(-1.1, about_point=[0.95, -0.75, 0])
        fl, _em = vsegments(4.9, 1.05, 5, 5, down=True)
        lab_t1 = lab("terrain", 4.9, -1.75, 32)
        lab_t2 = lab("knowledge", 4.9, -2.2, 32)
        self.play(FadeIn(w), FadeIn(phone), FadeIn(lab_app), run_time=1.2)
        until(self, "Like GPS")
        self.play(*[Create(s) for s in route], FadeIn(ahead), run_time=1.0)
        self.play(*[FadeIn(s) for s in fl], FadeIn(lab_t1), FadeIn(lab_t2), run_time=0.9)
        until(self, "you stop learning the terrain")
        self.play(*[FadeOut(s) for s in fl[1:]], run_time=1.0)
        until(self, "lost in your own city")
        finish(self)


class B02_OneLine(Scene):
    """Work flies into the AI box and earns a check; understanding stays with you."""

    def construct(self):
        w = worker(-2.6, -0.5)
        lab_you = lab("you", -2.6, -2.2)
        ab = ai_box(3.3, -0.85)
        lab_ai = lab("your AI", 3.3, -2.2)
        self.play(FadeIn(w), FadeIn(lab_you), FadeIn(ab), FadeIn(lab_ai), run_time=1.2)
        g = Iso(0, 0, 0.75)
        pages = VGroup(*[g.page(-1.3 + i * 1.3, 0, 0) for i in range(3)])
        pages.move_to([-4.1, 1.35, 0])
        gr = gear(-4.1, -0.35, 0.42)
        lab_work = lab("work", -4.1, -1.15, 34)
        until(self, "Outsource work to AI")
        self.play(FadeIn(pages), FadeIn(gr), FadeIn(lab_work), run_time=1.0)
        tgt = np.array([3.3, 0.85, 0])
        flyers = [MoveAlongPath(m, ArcBetweenPoints(np.array(m.get_center()), tgt, angle=0.5))
                  for m in list(pages) + [gr]]
        self.play(*flyers, FadeOut(lab_work), run_time=1.5)
        self.play(FadeOut(pages), FadeOut(gr), run_time=0.3)
        chk = check(5.35, 1.05)
        lab_w2 = lab("work", 5.35, 0.35, 34)
        self.play(GrowFromCenter(chk), FadeIn(lab_w2), run_time=0.8)
        until(self, "cannot outsource understanding")
        ring = Circle(radius=1.12, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to([-2.6, 0.8, 0])
        rdot = Dot([-2.6, 1.92, 0], radius=0.14, color=TERRA)
        self.play(GrowFromCenter(ring), FadeIn(rdot), run_time=0.8)
        lab_u = lab("understanding", -2.6, -2.2, 34)
        self.play(FadeOut(lab_you), FadeIn(lab_u), run_time=0.6)
        until(self, "Clear intent in")
        finish(self)


class B03_ThinkFirst(Scene):
    """Constraints first, then the rough draft: your thinking, on paper."""

    def construct(self):
        card = RoundedRectangle(width=3.2, height=2.4, corner_radius=0.15, fill_color=CARD,
                                fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-3.4, 0.3, 0])
        lab_c = lab("constraints", -3.4, 2.0)
        words = VGroup(lab("format", -3.4, 0.85, 32), lab("audience", -3.4, 0.3, 32),
                       lab("not allowed", -3.4, -0.25, 32))
        self.play(FadeIn(card), FadeIn(lab_c), *[FadeIn(x) for x in words], run_time=1.2)
        g = Iso(0, 0, 0.8)
        pg = g.page(0, 0, 0)
        pg.move_to([2.9, -0.15, 0])
        pcl = pencil(2.9, 1.05, 0.9)
        lab_d = lab("rough draft", 2.9, -1.5, 34)
        until(self, "Two: write a rough draft")
        self.play(FadeIn(pg), FadeIn(pcl), run_time=0.9)
        sq = VGroup(zigzag(2.45, 0.05, 0.9), zigzag(2.45, -0.3, 0.9), zigzag(2.45, -0.62, 0.7))
        self.play(*[Create(z) for z in sq], run_time=1.2)
        self.play(FadeIn(lab_d), run_time=0.6)
        until(self, "on paper")
        finish(self)


class B04_HandOver(Scene):
    """Draft + constraints slide into the AI; three versions spring out."""

    def construct(self):
        g = Iso(0, 0, 0.8)
        pg = g.page(0, 0, 0)
        pg.move_to([-3.9, 0.35, 0])
        card = RoundedRectangle(width=2.0, height=1.4, corner_radius=0.12, fill_color=CARD,
                                fill_opacity=1, stroke_color=INK, stroke_width=3.5).move_to([-3.9, -1.35, 0])
        lab_dc = lab("draft + rules", -3.9, -2.5, 32)
        ab = ai_box(2.9, -0.85)
        lab_ai = lab("your AI", 2.9, -2.2)
        self.play(FadeIn(pg), FadeIn(card), FadeIn(lab_dc), FadeIn(ab), FadeIn(lab_ai), run_time=1.2)
        until(self, "Three: paste")
        tgt = np.array([2.9, 0.85, 0])
        self.play(MoveAlongPath(pg, ArcBetweenPoints(np.array(pg.get_center()), tgt, angle=0.5)),
                  MoveAlongPath(card, ArcBetweenPoints(np.array(card.get_center()), tgt, angle=0.35)),
                  FadeOut(lab_dc), run_time=1.5)
        self.play(FadeOut(pg), FadeOut(card), run_time=0.3)
        until(self, "ask for three versions")
        outs = VGroup(*[g.page(0, 0, 0).move_to([1.65 + i * 1.25, 1.55, 0]) for i in range(3)])
        lab3 = lab("3 versions", 2.9, 2.62)
        self.play(*[FadeIn(o) for o in outs], FadeIn(lab3), run_time=1.0)
        until(self, "not instead of it")
        finish(self)


class B05_YouDecide(Scene):
    """Pick one version, edit it, call it yours."""

    def construct(self):
        g = Iso(0, 0, 0.8)
        pages = VGroup(*[g.page(0, 0, 0).move_to([-2.4 + i * 2.4, 0.2, 0]) for i in range(3)])
        self.play(*[FadeIn(p) for p in pages], run_time=1.0)
        until(self, "pick one version")
        mid = pages[1]
        self.play(mid.animate.shift([0, 0.9, 0]), run_time=0.8)
        until(self, "edit it")
        c = np.array(mid.get_center())
        el = Line([c[0] - 0.5, c[1] + 0.12, 0], [c[0] + 0.5, c[1] + 0.12, 0],
                  color=INK, stroke_width=5)
        self.play(Create(el), run_time=0.7)
        chk = check(c[0] + 1.05, c[1] + 0.55)
        lab_y = lab("yours", c[0], -1.35)
        self.play(GrowFromCenter(chk), FadeIn(lab_y), run_time=0.8)
        until(self, "genuinely yours")
        finish(self)


class B06_ThreeDomains(Scene):
    """Three stations, one method: the pencil writes first, then the work slides into the AI box."""

    def construct(self):
        g = Iso(0, 0, 0.7)
        xs = [-4.2, 0.0, 4.2]
        tags = ["strategy", "email", "spreadsheet"]
        pg = g.page(0, 0, 0)
        pg.move_to([-4.2, 1.35, 0])
        env = envelope(0.0, 1.35, 0.85)
        grd = sheet_grid(4.2, 1.35, 1.7, 1.2)
        icons = [pg, env, grd]
        boxes = [ai_box(x, -1.95, 0.6) for x in xs]
        pcls = [pencil(x + 1.25, 1.5, 0.7) for x in xs]
        labs = [lab(t, x, -2.95, 32) for x, t in zip(xs, tags)]
        self.play(*[FadeIn(i) for i in icons], *[FadeIn(b) for b in boxes],
                  *[FadeIn(p) for p in pcls], *[FadeIn(t) for t in labs], run_time=1.4)
        phrases = ["you write the goals first", "you write the one point", "you list your assumptions"]
        for k, x in enumerate(xs):
            until(self, phrases[k])
            sq = zigzag(x - 0.3, 1.5, 0.8)
            self.play(Create(sq), run_time=0.6)
            cp = icons[k].copy()
            self.play(FadeIn(cp), run_time=0.15)
            self.play(MoveAlongPath(cp, ArcBetweenPoints(np.array(cp.get_center()),
                                                         np.array([x, -1.25, 0]), angle=0.4)),
                      FadeOut(sq), run_time=0.9)
            self.play(FadeOut(cp), run_time=0.25)
        finish(self)


class B07_GPSBrain(Scene):
    """Follow the GPS and the brain's navigation areas go quiet."""

    def construct(self):
        head = Circle(radius=1.5, fill_color=CARD, fill_opacity=1, stroke_color=INK,
                      stroke_width=4).move_to([-1.6, 0.2, 0])
        offs = [(-0.4, 0.35), (0.05, 0.5), (0.45, 0.25), (-0.25, -0.2), (0.3, -0.3)]
        glow = VGroup(*[Dot([-1.6 + dx, 0.2 + dy, 0], radius=0.17, color=TERRA) for dx, dy in offs])
        lab1 = lab("you navigate", -1.6, 2.3, 34)
        self.play(FadeIn(head), FadeIn(glow), FadeIn(lab1), run_time=1.2)
        until(self, "followed turn-by-turn directions")
        turns = []
        for i in range(3):
            x0, y0 = 1.3 + i * 1.25, 1.5 - i * 0.55
            turns.append(VGroup(Line([x0, y0, 0], [x0 + 0.75, y0, 0], color=DIM, stroke_width=5),
                                Line([x0 + 0.75, y0, 0], [x0 + 0.75, y0 - 0.7, 0],
                                     color=DIM, stroke_width=5)))
        self.play(*[Create(t) for t in turns], run_time=1.1)
        ghost = VGroup(*[Dot([-1.6 + dx, 0.2 + dy, 0], radius=0.17, color=GHOST) for dx, dy in offs])
        lab2 = lab("GPS navigates", -1.6, 2.3, 34)
        cap = lab("UCL, 2017", 4.9, -2.9, 32)
        self.play(FadeOut(glow), FadeIn(ghost), FadeOut(lab1), FadeIn(lab2), FadeIn(cap), run_time=1.0)
        until(self, "switched off its interest")
        finish(self)


class B08_EightyThree(Scene):
    """The number: 83% of the ChatGPT group couldn't quote their own essay."""

    def construct(self):
        fl_a, em_a = vsegments(-3.4, -1.35, 10, 8, w=0.62, h=0.26, gap=0.1)
        lab_a = lab("wrote with AI", -3.4, -2.35, 32)
        num_a = T("83%", size=96, bold=True).move_to([-3.4, 2.55, 0])
        fl_b, em_b = vsegments(3.4, -1.35, 10, 1, w=0.62, h=0.26, gap=0.1)
        lab_b = lab("wrote without AI", 3.4, -2.35, 32)
        num_b = T("11%", size=72, bold=True).move_to([3.4, 2.55, 0])
        cap1 = lab("per MIT Media Lab, 2025", 0, -2.72, 32)
        cap2 = lab("(preprint)", 0, -3.12, 32)
        self.play(*[FadeIn(s) for s in fl_a[:4]], run_time=0.9)
        until(self, "eighty-three percent")
        self.play(*[FadeIn(s) for s in fl_a[4:]], *[FadeIn(s) for s in em_a],
                  GrowFromCenter(num_a), FadeIn(lab_a), run_time=1.1)
        until(self, "eleven percent")
        self.play(*[FadeIn(s) for s in fl_b], *[FadeIn(s) for s in em_b],
                  GrowFromCenter(num_b), FadeIn(lab_b), run_time=1.0)
        self.play(FadeIn(cap1), FadeIn(cap2), run_time=0.7)
        until(self, "not settled")
        finish(self)


class B09_FastTrap(Scene):
    """Fast feels fine: pages stream out of the AI while the brain gauge drains."""

    def construct(self):
        ab = ai_box(-3.6, -0.85)
        lab_ai = lab("your AI", -3.6, -2.2, 34)
        w = worker(3.6, -0.5, 0.9)
        fl, _em = vsegments(5.05, 1.05, 4, 4, w=0.5, down=True)
        self.play(FadeIn(ab), FadeIn(lab_ai), FadeIn(w), *[FadeIn(s) for s in fl], run_time=1.2)
        until(self, "getting fast")
        g = Iso(0, 0, 0.7)
        outs = [g.page(0, 0, 0).move_to([-3.6 + i * 0.75, 1.25 + i * 0.5, 0]) for i in range(4)]
        dial = Arc(radius=1.0, start_angle=0, angle=np.pi, color=INK, stroke_width=5).move_to([-0.7, -1.35, 0])
        ndl = Line([-0.7, -1.35, 0], [-1.5, -0.75, 0], color=INK, stroke_width=7)
        lab_f = lab("shipping", -0.7, -2.2, 34)
        self.play(*[FadeIn(p) for p in outs], Create(dial), FadeIn(ndl), FadeIn(lab_f), run_time=1.2)
        ndl2 = Line([-0.7, -1.35, 0], [0.1, -0.75, 0], color=INK, stroke_width=7)
        self.play(Transform(ndl, ndl2), run_time=0.8)
        until(self, "why you did it that way")
        bub = RoundedRectangle(width=1.15, height=1.15, corner_radius=0.2, fill_color=CARD,
                               fill_opacity=1, stroke_color=INK, stroke_width=3.5).move_to([4.85, 1.85, 0])
        tail = Triangle(fill_color=CARD, fill_opacity=1, stroke_color=INK,
                        stroke_width=3).scale(0.22).move_to([4.35, 1.15, 0])
        qm = T("?", size=64, bold=True).move_to([4.85, 1.85, 0])
        self.play(FadeIn(bub), FadeIn(tail), FadeIn(qm), run_time=0.7)
        self.play(*[FadeOut(s) for s in fl[1:]], run_time=0.9)
        until(self, "wouldn't have to")
        finish(self)
