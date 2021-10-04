import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.subscriber = self.create_subscription(
            String, "topic", self.listener_callback, 10
        )
        self.subscriber  # prevent unused warning.

    def listener_callback(self, msg: String):
        self.get_logger().info(f"received {msg}")


def main(args=None):
    rclpy.init(args=args)
    listener = Listener()
    rclpy.spin(listener)
