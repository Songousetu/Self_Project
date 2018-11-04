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
    if line.find(u"服务") != -1 or line.find(u"介绍") != -1 or line.find(u"热情") != -1 \
        or line.find(u"接待") != -1 or line.find(u"态度") != -1 or line.find(u"耐心") != -1 \
        or line.find(u"到位") != -1 or line.find(u"邀请") != -1 or line.find(u"周到") != -1 \
        or line.find(u"看车") != -1 or line.find(u"推荐") != -1 or line.find(u"解答") != -1 \
        or line.find(u"流程") != -1 or line.find(u"手续") != -1 or line.find(u"主动") != -1 \
        or line.find(u"办理") != -1 or line.find(u"细致") != -1 or line.find(u"及时") != -1 \
        or line.find(u"清楚") != -1 or line.find(u"咨询") != -1 or line.find(u"细心") != -1 \
        or line.find(u"询问") != -1 or line.find(u"安排") != -1 or line.find(u"沟通") != -1 \
        or line.find(u"随时") != -1 or line.find(u"讲解") != -1 or line.find(u"详细") != -1 \
        or line.find(u"专业") != -1 or line.find(u"好") != -1 or line.find(u"满意") != -1 :
        print ("1")
        result.write("1")
    else:
        print ("0")
        result.write("0")
    result.write('\n')
            # print (line.decode('utf-8'))