#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
cap=cv2.VideoCapture(1)
while(1):
    ret,frame=cap.read()   #get frame
    cv2.imshow("xiaorun",frame)
    # if cv2.waitKey(1)&0xFF==ord('q')or ret==False:
    if cv2.waitKey(60):
        break
cap.release()
cv2.destroyAllwindows()
