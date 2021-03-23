# 0703.py
import cv2
import numpy as np

src = cv2.imread('../data/rect.jpg')
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 100)

lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180.0, threshold=100)
# https://docs.opencv.org/3.4/dd/d1a/group__imgproc__feature.html#ga8618180a5948286384e3b7ca02f6feeb
print('lines.shape=', lines.shape)
#src = W × H, Temp w x h result : (W-w+1)×(H-h+1)이다.

for line in lines:
    x1, y1, x2, y2   = line[0]
    cv2.line(src,(x1,y1),(x2,y2),(0,0,255),2)
    
cv2.imshow('edges',  edges)
cv2.imshow('src',  src)
cv2.waitKey()
cv2.destroyAllWindows()
