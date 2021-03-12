# Use 3×3 Mask for low pass filter and high pass filter
import cv2
import numpy as np

def main():
	img = cv2.imread("resources/image-square.jpeg", 1)

	# Low pass filter
	low_pass_kernel = np.array((
		[1, 2, 1],
		[2, 4, 2],
		[1, 2, 1]
	), np.float32)/16

	low_pass_output = cv2.filter2D(img, -1, low_pass_kernel)

	# High pass filter
	high_pass_kernel = np.array((
		[-1, -1, -1],
		[-1, 8, -1],
		[-1, -1, -1]
	), np.float32)

	high_pass_output = cv2.filter2D(img, -1, high_pass_kernel)

	cv2.imshow("Original",img)
	cv2.imshow("Low Pass filter",low_pass_output)
	cv2.imshow("High Pass filter",high_pass_output)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()