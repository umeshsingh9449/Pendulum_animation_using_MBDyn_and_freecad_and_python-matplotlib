import FreeCAD
import ImportGui
import os
import time

doc = FreeCAD.open("../models/pendulum.FCStd")
rod = doc.getObject("Rod")
bob = doc.getObject("Bob")

os.makedirs("../frames", exist_ok=True)

frame = 0

with open("../outputs/pendulum.mov") as f:
    for line in f:
        if line.startswith("#"):
            continue

        data = list(map(float, line.split()))

        px, py, pz = data[1:4]
        r11, r12, r13 = data[4:7]
        r21, r22, r23 = data[7:10]
        r31, r32, r33 = data[10:13]

        rot = FreeCAD.Rotation(
            FreeCAD.Matrix(
                r11, r12, r13, 0,
                r21, r22, r23, 0,
                r31, r32, r33, 0,
                0,   0,   0,   1
            )
        )

        rod.Placement = FreeCAD.Placement(
            FreeCAD.Vector(px, py, pz),
            rot
        )
        bob.Placement = rod.Placement

        doc.recompute()

        # Export snapshot
        ImportGui.export(
            [rod, bob],
            f"../frames/frame_{frame:04d}.step"
        )

        frame += 1
        time.sleep(0.02)

print("Frames exported.")
