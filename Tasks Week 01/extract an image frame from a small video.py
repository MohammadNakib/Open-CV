import cv2

# Initialize video capture object
cap = cv2.VideoCapture('10 Seconds Countdown Timer.mp4')

# Check if the video capture object is initialized
if not cap.isOpened():
    print("Error: Couldn't open the video.")
    exit()

# Read a frame. You can loop through to read multiple frames
ret, frame = cap.read()

# Save the frame if it's successfully read
if ret:
    cv2.imwrite('extracted_frame.jpg', frame)

# Release the video capture object
cap.release()
