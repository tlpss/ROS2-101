#!/bin/shell
source /opt/ros/foxy/setup.bash
colcon build --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=1 --symlink-install  # symlink to make python scripts changeable & compile commands export for intellisense
source install/setup.bash