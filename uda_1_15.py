# -*- encoding: utf-8 -*-
'''
def doPCA():
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    pca.fit(data)
    return pca

pca = doPCA()
print (pca.explained_variance_ratio_)
first_pc = pca.components_[0]
second_pc = pca.components_[1]
'''
from keras.models import Sequential
from keras.layers import Dense,Flatten,Dropout
from keras.callbacks import ModelCheckpoint #允许我们在每个epoch之后保存模型的权重

from keras.datasets import mnist
from keras.utils import np_utils
from keras.layers import MaxPool2D
from keras.layers import Conv2D
# Conv2D(filters, kernel_size, strides, padding, activation='relu', input_shape)



(X_train,y_train),(X_test,y_test) = mnist.load_data()

# rescale [0,255] to [0,1]
X_train = X_train.astype('float32')/255
X_test = X_test.astype('float32')/255

print (X_test)

print ("Integer-valued labels:")
print (y_train[:10])

# one- hot encode the labels

y_train = np_utils.to_categorical(y_train,10)
y_test = np_utils.to_categorical(y_test,10)
print ("One-hot labels:")
print (y_train[:10])

# define the model

model = Sequential()
model.add(Flatten(input_shape=X_train.shape[1:])) # 展平，将图片矩阵 转换成向量
model.add(Dense(512,activation='relu'))
model.add(Dropout(0.2)) #每个点被忽略掉的概率，用来防止过拟合
model.add(Dense(512,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))


## summarize the model

model.summary()

## compile the model
# model.compile(loss='categorical_crossentropy', optimizer='rmsprop',metrics=['accuracy'])
model.compile(loss='categorical_crossentropy', optimizer='sgd',metrics=['accuracy'])

## train the model
checkpointer = ModelCheckpoint(filepath='mnist.model.best.hdf5',verbose=1,save_best_only=True)
# filepath 指定了权重的保存位置，save_best_only=True 仅保存权重以让验证集达到最佳准确率，verbose=1何时更新

hist = model.fit(X_train,y_train,batch_size=128,epochs=10,validation_split=0.2,callbacks=[checkpointer],verbose=1,shuffle=True)

# 加载达到最佳验证准确率的权重
model.load_weights('mnist.model.best.hdf5')

## evaluate test accuracy
score = model.evaluate(X_test,y_test,verbose=0)
accuracy = 100*score[1]
print ('Test accuracy : %.4f%%' % accuracy)
