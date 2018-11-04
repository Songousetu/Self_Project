# -*- coding: utf-8 -*-

from keras.models import Sequential

import cv2
import numpy as np
import json
from keras.models import load_model
from numba import jit


#model = Sequential()

model = load_model('my_model.h5')

img_path = '2_214.jpg'
# img_path = 'C:/Sunaoxue/IT_Project/Pictrure_Big data_V1/test_663.jpg'
# img_path = 'C:/Sunaoxue/IT_Project/Pictrure_Big data_V1/test_0.jpg'



@jit
def getdata(img_path,resize=True,data_format=None):

    img = cv2.imread(img_path)
    # img = image.load_img(img_path, target_size=(2448, 2448,3))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if resize:
        img = cv2.resize(img, (Width, Height))
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
    print (results)
    return results


def main():
    global Width, Height
    Width = 32
    Height = 32
    # num_classes = 3  # Caltech101为102  cifar10为10
    results = getdata(img_path,data_format='channels_last')
    results = Getresult(results)


if __name__ == '__main__':
    main()