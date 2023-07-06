import cv2
import numpy as np  

img = cv2.imread('corner.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_gray = np.float32(img_gray)


corners = cv2.goodFeaturesToTrack(img_gray,100,0.01,10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,(255,0,255),1)

cv2.imshow("img",img)
cv2.waitKey(0)
