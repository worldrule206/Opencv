# 0212.py
# FuncAnimation를 사용하여 사진을 영상처럼 프레임으로 보여준다.

import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 프로그램 시작    
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('./data/vtest.avi')
fig = plt.figure(figsize=(10, 6)) # fig.set_size_inches(10, 6)
fig.canvas.set_window_title('Video Capture')
plt.axis('off')

def init():
    global im
    retval, frame = cap.read() # 첫 프레임 캡처
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
##    return im,

def updateFrame(k): 
    retval, frame = cap.read()
    if retval:
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

ani = animation.FuncAnimation(fig, updateFrame, init_func=init, interval= 90)
# interval = 프레임 재생속도
plt.show()
if cap.isOpened():
    cap.release()
