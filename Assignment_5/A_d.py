import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import *
# from scipy.misc import *
from skimage import color, data, restoration
# from scipy.signal import convolve2d as conv2

def main():
	image = cv2.imread("resources/noise.jpeg")

	psf = np.ones((5, 5)) / 25
	image = signal.conv2(image, psf, 'same')
	image += 0.1 * image.std() * np.random.standard_normal(image.shape)

	deconvolved = restoration.wiener(image, psf, 1, clip=False)

	plt.imshow(deconvolved, cmap='gray')
	plt.show()

if __name__ == "__main__":
	main()