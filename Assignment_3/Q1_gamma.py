# Implement basic gray level transformation for Power-law(Gamma)
import cv2
import numpy as np

img = cv2.imread('resources/gray.jpg')

cv2.imshow("Original Image", img)

for gamma in [0.1, 0.5, 1.2, 1.8, 2.2]:
	gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
	cv2.imshow("Gamma "+str(gamma), gamma_corrected)

cv2.waitKey(0)
cv2.destroyAllWindows()