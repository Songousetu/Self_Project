# -*- coding: utf-8 -*-

# 定义层
import sys
import argparse
import numpy as np
from PIL import Image
# import requests
from io import BytesIO
import matplotlib.pyplot as plt
import os
from keras.preprocessing import image
from keras.models import load_model
from keras.applications.inception_v3 import preprocess_input

# 狂阶图片指定尺寸
target_size = (229, 229) #fixed size for InceptionV3 architecture
model = load_model('Nsm_0602.h5')


# img = Image.open('/root/DD/NSM/Test/NSM9900837/IMG_2237.JPG')
# 预测函数
# 输入：model，图片，目标尺寸
# 输出：预测predict
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
  print (preds[0])
  return preds[0]

# 画图函数
# 预测之后画图，这里默认是猫狗，当然可以修改label
'''
labels = ("1", "2","3","4", "5","6")

'''
# 载入模型


# 本地图片

def allfile(file_path,model,target_size):
  filelist = os.path.abspath(file_path)
  total_num = len(filelist)
  print (total_num)
  i = 0
  for item in filelist:
    print(item)
    # img = Image.open(item)
    # print(item)
    preds =0
    # preds = predict(model,img, target_size)
  print (preds)
  return preds

# result = allfile('/root/DD/Test_0530/24_C',model,target_size)
result = allfile('C:\Sunaoxue\IT_Project/NSM/Data/Test',model,target_size)

# plot_preds(img, preds)
'''
# 图片URL
response = requests.get('C:\Sunaoxue\IT_Project/NSM/Data/Test')
img = Image.open(BytesIO(response.content))
preds = predict(model, img, target_size)
plot_preds(img, preds)

'''