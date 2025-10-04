import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class OpenLoopController(Node):
    def __init__(self):
        super().__init__('tb_openLoop')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.start_time = time.time()
        self.duration = 10  # seconds
        self.velocity = 0.1  # meters per second

    def timer_callback(self):
        msg = Twist()
        elapsed = time.time() - self.start_time
        if elapsed < self.duration:
            msg.linear.x = self.velocity
        else:
            msg.linear.x = 0.0
            self.get_logger().info('Stopping robot.')
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = OpenLoopController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

