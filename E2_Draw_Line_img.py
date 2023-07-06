from matplotlib import pyplot as plt
import cv2
import numpy as np 

img = cv2.imread('python.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img,cmap='gray')
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([100,200],[200,300],'r',linewidth=2)
plt.show()
cv2.imwrite('imgout.jpg',img)