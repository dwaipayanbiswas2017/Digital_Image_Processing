# Resize given image
import cv2

img=cv2.imread("TestRGB2.jpeg", cv2.IMREAD_COLOR)
cv2.imshow("Original",img)

resize=cv2.resize(img,(250,250))
cv2.imshow("Resized",resize)

cv2.waitKey(0)
cv2.destroyAllWindows()