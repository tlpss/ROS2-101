#! /bin/bash

# build workspace
source /opt/ros/foxy/setup.bash
apt-get update 
# vcs import src < _repo_dependencies_file_.repos
rosdep install -r --from-paths . --ignore-src --rosdistro foxy -y # install all dependencies in the package.xml files
colcon build --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=1 # export build information for vscode 