"""scenes.py — show-tell: Meetings into Notes (Liam, Teardown, claude-liam).

Nine drawn body beats, one Manim scene per beat. The iso_kit block is pasted
verbatim at the top (Gate A copies only this file — never import the kit).
Film helpers (chat window, doc cards, labels, transcript page, fragments,
bullets, owner pills, email card, lock) follow the kit; every scene class is
written literally as `class BNN_Name(Scene):`.

Drawing laws obeyed: labels sit beside objects (never inside, never on
terracotta); terracotta only for dots/checks; chart blocks not used; type >=
32; every coordinate inside +-6.2 x +-3.3; every scene adds a new non-text
shape after its first frame; no path_arc, no ease_in_quad/ease_out_cubic; no
MoveAlongPath + .animate on the same object in one play; major motion is kept
off the clip midpoint via until() phrase timing (see SHOTLIST.md).

Pacing: until()/finish() read beat_sheet.json beside this file (the measured
Kokoro audio at render time); with no sheet they degrade to short waits.
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


# ═════════════════════════════ film helpers (meetings-into-notes) ═════════════════════════════
def chat_window(cx=0.0, cy=0.0, w=5.2, h=3.1, composer=True, wide_composer=False):
    """Front-facing Claude chat window: ink-outlined cream card, thin dark title
    strip (carries contrast on the pale panel), composer pill at the bottom."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.18, fill_color=CARD,
                            fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    bar = RoundedRectangle(width=w - 0.04, height=0.5, corner_radius=0.15, fill_color=DARK_TOP,
                           fill_opacity=1, stroke_width=0).move_to([cx, cy + h / 2 - 0.26, 0])
    parts = [body, bar]
    if composer:
        cw = w * (0.86 if wide_composer else 0.8)
        comp = RoundedRectangle(width=cw, height=0.58, corner_radius=0.29, fill_color="#FFFFFF",
                                fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([cx, cy - h / 2 + 0.6, 0])
        parts.append(comp)
    return VGroup(*parts)


def doc_card(x, y, w=1.5, h=1.9, outline=DIM, dot=True, lines=3):
    """Small flat document card. Grey outline so it stays legible inside
    ink-outlined containers (GATE T: ink-in-ink reads as overlapping text)."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=outline, stroke_width=2).move_to([x, y, 0])
    ls = VGroup(*[Line([x - w / 2 + 0.24, y + h / 2 - 0.42 - i * 0.36, 0],
                       [x + w / 2 - 0.24 - (0.35 if i == lines - 1 else 0), y + h / 2 - 0.42 - i * 0.36, 0],
                       color=GHOST, stroke_width=4) for i in range(lines)])
    parts = [card, ls]
    if dot:
        parts.append(Dot([x - w / 2 + 0.3, y + h / 2 - 0.24, 0], radius=0.06, color=TERRA))
    return VGroup(*parts)


def tag(text, lx, ly, ox, oy, size=36):
    """Ink label at (lx, ly) with a dim leader line from object point (ox, oy).
    The leader stops 0.35 units short of the label (GATE T: a touching leader fails)."""
    lab = T(text, size=size).move_to([lx, ly, 0])
    half = lab.width / 2 + 0.35
    d = np.array([lx - ox, ly - oy, 0.0])
    n = np.linalg.norm(d)
    d = d / n if n > 1e-6 else np.array([1.0, 0.0, 0.0])
    end = np.array([lx, ly, 0.0]) - d * half
    line = Line([ox, oy, 0], end, color=DIM, stroke_width=2)
    return VGroup(line, lab)


def transcript_page(x, y, w=2.6, h=3.4):
    """The film's messy transcript: white card, uneven ghost text lines
    (the ramble), one terracotta dot. Grey outline keeps it legible."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    fracs = [0.9, 0.55, 1.0, 0.7, 0.45, 0.95, 0.6, 0.85]
    ls = VGroup(*[Line([x - w / 2 + 0.24, y + h / 2 - 0.55 - i * 0.36, 0],
                       [x - w / 2 + 0.24 + (w - 0.7) * f, y + h / 2 - 0.55 - i * 0.36, 0],
                       color=GHOST, stroke_width=4) for i, f in enumerate(fracs)])
    dot = Dot([x - w / 2 + 0.3, y + h / 2 - 0.3, 0], radius=0.06, color=TERRA)
    return VGroup(card, ls, dot)


def scribbles(x, y):
    """Jagged ink polylines across the transcript (straight segments only —
    no curves, so the layout audit's --curve-strict stays quiet)."""
    paths = [
        [(-1.1, -0.9), (-0.6, -0.7), (-0.9, -0.4), (-0.3, -0.5)],
        [(-0.7, 0.2), (-0.2, 0.4), (-0.5, 0.7), (0.1, 0.6)],
        [(-1.0, 1.0), (-0.4, 1.2), (-0.7, 1.45)],
    ]
    return VGroup(*[VMobject().set_points_as_corners(
        [np.array([x + dx, y + dy, 0]) for dx, dy in p]).set_stroke(INK, width=3)
        for p in paths])


def bubble(x, y, text):
    """Small ink-outlined speech bubble with one short word."""
    lab = T(text, size=32).move_to([x, y - 0.02, 0])
    bg = RoundedRectangle(width=lab.width + 0.5, height=0.55, corner_radius=0.27,
                          fill_color="#FFFFFF", fill_opacity=1,
                          stroke_color=INK, stroke_width=2).move_to([x, y, 0])
    return VGroup(bg, lab)


def fragment_card(x, y, text, w=2.3):
    """A rough-notes fragment: white card with one short unfinished line."""
    card = RoundedRectangle(width=w, height=0.62, corner_radius=0.12, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    lab = T(text, size=32).move_to([x, y - 0.02, 0])
    return VGroup(card, lab)


def owner_pill(x, y, name):
    """Owner tag: ink-outlined pill with a name."""
    lab = T(name, size=32).move_to([x, y - 0.02, 0])
    bg = RoundedRectangle(width=lab.width + 0.5, height=0.5, corner_radius=0.25,
                          fill_color="#FFFFFF", fill_opacity=1,
                          stroke_color=INK, stroke_width=2).move_to([x, y, 0])
    return VGroup(bg, lab)


def email_card(x, y, w=2.2, h=1.6):
    """A follow-up email: white card with an ink envelope glyph."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    env = RoundedRectangle(width=w * 0.62, height=h * 0.5, corner_radius=0.06, fill_color=CARD,
                           fill_opacity=1, stroke_color=INK, stroke_width=2.5).move_to([x, y, 0])
    flap = VGroup(Line([x - w * 0.31, y + h * 0.25, 0], [x, y, 0], color=INK, stroke_width=2.5),
                  Line([x, y, 0], [x + w * 0.31, y + h * 0.25, 0], color=INK, stroke_width=2.5))
    return VGroup(card, env, flap)


def lock(x, y, s=1.0):
    """A padlock, drawn large with ink outlines (GATE T: tiny icons read as text)."""
    body = RoundedRectangle(width=0.9 * s, height=0.7 * s, corner_radius=0.1, fill_color=CARD,
                            fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y - 0.1 * s, 0])
    shackle = Arc(radius=0.3 * s, angle=PI, arc_center=[x, y + 0.25 * s, 0],
                  stroke_color=INK, stroke_width=4)
    hole = Dot([x, y - 0.05 * s, 0], radius=0.07 * s, color=INK)
    return VGroup(shackle, body, hole)


# ═════════════════════════════ scenes ═════════════════════════════
class B00_RamblingMeeting(Scene):
    """The pain: a rambling transcript page; tangled lines draw; three bubbles
    land, each remembering a different version of the decision."""

    def construct(self):
        page = transcript_page(-1.2, 0.0)
        lab = tag("the meeting", 2.6, 1.9, 0.1, 1.2)
        self.play(FadeIn(page), FadeIn(lab), run_time=1.0)
        until(self, "Nobody writes it down")
        tang = scribbles(-1.2, 0.0)
        self.play(Create(tang), run_time=0.9)
        until(self, "By Friday")
        bubs = VGroup(bubble(-3.4, 2.2, "Friday?"), bubble(-1.2, 2.4, "Monday?"),
                       bubble(1.0, 2.2, "June?"))
        self.play(FadeIn(bubs), run_time=0.8)
        finish(self)


class B01_PasteIt(Scene):
    """What it is: the transcript page slides into the composer; a reply card
    grows beside the window with a terracotta check."""

    def construct(self):
        win = chat_window(0.8, 0.0)
        page = transcript_page(-3.6, 0.3, w=2.4, h=2.8)
        lab = tag("mess in", -3.6, 2.3, -3.6, 1.7)
        self.play(FadeIn(win), FadeIn(page), FadeIn(lab), run_time=1.0)
        until(self, "Paste the transcript")
        self.play(page.animate.scale(0.32).move_to([0.8, -0.95, 0]), run_time=0.9)
        until(self, "No formatting")
        reply = doc_card(4.7, 0.5, w=2.0, h=1.4, dot=False, lines=2)
        tick = check(4.7, 0.5, s=0.25, color=TERRA)
        lab2 = tag("notes out", 4.7, 1.9, 4.7, 1.2)
        self.play(Create(reply), FadeIn(tick), FadeIn(lab2), run_time=0.9)
        finish(self)


class B02_RoughNotes(Scene):
    """The reassurance: three fragment cards drop into the window as-is;
    a terracotta check lands on the composer."""

    def construct(self):
        win = chat_window(0.0, 0.0)
        lab = tag("rough notes", -4.3, 1.3, -2.6, 0.9)
        self.play(FadeIn(win), FadeIn(lab), run_time=1.0)
        until(self, "already", lead=0.6)
        frags = VGroup(fragment_card(0.0, 1.0, "launch??"),
                       fragment_card(0.0, 0.3, "Sam \u2014 paymt"),
                       fragment_card(0.0, -0.4, "release notes?"))
        self.play(FadeIn(frags), run_time=0.9)
        until(self, "Claude reads the sense")
        tick = check(0.0, -0.95, s=0.22, color=TERRA)
        self.play(FadeIn(tick), run_time=0.6)
        finish(self)


class B03_ThreeBullets(Scene):
    """Prompt 1: the exact prompt sits in the composer; a reply grows with
    three bullet lines; terracotta dots land on the spoken payoff."""

    def construct(self):
        win = chat_window(0.0, 0.0, wide_composer=True)
        prompt = T("summarize this meeting in 3 bullets", size=32).move_to([0.0, -0.95, 0])
        self.play(FadeIn(win), FadeIn(prompt), run_time=1.0)
        until(self, "Three, not ten")
        body = RoundedRectangle(width=3.6, height=1.5, corner_radius=0.1, fill_color="#FFFFFF",
                                fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([0.0, 0.55, 0])
        lines = VGroup(*[Line([-1.25, 0.95 - i * 0.38, 0], [1.5 - (0.7 if i == 2 else 0), 0.95 - i * 0.38, 0],
                               color=INK, stroke_width=5) for i in range(3)])
        lab = tag("summarize", 3.3, 1.6, 1.8, 1.1)
        self.play(Create(body), Create(lines), FadeIn(lab), run_time=0.8)
        until(self, "about thirty seconds")
        dots = VGroup(*[Dot([-1.48, 0.95 - i * 0.38, 0], radius=0.07, color=TERRA) for i in range(3)])
        self.play(FadeIn(dots), run_time=0.6)
        finish(self)


class B04_DecisionsOwners(Scene):
    """Prompt 2: the exact prompt in two lines; a reply card grows with two
    decision rows, each carrying an owner pill (Maya, Sam)."""

    def construct(self):
        win = chat_window(-0.6, 0.0)
        p1 = T("list every decision", size=32).move_to([-0.6, 0.78, 0])
        p2 = T("and who owns the next step", size=32).move_to([-0.6, 0.4, 0])
        self.play(FadeIn(win), FadeIn(p1), FadeIn(p2), run_time=1.0)
        until(self, "This is the one that matters most")
        card = RoundedRectangle(width=3.0, height=1.9, corner_radius=0.1, fill_color="#FFFFFF",
                                fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([3.8, 0.3, 0])
        lab = tag("owners", 3.8, 1.95, 3.8, 1.25)
        self.play(Create(card), FadeIn(lab), run_time=0.8)
        until(self, "who actually does what")
        rows = VGroup(
            VGroup(Line([2.7, 0.62, 0], [3.95, 0.62, 0], color=INK, stroke_width=5),
                   owner_pill(4.6, 0.62, "Maya")),
            VGroup(Line([2.7, -0.02, 0], [3.95, -0.02, 0], color=INK, stroke_width=5),
                   owner_pill(4.6, -0.02, "Sam")))
        self.play(FadeIn(rows), run_time=0.8)
        finish(self)


class B05_Unresolved(Scene):
    """Prompt 3: two loose-end cards drop in; ink '?' marks with rings land
    on the spoken payoff — the hunt for what nobody resolved."""

    def construct(self):
        c1 = doc_card(-1.6, 0.3, w=2.2, h=1.4, dot=False, lines=2)
        c2 = doc_card(1.6, 0.3, w=2.2, h=1.4, dot=False, lines=2)
        lab = tag("unresolved", 0.0, 2.0, 0.0, 1.05)
        until(self, "what was left unresolved")
        self.play(FadeIn(c1), FadeIn(c2), FadeIn(lab), run_time=0.8)
        until(self, "This prompt hunts them down")
        q1 = T("?", size=56).move_to([-1.6, 0.3, 0])
        q2 = T("?", size=56).move_to([1.6, 0.3, 0])
        r1 = Circle(radius=0.34, stroke_color=INK, stroke_width=3).move_to([-1.6, 0.3, 0])
        r2 = Circle(radius=0.34, stroke_color=INK, stroke_width=3).move_to([1.6, 0.3, 0])
        self.play(FadeIn(q1), FadeIn(q2), Create(r1), Create(r2), run_time=0.7)
        finish(self)


class B06_Example(Scene):
    """The fictional example end-to-end: the transcript page lands; three
    output cards spring out of the window; the unresolved '?' gets circled."""

    def construct(self):
        page = transcript_page(-3.8, 0.3)
        win = chat_window(0.8, 0.3, w=4.4, h=2.9)
        lab = tag("example", 2.2, 2.3, 1.6, 1.75)
        self.play(FadeIn(page), FadeIn(win), FadeIn(lab), run_time=1.0)
        until(self, "Transcript in")
        # card 1: summary — three lines
        card1 = VGroup(
            RoundedRectangle(width=2.6, height=1.3, corner_radius=0.1, fill_color="#FFFFFF",
                             fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([4.3, 1.65, 0]),
            T("summary", size=32).move_to([4.3, 2.02, 0]),
            VGroup(*[Line([3.35, 1.7 - i * 0.32, 0], [5.25 - (0.6 if i == 2 else 0), 1.7 - i * 0.32, 0],
                           color=INK, stroke_width=5) for i in range(3)]))
        # card 2: decisions — two lines
        card2 = VGroup(
            RoundedRectangle(width=2.6, height=1.3, corner_radius=0.1, fill_color="#FFFFFF",
                             fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([4.3, 0.2, 0]),
            T("decisions", size=32).move_to([4.3, 0.57, 0]),
            VGroup(*[Line([3.35, 0.25 - i * 0.34, 0], [5.25 - (0.5 if i == 1 else 0), 0.25 - i * 0.34, 0],
                           color=INK, stroke_width=5) for i in range(2)]))
        # card 3: actions — two checked rows + one unresolved '?' row
        rows3 = VGroup(
            VGroup(check(3.35, -1.16, s=0.12, color=TERRA, w=5),
                   Line([3.65, -1.16, 0], [5.2, -1.16, 0], color=INK, stroke_width=5)),
            VGroup(check(3.35, -1.44, s=0.12, color=TERRA, w=5),
                   Line([3.65, -1.44, 0], [5.2, -1.44, 0], color=INK, stroke_width=5)),
            VGroup(T("?", size=40).move_to([3.32, -1.72, 0]),
                   Line([3.65, -1.72, 0], [5.2, -1.72, 0], color=INK, stroke_width=5)))
        card3 = VGroup(
            RoundedRectangle(width=2.6, height=1.3, corner_radius=0.1, fill_color="#FFFFFF",
                             fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([4.3, -1.25, 0]),
            T("actions", size=32).move_to([4.3, -0.88, 0]),
            rows3)
        self.play(FadeIn(card1), FadeIn(card2), FadeIn(card3), run_time=1.0)
        until(self, "unresolved question")
        ring = Circle(radius=0.3, stroke_color=INK, stroke_width=3).move_to([3.32, -1.72, 0])
        self.play(Create(ring), run_time=0.6)
        finish(self)


class B07_KeepAsking(Scene):
    """Keep asking: the follow-up question sits in the composer; an email card
    grows beside the window; a check stamps it."""

    def construct(self):
        win = chat_window(-0.8, 0.0, wide_composer=True)
        q = T("Draft the follow-up email to the team", size=32).move_to([-0.8, -0.95, 0])
        lab = tag("keep asking", -0.8, 2.2, -0.8, 1.55)
        self.play(FadeIn(win), FadeIn(q), FadeIn(lab), run_time=1.0)
        until(self, "Draft the follow-up email")
        ecard = email_card(3.6, 0.2)
        self.play(GrowFromCenter(ecard), run_time=0.8)
        until(self, "The transcript is now")
        tick = check(3.6, 0.2, s=0.25, color=TERRA)
        self.play(FadeIn(tick), run_time=0.6)
        finish(self)


class B08_CheckRules(Scene):
    """The privacy line: the transcript page drops; an ink lock lands over it;
    a rough-notes fragment appears as the safer alternative."""

    def construct(self):
        page = transcript_page(-1.0, 0.0)
        lab = tag("check your rules", 3.1, 1.6, 0.3, 1.2)
        self.play(FadeIn(page), FadeIn(lab), run_time=1.0)
        until(self, "Check your workplace rules")
        lk = lock(-1.0, 0.2, s=1.1)
        self.play(FadeIn(lk), run_time=0.8)
        until(self, "If the rules say no")
        frag = fragment_card(3.0, -1.0, "rough notes")
        self.play(FadeIn(frag), run_time=0.7)
        finish(self)
