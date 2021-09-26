"""
Python program to demonstrate erosion and dilation of images
"""
import cv2
import numpy as np
# Reading the input image
img = cv2.imread("images/playboy.jpg")
# Talking a matrix of size 5 as the kernel
kernel = np.ones((5, 5), np.uint8)
"""
The first parameter is the original image, kernel is the matrix with image is
convolved and third parameter is the number of iterations, which will determine 
how much you want to erode/dilate a give image
"""
# Làm mòn
img_erosion = cv2.erode(img, kernel, iterations=2)
# Giãn nở
img_dilation = cv2.dilate(img, kernel, iterations=2)
cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()