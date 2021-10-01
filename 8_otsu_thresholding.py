import cv2
import numpy as np
image1 = cv2.imread('images/parrot.jpg')
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# applying Otsu thresholding
# as an extra flag in binary
# thresholding
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Otsu Threshold', thresh1)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()