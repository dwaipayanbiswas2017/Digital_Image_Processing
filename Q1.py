# Read and display image
import cv2

img = cv2.imread("TestRGB2.jpeg", 1)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()