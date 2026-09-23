# acovia-fcitx5-theme

一个通过 svg 实现的最小 fcitx5 主题，风格为圆角，类 gnome 主题。

dark:

<img width="660" height="268" alt="图片" src="https://github.com/user-attachments/assets/1b6e5066-58f2-4b19-b473-377279422f50" />

light:

<img width="660" height="268" alt="图片" src="https://github.com/user-attachments/assets/3395410f-dc45-4d4f-9d65-1da07a1958de" />

## 安装

```bash
git clone https://github.com/fovlin/fcitx5-theme-acovia.git
cd fcitx5-theme-acovia
mkair -p ~/.local/share/fcitx5/themes/
cp -r ./* ~/.local/share/fcitx5/themes/
```

随后在 `fcitx5-configtool` 工具 - 经典用户界面设置内选择 Acovia 主题。

## 定制

主题外观以来 svg 实现，编辑 svg 文件，修改其中 `fill`，`stroke` 的值来更改其颜色。

可选在 `fcitx5-configtool` 工具中调整具体参数，这本质上是通过 gui 工具编辑 `theme.conf` 的值。

参考开发文档：[https://fovlin.com/docs/linux-notes/fcitx5-theme-dev.html](https://fovlin.com/docs/linux-notes/fcitx5-theme-dev.html)