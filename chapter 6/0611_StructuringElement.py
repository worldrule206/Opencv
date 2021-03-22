# 0611.py
"""
ref: https://gist.github.com/jsheedy/3913ab49d344fac4d02bcc887ba4277d
ref: http://felix.abecassis.me/2011/09/opencv-morphological-skeleton/
"""
import cv2
import numpy as np

#1
src   = cv2.imread('../data/T.jpg', cv2.IMREAD_GRAYSCALE)
# src   = cv2.imread('alphabet.bmp', cv2.IMREAD_GRAYSCALE)
# src = cv2.bitwise_not(src) # 반전.
skel_dst = np.zeros(src.shape, np.uint8)

shape1= cv2.MORPH_CROSS
shape2= cv2.MORPH_RECT

ret, A = cv2.threshold(src, 50, 255, cv2.THRESH_BINARY)
B = cv2.getStructuringElement(shape=shape1, ksize=(3,3)) # Kernel 생성

done = True
while done:   
    erode  = cv2.erode(A, B)
    # https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#gaeb1e0c1033e3f6b891a25d0511362aeb
    # opening = cv2.dilate(erode,B)
    opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, B)
    # https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f
    tmp  = cv2.subtract(erode, opening)
    tmp = cv2.absdiff(erode, opening)
    skel_dst = cv2.bitwise_or(skel_dst, tmp)
    A = erode.copy()
    done = cv2.countNonZero(A) != 0
    
cv2.imshow('opening',  opening)
cv2.imshow('tmp',  tmp)
cv2.imshow('src',  src)    
cv2.imshow('skel_dst',  skel_dst)
cv2.waitKey()
cv2.destroyAllWindows()
