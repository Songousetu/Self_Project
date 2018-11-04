# -*- encoding: utf-8 -*-


import keras
from keras.datasets import cifar10
from keras.utils import np_utils
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Flatten,Dropout
from keras.callbacks import ModelCheckpoint #允许我们在每个epoch之后保存模型的权重
from keras.layers import Convolution2D,MaxPool2D,Flatten,Dense,Dropout

(x_train,y_train),(x_test,y_test) = cifar10.load_data()

## visualize the first 24 training images
'''
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inlinex

figt = plt.figure(figsize=(20,5))
for i in range (36):
    ax = figt.add_subplot(3,12,i+1,xticks=[],yticks=[])
    ax.imshow(np.squeeze(X_train[i]))
'''
# rescale [0,255] to [0,1]
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255

# one- hot encode the labels
num_classes = len(np.unique(y_train))
y_train = np_utils.to_categorical(y_train,num_classes)
y_test = np_utils.to_categorical(y_test,num_classes)


# break training set into training and validation sets
(x_train,x_valid) = x_train[5000:],x_train[:5000] #前5000行为valid
(y_train,y_valid) = y_train[5000:],y_train[:5000]


# print shape of training sets
print (x_train.shape)
# print number of training ,validation, and test images
print(x_train.shape[0])
print(x_test.shape[0])
print(x_valid.shape[0])
'''
model = Sequential()
model.add(Flatten(input_shape=x_train.shape[1:])) # 展平，将图片矩阵 转换成向量
model.add(Dense(1000,activation='relu'))
model.add(Dropout(0.2)) #每个点被忽略掉的概率，用来防止过拟合
model.add(Dense(1000,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))
'''
## summarize the model

model = Sequential()
model.add(Convolution2D(filters=16,kernel_size=2,padding="same",activation='relu',input_shape=(32,32,3)))
model.add(MaxPool2D(pool_size=2))
model.add(Convolution2D(filters=32,kernel_size=2,padding="same",activation='relu'))
model.add(MaxPool2D(pool_size=2))
model.add(Convolution2D(filters=64,kernel_size=2,padding="same",activation='relu'))
model.add(MaxPool2D(pool_size=2))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(500,activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(10,activation='softmax'))# 最后分为10类
model.summary()



## compile the model
model.compile(loss='categorical_crossentropy', optimizer='rmsprop',metrics=['accuracy'])

## train the model
checkpointer = ModelCheckpoint(filepath='MLP.model.best.hdf5',verbose=1,save_best_only=True)
# filepath 指定了权重的保存位置，save_best_only=True 仅保存权重以让验证集达到最佳准确率，verbose=1何时更新，保存了验证准确率最高的权重

hist = model.fit(x_train,y_train,batch_size=32,epochs=100,validation_split= (x_valid,y_valid),callbacks=[checkpointer],verbose=2,shuffle=True)

# 加载达到最佳验证准确率的权重
model.load_weights('MLP.model.best.hdf5')

## evaluate test accuracy
score = model.evaluate(x_test,y_test,verbose=0)
accuracy = 100*score[1]
print ('Test accuracy : %.4f%%' % accuracy)