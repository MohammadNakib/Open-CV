import cv2

videofootage=cv2.VideoCapture('10 Sec TVC.mp4')

if not videofootage.isOpened():
    print("Error! Couldn't open the video")
    exit()

fps=int(videofootage.get(cv2.CAP_PROP_FPS))

desired_second=2
frame_number=desired_second*fps

videofootage.set(cv2.CAP_PROP_POS_FRAMES,frame_number)
ret, frame = videofootage.read()

cv2.imshow('Captured Image',frame)

cv2.waitKey(0)
cv2.destroyAllWindows