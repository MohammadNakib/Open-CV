import cv2
import numpy as np

# Load the image
image_path = 'OpenCV.png'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Contours Extraction
_, thresholded = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)  # Draw green contours

# Corners Detection
corners = cv2.goodFeaturesToTrack(gray_image, maxCorners=100, qualityLevel=0.01, minDistance=10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x, y), 3, (255, 0, 0), -1)  # Draw blue corners

# Display the result
cv2.imshow('Contours and Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
