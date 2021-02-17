# Zooming of an image
import cv2
import numpy as np

image = cv2.imread('resources/image-square.jpeg')

height, width = image.shape[:2]
print("Original image size : ",height," ",width)

zoomed_img = cv2.resize(image, (int(height*1.5), int(width*1.5)))

cv2.imshow("Original ("+str(height)+", "+str(width)+")", image)
cv2.imshow("Zoomed ("+str(int(height*1.5))+", "+str(int(width*1.5))+")", zoomed_img)
cv2.waitKey()

cv2.destroyAllWindows()
