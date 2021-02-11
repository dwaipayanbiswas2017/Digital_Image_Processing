# Implement basic gray level transformation for the Logarithmic
import cv2
import numpy as np

img = cv2.imread('resources/gray.jpg')

c = 255 / np.log(1 + np.max(img))
log_image = c * (np.log(img + 1))
log_image = np.array(log_image, dtype = np.uint8)

cv2.imshow("Original Image", img)
cv2.imshow("Log transformed Image", log_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
