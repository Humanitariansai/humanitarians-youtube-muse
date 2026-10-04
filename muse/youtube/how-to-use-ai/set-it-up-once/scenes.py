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


# ═════════════════════════════ film helpers (set-it-up-once) ═════════════════════════════
# Cast: the pinned note (recurs B01–B08), chat windows, chat bubbles, the
# settings panel, keyword pills, kraft cables. Labels sit beside objects.

KRAFT_CABLE = "#9C8462"  # deep kraft for connectors (never ink-edged cables)


def lab(s, x, y, size=34, color=INK):
    return T(s, size=size, color=color).move_to([x, y, 0])


def floor_shadow(cx, w=3.0):
    return Ellipse(width=w, height=0.3, fill_color=GHOST, fill_opacity=1,
                   stroke_width=0).move_to([cx, -2.9, 0])


def chat_window(cx, cy, w, h):
    """Pale chat window: card body, dark title bar (contrast law), terracotta dot."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    bar = RoundedRectangle(width=w - 0.04, height=0.5, corner_radius=0.14,
                           fill_color=DARK_TOP, fill_opacity=1,
                           stroke_width=0).move_to([cx, cy + h / 2 - 0.27, 0])
    dot = Dot([cx - w / 2 + 0.45, cy + h / 2 - 0.27, 0], radius=0.09, color=TERRA)
    return VGroup(body, bar, dot)


def bubble(lines, cx, cy, w, fill=CARD):
    """Chat bubble with grey (DIM) outline so it stays distinct inside the ink window."""
    texts = VGroup(*[T(s, size=32) for s in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
    bg = RoundedRectangle(width=max(w, texts.width + 0.7),
                          height=texts.height + 0.55, corner_radius=0.22,
                          fill_color=fill, fill_opacity=1,
                          stroke_color=DIM, stroke_width=2.5).move_to([cx, cy, 0])
    texts.move_to(bg.get_center())
    return VGroup(bg, texts)


def note(cx, cy, w=4.2, h=3.2):
    """The pinned note: white page, ink outline, terracotta pin dot at top."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.12,
                            fill_color="#FFFFFF", fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    pin = Dot([cx, cy + h / 2 - 0.28, 0], radius=0.12, color=TERRA)
    return VGroup(body, pin)


def settings_panel(cx, cy, w=4.6, h=3.8):
    body = RoundedRectangle(width=w, height=h, corner_radius=0.16,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    rows = VGroup(*[RoundedRectangle(width=w - 0.9, height=0.52, corner_radius=0.1,
                                     fill_color=GHOST, fill_opacity=1,
                                     stroke_width=0).move_to(
                                         [cx, cy + h / 2 - 0.85 - i * 0.78, 0])
                     for i in range(4)])
    return VGroup(body, rows)


def kw_pill(text, cx, cy, w):
    bg = RoundedRectangle(width=w, height=0.72, corner_radius=0.36,
                          fill_color="#FFFFFF", fill_opacity=1,
                          stroke_color=INK, stroke_width=3).move_to([cx, cy, 0])
    t = T(text, size=32).move_to([cx, cy - 0.02, 0])
    return VGroup(bg, t)


def xmark(cx, cy, s=0.28, color=TERRA, w=8):
    return VGroup(
        Line([cx - s, cy + s, 0], [cx + s, cy - s, 0], color=color, stroke_width=w),
        Line([cx - s, cy - s, 0], [cx + s, cy + s, 0], color=color, stroke_width=w))


def zigzag(x, y, w, color=DIM):
    grp = VGroup()
    segs = 12
    for k in range(segs):
        x0 = x - w / 2 + w * k / segs
        x1 = x - w / 2 + w * (k + 1) / segs
        y0 = y + (0.08 if k % 2 == 0 else -0.08)
        y1 = y + (0.08 if (k + 1) % 2 == 0 else -0.08)
        grp.add(Line([x0, y0, 0], [x1, y1, 0], color=color, stroke_width=3))
    return grp


def pencil(cx, cy, s=1.0):
    body = Rectangle(width=1.3 * s, height=0.34 * s, fill_color=BOX_TOP,
                     fill_opacity=1, stroke_color=INK,
                     stroke_width=3).move_to([cx, cy, 0])
    tip = Polygon([cx + 0.65 * s, cy + 0.17 * s, 0],
                  [cx + 0.65 * s, cy - 0.17 * s, 0],
                  [cx + 1.05 * s, cy, 0],
                  fill_color=INK, fill_opacity=1, stroke_width=0)
    return VGroup(body, tip)


def cable(a, b):
    return Line(a, b, color=KRAFT_CABLE, stroke_width=5)


def arrowhead(pt, ang):
    return Triangle(fill_color=INK, fill_opacity=1, stroke_width=0).scale(
        0.14).move_to(pt).rotate(ang, about_point=pt)


# ═════════════════════════════ scenes ═════════════════════════════

class B00_Repeat(Scene):
    """The annoyance: a fresh chat is a stranger; the jargon answer lands; the loop closes."""

    def construct(self):
        sh = floor_shadow(-0.2, w=5.4)
        win = chat_window(-0.2, 0.15, 5.8, 3.8)
        lab_chat = lab("one chat", -0.2, 2.5)
        self.play(FadeIn(sh), FadeIn(win), FadeIn(lab_chat), run_time=1.0)
        until(self, "Back comes a wall")
        uq = bubble(["explain p-values"], -0.2, 1.25, w=3.4)
        self.play(FadeIn(uq), run_time=0.7)
        ans = bubble(["the probability of getting", "results at least as extreme",
                      "under the null hypothesis"], -0.2, -0.55, w=5.0, fill="#EFE9DB")
        self.play(FadeIn(ans), run_time=0.9)
        until(self, "so you explain yourself")
        loop = ArcBetweenPoints(np.array([2.0, -0.8, 0]), np.array([2.0, 0.9, 0]), angle=-2.0)
        head = arrowhead([2.0, 0.9, 0], -0.5)
        lab_again = lab("again?", 4.15, 0.15)
        self.play(Create(loop), run_time=0.7)
        self.play(FadeIn(head), FadeIn(lab_again), run_time=0.6)
        finish(self)


class B01_TheNote(Scene):
    """The fix: the note drops into settings, gets pinned, and cables to every chat."""

    def construct(self):
        sh = floor_shadow(-3.3, w=4.4)
        panel = settings_panel(-3.3, 0.0, 4.6, 3.8)
        lab_s = lab("settings", -3.3, 2.35)
        self.play(FadeIn(sh), FadeIn(panel), FadeIn(lab_s), run_time=1.0)
        until(self, "your standing instructions")
        nt = note(-3.3, 2.4, 3.0, 2.4)
        self.play(FadeIn(nt), run_time=0.5)
        self.play(MoveAlongPath(nt, Line(np.array([-3.3, 2.4, 0]),
                                         np.array([-3.3, 0.2, 0]))), run_time=0.8)
        until(self, "a cover page")
        w1 = chat_window(2.7, 1.35, 3.2, 1.9)
        w2 = chat_window(2.7, -1.45, 3.2, 1.9)
        lab_e = lab("every chat", 2.7, -2.75)
        self.play(FadeIn(w1), FadeIn(w2), FadeIn(lab_e), run_time=0.9)
        c1 = cable([-1.8, 0.2, 0], [1.1, 1.35, 0])
        c2 = cable([-1.8, 0.2, 0], [1.1, -1.45, 0])
        self.play(Create(c1), Create(c2), run_time=0.8)
        finish(self)


class B02_WhereItLives(Scene):
    """Where the setting lives: the cursor picks 'instructions' out of three candidate words."""

    def construct(self):
        panel = settings_panel(-0.6, -0.1, 5.8, 4.0)
        lab_s = lab("settings", -0.6, 2.35)
        self.play(FadeIn(panel), FadeIn(lab_s), run_time=1.0)
        until(self, "or your profile page")
        p1 = kw_pill("instructions", -0.6, 1.0, 2.7)
        p2 = kw_pill("personalization", -0.6, 0.1, 3.7)
        p3 = kw_pill("memory", -0.6, -0.8, 2.2)
        self.play(FadeIn(p1), run_time=0.5)
        self.play(FadeIn(p2), run_time=0.5)
        self.play(FadeIn(p3), run_time=0.5)
        cur = cursor(1.9, 1.0)
        self.play(FadeIn(cur), run_time=0.4)
        self.play(MoveAlongPath(cur, ArcBetweenPoints(np.array([1.9, 1.0, 0]),
                                                      np.array([1.35, 1.0, 0]),
                                                      angle=0.3)), run_time=0.5)
        until(self, "so search for the word")
        chk = check(1.55, 1.0, color=TERRA)
        lab_w = lab("look for these words", 4.35, 0.1)
        self.play(GrowFromCenter(chk), FadeIn(lab_w), run_time=0.7)
        finish(self)


class B03_GoodLines(Scene):
    """Good instructions: four concrete lines write themselves onto the note."""

    def construct(self):
        nt = note(0, 0.05, 4.6, 3.4)
        lab_n = lab("the note", 0, 2.25)
        self.play(FadeIn(nt), FadeIn(lab_n), run_time=0.9)
        lines = ["keep answers short", "beginner at statistics",
                 "plain English, no jargon", "steps I can try today"]
        ys = [1.05, 0.45, -0.15, -0.75]
        waits = ["I'm a beginner at statistics.", "Plain English, no jargon.",
                 "Give me steps I can try today."]
        until(self, "Keep answers short.")
        for i, (s, y) in enumerate(zip(lines, ys)):
            dot = Dot([-1.85, y, 0], radius=0.08, color=INK)
            tx = T(s, size=32).move_to([-0.15, y - 0.03, 0])
            self.play(FadeIn(dot), FadeIn(tx), run_time=0.5)
            if i < 3:
                until(self, waits[i])
        finish(self)


class B04_BadNote(Scene):
    """Bad instructions: the life story spills off the page; two orders collide on the X."""

    def construct(self):
        nt = note(0, 0.75, 4.0, 3.0)
        lab_n = lab("the note", 0, 2.7)
        self.play(FadeIn(nt), FadeIn(lab_n), run_time=0.9)
        until(self, "the AI can't use your biography")
        sq = VGroup(*[zigzag(0, 1.55 - i * 0.34, 3.2) for i in range(8)])
        self.play(*[Create(z) for z in sq], run_time=1.2)
        until(self, "be brief, and explain everything")
        p1 = kw_pill("be brief!", -2.3, -1.95, 2.0)
        p2 = kw_pill("explain everything!", 2.3, -1.95, 3.4)
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.7)
        xm = xmark(0.15, -1.95, s=0.3)
        self.play(GrowFromCenter(xm), run_time=0.6)
        until(self, "so give it one rule per line")
        finish(self)


class B05_Payoff(Scene):
    """The payoff: the same question gets two answers; the note is the only difference."""

    def construct(self):
        qbg = RoundedRectangle(width=7.0, height=0.7, corner_radius=0.35,
                               fill_color="#FFFFFF", fill_opacity=1,
                               stroke_color=INK, stroke_width=3).move_to([0, 2.95, 0])
        qt = T("explain p-values", size=32).move_to([0, 2.92, 0])
        lab_q = lab("same question", -5.25, 2.95, size=32)
        self.play(FadeIn(qbg), FadeIn(qt), FadeIn(lab_q), run_time=0.8)
        until(self, "two chats")
        wl = chat_window(-3.05, -0.35, 5.5, 3.1)
        wr = chat_window(3.05, -0.75, 5.5, 2.6)
        lab_l = lab("without the note", -3.05, -2.35)
        lab_r = lab("with the note", 3.05, -2.5)
        self.play(FadeIn(wl), FadeIn(wr), FadeIn(lab_l), FadeIn(lab_r), run_time=0.9)
        until(self, "Without the note")
        j1 = T("the probability of getting", size=32).move_to([-3.05, 0.35, 0])
        j2 = T("results at least as extreme", size=32).move_to([-3.05, -0.05, 0])
        j3 = T("under the null hypothesis", size=32).move_to([-3.05, -0.45, 0])
        self.play(FadeIn(j1), FadeIn(j2), FadeIn(j3), run_time=0.8)
        until(self, "With the note")
        nt = note(3.05, 0.95, 3.0, 1.4)
        self.play(FadeIn(nt), run_time=0.6)
        a1 = T("a small number,", size=32).move_to([3.05, -0.5, 0])
        a2 = T("below 0.05 means:", size=32).move_to([3.05, -0.9, 0])
        a3 = T("probably not chance", size=32).move_to([3.05, -1.3, 0])
        self.play(FadeIn(a1), FadeIn(a2), FadeIn(a3), run_time=0.7)
        until(self, "You wrote four lines once")
        chk = check(5.95, -0.75, color=TERRA)
        self.play(GrowFromCenter(chk), run_time=0.5)
        finish(self)


class B06_NeverWant(Scene):
    """Negative instructions: three unwanted habits are written down and crossed out."""

    def construct(self):
        nt = note(0, 0.1, 4.4, 3.2)
        lab_n = lab("the note", 0, 2.15)
        self.play(FadeIn(nt), FadeIn(lab_n), run_time=0.9)
        bans = ["no emojis", "no 'as an AI'", "no sorry-first opens"]
        ys = [0.9, 0.2, -0.5]
        waits = ["No 'as an AI language model.'", "Don't open with an apology"]
        until(self, "No emojis")
        for i, (s, y) in enumerate(zip(bans, ys)):
            tx = T(s, size=32).move_to([-0.5, y, 0])
            xm = xmark(1.45, y, s=0.24)
            self.play(FadeIn(tx), GrowFromCenter(xm), run_time=0.55)
            if i < 2:
                until(self, waits[i])
        until(self, "and they're gone")
        finish(self)


class B07_KeepFresh(Scene):
    """Keep it fresh: one line is rewritten and the note pins back into place."""

    def construct(self):
        nt = note(0, 0.05, 4.6, 3.2)
        l1 = T("keep answers short", size=32).move_to([0, 0.75, 0])
        l2 = T("beginner at statistics", size=32).move_to([0, 0.1, 0])
        l3 = T("plain English", size=32).move_to([0, -0.55, 0])
        lab_n = lab("the note", 0, 2.1)
        self.play(FadeIn(nt), FadeIn(l1), FadeIn(l2), FadeIn(l3), FadeIn(lab_n),
                  run_time=1.0)
        until(self, "Pull it out")
        pen = pencil(-2.9, 0.1)
        self.play(FadeIn(pen), run_time=0.5)
        grp = VGroup(nt, l1, l2, l3, lab_n)
        self.play(MoveAlongPath(grp, Line(np.array([0.0, 0.0, 0]),
                                          np.array([0.0, 1.0, 0]))), run_time=0.7)
        until(self, "rewrite a line")
        l2b = T("comfortable with basics", size=32).move_to([0, 1.1, 0])
        edit = Dot([2.0, 1.1, 0], radius=0.1, color=TERRA)
        self.play(FadeOut(l2), FadeIn(l2b), FadeIn(edit), run_time=0.7)
        until(self, "Review it every few months")
        cal = kw_pill("every few months", 4.35, 2.2, 3.2)
        self.play(FadeIn(cal), run_time=0.6)
        grp2 = VGroup(nt, l1, l2b, l3, lab_n, edit)
        self.play(MoveAlongPath(grp2, Line(np.array([0.0, 0.0, 0]),
                                            np.array([0.0, -1.0, 0]))), run_time=0.7)
        finish(self)


class B08_FollowsYou(Scene):
    """It follows you: the same note feeds the phone and the computer."""

    def construct(self):
        nt = note(0, 0.35, 3.4, 2.6)
        lab_n = lab("the note", 0, 2.1)
        self.play(FadeIn(nt), FadeIn(lab_n), run_time=0.8)
        until(self, "your phone and your computer")
        phone = RoundedRectangle(width=1.9, height=3.2, corner_radius=0.25,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=4).move_to([-4.0, -0.7, 0])
        lab_p = lab("phone", -4.0, -2.65)
        web = chat_window(4.0, -0.55, 3.4, 2.5)
        lab_c = lab("computer", 4.0, -2.2)
        self.play(FadeIn(phone), FadeIn(lab_p), FadeIn(web), FadeIn(lab_c),
                  run_time=0.9)
        c1 = cable([-1.7, 0.35, 0], [-3.05, -0.7, 0])
        c2 = cable([1.7, 0.35, 0], [2.3, -0.55, 0])
        self.play(Create(c1), Create(c2), run_time=0.8)
        until(self, "written once")
        finish(self)
