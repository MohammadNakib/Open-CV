import cv2
import numpy as np

def detect_contours(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find contours
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    return image

def detect_corners(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect corners
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    corners = np.int0(corners)

    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(image, (x, y), 3, 255, -1)

    return image

if __name__ == "__main__":
    image_path = "OpenCV.png"
    
    contour_image = detect_contours(image_path)
    cv2.imshow('Contours', contour_image)
    
    corner_image = detect_corners(image_path)
    cv2.imshow('Corners', corner_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
