import time
import serial

import rclpy
from rclpy.node import Node

# from std_msgs.msg import Float64
from geometry_msgs.msg import PointStamped

class ATJoyNode(Node):
	def __init__(self):
		super().__init__('atjoy_node')
		# self.steering_publisher_ = self.create_publisher(Float64, 'steering', 1)
		# self.throttle_publisher_ = self.create_publisher(Float64, 'throttle', 1)
		self.command_publisher_ = self.create_publisher(PointStamped, 'control_command', 1)
		timer_period = 0.05  # seconds
		self.timer = self.create_timer(timer_period, self.timer_callback)
		
		self.ser = serial.Serial( port = '/dev/ttyACM0',baudrate=115200)  # series port of arduino
		self.ser.isOpen()  # open port receiver
		
	def isint(self,num):
		try:
			for k in num:
				int(k)
			return True
		except ValueError:
			return False
		
	def timer_callback(self):
		out = ''
		while self.ser.inWaiting() > 0:
			out += str(self.ser.readline(),encoding='utf-8')
			
		if out != '':
			spl = out.split(",")
			
			# at beginning, arduino send some cache string data
			if self.isint(spl):
				# mapping from [2000,1000] to [-1,1]
				spl[0] = 1-2*(float(spl[0])-1000)/(2000-1000)	
				spl[1] = 1-2*(float(spl[1])-1000)/(2000-1000)	
			
				# Publisher
				msg  = PointStamped()
				msg.header.stamp = self.get_clock().now().to_msg()
				msg.header.frame_id = 'at9s_joy'
				msg.point.x = float(spl[0])
				msg.point.y = float(spl[1])
				msg.point.z = 0.0  # for future use
				self.command_publisher_.publish(msg)
				
				# printing for debug purpose
				self.get_logger().info('throttle: "%f, steering: "%f"' % (msg.point.x, msg.point.y))


def main(args=None):
    rclpy.init(args=args)

    atjoy_node = ATJoyNode()

    rclpy.spin(atjoy_node)

    atjoy_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
