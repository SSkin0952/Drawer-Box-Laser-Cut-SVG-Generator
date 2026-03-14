def generate_Part7_svg(width_mm, height_mm, filename="Drawer Box part7.svg"):
    if width_mm <= 60 or height_mm <= 60:
        raise ValueError("Width and height must be more than 60mm.")

    if width_mm > 150 or height_mm > 150:
        raise ValueError("Width and height must be 150mm or smaller.")

    notch_height = 4
    notch_width = 10
    screw_d = 2.3
    screw_l = 10
    screw_in = screw_l - notch_height
    nut_l = 1.8
    nut_w = 5
    nut_in = 3
    t_notch = ((0.25 * height_mm) ** 2 + (width_mm - 10) ** 2) ** 0.5 * notch_height / (width_mm - 10)
    slot_path_d = ""
    width_in = width_mm / 25.4
    height_in = height_mm / 25.4
    path_d = ""
    circles_svg = ""
    text_x = height_mm / 3 * 2
    text_y = width_mm * 0.8
    # ===== SVG Path =====

    # left up line
    path_d += f"M {height_mm * 0.25} 0 L 0 {width_mm - 10} L 0 {width_mm - notch_height} H {height_mm % 10}"
    # left up gap
    slot_path_d += f"""
    M 0.5 {width_mm - notch_height}
    L {(height_mm * 0.25) * (width_mm - notch_height) / (width_mm - 10) + 0.5} 0
    L {(height_mm * 0.25) * (width_mm - notch_height) / (width_mm - 10) + 0.5 + t_notch} 0
    L {0.5 + t_notch} {width_mm - notch_height}
    Z
    """
    # down line
    x = height_mm
    step = notch_width + 10
    while x > 10:
        path_d += f"M {x} {width_mm} H {max(x - 10, 10)}\n"
        x -= step
    # make up down gap
    path_d += f"M {x + 10} {width_mm} V {width_mm - notch_height} H 0\n"
    # up line
    x = height_mm
    n = 0
    while x > height_mm * 0.25:
        if x > height_mm - notch_height:
            path_d += f"M {x - notch_height} 0 H {max(x - 10, height_mm * 0.25)}\n"
            n += 1
        elif x < height_mm:
            path_d += f"M {x} 0 H {max(x - 10, height_mm * 0.25)}\n"
            n += 1
        x -= step
    # make up up left gap
    path_d += f"M {height_mm * 0.25} 0 H {height_mm - n * 20 + 30}\n"
    # make up up right gap
    path_d += f"M {height_mm - notch_height} 0 V {notch_width} H {height_mm}\n"
    # right line
    y = 0
    step = notch_width + 10
    while y + 10 < width_mm:
        path_d += f"M {height_mm} {y + 10} V {min(y + 20, width_mm)}\n"
        y += step
    # make up right down gap
    path_d += f"M {height_mm} {y - 10} V {width_mm}\n"

    # up rect
    x = height_mm - notch_width
    while x > height_mm * 0.25 + 20:
        path_d += f"M {x} 0 V {notch_height} H {x - notch_width} V 0\n"
        x -= step
    # up hole
    x = height_mm - notch_width - 10
    while x > height_mm * 0.25 + 5:
        circles_svg += f'''
             <circle cx="{x - notch_width / 2}"
                cy="{notch_height / 2}"
                r="{screw_d / 2}"/>
                '''
        x -= step

    # right rect + hole
    y = 0
    while y < width_mm:
        if y + notch_width <= 20:
            path_d += f"""
            M {height_mm - notch_height} {y}
            V {y + notch_width}
            H {height_mm}
            """
        elif y + notch_width <= width_mm - 20:
            path_d += f"""
                M {height_mm} {y}
                H {height_mm - notch_height}
                V {y + (notch_width - screw_d) / 2}
                H {height_mm - (notch_height + nut_in)}
                V {y + (notch_width - nut_w) / 2}
                H {height_mm - (notch_height + nut_in + nut_l)}
                V {y + (notch_width - screw_d) / 2}
                H {height_mm - notch_width}
                V {y + (notch_width + screw_d) / 2}
                H {height_mm - (notch_height + nut_in + nut_l)}
                V {y + (notch_width + nut_w) / 2}
                H {height_mm - (notch_height + nut_in)}
                V {y + (notch_width + screw_d) / 2}
                H {height_mm - notch_height}
                V {y + notch_width}
                H {height_mm}
                """
        elif y + notch_width <= width_mm:
            path_d += f"""
                M {height_mm} {y}
                H {height_mm - notch_height}
                V {y + notch_width}
                H {height_mm}
                """

        circles_svg += f'''
             <circle cx="{height_mm - notch_height / 2}"
                cy="{y + notch_width / 2 + 10}"
                r="{screw_d / 2}" />
             '''
        y += step

    # down rect + hole
    x = height_mm
    while x > 10:
        current_x = x + 10

        if current_x - notch_width >= height_mm - 10:
            path_d += f"""
            M {current_x} {width_mm}
            H {current_x - notch_width}
            V {width_mm - notch_height}
            """
        elif current_x - notch_width >= 10:
            path_d += f"""
                M {current_x} {width_mm}
                V {width_mm - notch_height}
                H {current_x - (notch_width - screw_d) / 2}
                V {width_mm - (notch_height + nut_in)}
                H {current_x - (notch_width - nut_w) / 2}
                V {width_mm - (notch_height + nut_in + nut_l)}
                H {current_x - (notch_width - screw_d) / 2}
                V {width_mm - notch_width}
                H {current_x - (notch_width + screw_d) / 2}
                V {width_mm - (notch_height + nut_in + nut_l)}
                H {current_x - (notch_width + nut_w) / 2}
                V {width_mm - (notch_height + nut_in)}
                H {current_x - (notch_width + screw_d) / 2}
                V {width_mm - notch_height}
                H {current_x - notch_width}
                V {width_mm}
                """
        if x >= 20 and x < height_mm - 10:
            circles_svg += f'''
                 <circle cx="{x - notch_width / 2}"
                    cy="{width_mm - notch_height / 2}"
                    r="{screw_d / 2}" />
                 '''
        x -= step

    # middle connection
    x = height_mm
    x1 = width_mm * 1 / 3 - notch_height
    x2 = width_mm * 2 / 3 - notch_height
    while x - notch_height > 0.25 * height_mm + 25:
        path_d += f"M {x - 10 - notch_height} {x1} V {x1 + notch_height} H {x - 20 - notch_height} V {x1} Z\n"
        path_d += f"M {x - 10 - notch_height} {x2} V {x2 + notch_height} H {x - 20 - notch_height} V {x2} Z\n"
        x -= step

    svg_content = f'''<?xml version="1.0" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{height_in}in"
     height="{width_in}in"
     viewBox="0 0 {height_mm} {width_mm}">
  <g transform="scale(-1, 1) translate(-{height_mm}, 0)">
  <path d="{path_d}"
        fill="none"
        stroke="black"
        stroke-width="0.05"/>
  <path d="{slot_path_d}"
      fill="none"
      stroke="red"
      stroke-width="0.05"/>

  <g fill="none" stroke="green" stroke-width="0.05">
    {circles_svg}
  </g>
  
  </g>
  
  <text x="{text_x}"
        y="{text_y}"
        text-anchor="middle"
        font-family="Arial"
        font-size="{height_mm * 0.08}"
        fill="red"
        transform="scale(-1, 1) translate({-text_x * 2}, 0)">
    ws2782
  </text>
</svg>
'''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"SVG file '{filename}' generated successfully.")


if __name__ == "__main__":
    try:
        w = float(input("Enter rectangle width (millimeters): "))
        h = float(input("Enter rectangle height (millimeters): "))

        generate_Part7_svg(w, h)

    except ValueError as e:
        print("Error:", e)