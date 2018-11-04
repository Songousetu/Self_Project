# -*- coding: utf-8 -*-
# coding=utf-8


import jieba
import jieba.analyse
result=open('result_1.txt','a+')
f = open('C:\Sunaoxue\learning/3xi.txt', 'r')  # 要进行分词处理的文本文件 (统统按照utf8文件去处理，省得麻烦)
lines = f.readlines()
for line in lines:

    print(line)
    # result.write(line.encode('utf-8') + ',')
    if line.find(u"交车") != -1 or line.find(u"提车") != -1 :
        print ("1")
        result.write("1")
    else:
        print ("0")
        result.write("0")
    result.write('\n')
            # print (line.decode('utf-8'))