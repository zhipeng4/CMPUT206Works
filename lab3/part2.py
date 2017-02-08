import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['image.cmap'] = 'gray'

def nothing(x):
	pass
	
def th1(x):
	th2 = cv2.getTrackbarPos('Threshold2','image')
	edges = cv2.Canny(img,x,th2)
	cv2.imshow('image',edges)

def th2(x):
	th1 = cv2.getTrackbarPos('Threshold1','image')
	edges = cv2.Canny(img,th1,x)
	cv2.imshow('image',edges)
	
img = cv2.imread('ex2.jpg',0)
edges = cv2.Canny(img,100,200)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('Threshold1','image',0,400,th1)
cv2.createTrackbar('Threshold2','image',0,400,th2)

# create switch for ON/OFF functionality
cv2.createTrackbar('Switch','image',0,1,nothing)
cv2.imshow('image',edges)


while(1):
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

    # get current positions of four trackbars
#	th1 = cv2.getTrackbarPos('Threshold1','image')
#	th2 = cv2.getTrackbarPos('Threshold2','image')
	s = cv2.getTrackbarPos('Switch','image')

	if s == 0:
		edges = img
		cv2.imshow('image',edges)
#	else:
#		edges = cv2.Canny(img,th1,th2)
	

cv2.destroyAllWindows()