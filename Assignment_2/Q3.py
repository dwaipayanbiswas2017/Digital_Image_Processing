# Calculate mean value of image
import cv2
import numpy as np

image = cv2.imread('resources/image-square.jpeg').astype(np.float32) / 255

res = image
res -= res.mean()

cv2.imshow('Result',res)
cv2.waitKey(0)
cv2.destroyAllWindows()