# -*- encoding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Convolution2D,MaxPool2D,Flatten,Dense,Dropout
from keras.callbacks import ModelCheckpoint #允许我们在每个epoch之后保存模型的权重


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

hist = model.fit(x_train,y_train,batch_size=32,epochs=20,validation_split=0.2,callbacks=[checkpointer],verbose=2,shuffle=True)

# 加载达到最佳验证准确率的权重
model.load_weights('MLP.model.best.hdf5')

## evaluate test accuracy
score = model.evaluate(x_test,y_test,verbose=0)
accuracy = 100*score[1]
print ('Test accuracy : %.4f%%' % accuracy)