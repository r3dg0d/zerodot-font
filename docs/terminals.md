# Using DotZero in terminals and editors

Install it first (see README). Font family name: **`DotZero`**. Variable family: **`DotZero`** (fontconfig exposes the named instances).
DotZero is monospaced (`post.isFixedPitch` = 1, every advance identical), so terminals that filter for monospace fonts list it.

## kitty (`~/.config/kitty/kitty.conf`)
```conf
font_family      family="DotZero"
bold_font        auto
italic_font      auto
bold_italic_font auto
font_size        13.0
# font_features DotZero-Regular +zero
```
## Alacritty (`~/.config/alacritty/alacritty.toml`, 0.13+ TOML)
```toml
[font]
size = 13.0
normal = { family = "DotZero", style = "Regular" }
bold = { family = "DotZero", style = "Bold" }
italic = { family = "DotZero", style = "Italic" }
bold_italic = { family = "DotZero", style = "Bold Italic" }
```
## foot (`~/.config/foot/foot.ini`)
```ini
[main]
font=DotZero:size=12
```
## WezTerm (`~/.wezterm.lua`)
```lua
local wezterm = require 'wezterm'
return {
  font = wezterm.font('DotZero', { weight = 'Regular' }),
  harfbuzz_features = { "zero=0" },
  font_size = 13.0,
}
```
## Ghostty (`~/.config/ghostty/config`)
```ini
font-family = DotZero
font-size = 13
font-feature = +zero
```
## GNOME Terminal / Ptyxis
```sh
gsettings set org.gnome.desktop.interface monospace-font-name 'DotZero 12'
```
## VS Code (`settings.json`)
```json
{
  "editor.fontFamily": "'DotZero', monospace",
  "editor.fontLigatures": false,
  "terminal.integrated.fontFamily": "'DotZero'"
}
```
## Neovim GUIs (Neovide etc.)
```lua
vim.o.guifont = "DotZero:h13"
```
## Emacs
```elisp
(set-face-attribute 'default nil :family "DotZero" :height 130)
```
## Powerline / Starship
U+E0A0–E0A2 and U+E0B0–E0B3 are included natively. No patching is needed for classic Powerline separators. Full Nerd Font icon sets are **not** included.
