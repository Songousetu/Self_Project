# -*- coding: utf8 -*-
#!/usr/bin/python
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf8')


import time
import datetime

fname = 'C:/Users/u0027623/Desktop/Xiaobao_10.11.xlsx'

#fname = 'C:/Users/u0027623/Desktop/xiaobao_0530.xlsx'
#fname = 'C:/sunaoxue/Qlik/xiaobao_failed/failedAns_2-4yue.xlsx'
#fname = 'C:/sunaoxue/Qlik/xiaobao_failed/failedAns_5yue.xlsx'
#fname = 'C:/sunaoxue/Qlik/xiaobao_failed/failedAns_6yue.xlsx'
#fname = 'C:/sunaoxue/Qlik/xiaobao_failed/failedAns_7yue.xlsx'
# fname = 'C:/sunaoxue/Qlik/xiaobao_failed/failedAns_6-8yue.xlsx'
Chinese_Eng=open('chinese_english.txt','a+')
result_C=open('Chinese.txt','a+')
result_E=open('English.txt','a+')
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print "no sheet in %s named Sheet1" % fname
# 获取行数
nrows = sh.nrows
# 获取列数
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows, ncols)
row_list = []
# 获取各行数据
#print row_data[7]
list_all = []

for i in range(1, nrows):
    row_data = sh.row_values(i)
    row_list.append(row_data)
    contents=str(row_data[1].encode('utf-8'))
    print contents

    def check_contain_chinese(contents):
       for ch in contents.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
            return False
    if __name__ == "__main__":
        print check_contain_chinese(contents)
        if check_contain_chinese(contents)==True:

         result_C.write(str(int(row_data[0])))
         result_C.write(',')
         result_C.write(str(row_data[1].encode('utf-8')))
         result_C.write('\n')
        else:
            #result_E.write(contents.decode('utf-8'))
            result_E.write(str(int(row_data[0])))
            result_E.write(',')
            result_E.write(str(row_data[1].encode('utf-8')))

            result_E.write('\n')





