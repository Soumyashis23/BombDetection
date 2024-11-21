import numpy as np
import cv2
import imutils
import datetime

bomb_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)
firstFrame = None
bomb_exist = False
while True:
    ret, frame = camera.read()
    if frame is None:
        break
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bomb = bomb_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))
    if len(bomb) > 0:
        gun_exist = True
    for (x, y, w, h) in bomb:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.imshow( "ALERT...SECURITY!", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break


if bomb_exist:
    print("bombs detected")
else:
    print("bombs NOT detected")

camera.release()
cv2.destroyAllWindows()
