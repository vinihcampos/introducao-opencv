import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('../xml/haarcascade_frontalface_default.xml')

img = cv2.imread('../images/messi.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mascara = cv2.imread('../images/mascara.jpg')

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
