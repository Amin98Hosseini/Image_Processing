import cv2
import numpy as np

img=cv2.imread('book1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret , threshold = cv2.threshold(gray,30,255,cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)


cv2.imshow('page1',img)
cv2.imshow('page2',threshold)
cv2.imshow('page3',th)

cv2.waitKey(0)
cv2.destroyAllWindows()