cmake_minimum_required(VERSION 3.5)
project(empty_cpp)

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

add_executable(empty_cpp_node src/empty_cpp_node.cpp) # create an executable (that can be called with ros2 run)
target_include_directories(empty_cpp_node PUBLIC # make the include directory linked to the executable publically available (.h file)
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)

ament_target_dependencies( # link dependencies for the executable
  empty_cpp_node
  "rclcpp"
)

install(TARGETS empty_cpp_node # install the headers/executables
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  find_package(ament_cmake_gtest REQUIRED)

  # the following line skips the linter which checks for copyrights in the ament_lint_common dependencies
  # set(ament_cmake_copyright_FOUND TRUE)
  ## add tests
  include_directories(test)
  ament_add_gtest(dummy_test test/dummy_test.cpp)
  # add dependencies if required
  #ament_target_dependencies(dummy_test <dummy_dependencies>)

  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
