# 0607.py
import cv2
import numpy as np

src  = cv2.imread('../data/rect.jpg', cv2.IMREAD_GRAYSCALE)
##src  = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

#1
kx, ky = cv2.getDerivKernels(1, 0, ksize=3)
# https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga6d6c23f7bd3f5836c31cfae994fc4aea
# cv2.getDerivKernels = 공간 이미지 파생 모델을 계산하기 위한 필터 계수를 반환합니다.

sobelX = ky.dot(kx.T) # 소벨필터 생성.
# kx.T =축을 기준으로 x -> y 로 y -> x로 축을 변경함.
# ky.dot(kx.T) = kx.T * ky dot는 행렬의 곱.
print('kx.T=', kx.T )
# print('kx=', kx )
print('ky=', ky )
print('sobelX=', sobelX)

gx = cv2.filter2D(src, cv2.CV_32F, sobelX) # 필터 적용.
cv2.imshow('gx',  gx)
# gx = cv2.sepFilter2D(src, cv2.CV_32F, kx, ky) # kx필터, ky필터 적용.

#2
kx, ky = cv2.getDerivKernels(0, 1, ksize=3)
sobelY = ky.dot(kx.T)
print('kx=', kx)
print('ky=', ky)
print('sobelY=', sobelY)
gy = cv2.filter2D(src, cv2.CV_32F, sobelY)
cv2.imshow('gy',  gy)
##gy = cv2.sepFilter2D(src, cv2.CV_32F, kx, ky)

#3
mag = cv2.magnitude(gx, gy) # magnitude = 벡터 연산.
ret, edge = cv2.threshold(mag, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('edge',  edge)
cv2.waitKey()    
cv2.destroyAllWindows()
