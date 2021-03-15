# 0417.py
import cv2
import numpy as np

src1 = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src2 = np.zeros(shape=(512,512), dtype=np.uint8) + 100

dst1 = src1 + src2
print(dst1)
#연산의 한계치가 없기 때문에 255넘어가는 픽셀값을 그대로 표현한다.
dst2 = cv2.add(src1, src2)
print(dst2)
#add함수는 255보다 큰값이 나오면 255로 수렴하게 만드는 함수이다.
#dst2 = cv2.add(src1, src2, dtype = cv2.CV_8U)

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()
cv2.destroyAllWindows()
