import cv2
import numpy as np

# Adaptive thresholding is the method where the threshold value is calculated for smaller regions.
# This leads to different threshold values for different regions with respect 
# to the change in lighting. We use cv2.adaptiveThreshold for this.

image1=cv2.imread('OpenCV.png')
img=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray Image',img)

# Syntax: cv2.adaptiveThreshold(source, maxVal, adaptiveMethod, thresholdType, blocksize, constant)

image_01=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,199,5)
image_02=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,5)

cv2.imshow('Mean',image_01)
cv2.imshow('Gaussian',image_02)

cv2.waitKey(0)
cv2.destroyAllWindows()