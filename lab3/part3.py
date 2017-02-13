import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

plt.rcParams['image.cmap'] = 'gray'

# Read the original image, get its standard deviation, and operate on its copy
oimg = cv2.imread('ex1.jpg',0)
img = oimg
img1 = cv2.GaussianBlur(img, (15,15), 0)
mean,std = cv2.meanStdDev(img)

drawing = False # True if mouse is pressed
ix, iy = -1, -1

# Expression of the callback function
def drawCircle(event, x, y, flags, param):
	global ix, iy, drawing, img, img1, std

	# When left mouse button is clicked, prepare to draw
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y

	# While mouse moving, keep drawing
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			draw(ix,iy,std,img,img1)

	# When the mouse button is released, complete the drawing
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		draw(ix,iy,std,img,img1)

	# After a draw, renew the prepared blurred image
	img1 = cv2.GaussianBlur(img, (15,15), 0)

# The calculation of the new pixel value
def newPixel(x,y,x0,y0,ro,img,blurImg):
	w = weight(x,y,x0,y0,ro)
	return (w*blurImg[y][x])+((1-w)*img[y][x])

def weight(x,y,x0,y0,ro):
	return cv2.exp(-((x-x0)**2 + (y-y0)**2)/(ro**2))

# Help function. Part of the edge finder that confirm the area of drawing
def edge(x,y,rad,img):
	xr,yr = len(img[0]),len(img)
	if x<rad:
		xs = 0
	else:
		xs = x-rad
	if y<rad:
		ys = 0
	else:
		ys = y-rad
	if x>(xr-rad):
		xl = xr
	else:
		xl = x+rad
	if y>(yr-rad):
		yl = yr
	else:
		yl = y+rad
	return xs,ys,xl,yl

# The drawing program. Including the other part of finding the edge of the area to be drawn
def draw(x0,y0,ro,img,blurImg,rad = 40):
	xs,ys,xl,yl = edge(x0,y0,rad,img)
	for i in range(ys,yl):
		for j in range(xs,xl):
			if radius(j-x0,i-y0)<=rad:
				img[i][j] = newPixel(j,i,x0,y0,ro,img,blurImg)

# Help function for edge finding
def radius(x,y):
	return (x**2 + y**2)**0.5

# Create a window and show the result
cv2.namedWindow('image')
cv2.setMouseCallback('image',drawCircle)
 
while(1):
	cv2.imshow('image',img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()