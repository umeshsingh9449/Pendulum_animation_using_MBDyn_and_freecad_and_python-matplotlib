import FreeCAD
import Part

doc = FreeCAD.newDocument("Pendulum")

# Parameters (meters)
rod_length = 1.0
rod_radius = 0.005
bob_radius = 0.08

# Rod (pivot at origin)
rod = doc.addObject("Part::Feature", "Rod")
rod.Shape = Part.makeCylinder(rod_radius, rod_length)
rod.Placement.Base = FreeCAD.Vector(0, 0, -rod_length)

# Bob
bob = doc.addObject("Part::Feature", "Bob")
bob.Shape = Part.makeSphere(bob_radius)
bob.Placement.Base = FreeCAD.Vector(
    0, 0, -rod_length - bob_radius
)

doc.recompute()
doc.saveAs("../models/pendulum3.FCStd")

print("Pendulum model created (geometry only).")
