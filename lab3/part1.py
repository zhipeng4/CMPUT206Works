import cv2
import numpy as np
from matplotlib import pyplot as plt

def sobelkernel(xy):
	if xy == "x":
		return np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
	elif xy == "y":
		return np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
		
def filter(img,kernel):
	return cv2.filter2D(img,-1,kernel)
	
def combine(channel1,channel2):
	result = np.zeros(channel1.shape)
	for i in range(channel1.shape[0]):
		for j in range(channel1.shape[1]):
			if (channel1[i][j] > 127) or (channel2[i][j] > 127):
				result[i][j] = 255
			else:
				result[i][j] = 0
	return result
	
def comAbs(channel1, channel2):
	return np.absolute(np.add(np.absolute(channel1),np.absolute(channel2)))

def main(img):
	imgh = imgv = imgc = img
	imgh = filter(imgh,sobelkernel("x"))
	imgv = filter(imgv,sobelkernel("y"))
	#imgc = combine(imgh,imgv)
	imgc = comAbs(imgh,imgv)
	
	plt.subplot(221),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(222),plt.imshow(imgh),plt.title('Horizontally filtered')
	plt.xticks([]), plt.yticks([])
	plt.subplot(223),plt.imshow(imgv),plt.title('Vertically filtered')
	plt.xticks([]), plt.yticks([])
	plt.subplot(224),plt.imshow(imgc),plt.title('Combined result')
	plt.xticks([]), plt.yticks([])
	plt.show()
	
plt.rcParams['image.cmap'] = 'gray'
img = cv2.imread("ex2.jpg",0)
main(img)