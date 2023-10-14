import cv2

# Capture video from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the camera
    ret, frame = cap.read()

    # Display the frame in a window named 'OpenCV Test'
    cv2.imshow('OpenCV Test', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
