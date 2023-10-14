import cv2
import numpy as np

image01=cv2.imread('GeeksForGeeks.png')
gray=cv2.cvtColor(image01,cv2.COLOR_BGR2GRAY)

# modify the data type 
# setting to 32-bit floating point 

gray=np.float32(gray)

# Syntax: cv2.cornerHarris(src, dest, blockSize, kSize, freeParameter, borderType)
#Parameters: 
#src – Input Image (Single-channel, 8-bit or floating-point) 
#dest – Image to store the Harris detector responses. Size is same as source image 
#blockSize – Neighborhood size ( for each pixel value blockSize * blockSize neighbourhood is considered ) 
#ksize – Aperture parameter for the Sobel() operator 
#freeParameter – Harris detector free parameter 
#borderType – Pixel extrapolation method ( the extrapolation mode used returns the coordinate of the pixel corresponding to the specified extrapolated pixel )

HarrisImage=cv2.cornerHarris(gray,2,5,0.07)

# Results are marked through the dilated corners 
HarrisImage=cv2.dilate(HarrisImage,None)

# Reverting back to the original image, 
# with optimal threshold value 
image01[HarrisImage> 0.01*HarrisImage.max()]=[0,0,255]

cv2.imshow('Image with corners',image01)

cv2.waitKey()
cv2.destroyAllWindows

