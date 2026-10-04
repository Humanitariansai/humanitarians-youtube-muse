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
scenes_body.py — the 8 Manim scenes for "Say what you want, plainly".

Concatenated after templates/iso_kit.py to form scenes.py (Gate A copies
only scenes.py, so the kit must be pasted in, not imported).

Cast (same objects, whole film): a kraft prompt slip (the prompt), a dark
AI block (the AI), white pages (answers), small kraft chips (the four
questions). Teardown register: one drawing per beat, labels beside objects,
ink text, terracotta only for dots/checks.
"""

# ── small film helpers ──
# Attach the kit's pacing helpers as Scene methods (the kit defines them as
# plain functions taking self).
Scene.until = until
Scene.finish = finish


def _chip(x, y, w=1.5, h=0.85):
    """A kraft question chip with an ink outline (Gate V: kraft-on-cream needs the outline).

    Plain Rectangle, not RoundedRectangle: the Gate A stub does not track
    RoundedRectangle in shape signatures, which fails a chip-only beat with
    "shapes never change".
    """
    return Rectangle(width=w, height=h,
                     fill_color="#F3E9D8", fill_opacity=1,
                     stroke_color=INK, stroke_width=4).move_to([x, y, 0])


def _brief_slip(iso, x0, y0, w=1.7, d=2.3):
    """A prompt slip with ink lines already on it (the brief, mid-film)."""
    slab = iso.box(x0, y0, 0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    zt = 0.06
    lines = VGroup(*[Line(iso.p(x0 + 0.3, y0 + d * f, zt), iso.p(x0 + w - 0.3, y0 + d * f, zt),
                         color=INK, stroke_width=5) for f in (0.3, 0.5, 0.7)])
    return VGroup(slab, lines)


def _dim_page(iso, x0, y0, w, d):
    """A washed-out answer page (a guess that fit nobody)."""
    slab = iso.box(x0, y0, 0, w, d, 0.06, GHOST, BAR2, BAR3, sw=2)
    zt = 0.06
    lines = VGroup(*[Line(iso.p(x0 + 0.2, y0 + d * f, zt), iso.p(x0 + w - 0.2, y0 + d * f, zt),
                          color=BAR3, stroke_width=4) for f in (0.35, 0.6)])
    return VGroup(slab, lines)


class B00_PromptSlip(Scene):
    def construct(self):
        iso = Iso(0, -0.3, 0.85)
        shadow = Ellipse(width=3.6, height=0.7, fill_color=GHOST, fill_opacity=1,
                         stroke_width=0).move_to([0, -2.45, 0])
        slip = iso.page(-0.8, -1.1, 0.0, w=1.6, d=2.2)
        slip.shift(UP * 5.5)
        self.play(FadeIn(shadow), run_time=0.4)
        self.play(FadeIn(slip, shift=DOWN * 5.5), rate_func=ease_in, run_time=1.4)
        self.until("A request")
        lab = T("prompt", 44).move_to([3.7, -0.2, 0])
        leader = Line([1.9, -0.25, 0], [3.05, -0.22, 0], color=DIM, stroke_width=3)
        self.play(FadeIn(lab), FadeIn(leader), run_time=0.5)
        self.until("The words you put in")
        dot = Dot(iso.p(-0.45, 0.1, 0.1), radius=0.11, color=TERRA)
        self.play(GrowFromCenter(dot), run_time=0.5)
        self.finish()


class B01_Guesses(Scene):
    def construct(self):
        iso = Iso(0, -0.4, 0.8)
        ai = iso.mcp(-1.6, -0.8, 0, w=1.7, d=1.7, h=1.1)
        ai_lab = T("AI", 40).move_to([-3.5, 0.7, 0])
        self.play(FadeIn(ai), run_time=0.8)
        self.play(FadeIn(ai_lab), run_time=0.4)
        slip = iso.page(-4.6, 1.0, 0.0, w=1.5, d=1.0)
        slip_lab = T("write a summary", 36).move_to([-3.9, -2.9, 0])
        self.play(FadeIn(slip), FadeIn(slip_lab), run_time=0.6)
        self.until("hands the AI")
        self.play(slip.animate.shift(iso.v(2.6, 0, 0)), run_time=0.9)
        self.play(FadeOut(slip), FadeOut(slip_lab), run_time=0.4)
        self.until("And its guesses")
        p1 = iso.page(1.6, -0.5, 0.0, w=1.0, d=1.8)
        p2 = iso.page(3.0, 0.1, 0.0, w=1.6, d=0.9)
        p3 = iso.page(4.4, -0.3, 0.0, w=0.9, d=0.9)
        self.play(FadeIn(p1), run_time=0.4)
        self.play(FadeIn(p2), run_time=0.4)
        self.play(FadeIn(p3), run_time=0.4)
        glab = T("guesses", 40).move_to([2.4, -2.4, 0])
        self.play(FadeIn(glab), run_time=0.4)
        self.finish()


class B02_MostCommon(Scene):
    def construct(self):
        iso = Iso(0, -0.4, 0.8)
        ai = iso.mcp(-0.9, -0.9, 0, w=1.8, d=1.8, h=1.2)
        ai_lab = T("AI", 40).move_to([-3.3, 0.9, 0])
        self.play(FadeIn(ai), run_time=0.8)
        self.play(FadeIn(ai_lab), run_time=0.4)
        crowd = VGroup(*[iso.page(x, y, 0.0, w=0.7, d=0.7)
                         for x, y in [(2.0, 2.4), (3.2, 1.2), (4.4, 0.0), (5.6, -1.2)]])
        clab = T("most people", 36).move_to([2.2, 2.5, 0])
        self.play(FadeIn(crowd), run_time=0.8)
        self.play(FadeIn(clab), run_time=0.4)
        you = iso.box(-4.55, 0.35, 0, 0.7, 0.7, 0.06, BOX_TOP, BOX_L, BOX_R, sw=3)
        youlab = T("you", 36).move_to([-3.4, -2.7, 0])
        self.play(FadeIn(you), FadeIn(youlab), run_time=0.5)
        self.until("most people want")
        slip = iso.page(-5.2, 0.9, 0.0, w=1.4, d=0.9)
        self.play(FadeIn(slip), run_time=0.5)
        self.play(slip.animate.shift(iso.v(2.8, 0, 0)), run_time=0.9)
        self.play(FadeOut(slip), run_time=0.4)
        self.until("Your reader")
        out = iso.page(3.0, -0.4, 0.0, w=1.1, d=1.4)
        olab = T("most common answer", 36).move_to([2.36, -1.1, 0])
        self.play(FadeIn(out), run_time=0.6)
        self.play(FadeIn(olab), run_time=0.4)
        self.until("none of it is in the answer")
        dot = Dot(iso.p(-4.2, 0.7, 0.1), radius=0.11, color=TERRA)
        self.play(GrowFromCenter(dot), run_time=0.5)
        self.finish()


class B03_TheFix(Scene):
    def construct(self):
        iso = Iso(0, -0.3, 0.85)
        vague = iso.page(-4.1, -0.5, 0.0, w=1.5, d=1.0)
        self.play(FadeIn(vague), run_time=0.5)
        slip = iso.page(0.6, -1.1, 0.0, w=1.7, d=2.3)
        slip.shift(UP * 5.5)
        self.play(FadeIn(slip, shift=DOWN * 5.5), rate_func=ease_in, run_time=1.2)
        self.until("Plainly")
        x0, y0, w, d = 0.6, -1.1, 1.7, 2.3
        lines = [Line(iso.p(x0 + 0.3, y0 + d * f, 0.08), iso.p(x0 + w - 0.3, y0 + d * f, 0.08),
                      color=INK, stroke_width=5) for f in (0.3, 0.5, 0.7)]
        for ln in lines:
            self.play(Create(ln), run_time=0.4)
        self.until("across from you")
        dot = Dot(iso.p(x0 + 0.3, y0 + d * 0.86, 0.08), radius=0.1, color=TERRA)
        lab = T("say it plainly", 40).move_to([4.0, 0.9, 0])
        leader = Line([2.75, 0.7, 0], [3.3, 0.85, 0], color=DIM, stroke_width=3)
        self.play(GrowFromCenter(dot), FadeIn(lab), FadeIn(leader), run_time=0.6)
        self.finish()


class B04_FourQuestions(Scene):
    def construct(self):
        slip = _brief_slip(Iso(0, -0.3, 0.8), -0.85, -1.15)
        self.play(FadeIn(slip), run_time=0.6)
        chips = [(1, "length", -3.4, 1.2), (2, "format", 3.4, 1.2),
                 (3, "audience", -3.4, -1.6), (4, "must-haves", 3.4, -1.6)]
        phrases = ["How long", "What shape", "Who it is for", "what must be in it"]
        for (n, term, cx, cy), phrase in zip(chips, phrases):
            self.until(phrase)
            chip = _chip(cx, cy + 1.2)
            num = T(str(n), 38, INK).move_to([cx, cy + 1.2 - 0.05, 0])
            tlab = T(term, 36).move_to([cx, cy - 0.75, 0])
            self.play(FadeIn(chip, shift=DOWN * 1.2), rate_func=ease_in, run_time=0.5)
            self.play(FadeIn(num), FadeIn(tlab), run_time=0.4)
        self.finish()


class B05_NewHire(Scene):
    def construct(self):
        iso = Iso(0, -0.4, 0.85)
        back, front = iso.open_box(-1.4, -1.4, 0, w=2.8, d=2.8, h=1.2)
        lab = T("day one", 40).move_to([3.7, 0.4, 0])
        leader = Line([2.3, 0.2, 0], [3.05, 0.35, 0], color=DIM, stroke_width=3)
        self.play(FadeIn(back), FadeIn(front), run_time=0.8)
        self.play(FadeIn(lab), FadeIn(leader), run_time=0.4)
        self.until("Smart, eager")
        spots = [(-1.0, 0.0), (-0.1, 0.15), (0.8, 0.0), (-0.1, 0.55)]
        for i, (cx, cy) in enumerate(spots):
            chip = _chip(cx, cy + 1.0, w=1.0, h=0.55)
            num = T(str(i + 1), 32, INK).move_to([cx, cy + 1.0 - 0.03, 0])
            grp = VGroup(chip, num)
            self.play(FadeIn(grp, shift=DOWN * 1.0), rate_func=ease_in, run_time=0.4)
        self.until("Explicitly")
        page = iso.page(-0.6, -0.9, 1.3, w=1.2, d=1.6)
        page.shift(DOWN * 1.6)
        self.play(FadeIn(page, shift=UP * 1.6), run_time=0.9)
        chk = check(1.7, 1.7, s=0.25, color=INK, w=7)
        self.play(GrowFromCenter(chk), run_time=0.5)
        self.finish()


class B06_BriefRewrite(Scene):
    def construct(self):
        iso = Iso(0, -0.3, 0.85)
        x0, y0, w, d = -0.85, -1.15, 1.7, 2.3
        slab = iso.box(x0, y0, 0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        ghost = Line(iso.p(x0 + 0.3, y0 + d * 0.18, 0.08), iso.p(x0 + w - 0.3, y0 + d * 0.18, 0.08),
                     color=GHOST, stroke_width=5)
        dot0 = Dot(iso.p(x0 + 0.3, y0 + d * 0.9, 0.08), radius=0.09, color=TERRA)
        slip = VGroup(slab, ghost, dot0)
        lab = T("brief", 40).move_to([3.9, 0.6, 0])
        leader = Line([1.85, 0.45, 0], [3.3, 0.55, 0], color=DIM, stroke_width=3)
        self.play(FadeIn(slip), run_time=0.6)
        self.play(FadeIn(lab), FadeIn(leader), run_time=0.4)
        self.until("Now fill the blanks")
        for i, f in enumerate((0.34, 0.5, 0.66, 0.82)):
            ln = Line(iso.p(x0 + 0.62, y0 + d * f, 0.08), iso.p(x0 + w - 0.3, y0 + d * f, 0.08),
                      color=INK, stroke_width=5)
            num = T(str(i + 1), 34, INK).move_to(iso.p(x0 + 0.38, y0 + d * f - 0.02, 0.08))
            self.play(FadeIn(num), Create(ln), run_time=0.5)
        self.until("no longer has to make")
        dot = Dot(iso.p(x0 + w - 0.25, y0 + d * 0.9, 0.08), radius=0.1, color=TERRA)
        self.play(GrowFromCenter(dot), run_time=0.5)
        self.finish()


class B07_Compare(Scene):
    def construct(self):
        iso = Iso(0, -0.2, 0.8)
        vslip = iso.page(-4.9, 1.3, 0.0, w=1.4, d=0.9)
        self.play(FadeIn(vslip), run_time=0.6)
        dims = VGroup(*[_dim_page(iso, x, y, w, d)
                        for x, y, w, d in [(-5.3, -0.9, 1.0, 1.4), (-3.9, -1.1, 1.4, 0.8), (-2.5, -0.9, 0.8, 0.8)]])
        self.play(FadeIn(dims), run_time=0.6)
        vlab = T("vague", 40).move_to([-3.9, -2.5, 0])
        self.play(FadeIn(vlab), run_time=0.4)
        self.until("gets you one page")
        bslip = _brief_slip(iso, 1.9, 0.6, w=1.5, d=1.0)
        neat = iso.page(1.9, -1.2, 0.0, w=1.5, d=1.3)
        chk = check(4.15, -0.1, s=0.28, color=INK, w=7)
        blab = T("brief", 40).move_to([2.65, -2.5, 0])
        self.play(FadeIn(bslip), FadeIn(neat), run_time=0.8)
        self.play(GrowFromCenter(chk), FadeIn(blab), run_time=0.5)
        self.finish()
