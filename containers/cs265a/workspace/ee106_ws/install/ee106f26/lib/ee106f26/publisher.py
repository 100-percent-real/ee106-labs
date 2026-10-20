#!/usr/bin/env python3

import rclpy 
import random
from rclpy.node import Node

from ee106f26.msg import EE106LabCustomNew


class Publisher(Node):

    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(EE106LabCustomNew, 'EE106lab_topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        

    def timer_callback(self):
        message = EE106LabCustomNew()
        message.int_var1= random.randint(0,100)
        message.int_var2= random.randint(0,100)
        message.header.stamp = self.get_clock().now().to_msg()
        self.publisher_.publish(message)

        info = f"Number 1:{message.int_var1}, Number 2:{message.int_var2},  {message.header.stamp.sec}.{message.header.stamp.nanosec}"


        
        self.get_logger().info(info)
        


        


def main(args=None):
    rclpy.init(args=args)

    publisher = Publisher()

    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()