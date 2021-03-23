# 0714.py
import cv2
import numpy as np
#1
src = cv2.imread('../data/hand.jpg')
# src = cv2.imread('./data/flower.jpg')
# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
data = src.reshape((-1,3)).astype(np.float32)
# data = hsv.reshape((-1,3)).astype(np.float32)
print('\n''src.shape = ', src.shape)
print('data.shape = ', data.shape, '\n')

#2
K = 2; attempt =5; KmeansFlags =  cv2.KMEANS_RANDOM_CENTERS;
term_crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# https://docs.opencv.org/master/d1/d5c/tutorial_py_kmeans_opencv.html

# https://docs.opencv.org/master/d5/d38/group__core__cluster.html#ga9a34dc06c6ec9460e90860f15bcd2f88
ret, labels, centers = cv2.kmeans(data, K, None, term_crit, attempt,
                                  KmeansFlags)
print('ret=', ret)
print('labels.shape=', labels.shape)
print('centers.shape=\n', centers.shape)
print('centers[float]=\n', centers)

#3
centers = np.uint8(centers) # float => int
print('centers[int]=\n', centers)

res= centers[labels.flatten()]
print('res.shape=\n', res.shape)
dst= res.reshape(src.shape)
print('dst.shape=\n', dst.shape)

labels2 = np.uint8(labels.reshape(src.shape[:2]))
print('labels2.max()=', labels2.max())
dst2 = np.zeros(src.shape, dtype=src.dtype)
for i in range(K): # 분할영역 표시
   r = np.random.randint(256)
   g = np.random.randint(256)
   b = np.random.randint(256)
   dst2[labels2 == i] = [b, g, r]
    
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
