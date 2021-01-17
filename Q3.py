# Convert given color image into gray-scale image
import cv2

img = cv2.imread("TestRGB2.jpeg",cv2.IMREAD_COLOR)
cv2.imshow("Original",img)

greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GreyScale",greyscale)

cv2.waitKey(0)
cv2.destroyAllWindows()