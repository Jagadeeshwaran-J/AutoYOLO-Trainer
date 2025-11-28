from setuptools import setup, find_packages
from pathlib import Path

# Read README.md for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="autoyolo-trainer",
    version="0.0.3",
    author="Jagadeeshwaran",
    description="Auto YOLO Trainer with custom augmentations and model downloader",
    long_description=long_description,
    long_description_content_type="text/markdown",  # important for PyPI
    packages=find_packages(),
    install_requires=[
        "ultralytics",
        "albumentations",
        "opencv-python",
        "numpy",
        "pillow"
    ],
    python_requires=">=3.8",
)
