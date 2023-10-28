import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import String
from geometry_msgs.msg import PointStamped

import numpy as np
import math
class Joy_Node(Node):
	def __init__(self):
		super().__init__("gokart_cockpit")
		self.get_logger().info("Node Created")
		self.subscribe = self.create_subscription(Joy,"/joy",self.ctrl_callback,10)
		self.publisher = self.create_publisher(PointStamped,"/control_command",10)
		self.fb = 0
		self.rl = 0
		self.delay = 0.0
		self.axes = np.zeros(6)
		self.button = np.zeros(18)
		self.command = np.zeros(3)
		self.throttle_scale, self.steering_scale = 0.2/2, math.pi/2
	
	
	
	def ctrl_callback(self, data):
		self.axes = data.axes
		self.button = data.buttons
		self.publish_data()
	
	def publish_data(self):

		
	    # all racing cockpit joystick command
	    self.steering = self.axes[0]     # +:left, -:right [-1,1]
	    self.throttle = self.axes[1]+1   # [-1,1] --> [0,2] default:-1
	    self.brake    = self.axes[2]+1   # [-1,1] --> [0,2] default:-1
	    self.clutch   = self.axes[3]     # [-1,1]
	    if self.axes[4] > 0.0:
	    	self.panel_left = 1
	    	self.panel_right = 0
	    else:
	    	self.panel_left = 0
	    	self.panel_right = 1
		
	    if self.axes[5] > 0.0:
	    	self.panel_up = 1
	    	self.panel_down = 0
	    else:
	    	self.panel_up = 0
	    	self.panel_down = 1
	    
	    self.A, self.B, self.X, self.Y = self.button[:4]
	    self.shift_paddle_right = self.button[4]
	    self.shift_paddle_left = self.button[5]
	    self.RSB = self.button[8]
	    self.LSB = self.button[9]
	    self.xbox = self.button[10]
	    self.gearshift_left_f = self.button[12]
	    self.gearshift_middle_f = self.button[14]
	    self.gearshift_right_f = self.button[16]
	    self.gearshift_left_b = self.button[13]
	    self.gearshift_middle_b = self.button[15]
	    self.gearshift_right_b = self.button[17]
	    
	    if self.steering > 0.167:
	    	self.command[0] = 0.167
	    elif self.steering < -0.167:
	    	self.command[0] =-0.167
	    else:
	    	self.command[0] = self.steering

	    self.command[1] = self.throttle
	    self.command[2] = 0
	    if self.gearshift_left_f==1 or self.gearshift_middle_f==1 or self.gearshift_right_f==1:
	    	self.command[1] = 1 * self.command[1]
	    if self.gearshift_left_b==1 or self.gearshift_middle_b==1 or self.gearshift_right_b==1:
	    	self.command[1] = -1 * self.command[1]
	    self.publisher_joy()

	def publisher_joy(self):
		joy_command = PointStamped()
		#joy_command.header.stamp = rospy.Time.now()
		joy_command.header.frame_id = 'cockpit input'
		joy_command.point.x = float(self.command[1]/2)
		joy_command.point.y = float(self.command[0]/0.167)
		joy_command.point.z = 0.0
		self.publisher.publish(joy_command)
    
    
        	
	
def main(args=None):
	rclpy.init(args=args)
	node = Joy_Node()
	node.get_logger().info("Object created")
	rclpy.spin(node)
	rclpy.shutdown()
	
if __name__ == "__main__":
	main() 
