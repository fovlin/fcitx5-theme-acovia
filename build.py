import os
import data

def build(color, panel):
    color_name, v_color = color
    panel_theme_name, v_panel_color, v_border_color, v_font_color= panel[0], panel[1][0], panel[1][1], panel[1][2]

    svg_file = open(f"acovia-{color_name}-{panel_theme_name}/highlight.svg", "w")
    panel_file = open(f"acovia-{color_name}-{panel_theme_name}/panel.svg", "w")
    conf_file = open(f"acovia-{color_name}-{panel_theme_name}/theme.conf", "w")

    svg_color = f'<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32"><rect width="32" height="32" x="0" y="0" fill="{v_color}" rx="12" ry="12"/></svg>'
    panel_color = f'<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32"><rect width="30" height="30" x="1" y="1" fill="{v_panel_color}" stroke="{v_border_color}" stroke-width="1" stroke-linecap="round" rx="12" ry="12"/></svg>'
    
    svg_file.write(svg_color)
    svg_file.close()
    panel_file.write(panel_color)
    panel_file.close()
    conf_file.write(data.gen_cfg(f"acovia-{color_name}-{panel_theme_name}", v_font_color))
    conf_file.close()

for panel in data.panel_color.items():
    for color in data.color_list.items():
        flag = False
        while flag == False:
            try:
                build(color, panel)
                flag = True
            except FileNotFoundError:
                os.mkdir(f"acovia-{color[0]}-{panel[0]}")
            except FileExistsError:
                flag = True