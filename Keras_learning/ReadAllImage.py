# -*- coding: utf-8 -*-



import cv2
import numpy as np
import json
from keras.models import load_model
# from numba import jit
from PIL import Image


import os

dirfile = "C:\Sunaoxue\IT_Project\warrantysmart\Data\NormalCase\seriouslydamaged"


for filename in os.listdir(r"C:\Sunaoxue\IT_Project\warrantysmart\Data\NormalCase\seriouslydamaged"):              #listdir的参数是文件夹的路径
   print ( filename)                                  #此时的filename是文件夹中文件的名称


'''


def load_Img(imgDir, imgFoldName):
    imgs = os.listdir(imgDir + imgFoldName)
    imgNum = len(imgs)
    data = np.empty((imgNum, 1, 12, 12), dtype="float32")
    label = np.empty((imgNum,), dtype="uint8")
    for i in range(imgNum):
        img = Image.open(imgDir + imgFoldName + "/" + imgs[i])
        arr = np.asarray(img, dtype="float32")
        data[i, :, :, :] = arr
        label[i] = int(imgs[i].split('.')[0])
    return data, label



if __name__ == '__main__':

    craterDir = "./data/CraterImg/Adjust/"
    foldName = "East_CraterAdjust12"
    data, label = load_Img(craterDir,foldName)

'''