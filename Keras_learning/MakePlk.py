# -*- coding: utf-8 -*-
############################################################################################
# !/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Author  : zhaoqinghui
# Date    : 2017.1.11
# Function:  1.生成train.Thumbs.db
#           2.生成label.Thumbs.db
#           3.将train.Thumbs.db 和label.Thumbs.db合并成train.pkl
##########################################################################################

import os
import cPickle
import numpy
from PIL import Image

''''' 
############################################################### 
'''
# flag='train'
flag = 'test'
filename = 'test'
outfile = 'gait' + flag + '.pkl'
imgsize = 32
''''' 
################################################################ 
'''


# 获得文件夹下所有图片
def getFilePicture(folder):
    assert os.path.exists(folder)
    assert os.path.isdir(folder)
    PictureList = os.listdir(folder)
    PictureList = [str(folder) + '/' + item for item in PictureList]
    return PictureList


# 转换函数
def writepkltemp(rootDir):
    for lists in os.listdir(rootDir):
        path = rootDir + '/' + lists
        if os.path.isdir(path):
            writepkltemp(path)
        else:
            label = path.split('/', -1)[-2]
            print path, label
            img = Image.open(path)
            img = img.resize((imgsize, imgsize))
            if img.size > 2:
                img = img.convert("1")
            img_ndarray = numpy.asarray(img, dtype='float64')  # /256
            # print img_ndarray.shape
            global vector
            global vector_label
            global num
            # print len(numpy.ndarray.flatten(img_ndarray))
            vector[num] = numpy.ndarray.flatten(img_ndarray)
            vector_label[num] = int(label)
            num = num + 1

            # 保存pkl格式图片集


def writepkl(filename):
    writepkltemp(filename)


# 获得文件夹下所有图片的数量
def getnum(rootDir):
    for lists in os.listdir(rootDir):
        path = rootDir + '/' + lists
        if os.path.isdir(path):
            getnum(path)
        else:
            global n
            n = n + 1

            # 图片总量


def getimgnum(numpath):
    getnum(numpath)


if __name__ == "__main__":
    num = 0
    n = 0
    numpath = filename
    getimgnum(numpath)
    vector = numpy.empty((n, imgsize * imgsize))
    vector_label = numpy.empty(n)
    writepkl(filename)
    vector_label = vector_label.astype(numpy.int)
    write_file = open(outfile, 'wb')
    cPickle.dump([vector[0:n], vector_label[0:n]], write_file, -1)
    write_file.close()