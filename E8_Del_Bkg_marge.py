import cv2
import numpy as np 

img2 = cv2.imread('python.jpg')
img1 = cv2.imread('pencil.jpg')

rows,cols,channels = img1.shape
roi = img2[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('img',img2gray)

ret,mask = cv2.threshold(img2gray,230,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask',mask_inv)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask_inv)

dst = cv2.add(img1_bg,img2_fg)
img2[0:rows,0:cols]=dst
cv2.imshow('img2',img2)







cv2.waitKey(0)
cv2.destroyAllWindows()