# 0712.py
import cv2
import numpy as np
# https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html#gada75b59bdaaca411ed6fee10085eb784 documentation

#1
src = cv2.imread('../data/lena.jpg')
print('src.shape=', src.shape)

width, height, channel = src.shape
print(width, height, channel)

down2 = cv2.pyrDown(src)
down4 = cv2.pyrDown(down2)
print('down2.shape=', down2.shape)
print('down2.shape=', down4.shape)

#2
up2 = cv2.pyrUp(src)
up4 = cv2.pyrUp(up2)
print('up2.shape=', up2.shape)
print('up4.shape=', up4.shape)

cv2.imshow('src', src)
cv2.imshow('down2',down2)
##cv2.imshow('down4',down4)
# cv2.imshow('up2',up2)
##cv2.imshow('up4',up4)
cv2.waitKey()
cv2.destroyAllWindows()
