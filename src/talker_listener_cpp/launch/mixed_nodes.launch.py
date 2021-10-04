"""Launch a talker and a listener in a component container."""

import launch
from launch_ros.actions import ComposableNodeContainer, Node
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    """Generate launch description with multiple components."""
    container = ComposableNodeContainer(
            name='my_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='talker_listener_cpp',
                    plugin='composition::Talker', # name as registered in CPP file
                    name='talker')
     
            ],
            output='screen',
    )

    node  = Node(package= "talker_listener_cpp", executable= "listener", name="listener")

    return launch.LaunchDescription([container, node])