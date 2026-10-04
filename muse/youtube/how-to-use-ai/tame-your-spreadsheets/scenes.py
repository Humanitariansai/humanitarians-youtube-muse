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

# ═════════════════════════════ film helpers (tame-your-spreadsheets) ═════════════════════════════
DEEPKRAFT = "#9C8462"   # connector/cable edges: clear of GATE T's ink tolerance


def drop_shadow(cx, cy, w, h):
    return RoundedRectangle(width=w + 0.5, height=h + 0.5, corner_radius=0.25,
                            fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to([cx + 0.15, cy - 0.2, 0])


def sheet_grid(cx, cy, cols, rows, cw, rh):
    """Flat spreadsheet: returns (group_of_rects, cells[r][c]). Ink outline, card fill."""
    grp = VGroup()
    cells = []
    x0 = cx - cols * cw / 2
    y0 = cy + rows * rh / 2
    for r in range(rows):
        row = []
        for c in range(cols):
            rect = Rectangle(width=cw, height=rh, stroke_color=INK, stroke_width=4,
                             fill_color=CARD, fill_opacity=1)
            rect.move_to([x0 + c * cw + cw / 2, y0 - r * rh - rh / 2, 0])
            grp.add(rect)
            row.append(rect)
        cells.append(row)
    return grp, cells


def cell_text(s, x, y, size=32, color=INK):
    return T(s, size=size, color=color).move_to([x, y, 0])


def grid_fill(cells, rows_data, size=32):
    """Text mobjects centred in each cell for a rows_data table. Returns VGroup."""
    texts = VGroup()
    for r, row in enumerate(rows_data):
        for c, s in enumerate(row):
            rect = cells[r][c]
            cx, cy = rect.get_center()[0], rect.get_center()[1]
            texts.add(cell_text(s, cx, cy, size=size, color=INK if r == 0 else INK))
    return texts


# ═════════════════════════════ B00 — the messy spreadsheet ═════════════════════════════
class B00_MessySheet(Scene):
    def construct(self):
        cx, cy, cols, rows, cw, rh = -0.75, 0.15, 4, 5, 1.5, 0.66
        w, h = cols * cw, rows * rh
        shadow = drop_shadow(cx, cy, w, h)
        grid, cells = sheet_grid(cx, cy, cols, rows, cw, rh)
        self.play(FadeIn(shadow, run_time=0.4), Create(grid, run_time=1.0))
        messy = [
            ["day", "sold", "city", "date"],
            ["Mon", "120", "NYC", "3/4"],
            ["Tue", "98", "N.Y.C.", "Mar 4"],
            ["Wed", "141", "new york", "04-03"],
            ["Fri", "203", "n y c", "Mar. 4"],
        ]
        labels = grid_fill(cells, messy, size=32)
        chaotic_cell = cells[2][2]                      # "N.Y.C." — the chaotic one
        frame = SurroundingRectangle(chaotic_cell, color=INK, buff=0.06, stroke_width=5)
        self.play(FadeIn(labels, run_time=0.8), GrowFromCenter(frame, run_time=0.7))
        dot = Dot([chaotic_cell.get_center()[0] + 0.55, chaotic_cell.get_center()[1] + 0.22, 0],
                  radius=0.11, color=TERRA)
        caption = T("a messy spreadsheet", size=36).move_to([cx, cy - h / 2 - 0.62, 0])
        self.play(FadeIn(dot, run_time=0.4), FadeIn(caption, run_time=0.6))
        until(self, "it is just a table")
        finish(self)


# ═════════════════════════════ B01 — the coach: plain words in ═════════════════════════════
class B01_Coach(Scene):
    def construct(self):
        cx, cy, cols, rows, cw, rh = -2.6, 0.15, 4, 5, 1.5, 0.66
        w, h = cols * cw, rows * rh
        shadow = drop_shadow(cx, cy, w, h)
        grid, cells = sheet_grid(cx, cy, cols, rows, cw, rh)
        tidyish = [
            ["day", "sold", "city", "date"],
            ["Mon", "120", "NYC", "3/4"],
            ["Tue", "98", "NYC", "3/5"],
            ["Wed", "141", "NYC", "3/6"],
            ["Thu", "87", "NYC", "3/7"],
        ]
        labels = grid_fill(cells, tidyish, size=32)
        self.play(FadeIn(shadow, run_time=0.4), Create(grid, run_time=1.0), FadeIn(labels, run_time=0.8))
        iso = Iso(3.0, 0.9, 1.5)
        page = iso.page(0, 0, 0, w=1.3, d=1.5)
        bubble = pill(3.35, -1.05, 4.5)
        prompt = T("write me the formula that…", size=32).move_to([3.35, -1.05, 0])
        cable = Line([2.35, 0.55, 0], [0.45, 0.35, 0], color=DEEPKRAFT, stroke_width=6)
        self.play(FadeIn(page, run_time=0.7), FadeIn(bubble, run_time=0.7))
        self.play(FadeIn(prompt, run_time=0.5), Create(cable, run_time=0.6))
        cap1 = T("plain words", size=36).move_to([3.35, -1.95, 0])
        cap2 = T("your sheet", size=36).move_to([cx, cy - h / 2 - 0.62, 0])
        self.play(FadeIn(cap1, run_time=0.4), FadeIn(cap2, run_time=0.4))
        until(self, "Plain English in, formula out")
        finish(self)


# ═════════════════════════════ B02 — the formula lands ═════════════════════════════
class B02_Formula(Scene):
    def construct(self):
        cx, cy, cols, rows, cw, rh = -2.6, 0.15, 4, 5, 1.5, 0.66
        w, h = cols * cw, rows * rh
        shadow = drop_shadow(cx, cy, w, h)
        grid, cells = sheet_grid(cx, cy, cols, rows, cw, rh)
        data = [
            ["day", "sold", "price", "date"],
            ["Mon", "120", "4", "3/4"],
            ["Tue", "98", "4", "3/5"],
            ["Wed", "141", "4", "3/6"],
            ["", "", "", ""],
        ]
        labels = grid_fill(cells, data, size=32)
        iso = Iso(3.0, 0.9, 1.5)
        page = iso.page(0, 0, 0, w=1.3, d=1.5)
        self.play(FadeIn(shadow, run_time=0.4), Create(grid, run_time=1.0),
                  FadeIn(labels, run_time=0.8), FadeIn(page, run_time=0.7))
        col_b = VGroup(*[cells[r][1] for r in range(1, 4)])
        bracket = SurroundingRectangle(col_b, color=INK, buff=0.08, stroke_width=6)
        b2 = T("B2", size=34).move_to([col_b[0].get_center()[0] + 1.05, col_b[0].get_center()[1], 0])
        b31 = T("B31", size=34).move_to([col_b[-1].get_center()[0] + 1.1, col_b[-1].get_center()[1], 0])
        self.play(GrowFromCenter(bracket, run_time=0.7), FadeIn(b2, run_time=0.4), FadeIn(b31, run_time=0.4))
        formula = T("=SUM(B2:B31)", size=36).move_to([-1.15, -1.47, 0])
        leader = Line([-2.55, -1.47, 0], [-2.0, -1.47, 0], color=INK, stroke_width=4)
        tick = check(0.15, -1.35, s=0.16, w=7)
        cap = T("the formula", size=36).move_to([-1.15, -2.2, 0])
        self.play(FadeIn(formula, run_time=0.5), Create(leader, run_time=0.4),
                  GrowFromCenter(tick, run_time=0.4), FadeIn(cap, run_time=0.4))
        until(self, "add up everything from B 2 to B 31")
        finish(self)


# ═════════════════════════════ B03 — sanity-check the formula ═════════════════════════════
class B03_Check(Scene):
    def construct(self):
        cx, cy, cols, rows, cw, rh = -2.6, 0.15, 4, 5, 1.5, 0.66
        w, h = cols * cw, rows * rh
        shadow = drop_shadow(cx, cy, w, h)
        grid, cells = sheet_grid(cx, cy, cols, rows, cw, rh)
        data = [
            ["day", "sold", "price", "date"],
            ["Mon", "120", "4", "3/4"],
            ["Tue", "98", "4", "3/5"],
            ["Wed", "141", "4", "3/6"],
            ["", "", "", ""],
        ]
        labels = grid_fill(cells, data, size=32)
        formula = T("=SUM(B2:B31)", size=36).move_to([-1.15, -1.47, 0])
        self.play(FadeIn(shadow, run_time=0.4), Create(grid, run_time=1.0),
                  FadeIn(labels, run_time=0.8), FadeIn(formula, run_time=0.5))
        wrong = VGroup(*[cells[r][2] for r in range(1, 4)])
        wrong_bracket = SurroundingRectangle(wrong, color=INK, buff=0.08, stroke_width=6)
        wx, wy = wrong[1].get_center()[0], wrong[1].get_center()[1]
        cross = VGroup(
            Line([wx - 0.3, wy + 0.3, 0], [wx + 0.3, wy - 0.3, 0], color=INK, stroke_width=8),
            Line([wx - 0.3, wy - 0.3, 0], [wx + 0.3, wy + 0.3, 0], color=INK, stroke_width=8))
        self.play(GrowFromCenter(wrong_bracket, run_time=0.6), FadeIn(cross, run_time=0.4))
        cap = T("check 5 rows", size=36).move_to([-2.6, -2.35, 0])
        self.play(FadeIn(cap, run_time=0.4))
        until(self, "sanity-check every formula on a small sample")
        self.play(FadeOut(wrong_bracket, run_time=0.3), FadeOut(cross, run_time=0.3))
        mx, my = cells[2][1].get_center()[0], cells[2][1].get_center()[1]
        lens = Circle(radius=0.95, color=INK, stroke_width=6).move_to([mx, my, 0])
        handle = Line([mx + 0.62, my - 0.72, 0], [mx + 1.25, my - 1.35, 0], color=INK, stroke_width=8)
        right = VGroup(*[cells[r][1] for r in range(1, 4)])
        right_bracket = SurroundingRectangle(right, color=INK, buff=0.08, stroke_width=6)
        tick = check(mx + 1.55, my + 0.55, s=0.2, w=8)
        self.play(Create(lens, run_time=0.5), Create(handle, run_time=0.4),
                  GrowFromCenter(right_bracket, run_time=0.5), GrowFromCenter(tick, run_time=0.5))
        finish(self)


# ═════════════════════════════ B04 — cleanup: messy in, clean out ═════════════════════════════
class B04_Cleanup(Scene):
    def construct(self):
        cx, cy, cols, rows, cw, rh = 0.0, 0.2, 3, 4, 2.0, 0.72
        w, h = cols * cw, rows * rh
        shadow = drop_shadow(cx, cy, w, h)
        grid, cells = sheet_grid(cx, cy, cols, rows, cw, rh)
        messy = [
            ["date", "city", "sold"],
            ["3/4", "NYC", "120"],
            ["Mar 4", "N.Y.C.", "98"],
            ["04-03", "new york", "141"],
        ]
        messy_labels = grid_fill(cells, messy, size=32)
        self.play(FadeIn(shadow, run_time=0.4), Create(grid, run_time=1.0), FadeIn(messy_labels, run_time=0.8))
        scan = Line([cx - w / 2 - 0.2, cy + h / 2 - 0.1, 0], [cx + w / 2 + 0.2, cy + h / 2 - 0.1, 0],
                    color=TERRA, stroke_width=8)
        messy_tag = T("messy", size=36).move_to([cx + w / 2 + 1.05, cy + 0.9, 0])
        self.play(Create(scan, run_time=0.3), FadeIn(messy_tag, run_time=0.3))
        self.play(scan.animate.shift(DOWN * (h - 0.2)), run_time=0.6)
        self.play(FadeOut(scan, run_time=0.2))
        tidy = [
            ["date", "city", "sold"],
            ["2026-03-04", "New York", "120"],
            ["2026-03-04", "New York", "98"],
            ["2026-03-04", "New York", "141"],
        ]
        tidy_labels = grid_fill(cells, tidy, size=30)
        clean_tag = T("clean", size=36).move_to([cx + w / 2 + 1.05, cy + 0.9, 0])
        self.play(FadeOut(messy_labels, run_time=0.4), FadeOut(messy_tag, run_time=0.3))
        self.play(FadeIn(tidy_labels, run_time=0.8), FadeIn(clean_tag, run_time=0.4))
        until(self, "make everything consistent")
        finish(self)


# ═════════════════════════════ B05 — what's interesting: one tall bar ═════════════════════════════
class B05_Insight(Scene):
    def construct(self):
        base_y = -1.9
        xs = [-2.9, -1.75, -0.6, 0.55, 1.7, 2.85]
        heights = [1.1, 0.9, 1.3, 1.0, 1.5, 2.8]
        days = ["M", "T", "W", "T", "F", "S"]
        fills = [BAR1, BAR2, BAR3, BAR1, BAR2, BAR3]
        baseline = Line([-3.6, base_y, 0], [3.6, base_y, 0], color=INK, stroke_width=5)
        bars = VGroup()
        for x, hh, f in zip(xs, heights, fills):
            bar = Rectangle(width=0.85, height=hh, stroke_color=INK, stroke_width=4,
                            fill_color=f, fill_opacity=1)
            bar.move_to([x, base_y + hh / 2, 0])
            bars.add(bar)
        self.play(Create(baseline, run_time=0.5),
                  LaggedStart(*[GrowFromEdge(bar, DOWN) for bar in bars], lag_ratio=0.12, run_time=1.6))
        tall_x = xs[-1]
        dot = Dot([tall_x, base_y + heights[-1] + 0.18, 0], radius=0.13, color=TERRA)
        sat = T("Saturday", size=36).move_to([tall_x, base_y + heights[-1] + 0.75, 0])
        day_labels = VGroup(*[T(d, size=32).move_to([x, base_y - 0.45, 0]) for d, x in zip(days, xs)])
        self.play(FadeIn(day_labels, run_time=0.5), FadeIn(dot, run_time=0.4), FadeIn(sat, run_time=0.5))
        until(self, "One tall bar")
        finish(self)


# ═════════════════════════════ B06 — the tamed sheet ═════════════════════════════
class B06_Payoff(Scene):
    def construct(self):
        cx, cy, cols, rows, cw, rh = -2.2, 0.15, 4, 5, 1.5, 0.66
        w, h = cols * cw, rows * rh
        shadow = drop_shadow(cx, cy, w, h)
        grid, cells = sheet_grid(cx, cy, cols, rows, cw, rh)
        tidy = [
            ["day", "sold", "city", "date"],
            ["Mon", "120", "New York", "2026-03-04"],
            ["Tue", "98", "New York", "2026-03-04"],
            ["Wed", "141", "New York", "2026-03-04"],
            ["", "", "", ""],
        ]
        labels = grid_fill(cells, tidy, size=30)
        formula = T("=SUM(B2:B31)", size=34).move_to([-1.15, -1.47, 0])
        self.play(FadeIn(shadow, run_time=0.4), Create(grid, run_time=1.0),
                  FadeIn(labels, run_time=0.8), FadeIn(formula, run_time=0.5))
        mini_base = -1.2
        mini = VGroup()
        for i, (x, hh, f) in enumerate([(2.3, 0.8, BAR1), (3.2, 1.2, BAR2), (4.1, 1.7, BAR3)]):
            bar = Rectangle(width=0.6, height=hh, stroke_color=INK, stroke_width=4,
                            fill_color=f, fill_opacity=1)
            bar.move_to([x, mini_base + hh / 2, 0])
            mini.add(bar)
        mini_line = Line([1.9, mini_base, 0], [4.5, mini_base, 0], color=INK, stroke_width=4)
        self.play(Create(mini_line, run_time=0.4),
                  LaggedStart(*[GrowFromEdge(bar, DOWN) for bar in mini], lag_ratio=0.2, run_time=1.0))
        big = check(2.9, 1.35, s=0.42, w=10)
        cap = T("you are in charge", size=36).move_to([cx, cy - h / 2 - 0.62, 0])
        self.play(GrowFromCenter(big, run_time=0.6), FadeIn(cap, run_time=0.4))
        until(self, "A tamed spreadsheet")
        finish(self)
