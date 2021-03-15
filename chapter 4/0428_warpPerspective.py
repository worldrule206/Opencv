#0428
#이미지 펼침 함수.
import sys
import numpy as np
import cv2

src = cv2.imread('../data/lena.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400
srcQuad = np.array([[355,204], [816,433], [593,722], [116,385]], np.float32)
# 사각형 기준으로 시계방향으로 사각형포인트를 입력한다.
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
