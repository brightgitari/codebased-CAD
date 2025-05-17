import FreeCAD as App
import Part
import Draft
from FreeCAD import Base
import math

# Create a new document
doc = App.newDocument("RobotArm")

# Define colors
base_color = (0.35, 0.35, 0.35)  # Dark gray for the base
link_color = (0.7, 0.7, 0.7)     # Medium gray for links
joint_pin_color = (0.2, 0.2, 0.2)  # Dark gray for joint pins

# Dimensions
base_height = 120
base_width = 60
base_depth = 60

link1_length = 100
link1_width = 30
link1_height = 20
link1_offset = 15  # Distance from end to joint center

link2_length = 100
link2_width = 30
link2_height = 20
link2_offset = 15  # Distance from end to joint center

link3_length = 60
link3_width = 30
link3_height = 20
link3_offset = 15  # Distance from end to joint center

joint_pin_radius = 6
joint_pin_length = 40
joint_hole_radius = 6.5  # Slightly larger than pin

# Create base
base = Part.makeBox(base_width, base_depth, base_height)
base.translate(Base.Vector(-base_width/2, -base_depth/2, 0))
base_obj = doc.addObject("Part::Feature", "Base")
base_obj.Shape = base
base_obj.ViewObject.ShapeColor = base_color

# Joint 1 position
j1_pos = Base.Vector(0, 0, base_height)

# Create joint pin for J1 that sticks out of the base
j1_pin = Part.makeCylinder(joint_pin_radius, joint_pin_length, 
                          j1_pos - Base.Vector(0, joint_pin_length/2, 0), 
                          Base.Vector(0, 1, 0))
j1_pin_obj = doc.addObject("Part::Feature", "J1_Pin")
j1_pin_obj.Shape = j1_pin
j1_pin_obj.ViewObject.ShapeColor = joint_pin_color

# Create Link 1 (first create a box)
link1_box = Part.makeBox(link1_length, link1_width, link1_height)

# Create hole for J1 connection (not at the edge, but offset from end)
link1_hole1 = Part.makeCylinder(joint_hole_radius, link1_width + 10, 
                              Base.Vector(link1_offset, -5, link1_height/2), 
                              Base.Vector(0, 1, 0))

# Create hole for J2 connection (offset from the other end)
link1_hole2 = Part.makeCylinder(joint_hole_radius, link1_width + 10, 
                              Base.Vector(link1_length - link1_offset, -5, link1_height/2), 
                              Base.Vector(0, 1, 0))

# Cut the holes from the link
link1_shape = link1_box.cut(link1_hole1)
link1_shape = link1_shape.cut(link1_hole2)

# Position and rotate link1
link1_shape.rotate(Base.Vector(link1_offset, 0, 0), Base.Vector(0, 1, 0), -45)
link1_pos = j1_pos + Base.Vector(-link1_offset, -link1_width/2, -link1_height/2)
link1_shape.translate(link1_pos)

# Add Link1 to document
link1_obj = doc.addObject("Part::Feature", "Link1")
link1_obj.Shape = link1_shape
link1_obj.ViewObject.ShapeColor = link_color

# Calculate J2 position based on Link 1's angle
link1_effective_length = link1_length - 2*link1_offset
j2_offset_x = link1_offset + link1_effective_length * math.cos(math.radians(45))
j2_offset_z = link1_effective_length * math.sin(math.radians(45))
j2_pos = j1_pos + Base.Vector(j2_offset_x, 0, j2_offset_z)

# Create joint pin for J2
j2_pin = Part.makeCylinder(joint_pin_radius, joint_pin_length, 
                          j2_pos - Base.Vector(0, joint_pin_length/2, 0), 
                          Base.Vector(0, 1, 0))
j2_pin_obj = doc.addObject("Part::Feature", "J2_Pin")
j2_pin_obj.Shape = j2_pin
j2_pin_obj.ViewObject.ShapeColor = joint_pin_color

# Create Link 2
link2_box = Part.makeBox(link2_length, link2_width, link2_height)

# Create hole for J2 connection
link2_hole1 = Part.makeCylinder(joint_hole_radius, link2_width + 10, 
                              Base.Vector(link2_offset, -5, link2_height/2), 
                              Base.Vector(0, 1, 0))

# Create hole for J3 connection
link2_hole2 = Part.makeCylinder(joint_hole_radius, link2_width + 10, 
                              Base.Vector(link2_length - link2_offset, -5, link2_height/2), 
                              Base.Vector(0, 1, 0))

# Cut the holes from the link
link2_shape = link2_box.cut(link2_hole1)
link2_shape = link2_shape.cut(link2_hole2)

# Position and rotate link2 (angled slightly up from J2)
link2_shape.rotate(Base.Vector(link2_offset, 0, 0), Base.Vector(0, 1, 0), 30)
link2_pos = j2_pos + Base.Vector(-link2_offset, -link2_width/2, -link2_height/2)
link2_shape.translate(link2_pos)

# Add Link2 to document
link2_obj = doc.addObject("Part::Feature", "Link2")
link2_obj.Shape = link2_shape
link2_obj.ViewObject.ShapeColor = link_color

# Calculate J3 position
link2_effective_length = link2_length - 2*link2_offset
j3_offset_x = link2_offset + link2_effective_length * math.cos(math.radians(-30))
j3_offset_z = link2_effective_length * math.sin(math.radians(-30))
j3_pos = j2_pos + Base.Vector(j3_offset_x, 0, j3_offset_z)

# Create joint pin for J3
j3_pin = Part.makeCylinder(joint_pin_radius, joint_pin_length, 
                         j3_pos - Base.Vector(0, joint_pin_length/2, 0), 
                         Base.Vector(0, 1, 0))
j3_pin_obj = doc.addObject("Part::Feature", "J3_Pin")
j3_pin_obj.Shape = j3_pin
j3_pin_obj.ViewObject.ShapeColor = joint_pin_color

# Create Link 3 (gripper mount)
link3_box = Part.makeBox(link3_length, link3_width, link3_height)

# Create hole for J3 connection
link3_hole = Part.makeCylinder(joint_hole_radius, link3_width + 10, 
                             Base.Vector(link3_offset, -5, link3_height/2), 
                             Base.Vector(0, 1, 0))

# Cut the hole from the link
link3_shape = link3_box.cut(link3_hole)

# Position and rotate link3
link3_shape.rotate(Base.Vector(link3_offset, 0, 0), Base.Vector(0, 1, 0), -10)
link3_pos = j3_pos + Base.Vector(-link3_offset, -link3_width/2, -link3_height/2)
link3_shape.translate(link3_pos)

# Add Link3 to document
link3_obj = doc.addObject("Part::Feature", "Link3")
link3_obj.Shape = link3_shape
link3_obj.ViewObject.ShapeColor = link_color

# Create a gripper (forked end)
# Create the main body
gripper_length = 20
gripper_width = 30
gripper_height = 15
finger_length = 20
finger_width = 10
finger_height = 10

# Calculate position for the gripper body
gripper_offset_x = link3_length - link3_offset
gripper_offset_z = 0  # No z offset for simplicity
gripper_base_pos = link3_pos + Base.Vector(link3_offset, 0, 0)
gripper_rotation_matrix = App.Rotation(App.Vector(0,1,0), -10).toMatrix()
gripper_dir = gripper_rotation_matrix.multiply(App.Vector(1,0,0))
gripper_pos = gripper_base_pos + gripper_dir.multiply(gripper_offset_x - link3_offset)
gripper_pos = gripper_pos + Base.Vector(0, -gripper_width/2 + link3_width/2, -gripper_height/2 + link3_height/2)

# Create the gripper body
gripper_body = Part.makeBox(gripper_length, gripper_width, gripper_height)
gripper_body.translate(gripper_pos)
gripper_body.rotate(gripper_pos + Base.Vector(0, gripper_width/2, gripper_height/2), Base.Vector(0, 1, 0), -10)
gripper_obj = doc.addObject("Part::Feature", "GripperBody")
gripper_obj.Shape = gripper_body
gripper_obj.ViewObject.ShapeColor = base_color

# Create the fingers
# Upper finger
upper_finger = Part.makeBox(finger_length, finger_width, finger_height)
upper_finger_pos = gripper_pos + Base.Vector(gripper_length, (gripper_width - finger_width)/2, gripper_height - finger_height)
upper_finger.translate(upper_finger_pos)
upper_finger.rotate(gripper_pos + Base.Vector(gripper_length, gripper_width/2, gripper_height/2), Base.Vector(0, 1, 0), -10)
upper_finger_obj = doc.addObject("Part::Feature", "UpperFinger")
upper_finger_obj.Shape = upper_finger
upper_finger_obj.ViewObject.ShapeColor = base_color

# Lower finger
lower_finger = Part.makeBox(finger_length, finger_width, finger_height)
lower_finger_pos = gripper_pos + Base.Vector(gripper_length, (gripper_width - finger_width)/2, 0)
lower_finger.translate(lower_finger_pos)
lower_finger.rotate(gripper_pos + Base.Vector(gripper_length, gripper_width/2, gripper_height/2), Base.Vector(0, 1, 0), -10)
lower_finger_obj = doc.addObject("Part::Feature", "LowerFinger")
lower_finger_obj.Shape = lower_finger
lower_finger_obj.ViewObject.ShapeColor = base_color

# Add Joint markers for visualization
# J1 marker
j1_marker = Part.makeSphere(3)
j1_marker.translate(j1_pos)
j1_marker_obj = doc.addObject("Part::Feature", "J1_Marker")
j1_marker_obj.Shape = j1_marker
j1_marker_obj.ViewObject.ShapeColor = (0.8, 0, 0)  # Red

# J2 marker
j2_marker = Part.makeSphere(3)
j2_marker.translate(j2_pos)
j2_marker_obj = doc.addObject("Part::Feature", "J2_Marker")
j2_marker_obj.Shape = j2_marker
j2_marker_obj.ViewObject.ShapeColor = (0.8, 0, 0)  # Red

# J3 marker
j3_marker = Part.makeSphere(3)
j3_marker.translate(j3_pos)
j3_marker_obj = doc.addObject("Part::Feature", "J3_Marker")
j3_marker_obj.Shape = j3_marker
j3_marker_obj.ViewObject.ShapeColor = (0.8, 0, 0)  # Red

# Add labels for joints
# J1 label
j1_label = doc.addObject("App::Annotation", "J1_Label")
j1_label.LabelText = "J1"
j1_label.Position = j1_pos + Base.Vector(-20, 0, 10)
j1_label.ViewObject.FontSize = 14
j1_label.ViewObject.TextColor = (0, 0, 0)

# J2 label
j2_label = doc.addObject("App::Annotation", "J2_Label") 
j2_label.LabelText = "J2"
j2_label.Position = j2_pos + Base.Vector(-10, 0, 15)
j2_label.ViewObject.FontSize = 14
j2_label.ViewObject.TextColor = (0, 0, 0)

# J3 label
j3_label = doc.addObject("App::Annotation", "J3_Label")
j3_label.LabelText = "J3"
j3_label.Position = j3_pos + Base.Vector(10, 0, 15)
j3_label.ViewObject.FontSize = 14
j3_label.ViewObject.TextColor = (0, 0, 0)

# Create a visual representation of the rotation axes
# J1 axis
j1_axis = Part.makeCylinder(1, 50, j1_pos - Base.Vector(0, 25, 0), Base.Vector(0, 1, 0))
j1_axis_obj = doc.addObject("Part::Feature", "J1_Axis")
j1_axis_obj.Shape = j1_axis
j1_axis_obj.ViewObject.ShapeColor = (0, 0.8, 0)  # Green

# J2 axis
j2_axis = Part.makeCylinder(1, 50, j2_pos - Base.Vector(0, 25, 0), Base.Vector(0, 1, 0))
j2_axis_obj = doc.addObject("Part::Feature", "J2_Axis")
j2_axis_obj.Shape = j2_axis
j2_axis_obj.ViewObject.ShapeColor = (0, 0.8, 0)  # Green

# J3 axis
j3_axis = Part.makeCylinder(1, 50, j3_pos - Base.Vector(0, 25, 0), Base.Vector(0, 1, 0))
j3_axis_obj = doc.addObject("Part::Feature", "J3_Axis")
j3_axis_obj.Shape = j3_axis
j3_axis_obj.ViewObject.ShapeColor = (0, 0.8, 0)  # Green

# Recompute and fit view
doc.recompute()
Gui.SendMsgToActiveView("ViewFit")

print("Robot arm created successfully!")
