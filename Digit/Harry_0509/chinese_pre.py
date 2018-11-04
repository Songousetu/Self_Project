#encoding=utf-8
#!/usr/bin/env python
# -*- coding:GBK -*-

import jieba
import jieba.analyse
import jieba.posseg as pseg
import sys

test_all=open('Chinese.txt', "r")
#test_all=open('Chinese.txt', "r")
result=open('result_chinese_pre.txt','a+')
Pre_all=open('result_chinese_pre.txt', "r")
result_Sorted=open('result_chinese_Sorted.txt','a+')
for line in test_all.readlines():
    #seg_list = jieba.cut(line, cut_all=False)
    #txt = line.split(',')[0]
    #result.write(txt)
    #result.write(',')

    seg_list = pseg.cut(line)
    for w in seg_list:

       result.write(w.word.encode('utf-8')+',')
result.write( '\n')

#l2 = []
for Pre_line in Pre_all.readlines():
    Number = Pre_line.split(',')[1]
    result_Sorted.write(Number)
    result_Sorted.write(',')

    Pre_txt_1 = Pre_line.split(',')[4:]

    #print Pre_txt_1
    #Pre_a=len(Pre_txt_1)
    #print Pre_a
    Pre_txt=Pre_txt_1[:-1]
    print Pre_txt
    Pre_txt_sort = sorted(Pre_txt)
    #print Pre_txt_sort
    #l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
    Pre_txt_Sorted=list(set(Pre_txt_sort))
    print Pre_txt_Sorted

    for i in Pre_txt_Sorted:

        try:
           i_s=i.decode('utf-8')
         #  result_Sorted.write(i + '，')
        except:
           # print i
            result_Sorted.write(i)
        else:
           print i_s
           result_Sorted.write(i_s.encode('utf-8'))

    result_Sorted.write( '\n')

        #else:
         #  result_Sorted.write(i.decode('utf-8') + '，')
    #result_Sorted.write('\n')
    #print Pre_txt_1
#    Pre_line_T = sorted(Pre_line)
#    l2 = []
#    for i in Pre_line:
#        if not i in l2:
#            l2.append(i)
#    print l2
    #print Pre_line
    #print(Pre_line_T.encode('utf-8'))


      #print "/ ".join(seg_list)

#seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
#print "Full Mode:", "/ ".join(seg_list)# 全模式
#seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
#print "Default Mode:", "/ ".join(seg_list)  # 精确模式
#seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
#print ", ".join(seg_list)

#words = pseg.cut("我爱北京天安门")
#for w in words:
 #print w.word, w.flag