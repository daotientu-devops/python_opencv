import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("images/image1.jpg")
# Loading the image
half = cv2.resize(image, (0, 0), fx = 0.1, fy= 0.1)
# One thing to keep in mind while using the cv2.resize() function is that the tuple passed for determining the size of the new image ((1050, 1610) in this case) follows the order (width, height) unlike as expected (height, width)
bigger = cv2.resize(image, (1050, 1610))
# Choice of Interpolation Method for Resizing
# cv2.INTER_AREA: This is used when we need to shrink an image (co rút image)
# cv2.INTER_CUBIC: This is slow but more efficient
# cv2.INTER_LINEAR: This is primarily used when zooming is required. This is the default interpolation technique in OpenCV
stretch_near = cv2.resize(image, (780, 540), interpolation=cv2.INTER_LINEAR)
Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [image, half, bigger, stretch_near]
count = 4
for i in range(count):
    plt.subplot(2, 2, i+1)
    plt.title(Titles[i])
    plt.imshow(images[i])
plt.show()