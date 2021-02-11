# Implement of histogram equalization
import cv2
import numpy as np

img = cv2.imread('resources/gray.jpg', 0)

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))

cv2.imshow("Original Image", img)
cv2.imshow("Histogram equalized", equ)

cv2.waitKey(0)
cv2.destroyAllWindows()