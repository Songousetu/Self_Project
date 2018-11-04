#encoding=utf-8
#!/usr/bin/env python
# -*- coding:GBK -*-

#import jieba
#import jieba.analyse
#import jieba.posseg as pseg
#import sys

# test_all=open('3xi.txt', "r")
#test_all=open('Chinese.txt', "r")
import sys
import collections
f = open('C:\Sunaoxue\learning/3xi.txt')
#f = open('C:\Sunaoxue\learning/3xi.txt', 'r', encoding='utf-8') # 打开文件，并读取要处理的大段文字
txt1 = f.read()
txt1 = txt1.replace('\n', '')  # 删掉换行符
txt1 = txt1.replace('，', '')  # 删掉逗号
txt1 = txt1.replace('。', '')  # 删掉句号
mylist = list(txt1)
mycount = collections.Counter(mylist)
for key, val in mycount.most_common(10):  # 有序（返回前10个）
    print(key, val)