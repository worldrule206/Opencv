# 0420.py
import cv2
import numpy as np

src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(src)
print('src:', minVal, maxVal, minLoc, maxLoc)

dst = cv2.normalize(src, None, 50, 100, cv2.NORM_MINMAX)
# normalize : 이미지를 정규화하기 위한 함수.
# 특정한 바운드리(기준) 안에 데이터를 넣고 분포도를 일정하게 맞춰주는 함수이다.
# 활용 : 어두운 이미지를 바운드리를 확장시켜 특정정보를 더 정확하게 볼 수 있다.
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dst)
print('dst:', minVal, maxVal, minLoc, maxLoc)

cv2.imshow('dst',  dst)
cv2.waitKey()
cv2.destroyAllWindows()
