# Shrinking of an image
import cv2
import numpy as np

image = cv2.imread('resources/image-square.jpeg')

height, width = image.shape[:2]
print("Original image size : ",height," ",width)

shrinked_img = cv2.resize(image, (int(height/2), int(width/2)))

cv2.imshow("Original ("+str(height)+", "+str(width)+")", image)
cv2.imshow("Shrinked ("+str(int(height/2))+", "+str(int(width/2))+")", shrinked_img)
cv2.waitKey()

cv2.destroyAllWindows()
