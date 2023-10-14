import cv2

# Initialize the video capture object
cap = cv2.VideoCapture('10 Seconds Countdown Timer.mp4')

# Check if the video capture object is initialized
if not cap.isOpened():
    print("Error: Couldn't open the video.")
    exit()

# Get the frames per second of the video
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Specify the desired second
desired_second = 9  # Change this to the desired second
frame_number = desired_second * fps

# Set the video capture object to the desired frame
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

# Read the frame
ret, frame = cap.read()

# Save the frame if it's successfully read
if ret:
    cv2.imwrite('extracted_frame_at_{}.jpg'.format(desired_second), frame)

# Release the video capture object
cap.release()
