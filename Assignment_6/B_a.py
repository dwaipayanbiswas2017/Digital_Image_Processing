# Apply wavelet transform at different level of decomposition
import cv2
import pywt
import matplotlib.pyplot as plt

def main():
	img = cv2.imread('resources/image-square.jpeg', 0)

	wavelet_type = 'haar'
	wavelet_level = 2

	c = pywt.wavedec2(img, wavelet_type, level=wavelet_level)
	cA2 = c[0]
	(cH1, cV1, cD1) = c[-1]
	(cH2, cV2, cD2) = c[-2]

	plt.figure(figsize=(10, 10))

	plt.subplot(2,2,1)
	plt.imshow(cA2, cmap=plt.cm.gray)
	plt.title('Approximate image at L: 2')

	plt.subplot(2,2,2)
	plt.imshow(cH1, cmap=plt.cm.gray)
	plt.title('Horizontal component at L: 1')

	plt.subplot(2,2,3)
	plt.imshow(cV1, cmap=plt.cm.gray)
	plt.title('Vertical component at L: 1')

	plt.subplot(2,2,4)
	plt.imshow(cD1, cmap=plt.cm.gray)
	plt.title('Diagonal component at L: 1')

	arr, coeff_slices = pywt.coeffs_to_array(c)

	plt.figure(figsize=(10, 10))
	plt.imshow(arr, cmap=plt.cm.gray)
	plt.title('2 Level decomposition')
	plt.show()

if __name__ == "__main__":
	main()