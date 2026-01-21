# Pendulum Post-Processing Pipeline for MBDyn

This repository demonstrates a complete, headless post-processing pipeline for
MBDyn (MultiBody Dynamics) simulations using Python.

The project focuses on converting raw MBDyn simulation output (`.mov` files)
into meaningful physical quantities and visualizations, including plots and
animated videos.

Currently, the pipeline is demonstrated using a simple pendulum system.

---

## Motivation

MBDyn produces accurate physical simulation data, but its raw output is not
directly suitable for analysis or visualization.

The objective of this project is to:
- Interpret raw MBDyn output data
- Extract physically meaningful quantities (e.g., angular displacement)
- Validate simulation results through plots and animations
- Provide a reusable, automated post-processing workflow

This work is intended as a preparatory contribution toward Google Summer of Code
with the MBDyn organization.

---

## Features

- Parses MBDyn `.mov` output files
- Converts raw nodal coordinate data into NumPy arrays
- Computes pendulum angular displacement (θ)
- Plots θ vs time
- Generates MP4 animations using Matplotlib (headless, no GUI required)
- Optional FreeCAD-based 3D visualization

---

## Pipeline Overview

MBDyn → .mov → Python parsing → NumPy arrays → Plots → MP4 animation

### Pipeline Description

1. **MBDyn Simulation**  
   MBDyn generates raw output (`.mov`) containing the coordinates of structural
   nodes (e.g., hinge point and pendulum bob).

2. **Data Processing**  
   Python scripts extract nodal coordinates and compute the angular displacement
   θ of the pendulum using geometric relations.

3. **Analysis & Visualization**  
   - Angular displacement is plotted as θ vs time.
   - A headless Matplotlib animation is generated and exported as an MP4 file.

4. **Optional FreeCAD Visualization**  
   A FreeCAD-based script can be used to visualize motion in 3D by updating
   object positions frame-by-frame using MBDyn output data.

---

## Requirements

- Python 3.10+
- NumPy
- Matplotlib
- FFmpeg (for video generation)

---

## Usage

1. Parse MBDyn output:
```bash
python scripts/parse_mbdyn_output.py

