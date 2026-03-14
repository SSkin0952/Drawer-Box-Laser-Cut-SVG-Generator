def generate_Part2_svg(width_mm, filename="Drawer Box part2.svg"):

    if width_mm <= 60:
        raise ValueError("Width must be more than 60mm.")

    if width_mm > 150:
        raise ValueError("Width must be 150mm or smaller.")

    notch_height = 4
    notch_width = 10
    screw_d = 2.3
    screw_l = 10
    screw_in = screw_l - notch_height
    nut_l = 1.8
    nut_w = 5
    nut_in = 3
    embed_w = 64
    embed_h = 64
    center_x = width_mm / 2
    center_y = width_mm / 2
    scale = width_mm / 100
    if width_mm < 95:
        notch_positions = [10, width_mm - 20]
    else:
        notch_positions = [10, 30, width_mm - 40, width_mm - 20]
    height_mm = width_mm
    width_in = width_mm / 25.4
    height_in = width_mm / 25.4
    path_d = ""
    circles_svg = ""
    # ===== SVG Path =====
    # up and down lines
    current_x = 0
    for x in notch_positions:
        path_d += f"M {x} 0 H {x + notch_width}\n"
        path_d += f"M {x} {width_mm} H {x + notch_width}\n"
        current_x = x + notch_width

    # left lines
    y = 0
    step = notch_width + 10
    while y < height_mm:
        if y < notch_height:
            path_d += f"M 0 {notch_height} V {notch_width}\n"
            y += step
        elif y < height_mm:
            path_d += f"M 0 {y} V {min(y + 10, height_mm)}\n"
            y += step
    # right lines
    y = 0
    while y < height_mm:
        if y < notch_height:
            path_d += f"M {width_mm} {notch_height} V {notch_width}\n"
            y += step
        elif y < height_mm:
            path_d += f"M {width_mm} {y} V {min(y + 10, height_mm)}\n"
            y += step

    # up and down gap
    if width_mm < 95:
        start_x = 30
        end_x = width_mm - 30
    else:
        start_x = 40
        end_x = width_mm - 40

    if width_mm < 95:
        path_d += f"""
        M {start_x} {notch_height}
        H {end_x}
        """
        path_d += f"""
        M {start_x} {width_mm - notch_height}
        H {end_x}
        """
    else:
        path_d += f"""
        M {start_x} 0
        V {notch_height}
        H {end_x}
        V 0
        """
        path_d += f"""
        M {start_x} {width_mm}
        V {width_mm - notch_height}
        H {end_x}
        V {width_mm}
        """
    path_d += f"""
        M 0 {notch_height} 
        H {notch_width}
        V 0
        """
    path_d += f"""
        M {width_mm - 10} 0
        V {notch_height}
        H {width_mm}
        """

    # up rect
    x_positions = [20, width_mm - 30]
    for x in x_positions:
        if width_mm < 95:
            path_d += f"""
            M {x} {notch_height}
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
            """
            if x < width_mm / 2:
                circles_svg += f'''
                 <circle cx="{x + notch_width / 2 - 10}"
                    cy="{notch_height / 2}"
                    r="{screw_d / 2}" />
                 '''
            elif x > width_mm / 2:
                circles_svg += f'''
                 <circle cx="{x + notch_width / 2 + 10}"
                    cy="{notch_height / 2}"
                    r="{screw_d / 2}"/>
                    '''

        else:
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
            V 0
            """

            if x < width_mm / 2:
                circles_svg += f'''
                 <circle cx="{x + notch_width / 2 + 10}"
                    cy="{notch_height / 2}"
                    r="{screw_d / 2}" />
                 '''
                circles_svg += f'''
                 <circle cx="{x + notch_width / 2 - 10}"
                    cy="{notch_height / 2}"
                    r="{screw_d / 2}" />
                 '''
            elif x > width_mm / 2:
                circles_svg += f'''
                 <circle cx="{x + notch_width / 2 - 10}"
                    cy="{notch_height / 2}"
                    r="{screw_d / 2}"/>
                    '''
                circles_svg += f'''
                 <circle cx="{x + notch_width / 2 + 10}"
                    cy="{notch_height / 2}"
                    r="{screw_d / 2}"/>
                    '''
    # make up down gap
    if width_mm % 20 <= 10 and not width_mm % 20 == 0:
        path_d += f"""
            M 0 {width_mm}
            H {notch_width}
            """
        path_d += f"""
            M {width_mm - notch_width} {width_mm}
            H {width_mm}
            """
    elif width_mm % 20 > 10 and not width_mm % 20 == 0:
        path_d += f"""
            M {notch_height} {width_mm}
            H {notch_width}
            """
        path_d += f"""
            M {width_mm- notch_height} {width_mm}
            H {width_mm - notch_width}
            """
    #down rect
    for x in x_positions:
        if width_mm < 95:
            path_d += f"""
            M {x} {width_mm - notch_height}
            H {x + (notch_width - screw_d) / 2}
            V {width_mm - (notch_height + nut_in)}
            H {x + (notch_width - nut_w) / 2}
            V {width_mm - (notch_height + nut_in + nut_l)}
            H {x + (notch_width - screw_d) / 2}
            V {width_mm - notch_width}
            H {x + (notch_width + screw_d) / 2}
            V {width_mm - (notch_height + nut_in + nut_l)}
            H {x + (notch_width + nut_w) / 2}
            V {width_mm - (notch_height + nut_in)}
            H {x + (notch_width + screw_d) / 2}
            V {width_mm - notch_height}
            H {x + notch_width}
            """

            if x < width_mm / 2:
                circles_svg += f'''
                     <circle cx="{x + notch_width / 2 - 10}"
                        cy="{width_mm - notch_height / 2}"
                        r="{screw_d / 2}" />
                     '''
            elif x > width_mm / 2:
                circles_svg += f'''
                 <circle cx="{x + notch_width / 2 + 10}"
                    cy="{width_mm - notch_height / 2}"
                    r="{screw_d / 2}"/>
                    '''
        else:
            path_d += f"""
            M {x} {width_mm}
            V {width_mm - notch_height}
            H {x + (notch_width - screw_d) / 2}
            V {width_mm - (notch_height + nut_in)}
            H {x + (notch_width - nut_w) / 2}
            V {width_mm - (notch_height + nut_in + nut_l)}
            H {x + (notch_width - screw_d) / 2}
            V {width_mm - notch_width}
            H {x + (notch_width + screw_d) / 2}
            V {width_mm - (notch_height + nut_in + nut_l)}
            H {x + (notch_width + nut_w) / 2}
            V {width_mm - (notch_height + nut_in)}
            H {x + (notch_width + screw_d) / 2}
            V {width_mm - notch_height}
            H {x + notch_width}
            V {width_mm}
            """

            if x < width_mm / 2:
                circles_svg += f'''
                     <circle cx="{x + notch_width / 2 + 10}"
                        cy="{width_mm - notch_height / 2}"
                        r="{screw_d / 2}" />
                     '''
                circles_svg += f'''
                     <circle cx="{x + notch_width / 2 - 10}"
                        cy="{width_mm - notch_height / 2}"
                        r="{screw_d / 2}" />
                     '''
            elif x > width_mm / 2:
                # 右边缺口的凹槽
                circles_svg += f'''
                  <circle cx="{x + notch_width / 2 - 10}"
                    cy="{width_mm - notch_height / 2}"
                    r="{screw_d / 2}"/>
                    '''
                circles_svg += f'''
                 <circle cx="{x + notch_width / 2 + 10}"
                    cy="{width_mm - notch_height / 2}"
                    r="{screw_d / 2}"/>
                    '''

    if width_mm < 95:
        path_d += f'M 20 0 V {notch_height}'
        path_d += f'M {width_mm - 20} 0 V {notch_height}'
        path_d += f'M 20 {width_mm} V {width_mm - notch_height}'
        path_d += f'M {width_mm - 20} {width_mm} V {width_mm - notch_height}'

    # side rect
    y = 10
    step = notch_width + 10

    while y < height_mm:
        if y < height_mm - 10:
            path_d += f"""
                M 0 {y}
                H {notch_height}
                V {y + (notch_width - screw_d)/2}
                H {notch_height + nut_in}
                V {y + (notch_width - nut_w)/2}
                H {notch_height + nut_in + nut_l}
                V {y + (notch_width - screw_d)/2}
                H {notch_width}
                V {y + (notch_width + screw_d)/2}
                H {notch_height + nut_in + nut_l}
                V {y + (notch_width + nut_w)/2}
                H {notch_height + nut_in}
                V {y + (notch_width + screw_d)/2}
                H {notch_height}
                V {y + notch_width}
                H 0
            """
            circles_svg += f'''
                <circle cx="{notch_height / 2}"
                        cy="{y + notch_width / 2 + 10}"
                        r="{screw_d / 2}" />
                '''

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
        elif y == height_mm - 10:
            path_d += f"""
                M 0 {y}
                H {notch_height}
                V {y + notch_width - notch_height}
                H {notch_width}
                V {width_mm}
            """
            path_d += f"""
                M {width_mm} {y}
                H {width_mm - notch_height}
                V {y + notch_width - notch_height}
                H {width_mm - notch_width}
                V {width_mm}
            """
        else:
            path_d += f"""
                M 0 {y}
                H {notch_height}
                V {width_mm}
            """
            path_d += f"""
                M {width_mm} {y}
                H {width_mm - notch_height}
                V {width_mm}
            """
        y += step


    #hollow king image
    embedded_svg = f'''
    <g>
        <path d="M17.375 4.25 C17.91125 4.4975 18.4475 4.745 19 5 C18.979375 5.763125 18.95875 6.52625 18.9375 7.3125 C18.87057159 10.10185786 18.87057159 10.10185786 20 12.999999999999998 C19.505 13.763125 19.01 14.52625 18.5 15.3125 C16.60362745 18.71016749 17.01665642 20.31246156 18 24 C18.33 24.66 18.66 25.32 19 26 C27.58 26 36.16 26 45 26 C47.15919484 18.69880511 47.15919484 18.69880511 44 13 C44.02025451 10.20994186 44.47669087 7.75926634 45 5 C46.625 4.25 46.625 4.25 49 4 C53.7606979 6.47953015 56.73603663 9.12377121 59 14 C60.01340792 21.43510506 59.50208906 26.95433754 55 33 C54.46890625 33.38414063 53.9378125 33.76828125 53.390625 34.1640625 C50.80106259 37.5828668 51.56413466 42.4179325 51.56054688 46.57617188 C51.42703895 51.8198107 50.54496554 54.88346197 47 59 C42.52950365 62.89524866 37.6331768 62.44847622 32 62.375 C31.11054688 62.38660156 30.22109375 62.39820313 29.3046875 62.41015625 C22.82495092 62.3811425 19.51953389 61.34755206 14.7109375 56.8671875 C12.34376797 52.90028696 12.57319232 49.65123379 12.625 45.125 C12.62737547 37.75505442 12.62737547 37.75505442 9 31.5625 C8.01 30.716875 7.02 29.87125 6 29 C4.0422079 22.97662369 4.00046547 16.26053591 6.675 10.5 C13.05 3.78947368 13.05 3.78947368 17.375 4.25 Z M14 8 C10.9332301 10.756442 8.40123603 13.31590049 7.42578125 17.41015625 C7.17011176 23.11423081 8.53714472 26.905834 11.7109375 31.6015625 C12.13632813 32.06304687 12.56171875 32.52453125 13 33 C13.66 33 14.32 33 15 33 C14.96519531 34.00160156 14.93039063 35.00320312 14.89453125 36.03515625 C14.45839979 45.96119362 14.45839979 45.96119362 18 55 C22.33312786 59.22202202 25.90460349 60.13835471 31.8125 60.25 C37.90191174 60.16928615 41.99493406 59.05783084 46.375 54.5625 C49.3077376 49.9377984 49.128386 45.61210687 49.0625 40.25 C49.05798828 39.55261719 49.05347656 38.85523437 49.04882812 38.13671875 C49.0371002 36.42444197 49.01916653 34.71220967 49 33 C49.99 32.67 50.98 32.34 52 32 C55.54289451 27.2423988 56.73899148 23.38865593 56.5390625 17.4453125 C55.62760816 13.31074427 53.0803554 10.76865277 50 8 C48.88267977 9.84334722 48.88267977 9.84334722 48 12 C48.309375 12.928125 48.61875 13.85625 48.9375 14.8125 C50.23609748 18.70829243 49.93911815 21.02680781 49 25 C48.03594077 26.68771075 47.0409554 28.35860132 46 30 C45.07960937 29.84402344 44.15921875 29.68804688 43.2109375 29.52734375 C34.17266167 28.13754777 26.13307741 27.95863216 17 29 C14.06832631 23.37118652 13.73326463 20.22811555 15 14 C15.33 13.34 15.66 12.68 16 12 C15.10836423 9.88316159 15.10836423 9.88316159 14 8 Z" fill="none" stroke="blue" stroke-width="0.05"/>    <path d="M0 0 C3 0.25 3 0.25 5 2.25 C5.265625 4.125 5.265625 4.125 5.25 6.25 C5.25515625 6.95125 5.2603125 7.6525 5.265625 8.375 C5 10.25 5 10.25 3 12.25 C0 12.5 0 12.5 -3 12.25 C-5 10.25 -5 10.25 -5.265625 8.375 C-5.26046875 7.67375 -5.2553125 6.9725 -5.25 6.25 C-5.25515625 5.54875 -5.2603125 4.8475 -5.265625 4.125 C-4.77431879 0.65695617 -3.28862917 0.27405243 0 0 Z" fill="none" stroke="blue" stroke-width="0.05" transform="translate(41,40.75)"/>
        <path d="M0 0 C3 0.25 3 0.25 5 2.25 C5.265625 4.125 5.265625 4.125 5.25 6.25 C5.25515625 6.95125 5.2603125 7.6525 5.265625 8.375 C5 10.25 5 10.25 3 12.25 C0 12.5 0 12.5 -3 12.25 C-5 10.25 -5 10.25 -5.265625 8.375 C-5.26046875 7.67375 -5.2553125 6.9725 -5.25 6.25 C-5.25515625 5.54875 -5.2603125 4.8475 -5.265625 4.125 C-4.77431879 0.65695617 -3.28862917 0.27405243 0 0 Z" fill="none" stroke="blue" stroke-width="0.05" transform="translate(23,40.75)"/>

</g>'''

    svg_content = f'''<?xml version="1.0" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{width_in}in"
     height="{height_in}in"
     viewBox="0 0 {width_mm} {height_mm * 1.2}">

  <path d="{path_d}"
        fill="none"
        stroke="black"
        stroke-width="0.05"
        fill-rule="evenodd"/>
  
  <g fill="none" stroke="green" stroke-width="0.05">
    {circles_svg}
  </g>
  
  <g transform="
     translate({center_x}, {center_y})
     scale({scale})
     translate({-embed_w/2}, {-embed_h/2})"
  >
     {embedded_svg}
  </g>
</svg>
'''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"SVG file '{filename}' generated successfully.")


if __name__ == "__main__":
    try:
        w = float(input("Enter rectangle width (millimeters): "))

        generate_Part2_svg(w)

    except ValueError as e:
        print("Error:", e)