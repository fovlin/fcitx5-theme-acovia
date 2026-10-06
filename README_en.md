# acovia-fcitx5-theme

A minimal fcitx5 theme implemented with SVG, in a rounded, GNOME-like style.


## Examples

### acovia-blue-dark/light

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/07d5d0ad-8f1b-4066-972c-e8cfbb69593f" />

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/3cf2540d-50ad-49d1-a6a5-bba18c224081" />

### acovia-gold-dark/light

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/5d4d9652-ff62-4606-b998-625dd061b7c0" />

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/69477021-71df-4a6d-96e2-6135b414ccc5" />

### acovia-pink-dark/light

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/5abc4ac6-e7e4-40d9-8a17-9905147bd889" />

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/4ce2c626-e3a8-4054-a612-f629b4b003b5" />

And more...

## Installation

```bash
git clone https://github.com/fovlin/fcitx5-theme-acovia.git
cd fcitx5-theme-acovia
mkdir -p ~/.local/share/fcitx5/themes/
cp -r ./* ~/.local/share/fcitx5/themes/
```

Then select the Acovia theme in fcitx5-configtool under Addons → Classic User Interface.

## Notes

When using fcitx5 on a desktop environment configured for English, text may float upward due to differences in text baseline. It is recommended to use a Chinese locale, or to adjust the parameters manually in fcitx5-configtool under a non-Chinese locale.

## Customization

Edit the color values in data.py and run the build.py script to generate a theme in the color scheme you specify.
python

```python
# color_list is the list of colors; you can add custom colors.
# Colors are expressed as hex color codes.
# panel_color is the list of light/dark theme colors; each tuple's three
# elements represent, in order: (panel background color - border color - text color)

color_list = {
    "red":    "#6f0000",
    "gold":   "#7f5f00",
    "green":  "#4f8f00",
    "blue":   "#004f8f",
    "aqua":   "#006f6f",
    "purple": "#6f006f",
    "pink":   "#8f004f"
}

panel_color = {
    "dark": ("#1a1a1a", "#4a4a4a", "#ffffff"),
    "light": ("#efefef", "#afafaf", "#000000")
}
```

You may optionally fine-tune individual parameters in fcitx5-configtool; this essentially edits the values in theme.conf through the GUI tool.

Reference documentation for theme development: https://fovlin.com/docs/linux-notes/fcitx5-theme-dev.html