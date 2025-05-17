import FreeCAD as App
import Part
from FreeCAD import Gui, Base
import math
import numpy as np
import time

doc = App.newDocument("rotating_box")
cube = Part.makeBox(20,20,20)
cube_obj = doc.addObject("Part::Feature", "AnimatedCue")
cube_obj.Shape = cube_obj.Shape = cube
cube_obj.ViewObject.ShapeColor = (1.0, 0.0, 0.0)
doc.recompute()
Gui.SendMsgToActiveView("ViewFit")

#Rotating Loop

for angle in range(0,360,10):
    cube_obj.Placement = App.Placement(
        Base.Vector(0,0,0),
        Base.Rotation(Base.Vector(1,1,0),
        angle))
    doc.recompute()
    time.sleep(0.1)
