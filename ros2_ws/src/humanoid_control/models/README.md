# Models Folder

This folder contains the AI model and class labels used by the Humanoid Robot.

## Required Files

### yolov8n.onnx
YOLOv8 Nano model exported in ONNX format for real-time human detection.

### coco.names
List of COCO dataset class labels used by the YOLO model.

## Notes

The model file is not included in this repository due to GitHub file size limitations.

To use this project:

1. Download the YOLOv8 Nano ONNX model.
2. Place `yolov8n.onnx` in this folder.
3. Place `coco.names` in this folder.

Expected structure:

models/
├── yolov8n.onnx
├── coco.names
└── README.md
