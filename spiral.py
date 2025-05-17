import FreeCAD as App
import Part
from FreeCAD import Gui, Base
import math
import numpy as np
doc = App.newDocument ("spiral - staircase")
num_steps = 12
steps_angle = 30
radius = 40
step_height = 10
step_size = 30

for i in range(num_steps):
    angle = i * steps_angle
    x = radius * np.cos(np.radians (angle))
    y = radius * np.sin(np.radians(angle))
    z = i * step_height
    step = Part.makeBox(step_size, step_size/3, step_height/2)
    step.rotate(Base.Vector (0,0,0), Base.Vector (0,0,1), angle)
    step.translate(Base.Vector(x, y, z))
    step_obj = doc.addObject("Part::Feature", f"step_{i+1}")
    step_obj.Shape = step
     #let us now add color to our project
    color_value = i/num_steps
    step_obj.ViewObject.ShapeColor = (0.3, 0.5, color_value)
doc.recompute()
Gui.SendMsgToActiveView("ViewFit")
