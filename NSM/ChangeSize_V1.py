# -*- encoding: utf-8 -*-

from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width=299, height=299):# 想要更改的尺寸
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)

for i in range(1, 10):
    fromPath = 'C:\Sunaoxue\IT_Project/NSM/tuzhuang/'+str(i)+'/*.jpg'
    toPath = 'C:\Sunaoxue\IT_Project/NSM/tuzhuang/train/'+str(i)
    for jpgfile in glob.glob(fromPath): #待处理图片的文件
        convertjpg(jpgfile, toPath)#处理后图片放入的文件夹
