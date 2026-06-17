import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TrackerNode(Node):
    def __init__(self):
        super().__init__('tracker_node')

        self.sub = self.create_subscription(
            String, 'detections', self.cb, 10)

        self.pub = self.create_publisher(String, 'commands', 10)

        # 🔥 TUNED VALUES
        self.target_area = 30000
        self.tolerance = 10000

        self.prev_cmd = "S"

    def cb(self, msg):
        cx, width, area, found = map(int, msg.data.split(','))

        if found == 0:
            self.send("S")
            return

        center = width // 2
        error_x = cx - center

        # ✅ DEAD ZONE (IMPORTANT)
        dead_zone = 60

        if abs(error_x) < dead_zone:
            direction = "C"
        elif error_x < 0:
            direction = "L"
        else:
            direction = "R"

        # DISTANCE CONTROL
        if abs(area - self.target_area) < self.tolerance:
            move = "S"
        elif area < self.target_area:
            move = "F"
        else:
            move = "B"

        # FINAL COMMAND
        if move == "S":
            cmd = "S"
        else:
            if direction == "L":
                cmd = "L"
            elif direction == "R":
                cmd = "R"
            else:
                cmd = move

        self.send(cmd)

    def send(self, cmd):
        if cmd != self.prev_cmd:
            msg = String()
            msg.data = cmd
            self.pub.publish(msg)
            self.get_logger().info(f"CMD: {cmd}")

        self.prev_cmd = cmd


def main(args=None):
    rclpy.init(args=args)
    node = TrackerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
