#!/usr/bin/env python
# -*- coding:GBK -*-
import xlrd
import time
import datetime

#fname = 'C:/Users/u0027623/Desktop/xiaobao.xlsx'
#fname = 'C:/Users/u0027623/Desktop/xiaobao_sun.xlsx'
test_all=open('C:\Sunaoxue\IT_Project\Xiaobao\Xiao0510.txt', "r")

result_C=open('Chinese.txt','a+')
result_E=open('English.txt','a+')

for line in test_all.readlines():
    #print line[0]
    if line[0].isalpha():
    #if list(line[0]) >= u'\u4e00' and list(line[0])<= u'\u9fa5':
        result_E.write(line)

    else:
        result_C.write(line)

