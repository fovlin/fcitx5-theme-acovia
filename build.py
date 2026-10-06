import os
import data

def build(color, theme):
    color_name, v_color = color
    back_theme_name, v_back_color, v_border_color, v_font_color= theme[0], theme[1][0], theme[1][1], theme[1][2]

    svg_file = open(f"acovia-{color_name}-{back_theme_name}/highlight.svg", "w")
    panel_file = open(f"acovia-{color_name}-{back_theme_name}/panel.svg", "w")
    conf_file = open(f"acovia-{color_name}-{back_theme_name}/theme.conf", "w")

    svg_color = f'<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32"><rect width="32" height="32" x="0" y="0" fill="{v_color}" rx="12" ry="12"/></svg>'
    panel_color = f'<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32"><rect width="31" height="31" x="0.5" y="0.5" fill="{v_back_color}" stroke="{v_border_color}" stroke-width="1" stroke-linecap="round" rx="12" ry="12"/></svg>'
    
    svg_file.write(svg_color)
    svg_file.close()
    panel_file.write(panel_color)
    panel_file.close()
    conf_file.write(data.gen_cfg(f"acovia-{color_name}-{back_theme_name}", v_font_color))
    conf_file.close()

for theme in data.back_color.items():
    for color in data.color_list.items():
        flag = False
        while flag == False:
            try:
                build(color, theme)
                flag = True
            except FileNotFoundError:
                os.mkdir(f"acovia-{color[0]}-{theme[0]}")
            except FileExistsError:
                flag = True