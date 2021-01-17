# Convert given color/gray-scale image into black & white image
import cv2
import numpy as np

img=cv2.imread("TestRGB2.jpeg",cv2.IMREAD_COLOR)

b,g,r=cv2.split(img)
zeroes=np.zeros(b.shape,np.uint8)

bluechannel=cv2.merge((b,zeroes,zeroes))
redchanel=cv2.merge((zeroes,zeroes,r))
green_channel=cv2.merge((zeroes,g,zeroes))

cv2.imshow("Original",img)
cv2.imshow("Blue Channel",bluechannel)
cv2.imshow("Green Channel",green_channel)
cv2.imshow("Red Channel",redchanel)

cv2.waitKey(0)
cv2.destroyAllWindows()