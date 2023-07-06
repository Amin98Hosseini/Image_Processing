import cv2
import numpy as np 

cap = cv2.VideoCapture(0)


while (1):
    ret,frame = cap.read()
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #frame = cv2.line(frame,(100,100),(200,400),(0,0,255),10)
    frame = cv2.rectangle(frame,(100,200),(200,300),(0,255,0),1)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1)& 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()