import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import String
from geometry_msgs.msg import PointStamped
from ackermann_msgs.msg import AckermannDriveStamped
import serial
import time


class Command_Node(Node):
    def __init__(self):
        super().__init__("gokart_command")
        self.get_logger().info("Node Created-for serial")

        try:
            self.ser = serial.Serial("/dev/micro/pico", 115200, timeout=2)
            if self.ser.isOpen():
                self.get_logger().info("\033[32mSBW Serial port opened successfully...\033[0m")
            else:
                self.ser.open()
                self.get_logger().info("\033[32mSBW Serial port opened successfully...\033[0m")
            self.ser.write(f"target_mode=auto".encode("utf-8"))
            self.ser.flush()
            time.sleep(1.0)
            self.get_logger().info("\033[32mSet target mode to auto...\033[0m")
        except Exception as e:
            print(e)
            self.get_logger().info("\033[31mSerial port opening failure\033[0m")
            exit(0)

        self.subscribe = self.create_subscription(AckermannDriveStamped, "/ackermann_cmd", self.getControl, 10)
        self.sbw_publisher = self.create_publisher(PointStamped, "/sbw_control", 10)

        timer_period = 0.0001  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def map(self, input):
        value = float(input + 1) / 2
        return -90 + (value * 180)

    def getControl(self, msg):
        data = msg
        msg = PointStamped()
        msg.header.frame_id = "sbw_input"
        msg.point.x = data.drive.steering_angle
        msg.point.y = 0.0
        msg.point.z = 0.0
        self.sbw_publisher.publish(msg)
        self.serial_communication(data.drive.steering_angle)

    def serial_communication(self, msg):
        self.ser.write(f"tire={msg}".encode("utf-8"))
        self.ser.flush()
        # self.get_logger().info(f'Writing tire={msg} to microcontroller')

    def timer_callback(self):
        # get SBW feedback from the microcontroller. todo: refactor
        # See (https://github.com/pyserial/pyserial/issues/216#issuecomment-369414522)
        # for a more efficient implementtation
        '''method 1'''
        try:
            read_val = self.ser.readline()  # or read
            if read_val is not '':
                self.get_logger().info(f"{str(read_val, encoding='utf-8')}")
        except (serial.SerialException, Exception) as e:
            self.get_logger().info(f'No SBW Feedback data. {e}')
            return

        '''method 2'''
        # while self.ser.inWaiting() > 0:
        #     spl = self.ser.readline().strip()
        #
        # try:
        #     if len(spl) > 0:
        #         data_length = len(spl)
        #
        #         try:
        #             self.get_logger().info(f"{str(spl, encoding='utf-8')}")
        #         except Exception:
        #             self.get_logger().info(f'No SBW Feedback data')
        # except UnboundLocalError as e:
        #     self.get_logger().info(f'No SBW Feedback data')
            

def main(args=None):
    rclpy.init(args=args)
    node = Command_Node()
    node.get_logger().info("Object created")
    try:
        rclpy.spin(node)
    except Exception as e: # (KeyboardInterrupt, serial.serialutil.SerialException)
        node.get_logger().info(f"{e}. Shutting down...")
        node.ser.close()
        node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
