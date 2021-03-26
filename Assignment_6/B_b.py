# Reconstruct image by applying inverse wavelet transform.
import cv2
import pywt
import numpy as np
import matplotlib.pyplot as plt

def main():
	img = cv2.imread('resources/image-square.jpeg', 0)

	c = pywt.wavedec2(img, 'db1', level=3)
	imgr = pywt.waverec2(c, 'db1')
	imgr = np.uint8(imgr)

	arr, coeff_slices = pywt.coeffs_to_array(c)

	plt.figure(figsize=(10, 10))
	plt.imshow(arr, cmap=plt.cm.gray)
	plt.title('3 Level Decomposition with Debauchee')
	plt.show()

	cv2.imshow('Original Image', imgr)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()