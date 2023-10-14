import cv2
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert the frame to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define blue color range in HSV
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])

    # Create mask to extract blue parts of the image
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)

    # Bitwise-AND mask and original frame to get blue components
    blue_result = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Display the result
    cv2.imshow('Detected Blue Objects', blue_result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
