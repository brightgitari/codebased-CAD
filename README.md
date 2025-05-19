
🦾3-DOF Robot Arm Design in FreeCAD with Python
This project demonstrates how to model a 3-degree-of-freedom (3-DOF) robot arm using Python scripting within FreeCAD. The script is modular, descriptive, and suitable for beginners and intermediate CAD/robotics users aiming to understand programmatic parametric modeling.

🧠 Purpose
The goal is to create a simple articulated robot arm composed of:
•	A base with a fixed mount
•	Three articulated links (Link 1, Link 2, Link 3)
•	Rotational joints (J1, J2, J3)
•	A gripper assembly to represent the end-effector
•	Joint markers and axes indicators for visualization
•	Labels for easy identification of joints
This model is primarily useful for educational demonstrations, robot kinematics visualizations, and early-stage design prototyping.

📁 File Structure
The repository includes:
•	robot_arm_freecad.py: Main script for generating the robot arm geometry.
•	(Optional) preview.png: A screenshot or render of the final robot arm.
•	README.md or this document: Project explanation.

🔧 How It Works – Component Breakdown
1. Base
A rectangular block that acts as the robot arm’s foundation. A joint pin (J1) extends upward from the center to anchor Link 1.
base = Part.makeBox(base_width, base_depth, base_height)
2. Link 1
•	A box-shaped link with two cylindrical holes—one for the base pin (J1) and one to connect to Link 2 via J2.
•	Positioned and rotated at -45° around the Y-axis to simulate motion.
3. Link 2
•	Similar to Link 1 but rotated 30° in the opposite direction to illustrate compound joint rotation.
•	Mounted at J2.
4. Link 3 (Gripper Mount)
•	A shorter link serving as the mount for the gripper.
•	Rotated slightly (-10°) for realism and orientation.
5. Gripper
•	Composed of a main body and two rectangular fingers (upper and lower).
•	Designed as a simple two-prong clamp.
6. Joints
•	Cylindrical pins (J1, J2, J3) represent revolute joints.
•	Joint markers (red spheres) and axes (green cylinders) help users understand rotational axes.
7. Annotations
•	Labels (J1, J2, J3) are added to clarify the joint locations.

🧰 Dependencies
•	FreeCAD (tested with v0.20+)
•	Python (FreeCAD’s embedded Python console or standalone interpreter with FreeCAD module path added)

▶️ Running the Script
Option 1: Inside FreeCAD
1.	Open FreeCAD.
2.	Go to the Python console or the Macro editor.
3.	Paste and run the script.
Option 2: From Terminal
Make sure FreeCAD’s Python environment is correctly set up.
freecadcmd robot_arm_freecad.py

📐 Design Considerations
•	Parametric Modeling: All dimensions (lengths, offsets, rotations) are controlled via variables for easy adjustment.
•	Clear Visual Hierarchy: Color coding and annotations enhance readability.
•	Realistic Constraints: Joint placements and axis orientations mimic real-world robotic arms.


✍️ Customization Tips
You can adapt the script by:
•	Changing joint angles to simulate different postures.
•	Modifying link lengths to test different arm reaches.
•	Adding servos, gears, or sensor placeholders.
•	Exporting parts as .STEP files for mechanical simulation or 3D printing.

📚 License
This project is open-source.
👤 Author
Script developed and maintained by Bright Mutuma
Feel free to contribute, raise issues, or fork for your own robotic creations!

