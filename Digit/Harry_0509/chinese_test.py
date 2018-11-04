#encoding=utf-8
#!/usr/bin/env python
# -*- coding:GBK -*-

import jieba
import jieba.analyse
import jieba.posseg as pseg

test_all=open('result_chinese_Sorted.txt', "r")
result=open('result_chinese.txt','a+')
for line in test_all.readlines():
    #seg_list = jieba.cut(line, cut_all=False)

    txt = line.split(',')[0]
    #Line_txt = (str(line.split(',')[1:])).encode('utf-8')

    #ID= round (int(txt))
    #print ID
    result.write(txt)
    result.write(',')

    #seg_list = pseg.cut(line)
    #for w in seg_list:
    #  print w.word, w.flag

    #w[1].startswith('VB')
    #if w.flag.startswith('n') or w.flag.startswith('v') or w.flag == str('l') or w.flag == str('i')or w.flag == str('t') or w.flag == str('j'):
    #if w.flag == str('n') or w.flag == str('ns') or w.flag == str('vn') or w.flag == str('v'):
    # if w.flag.startswith('n') or w.flag.startswith('v') or w.flag.startswith('eng')
    # result.write(w.word.encode('utf-8')+'+')
    #result.write(w.word.encode('utf-8')+w.flag.encode('utf-8') + '+')
    #result.write('\n')

    seg_list = pseg.cut(line)

    judge =0


    for w in seg_list:
        print w.word, w.flag
        # with n
        if w.flag.startswith('n') or w.flag.startswith('v')or w.flag.startswith('eng'): #or w.flag.startswith('v') or w.flag.startswith('eng'):
            result.write(w.word.encode('utf-8') + '+')
            judge =1
        #result.write(w.word.encode('\n')
           # break
        # with other
        else:
            # with l
            if judge !=1 and w.flag.startswith('l'):
                result.write(w.word.encode('utf-8') + '+')
                judge = 2
                    #break
                #result.write(w.word.encode('\n')
            else:
                if judge !=2 and judge !=1 and w.flag.startswith('a'):
                    result.write(w.word.encode('utf-8') + '+')
                    judge = 3
                else:
                    if judge != 2 and judge != 1 and judge != 3 and w.flag.startswith('i'):
                        result.write(w.word.encode('utf-8') + '+')
                        #judge = 3

    result.write('\n')


#if w.flag == str('l') or w.flag == str('i') and w.flag != str('\An') and w.flag != str('\Av'): #or w.flag != str('ns') or w.flag != str('vn') or w.flag != str('v'):




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