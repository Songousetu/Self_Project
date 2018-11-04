
import os
import numpy as np




Width = 32
Height = 32
num_classes = 102
pic_dir_out = 'E:/pic_cnn/pic_out/'
pic_dir_data = 'E:/pic_cnn/pic_dataset/Caltech101/'



def eachFile(filepath):  # 将目录内的文件名放入列表中
    pathDir = os.listdir(filepath)
    out = []
    for allDir in pathDir:
        child = allDir.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题
        out.append(child)
    return out


def get_data(data_name, train_percentage=0.7, resize=True, data_format=None):  # 从文件夹中获取图像数据
    file_name = os.path.join(pic_dir_out, data_name + str(Width) + "X" + str(Height) + ".pkl")
    if os.path.exists(file_name):  # 判断之前是否有存到文件中
        (X_train, y_train), (X_test, y_test) = cPickle.load(open(file_name, "rb"))
        return (X_train, y_train), (X_test, y_test)
    data_format = conv_utils.normalize_data_format(data_format)
    pic_dir_set = eachFile(pic_dir_data)
    X_train = []
    y_train = []
    X_test = []
    y_test = []
    label = 0
    for pic_dir in pic_dir_set:
        print (pic_dir_data + pic_dir)
        if not os.path.isdir(os.path.join(pic_dir_data, pic_dir)):
            continue
        pic_set = eachFile(os.path.join(pic_dir_data, pic_dir))
        pic_index = 0
        train_count = int(len(pic_set) * train_percentage)
        for pic_name in pic_set:
            if not os.path.isfile(os.path.join(pic_dir_data, pic_dir, pic_name)):
                continue
            img = cv2.imread(os.path.join(pic_dir_data, pic_dir, pic_name))
            if img is None:
                continue
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            if (resize):
                img = cv2.resize(img, (Width, Height))
            if (data_format == 'channels_last'):
                img = img.reshape(-1, Width, Height, 1)
            elif (data_format == 'channels_first'):
                img = img.reshape(-1, 1, Width, Height)
            if (pic_index < train_count):
                X_train.append(img)
                y_train.append(label)
            else:
                X_test.append(img)
                y_test.append(label)
            pic_index += 1
        if len(pic_set) <> 0:
            label += 1
    X_train = np.concatenate(X_train, axis=0)
    X_test = np.concatenate(X_test, axis=0)
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    cPickle.dump([(X_train, y_train), (X_test, y_test)], open(file_name, "wb"))
    return (X_train, y_train), (X_test, y_test)


def get_2data(data_name, resize=True, data_format=None):  # 当数据被分为train和test两个部分时使用
    file_name = os.path.join(pic_dir_out, data_name + str(Width) + "X" + str(Height) + ".pkl")
    if os.path.exists(file_name):  # 判断之前是否有存到文件中
        (X_train, y_train), (X_test, y_test) = cPickle.load(open(file_name, "rb"))
        return (X_train, y_train), (X_test, y_test)
    data_format = conv_utils.normalize_data_format(data_format)
    all_dir_set = eachFile(pic_dir_data)
    X_train = []
    y_train = []
    X_test = []
    y_test = []

    for all_dir in all_dir_set:
        if not os.path.isdir(os.path.join(pic_dir_data, all_dir)):
            continue
        label = 0
        pic_dir_set = eachFile(os.path.join(pic_dir_data, all_dir))
        for pic_dir in pic_dir_set:
            print
            pic_dir_data + pic_dir
            if not os.path.isdir(os.path.join(pic_dir_data, all_dir, pic_dir)):
                continue
            pic_set = eachFile(os.path.join(pic_dir_data, all_dir, pic_dir))
            for pic_name in pic_set:
                if not os.path.isfile(os.path.join(pic_dir_data, all_dir, pic_dir, pic_name)):
                    continue
                img = cv2.imread(os.path.join(pic_dir_data, all_dir, pic_dir, pic_name))
                if img is None:
                    continue
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                if resize:
                    img = cv2.resize(img, (Width, Height))
                if (data_format == 'channels_last'):
                    img = img.reshape(-1, Width, Height, 1)
                elif (data_format == 'channels_first'):
                    img = img.reshape(-1, 1, Width, Height)
                if ('train' in all_dir):
                    X_train.append(img)
                    y_train.append(label)
                elif ('test' in all_dir):
                    X_test.append(img)
                    y_test.append(label)
            if len(pic_set) <> 0:
                label += 1
    X_train = np.concatenate(X_train, axis=0)
    X_test = np.concatenate(X_test, axis=0)
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    cPickle.dump([(X_train, y_train), (X_test, y_test)], open(file_name, "wb"))
    return (X_train, y_train), (X_test, y_test)