# acovia-fcitx5-theme

一个通过 svg 实现的最小 fcitx5 主题，风格为圆角，类 gnome 主题。

## 示例

### acovia-blue-dark/light

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/07d5d0ad-8f1b-4066-972c-e8cfbb69593f" />

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/3cf2540d-50ad-49d1-a6a5-bba18c224081" />

### acovia-gold-dark/light

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/5d4d9652-ff62-4606-b998-625dd061b7c0" />

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/69477021-71df-4a6d-96e2-6135b414ccc5" />

### acovia-pink-dark/light

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/5abc4ac6-e7e4-40d9-8a17-9905147bd889" />

<img width="743" height="311" alt="图片" src="https://github.com/user-attachments/assets/4ce2c626-e3a8-4054-a612-f629b4b003b5" />

以及更多...

## 安装

```bash
git clone https://github.com/fovlin/fcitx5-theme-acovia.git
cd fcitx5-theme-acovia
mkdir -p ~/.local/share/fcitx5/themes/
cp -r ./* ~/.local/share/fcitx5/themes/
```

随后在 `fcitx5-configtool` 工具 - 经典用户界面设置内选择 Acovia 主题。

## 注意

- 在英文环境下的桌面环境使用 fcitx5，会因文字基准线差异导致文字上浮，请使用中文环境。

## 定制

编辑 `data.py` 内的颜色值，并运行 `build.py` 脚本，可构建出指定系列的主题。

可选在 `fcitx5-configtool` 工具中调整具体参数，这本质上是通过 gui 工具编辑 `theme.conf` 的值。

可供参考的开发文档：[https://fovlin.com/docs/linux-notes/fcitx5-theme-dev.html](https://fovlin.com/docs/linux-notes/fcitx5-theme-dev.html)
