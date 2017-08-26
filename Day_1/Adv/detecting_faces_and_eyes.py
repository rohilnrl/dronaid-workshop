import cv2
import numpy as np

face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')


cap=cv2.VideoCapture(0)

while True:
    _,frame= cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray,1.3,5)
    #used to find faces.

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,0),2)
        roi_gray=frame[y:y+h,x:x+w]
        roi_color= frame[y:y+h,x:x+w]
     #for marking rectangle around the detected faces

        
        eyes= eye_cascade.detectMultiScale(roi_gray)
        #finding eyes in the given region of face

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,0),2)

    cv2.imshow('frame',frame)
    k=cv2.waitKey(30) &0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
