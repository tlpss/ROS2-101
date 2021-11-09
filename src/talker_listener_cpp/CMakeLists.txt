cmake_minimum_required(VERSION 3.5)
project(talker_listener_cpp)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rclcpp_components REQUIRED)

# include include
include_directories(include)

### ADD EXECUTABLES ###
# add executables and declare dependencies
add_executable(listener src/listener.cpp)
ament_target_dependencies(
  listener
  rclcpp
  std_msgs
)

### ADD COMPONENT ###

# add component to library
add_library(talker_component SHARED
   src/talker_component.cpp)
# link component dependencies
ament_target_dependencies(
  talker_component
  rclcpp
  std_msgs
  rclcpp_components
)
# register component
rclcpp_components_register_nodes(talker_component "composition::Talker")


### INSTALL ###
# install executables to the lib to allow ros to find them
install(
  TARGETS
  listener
  DESTINATION lib/${PROJECT_NAME})

  install(TARGETS # components require additional target? TODO: figure out why...
  talker_component
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME})

# install launc files to allow ros to find them
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

# include library headers so that they are visible for other packages
target_include_directories(listener PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
