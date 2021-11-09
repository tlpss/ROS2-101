# get ROS2 rolling base container
FROM ros:foxy-ros-base-focal

# install CI tools
RUN apt-get update && apt-get install -y clang-format-10 && \ 
apt-get install -y python3-pip && \ 
rm -rf /var/lib/apt/lists/* && \
pip install pre-commit