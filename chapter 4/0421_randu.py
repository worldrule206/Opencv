# 0421.py
# 이미지 노이즈 추가.
import cv2
import numpy as np
import time

dst = np.full((512, 512, 3), (255, 255, 255), dtype=np.uint8)
nPoints = 200
pts = np.zeros((1, nPoints, 2), dtype=np.uint16)
rows, cols, chn = dst.shape
print(rows)
print(cols)
print(chn)

cv2.setRNGSeed(int(time.time()))
cv2.randu(pts, (0, 0), (512, 512))

# cv2.randn(pts, mean=(256,256), stddev = (100, 100))
# # mean 평균값좌표, stddev 분산률

# draw points
for k in range(nPoints):
    x, y = pts[0, k][:]  # pts[0, k, :]
    cv2.circle(dst, (x, y), radius=5, color=(0, 0, 255), thickness=-1)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
