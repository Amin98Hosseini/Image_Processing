import cv2
import numpy as np 

img1 = cv2.imread('python.jpg')
img2 = cv2.imread('pencil.jpg')

#add=img1+img2
#add=cv2.add(img1,img2)
add=cv2.addWeighted(img1,0.4,img2,0.7,0)
cv2.imshow('add',add)

cv2.waitKey(0)
cv2.destroyAllWindows()