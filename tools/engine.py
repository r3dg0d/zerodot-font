"""DotZero procedural engine: 5x7 dot matrices -> independent round dots.

Construction model:
  * a fixed pitch of 110 units in both directions (monospaced 6-dot cell);
  * every lit matrix position becomes one closed dot contour; dots never merge,
    so counters are always preserved and the display texture stays legible;
  * weight changes *dot diameter* and *dot squareness* (superellipse handle
    length): Thin is a sparse pin-prick LED, Black is a fat, slightly
    squared dot like a high-brightness segment display;
  * italics slant the matrix (dot centres sheared 10 degrees) while dots stay
    round, as on a slanted physical display.
Every lit dot is drawn at every weight with the same 4-curve structure, so the
masters interpolate cleanly into a variable font.
"""
from __future__ import annotations

import math
import os
import re
import unicodedata

from ttcore import (BLOCK_RANGE, BOX_RANGE, COMPOSITES, POWERLINE, Glyph,
                    glyph_name, parse_box_name)

HERE = os.path.dirname(os.path.abspath(__file__))
MAPS = os.path.join(HERE, "..", "sources", "dotmatrix.txt")

P = 110             # dot pitch
COLS = 6            # cell: 5 dots + 1 gap
ADV = P * COLS      # 660, monospaced
SLANT = math.tan(math.radians(10))
DOT = {100: (28, .5523), 200: (42, .5523), 300: (56, .5523), 400: (72, .5523), 500: (82, .60),
       600: (90, .64), 700: (97, .68), 800: (102, .72), 900: (106, .76)}

FAMILY = {
    "name": "DotZero", "ps": "DotZero", "version": (1, 0), "vendor": "R3DG",
    "copyright": "Copyright 2026 Vincent Patrick Chambers (https://github.com/r3dg0d/dotzero-font), with Reserved Font Name \"DotZero\".",
    "designer": "Vincent Patrick Chambers", "url": "https://github.com/r3dg0d/dotzero-font",
    "description": "DOT//ZERO: an original dot-matrix display family. Every glyph is a 5x7 matrix of round dots.",
    "upm": 1000, "italic_angle": 10.0, "monospace": True,
    "metrics": {"ascender": 770, "descender": -220, "cap": 770, "x": 550,
                "line_ascent": 1045, "line_descent": 275, "win_ascent": 1100, "win_descent": 330,
                "underline_pos": -165, "underline_thick": 70},
}
BOX_TOP, BOX_BOTTOM = 1045, -275
MIDY = (BOX_TOP + BOX_BOTTOM) / 2  # 385 = row-3 centre

ACCENTS = {
    "grave": ["#..", ".#."], "acute": ["..#", ".#."], "circumflex": [".#.", "#.#"],
    "tilde": [".#.#", "#.#."], "dieresis": ["#.#"], "ring": ["##", "##"],
    "cedilla": [".#", "#."],
}


def load_maps():
    entries, order = {}, []
    with open(MAPS) as fh:
        blocks = re.split(r"\n\s*\n", fh.read())
    for blk in blocks:
        lines = [l for l in blk.strip().splitlines() if l and not l.startswith("# ")]
        if not lines:
            continue
        head = lines[0].split()
        name, cp, top = head[0], head[1], int(head[2])
        entries[name] = {"cp": None if cp == "-" else int(cp, 16), "top": top,
                         "rows": lines[1:], "dir": head[3:]}
        order.append(name)
    for name in order:
        e = entries[name]
        if e["dir"] and e["dir"][0] == "blank":
            e["rows"], e["blank"] = ["....."], True
        elif e["dir"]:
            op, src = e["dir"]
            rows = entries[src]["rows"]
            e["blank"] = entries[src].get("blank", False)
            if op == "=mirror":
                rows = [r[::-1] for r in rows]
            elif op == "=rot":
                rows = [r[::-1] for r in reversed(rows)]
            elif op == "=vflip":
                rows = list(reversed(rows))
            e["rows"] = list(rows)
    for name in order:
        rows = entries[name]["rows"]
        assert all(len(r) == len(rows[0]) for r in rows), name
    return order, entries


def lit(rows, top, dx=0):
    return {(c + dx, top - i) for i, r in enumerate(rows) for c, ch in enumerate(r) if ch == "#"}


def centre(c, h, italic, cols=5):
    x0 = (ADV - cols * P) / 2 + P / 2
    x = x0 + c * P
    y = h * P + P / 2
    if italic:
        x += (y - 300) * SLANT
    return x, y


def dot_glyph(name, cps, dots, weight, italic, cols=5):
    d, k = DOT[weight]
    g = Glyph(name, list(cps), ADV)
    for (c, h) in sorted(dots, key=lambda t: (-t[1], t[0])):
        x, y = centre(c, h, italic, cols)
        g.ellipse(x, y, d / 2, d / 2, k)
    return g


def accent_dots(cols, acc, upper):
    rows = ACCENTS[acc]
    dx = (cols - len(rows[0]) + 1) // 2
    if acc == "cedilla":
        return lit(rows, -1, dx)
    top = (8 if upper else 6) if len(rows) > 1 else (7 if upper else 6)
    if acc == "ring":
        top = 8 if upper else 6
    return lit(rows, top, dx)


# --------------------------------------------------------- terminal glyphs
def box_glyph(cp, weight, italic):
    """Box drawing as dotted rules on the same 110-unit pitch, so dotted lines
    continue seamlessly across cells (edge dots are shared by neighbours)."""
    d, k = DOT[weight]
    light = max(d, 44)
    heavy = min(light * 1.45, 108)
    g = Glyph(glyph_name(cp), [cp], ADV)
    cx = ADV / 2
    spec = parse_box_name(cp)
    name = unicodedata.name(chr(cp))
    pts = {}

    def put(x, y, dia):
        key = (round(x), round(y))
        pts[key] = max(pts.get(key, 0), dia)

    def arm(direction, w):
        dia = heavy if w == 2 else light
        offs = (-P / 2, P / 2) if w == 3 else (0,)
        for off in offs:
            if direction in ("left", "right"):
                xs = range(0, 4) if direction == "left" else range(3, 7)
                for i in xs:
                    put(i * P, MIDY + off, dia)
            else:
                ys = range(0, 7) if direction == "down" else range(6, 13)
                for j in ys:
                    put(cx + off, BOX_BOTTOM + j * P, dia)

    if spec:
        for dd, w in spec.items():
            arm(dd, w)
    elif "DASH" in name:
        n = 2 if "DOUBLE DASH" in name else 3 if "TRIPLE" in name else 4
        dia = heavy if "HEAVY" in name else light
        if "HORIZONTAL" in name:
            for i in range(n):
                put(P / 2 + i * (ADV - P) / max(n - 1, 1), MIDY, dia)
        else:
            for i in range(n):
                put(cx, BOX_BOTTOM + P + i * (BOX_TOP - BOX_BOTTOM - 2 * P) / (n - 1), dia)
    elif "ARC" in name:
        vd = "up" if " UP " in f" {name} " else "down"
        hd = "right" if "RIGHT" in name else "left"
        sx, sy = (1 if hd == "right" else -1), (1 if vd == "up" else -1)
        for j in range(2, 7):
            put(cx, MIDY + sy * j * P, light)
        for i in range(2, 4):
            put(cx + sx * i * P, MIDY, light)
        put(cx + sx * P * 0.8, MIDY + sy * P * 0.8, light)
    elif "DIAGONAL" in name:
        n = 12
        for dd in ([1] if "UPPER RIGHT TO LOWER LEFT" in name else []) + \
                  ([-1] if "UPPER LEFT TO LOWER RIGHT" in name else []) + ([1, -1] if "CROSS" in name else []):
            for i in range(n + 1):
                x = ADV * i / n
                y = BOX_BOTTOM + (BOX_TOP - BOX_BOTTOM) * (i / n if dd == 1 else 1 - i / n)
                put(x, y, light)
    for (x, y), dia in sorted(pts.items()):
        g.ellipse(x, y, dia / 2, dia / 2, k)
    return g


def block_glyph(cp, weight, italic):
    """Blocks are solid (terminal UIs depend on them tiling); shades are dot fields."""
    g = Glyph(glyph_name(cp), [cp], ADV)
    T, B, W = BOX_TOP, BOX_BOTTOM, ADV
    H = T - B
    if 0x2581 <= cp <= 0x2588:
        g.rect(0, B, W, B + H * (cp - 0x2580) / 8)
    elif cp == 0x2580:
        g.rect(0, B + H / 2, W, T)
    elif 0x2589 <= cp <= 0x258F:
        g.rect(0, B, W * (8 - (cp - 0x2588)) / 8, T)
    elif cp == 0x2590:
        g.rect(W / 2, B, W, T)
    elif cp in (0x2591, 0x2592, 0x2593):
        d, k = DOT[weight]
        dia = {0x2591: 40, 0x2592: 70, 0x2593: 100}[cp]
        for j in range(12):
            for i in range(6):
                g.ellipse(P / 2 + i * P, B + P / 2 + j * P, dia / 2, dia / 2, k)
    elif cp == 0x2594:
        g.rect(0, T - H / 8, W, T)
    elif cp == 0x2595:
        g.rect(W * 7 / 8, B, W, T)
    else:
        quads = {0x2596: "3", 0x2597: "4", 0x2598: "1", 0x2599: "134", 0x259A: "14",
                 0x259B: "123", 0x259C: "124", 0x259D: "2", 0x259E: "23", 0x259F: "234"}[cp]
        boxes = {"1": (0, B + H / 2, W / 2, T), "2": (W / 2, B + H / 2, W, T),
                 "3": (0, B, W / 2, B + H / 2), "4": (W / 2, B, W, B + H / 2)}
        for q in quads:
            g.rect(*boxes[q])
    return g


PL_MAPS = {
    0xE0A0: ["#...#", "#...#", "#..#.", "#.#..", "##...", "#....", "#...."],
    0xE0A1: ["#....", "#....", "###..", ".....", "#..#.", "##.#.", "#.##."],
    0xE0A2: [".###.", "#...#", "#...#", "#####", "##.##", "#####", "#####"],
}


def powerline_glyph(cp, weight, italic):
    if cp in PL_MAPS:
        return dot_glyph(glyph_name(cp), [cp], lit(PL_MAPS[cp], 6), weight, False)
    g = Glyph(glyph_name(cp), [cp], ADV)
    T, B, W = BOX_TOP, BOX_BOTTOM, ADV
    m = (T + B) / 2
    d, k = DOT[weight]
    if cp == 0xE0B0:
        g.poly([(0, B), (W, m), (0, T)])
    elif cp == 0xE0B2:
        g.poly([(W, B), (W, T), (0, m)])
    else:  # chevrons drawn as dotted strokes
        n = 9
        for i in range(n + 1):
            t = i / n
            y = B + (T - B) * t
            x = W * (1 - abs(2 * t - 1)) * 0.9 + 30
            if cp == 0xE0B3:
                x = W - x
            g.ellipse(x, y, max(d, 44) / 2, max(d, 44) / 2, k)
    return g


def notdef(weight):
    d, k = DOT[weight]
    g = Glyph(".notdef", [], ADV)
    for (c, h) in [(c, h) for c in range(5) for h in range(7) if c in (0, 4) or h in (0, 6)]:
        x, y = centre(c, h, False)
        g.ellipse(x, y, d / 2, d / 2, k)
    return g


def build(weight, italic):
    order, M = load_maps()
    glyphs = [notdef(weight)]
    for name in order:
        e = M[name]
        cps = [e["cp"]] if e["cp"] is not None else []
        cols = len(e["rows"][0])
        dots = set() if e.get("blank") else lit(e["rows"], e["top"])
        glyphs.append(dot_glyph(name, cps, dots, weight, italic, cols))
    by_cp = {e["cp"]: e for e in M.values() if e["cp"] is not None}
    for cp, (bcp, acc) in sorted(COMPOSITES.items()):
        if bcp == 0x69:
            bcp = 0x131
        be = by_cp[bcp]
        upper = chr(bcp).isupper()
        dots = lit(be["rows"], be["top"]) | accent_dots(len(be["rows"][0]), acc, upper)
        glyphs.append(dot_glyph(glyph_name(cp), [cp], dots, weight, italic, len(be["rows"][0])))
    for cp in BOX_RANGE:
        glyphs.append(box_glyph(cp, weight, italic))
    for cp in BLOCK_RANGE:
        glyphs.append(block_glyph(cp, weight, italic))
    for cp in POWERLINE:
        glyphs.append(powerline_glyph(cp, weight, italic))
    return glyphs


def kerning():
    return None  # monospaced display face: fixed pitch, no kerning by design


def features():
    return """languagesystem DFLT dflt;
languagesystem latn dflt;

feature zero {
    sub zero by zero.slash;
} zero;

feature ss01 {
    featureNames { name "Plain zero (no centre dot)"; };
    sub zero by zero.plain;
} ss01;
"""
