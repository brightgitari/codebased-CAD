"""import sys
sys.path.append('C:/Program Files/FreeCAD 1.0/bin')  

import FreeCAD as App
import Part
from FreeCAD import Gui

# clear any open document
if App.activeDocument():
    App.closeDocument(App.activeDocument().Name)

# create a new document
doc = App.newDocument("simple-box")
width = 50
length = 30
height = 20
my_box = Part.makeBox(width, length, height)

box_obj = doc.addObject("Part::Feature", "MyBox")
box_obj.Shape = my_box
doc.recompute()
Gui.SendMsgToActiveView("View Fit")
num_i
"""
for i in range (5):
    size = 50 - (i * 8)
    height = i * 10

    print(f"Box {i + 1}")
    print(f"size: {size} x {size}")
    print(f"Height Position : {height}")
    print("_" * 30)