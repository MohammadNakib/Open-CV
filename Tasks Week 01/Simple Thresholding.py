import cv2
import numpy as np

# Steps:(Nakib)
# 1. Coverting the image BGR to Gray
# 2. Use Thresholding techniques
image01=cv2.imread('HackerBoy.jpg')
img=cv2.cvtColor(image01,cv2.COLOR_BGR2GRAY)

#cv2.imshow('Gray Image',img)
#cv2.waitKey(0)

#Syntex : cv2.threshold(source,threshold value,maximum value, threshold technique)

ret,thresh1=cv2.threshold(img,20,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,20,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,20,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,20,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,20,255,cv2.THRESH_TOZERO_INV)
ret,thresh6=cv2.threshold(img,20,255,cv2.THRESH_MASK)
ret,thresh7=cv2.threshold(img,20,255,cv2.THRESH_TRIANGLE)
ret,thresh8=cv2.threshold(img,20,255,cv2.THRESH_OTSU)
cv2.imshow('Original Image',image01)

#Why ret is used in here? without ret the program is not working!!!

cv2.imshow('Threshold Binary',thresh1)
cv2.imshow('Threshold Binary Inverse',thresh2)
cv2.imshow('Threshold Truncated',thresh3)
cv2.imshow('Threshold to Zero',thresh4)
cv2.imshow('Threshold to Zero inverse',thresh5)
cv2.imshow('Threshold Mask',thresh6)
cv2.imshow('Threshold triangle',thresh7)
cv2.imshow('Threshold Otsu',thresh8)

cv2.waitKey(0)
cv2.destroyAllWindows()








