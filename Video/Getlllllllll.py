#coding:utf-8
'''
通过摄像头识别一维条形码
'''

import cv2
from pyzbar.pyzbar import decode

# results = decode(cv2.imread('datas/images/barcode-3.jpg'))
# for result in results:
#     print('barcode = %s'% str(result.data))
# camera = cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print('cannot open camera 0')
    exit(0)

while True:
    ret,frame = cap.read()
    if not ret:
        print('cannot grab frame from camera')
        continue
    results = decode(frame)
    for result in results:
        print ("已识别")
        print('barcode = %s' % result.data)
        print(frame)
        cv2.imwrite("test_1015.jpg", frame)

        barcode_roi = frame[result.rect.left:result.rect.width,result.rect.top:result.rect.height]
        cv2.imshow('barcode:%s' % result.data,barcode_roi)

    cv2.imshow('camera',frame)
    key = cv2.waitKey(10)

    if key == 27:
        break

cv2.destroyAllWindows()