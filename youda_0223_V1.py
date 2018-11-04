from keras.preprocessing.image import ImageDataGenerator
from keras.datasets import cifar10

(x_train,y_train),(x_test,y_test) = cifar10.load_data()
datagen = ImageDataGenerator(
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)

datagen.fit(x_train)