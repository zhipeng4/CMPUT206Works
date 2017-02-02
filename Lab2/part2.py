import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('noisy.jpg')

median = cv2.medianBlur(img,3)
blur = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(median),plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()