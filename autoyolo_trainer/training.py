from ultralytics import YOLO


def train_yolo(dataset_yaml, epochs=100, imgsz=640, model_name="yolo11l.pt", batch=8):
    """
    Auto-train YOLO model using simple built-in Ultralytics augmentations.

    Args:
        dataset_yaml (str): Path to dataset YAML
        epochs (int): Number of epochs
        imgsz (int): Image size
        model_name (str): base model to download automatically
        batch (int): batch size
    """

    print(f"🔄 Downloading base model {model_name} if not exists...")
    model = YOLO(model_name)  # Auto-downloads if not available

    print("🚀 Starting training...")
    results = model.train(
        data=dataset_yaml,
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,

        # Optimizer
        optimizer="AdamW",
        lr0=0.001,
        lrf=0.01,
        weight_decay=0.0002,
        warmup_epochs=5,

        # Built-in augmentations
        degrees=0.0,
        translate=0.1,
        scale=0.6,
        shear=0.0,
        perspective=0.0,
        flipud=0.0,
        fliplr=0.5,
        hsv_h=0.015, hsv_s=0.7, hsv_v=0.4,
        mosaic=1.0,
        mixup=0.2,

        # CPU workers
        workers=8,

        # Logging / saving
        project="autoyolo_training",
        name="run",
        exist_ok=True,
        save=True,
        val=True,
        verbose=True
    )

    print("🎉 Training Completed!")
    return results
