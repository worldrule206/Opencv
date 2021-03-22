# 0609.py
import cv2
import numpy as np

src   = cv2.imread('../data/morphology.jpg', cv2.IMREAD_GRAYSCALE)

kernel= cv2.getStructuringElement(shape=cv2.MORPH_RECT , ksize=(3,3))
# https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html#gac342a1bb6eabf6f55c803b09268e36dc
# kenel filter 생성.

dilate = cv2.dilate(src,kernel,iterations = 5)
erode = cv2.erode(src,kernel,iterations = 5)

erode2= cv2.erode(dilate,kernel,iterations = 7)
dilate2= cv2.dilate(erode2,kernel,iterations = 2)

cv2.imshow('src',       src)
cv2.imshow('erode',     erode)
cv2.imshow('dilate',    dilate)
cv2.imshow('erode2',    erode2) # 노이즈 제거(Holefilled)
cv2.imshow('dilate2',   dilate2) # 노이즈 제거(Holefilled)

cv2.waitKey()
cv2.destroyAllWindows()
