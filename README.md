# ROS2-101
Some ROS2 examples made during my exploration to complement the available documentation &amp; tutorials

## installation
- install [ros2 foxy](https://docs.ros.org/en/foxy/Installation.html)

- add [.vscode ros extension](https://marketplace.visualstudio.com/items?itemName=ms-iot.vscode-ros), cmake, cmaketools, pylance, c++ intellisense (and configure, see vs code setup link)

## information sources
- https://docs.ros.org/en/foxy/Tutorials.html
- example node https://github.com/SteveMacenski/slam_toolbox/tree/foxy-devel (and Nav2 stack in general)
- [gh actions CI](https://github.com/marketplace/actions/ros-2-ci-action#Build-and-run-tests-for-your-ROS-2-package)
- [vs code setup](https://samarth-robo.github.io/blog/2020/12/03/vscode_ros.html)



## ROS2
ROS can be seen as a core message passing system over a middleware, that allows to create software components (nodes) that can interact through async communications (topics w/ publishers and subscribers) or sync communication (services) or long-term communication (action servers). Because of its modularity, ROS allows to reuse nodes in different projects.

More about ROS2 vs. ROS1 [here](https://roboticsbackend.com/ros1-vs-ros2-practical-overview/#Why_ROS2_and_not_keep_ROS1)


create ros systems always involves a few steps:
- create a common `/src` folder to keep the top level clean
- create packages
- write code for the packages to build nodes (or in cpp [Components](https://docs.ros.org/en/foxy/Concepts/About-Composition.html#writing-a-component)) in one of the client library languages.
- create the build files that are required for colcon (ament) to build and connect everything
- run the executable nodes or create launch files



## package creation
### creating new packages
 (cf https://docs.ros.org/en/foxy/Tutorials/Creating-Your-First-ROS2-Package.html)
- rclpy: `ros2 pkg create <package name> [--node-name <node name> ] --build-type ament_python --dependencies rclpy`
- rclcpp: `ros2 pkg create --build-type ament_cmake [--node-name <node name>] <package name>  --dependencies rclcpp`

where `ament_cmake/python` tells colcon which additional files to create to build the packages (setup.cfg setup. py vs cmakelist.txt).
to see examples of this template, see the `empty_{cpp|python}` nodes.

The `package.xml` helps to discover and install dependencies with rosdep using `rosdep install --from-paths src --ignore-src -r -y`

### Nodes vs Composables
in ROS2 (rclcpp), composables are nodes that can be @runtime spinned up on the same process to allow for efficient data-sharing. (cf ROS1 "nodelet")

They use the `composableNode` action in a launch file and should be declared without main function (but included in the component library). This is the preferred way of creating new C++ "nodes".
https://docs.ros.org/en/foxy/Concepts/About-Composition.html#writing-a-component
## package build information
#### cmakelist syntax (rclcpp)
https://docs.ros.org/en/foxy/How-To-Guides/Ament-CMake-Documentation.html


some steps:
- add dependencies for all executables
- link executables
- library -> same + header discovery
- other folders -> migrate to share.

A nicely documented example can be found [here](https://github.com/ros-planning/moveit2/blob/foxy/moveit_ros/moveit_servo/CMakeLists.txt)
#### setup. py syntax (rclpy)
just include the executables (entrypoints).. no build etc required, so considerably easier.
Don't forget to include the launch files if applicable (see )

## Executing Nodes
There are two ways to start up nodes:

- `ros2 run` can run all executables that were linked in the setup.py entrypoints or as executable in the cmake file
- `ros2 launch` uses "launchfiles" that can launch multiple nodes (executables typically run 1 node).

both command will look in the `/lib` folder when using the ` <package> <executable/launch>` syntax. Alternatively you can navigate to the source file which avoids the need for having it in lib (useful for testing launch files)

### launch files (python)
ROS2 has created a new syntax for launching multiple nodes etc. from python.

More information:
- basic tutorial - https://docs.ros.org/en/foxy/Tutorials/Launch-system.html
- advanced (source code == documentation..):
    - [ launch system](https://github.com/ros2/launch/blob/foxy/launch/doc/source/architecture.rst)
    - [ros launch syntax](https://github.com/ros2/launch_ros/tree/master/launch_ros/launch_ros)

- launch files can also be [nested](https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver/blob/foxy/ur_bringup/launch/ur3e.launch.py)
## Coding
### using virtualenvs for python
https://docs.ros.org/en/foxy/How-To-Guides/Using-Python-Packages.html#installing-via-a-virtual-environment
### creating custom interfaces
https://docs.ros.org/en/foxy/Concepts/About-ROS-Interfaces.html
### using parameters
https://docs.ros.org/en/foxy/Tutorials/Using-Parameters-In-A-Class-Python.html#pythonparamnode

### debugging / visualisation
- rqt (can also view log/topics/...)
-rqt_graph (nodes/topics)
- cli interface with topics/services/actions/...

### testing
- build using colcon  **from ws root!** (with arg to create compilation database for vscode IDE ) `colcon build --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=1`
- to run the tests`colcon test --packages-select <package>`
- to see the test output `colcon test-result --test-result-base build/<package> --verbose`
#### license sidenote:
- ament requires license + copyrights to pass the tests.. TODO-> find way to disable this.
### creating tests
| client | library unittest | ros unittest | ros integrationtest|
| --- | ---- | --- |---|
| rclcpp| gtest | .. | .. |
| rclpy | unittest/pytest | ..| .. |


[gtest](https://google.github.io/googletest/quickstart-cmake.html) documentation & [test/ build example](https://github.com/SteveMacenski/slam_toolbox/blob/foxy-devel/CMakeLists.txt)
