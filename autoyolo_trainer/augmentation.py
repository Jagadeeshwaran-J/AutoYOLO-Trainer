import albumentations as A

def get_augmentations():
    aug = A.Compose([
        A.RandomBrightnessContrast(p=0.4),
        A.HorizontalFlip(p=0.5),
        A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0.2, rotate_limit=30, p=0.5),
        A.Blur(blur_limit=3, p=0.2),
        A.MotionBlur(p=0.2),
        A.RandomGamma(p=0.3),
    ])
    return aug
