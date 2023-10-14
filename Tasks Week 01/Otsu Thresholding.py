import cv2
import numpy as np

image1=cv2.imread('OpenCV.png')
img=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)

#In Otsu Thresholding, a value of the threshold isn’t chosen but is determined automatically. 

#Syntax: cv2.threshold(source, thresholdValue, maxVal, thresholdingTechnique)

ret,thresh=cv2.threshold(img,120,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('Otsu Thresholding',thresh)

cv2.waitKey(0)
cv2.destroyAllWindows