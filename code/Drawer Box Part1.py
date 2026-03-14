import math
def generate_snowflake_path(center_x, center_y, size=10):

    outer_radius = size
    inner_radius = size * 0.6
    arm_count = 6
    small_arms_per_arm = 2

    path_d = []

    for i in range(arm_count):
        angle = (i * 2 * math.pi) / arm_count

        start_x = center_x
        start_y = center_y

        end_x = center_x + outer_radius * math.cos(angle)
        end_y = center_y + outer_radius * math.sin(angle)

        path_d.append(f"M {start_x:.2f} {start_y:.2f}")
        path_d.append(f"L {end_x:.2f} {end_y:.2f}")

        for j in range(small_arms_per_arm):
            t = 0.3 + 0.4 * j
            arm_x = start_x + t * (end_x - start_x)
            arm_y = start_y + t * (end_y - start_y)

            small_arm_angle1 = angle + math.pi / 2
            small_arm_angle2 = angle - math.pi / 2

            small_arm_length = inner_radius * 0.5

            small_end_x1 = arm_x + small_arm_length * math.cos(small_arm_angle1)
            small_end_y1 = arm_y + small_arm_length * math.sin(small_arm_angle1)
            path_d.append(f"M {arm_x:.2f} {arm_y:.2f}")
            path_d.append(f"L {small_end_x1:.2f} {small_end_y1:.2f}")

            small_end_x2 = arm_x + small_arm_length * math.cos(small_arm_angle2)
            small_end_y2 = arm_y + small_arm_length * math.sin(small_arm_angle2)
            path_d.append(f"M {arm_x:.2f} {arm_y:.2f}")
            path_d.append(f"L {small_end_x2:.2f} {small_end_y2:.2f}")

    hexagon_points = []
    for i in range(6):
        angle = (i * 2 * math.pi) / 6
        hx = center_x + (size * 0.2) * math.cos(angle)
        hy = center_y + (size * 0.2) * math.sin(angle)
        hexagon_points.append(f"{hx:.2f},{hy:.2f}")

    path_d.append(f"M {hexagon_points[0]}")
    for i in range(1, 6):
        path_d.append(f"L {hexagon_points[i]}")
    path_d.append("Z")

    return " ".join(path_d)


def generate_Part1_svg(width_mm, height_mm, filename="Drawer Box part1.svg"):
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

    if width_mm < 95:
        notch_positions = [10, width_mm - 20]
    else:
        notch_positions = [10, 30, width_mm - 40, width_mm - 20]

    width_in = width_mm / 25.4
    height_in = height_mm / 25.4
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

    while y + 10 < height_mm:
        path_d += f"M 0 {y + 10} V {min(y + 20, height_mm)}\n"
        y += step

    y = 0
    while y + 10 < height_mm:
        path_d += f"M {width_mm} {y + 10} V {min(y + 20, height_mm)}\n"
        y += step

    path_d += f"M 0 {height_mm} H {width_mm}\n"

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

    # ===== side rect =====
    y = 0
    step = notch_width + 10

    path_d += f"""
        M 0 {width_mm}
        V {width_mm - width_mm % 10}
        """
    path_d += f"""
        M {width_mm} {width_mm}
        V {width_mm - width_mm % 10}
        """

    while y < height_mm:
        # left
        if y + notch_width <= 20:
            path_d += f"""
            M {notch_height} {y}
            V {y + notch_width}
            H 0
            """
        elif y + notch_width <= height_mm:
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
        circles_svg += f'''
            <circle cx="{notch_height / 2}"
                    cy="{y + notch_width / 2 + 10}"
                    r="{screw_d / 2}" />
            '''

        # right
        if y + notch_width <= 20:
            path_d += f"""
            M {width_mm - notch_height} {y}
            V {y + notch_width}
            H {width_mm}
            """
        elif y + notch_width <= height_mm:
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
        circles_svg += f'''
             <circle cx="{width_mm - notch_height / 2}"
                cy="{y + notch_width / 2 + 10}"
                r="{screw_d / 2}" />
             '''

        y += step

    path_d += f"""
    M 0 {height_mm - notch_height} 
    V {height_mm}
    """

    path_d += f"""
    M {width_mm} {height_mm - notch_height}
    V {height_mm}
    """

    # ===== snow figure generate =====
    # size
    snowflake_size = min(width_mm, height_mm) * 0.15
    snowflake_size = max(10, min(snowflake_size, 20))

    # center
    snowflake_center_x = width_mm / 2
    snowflake_center_y = height_mm / 2

    # path of snow
    snowflake_path = generate_snowflake_path(
        snowflake_center_x,
        snowflake_center_y,
        snowflake_size
    )

    svg_content = f'''<?xml version="1.0" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{width_in}in"
     height="{height_in}in"
     viewBox="0 0 {width_mm} {height_mm}">

  <path d="{path_d}"
        fill="none"
        stroke="black"
        stroke-width="0.05"
        fill-rule="evenodd"/>

  <g fill="none" stroke="green" stroke-width="0.05">
    {circles_svg}
  </g>

  <path d="{snowflake_path}"
        fill="none"
        stroke="yellow"
        stroke-width="0.1"
        stroke-linecap="round"/>

</svg>
'''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"SVG file '{filename}' generated successfully.")
    print(f"Snowflake added at center position: ({snowflake_center_x:.1f}, {snowflake_center_y:.1f})")
    print(f"Snowflake size: {snowflake_size:.1f}mm")


if __name__ == "__main__":
    try:
        w = float(input("Enter rectangle width (millimeters): "))
        h = float(input("Enter rectangle height (millimeters): "))

        generate_Part1_svg(w, h)

    except ValueError as e:
        print("Error:", e)