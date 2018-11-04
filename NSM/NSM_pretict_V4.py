# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from keras.applications.inception_v3 import preprocess_input
import json

# 狂阶图片指定尺寸
target_size = (229, 229) #fixed size for InceptionV3 architecture
model = load_model('Nsm_0630.h5')

def Getresult(results):
    tempJson = {}
    for i in range(len(results[0])):
        temp = {}
        key = i+1
        value = str(round(results[0][i],3))
        temp[key] = value
        tempJson.update(temp)
    results = json.dumps(tempJson)
    print (results)
    return results



def predict(model, img, target_size):
  """Run model prediction on image
  Args:
    model: keras model
    img: PIL format image
    target_size: (w,h) tuple
  Returns:
    list of predicted labels and their probabilities
  """
  if img.size != target_size:
    img = img.resize(target_size)

  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  preds = model.predict(x)
  # print (preds[0])
  return preds


## rootdir = '/root/DD/Test_0530/24_C'
rootdir = 'C:\Sunaoxue\IT_Project\NSM\Data/test'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
  path = os.path.join(rootdir,list[i])
  if os.path.isfile(path):
    print (path)
    img = Image.open(path)
    preds = predict(model, img, target_size)
    reuslt = Getresult(preds)




