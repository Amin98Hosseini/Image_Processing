import cv2
import numpy as np 

cap = cv2.VideoCapture(1)

while (1):
    _,frame=cap.read()
    laplacian = cv2.Laplacian(frame,cv2.CV_8U)
    #sobelx = cv2.Sobel(frame,cv2.CV_8U,1,0,ksize=5)
    #sobely = cv2.Sobel(frame,cv2.CV_8U,0,1,ksize=5)
    canny = cv2.Canny(frame,100,200)


    cv2.imshow("laplacian",laplacian)
    #cv2.imshow("sobelx",sobelx)
    #cv2.imshow("sobely",sobely)
    cv2.imshow("canny",canny)

    k = cv2.waitKey(27)&0xff
    if (k == 27):
        break
cv2.destroyAllWindows()
cv2.release()