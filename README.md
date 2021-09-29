# ROS2-101
Some ROS2 examples made during my exploration to complement the available documentation &amp; tutorials

## installation
- install ros2 [foxy](https://docs.ros.org/en/foxy/Installation.html)

- add .vscode ros [extension](https://marketplace.visualstudio.com/items?itemName=ms-iot.vscode-ros)

## information sources
- https://docs.ros.org/en/foxy/Tutorials.html



## ROS2 commands / information

running ros code always involves a few steps:
- create a common `/src` folder to keep the top level clean
- create packages
- write code for the packages
- create the build files that are required for colcon (ament) to build and connect everything
- run the executable nodes or run launch files (after creating them)


### package creation
 (cf https://docs.ros.org/en/foxy/Tutorials/Creating-Your-First-ROS2-Package.html)
- python: `ros2 pkg create <package name> [--node-name <node name> ] --build-type ament_python --dependencies rclpy`
- cpp: `ros2 pkg create --build-type ament_cmake [--node-name <node name>] <package name>  --dependencies rclcpp`

where `ament_cmake/python` tells colcon which additional files to create to build the packages (setup.cfg setup.py vs cmakelist.txt)

### cmakelist syntax

### setup.py syntax


#### run vs launch
- `ros2 run` can run all executables that were linked in the setup.py entrypoints or as executable in the cmake file
- `ros2 launch` uses "launchfiles" that can launch multiple nodes (executables typically run 1 node). 

### launch files (python)

### debugging / visualisation
- rqt 
-rqt_graph (nodes/topics)
- cli interface with topics/services/actions/...