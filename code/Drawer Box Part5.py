def generate_Part5_svg(width_mm, height_mm, filename="Drawer Box part5.svg"):

    if width_mm <= 60 or height_mm <= 60:
        raise ValueError("Width and height must be more than 60mm.")

    if width_mm > 150 or height_mm > 150:
        raise ValueError("Width and height must be 150mm or smaller.")

    notch_height = 4
    notch_width = 10
    real_height = 0.7 * height_mm
    width_in = width_mm / 25.4
    height_in = real_height / 25.4
    step = notch_width + 10
    path_d = ""
    #side lines
    y = 10
    step = notch_width + 10

    path_d += f"M {notch_height} 0 H {width_mm - notch_height}\n"
    path_d += f"M {notch_height} {real_height} H {width_mm - notch_height}\n"
    while y < real_height - 10:
        path_d += f"M {width_mm} {y} V {y + notch_width}\n"
        path_d += f"M 0 {y} V {y + notch_width}\n"
        y += step


    y = 0
    while y < real_height - step:
        if y < 20:
            path_d += f"""
            M {width_mm - notch_height} 0
            V {y + notch_width}
            H {width_mm}
            """
            path_d += f"""
            M {notch_height} 0
            V {y + notch_width}
            H 0
            """
        elif y < real_height:
            path_d += f"""
            M {width_mm} {y}
            H {width_mm - notch_height}
            V {y + notch_width}
            H {width_mm}
            """
            path_d += f"""
            M 0 {y}
            H {notch_height}
            V {y + notch_width}
            H 0
            """
        y += step
    path_d += f"M {width_mm} {y} H {width_mm - notch_height} V {real_height}\n"
    path_d += f"M 0 {y} H {notch_height} V {real_height}\n"

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

</svg>
'''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"SVG file '{filename}' generated successfully.")


if __name__ == "__main__":
    try:
        w = float(input("Enter rectangle width (millimeters): "))
        h = float(input("Enter rectangle height (millimeters): "))

        generate_Part5_svg(w, h)

    except ValueError as e:
        print("Error:", e)