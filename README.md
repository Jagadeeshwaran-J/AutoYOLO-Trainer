# AutoYOLO Trainer

[![PyPI version](https://badge.fury.io/py/autoyolo-trainer.svg)](https://pypi.org/project/autoyolo-trainer/)

**AutoYOLO Trainer** is a Python package for automatically training YOLO models with custom augmentations and an integrated model downloader. It simplifies the training pipeline for object detection tasks.

---

## Features

- Train YOLO models easily with a single function call.
- Built-in custom augmentations for data enhancement.
- Download pre-trained YOLO models automatically.
- Fully compatible with Python ≥ 3.8.
- Works seamlessly with `ultralytics` YOLO framework.

---

## Installation

Install directly from PyPI:

```bash
pip install autoyolo-trainer
```

Or install from source:

```bash
git clone https://github.com/<your-github-username>/autoyolo-trainer.git
cd autoyolo-trainer
pip install .
```

---

## Project Structure

```
autoyolo-trainer/
│
├── autoyolo_trainer/
│   ├── __init__.py          # Package initializer
│   ├── training.py          # YOLO training logic
│   ├── model_downloader.py  # Download pre-trained YOLO models
│   ├── augmentation.py      # Custom image augmentations
│
├── README.md
├── LICENSE
├── setup.py
├── pyproject.toml
├── Inference.py
```

---

## Usage

```python
from autoyolo_trainer import train_yolo

# Path to your dataset YAML file
dataset = r"E:\datasets\my_data.yaml"

# Train YOLO model
train_yolo(dataset_yaml=dataset, epochs=100, imgsz=640)
```

- `dataset_yaml`: Path to your dataset configuration in YOLO format.
- `epochs`: Number of training epochs.
- `imgsz`: Input image size for the model.

---

## Requirements

- Python ≥ 3.8  
- ultralytics  
- albumentations  
- opencv-python  
- numpy  
- pillow  

All dependencies are automatically installed with pip.

---

## Uploading to PyPI

Follow these steps to publish your package to PyPI:

1. **Ensure your project has the required files**:  
   - `setup.py`  
   - `pyproject.toml`  
   - `README.md`  
   - `LICENSE`  

2. **Install build tools**:

```bash
pip install --upgrade setuptools wheel twine
```

3. **Build your package**:

```bash
python -m build
```

This will generate distribution files in the `dist/` folder: `.tar.gz` and `.whl`.

4. **Upload to PyPI**:

```bash
twine upload dist/*
```

- You will be prompted for your PyPI username and password.  
- To test first, use Test PyPI:

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

5. **Verify Installation**:

```bash
pip install autoyolo-trainer
```

---


## License

MIT License – see the [LICENSE](LICENSE) file for details.

---

## Contact

Created by **Jagadeeshwaran** – feel free to reach out for any questions or support.

