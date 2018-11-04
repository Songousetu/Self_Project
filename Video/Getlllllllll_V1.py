#coding:utf-8
'''
通过摄像头识别一维条形码
'''

import cv2
from pyzbar.pyzbar import decode
from Video.Cexing_Function import Getsize
from Video.Gettiaoxingma import detect_bar,Resize

# results = decode(cv2.imread('datas/images/barcode-3.jpg'))
# for result in results:
#     print('barcode = %s'% str(result.data))
# camera = cv2.VideoCapture(1)
cap = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(0)
box=[]

if not cap.isOpened():
    print('cannot open camera 0')
    exit(0)

while True:
    ret,frame = cap.read()
    if not ret:
        print('cannot grab frame from camera')
        continue
    # bar_image = detect_bar(frame)
    #bar_image,box = detect_bar(frame,box)
    #frame = Resize(bar_image,box)
    results = decode(frame)
    for result in results:
        print ("已识别")
        print('barcode = %s' % result.data)
        barcode_roi = frame[result.rect.left:result.rect.width,result.rect.top:result.rect.height]
        ret2, frame2 = cap2.read()
        Image_Path = 'C:\Sunaoxue\IT_Project\ADD/' + str(result.data) + '.jpg'
        cv2.imwrite(Image_Path, frame2)
        Getsize(Image_Path)
        # .imshow('barcode:%s' % result.data,barcode_roi)
        #cv2.imshow('barcode:%s' % result.data,)

    cv2.imshow('camera',frame)
    key = cv2.waitKey(10)
    print (key)
    if key == 27:
        break

cv2.destroyAllWindows()