def generate_Part3_svg(width_mm, height_mm, filename="Drawer Box part3.svg"):
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
    text_x = width_mm / 2
    text_y = height_mm / 3
    # real height is 2/3
    real_height = int(height_mm * 2 / 3)

    if width_mm < 95:
        notch_positions = [10, width_mm - 20]
    else:
        notch_positions = [10, 30, width_mm - 40, width_mm - 20]

    width_in = width_mm / 25.4
    height_in = real_height / 25.4
    path_d = ""
    circles_svg = ""

    # ===== SVG Path =====
    current_x = notch_height
    for x in notch_positions:
        if x > current_x:
            path_d += f"M {current_x} 0 H {x}\n"
        current_x = x + notch_width

    if current_x < width_mm:
        path_d += f"M {current_x} 0 H {width_mm - notch_height}\n"

    y = 0
    step = notch_width + 10

    # side lines
    while y + 10 < real_height - real_height % 20:
        path_d += f"M 0 {y + 10} V {min(y + 20, real_height)}\n"
        path_d += f"M {width_mm} {y + 10} V {min(y + 20, real_height)}\n"
        y += step

    # down line
    path_d += f"M {notch_height} {real_height} H {width_mm - notch_height}\n"

    # up rect
    for x in notch_positions:
        path_d += f"""
        M {x} 0
        V {notch_height}
        H {x + (notch_width - screw_d) / 2}
        V {notch_height + nut_in}
        H {x + (notch_width - nut_w) / 2}
        V {notch_height + nut_in + nut_l}
        H {x + (notch_width - screw_d) / 2}
        V {notch_width}
        H {x + (notch_width + screw_d) / 2}
        V {notch_height + nut_in + nut_l}
        H {x + (notch_width + nut_w) / 2}
        V {notch_height + nut_in}
        H {x + (notch_width + screw_d) / 2}
        V {notch_height}
        H {x + notch_width}
        V {0}
        """
        if x < width_mm / 2:
            circles_svg += f'''
                 <circle cx="{x + notch_width / 2 + 10}"
                    cy="{notch_height / 2}"
                    r="{screw_d / 2}" />
                 '''
        elif x > width_mm / 2:
            circles_svg += f'''
                 <circle cx="{x + notch_width / 2 - 10}"
                    cy="{notch_height / 2}"
                    r="{screw_d / 2}"/>
                    '''

    # side rect
    y = 0
    step = notch_width + 10

    while y < real_height:
        if y + notch_width <= 20:
            path_d += f"""
            M {notch_height} {y}
            V {y + notch_width}
            H 0
            """
        elif y + notch_width <= real_height - 10:
            path_d += f"""
            M 0 {y}
            H {notch_height}
            V {y + (notch_width - screw_d) / 2}
            H {notch_height + nut_in}
            V {y + (notch_width - nut_w) / 2}
            H {notch_height + nut_in + nut_l}
            V {y + (notch_width - screw_d) / 2}
            H {notch_width}
            V {y + (notch_width + screw_d) / 2}
            H {notch_height + nut_in + nut_l}
            V {y + (notch_width + nut_w) / 2}
            H {notch_height + nut_in}
            V {y + (notch_width + screw_d) / 2}
            H {notch_height}
            V {y + notch_width}
            H 0
            """
        else :
            path_d += f"""
            M 0 {y}
            H {notch_height}
            V {real_height}
            """
        if y + notch_width <= 20:
            path_d += f"""
            M {width_mm - notch_height} {y}
            V {y + notch_width}
            H {width_mm}
            """
        elif y + notch_width <= real_height - 10:
            path_d += f"""
                M {width_mm} {y}
                H {width_mm - notch_height}
                V {y + (notch_width - screw_d) / 2}
                H {width_mm - (notch_height + nut_in)}
                V {y + (notch_width - nut_w) / 2}
                H {width_mm - (notch_height + nut_in + nut_l)}
                V {y + (notch_width - screw_d) / 2}
                H {width_mm - notch_width}
                V {y + (notch_width + screw_d) / 2}
                H {width_mm - (notch_height + nut_in + nut_l)}
                V {y + (notch_width + nut_w) / 2}
                H {width_mm - (notch_height + nut_in)}
                V {y + (notch_width + screw_d) / 2}
                H {width_mm - notch_height}
                V {y + notch_width}
                H {width_mm}
                """
        else :
            path_d += f"""
                M {width_mm} {y}
                H {width_mm - notch_height}
                V {real_height}
                """
        y += step


    svg_content = f'''<?xml version="1.0" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{width_in}in"
     height="{height_in}in"
     viewBox="0 0 {width_mm} {real_height}">

  <path d="{path_d}"
        fill="none"
        stroke="black"
        stroke-width="0.05"
        fill-rule="evenodd"/>

  <g fill="none" stroke="green" stroke-width="0.05">
    {circles_svg}
  </g>
  <text x="{text_x}"
        y="{text_y}"
        text-anchor="middle"
        font-family="Arial"
        font-size="{width_mm / 100 * 14}"
        fill="red">
    Drawer Box
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

        generate_Part3_svg(w, h)

    except ValueError as e:
        print("Error:", e)