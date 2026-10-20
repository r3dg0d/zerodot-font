"""Zerodot-specific tests: glyphs are made of separate dots on a fixed pitch."""
import os
import sys

import ufoLib2
from test_fonts import FAM, ROOT, path, shape

sys.path.insert(0, os.path.join(ROOT, "tools"))
import engine  # noqa: E402


def test_every_letter_is_a_dot_matrix():
    order, M = engine.load_maps()
    u = ufoLib2.Font.open(os.path.join(ROOT, "sources", "ufo", "Zerodot-Regular.ufo"))
    for name in order:
        rows = M[name]["rows"]
        lit = sum(r.count("#") for r in rows) if not M[name].get("blank") else 0
        g = u[name]
        assert len(g.contours) == lit, name
        assert all(len(c.points) == 12 for c in g.contours), name


def test_dotted_zero_is_default():
    assert shape(path(400, False, "ttf"), "0")[0] == ["zero"]
    order, M = engine.load_maps()
    assert M["zero"]["rows"][3] == "#.#.#"
