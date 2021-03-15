# 0402.py
import cv2
##import numpy as np

img = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)
print('img.shape=', img.shape)

img = img.reshape(img.shape[0]*img.shape[1]) # 데이터를 하나의 행으로 데이터를 펼침.
print('img.shape=', img.shape)

img = img.flatten() # 데이터를 하나의 행으로 데이터를 펼침.
print('img.shape=', img.shape)

img = img.reshape(-1, 512, 512) # 가로 512, 세로 512로 데이터정렬.
print('img.shape=', img.shape)

cv2.imshow('img', img[0])
cv2.waitKey()
cv2.destroyAllWindows()
