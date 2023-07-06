import cv2
import numpy as np 

img = cv2.imread('python.jpg',cv2.IMREAD_COLOR)

px = img[200,200]
print(px)
px = img[100:200,200:400]
print(px)

img [100:200 , 200:400] =[0,0,255]

'''part1 = img[100:200,100:200]
img[200:300 ,200:300]=part1'''

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()