# -*- coding:utf-8 -*-


import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)
# image = cv2.imread('C:\Sunaoxue\IT_Project\ADD\Test_YingZhang/20180525164038159.png')
image = cv2.imread('C:\Sunaoxue\IT_Project\ADD\Test_YinZhang/Picture1.PNG')
hue_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

print (hue_image)
low_range = np.array([150, 100, 100])
high_range = np.array([180, 255, 255])

#low_range = np.array([80, 0, 150])
#high_range = np.array([180, 70, 200])


th = cv2.inRange(hue_image, low_range, high_range)
index1 = th == 255

img = np.zeros(image.shape, np.uint8)
img[:, :] = (255,255,255)
img[index1] = image[index1]#(0,0,255)
cv2.imshow('img', img)
cv2.waitKey(3000)
cv2.imwrite("Aftersale_test_2.jpg",img)
