import cv2 as cv
import numpy as np

face_cas = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv.VideoCapture(0)
while 1:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow("Detect Face", frame)
    if cv.waitKey(0) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
