import cv2
import numpy as np

def load_image(path):
    """
    Load an image from a file path.

    Args:
        path (str): Path to the image file.

    Returns:
        numpy.ndarray: Loaded BGR image.
    """
    return cv2.imread(path)

def to_gray(img, contrast=1.0, brightness=0):
    """
    Convert a BGR image to grayscale with optional contrast and brightness adjustment.

    Args:
        img (numpy.ndarray): Input BGR image.
        contrast (float): Contrast multiplier (default 1.0).
        brightness (int): Brightness offset (default 0).

    Returns:
        numpy.ndarray: Grayscale image with adjusted contrast and brightness.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.convertScaleAbs(gray, alpha=contrast, beta=brightness)

def to_sepia(img, contrast=1.0, brightness=0):
    """
    Apply a sepia filter to a BGR image with optional contrast and brightness adjustment.

    Args:
        img (numpy.ndarray): Input BGR image.
        contrast (float): Contrast multiplier (default 1.0).
        brightness (int): Brightness offset (default 0).

    Returns:
        numpy.ndarray: Sepia-toned image.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sepia = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    sepia_img = cv2.transform(sepia, kernel)
    sepia_img = np.clip(sepia_img, 0, 255)
    return cv2.convertScaleAbs(sepia_img, alpha=contrast, beta=brightness)

def invert_image(img, contrast=1.0, brightness=0):
    """
    Invert the colors of a BGR image with optional contrast and brightness adjustment.

    Args:
        img (numpy.ndarray): Input BGR image.
        contrast (float): Contrast multiplier (default 1.0).
        brightness (int): Brightness offset (default 0).

    Returns:
        numpy.ndarray: Color-inverted image.
    """
    inverted = cv2.bitwise_not(img)
    return cv2.convertScaleAbs(inverted, alpha=contrast, beta=brightness)

def sketch_image(img, contrast=1.0, brightness=0):
    """
    Create a pencil sketch effect from a BGR image.

    Args:
        img (numpy.ndarray): Input BGR image.
        contrast (float): Contrast multiplier (default 1.0).
        brightness (int): Brightness offset (default 0).

    Returns:
        numpy.ndarray: Grayscale sketch image.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    return cv2.convertScaleAbs(sketch, alpha=contrast, beta=brightness)

def threshold_image(img, contrast=1.0, brightness=0):
    """
    Convert a BGR image to a binary black-and-white image using fixed thresholding.

    Args:
        img (numpy.ndarray): Input BGR image.
        contrast (float): Contrast multiplier (default 1.0).
        brightness (int): Brightness offset (default 0).

    Returns:
        numpy.ndarray: Thresholded binary image.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return cv2.convertScaleAbs(threshed, alpha=contrast, beta=brightness)
