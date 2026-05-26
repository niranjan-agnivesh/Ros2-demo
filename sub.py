#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        self.subscription_ = self.create_subscription(
            String,'my_topic1',
            self.listener_callback,
            10
        )
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    my_subscriber=MySubscriber()
    rclpy.spin(my_subscriber)
    my_subscriber.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':    main()