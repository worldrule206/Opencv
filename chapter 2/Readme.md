# 1.3 이미지 편집 

- 1.3.1 [Image Interpolation ](#131-image-interpolation)
- 1.3.2 [Image Format](#122-ImageFormat)
#

### 1.3.1 Image Interpolation
```python
imageFile = './data'    # 이미지의 경로를 지정.
imgeName = 'lena.jpg'   # 이미지 이름. 

img = os.path.join(imageFile, imgeName) #저장경로 지정.
src = cv2.imread(img)                   # 지정된 이미지를 읽음.

st = cv2.resize(src, None, fx= 1.0, fy= 1.0, interpolation=cv2.INTER_LINEAR)

cv2.imshow('Lena color',img)            # 읽어드린 이미지를 윈도우로 출력.
cv2.waitKey(0)
```

&nbsp;
 **"cv2.resize()"** 원하는 크기의 이미지를 읽어 올 수 있다.
 &#160;&#160;[[링크]](https://docs.opencv.org/master/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d)

   &#160; &#160; &#160;dst = cv.resize(src, dsize, dst, fx , fy, [interpolation](https://docs.opencv.org/master/da/d54/group__imgproc__transform.html#ga5bb5a1fea74ea38e1a5445ca803ff121))
- src : 이미지 
- dsize : dsize= (640, 480) 이미지의 크기를 지정 가능.
- fx, fy : x, y의 비율을 지정하여 이미지의 크기를 지정 가능.
- interpolation : 이미지를 축소하거나 확대 시 이미지 데이터를 보간방법을 지정하여 이미지의 데이터를 생성 또는 제거함.
  ##
  &#160;&#160; **확 대**
  ##
  &#160;&#160; cv2.INTER_CUBIC 바이큐빅보간법    
  &#160;&#160; cv2.INTER_LINEAR 쌍 선형 보간법
  ##
  &#160;&#160; **축 소**
  ##
  &#160;&#160; cv2.INTER_AREA 영역 보간법
#

### 1.3.2 Image Format

```python
imageFile = './data/lena.jp'    # 이미지의 경로를 지정.
src = cv2.imread(imageFile)     # 지정된 이미지를 읽음.

cv2.imwrite('./data/Lena.bmp', img)
cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena2.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])

```
**"cv2.imwrite( )"**  원하는 형식의 이미지를 저장 할 수 있다.
&#160;&#160;[[링크]](https://docs.opencv.org/3.4/d8/d6a/group__imgcodecs__flags.html#ga292d81be8d76901bff7988d18d2b42ac)
#
