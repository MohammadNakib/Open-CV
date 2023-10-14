import cv2 
import numpy as np 

image1=cv2.imread('Shapes.png')
gray=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)


#Syntax : cv2.goodFeaturesToTrack(gray_img, maxc, Q, minD)
corners=cv2.goodFeaturesToTrack(gray,100,0.1,10)

# convert corners values to integer 
# So that we will be able to draw circles on them 
corners=np.int0(corners)

# draw red color circles on all corners 
for i in corners:
    x,y=i.ravel() #  The ravel() method simplifies it to a flat array (e.g., [x, y])
    cv2.circle(image1,(x,y),3,(255,0,0),-1)

# cv2.circle(img, (x, y), 3, (255, 0, 0), -1):
# img: This is the image on which the circle will be drawn.
# (x, y): These are the coordinates of the center of the circle.
# 3: This is the radius of the circle.
# (255, 0, 0): This is the color of the circle in BGR format (Blue, Green, Red). Here, it specifies red color.
# -1: This is the thickness of the circle. A value of -1 indicates that the circle should be filled [1, 2].

cv2.imshow('Corners',image1)

cv2.waitKey(0)
cv2.destroyAllWindows