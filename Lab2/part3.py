import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['image.cmap'] = 'gray'

img = cv2.imread('damaged_cameraman.bmp',0)
mask = cv2.imread('damage_mask.bmp',0)

def Gaussian(img):
	return cv2.GaussianBlur(img,(5,5),0)

def storepixels(img,mask):
	needed= np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
	for line in range(img.shape[0]):
		for pixel in range(img.shape[1]):
			if mask[line,pixel] != 255:
				needed[line,pixel] = img[line,pixel]
	return needed

def assign(img,need):
	for line in range(img.shape[0]):
		for pixel in range(img.shape[1]):
			if need[line,pixel] != 0:
				img[line,pixel] = need[line,pixel]

img1 = img.copy()
i = 0
while i<50:
	newImg = Gaussian(img1)
	need = storepixels(newImg,mask)
	assign(img1,need)
	i += 1

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(mask),plt.title('Mask')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img1),plt.title('Result')
plt.xticks([]), plt.yticks([])

plt.show()