#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from ee106f26.msg import EE106LabCustomNew

class Subscriber(Node):

    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            EE106LabCustomNew,
            'EE106lab_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, message):

        info = f"Number 1:{message.int_var1}, Number 2:{message.int_var2} Added: {message.int_var1 + message.int_var2} Time: {message.header.stamp.sec}.{message.header.stamp.nanosec}"

        self.get_logger().info(info)


def main(args=None):
    rclpy.init(args=args)

    subscriber = Subscriber()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()