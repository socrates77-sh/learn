import cv2
import numpy as np

img = cv2.imread('fruits.jpg')

# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

height, width = img.shape[:2]
res = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)

cv2.imshow('image', res)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
