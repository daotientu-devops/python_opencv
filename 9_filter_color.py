import cv2
import numpy as np
img = cv2.imread('images/parrot.jpg')
# convert the bgr color space of image to hsv color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# threshold of blue in hsv space
lower_blue = np.array([60, 35, 140])
upper_blue = np.array([180, 255, 255])
# preparing the mask to overlay
mask = cv2.inRange(hsv, lower_blue, upper_blue)
# The black region in the mask has the value of 0,
# so when multiplied with original image removes all non-blue regions
result = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey(0)