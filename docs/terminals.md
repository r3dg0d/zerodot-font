# Using Zerodot in terminals and editors

Install it first (see README). Font family name: **`Zerodot`**. Variable family: **`Zerodot`** (fontconfig exposes the named instances).
Zerodot is monospaced (`post.isFixedPitch` = 1, every advance identical), so terminals that filter for monospace fonts list it.

## kitty (`~/.config/kitty/kitty.conf`)
```conf
font_family      family="Zerodot"
bold_font        auto
italic_font      auto
bold_italic_font auto
font_size        13.0
# font_features Zerodot-Regular +zero
```
## Alacritty (`~/.config/alacritty/alacritty.toml`, 0.13+ TOML)
```toml
[font]
size = 13.0
normal = { family = "Zerodot", style = "Regular" }
bold = { family = "Zerodot", style = "Bold" }
italic = { family = "Zerodot", style = "Italic" }
bold_italic = { family = "Zerodot", style = "Bold Italic" }
```
## foot (`~/.config/foot/foot.ini`)
```ini
[main]
font=Zerodot:size=12
```
## WezTerm (`~/.wezterm.lua`)
```lua
local wezterm = require 'wezterm'
return {
  font = wezterm.font('Zerodot', { weight = 'Regular' }),
  harfbuzz_features = { "zero=0" },
  font_size = 13.0,
}
```
## Ghostty (`~/.config/ghostty/config`)
```ini
font-family = Zerodot
font-size = 13
font-feature = +zero
```
## GNOME Terminal / Ptyxis
```sh
gsettings set org.gnome.desktop.interface monospace-font-name 'Zerodot 12'
```
## VS Code (`settings.json`)
```json
{
  "editor.fontFamily": "'Zerodot', monospace",
  "editor.fontLigatures": false,
  "terminal.integrated.fontFamily": "'Zerodot'"
}
```
## Neovim GUIs (Neovide etc.)
```lua
vim.o.guifont = "Zerodot:h13"
```
## Emacs
```elisp
(set-face-attribute 'default nil :family "Zerodot" :height 130)
```
## Powerline / Starship
U+E0A0–E0A2 and U+E0B0–E0B3 are included natively. No patching is needed for classic Powerline separators. Full Nerd Font icon sets are **not** included.
