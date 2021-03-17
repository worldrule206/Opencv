# 0510.py
import cv2
import numpy as np

src = np.array([[0, 0, 0, 0],
              [1, 1, 3, 5],
              [6, 1, 1, 3],
              [4, 3, 1, 7]
              ], dtype=np.uint8)

hist = cv2.calcHist(images=[src], channels=[0], mask=None,
                    histSize=[4], ranges=[0, 8])
print('hist = ', hist)

backP = cv2.calcBackProject([src], [0], hist, [0, 8], scale=1)
#  히스토그램 역투영 함수 - cv2.calcBackProjection
#  만든 히스토그램으로 히스토그램 역투영을 합니다.
#  히스토그램 역투영을 마스크로 이용하여 기존 영상과 마스크 연산을 통해 원하는 색을 검출할 수 있습니다.
#  https://deep-learning-study.tistory.com/132
print('backP = ', backP)
