# 0706.py
import cv2
import numpy as np

#1
src = np.zeros(shape=(512,512,3), dtype=np.uint8)
cv2.rectangle(src, (50, 100), (450, 400), (255, 255, 255), -1)
cv2.rectangle(src, (100, 150), (400, 350), (0, 0, 0), -1)
cv2.rectangle(src, (200, 200), (300, 300), (255, 255, 255), -1)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

#2
mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
##method =cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(gray, mode, method) #윤곽선 찾기
# https://docs.opencv.org/master/d3/dc0/group__imgproc__shape.html#gadf1ad6a0b82947fa1fe3c3d497f260e0

print('type(contours)=', type(contours))
print('type(contours[0])=', type(contours[0]))
print('len(contours)=', len(contours))
print('contours[0].shape=', contours[0].shape)
print('contours[0]=', contours[0])

#3
cv2.drawContours(src, contours, -1, (255,0,0), 3) # 윤곽선 그리기
# https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga746c0625f1781f1ffc9056259103edbc

#4
for pt in contours[0][:]: # 윤곽선 좌표
    print("\n꼭지점좌표= ", pt)
    cv2.circle(src, (pt[0][0], pt[0][1]), 5, (0,0,255), -1)

cv2.imshow('src',  src)
cv2.waitKey()
cv2.destroyAllWindows()
