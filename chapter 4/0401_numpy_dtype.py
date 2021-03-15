# 0401.py
import cv2
import numpy as np

img = cv2.imread('../data/lena.jpg') # cv2.IMREAD_COLOR
##img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

print('img.ndim=', img.ndim)    # 차원,채널의 갯수
print('img.shape=', img.shape)  # 512, 512 , 3채널
print('img.dtype=', img.dtype)  # data-type uint8

## np.bool, np.uint16, np.uint32, np.float32, np.float64, np.complex64
img = img.astype(np.int32)      # int32로 변환
print('img.dtype=',img.dtype)

img = np.uint8(img)              # int8로 변환
print('img.dtype=',img.dtype)
