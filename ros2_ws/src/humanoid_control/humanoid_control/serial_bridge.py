import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial


class SerialBridge(Node):
    def __init__(self):
        super().__init__('serial_bridge')

        self.port = '/dev/ttyUSB0'
        self.baudrate = 115200

        try:
            self.ser = serial.Serial(
                self.port,
                self.baudrate,
                timeout=1
            )

            self.get_logger().info(
                f"Connected to ESP32 on {self.port}"
            )

        except Exception as e:
            self.get_logger().error(
                f"Serial connection failed: {e}"
            )
            self.ser = None

        self.sub = self.create_subscription(
            String,
            'commands',
            self.command_callback,
            10
        )

    def command_callback(self, msg):
        cmd = msg.data.strip()

        if self.ser is not None:
            try:
                self.ser.write((cmd + '\n').encode())
                self.get_logger().info(f"Sent: {cmd}")
            except Exception as e:
                self.get_logger().error(f"Write failed: {e}")

    def destroy_node(self):
        if self.ser:
            self.ser.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SerialBridge()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
