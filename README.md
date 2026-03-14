# Parametric Drawer Box Laser-Cut SVG Generator

A Python-based parametric generator for creating SVG files used in laser cutting a **Drawer Box** structure.

This project was developed for **MECEE4606 – Digital Manufacturing at Columbia University**.  
The software automatically generates precise SVG drawings of drawer box components with assembly notches, screw holes, and decorative patterns, making them ready for **laser cutting or CNC fabrication**.

The design is **fully parametric**, allowing users to change the box dimensions and automatically regenerate all parts.

---

## Project Overview

The project combines **digital fabrication**, **parametric design**, and **Python-based geometry generation**.

The program:

- Generates SVG cutting files for each structural component
- Calculates notch geometry for mechanical assembly
- Automatically places screw holes and nut slots
- Adds optional decorative elements (e.g., snowflake pattern, hollow knight)
- Ensures dimensional constraints required for fabrication

All generated files can be directly used in **laser cutting software such as LightBurn, Illustrator, or CorelDRAW**.

---

## Final Product

Example laser-cut drawer boxes produced using the generated SVG files.

![Drawer Box](images/1.png)
![Drawer Box](images/2.png)
![Drawer Box](images/3.png)
![Drawer Box](images/4.png)

---

## Features

- Parametric drawer box design
- Automatic notch generation for panel assembly
- Screw hole and nut slot placement
- Error detection for invalid dimensions
- Decorative vector pattern generation
- Manufacturing-ready SVG output

---
## Parametric Constraints

The program enforces fabrication constraints to ensure the box can be manufactured properly.

Example limits:

- Width: **60 mm < width ≤ 150 mm**
- Height: **60 mm < height ≤ 150 mm**
- Notch height: **4 mm**
- Notch width: **10 mm**
- Screw diameter: **2.3 mm**

These parameters ensure that joints, screw holes, and assembly slots remain valid for fabrication.

---

## How It Works

The Python scripts generate SVG geometry using coordinate-based vector drawing.

Core steps include:

1. Define input parameters (box width and height)
2. Compute notch positions and panel edges
3. Generate screw hole coordinates
4. Construct SVG paths using `M`, `L`, and `Z` commands
5. Export the SVG file for laser cutting

Example mathematical conversion:

x = center_x + radius * cos(angle)
y = center_y + radius * sin(angle)

This allows procedural generation of decorative elements such as the snowflake pattern.

---

## Usage

Run the Python script and enter the desired box dimensions.

Example:

python
Drawer Box Part1.py

Input:

Enter rectangle width (millimeters): 100
Enter rectangle height (millimeters): 100

Output:

SVG file 'Drawer Box part1.svg' generated successfully.

The generated SVG file can then be opened in a laser cutter software.

## Example SVG Output

Example of generated cutting layout:

## Hardware

The drawer box panels are assembled using standard machine screws and square nuts.  
The following hardware was used in the physical prototype:

- Square Nut (2-56 thread)  
  https://www.mcmaster.com/products/94855a279/

- Pan Head Phillips Machine Screw (2-56 thread)  
  https://www.mcmaster.com/91772A079/

These components were selected because they are small enough to fit within the notch geometry while still providing reliable fastening for acrylic panels.

Typical specifications:

- Thread size: **2-56**
- Material: **18-8 stainless steel screw**
- Head type: **Phillips pan head**
- Compatible with square nuts for easy alignment inside laser-cut slots

Square nuts are particularly useful in laser-cut assemblies because their flat sides prevent rotation inside square pockets or channels during tightening. :contentReference[oaicite:0]{index=0}

## Manufacturing Process

Generate SVG cutting files using the Python scripts

Import the SVG files into laser cutting software

Cut panels from acrylic or wood sheets

Assemble panels using screws and interlocking notches

Install sliding lid to complete the drawer box

## Course Information

This project was completed as part of:

MECEE4606 – Digital Manufacturing
Columbia University

Assignment: Laser Cut Vessel

## Author

Wei Sun(ws2782@columbia.edu)
Columbia University
MS Mechanical Engineering