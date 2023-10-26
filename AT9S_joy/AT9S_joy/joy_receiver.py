import time
import serial

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class JoyPublisher(Node):

    def __init__(self):
        super().__init__('joy_publisher')
        self.steering_publisher_ = self.create_publisher(String, 'steering', 1)
        self.throttle_publisher_ = self.create_publisher(String, 'throttle', 1)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        
        self.ser = serial.Serial( port = '/dev/ttyACM0',baudrate=115200)  # series port of arduino
		self.ser.isOpen()  # open port receiver

    def timer_callback(self):
		out = ''
		while ser.inWaiting() > 0:
			out += str(ser.readline(),encoding='utf-8')
		
		
		if out != '':
			spl = out.split(",")
					
			# Publisher
			msg_thro  = String()
			msg_steer = String()
			msg_thro.data = spl[0]
			msg_steer.data = spl[1]
			self.throttle_publisher_.publish(msg_thro)
			self.steering_publisher_.publish(msg_steer)
			
			self.get_logger().info('throttle: "%d"' % msg_thro.data, ', steering: "%d" \n')


def main(args=None):
    rclpy.init(args=args)

    joy_publisher = JoyPublisher()

    rclpy.spin(joy_publisher)

    joy_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
