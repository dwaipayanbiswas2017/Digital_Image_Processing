# Implement basic gray level transformation for the Linear
import cv2
import numpy as np

img = cv2.imread('resources/gray.jpg')

out = 2.0 * img
out[out > 255] = 255
out = np.around(out)
out = out.astype(np.uint8)

cv2.imshow("Original Image", img)
cv2.imshow("Linear transformed", out)

cv2.waitKey(0)
cv2.destroyAllWindows()