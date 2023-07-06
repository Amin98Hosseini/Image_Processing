import cv2
import numpy as np  

cap = cv2.VideoCapture(1)
fg = cv2.createBackgroundSubtractorMOG2()

while (1):
     _,frame=cap.read()
     fmask = fg.apply(frame)
     cv2.imshow('org',frame)
     cv2.imshow('fg',fmask)

     k = cv2.waitKey(27)&0xff
     if (k == 27):
        break
cv2.destroyAllWindows()
cv2.release()