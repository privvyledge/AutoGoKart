import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import String
from geometry_msgs.msg import PointStamped

class Joy_Node(Node):
	def __init__(self):
		super().__init__("gokart_joystick")
		self.get_logger().info("Node Created")
		self.subscribe = self.create_subscription(Joy,"/joy",self.getControll,10)
		self.publisher = self.create_publisher(PointStamped,"/control_command",10)
		self.fb = 0
		self.rl = 0
		
	def getControll(self,msg):
		data = msg
		#white Joy
		self.fb =data.axes[1]
		self.rl = data.axes[3]
		#black Joy
		#self.fb =data.axes[4]
		#self.rl = data.axes[3]
		message = "Received Data:" + str(self.fb) + ":" + str(self.rl)
		self.get_logger().info(message)
		msg = PointStamped();
		msg.header.frame_id = "Joystick"
		msg.point.x = self.fb
		msg.point.y = self.rl
		msg.point.z = 0.0
		self.publisher.publish(msg)
	
def main(args=None):
	rclpy.init(args=args)
	node = Joy_Node()
	node.get_logger().info("Object created")
	rclpy.spin(node)
	rclpy.shutdown()
	
if __name__ == "__main__":
	main() 
