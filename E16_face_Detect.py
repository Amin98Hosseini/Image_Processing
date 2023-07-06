import cv2
import numpy as np 


faceXML = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
eyeXML = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(1)


while (1):
    _,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceXML.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h , x:x+w]
        roi_Color = frame[y:y+h , x:x+w]

        eyes = eyeXML.detectMultiScale(roi_gray)
        for(ex,ey,eh,ew) in eyes:
            cv2.rectangle(roi_Color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    cv2.imshow('face',frame)
    if cv2.waitKey(1)& 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

