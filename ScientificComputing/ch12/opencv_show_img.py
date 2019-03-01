# -*- coding: utf-8 -*-
import cv2 as cv
import sys

try:
    filename = sys.argv[1]
except:
    filename = "lena.jpg"
img = cv.imread(filename)

img[:, :, 0] = 0
img[:, :, 1] = 0
cv.namedWindow("demo1")
cv.imshow("demo1", img)
cv.waitKey(0)
