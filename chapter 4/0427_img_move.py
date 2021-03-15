#0427
# 영상의 이동. 
import sys
import numpy as np
import cv2


src = cv2.imread('../data/lena.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()
# 영상파일의 유무 확인.

aff = np.array([[1, 0, 200],[0, 1, 100]], dtype=np.float32)
# 영상의 이동 x값에 대해 200, y값에 대해 100 이동.
dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
