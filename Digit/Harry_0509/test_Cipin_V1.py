# -*- coding: utf-8 -*-
# coding=utf-8


import jieba
import jieba.analyse
from collections import Counter
#c = Counter(santi_words).most_common(20)
#print c

# text = "故宫的著名景点包括乾清宫、太和殿和午门等。其中乾清宫非常精美，午门是紫禁城的正门，午门居中向阳。"
text = ''
#jieba.load_userdict("jieba_dict.txt")  # 用户自定义词典 （用户可以自己在这个文本文件中，写好自定制词汇）
f = open('C:\Sunaoxue\learning/3xi.txt', 'r') # 要进行分词处理的文本文件 (统统按照utf8文件去处理，省得麻烦)
lines = f.readlines()
for line in lines:
    text += line

# seg_list = jieba.cut(text, cut_all=False)  #精确模式（默认是精确模式）
seg_list = jieba.cut(text, cut_all=False)  # 精确模式（默认是精确模式）

#for w in seg_list:
#    print (w.encode('utf-8'))
print( "/ ".join(seg_list))

# seg_list2 = jieba.cut(text, cut_all=True)    #全模式
# print("[全模式]: ", "/ ".join(seg_list2))

# seg_list3 = jieba.cut_for_search(text)    #搜索引擎模式
# print("[搜索引擎模式]: ","/ ".join(seg_list3))


tags = jieba.analyse.extract_tags(text, topK=100)
# for T in tags:
#    print (T.encode('utf-8'))
print("关键词:    ", " / ".join(tags))

c = Counter(text).most_common(20)
print (c)