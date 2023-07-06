import cv2
import numpy as np 

cap = cv2.VideoCapture(1)

while (1):
    _,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,10])
    upper_red = np.array([255,255,255])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    k = cv2.waitKey(27)&0xff
    if (k == 27):
        break
cv2.destroyAllWindows()
cv2.release()