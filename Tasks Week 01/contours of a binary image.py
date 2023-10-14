import cv2

# Read the image
image = cv2.imread("OpenCV. png")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary threshold
_, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw all the contours
cv2.drawContours(image, contours, -1, (0,255,0), 3)

# Display the image with contours
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
