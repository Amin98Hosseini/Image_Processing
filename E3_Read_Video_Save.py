import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,24.0,(640,480))

while (1):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    out.write(frame)

    if cv2.waitKey(1)& 0xff == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()