# services/object_detection_service.py

from ultralytics import YOLO
import cv2

# Load the upgraded YOLOv8 medium model
model = YOLO("yolov8m.pt")  # Previously yolov8n.pt

def detect_object(image_path):
    results = model(image_path)

    objects = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])

            objects.append({
                "class": class_name,
                "confidence": round(confidence, 2)
            })

    return objects
