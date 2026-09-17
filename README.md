# acovia-fcitx5-theme

A minimal Fcitx5 theme implemented via SVG, featuring a rounded, GNOME-like style.

dark:

<img width="660" height="268" alt="图片" src="https://github.com/user-attachments/assets/1b6e5066-58f2-4b19-b473-377279422f50" />

light:

<img width="660" height="268" alt="图片" src="https://github.com/user-attachments/assets/3395410f-dc45-4d4f-9d65-1da07a1958de" />

## Installation

```bash
git clone https://github.com/fovlin/fcitx5-theme-acovia.git
cd acovia-fcitx5-theme
mkdir -p ~/.local/share/fcitx5/themes/
cp -r ./* ~/.local/share/fcitx5/themes/
```

Then open `fcitx5-configtool`, go to the Classic UI settings, and select the Acovia theme.

## Customization

The theme's appearance is implemented via SVG files. Edit the SVG files and modify the fill and stroke values to change colors.

You can also adjust specific parameters in `fcitx5-configtool`, which essentially edits the `theme.conf` file through the GUI.
