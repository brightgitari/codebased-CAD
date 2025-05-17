import FreeCAD as App
import Part
from FreeCAD import Gui, Base
doc = App.newDocument("Tower_of_boxes")
num_boxes = 5
for i in range(num_boxes):
    size = 50 - (i * 8)
    height = 10
    box = Part.makeBox(size, size, height)
    z_pos = i * height # Stack them
    box.translate (Base.Vector (0, 0, z_pos))
    box_obj = doc.addObject("Part::Feature", f" Box_{i +1}")
    box_obj.Shape = box
doc.recompute
Gui.SendMsgToActiveView("ViewFit")
