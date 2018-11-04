# -*- coding: utf-8 -*-



import cv2
import numpy as np
import json
from keras.models import load_model
# from numba import jit
from PIL import Image
import shutil
from  shutil import copy2


import os


model = load_model('my_model_0418.h5')

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



# img_path = '2_214.JPG'
# img_path = 'C:\Sunaoxue\IT_Project\warrantysmart\Data\NormalCase\seriouslydamaged\F15_518801_0S03405_L_20180110_2.jpg'
# img_path = 'C:\Sunaoxue\IT_Project\warrantysmart\Data\AbnormalCase\ExternalDamage\F25_518801_0L27772_L_20171207_2.jpg'
# img_path = 'C:/Sunaoxue/IT_Project/Pictrure_Big data_V1/test_0.jpg'

# @jit
def getdata(img_path,resize=True,data_format=None):

    img = cv2.imread(img_path)
    # img = image.load_img(img_path, target_size=(2448, 2448,3))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = Image.open(img_path)
    #img = img.convert("L")

    if resize:
        img = cv2.resize(img, (Width, Height))
        # img = img.resize(Width, Height)
    if (data_format == 'channels_last'):
        img = img.reshape(-1, Width, Height, 1)
    elif (data_format == 'channels_first'):
        img = img.reshape(-1, 1, Width, Height)
    x = img / 255.

    preds = model.predict(x)
    preds = np.round(preds,3)
    # print (preds)
    return preds


def Getresult(results):
    tempJson = {}
    for i in range(len(results[0])):
        temp = {}
        key = i+1
        value = str(results[0][i])
        temp[key] = value
        tempJson.update(temp)
    results = json.dumps(tempJson)
    # print (results)
    return results


def main(img_path):
    global Width, Height
    Width = 128
    Height = 128
    # num_classes = 3  # Caltech101为102  cifar10为10
    Results = getdata(img_path,data_format='channels_last')
    REsults = Getresult(Results)
    # print (REsults)
    return REsults


if __name__ == '__main__':

    dirfile = "C:\Sunaoxue\IT_Project\warrantysmart\Testfor0423/all"

    for filename in os.listdir(r"C:\Sunaoxue\IT_Project\warrantysmart\Testfor0423/all"):  # listdir的参数是文件夹的路径
        print (dirfile + "/" + filename)
        img_path = dirfile + "/" + filename

        testR = main(img_path)
        TestR = json.loads(testR)
        for key in TestR.keys():
            # print (int(TestR[key]).type())
            if float(TestR[key]) == 1 and int(key) == 1:
                # print (img_path)

                copy2(img_path, "C:\Sunaoxue\IT_Project\warrantysmart\Testfor0423\Abnormal")
            elif float(TestR[key]) == 1 and int(key) == 2:
                copy2(img_path, "C:\Sunaoxue\IT_Project\warrantysmart\Testfor0423\Normal")

            #     print (testR)


    # main()