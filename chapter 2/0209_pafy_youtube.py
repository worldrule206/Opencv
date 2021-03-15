# 0209.py
'''
 pip install youtube_dl
 pip install pafy
'''
import cv2, pafy

url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
video = pafy.new(url)
# documentation
# https://pythonhosted.org/pafy/#Pafy.pafy.new
try:
        print('title = ', video.title)
        print('video.rating = ', video.rating)
        print('video.duration = ', video.duration)
        print('video.bigthumb = ', video.bigthumb)
        print('video.author = ', video.author)
        print('video.dislikes = ', video.dislikes)
        print('video.keywords = ', video.keywords)
        print('video.length = ', video.length)
        print('video.likes = ',  video.likes)
        print('video.published = ', video.published)
        print('video.mix = ', video.mix)
        print('video.length = ', video.length)
except:
        pass

best = video.getbest(preftype='mp4')     # 'mp4','3gp'
print('best.resolution', best.resolution)

cap=cv2.VideoCapture(best.url)
while(True):
        retval, frame = cap.read()
        if not retval:
                break
        cv2.imshow('frame',frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,100,200)
        cv2.imshow('edges',edges)

        key = cv2.waitKey(25)
        if key == 27: # Esc
                break

cv2.destroyAllWindows()
