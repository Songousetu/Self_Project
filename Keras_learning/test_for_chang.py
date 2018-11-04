# -*- coding: utf-8 -*-

from PIL import Image

img = Image.open('2_214.jpg')
(width,height) = img.size
img = img.convert("L")
print (width)

#img = img.resize(32,32)


