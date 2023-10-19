#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import NavSatFix


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('GPS_subscriber')
        self.subscription = self.create_subscription(
            NavSatFix,
            '/fix',
            self.GPSCallback,
            10)
        self.subscription  # prevent unused variable warning

    def GPSCallback(self,msg):
        self.get_logger().info('latitude:%0.6f, longitude:%0.6f, altitude:%0.6f' % (msg.latitude, msg.latitude,msg.altitude))


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
