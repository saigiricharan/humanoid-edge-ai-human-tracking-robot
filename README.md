# 🤖 Humanoid Robot Using Edge AI for Real-Time Human Detection and Tracking

Humanoid-inspired autonomous robot using Edge AI, ROS2, Raspberry Pi, ESP32, and YOLOv8 for real-time human detection and tracking.

[![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)](https://docs.ros.org/en/humble/)
[![Python](https://img.shields.io/badge/Python-3.10-yellow)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)](https://opencv.org/)
[![ESP32](https://img.shields.io/badge/ESP32-Embedded-red)](https://www.espressif.com/)
[![Raspberry Pi](https://img.shields.io/badge/RaspberryPi-4-success)](https://www.raspberrypi.com/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-ONNX-orange)](https://github.com/ultralytics/ultralytics)

## 📑 Table of Contents

- [Overview](#-overview)
- [Demo](#-demo)
- [System Architecture](#️-system-architecture)
- [Hardware Components](#️-hardware-components)
- [Software Stack](#-software-stack)
- [Setup & Run](#-setup--run)
- [Working Principle](#-working-principle)
- [Results](#-results)
- [Key Achievements](#-key-achievements)
- [Future Enhancements](#-future-enhancements)
- [SDG Alignment](#-sustainable-development-goals-sdgs)
- [Authors](#-authors)

---

## 📌 Overview

This project presents a humanoid-inspired autonomous robot capable of detecting and tracking a person in real time using Edge AI. It combines computer vision, embedded systems, and robotics into a robot that autonomously follows a human target while maintaining a safe distance.

A Raspberry Pi 4 handles vision processing, an ESP32 handles motor control, a YOLOv8 ONNX model performs real-time human detection through a USB camera, and ROS2 Humble provides modular communication between components.

## 📷 Demo

<p align="center">
  <img src="images/robot_front.jpg.jpeg" width="45%" alt="Robot Prototype">
  <img src="images/detection_output.png.jpeg" width="45%" alt="Human Detection Output">
</p>
<p align="center"><i>Left: physical prototype · Right: live YOLOv8 detection output</i></p>

## 🏗️ System Architecture

```mermaid
flowchart LR
    A[USB Camera] --> B[Vision Node<br/>YOLOv8 ONNX]
    B --> C[Tracker Node]
    C --> D[Serial Bridge]
    D --> E[ESP32]
    E --> F[L298N Motor Drivers]
    F --> G[4x DC Motors]
```

The Raspberry Pi runs the vision and tracking nodes under ROS2; tracking decisions are sent over serial to the ESP32, which drives the motors directly.

## ⚙️ Hardware Components

| Component | Purpose |
|---|---|
| Raspberry Pi 4 | Edge AI processing |
| ESP32 | Motor controller |
| USB Camera | Human detection input |
| L298N Motor Drivers | Motor control |
| DC Motors (x4) | Locomotion |
| Battery Pack | Power supply |

## 💻 Software Stack

- Ubuntu 22.04
- ROS2 Humble
- Python 3.10
- OpenCV
- YOLOv8 (ONNX runtime)
- NumPy
- PySerial

## 🚀 Setup & Run

> ⚠️ Adjust package/launch names below to match your actual `ros2_ws` structure.

**1. Clone the repo**
```bash
git clone https://github.com/saigiricharan/humanoid-edge-ai-human-tracking-robot.git
cd humanoid-edge-ai-human-tracking-robot
```

**2. Set up the Raspberry Pi side (Python + ROS2)**
```bash
pip install -r requirements.txt

# Build the ROS2 workspace
cd ros2_ws
colcon build
source install/setup.bash
```

**3. Flash the ESP32 firmware**
```bash
# Using PlatformIO (or open in Arduino IDE and upload)
cd ../esp32
pio run --target upload
```

**4. Launch the system**
```bash
cd ../ros2_ws
ros2 launch <your_package_name> tracking.launch.py
```

The robot should power on, the camera feed will start processing through YOLOv8, and detected tracking commands will stream to the ESP32 over serial.

## 🔄 Working Principle

1. USB camera captures live video.
2. YOLOv8 ONNX detects a person in frame.
3. Bounding box center and area are extracted.
4. Tracker node computes the required movement.
5. Movement commands are sent to the ESP32 over serial.
6. ESP32 drives the motors accordingly.
7. Robot follows the target autonomously while keeping a safe distance.

## 📊 Results

- Successful real-time human detection
- Autonomous human tracking
- Stable Raspberry Pi ↔ ESP32 communication
- Smooth navigation
- Safe stopping mechanism

## 🏆 Key Achievements

- Built a complete ROS2-based autonomous tracking robot end to end
- Integrated Raspberry Pi and ESP32 via serial communication
- Implemented real-time human detection with YOLOv8 ONNX
- Demonstrated autonomous human-following behavior using Edge AI

## 🔮 Future Enhancements

- Voice control
- AI chatbot integration
- PID-based smooth tracking
- Obstacle avoidance
- Multi-person tracking
- SLAM navigation

## 🌍 Sustainable Development Goals (SDGs)

| SDG | Relevance |
|---|---|
| **SDG 3** – Good Health and Well-being | Assistive robotic systems for elderly and disabled individuals |
| **SDG 9** – Industry, Innovation and Infrastructure | Promotes innovation through Edge AI and robotics |
| **SDG 11** – Sustainable Cities and Communities | Supports smart surveillance and intelligent automation |

## 👨‍💻 Authors

- **S. Sai Giri Charan** — Electronics and Communication Engineering, Dayananda Sagar University
- **Rohan Krishnan Susarla** — Electronics and Communication Engineering, Dayananda Sagar University
