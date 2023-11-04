import time
import serial

import rclpy
from rclpy.node import Node

# from std_msgs.msg import Float64
from sensor_msgs.msg import Joy

class ATJoyNode(Node):
	def __init__(self):
		super().__init__('atjoy_node')
		# self.steering_publisher_ = self.create_publisher(Float64, 'steering', 1)
		# self.throttle_publisher_ = self.create_publisher(Float64, 'throttle', 1)
		self.command_publisher_ = self.create_publisher(Joy, 'joy/at9s', 1)
		timer_period = 0.05  # seconds
		self.timer = self.create_timer(timer_period, self.timer_callback)
		
		self.ser = serial.Serial( port = '/dev/ttyACM0',baudrate=115200)  # series port of arduino
		self.ser.isOpen()  # open port receiver
		self.buttons = [0,0,0,0,0,0]
		self.push = [0.0,0.0,0.0,0.0]
		
		self.declare_parameter('sensitivity', 0.8)
		
	def isint(self,num):
		try:
			for k in num:
				int(k)
			return True
		except ValueError:
			return False
		
	def timer_callback(self):
		# sensitivities param
		sen_gain = self.get_parameter('sensitivity').value
		
		# read arduino
		out = ''
		while self.ser.inWaiting() > 0:
			out += str(self.ser.readline(),encoding='utf-8')
			
		if out != '':
			spl = out.split(",")
			
			# at beginning, arduino send some cache string data
			if self.isint(spl):
				# The first two are for axes
				# mapping from [2000,1000] to [-1,1]
				data_length = len(spl)
				try:
					self.push[0] = -1.0+2.0*(float(spl[0])-1000.0)/(2000.0-1000.0) # throttle
					self.push[0] = sen_gain*self.push[0]
				except Exception: # if there is no data received for long time
					self.get_logger().info('No throttle commands /n')
					self.push[0] = 0.0
				try:
					self.push[1] = -1.0+2.0*(float(spl[1])-1000.0)/(2000.0-1000.0) # steering
				except Exception:
					self.get_logger().info('No steering commands /n')
					self.push[1] = 0.0
				try:
					self.push[2] = 1.0-2.0*(float(spl[2])-1000.0)/(2000.0-1000.0) # Rudder
				except Exception:
					self.get_logger().info('No rudder commands /n')
					self.push[2] = 0.0
				try:
					self.push[3] = -1.0+2.0*(float(spl[3])-1000.0)/(2000.0-1000.0) # Elevator
				except Exception:
					self.get_logger().info('No elevator commands /n')
					self.push[3] = 0.0
					
				

				
				# if the port does not have data for long time, 
				# arduino does not send any data
				if data_length> 4:
					for i in range(2,data_length):
						# For buttons: back: 2000, forward: 1000;
						if int(spl[i])<1500:
							self.buttons[i-4]=1;
						else:
							self.buttons[i-4]=0;
					 
				# Publisher
				msg  = Joy()
				msg.header.stamp = self.get_clock().now().to_msg()
				msg.header.frame_id = 'at9s_joy'
				msg.axes = self.push
				msg.buttons = self.buttons
				self.command_publisher_.publish(msg)
				
				# printing for debug purpose
				self.get_logger().info('throttle: "%f", steering: "%f" /n' % (msg.axes[0], msg.axes[1]))
				self.get_logger().info('sWA: "%d", sWD: "%d" /n' % (msg.buttons[0],msg.buttons[3]))


def main(args=None):
    rclpy.init(args=args)

    atjoy_node = ATJoyNode()

    rclpy.spin(atjoy_node)

    atjoy_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
