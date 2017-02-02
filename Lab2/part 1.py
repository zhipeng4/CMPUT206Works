import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gray_image.png')

kernel = -np.ones((3,3),np.float32)
kernel[1][1] = 8;
dst = cv2.filter2D(img,-1,kernel)

added = cv2.add(img,dst)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(added),plt.title('Add_Result')
plt.xticks([]), plt.yticks([])
plt.show()