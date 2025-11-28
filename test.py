from autoyolo_trainer import train_yolo

dataset = r"E:\datasets\my_data.yaml"
train_yolo(dataset_yaml=dataset, epochs=100, imgsz=640)

