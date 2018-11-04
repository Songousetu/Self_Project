# -*- encoding: utf-8 -*-
from pyecharts import Bar,Line,Overlap
import numpy as np

attr = ['A','B','C','D','E','F']
V1 = [10,20,30,40,50,60]
V2 = [38,28,58,48,78,68]
bar = Bar("Line - Bar")
bar.add("bar",attr,V1)
line = Line()
line.add("line",attr,V2)
v = np.array([1,2,3,4])
x = v[None, :]

print(x)


overlap = Overlap()
overlap.add(bar)
overlap.add(line)

overlap.render()
