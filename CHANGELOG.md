# Changelog — Zerodot

All notable changes are documented here. The format follows Keep a Changelog. Font versions use `major.minor` (`head.fontRevision` = 1.000).

## [1.000] — unreleased (prepared 2026-10-19)
### Changed
- Family renamed before first publication: DotZero → Zerodot (DOT//ZERO display branding dropped), to avoid name conflicts with an existing product/font.

### Added
- First release: 9 weights (Thin 100 → Black 900) × upright + italic = 18 static styles.
- TTF (TrueType outlines), OTF (CFF outlines, subroutinised), WOFF2 for every style.
- Variable fonts: `Zerodot[wght].ttf/.woff2` and `Zerodot-Italic[wght].ttf/.woff2` (wght 100–900, STAT with ital linking).
- Coverage: printable ASCII, Latin-1 Supplement (except ¼ ½ ¾), dotless i, Ÿ, selected punctuation, currency, arrows,
  the full Box Drawing (U+2500–257F) and Block Elements (U+2580–259F) blocks, and Powerline U+E0A0–E0A2, U+E0B0–E0B3.
- OpenType: `zero` (slashed zero), `ss01` (plain zero).
- Editable sources: `sources/dotmatrix.txt` plus generated UFO masters and designspaces in `sources/`.
- Web subsets + CSS, specimens, a showcase site, a Nix flake, PKGBUILD, and CI workflows.
