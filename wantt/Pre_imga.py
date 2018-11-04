
# encoding: utf-8
# -*- encoding: utf-8 -*-
import glob
import os
import numpy as np
from PIL import Image


# 如下图所示，我要找出JPEGImages文件夹下，所有与SegmentationClass文件夹里面的图片名称（不包括图片格式）相同的图片，
# 并将这些名称一样的图片保存输出到output文件夹下。

#outDir = os.path.abspath('/home/chenxp/datadisk/pascal/VOCdevkit/VOC2010/output')

outDir = os.path.abspath('C:/Sunaoxue/IT_Project/warrantysmart/Data/temp')


#Use the function: os.path.join
# mageDir1 = os.path.abspath('/home/chenxp/datadisk/pascal/VOCdevkit/VOC2010/JPEGImages')
# imageDir1 = os.path.abspath('C:/Sunaoxue/IT_Project/warrantysmart/Data/AbnormalCase/ExternalDamage')
imageDir1 = os.path.abspath('C:/Sunaoxue/IT_Project/warrantysmart/Data/AbnormalCase/SlightFault')
#Define the List of the images
image1 = []

#Get the absolute path of the images
imageList1 = glob.glob(os.path.join(imageDir1, '*.jpg'))

#Use the function: os.path.basename() Get the name of the images
for item in imageList1:
    image1.append(os.path.basename(item))

imageDir2 = os.path.abspath('C:/Sunaoxue/IT_Project/warrantysmart/Data/Abnormal')
image2 = []
imageList2 = glob.glob(os.path.join(imageDir2, '*.xml'))

for item in imageList2:
    image2.append(os.path.basename(item))

for item in image1:
    print item

for item in image2:
    print item

for item1 in image1:
    for item2 in image2:
        if item1 == item2:
            img = Image.open(os.path.join(imageDir2, item1))
            img.save(os.path.join(outDir, item2))