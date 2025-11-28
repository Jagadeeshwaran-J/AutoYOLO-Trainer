from ultralytics import YOLO

def download_model():
    model = YOLO("yolov8n.pt")   # auto-download from ultralytics hub
    return model
