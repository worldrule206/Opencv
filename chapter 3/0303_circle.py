#0303.py
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
cx = img.shape[0]//2
cy = img.shape[1]//2

x = range(0, 501, 100) # 0~ 500까지 100씩 증가.
for r in x:
    cv2.circle(img, (cx, cy), r, color=(255, 0, 0))

cv2.circle(img, (cx, cy), radius=20, color=(0, 0, 255), thickness=-1)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
