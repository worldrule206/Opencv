# 0416.py
import cv2
src = cv2.imread('../data/lena.jpg')

rows, cols, channels = src.shape
M1 = cv2.getRotationMatrix2D( (rows/2, cols/2),  45, 0.5 )
M2 = cv2.getRotationMatrix2D( (rows/2, cols/2), -45, 1.0 )

dst1 = cv2.warpAffine( src, M1, (rows, cols), cv2.INTER_CUBIC , cv2.BORDER_REPLICATE, 0,(255,255,255))
#                      img , Matrix2, size, interpolation , board type , Fill, Fillcolor
dst2 = cv2.warpAffine( src, M2, (rows, cols),None, None, 1, 50)

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
