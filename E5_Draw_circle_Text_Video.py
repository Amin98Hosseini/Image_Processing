import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
pts = np.array([[10,12],[15,17],[22,76],[50,20]])

while (1):
    ret,frame = cap.read()
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #frame = cv2.line(frame,(100,100),(200,400),(0,0,255),10)
    #frame = cv2.rectangle(frame,(100,200),(200,300),(0,255,0),1)
    #Draw circle
    frame = cv2.circle(frame,(200,200),70,(0,0,255),2)
    #frame - cv2.polylines(frame,[pts],False,(255,0,0),2)
    #Wirte Text
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame,'Amin',(100,100),font,1,(100,0,0),2)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1)& 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()