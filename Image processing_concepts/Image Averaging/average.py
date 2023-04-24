import numpy as np
import argparse as ap
import cv2
import glob
import warnings
import imutils
from math import cos, sin

image = cv2.imread("panda1.jpg")
t=image.flatten()
arr=[]
for i in range(576):
	for j in range(1024):
		arr.append([i,j])
arr = np.array(arr)
c,s = cos(45),sin(45)
m = [[c,-s],[s,c]]
f = arr.dot(np.array(m))
f = f.astype(int)
k = np.zeros((1200, 1200), dtype=np.uint32)
for i,j in zip(f,t):
	k[i[0],i[1]+600]=j
k = k.astype(np.uint8)
cv2.imshow("", k)
cv2.waitKey()
cv2.imwrite("avg_img.png", k)
