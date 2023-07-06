import cv2
import numpy as np  
import matplotlib.pyplot as plt


img_temp = cv2.imread('flower1.jpg',0)
img = cv2.imread('flower3.jpg',0)

orb = cv2.ORB.create()

kp1,des1 = orb.detectAndCompute(img_temp,None)
kp2,des2 = orb.detectAndCompute(img,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches,key=lambda  x: x.distance)

img_out = cv2.drawMatches(img,kp2,img_temp,kp1,matches[:10],None,flags=2)
plt.imshow(img_out)
plt.show()
