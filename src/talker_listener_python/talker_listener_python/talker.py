import rclpy

from rclpy.node import Node
from std_msgs.msg import String

from talker_listener_python.fibonacci import Fibonacci
class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.publisher  = self.create_publisher(String, "topic", 10) # QoS == buffer size
        self.logger = self.get_logger()
        self.message_counter = 0
        self.fibonacci = Fibonacci()
        # create periodic timer every second 
        self.timer = self.create_timer(1,self.timer_callback) 


    def timer_callback(self) -> None:
        msg = String()
        fibonacci = self.fibonacci()
        msg.data = f" Hello World # {self.message_counter}, fibonacci = {fibonacci}"
        self.publisher.publish(msg)
        self.logger.info(f"publishing -  {msg.data}")
        self.message_counter += 1


def main(args= None):
    # start ros communication with client lib
    rclpy.init(args = args) 
    # start up the node
    talker = Talker()
    rclpy.spin(talker)
