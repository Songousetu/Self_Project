#encoding=utf-8
#!/usr/bin/env python
# -*- coding:GBK -*-

import jieba
import jieba.analyse
import jieba.posseg as pseg
import sys

test_all=open('3xi.txt', "r")
#test_all=open('Chinese.txt', "r")

for line in test_all.readlines():

    seg_list = pseg.cut(line)
    for w in seg_list:

       result.write(w.word.encode('utf-8')+',')
result.write( '\n')




#seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
#print "Full Mode:", "/ ".join(seg_list)# 全模式
#seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
#print "Default Mode:", "/ ".join(seg_list)  # 精确模式
#seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
#print ", ".join(seg_list)

#words = pseg.cut("我爱北京天安门")
#for w in words:
 #print w.word, w.flag