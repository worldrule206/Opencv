# 0601.py
import cv2
import numpy as np

src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)

dst1= cv2.boxFilter(src, ddepth=-1, ksize=(11, 11))
dst2 = cv2.boxFilter(src, ddepth=-1, ksize=(21, 21))

dst3 = cv2.bilateralFilter(src, d=11, sigmaColor=10, sigmaSpace=10)
dst4 = cv2.bilateralFilter(src, d=-1, sigmaColor=10, sigmaSpace=10,\
                           borderType= cv2.BORDER_REFLECT )
# https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html#ga9d7064d478c95d60003cf839430737ed
# cv.bilateralFilter( src, d, sigmaColor, sigmaSpace[, dst[, borderType]])
# src = img, d = same size and type as src,
# sigmaColor = 색 공간에서 시그마를 필터링합니다. 매개 변수 값이 클수록 픽셀 이웃 (sigmaSpace 참조) 내에서 더 먼 색상이 함께 혼합되어 더 큰 준 동일 색상 영역이 생성됩니다.
# sigmaSpace = 좌표 공간에서 시그마를 필터링합니다. 매개 변수 값이 클수록 색상이 충분히 가까우면 더 먼 픽셀이 서로 영향을 미칩니다 (sigmaColor 참조). d> 0이면 sigmaSpace에 관계없이 이웃 크기를 지정합니다. 그렇지 않으면 d는 sigmaSpace에 비례합니다.
# borderType = 이미지 외부의 픽셀을 외삽하는데 사용되는 테두리 모드

# cv2.imshow('dst1',  dst1)
# cv2.imshow('dst2',  dst2)
# cv2.imshow('dst3',  dst3)
cv2.imshow('dst4',  dst4)
cv2.waitKey()    
cv2.destroyAllWindows()
