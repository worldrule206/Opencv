# 0715.py
import cv2
import numpy as np

#1
src = cv2.imread('../data/circles.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, res = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

print('\n''res.shape=',res.shape)
print('gray ret=', ret, '\n')

#2
ret, labels, stats, centriods = cv2.connectedComponentsWithStats(res)
print('labels.shape=', labels.shape)
print('labels ret=', ret)

#3
dst = np.zeros(src.shape, dtype=src.dtype)
for i in range(1, ret): # 분할영역 표시
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    dst[labels == i] = [b, g, r]
    print(i, [b, g, r])

    print(stats[i])
    x, y, width, height, pixels = stats[i]
    cv2.rectangle(dst, (x, y), (x + width, y + height), (0, 0, 255), 2)
    print ((x,y))

cv2.imshow('dst',  dst) 
cv2.waitKey()
cv2.destroyAllWindows()
