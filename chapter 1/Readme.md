# 1.2 기본 명령어 

- 1.2.1 [Image Read & Write](#121-ImageRead&Write)
- 1.2.2 [Image Format](#122-ImageFormat)
#

### 1.2.1 Image Read & Write
```python
imageFile = './data'    # 이미지의 경로를 지정.
imgeName = 'lena.jpg'   # 이미지 이름. 
Rename = 'lena-1.jpg'   # 이미지의 다른이름.

src = os.path.join(imageFile, imgeName)        #저장경로 지정.
As_save = os.path.join(imageFile, imgreName)   #저장경로 지정.

img = cv2.imread(src)              # 지정된 이미지를 읽음.
cv2.imwrite(Rename, imageFile)     # 이미지를 다른이름으로 저장.
cv2.imshow('Lena color',img)       # 읽어드린 이미지를 윈도우로 출력.
```

&nbsp;
 **"cv2.imread()"** 원하는 모드의 이미지를 읽어 올 수 있다.
 &#160;&#160;[[링크]](https://docs.opencv.org/3.4/d8/d6a/group__imgcodecs__flags.html#ga61d9b0126a3e57d9277ac48327799c80)
#

### 1.2.2 Image Format

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
