import rclpy
from rclpy.node import Node
import cv2
import numpy as np
import time
import os
from std_msgs.msg import String
from ament_index_python.packages import get_package_share_directory


class VisionNode(Node):
    def __init__(self):
        super().__init__('vision_node')

        self.pub = self.create_publisher(String, 'detections', 10)

        pkg_path = get_package_share_directory('humanoid_control')
        model_path = os.path.join(pkg_path, 'models', 'yolov8n.onnx')
        names_path = os.path.join(pkg_path, 'models', 'coco.names')

        self.net = cv2.dnn.readNetFromONNX(model_path)

        with open(names_path) as f:
            self.classes = f.read().strip().split("\n")

        # ================= CAMERA FIX (FINAL STABLE) =================
        self.cap = None

        for i in range(5):
            cap = cv2.VideoCapture(i)

            if cap.isOpened():
                for _ in range(5):  # retry reads (IMPORTANT)
                    ret, frame = cap.read()
                    if ret and frame is not None:
                        self.cap = cap
                        self.get_logger().info(f"Camera opened on index {i} ✅")
                        break

            if self.cap is not None:
                break

        if self.cap is None:
            self.get_logger().error("No working camera found ❌")
            return  # 🚨 STOP HERE (prevents crash)

        # Safe to use now
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        self.prev_time = time.time()
        self.timer = self.create_timer(0.05, self.process)

    def process(self):
        if self.cap is None:
            return

        ret, frame = self.cap.read()

        if not ret or frame is None:
            self.get_logger().warn("Frame not received ⚠️")
            return

        h, w, _ = frame.shape

        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (640, 640), swapRB=True)
        self.net.setInput(blob)

        outputs = self.net.forward()[0]
        outputs = np.squeeze(outputs).T

        best_person = None
        best_conf = 0

        for row in outputs:
            x, y, bw, bh = row[:4]
            scores = row[4:]
            class_id = np.argmax(scores)
            conf = scores[class_id]

            if class_id >= len(self.classes):
                continue  # safety

            if self.classes[class_id] == "person" and conf > 0.4:

                # scaling
                scale_x = w / 640
                scale_y = h / 640

                x = x * scale_x
                y = y * scale_y
                bw = bw * scale_x
                bh = bh * scale_y

                if conf > best_conf:
                    best_conf = conf
                    best_person = (x, y, bw, bh)

        msg = String()

        if best_person:
            x, y, bw, bh = best_person

            cx = int(x)
            area = int(bw * bh)

            msg.data = f"{cx},{w},{area},1"
            self.get_logger().info(f"cx={cx}, area={area}")

        else:
            msg.data = "0,0,0,0"

        self.pub.publish(msg)

    def destroy_node(self):
        if self.cap is not None:
            self.cap.release()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
