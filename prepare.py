# -*- coding: utf-8 -*-

import os
import random
import shutil
from  shutil import copy2
trainfiles = os.listdir('/root/DD/NSM/All_0530/03_C')
num_train = len(trainfiles)
index_list = range(num_train)
random.shuffle(index_list)
num = 0
trainDir = '/root/DD/NSM/Train_0530/03_C'
validDir = '/root/DD/NSM/Valid_0530/03_C'
testDir = '/root/DD/NSM/Test_0530/03_C'
for i in index_list:
    fileName = os.path.join('/root/DD/NSM/All_0530/03_C', trainfiles[i])
    if num <= num_train*0.7:
        copy2(fileName, trainDir)
    if num < num_train*0.9 and num > num_train*0.7:
        copy2(fileName, validDir)
    else:
        copy2(fileName, testDir)
    num += 1