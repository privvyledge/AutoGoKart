#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import rclpy
from sensor_msgs.msg import NavSatFix

def GPSCallback(msg):
    rclpy.get_logger().info("latitude:%0.6f, longitude:%0.6f,altitude:%0.6f", msg.latitude, msg.latitude,msg.altitude)    
def GPS_subscriber(args=None):
    # self.init_node('GPS_subscriber', anonymous=True)
    rclpy.init(args=args)
    node = rclpy.create_node('GPS_subscriber')
    self.create_subscription(NavSatFix, "/fix", GPSCallback)
    rospy.spin(node)
if __name__ == '__main__': 
    GPS_subscriber()
