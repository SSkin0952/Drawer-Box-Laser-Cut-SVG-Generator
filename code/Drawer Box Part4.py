def generate_Part4_svg(width_mm, height_mm, filename="Drawer Box part4.svg"):
    if width_mm <= 60 or height_mm <= 60:
        raise ValueError("Width and height must be more than 60mm.")
    if width_mm > 150 or height_mm > 150:
        raise ValueError("Width and height must be 150mm or smaller.")

    real_height = ((height_mm * 0.25) ** 2 + width_mm ** 2) ** 0.5 + 5  # 不再额外增加高度

    notch_height = 4
    rect_width = width_mm - notch_height - 2
    rect_height = real_height

    rect_x = (width_mm - rect_width) / 2
    rect_y = 0

    # ===== CU image parameters =====
    cu_w = 1264
    cu_h = 1028

    width_scale = (rect_width * 0.6) / cu_w
    height_scale = (rect_height * 0.6) / cu_h
    scale = min(width_scale, height_scale)

    image_w = cu_w * scale
    image_h = cu_h * scale

    image_x = rect_x + (rect_width - image_w) / 2
    image_y = rect_y + (rect_height - image_h) / 2

    # text parameters
    text_x = width_mm / 2
    text_y = rect_height * 0.85

    # ===== CU path =====
    embedded_svg = f'''
    <g transform="translate({image_x:.3f},{image_y:.3f}) scale({scale:.6f})">
    <path d="m620 4-14 1-2 1-2 54-51 1-5 2-3 9-1 5v32l3 11 4 3 13 1h40l2 9 1 11v22l-2 10-4 6-12 9-10 9-5 5-8 9-8 13-7 16-4 14-1 8v12l4 16 4 10 11 18 10 14 10 10v2l-9 7-11 14-10 7-10-1-39-9-52-14-28-7-49-16-35-11-30-8-30-5-51-7-11-1h-49l-30 5-29 7-14 6-17 12-10 8-10 9-14 14-9 13-8 16-10 30-5 26v42l5 27 11 44 8 19 12 22 9 19 4 9 24 40 13 24 17 28 9 16 6 15 14 30 7 19 6 21 4 35 3 31 1 1h933l1-1 2-24 5-33 8-36 6-16 16-32 13-27 14-24 9-14 6-9 6-14 10-17 11-17 7-14 6-15 9-17 12-29 6-23 4-30 2-10v-33l-6-43-5-14-9-17-8-12-11-13-13-13-14-11-14-10-15-7-21-6-26-5-13-2h-49l-47 6-40 6-25 6-26 8-49 16-31 9-36 9-28 8-44 10-11 1-12-12-6-7-9-7-3-2-1-3 5-2 12-11 7-11 8-16 4-9 4-14v-20l-5-19-8-19-7-12-9-9-11-9-15-13-4-5-2-6-1-8v-11l2-18 3-6v-2h46l6-2 6-7 2-7v-28l-3-13-2-4-5-2-11-1h-39l-1-1-1-43-1-9-3-2z" fill="none" stroke="blue" stroke-width="1"/>
    <path d="m1034 351h39l16 2 18 4 20 7 13 7 14 11 14 14 9 13 4 13 4 27v26l-5 40-5 17-9 21-10 20-6 10-6 13-8 16-11 18-7 11-14 26-13 17-7 11-9 15-7 9-11 13-10 13-10 14-4 5-11 9-13 13-8 7-15 11-17 9-13 3h-22l-13-4-8-7-4-6-2-8v-26l4-16 6-11 8-7 43-2 25-3 7-3 5-8 2-9 2-32-52 2h-21l-2-1 1-10 7-31 4-15v-4l-4-1h-32l-21 4-3 3-6 18-8 37-1 1-66 1-7 19-6 22-2 12 63 1 5 4v9l-5 15-14 21-8 10-10 9-14 9-10 5-19 3h-10l-13-2-12-6-10-9-12-14-11-15-8-16-10-31-4-16-1-7v-31l3-26 8-41 8-35 7-19 8-16 8-17 6-16 9-32 2-10v-13l9-6 22-12 23-11 20-8 22-8 28-7 61-19 43-12 37-8 12-2z" fill="none" stroke="blue" stroke-width="1"/>
    <path d="m189 351h40l24 3 30 6 45 12 45 14 52 15 26 9 36 16 23 13 8 5 1 4v13l4 17 16 44 14 30 7 20 6 21 5 30 6 41 1 16v14l-2 16-8 35-5 13-7 12-9 12-11 14-7 8-13 8-12 4-7 1h-14l-14-3-17-8-12-9-10-11-8-11-9-13-4-8-2-6v-11l4-4 2-1h50l10-2v-8l-8-35-3-9-63-1-4-4-5-16-9-30-4-8-8-3-12-2h-32l-6 1 1 10 10 30 2 9v11l-4 1h-16l-56-2 3 23 5 24 1 3 8 2 21 3 15 1 31 1 8 7 7 14 4 15 1 16-2 10-6 11-8 7-10 4-4 1h-21l-15-4-17-9-13-10-15-14-13-12-8-9-8-11-14-17-11-14-10-16-12-17-9-13-14-26-14-21-9-17-8-16-15-26-10-23-7-26-6-31-2-14v-14l2-16 5-19 4-11 3-9 7-8 12-12 14-10 10-6 15-6 14-4 15-3z" fill="none" stroke="blue" stroke-width="1"/>
    <path d="m165 945h945v75l-567 1h-80l-306-1-1-1v-73z" fill="none" stroke="blue" stroke-width="1"/>
</g>'''

    # ===== Final SVG =====
    svg_content = f'''<?xml version="1.0" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{width_mm}mm"
     height="{real_height}mm"
     viewBox="0 0 {width_mm} {real_height}">

  <rect x="{rect_x}"
        y="{rect_y}"
        width="{rect_width}"
        height="{rect_height}"
        fill="none"
        stroke="black"
        stroke-width="0.05"/>

  {embedded_svg}

  <text x="{text_x}"
        y="{text_y}"
        text-anchor="middle"
        font-family="Arial"
        font-size="{width_mm * 0.09}"
        fill="red">
    Digital Manufacturing
  </text>
</svg>
'''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"SVG file '{filename}' generated successfully.")


if __name__ == "__main__":
    try:
        w = float(input("Enter width (mm): "))
        h = float(input("Enter height (mm): "))
        generate_Part4_svg(w, h)
    except ValueError as e:
        print("Error:", e)