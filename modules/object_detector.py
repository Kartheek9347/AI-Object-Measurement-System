from ultralytics import YOLO

# Load YOLO model (auto-downloads first time)
model = YOLO("yolov8n.pt")


def detect_objects(image_path):

    results = model(image_path)

    detections = []

    for r in results:
        for box in r.boxes:

            x1, y1, x2, y2 = box.xyxy[0].tolist()
            cls = int(box.cls[0])

            detections.append({
                "bbox": [int(x1), int(y1), int(x2), int(y2)],
                "class": model.names[cls]
            })

    return detections