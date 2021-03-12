import cv2
# import matplotlib.pyplot as plt
import numpy as np
import random

def main():

	path = "resources/"
	imgpath =  path + "image-square.jpeg"
	img = cv2.imread(imgpath, 1)

	rows, columns, channels = img.shape

	p = 0.05
	output = np.zeros(img.shape, np.uint8)

	for i in range(rows):
		for j in range(columns):
			r = random.random()
			if r < p/2:
				output[i][j] = [0, 0, 0]
			elif r < p:
				output[i][j] = [255, 255, 255]
			else:
				output[i][j] = img[i][j]

	cv2.imwrite("resources/noise.jpeg", output)

	cv2.imshow("Original Image",img)
	cv2.imshow("Noisy Image",output)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()