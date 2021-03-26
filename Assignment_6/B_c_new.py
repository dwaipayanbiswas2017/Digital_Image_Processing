import cv2
import skimage
from skimage.restoration import (denoise_wavelet,
estimate_sigma)
img = cv2.imread('resources/Gaussian-noise-added-Image.png', 0)
img = skimage.img_as_float(img)
sigma_est = estimate_sigma(img, average_sigmas=True)
# Denoising using Byes
img_byes = denoise_wavelet(img, method='BayesShrink',
mode='soft', wavelet_levels=3, wavelet='bior6.8',
rescale_sigma=True)
# Denoising using Visushrink
img_visushrink = denoise_wavelet(img, method='VisuShrink',
mode='soft', sigma=sigma_est/6, wavelet_levels=5,
wavelet='bior6.8', rescale_sigma=True)
cv2.imshow('Original image', img)
cv2.imshow('Denoise image Byes', img_byes)
cv2.imshow('Denoise image Visushrink', img_visushrink)
cv2.waitKey(0)
cv2.destroyAllWindows()