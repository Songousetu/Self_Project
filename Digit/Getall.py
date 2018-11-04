# -*- coding: utf-8 -*-

import os

'''
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件
'''

def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                L.append(os.path.join(root, file))
    print (L)
    return L
if __name__ == '__main__':
    file_name("C:\Sunaoxue\IT_Project\warrantysmart\Data\Data_Test\train\train_AB")