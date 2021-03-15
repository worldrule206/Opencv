# 0418.py: OpenCV-Python Tutorials 참조
# 이미지 합성.
import cv2
import numpy as np

src1 = cv2.imread('../data/lena.jpg')
src2 = cv2.imread('../data/opencv_logo.png')

#1
rows, cols, channels = src2.shape
print(rows)
print(cols)
print(channels)
roi = src1[0:rows, 0:cols]
# 레나이미지의 로고의 영역 row값, col값으로 roi로 지정.
#
#2
gray = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 160, 250, cv2.THRESH_BINARY)
#마스크 영역지정,입력값은 검정색, 흰색은 통과색값은 통과.
mask_inv = cv2.bitwise_not(mask)

cv2.imshow('mask',  mask)
cv2.imshow('mask_inv',  mask_inv)
cv2.waitKey()
cv2.destroyAllWindows()
#
# #3
# src1_bg = cv2.bitwise_and(roi, roi, mask = mask)
# #마스크 영역을 만들기 위해 bitwise_not을 사용한다. 검은색값은 통과 흰색영역은 입력값.
# cv2.imshow('src1_bg',  src1_bg)
#
# #4
# src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)
# cv2.imshow('src2_fg',  src2_fg)
#
# #5
# ##dst = cv2.add(src1_bg, src2_fg)
# dst = cv2.bitwise_or(src1_bg, src2_fg)
# cv2.imshow('dst',  dst)
#
# #6
# src1[0:rows, 0:cols] = dst
#
# #7
# # 이미지 합성 후 마감이 부자연스러울 때 블러를 사용하여 영상을 부드럽게 처리한다.
# dst1 = cv2.blur(src1, (3, 3), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
