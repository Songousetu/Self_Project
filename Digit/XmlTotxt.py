# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 15:36:44 2018

@author: gg
"""

import xml.dom.minidom
import os

save_dir = 'D:\plate_train'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
f = open(os.path.join(save_dir, 'landmark.txt'), 'w')

DOMTree = xml.dom.minidom.parse('D:\plate_train\label\Drivingrecord_001.xml')
annotation = DOMTree.documentElement

filename = annotation.getElementsByTagName("filename")[0]
imgname = filename.childNodes[0].data + '.jpg'
print(imgname)

objects = annotation.getElementsByTagName("object")

loc = [imgname]  # 文档保存格式：文件名 坐标

for object in objects:
    bbox = object.getElementsByTagName("bndbox")[0]
    leftTopx = bbox.getElementsByTagName("leftTopx")[0]
    lefttopx = leftTopx.childNodes[0].data
    print(lefttopx)
    leftTopy = bbox.getElementsByTagName("leftTopy")[0]
    lefttopy = leftTopy.childNodes[0].data
    print(lefttopy)
    rightTopx = bbox.getElementsByTagName("rightTopx")[0]
    righttopx = rightTopx.childNodes[0].data
    print(righttopx)
    rightTopy = bbox.getElementsByTagName("rightTopy")[0]
    righttopy = rightTopy.childNodes[0].data
    print(righttopy)
    rightBottomx = bbox.getElementsByTagName("rightBottomx")[0]
    rightbottomx = rightBottomx.childNodes[0].data
    print(rightbottomx)
    rightBottomy = bbox.getElementsByTagName("rightBottomy")[0]
    rightbottomy = rightBottomy.childNodes[0].data
    print(rightbottomy)
    leftBottomx = bbox.getElementsByTagName("leftBottomx")[0]
    leftbottomx = leftBottomx.childNodes[0].data
    print(leftbottomx)
    leftBottomy = bbox.getElementsByTagName("leftBottomy")[0]
    leftbottomy = leftBottomy.childNodes[0].data
    print(leftbottomy)

    loc = loc + [lefttopx, lefttopy, righttopx, righttopy, rightbottomx, rightbottomy, leftbottomx, leftbottomy]

for i in range(len(loc)):
    f.write(str(loc[i]) + ' ')
f.write('\t\n')
f.close()
