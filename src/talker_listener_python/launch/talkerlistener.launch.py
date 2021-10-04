from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():
    remappings = [("/topic", "/test_remap/topic")]
    talker_node = Node(package='talker_listener_python',
                       executable="talker", name="talker", remappings=remappings)

    listener_node = Node(package='talker_listener_python',
                         executable="listener", name="listener", remappings=remappings)

    # ld = LaunchDescription()
    # ld.add_action(talker_node)
    # ld.add_action(listener_node)
    # return ld

    return LaunchDescription([talker_node, listener_node])
