# -*- coding: utf-8 -*-



from keras.applications.resnet50 import ResNet50

# 定义ResNet50模型
ResNet50_model = ResNet50(weights='imagenet')
print (ResNet50_model)