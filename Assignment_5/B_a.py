# Implement 2-D convolution process on an image
import cv2
import numpy as np

def main():
	img = cv2.imread("resources/image-square.jpeg", 1)

	# Sharpen filter
	sharpen_kernel = np.array((
				[0, -1, 0],
				[-1, 5, -1],
				[0, -1, 0]), np.float32)

	output = cv2.filter2D(img, -1, sharpen_kernel)

	cv2.imshow("Original Image", img)
	cv2.imshow("Output Image", output)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()