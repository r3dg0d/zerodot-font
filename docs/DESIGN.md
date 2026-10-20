# Zerodot design notes

Zerodot is a **fixed-pitch dot-matrix**: a 5×7 matrix (x-height 5, 2-row descenders, accents above) on a 110-unit pitch, in a 6-dot (660-unit) monospaced cell.

* Each lit cell is **one closed dot**. Dots are never unioned, so no weight can close a counter: a one-dot gap is always ≥ 4 units of paper, even at Black.
* **Weight changes the dot**: 28-unit pin-pricks at Thin, 72 at Regular, 106 at Black. From Medium up the dot also becomes slightly squarer (superellipse handle 0.5523 → 0.76), like a high-brightness LED segment. Ink grows without the dots touching.
* **Italics** slant the matrix 10° but keep every dot round, as on a physically tilted display.
* The **dotted zero** is the brand mark and the default. `zero` gives a slashed zero and `ss01` a plain one.
* Terminal glyphs keep the pitch: box-drawing rules are dotted on the same 110-unit grid (edge dots are shared, so lines continue across cells). Blocks are solid so TUIs tile, and shades are dot fields.

## Variable font
Built from all 9 masters per slope. Dot diameter and squareness interpolate continuously, so `wght` is a smooth LED-brightness control.

## Engine
5×7 matrix → one closed 4-curve dot contour per lit cell (never merged)
