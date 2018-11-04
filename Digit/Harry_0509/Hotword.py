#encoding=utf-8
#!/usr/bin/env python
# -*- coding:GBK -*-

import jieba
import jieba.analyse
from collections import Counter


santi_text = open('C:\Sunaoxue\IT_Project\Xiaobao/June_item.txt').read()

print (len(santi_text))


santi_text = santi_text.replace('\n', '')  # 删掉换行符
santi_text = santi_text.replace('，', '')  # 删掉逗号
santi_text = santi_text.replace('。', '')  # 删掉句号
santi_text = santi_text.replace('2018', '')

santi_words = [x for x in jieba.cut(santi_text) if len(x) >= 3] #删掉长度小于3的
c = Counter(santi_words).most_common(100)
print (c)