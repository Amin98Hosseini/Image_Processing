import cv2
import numpy as np 

img_rgb = cv2.imread('mario.jpg')
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

temp = cv2.imread('mario1.jpg',0) 

w,h = temp.shape[::-1]


res = cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)

threshold = 0.7

loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),3)
cv2.imshow("img_rgb",img_rgb)
cv2.waitKey(0)