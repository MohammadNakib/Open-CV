import cv2
import numpy as np

image01=cv2.imread('HackerBoy.jpg')
grayimage=cv2.cvtColor(image01,cv2.COLOR_BGR2GRAY)

ret,threshimage=cv2.threshold(grayimage,120,255,cv2.THRESH_BINARY)
contours,finalimage=cv2.findContours(threshimage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image01, contours, -1, (0,0,255), 3)

cv2.imshow('Contours Detected Image',image01)

cv2.waitKey(0)
cv2.destroyAllWindows