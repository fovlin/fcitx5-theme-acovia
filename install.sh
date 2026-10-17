#!/bin/bash
mkdir -p ~/.local/share/fcitx5/themes/
cp -r ./* ~/.local/share/fcitx5/themes/
fcitx5 -r &