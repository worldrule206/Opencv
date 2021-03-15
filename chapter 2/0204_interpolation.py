# 0204.py
import cv2
from   matplotlib import pyplot as plt

imageFile = './data/lena.jpg'
src = cv2.imread(imageFile)
dst = cv2.resize(src, dsize=(0, 0), fx= 2, fy= 2, interpolation=cv2.INTER_LINEAR)

cv2.imshow("dst", dst)
cv2.waitKey(0)

#plt.axis('off')
#plt.imshow(imgGray, cmap = "gray", interpolation='hamming')

# interpolation[보간법] 지원되는 값은
# 'none', 'antialiased', 'nearest', 'bilinear', 'bicubic',
# 'spline16', 'spline36', 'hanning', 'hamming', 'hermite',
# 'kaiser', 'quadric'입니다. , 'catrom', 'gaussian', 'bessel',
# 'mitchell', 'sinc', 'lanczos'.

plt.show()
